#!/usr/bin/env python3
"""
Hook to automatically validate rule review YAML files after they are written or edited.
This hook runs the rules-validate command and displays the results to provide immediate feedback.

Targets files matching: rules/**/*-review.yaml

**NOTE**

Be sure to exit with code 2 if you want to block the operation.
https://docs.claude.com/en/docs/claude-code/hooks#exit-code-2-behavior
"""

import sys
import json
import subprocess
import os
from pathlib import Path


def main():
    # Read the hook input from stdin
    data = json.load(sys.stdin)

    # Extract the file path from the tool input
    tool_name = data.get("tool_name", "")
    file_path = data.get("tool_input", {}).get("file_path", "")

    # Only process Write and Edit tool calls
    if tool_name not in ["Write", "Edit", "MultiEdit"]:
        sys.exit(0)

    # Check if this is a rule review YAML file in the rules directory
    if not file_path.endswith("-review.yaml"):
        sys.exit(0)

    # Must be in rules/ directory (not genes/)
    if "/rules/" not in file_path and not file_path.startswith("rules/"):
        sys.exit(0)

    # Convert to Path object for easier manipulation
    file_path = Path(file_path)

    # Check if the file exists (it should after Write/Edit)
    if not file_path.exists():
        print(f"Warning: File not found: {file_path}", file=sys.stderr)
        sys.exit(0)

    # Run the validation command
    project_root = os.path.dirname(
        os.path.dirname(os.path.dirname(__file__))
    )

    cmd = ["uv", "run", "ai-gene-review", "rules-validate", str(file_path)]

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        cwd=project_root,
    )

    # Display the validation output
    print("\n" + "=" * 60, file=sys.stderr)
    print(f"Rule Review Validation: {file_path.name}", file=sys.stderr)
    print("=" * 60, file=sys.stderr)

    # Show stdout (the actual validation results)
    if result.stdout:
        # Filter out the uv warning lines and eutils deprecation warnings
        lines = result.stdout.split("\n")
        filtered_lines = []
        for line in lines:
            if "warning: Failed to uninstall package" in line:
                continue
            if "/eutils/__init__.py" in line and "UserWarning" in line:
                continue
            if "pkg_resources is deprecated" in line:
                continue
            if "Uninstalled" in line or "Installed" in line:
                continue
            filtered_lines.append(line)

        output = "\n".join(filtered_lines).strip()
        if output:
            print(output, file=sys.stderr)

    # Show any errors
    if result.returncode != 0 and result.stderr:
        # Filter stderr similarly
        lines = result.stderr.split("\n")
        filtered_lines = []
        for line in lines:
            if "/eutils/__init__.py" not in line:
                filtered_lines.append(line)

        error_output = "\n".join(filtered_lines).strip()
        if error_output:
            print("\nValidation errors:", file=sys.stderr)
            print(error_output, file=sys.stderr)

    print("=" * 60 + "\n", file=sys.stderr)

    # Return exit code 2 to block if validation failed
    if result.returncode != 0:
        print("Validation failed - blocking file modification", file=sys.stderr)
        print("Fix validation errors before saving the file.", file=sys.stderr)
        sys.exit(2)  # Block the operation

    # Exit 0 if validation passed
    sys.exit(0)


if __name__ == "__main__":
    main()
