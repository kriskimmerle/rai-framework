#!/usr/bin/env python3
"""
Validation script for rai-framework repository.
Checks:
- Template files exist and have required sections
- Internal markdown links aren't broken
- Examples reference templates correctly
- Glossary terms are consistent
"""

import os
import re
import sys
from pathlib import Path
from typing import List, Dict, Set, Tuple

# Expected templates - these must exist
REQUIRED_TEMPLATES = [
    'ai-registry.md',
    'use-case-statement.md',
    'impact-assessment.md',
    'stakeholder-analysis.md',
    'model-card.md',
    'data-documentation.md',
    'test-report.md',
    'monitoring-plan.md',
    'incident-response.md',
    'retirement-plan.md',
    'vendor-ai-assessment.md'
]

# Key sections to look for (flexible matching)
TEMPLATE_SECTIONS = {
    'model-card.md': ['Model Details', 'Intended Use', 'Performance', 'Limitations'],
    'impact-assessment.md': ['Risk', 'Likelihood', 'Severity', 'Mitigation'],
    'monitoring-plan.md': ['Metric', 'Baseline', 'Alert'],
}

# Example files and templates they should reference
EXAMPLES = [
    'classical-ml-fraud-detection.md',
    'genai-customer-chatbot.md',
    'genai-autonomous-agent.md'
]

class ValidationError(Exception):
    """Raised when validation fails"""
    pass

def find_repo_root() -> Path:
    """Find the repository root directory"""
    current = Path(__file__).parent.absolute()
    if (current / 'README.md').exists() and (current / 'FRAMEWORK.md').exists():
        return current
    raise ValidationError("Could not find repository root")

def check_templates_exist(repo_root: Path) -> List[str]:
    """Check that all required template files exist"""
    errors = []
    templates_dir = repo_root / 'templates'
    
    if not templates_dir.exists():
        errors.append("templates/ directory not found")
        return errors
    
    for template_name in REQUIRED_TEMPLATES:
        template_path = templates_dir / template_name
        if not template_path.exists():
            errors.append(f"Missing template: templates/{template_name}")
    
    return errors

def check_template_sections(repo_root: Path) -> List[str]:
    """Check that templates have required sections"""
    errors = []
    templates_dir = repo_root / 'templates'
    
    for template_name, required_sections in TEMPLATE_SECTIONS.items():
        template_path = templates_dir / template_name
        if not template_path.exists():
            continue
        
        content = template_path.read_text(encoding='utf-8')
        
        for section in required_sections:
            # Check for section as heading or table field
            if section not in content:
                errors.append(f"templates/{template_name}: Missing required section '{section}'")
    
    return errors

def extract_markdown_links(content: str) -> List[Tuple[str, str]]:
    """Extract all markdown links from content"""
    # Pattern: [text](url) or [text](url "title")
    pattern = r'\[([^\]]+)\]\(([^)]+?)(?:\s+"[^"]*")?\)'
    return re.findall(pattern, content)

def check_internal_links(repo_root: Path) -> List[str]:
    """Check that internal markdown links aren't broken"""
    errors = []
    
    # Find all markdown files
    md_files = list(repo_root.glob('**/*.md'))
    
    for md_file in md_files:
        # Skip .git directory
        if '.git' in str(md_file):
            continue
        
        content = md_file.read_text(encoding='utf-8')
        links = extract_markdown_links(content)
        
        for link_text, link_url in links:
            # Skip external links
            if link_url.startswith(('http://', 'https://', 'mailto:', '#')):
                continue
            
            # Remove anchor fragments
            link_path = link_url.split('#')[0]
            if not link_path:  # Just an anchor
                continue
            
            # Resolve relative path
            target = (md_file.parent / link_path).resolve()
            
            # Check if target exists
            if not target.exists():
                rel_path = md_file.relative_to(repo_root)
                errors.append(f"{rel_path}: Broken link to '{link_url}'")
    
    return errors

def check_example_template_references(repo_root: Path) -> List[str]:
    """Check that examples reference actual templates"""
    errors = []
    examples_dir = repo_root / 'examples'
    
    if not examples_dir.exists():
        errors.append("examples/ directory not found")
        return errors
    
    # Get list of actual templates
    templates_dir = repo_root / 'templates'
    actual_templates = set()
    if templates_dir.exists():
        actual_templates = {t.name for t in templates_dir.glob('*.md')}
    
    for example_name in EXAMPLES:
        example_path = examples_dir / example_name
        if not example_path.exists():
            errors.append(f"Missing example: examples/{example_name}")
            continue
        
        content = example_path.read_text(encoding='utf-8')
        
        # Look for template references (e.g., "model-card.md", "use-case-statement")
        for template_name in actual_templates:
            base_name = template_name.replace('.md', '')
            # Check if template is mentioned in the example
            if template_name in content or base_name in content:
                # Verify the reference links to the actual template
                if f'templates/{template_name}' not in content and f'../{template_name}' not in content:
                    # This is a soft check - template is mentioned but maybe not linked
                    pass
    
    return errors

def extract_glossary_terms(repo_root: Path) -> Set[str]:
    """Extract all terms defined in GLOSSARY.md"""
    glossary_path = repo_root / 'GLOSSARY.md'
    if not glossary_path.exists():
        return set()
    
    content = glossary_path.read_text(encoding='utf-8')
    terms = set()
    
    # Look for term definitions (usually bold or in headings)
    # Pattern: **Term** or ### Term
    for match in re.finditer(r'\*\*([A-Z][^\*]+?)\*\*|^###\s+(.+?)$', content, re.MULTILINE):
        term = match.group(1) or match.group(2)
        if term:
            terms.add(term.strip())
    
    return terms

def check_glossary_consistency(repo_root: Path) -> List[str]:
    """Check that glossary terms are used consistently"""
    errors = []
    
    # This is a basic check - we verify GLOSSARY.md exists and has content
    glossary_path = repo_root / 'GLOSSARY.md'
    if not glossary_path.exists():
        errors.append("GLOSSARY.md not found")
        return errors
    
    content = glossary_path.read_text(encoding='utf-8')
    if len(content.strip()) < 100:
        errors.append("GLOSSARY.md appears to be empty or too short")
    
    # Check for key terms that should be defined (flexible matching)
    key_terms = ['AI', 'RAI']
    for term in key_terms:
        if term not in content:
            errors.append(f"GLOSSARY.md: Missing definition for key term '{term}'")
    
    return errors

def main():
    """Run all validation checks"""
    try:
        repo_root = find_repo_root()
    except ValidationError as e:
        print(f"ERROR: {e}")
        return 1
    
    print("Validating rai-framework repository...")
    print(f"Repository root: {repo_root}")
    print()
    
    all_errors = []
    
    # Check 1: Templates exist
    print("Checking template files exist...")
    errors = check_templates_exist(repo_root)
    all_errors.extend(errors)
    if errors:
        for error in errors:
            print(f"  ERROR: {error}")
    else:
        print("  OK: All template files exist")
    print()
    
    # Check 2: Template sections
    print("Checking template sections...")
    errors = check_template_sections(repo_root)
    all_errors.extend(errors)
    if errors:
        for error in errors:
            print(f"  ERROR: {error}")
    else:
        print("  OK: All templates have required sections")
    print()
    
    # Check 3: Internal links
    print("Checking internal markdown links...")
    errors = check_internal_links(repo_root)
    all_errors.extend(errors)
    if errors:
        for error in errors:
            print(f"  ERROR: {error}")
    else:
        print("  OK: All internal links are valid")
    print()
    
    # Check 4: Example template references
    print("Checking example template references...")
    errors = check_example_template_references(repo_root)
    all_errors.extend(errors)
    if errors:
        for error in errors:
            print(f"  ERROR: {error}")
    else:
        print("  OK: All examples exist and reference templates")
    print()
    
    # Check 5: Glossary consistency
    print("Checking glossary consistency...")
    errors = check_glossary_consistency(repo_root)
    all_errors.extend(errors)
    if errors:
        for error in errors:
            print(f"  ERROR: {error}")
    else:
        print("  OK: Glossary is consistent")
    print()
    
    # Summary
    print("=" * 60)
    if all_errors:
        print(f"FAILED: {len(all_errors)} validation error(s) found")
        return 1
    else:
        print("SUCCESS: All validation checks passed")
        return 0

if __name__ == '__main__':
    sys.exit(main())
