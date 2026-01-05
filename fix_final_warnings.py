#!/usr/bin/env python3
"""
Fix remaining substring_not_found warnings from validation report.
"""

import re
import os
import csv

def extract_fixes_from_report(report_file):
    """Extract fixes from the validation report."""
    fixes = []

    with open(report_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            if len(row) < 6:
                continue

            file_path = row[0]
            warning_type = row[2]
            error_code = row[3]
            location = row[4]
            message = row[5]
            suggestion = row[6] if len(row) > 6 else ""

            if 'substring_not_found' in error_code:
                # Extract file path and location
                if not os.path.exists(file_path):
                    print(f"File not found: {file_path}")
                    continue

                # Parse different types of warnings
                if "has finding without supporting_text" in message:
                    # This needs manual intervention or deletion
                    print(f"Empty finding in {file_path} at {location} - needs manual fix")
                    continue

                # Extract percentage match suggestions
                match_percent = re.search(r'\((\d+)%\)', suggestion)
                if match_percent:
                    percent = int(match_percent.group(1))
                    if percent >= 80:  # Fix high confidence matches
                        # Extract the suggested text
                        suggested_match = re.search(r'try: "(.*?)"(?:\s*$|")', suggestion)
                        if suggested_match:
                            new_text = suggested_match.group(1)

                            # Extract the old text from message
                            old_match = re.search(r'Query text "(.*?)"', message)
                            if old_match:
                                old_partial = old_match.group(1)

                                fixes.append({
                                    'file': file_path,
                                    'location': location,
                                    'old_text': old_partial,
                                    'new_text': new_text,
                                    'percentage': percent
                                })

    return fixes

def needs_quotes(text):
    """Check if text needs quotes in YAML."""
    special_chars = [':', '{', '}', '[', ']', ',', '&', '*', '#', '?', '|', '-', '<', '>', '=', '!', '%', '@', '`', '"', "'"]
    return any(char in text for char in special_chars)

def apply_fixes(fixes):
    """Apply fixes to the files."""
    files_processed = {}

    for fix in fixes:
        file_path = fix['file']
        if file_path not in files_processed:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            files_processed[file_path] = lines
        else:
            lines = files_processed[file_path]

        old_partial = fix['old_text']
        new_text = fix['new_text']

        # Format the new text with quotes if needed
        if needs_quotes(new_text):
            # Escape quotes in the text
            escaped_text = new_text.replace('"', '\\"')
            formatted_text = f'"{escaped_text}"'
        else:
            formatted_text = new_text

        # Search for the line with the partial match
        found = False
        for i, line in enumerate(lines):
            if 'supporting_text:' in line:
                # Check if this line contains the old text (case insensitive)
                line_content = line.split('supporting_text:')[1].strip().lower()
                # Remove quotes if present
                if line_content.startswith('"') and line_content.endswith('"'):
                    line_content = line_content[1:-1]

                # Check if the old partial text is in this line
                if old_partial.lower()[:50] in line_content or \
                   (old_partial.endswith('...') and old_partial[:-3].lower() in line_content):
                    # Replace the line with the corrected version
                    indent = len(line) - len(line.lstrip())
                    lines[i] = ' ' * indent + f'supporting_text: {formatted_text}\n'
                    found = True
                    print(f"Fixed {file_path} at line {i+1} ({fix['percentage']}% match)")
                    break

        if found:
            files_processed[file_path] = lines

    # Write all modified files
    for file_path, lines in files_processed.items():
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        print(f"Saved {file_path}")

    return len(files_processed)

def main():
    report_file = 'reports/validation-all.tsv'

    if not os.path.exists(report_file):
        print(f"Report file not found: {report_file}")
        return

    print("Extracting fixes from report...")
    fixes = extract_fixes_from_report(report_file)

    print(f"Found {len(fixes)} fixable warnings (80%+ match)")

    if fixes:
        print("\nApplying fixes...")
        num_files = apply_fixes(fixes)
        print(f"\nFixed {len(fixes)} warnings in {num_files} files")
    else:
        print("No high-confidence fixes found")

if __name__ == "__main__":
    main()