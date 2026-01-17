#!/usr/bin/env python3
"""Validate mermaid syntax using the official mmdc CLI tool.

This validator uses the official mermaid-cli (mmdc) parser for accurate validation.
Requires @mermaid-js/mermaid-cli to be installed via npm.
"""
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import List, Tuple, Optional


def find_mermaid_blocks(file_path: Path) -> List[Tuple[str, int, str]]:
    """Find all mermaid blocks in a markdown file."""
    try:
        content = file_path.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        # Try with latin-1 as fallback
        content = file_path.read_text(encoding='latin-1')

    blocks = []
    for match in re.finditer(r'```mermaid\n(.*?)\n```', content, re.DOTALL):
        line_num = content[:match.start()].count('\n') + 1
        blocks.append((str(file_path), line_num, match.group(1)))

    return blocks


def get_puppeteer_config() -> Optional[Path]:
    """Get the puppeteer configuration file path."""
    config_path = Path(__file__).parent.parent.parent.parent / "config" / "puppeteer-config.json"
    if config_path.exists():
        return config_path
    return None


def validate_with_mmdc(code: str, puppeteer_config: Optional[Path] = None) -> Tuple[bool, str]:
    """Validate mermaid code using the official mmdc CLI tool.

    Args:
        code: The mermaid diagram code to validate
        puppeteer_config: Optional path to puppeteer configuration

    Returns:
        Tuple of (is_valid, message)
    """
    # Create temporary files for input and output
    with tempfile.NamedTemporaryFile(mode='w', suffix='.mmd', delete=False) as f:
        f.write(code)
        input_file = Path(f.name)

    output_file = input_file.with_suffix('.svg')

    try:
        # Build mmdc command
        cmd = ['mmdc', '-i', str(input_file), '-o', str(output_file)]

        # Add puppeteer config if available
        if puppeteer_config and puppeteer_config.exists():
            cmd.extend(['-p', str(puppeteer_config)])

        # Run mmdc
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=10  # 10 second timeout
        )

        # Check if successful
        if result.returncode == 0:
            return True, "Valid"
        else:
            # Parse error from stderr
            error_msg = result.stderr.strip()

            # Try to extract the most relevant error line
            error_lines = error_msg.split('\n')
            for line in error_lines:
                if 'error' in line.lower() and 'spawn' not in line.lower():
                    return False, line
                if 'parse' in line.lower() or 'syntax' in line.lower():
                    return False, line

            # If no clear error message, return the first non-empty line
            for line in error_lines:
                if line.strip() and not line.startswith('Generating'):
                    return False, line

            return False, "Invalid syntax (mmdc validation failed)"

    except subprocess.TimeoutExpired:
        return False, "Validation timeout"
    except FileNotFoundError:
        return False, "mmdc not found - install with: npm install -g @mermaid-js/mermaid-cli"
    except Exception as e:
        return False, f"Validation error: {str(e)}"
    finally:
        # Clean up temporary files
        if input_file.exists():
            input_file.unlink()
        if output_file.exists():
            output_file.unlink()


def validate_file(file_path: Path, puppeteer_config: Optional[Path] = None) -> bool:
    """Validate all mermaid blocks in a file using mmdc."""
    blocks = find_mermaid_blocks(file_path)

    if not blocks:
        print(f"No mermaid blocks found in {file_path}")
        return True

    print(f"\nValidating {len(blocks)} mermaid block(s) in {file_path}:")

    errors = 0
    for file_name, line_num, code in blocks:
        is_valid, message = validate_with_mmdc(code, puppeteer_config)
        if is_valid:
            print(f"  ✅ Line {line_num}: {message}")
        else:
            print(f"  ❌ Line {line_num}: {message}")
            errors += 1

    if errors:
        print(f"  Summary: {errors}/{len(blocks)} blocks have errors")
        return False
    else:
        print("  Summary: All blocks valid!")
        return True


def check_mmdc_installation() -> bool:
    """Check if mmdc is installed and working."""
    try:
        result = subprocess.run(['mmdc', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Using mmdc version: {result.stdout.strip()}")
            return True
    except FileNotFoundError:
        pass

    print("ERROR: mmdc (mermaid-cli) is not installed or not in PATH")
    print("Install it with: npm install -g @mermaid-js/mermaid-cli")
    return False


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python validate_mermaid_mmdc.py <markdown_file_or_directory>")
        print("\nExamples:")
        print("  python validate_mermaid_mmdc.py genes/human/JAK1/JAK1-pathway.md")
        print("  python validate_mermaid_mmdc.py genes/")
        sys.exit(1)

    # Check mmdc installation
    if not check_mmdc_installation():
        sys.exit(1)

    # Get puppeteer config if available
    puppeteer_config = get_puppeteer_config()
    if puppeteer_config:
        print(f"Using puppeteer config: {puppeteer_config}")

    path = Path(sys.argv[1])

    if path.is_file():
        # Single file validation
        success = validate_file(path, puppeteer_config)
        sys.exit(0 if success else 1)
    elif path.is_dir():
        # Directory validation - find all .md files
        md_files = list(path.rglob("*.md"))
        files_with_mermaid = []

        for md_file in md_files:
            try:
                content = md_file.read_text(encoding='utf-8')
            except UnicodeDecodeError:
                content = md_file.read_text(encoding='latin-1')
            if '```mermaid' in content:
                files_with_mermaid.append(md_file)

        if not files_with_mermaid:
            print(f"No markdown files with mermaid blocks found in {path}")
            sys.exit(0)

        print(f"Found {len(files_with_mermaid)} file(s) with mermaid blocks")

        all_valid = True
        for md_file in files_with_mermaid:
            if not validate_file(md_file, puppeteer_config):
                all_valid = False

        if all_valid:
            print(f"\n✅ All mermaid blocks in {len(files_with_mermaid)} files are valid!")
            sys.exit(0)
        else:
            print("\n❌ Some mermaid blocks have validation errors")
            sys.exit(1)
    else:
        print(f"Error: {path} is not a file or directory")
        sys.exit(1)


if __name__ == "__main__":
    main()