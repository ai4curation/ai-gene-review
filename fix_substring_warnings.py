#!/usr/bin/env python3
"""
Auto-fix substring warnings with high confidence matches (>=98%)
"""

import re
import sys
from pathlib import Path

def extract_fix_info(line):
    """Extract file, location, and suggested fix from TSV line"""
    parts = line.strip().split('\t')
    if len(parts) < 7:
        return None

    filepath = parts[0]
    location = parts[4]
    suggestion = parts[6]

    # Extract percentage if present
    percent_match = re.search(r'(\d+)%', suggestion)
    if not percent_match:
        return None

    percentage = int(percent_match.group(1))

    # Extract suggested text
    match = re.search(r'try: "([^"]+)"', suggestion)
    if not match:
        return None

    suggested_text = match.group(1)

    # Parse location like "existing_annotations[4].review.supported_by[0].supporting_text"
    # or "references[10].findings[2].supporting_text"
    return {
        'filepath': filepath,
        'location': location,
        'percentage': percentage,
        'suggested_text': suggested_text
    }

def apply_fix(filepath, location, new_text):
    """Apply a fix to a YAML file"""
    import yaml

    # Read the file
    with open(filepath, 'r') as f:
        data = yaml.safe_load(f)

    # Parse the location path
    parts = location.replace('][', '.').replace('[', '.').replace(']', '').split('.')

    # Navigate to the location
    current = data
    for i, part in enumerate(parts[:-1]):
        if part.isdigit():
            current = current[int(part)]
        else:
            current = current[part]

    # Set the new value
    last_part = parts[-1]
    current[last_part] = new_text

    # Write back
    with open(filepath, 'w') as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, width=1000)

def main():
    # Read validation report
    report_file = '/Users/cjm/repos/ai-gene-review/reports/validation-all.tsv'

    fixes_to_apply = []

    with open(report_file, 'r') as f:
        for line in f:
            if 'substring_not_found' not in line:
                continue

            fix_info = extract_fix_info(line)
            if fix_info and fix_info['percentage'] >= 98:
                fixes_to_apply.append(fix_info)

    print(f"Found {len(fixes_to_apply)} high-confidence fixes (>=98% match)")

    # Group by file
    fixes_by_file = {}
    for fix in fixes_to_apply:
        filepath = fix['filepath']
        if filepath not in fixes_by_file:
            fixes_by_file[filepath] = []
        fixes_by_file[filepath].append(fix)

    print(f"Files to fix: {len(fixes_by_file)}")

    # Apply fixes
    for filepath, file_fixes in fixes_by_file.items():
        print(f"\nFixing {filepath}: {len(file_fixes)} fixes")

        # Read file content
        with open(filepath, 'r') as f:
            content = f.read()

        # For each fix, do a simple string replacement
        # We'll look for the pattern around supporting_text
        for fix in file_fixes:
            # Try to find and replace the supporting_text line
            # This is a simpler approach than parsing YAML

            # First, let's identify what we're looking for
            location_parts = fix['location'].split('.')

            # Create a pattern to find the supporting_text line
            # We'll look for "supporting_text:" followed by the text
            old_pattern = r'(supporting_text:\s*)([^\n]+)'

            # Find all matches and try to identify the right one based on context
            import re

            # For safety, let's be very specific
            # We'll only replace if we can find a unique match

            # Build a more specific pattern based on location
            if 'existing_annotations' in fix['location']:
                # More specific pattern for existing_annotations
                section_pattern = r'existing_annotations:.*?(?=\n(?:references:|proposed_new_terms:|core_functions:|suggested_questions:|suggested_experiments:|status:|$))'
            elif 'references' in fix['location']:
                section_pattern = r'references:.*?(?=\n(?:existing_annotations:|proposed_new_terms:|core_functions:|suggested_questions:|suggested_experiments:|status:|$))'
            else:
                continue

            # Find the section
            section_match = re.search(section_pattern, content, re.DOTALL)
            if not section_match:
                continue

            section_text = section_match.group(0)
            section_start = section_match.start()

            # Within this section, find supporting_text lines
            support_pattern = r'(\s+supporting_text:\s*)([^\n]+?)(?=\n)'

            # Count which occurrence we need
            # Parse the index from location
            indices = re.findall(r'\[(\d+)\]', fix['location'])

            # Find all supporting_text in this section
            matches = list(re.finditer(support_pattern, section_text))

            if matches:
                # Try to identify the right match
                # This is approximate - we'll replace all that are close enough
                for match in matches:
                    old_text = match.group(2)
                    # Clean up old text
                    old_text_clean = old_text.strip().strip('"').strip("'")

                    # Check if this looks like the text we want to replace
                    # Simple heuristic: if the first 20 chars match or last 20 chars match
                    new_text_clean = fix['suggested_text']

                    if (len(old_text_clean) > 15 and len(new_text_clean) > 15 and
                        (old_text_clean[:15].lower() in new_text_clean.lower() or
                         new_text_clean[:15].lower() in old_text_clean.lower() or
                         old_text_clean[-15:].lower() in new_text_clean.lower() or
                         new_text_clean[-15:].lower() in old_text_clean.lower())):

                        # Found a likely match - replace it
                        full_old = match.group(0)
                        full_new = match.group(1) + fix['suggested_text']

                        # Calculate position in full content
                        pos_in_content = section_start + match.start()

                        # Replace in content
                        content = content[:pos_in_content] + full_new + content[pos_in_content + len(full_old):]
                        print(f"  - Fixed: {fix['location'][:50]}...")
                        break

        # Write back
        with open(filepath, 'w') as f:
            f.write(content)

    print("\nDone! Run validation again to check results.")

if __name__ == '__main__':
    main()