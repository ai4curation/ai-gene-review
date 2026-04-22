#!/usr/bin/env python3
"""
Fix ALL remaining substring_not_found warnings from validation report.
This is the final push to get to ZERO warnings.
"""

import re
import os
import csv

def extract_fixes_from_report(report_file):
    """Extract all possible fixes from the validation report."""
    fixes = []
    empty_findings = []

    with open(report_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            if len(row) < 6:
                continue

            file_path = row[0]
            row[2]
            error_code = row[3]
            location = row[4]
            message = row[5]
            suggestion = row[6] if len(row) > 6 else ""

            if 'substring_not_found' in error_code:
                if not os.path.exists(file_path):
                    print(f"File not found: {file_path}")
                    continue

                # Handle empty findings differently
                if "has finding without supporting_text" in message:
                    empty_findings.append({
                        'file': file_path,
                        'location': location
                    })
                    continue

                # Extract percentage match suggestions - be more aggressive
                match_percent = re.search(r'\((\d+)%\)', suggestion)
                if match_percent:
                    percent = int(match_percent.group(1))
                    if percent >= 80:  # Lower threshold to 80%
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

    return fixes, empty_findings

def needs_quotes(text):
    """Check if text needs quotes in YAML."""
    special_chars = [':', '{', '}', '[', ']', ',', '&', '*', '#', '?', '|', '-', '<', '>', '=', '!', '%', '@', '`', '"', "'"]
    # Also quote if starts/ends with spaces or contains newlines
    if text.startswith(' ') or text.endswith(' ') or '\n' in text:
        return True
    return any(char in text for char in special_chars)

def apply_fixes(fixes):
    """Apply fixes to the files."""
    files_processed = {}
    fixes_applied = 0

    for fix in sorted(fixes, key=lambda x: x['percentage'], reverse=True):  # Start with highest confidence
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

                # More aggressive matching
                if old_partial.lower()[:30] in line_content or \
                   (old_partial.endswith('...') and old_partial[:-3].lower() in line_content) or \
                   (len(old_partial) > 20 and old_partial[:20].lower() in line_content):
                    # Replace the line with the corrected version
                    indent = len(line) - len(line.lstrip())
                    lines[i] = ' ' * indent + f'supporting_text: {formatted_text}\n'
                    found = True
                    fixes_applied += 1
                    print(f"Fixed {file_path} at line {i+1} ({fix['percentage']}% match)")
                    break

        if found:
            files_processed[file_path] = lines

    # Write all modified files
    for file_path, lines in files_processed.items():
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        print(f"Saved {file_path}")

    return fixes_applied, len(files_processed)

def main():
    report_file = 'reports/validation-all.tsv'

    if not os.path.exists(report_file):
        print(f"Report file not found: {report_file}")
        return

    print("Extracting fixes from report...")
    fixes, empty_findings = extract_fixes_from_report(report_file)

    print(f"Found {len(fixes)} fixable warnings (80%+ match)")
    print(f"Found {len(empty_findings)} empty findings that need manual fixing")

    if fixes:
        print("\nApplying fixes...")
        num_fixes, num_files = apply_fixes(fixes)
        print(f"\nApplied {num_fixes} fixes in {num_files} files")
    else:
        print("No high-confidence fixes found")

    if empty_findings:
        print(f"\n⚠️  {len(empty_findings)} findings need supporting_text added manually:")
        for ef in empty_findings[:5]:  # Show first 5
            print(f"  - {ef['file']} at {ef['location']}")

if __name__ == "__main__":
    main()