"""Tests for mermaid diagram validation."""
import pytest
from ai_gene_review.tools.validate_mermaid import MermaidValidator, ValidationIssue


class TestMermaidValidator:
    """Test the MermaidValidator class."""

    def test_valid_graph(self):
        """Test validation of a valid graph diagram."""
        code = """graph TD
            A[Node A] --> B[Node B]
            B --> C[Node C]
        """
        validator = MermaidValidator()
        issues = validator.validate(code)
        assert len(issues) == 0

    def test_graph_with_escaped_parentheses(self):
        """Test that escaped parentheses are accepted."""
        code = """graph LR
            A[Test \\(escaped\\)] --> B[Another node]
            C[Also \\(good\\)] --> D[Final node]
        """
        validator = MermaidValidator()
        issues = validator.validate(code)
        assert len(issues) == 0

    def test_graph_with_unescaped_parentheses(self):
        """Test that unescaped parentheses are detected."""
        code = """graph TD
            A[Test (unescaped)] --> B[Another node]
        """
        validator = MermaidValidator()
        issues = validator.validate(code)
        assert len(issues) == 1
        assert issues[0].severity == "error"
        assert "Unescaped parentheses" in issues[0].message

    def test_missing_diagram_type(self):
        """Test detection of missing diagram type."""
        code = """
            A --> B
            B --> C
        """
        validator = MermaidValidator()
        issues = validator.validate(code)
        assert len(issues) == 1
        assert issues[0].severity == "error"
        assert "Missing or invalid diagram type" in issues[0].message

    def test_unbalanced_brackets(self):
        """Test detection of unbalanced brackets."""
        code = """graph TD
            A[Unbalanced bracket --> B
            C[Good] --> D[Also good]
        """
        validator = MermaidValidator()
        issues = validator.validate(code)
        errors = [i for i in issues if i.severity == "error"]
        assert len(errors) >= 1
        assert any("Unbalanced square brackets" in e.message for e in errors)

    def test_valid_sequence_diagram(self):
        """Test validation of a sequence diagram."""
        code = """sequenceDiagram
            participant Alice
            participant Bob
            Alice->>Bob: Hello Bob!
            Bob->>Alice: Hi Alice!
        """
        validator = MermaidValidator()
        issues = validator.validate(code)
        assert len(issues) == 0

    def test_valid_pie_chart(self):
        """Test validation of a pie chart."""
        code = """pie title My Pie Chart
            "Dogs" : 386
            "Cats" : 85
            "Birds" : 15
        """
        validator = MermaidValidator()
        issues = validator.validate(code)
        assert len(issues) == 0

    def test_pie_chart_with_invalid_value(self):
        """Test detection of invalid values in pie chart."""
        code = """pie
            "Dogs" : 386
            "Cats" : not_a_number
        """
        validator = MermaidValidator()
        issues = validator.validate(code)
        errors = [i for i in issues if i.severity == "error"]
        assert len(errors) >= 1
        assert any("Invalid number value" in e.message for e in errors)

    def test_graph_with_edge_labels(self):
        """Test graph with edge labels."""
        code = """graph TD
            A -->|edge label| B
            B -.->|another label| C
        """
        validator = MermaidValidator()
        issues = validator.validate(code)
        assert len(issues) == 0

    def test_graph_with_unbalanced_pipes(self):
        """Test detection of unbalanced pipes in edge labels."""
        code = """graph TD
            A -->|edge label B
            C --> D
        """
        validator = MermaidValidator()
        issues = validator.validate(code)
        errors = [i for i in issues if i.severity == "error"]
        assert len(errors) >= 1
        assert any("Unbalanced pipes" in e.message for e in errors)

    @pytest.mark.parametrize("arrow", [
        "-->", "---", "-.->", "==>", "===",
        "--o", "--x", "o--o", "x--x",
        "<-->", "<-.->", "--|", "-->|"
    ])
    def test_valid_arrow_types(self, arrow):
        """Test that various arrow types are recognized."""
        code = f"""graph TD
            A {arrow} B
        """
        if arrow.endswith('|'):
            code = f"""graph TD
            A {arrow}label| B
        """
        validator = MermaidValidator()
        issues = validator.validate(code)
        # Should have no errors (might have warnings about missing connections)
        errors = [i for i in issues if i.severity == "error"]
        assert len(errors) == 0

    def test_incomplete_arrow(self):
        """Test detection of incomplete arrow syntax."""
        code = """graph TD
            A -- B
            C --> D
        """
        validator = MermaidValidator()
        issues = validator.validate(code)
        errors = [i for i in issues if i.severity == "error"]
        assert any("Incomplete arrow" in e.message for e in errors)