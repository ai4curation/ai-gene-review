#!/usr/bin/env python3
"""
Automatically fix substring warnings from validation report
"""

import re

def process_validation_report(report_path):
    """Process validation report and generate fix commands"""

    fixes = []

    with open(report_path, 'r') as f:
        for line in f:
            if 'substring_not_found' not in line:
                continue

            parts = line.strip().split('\t')
            if len(parts) < 7:
                continue

            filepath = parts[0]
            location = parts[4]
            current_text = parts[5]
            suggestion = parts[6]

            # Extract percentage match
            percent_match = re.search(r'Very close match \((\d+)%\)', suggestion)
            if not percent_match:
                # Also check for "Partial match found"
                percent_match = re.search(r'Partial match found \((\d+)%\)', suggestion)
                if not percent_match:
                    continue

            percentage = int(percent_match.group(1))

            # Extract suggested text
            text_match = re.search(r'try: "([^"]*)"', suggestion)
            if not text_match:
                continue

            suggested_text = text_match.group(1)

            # Extract what text to look for - get it from the message
            old_text_match = re.search(r'Query text "([^"]+)"', current_text)
            if old_text_match:
                old_text = old_text_match.group(1)
            else:
                continue

            fixes.append({
                'file': filepath,
                'location': location,
                'percentage': percentage,
                'old_text': old_text,
                'new_text': suggested_text
            })

    return fixes

def apply_fixes(fixes, min_percentage=98):
    """Apply fixes to files"""

    # Group by file
    by_file = {}
    for fix in fixes:
        if fix['percentage'] >= min_percentage:
            if fix['file'] not in by_file:
                by_file[fix['file']] = []
            by_file[fix['file']].append(fix)

    total_fixes = sum(len(f) for f in by_file.values())
    print(f"Found {total_fixes} fixes with >= {min_percentage}% match in {len(by_file)} files")

    for filepath, file_fixes in by_file.items():
        print(f"\nProcessing {filepath}: {len(file_fixes)} fixes")

        # Read file
        with open(filepath, 'r') as f:
            content = f.read()

        # Apply each fix
        for fix in file_fixes:
            old_text = fix['old_text']
            new_text = fix['new_text']

            # Try to find the old text (it might be truncated with ...)
            if old_text.endswith('...'):
                # Truncated - look for the beginning
                search_text = old_text[:-3]

                # Find lines containing this text
                lines = content.split('\n')
                for i, line in enumerate(lines):
                    if 'supporting_text:' in line and search_text in line.lower():
                        # Found it - replace the whole supporting_text value
                        # Extract current indentation
                        indent = len(line) - len(line.lstrip())
                        new_line = ' ' * indent + f'supporting_text: {new_text}'
                        lines[i] = new_line
                        print(f"  Fixed: {fix['location']}")
                        break

                content = '\n'.join(lines)

            else:
                # Full text - do a simple replacement
                # Look for the pattern: supporting_text: <old_text>
                # Handle different quote styles
                patterns = [
                    f'supporting_text: {old_text}',
                    f'supporting_text: "{old_text}"',
                    f"supporting_text: '{old_text}'",
                    f'supporting_text: {old_text}\n',
                ]

                replaced = False
                for pattern in patterns:
                    if pattern in content:
                        # Simple replacement
                        new_pattern = f'supporting_text: {new_text}'
                        content = content.replace(pattern, new_pattern)
                        print(f"  Fixed: {fix['location']}")
                        replaced = True
                        break

                if not replaced:
                    # Try multiline format
                    # Look for supporting_text: followed by the text on next lines
                    import re
                    pattern = rf'(\s+supporting_text:\s+)([^\n]*{re.escape(old_text[:50])}[^\n]*)'
                    matches = re.finditer(pattern, content, re.IGNORECASE)
                    for match in matches:
                        old_full = match.group(0)
                        new_full = match.group(1) + new_text
                        content = content.replace(old_full, new_full)
                        print(f"  Fixed: {fix['location']}")
                        replaced = True
                        break

        # Write back
        with open(filepath, 'w') as f:
            f.write(content)

    return total_fixes

if __name__ == '__main__':
    report_path = '/Users/cjm/repos/ai-gene-review/reports/validation-all.tsv'

    # First try with 100% matches
    fixes = process_validation_report(report_path)
    count_100 = apply_fixes(fixes, min_percentage=100)

    # Then 99% matches
    count_99 = apply_fixes(fixes, min_percentage=99)

    # Then 98% matches
    count_98 = apply_fixes(fixes, min_percentage=98)

    # Then 97% matches
    count_97 = apply_fixes(fixes, min_percentage=97)

    # Then 96% matches
    count_96 = apply_fixes(fixes, min_percentage=96)

    # Then 94% and up
    count_94 = apply_fixes(fixes, min_percentage=94)

    print(f"\n\nTotal fixes applied: {count_100 + count_99 + count_98 + count_97 + count_96 + count_94}")
    print("Run 'just validate-all' to verify the fixes")