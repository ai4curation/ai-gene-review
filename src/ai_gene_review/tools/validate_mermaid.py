#!/usr/bin/env python3
"""Validate mermaid syntax in markdown files.

This validator performs comprehensive syntax checking without requiring
mermaid-cli (mmdc) or puppeteer, avoiding npm dependency issues.
"""
import re
import sys
from pathlib import Path
from typing import List, Tuple, Optional
from dataclasses import dataclass
from enum import Enum

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

class DiagramType(Enum):
    """Supported mermaid diagram types."""
    GRAPH = "graph"
    FLOWCHART = "flowchart"
    SEQUENCE = "sequenceDiagram"
    CLASS = "classDiagram"
    STATE = "stateDiagram"
    GANTT = "gantt"
    PIE = "pie"
    ER = "erDiagram"
    JOURNEY = "journey"
    GITGRAPH = "gitGraph"

@dataclass
class ValidationIssue:
    """Represents a validation issue found in mermaid code."""
    line: int
    severity: str  # 'error' or 'warning'
    message: str

    def __str__(self):
        icon = "❌" if self.severity == "error" else "⚠️"
        return f"{icon} Line {self.line}: {self.message}"

class MermaidValidator:
    """Comprehensive mermaid syntax validator."""

    # Valid arrow types for different diagram types
    GRAPH_ARROWS = [
        '-->', '---', '-.->',  # Basic arrows
        '==>', '===',          # Thick arrows
        '--o', '--x',          # Circle/cross endings
        'o--o', 'x--x',        # Double endings
        '<-->', '<-.->',       # Bidirectional
        '--|', '-->|',         # With labels
    ]

    SEQUENCE_KEYWORDS = [
        'participant', 'actor', 'note', 'loop', 'alt', 'else', 'opt',
        'par', 'and', 'rect', 'activate', 'deactivate', 'autonumber'
    ]

    def __init__(self):
        self.issues: List[ValidationIssue] = []
        self.diagram_type: Optional[DiagramType] = None
        self.node_ids: set = set()

    def validate(self, code: str) -> List[ValidationIssue]:
        """Validate mermaid code and return list of issues."""
        self.issues = []
        self.node_ids = set()
        lines = code.split('\n')

        # Detect diagram type
        self.diagram_type = self._detect_diagram_type(code)
        if not self.diagram_type:
            self.issues.append(ValidationIssue(
                line=1,
                severity="error",
                message="Missing or invalid diagram type declaration"
            ))
            return self.issues

        # Validate based on diagram type
        if self.diagram_type in [DiagramType.GRAPH, DiagramType.FLOWCHART]:
            self._validate_graph(lines)
        elif self.diagram_type == DiagramType.SEQUENCE:
            self._validate_sequence(lines)
        elif self.diagram_type == DiagramType.PIE:
            self._validate_pie(lines)
        # Add more diagram type validations as needed

        # Common validations for all types
        self._validate_common_syntax(lines)

        return self.issues

    def _detect_diagram_type(self, code: str) -> Optional[DiagramType]:
        """Detect the diagram type from the code."""
        first_lines = '\n'.join(code.split('\n')[:3]).lower()

        for dtype in DiagramType:
            if dtype.value.lower() in first_lines:
                return dtype
        return None

    def _validate_graph(self, lines: List[str]):
        """Validate graph/flowchart specific syntax."""
        has_direction = False
        has_connections = False

        for i, line in enumerate(lines, 1):
            stripped = line.strip()

            # Check for direction declaration
            if i == 1 and any(d in stripped for d in ['TD', 'TB', 'LR', 'RL', 'BT']):
                has_direction = True

            # Skip empty lines and comments
            if not stripped or stripped.startswith('%%'):
                continue

            # Check for node definitions and connections
            # Check if line has any connection-like syntax
            if any(arrow in line for arrow in self.GRAPH_ARROWS) or '--' in line:
                # Validate the connection syntax
                self._validate_graph_connection(line, i)
                # Also check for node definitions in connection lines
                self._validate_node_definition(line, i)
                # Only count as connection if valid
                if any(arrow in line for arrow in self.GRAPH_ARROWS):
                    has_connections = True
            elif '[' in line or '(' in line or '{' in line or '>' in line:
                self._validate_node_definition(line, i)

        if not has_direction and self.diagram_type == DiagramType.GRAPH:
            self.issues.append(ValidationIssue(
                line=1,
                severity="warning",
                message="Missing direction declaration (TD, LR, etc.)"
            ))

        if not has_connections and len(lines) > 2:
            self.issues.append(ValidationIssue(
                line=1,
                severity="warning",
                message="Graph has no connections between nodes"
            ))

    def _validate_node_definition(self, line: str, line_num: int):
        """Validate node definition syntax."""
        # Extract node ID and label - handle both standalone and in connections
        # Look for all square bracket labels in the line
        for match in re.finditer(r'(\w+)\[([^\]]+)\]', line):
            node_id, label = match.groups()
            self.node_ids.add(node_id)
            self._validate_label(label, line_num, 'square')

        if '(' in line and ')' in line:
            # Round bracket label
            round_match = re.match(r'\s*(\w+)\(([^)]+)\)', line)
            if round_match is not None:
                node_id, label = round_match.groups()
                self.node_ids.add(node_id)
                self._validate_label(label, line_num, 'round')

    def _validate_label(self, label: str, line_num: int, bracket_type: str):
        """Validate node label content."""
        # Check for unescaped parentheses
        if bracket_type == 'square':  # Only check in square brackets
            # Count actual parentheses vs escaped ones
            open_parens = label.count('(')
            close_parens = label.count(')')
            escaped_open = label.count(r'\(')
            escaped_close = label.count(r'\)')

            # If there are unescaped parentheses
            if (open_parens > escaped_open) or (close_parens > escaped_close):
                self.issues.append(ValidationIssue(
                    line=line_num,
                    severity="error",
                    message=f"Unescaped parentheses in node label: '{label[:30]}...' - use \\( and \\)"
                ))

        # Check for unescaped quotes
        quote_count = label.count('"') - label.count('\\"')
        if quote_count % 2 != 0:
            self.issues.append(ValidationIssue(
                line=line_num,
                severity="warning",
                message="Unbalanced quotes in label"
            ))

    def _validate_graph_connection(self, line: str, line_num: int):
        """Validate graph connection syntax."""
        # Check for valid arrow syntax
        has_valid_arrow = any(arrow in line for arrow in self.GRAPH_ARROWS)
        if not has_valid_arrow:
            # Check for incomplete arrows - look for -- followed by space or end of meaningful content
            if re.search(r'--\s+\w', line) or re.search(r'--\s*$', line):
                self.issues.append(ValidationIssue(
                    line=line_num,
                    severity="error",
                    message="Incomplete arrow syntax - use --> or --- for connections"
                ))

        # Check edge labels between pipes
        if '|' in line:
            pipe_count = line.count('|')
            if pipe_count % 2 != 0:
                self.issues.append(ValidationIssue(
                    line=line_num,
                    severity="error",
                    message="Unbalanced pipes for edge label"
                ))
            else:
                # Extract and validate edge label
                match = re.search(r'\|([^|]+)\|', line)
                if match:
                    label = match.group(1)
                    if ('(' in label or ')' in label) and not ('\\(' in label or '\\)' in label):
                        self.issues.append(ValidationIssue(
                            line=line_num,
                            severity="warning",
                            message="Unescaped parentheses in edge label"
                        ))

    def _validate_sequence(self, lines: List[str]):
        """Validate sequence diagram specific syntax."""
        participants = set()

        for i, line in enumerate(lines, 1):
            stripped = line.strip()

            # Skip empty lines and comments
            if not stripped or stripped.startswith('%%'):
                continue

            # Check for sequence diagram keywords
            words = stripped.split()
            if words and words[0] in self.SEQUENCE_KEYWORDS:
                if words[0] in ['participant', 'actor']:
                    if len(words) > 1:
                        participants.add(words[1])

            # Check for message syntax with more lenient validation
            if any(arrow in line for arrow in ['->', '-->', '->>', '-->>', '->>>']):
                # Only warn if it looks like a message without a label
                pass  # Sequence diagrams are valid with or without labels

    def _validate_pie(self, lines: List[str]):
        """Validate pie chart specific syntax."""
        has_data = False

        for i, line in enumerate(lines, 1):
            stripped = line.strip()

            if stripped.startswith('title'):
                pass
            elif ':' in stripped and not stripped.startswith('%%'):
                has_data = True
                # Check for valid number after colon
                parts = stripped.split(':')
                if len(parts) == 2:
                    try:
                        float(parts[1].strip())
                    except ValueError:
                        self.issues.append(ValidationIssue(
                            line=i,
                            severity="error",
                            message=f"Invalid number value: {parts[1].strip()}"
                        ))

        if not has_data:
            self.issues.append(ValidationIssue(
                line=1,
                severity="error",
                message="Pie chart has no data entries"
            ))

    def _validate_common_syntax(self, lines: List[str]):
        """Validate common syntax issues across all diagram types."""
        for i, line in enumerate(lines, 1):
            # Skip empty lines, comments, and style declarations
            if not line.strip() or line.strip().startswith('%%') or line.strip().startswith('style'):
                continue

            # Check for balanced brackets
            if line.count('[') != line.count(']'):
                self.issues.append(ValidationIssue(
                    line=i,
                    severity="error",
                    message="Unbalanced square brackets"
                ))

            if line.count('{') != line.count('}'):
                self.issues.append(ValidationIssue(
                    line=i,
                    severity="error",
                    message="Unbalanced curly braces"
                ))

            if line.count('(') != line.count(')'):
                # Only report if not in a label (where escaping matters)
                if '[' not in line:
                    self.issues.append(ValidationIssue(
                        line=i,
                        severity="warning",
                        message="Unbalanced parentheses"
                    ))

            # Check for common typos
            if 'grpah' in line.lower() or 'diagrma' in line.lower():
                self.issues.append(ValidationIssue(
                    line=i,
                    severity="warning",
                    message="Possible typo detected"
                ))

def validate_mermaid_syntax(code: str) -> List[str]:
    """Legacy function for compatibility - validates mermaid syntax."""
    validator = MermaidValidator()
    issues = validator.validate(code)
    return [str(issue) for issue in issues]

def validate_mermaid_block(code: str) -> Tuple[bool, str]:
    """Validate a single mermaid block using the Python validator."""
    validator = MermaidValidator()
    issues = validator.validate(code)

    if not issues:
        return True, "Valid"

    # Separate errors and warnings
    errors = [i for i in issues if i.severity == "error"]
    warnings = [i for i in issues if i.severity == "warning"]

    if errors:
        # Report first error
        return False, str(errors[0])
    elif warnings:
        # Only warnings, consider valid but report
        return True, f"Valid with warnings: {str(warnings[0])}"
    else:
        return True, "Valid"

def validate_file(file_path: Path) -> bool:
    """Validate all mermaid blocks in a file."""
    blocks = find_mermaid_blocks(file_path)
    
    if not blocks:
        print(f"No mermaid blocks found in {file_path}")
        return True
    
    print(f"\nValidating {len(blocks)} mermaid block(s) in {file_path}:")
    
    errors = 0
    for file_name, line_num, code in blocks:
        is_valid, message = validate_mermaid_block(code)
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

def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python validate_mermaid.py <markdown_file_or_directory>")
        print("\nExamples:")
        print("  python validate_mermaid.py genes/human/JAK1/JAK1-pathway.md")
        print("  python validate_mermaid.py genes/")
        sys.exit(1)
    
    path = Path(sys.argv[1])
    
    if path.is_file():
        # Single file validation
        success = validate_file(path)
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
            if not validate_file(md_file):
                all_valid = False
        
        if all_valid:
            print(f"\n✅ All mermaid blocks in {len(files_with_mermaid)} files are valid!")
            sys.exit(0)
        else:
            print("\n❌ Some mermaid blocks have errors")
            sys.exit(1)
    else:
        print(f"Error: {path} is not a file or directory")
        sys.exit(1)

if __name__ == "__main__":
    main()