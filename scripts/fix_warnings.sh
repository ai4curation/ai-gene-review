#!/bin/bash

# Extract all high-confidence fixes from validation report
echo "Extracting high-confidence fixes (>=94% match)..."

# Process each warning
grep substring_not_found reports/validation-all.tsv | while IFS=$'\t' read -r file level validator error_type location message suggestion extra timestamp; do
    # Extract percentage
    if [[ $suggestion =~ \(([0-9]+)%\) ]]; then
        percentage="${BASH_REMATCH[1]}"

        # Only process high confidence matches
        if [ "$percentage" -ge 94 ]; then
            # Extract the suggested text
            if [[ $suggestion =~ try:\ \"(.*)\" ]]; then
                new_text="${BASH_REMATCH[1]}"

                # Extract the old text from message (truncated version)
                if [[ $message =~ Query\ text\ \"([^\"]+)\" ]]; then
                    old_text="${BASH_REMATCH[1]}"

                    echo "File: $file"
                    echo "  Location: $location"
                    echo "  Match: $percentage%"
                    echo "  Old (truncated): $old_text"
                    echo "  New: $new_text"

                    # Use a Python one-liner to do the replacement
                    python3 -c "
import sys
filepath = '$file'
old_partial = '''$old_text'''
new_text = '''$new_text'''

with open(filepath, 'r') as f:
    content = f.read()

# Handle truncated text
if old_partial.endswith('...'):
    search = old_partial[:-3]
    # Find lines with supporting_text containing this partial
    lines = content.split('\\n')
    found = False
    for i, line in enumerate(lines):
        if 'supporting_text:' in line and search.lower() in line.lower():
            indent = len(line) - len(line.lstrip())
            lines[i] = ' ' * indent + 'supporting_text: ' + new_text
            found = True
            print(f'    Fixed line {i+1}')
            break
    if found:
        content = '\\n'.join(lines)
else:
    # Try direct replacement
    if f'supporting_text: {old_partial}' in content:
        content = content.replace(f'supporting_text: {old_partial}', f'supporting_text: {new_text}')
        print('    Fixed with direct replacement')

with open(filepath, 'w') as f:
    f.write(content)
"
                    echo ""
                fi
            fi
        fi
    fi
done

echo "Done! Run 'just validate-all' to verify"