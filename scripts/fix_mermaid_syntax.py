#!/usr/bin/env python3
"""Fix mermaid syntax to use quotes instead of escaped parentheses."""
import re
import sys
from pathlib import Path


def fix_mermaid_block(code: str) -> str:
    """Fix mermaid syntax in a code block."""
    lines = []
    for line in code.split('\n'):
        # Find node labels with escaped parentheses
        if r'\(' in line or r'\)' in line:
            # Replace [Label \(text\)] with ["Label (text)"]
            # Match pattern: word[content with \( or \)]
            def replace_label(match):
                node_id = match.group(1)
                label = match.group(2)
                # Remove the backslashes
                label = label.replace(r'\(', '(').replace(r'\)', ')')
                # Add quotes if label contains parentheses
                if '(' in label or ')' in label:
                    return f'{node_id}["{label}"]'
                return f'{node_id}[{label}]'

            line = re.sub(r'(\w+)\[([^\]]+)\]', replace_label, line)

        lines.append(line)

    return '\n'.join(lines)


def fix_file(file_path: Path) -> bool:
    """Fix mermaid blocks in a markdown file."""
    try:
        content = file_path.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        content = file_path.read_text(encoding='latin-1')

    # Find and fix all mermaid blocks
    def fix_block(match):
        return f'```mermaid\n{fix_mermaid_block(match.group(1))}\n```'

    new_content = re.sub(r'```mermaid\n(.*?)\n```', fix_block, content, flags=re.DOTALL)

    if new_content != content:
        file_path.write_text(new_content, encoding='utf-8')
        return True
    return False


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python fix_mermaid_syntax.py <file_or_directory>")
        sys.exit(1)

    path = Path(sys.argv[1])

    if path.is_file():
        if fix_file(path):
            print(f"Fixed: {path}")
        else:
            print(f"No changes needed: {path}")
    elif path.is_dir():
        fixed_count = 0
        for md_file in path.rglob("*-pathway.md"):
            if fix_file(md_file):
                print(f"Fixed: {md_file}")
                fixed_count += 1

        print(f"\nFixed {fixed_count} files")
    else:
        print(f"Error: {path} not found")
        sys.exit(1)


if __name__ == "__main__":
    main()