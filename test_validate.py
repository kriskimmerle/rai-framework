#!/usr/bin/env python3
"""
Tests for validate.py
"""

import unittest
import tempfile
import shutil
from pathlib import Path
from validate import (
    find_repo_root,
    check_templates_exist,
    check_template_sections,
    extract_markdown_links,
    check_internal_links,
    check_example_template_references,
    extract_glossary_terms,
    check_glossary_consistency,
    ValidationError
)

class TestValidation(unittest.TestCase):
    """Test validation functions"""
    
    def setUp(self):
        """Create a temporary test repository"""
        self.test_dir = tempfile.mkdtemp()
        self.repo_root = Path(self.test_dir)
        
        # Create basic structure
        (self.repo_root / 'README.md').write_text('# Test Repo')
        (self.repo_root / 'FRAMEWORK.md').write_text('# Framework')
        (self.repo_root / 'templates').mkdir()
        (self.repo_root / 'examples').mkdir()
    
    def tearDown(self):
        """Clean up temporary directory"""
        shutil.rmtree(self.test_dir)
    
    def test_extract_markdown_links(self):
        """Test markdown link extraction"""
        content = """
        Here is a [link](file.md) and [another](https://example.com).
        Also [one with title](file2.md "title").
        """
        links = extract_markdown_links(content)
        self.assertEqual(len(links), 3)
        self.assertIn(('link', 'file.md'), links)
        self.assertIn(('another', 'https://example.com'), links)
        self.assertIn(('one with title', 'file2.md'), links)
    
    def test_check_templates_exist_missing(self):
        """Test detection of missing templates"""
        # Create only one template
        (self.repo_root / 'templates' / 'model-card.md').write_text('# Model Card')
        
        errors = check_templates_exist(self.repo_root)
        self.assertTrue(len(errors) > 0)
        self.assertTrue(any('Missing template' in e for e in errors))
    
    def test_check_templates_exist_all_present(self):
        """Test when all templates are present"""
        # Create all required templates
        from validate import REQUIRED_TEMPLATES
        for template_name in REQUIRED_TEMPLATES:
            (self.repo_root / 'templates' / template_name).write_text(f'# {template_name}')
        
        errors = check_templates_exist(self.repo_root)
        self.assertEqual(len(errors), 0)
    
    def test_check_template_sections_missing(self):
        """Test detection of missing sections in templates"""
        # Create template without required sections
        (self.repo_root / 'templates' / 'model-card.md').write_text('# Model Card\n\nSome content')
        
        errors = check_template_sections(self.repo_root)
        self.assertTrue(len(errors) > 0)
        self.assertTrue(any('Missing required section' in e for e in errors))
    
    def test_check_template_sections_present(self):
        """Test when all required sections are present"""
        content = """
# Model Card

## Overview
Content here

## Model Details
More content

## Intended Use
Usage info

## Performance
Metrics

## Limitations
Known issues
"""
        (self.repo_root / 'templates' / 'model-card.md').write_text(content)
        
        errors = check_template_sections(self.repo_root)
        self.assertEqual(len(errors), 0)
    
    def test_check_internal_links_broken(self):
        """Test detection of broken internal links"""
        content = """
# Test Document

Here is a [broken link](nonexistent.md).
And an [external link](https://example.com) which should be ignored.
"""
        (self.repo_root / 'test.md').write_text(content)
        
        errors = check_internal_links(self.repo_root)
        self.assertTrue(len(errors) > 0)
        self.assertTrue(any('Broken link' in e for e in errors))
    
    def test_check_internal_links_valid(self):
        """Test when all internal links are valid"""
        (self.repo_root / 'target.md').write_text('# Target')
        content = """
# Test Document

Here is a [valid link](target.md).
And an [external link](https://example.com).
"""
        (self.repo_root / 'test.md').write_text(content)
        
        errors = check_internal_links(self.repo_root)
        self.assertEqual(len(errors), 0)
    
    def test_check_glossary_missing(self):
        """Test detection of missing glossary"""
        # Remove GLOSSARY.md
        glossary_path = self.repo_root / 'GLOSSARY.md'
        if glossary_path.exists():
            glossary_path.unlink()
        
        errors = check_glossary_consistency(self.repo_root)
        self.assertTrue(len(errors) > 0)
        self.assertTrue(any('GLOSSARY.md not found' in e for e in errors))
    
    def test_check_glossary_present(self):
        """Test when glossary is present with key terms"""
        content = """
# Glossary

**AI**: Artificial Intelligence

**RAI**: Responsible AI

**Risk Tier**: Classification of system impact

**Impact Assessment**: Process of identifying potential harms

**Stakeholder**: Person or group affected by the system
"""
        (self.repo_root / 'GLOSSARY.md').write_text(content)
        
        errors = check_glossary_consistency(self.repo_root)
        self.assertEqual(len(errors), 0)
    
    def test_extract_glossary_terms(self):
        """Test glossary term extraction"""
        content = """
# Glossary

**Artificial Intelligence**: Definition here

**Machine Learning**: Another definition

### Deep Learning
Third definition
"""
        (self.repo_root / 'GLOSSARY.md').write_text(content)
        
        terms = extract_glossary_terms(self.repo_root)
        self.assertTrue(len(terms) > 0)

class TestExampleReferences(unittest.TestCase):
    """Test example-template reference validation"""
    
    def setUp(self):
        """Create test structure"""
        self.test_dir = tempfile.mkdtemp()
        self.repo_root = Path(self.test_dir)
        
        (self.repo_root / 'README.md').write_text('# Test')
        (self.repo_root / 'FRAMEWORK.md').write_text('# Framework')
        (self.repo_root / 'templates').mkdir()
        (self.repo_root / 'examples').mkdir()
    
    def tearDown(self):
        """Clean up"""
        shutil.rmtree(self.test_dir)
    
    def test_missing_examples(self):
        """Test detection of missing example files"""
        errors = check_example_template_references(self.repo_root)
        self.assertTrue(len(errors) > 0)
        self.assertTrue(any('Missing example' in e for e in errors))

if __name__ == '__main__':
    unittest.main()
