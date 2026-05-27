#!/usr/bin/env python3
"""
Fix all substring warnings from validation report
"""

import re
import csv

# Read the TSV file
report_file = '/Users/cjm/repos/ai-gene-review/reports/validation-all.tsv'

fixes_by_file = {}

with open(report_file, 'r', newline='') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        if len(row) < 8:
            continue

        file_path = row[0]
        level = row[1]
        validator = row[2]
        error_type = row[3]
        location = row[4]
        message = row[5]
        suggestion = row[6]

        if 'substring_not_found' not in error_type:
            continue

        # Extract percentage from suggestion
        percent_match = re.search(r'match[^(]*\((\d+)%\)', suggestion)
        if not percent_match:
            continue

        percentage = int(percent_match.group(1))

        # Only fix high confidence matches
        if percentage < 94:
            continue

        # Extract suggested text
        suggested_match = re.search(r'try: "([^"]*)"', suggestion)
        if not suggested_match:
            continue

        suggested_text = suggested_match.group(1)

        # Extract truncated old text from message
        old_match = re.search(r'Query text "([^"]+)"', message)
        if not old_match:
            continue

        old_text = old_match.group(1)

        if file_path not in fixes_by_file:
            fixes_by_file[file_path] = []

        fixes_by_file[file_path].append({
            'location': location,
            'old_text': old_text,
            'new_text': suggested_text,
            'percentage': percentage
        })

print(f"Found fixes for {len(fixes_by_file)} files")

# Apply fixes
for file_path, fixes in fixes_by_file.items():
    print(f"\nFixing {file_path}: {len(fixes)} changes")

    # Read file
    with open(file_path, 'r') as f:
        lines = f.readlines()

    # Apply each fix
    for fix in fixes:
        old_partial = fix['old_text']
        new_text = fix['new_text']

        # Handle truncated text
        if old_partial.endswith('...'):
            search_text = old_partial[:-3].lower()

            # Find and replace
            for i, line in enumerate(lines):
                if 'supporting_text:' in line and search_text in line.lower():
                    # Get indentation
                    indent = len(line) - len(line.lstrip())
                    # Replace the line
                    lines[i] = ' ' * indent + f'supporting_text: {new_text}\n'
                    print(f"  Fixed {fix['location']} ({fix['percentage']}%)")
                    break
        else:
            # Full text match - try exact replacement
            for i, line in enumerate(lines):
                if 'supporting_text:' in line:
                    # Check if this line contains our text
                    if old_partial in line:
                        # Get indentation
                        indent = len(line) - len(line.lstrip())
                        # Replace the line
                        lines[i] = ' ' * indent + f'supporting_text: {new_text}\n'
                        print(f"  Fixed {fix['location']} ({fix['percentage']}%)")
                        break

    # Write back
    with open(file_path, 'w') as f:
        f.writelines(lines)

print("\nAll fixes applied! Running validation...")