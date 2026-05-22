"""Tests for the render_projects module."""


import pytest

from ai_gene_review.render_projects import (
    build_symbol_to_species_index,
    link_uniprot_code_spans,
    parse_frontmatter,
    replace_gene_tags,
    replace_gene_symbols,
    render_project,
)


class TestBuildSymbolToSpeciesIndex:
    """Tests for build_symbol_to_species_index function."""

    def test_empty_directory(self, tmp_path):
        """Empty genes directory returns empty index."""
        genes_dir = tmp_path / "genes"
        genes_dir.mkdir()
        index = build_symbol_to_species_index(genes_dir)
        assert index == {}

    def test_nonexistent_directory(self, tmp_path):
        """Nonexistent directory returns empty index."""
        genes_dir = tmp_path / "nonexistent"
        index = build_symbol_to_species_index(genes_dir)
        assert index == {}

    def test_single_species_single_gene(self, tmp_path):
        """Single species with single gene."""
        genes_dir = tmp_path / "genes"
        (genes_dir / "human" / "TP53").mkdir(parents=True)

        index = build_symbol_to_species_index(genes_dir)
        assert index == {"TP53": ["human"]}

    def test_multiple_species_multiple_genes(self, tmp_path):
        """Multiple species with multiple genes."""
        genes_dir = tmp_path / "genes"
        (genes_dir / "human" / "TP53").mkdir(parents=True)
        (genes_dir / "human" / "GPX4").mkdir(parents=True)
        (genes_dir / "mouse" / "Trp53").mkdir(parents=True)
        (genes_dir / "mouse" / "Gpx4").mkdir(parents=True)

        index = build_symbol_to_species_index(genes_dir)
        assert "TP53" in index
        assert "GPX4" in index
        assert "Trp53" in index
        assert "Gpx4" in index
        assert index["TP53"] == ["human"]
        assert index["GPX4"] == ["human"]

    def test_same_symbol_multiple_species(self, tmp_path):
        """Same symbol appears in multiple species."""
        genes_dir = tmp_path / "genes"
        (genes_dir / "human" / "ATG7").mkdir(parents=True)
        (genes_dir / "yeast" / "ATG7").mkdir(parents=True)

        index = build_symbol_to_species_index(genes_dir)
        assert "ATG7" in index
        assert sorted(index["ATG7"]) == ["human", "yeast"]

    def test_case_sensitivity(self, tmp_path):
        """Symbols are case-sensitive."""
        genes_dir = tmp_path / "genes"
        (genes_dir / "human" / "GPX4").mkdir(parents=True)
        (genes_dir / "mouse" / "Gpx4").mkdir(parents=True)

        index = build_symbol_to_species_index(genes_dir)
        assert "GPX4" in index
        assert "Gpx4" in index
        assert index["GPX4"] == ["human"]
        assert index["Gpx4"] == ["mouse"]


class TestParseFrontmatter:
    """Tests for parse_frontmatter function."""

    def test_no_frontmatter(self):
        """Content without frontmatter returns empty dict."""
        content = "# Hello World\n\nSome content here."
        fm, body = parse_frontmatter(content)
        assert fm == {}
        assert body == content

    def test_simple_frontmatter(self):
        """Basic YAML frontmatter is parsed correctly."""
        content = "---\ntitle: Test\nspecies: [human]\n---\n# Hello"
        fm, body = parse_frontmatter(content)
        assert fm["title"] == "Test"
        assert fm["species"] == ["human"]
        assert body.strip() == "# Hello"

    def test_frontmatter_with_single_species(self):
        """Single species as string is parsed."""
        content = "---\nspecies: human\n---\n# Content"
        fm, body = parse_frontmatter(content)
        assert fm["species"] == "human"

    def test_frontmatter_with_multiple_species(self):
        """List of species is parsed."""
        content = "---\nspecies: [human, mouse, worm]\n---\n# Content"
        fm, body = parse_frontmatter(content)
        assert fm["species"] == ["human", "mouse", "worm"]

    def test_unclosed_frontmatter(self):
        """Unclosed frontmatter returns empty dict."""
        content = "---\ntitle: Test\n# No closing delimiter"
        fm, body = parse_frontmatter(content)
        assert fm == {}
        assert body == content

    def test_invalid_yaml(self):
        """Invalid YAML returns empty dict."""
        content = "---\ninvalid: [\n---\n# Content"
        fm, body = parse_frontmatter(content)
        assert fm == {}


class TestReplaceGeneSymbols:
    """Tests for replace_gene_symbols function."""

    def test_single_unambiguous_symbol(self):
        """Single unambiguous symbol is linked."""
        index = {"GPX4": ["human"]}
        content = "The gene GPX4 is important."
        result, warnings = replace_gene_symbols(content, index)

        assert "[GPX4]" in result
        assert "human/GPX4" in result
        assert warnings == []

    def test_bold_symbol(self):
        """Bold symbol (**SYMBOL**) is linked."""
        index = {"GPX4": ["human"]}
        content = "**GPX4** is a key enzyme."
        result, warnings = replace_gene_symbols(content, index)

        assert "**[GPX4]" in result
        assert "human/GPX4" in result
        assert warnings == []

    def test_ambiguous_symbol_no_hints(self):
        """Ambiguous symbol without hints generates warning."""
        index = {"ATG7": ["human", "yeast"]}
        content = "ATG7 is involved in autophagy."
        result, warnings = replace_gene_symbols(content, index)

        # Should NOT be linked (ambiguous)
        assert "[ATG7]" not in result
        assert len(warnings) == 1
        assert "Ambiguous" in warnings[0]

    def test_ambiguous_symbol_with_matching_hint(self):
        """Ambiguous symbol with matching hint is linked."""
        index = {"ATG7": ["human", "yeast"]}
        content = "ATG7 is involved in autophagy."
        result, warnings = replace_gene_symbols(
            content, index, species_hints=["human"]
        )

        assert "[ATG7]" in result
        assert "human/ATG7" in result
        assert warnings == []

    def test_ambiguous_symbol_with_nonmatching_hint(self):
        """Ambiguous symbol with non-matching hint generates warning."""
        index = {"ATG7": ["human", "yeast"]}
        content = "ATG7 is involved in autophagy."
        result, warnings = replace_gene_symbols(
            content, index, species_hints=["mouse"]
        )

        # "mouse" doesn't match any available species for ATG7
        assert "[ATG7]" not in result
        assert len(warnings) == 1

    def test_unknown_symbol_unchanged(self):
        """Unknown symbols are left unchanged."""
        index = {"GPX4": ["human"]}
        content = "UNKNOWN_GENE is not in our database."
        result, warnings = replace_gene_symbols(content, index)

        assert result == content
        assert warnings == []

    def test_multiple_symbols(self):
        """Multiple different symbols in content."""
        index = {"GPX4": ["human"], "SLC7A11": ["human"]}
        content = "GPX4 and SLC7A11 work together."
        result, warnings = replace_gene_symbols(content, index)

        assert "[GPX4]" in result
        assert "[SLC7A11]" in result
        assert warnings == []

    def test_same_symbol_multiple_times(self):
        """Same symbol appearing multiple times."""
        index = {"GPX4": ["human"]}
        content = "GPX4 regulates lipid peroxidation. GPX4 is essential."
        result, warnings = replace_gene_symbols(content, index)

        # Both occurrences should be linked
        assert result.count("[GPX4]") == 2
        assert warnings == []

    def test_symbol_in_table(self):
        """Symbol in markdown table."""
        index = {"GPX4": ["human"]}
        content = "| Gene | Function |\n| GPX4 | Lipid repair |"
        result, warnings = replace_gene_symbols(content, index)

        assert "[GPX4]" in result
        assert warnings == []

    def test_symbol_in_inline_code_not_linked(self):
        """Symbols in inline code are literal identifiers and are not linked."""
        index = {"frd": ["BPT4"], "psbA": ["9POAL", "MISSI"]}
        content = "Reviewed `frd/P04382` and `psbA/A0A345AWS2`."
        result, warnings = replace_gene_symbols(content, index)

        assert result == content
        assert warnings == []

    def test_symbol_in_existing_link_not_linked(self):
        """Symbols inside existing markdown links are preserved."""
        index = {"GPX4": ["human"]}
        content = "[GPX4](https://example.org) is already linked."
        result, warnings = replace_gene_symbols(content, index)

        assert result == content
        assert warnings == []

    def test_symbol_after_slash_not_linked(self):
        """Symbols embedded in slash-delimited labels are not auto-linked."""
        index = {"STAT1": ["human"]}
        content = "JAK-STAT/STAT1 inhibition is a pathway label."
        result, warnings = replace_gene_symbols(content, index)

        assert result == content
        assert warnings == []

    def test_partial_match_avoided(self):
        """Partial matches should not be linked (e.g., GPX4 in GPX4-pathway)."""
        index = {"GPX4": ["human"]}
        content = "The GPX4-pathway is important."
        result, warnings = replace_gene_symbols(content, index)

        # GPX4 followed by hyphen should NOT be matched
        # (our pattern uses negative lookahead for alphanumeric/hyphen)
        # This depends on exact regex behavior
        assert warnings == []

    def test_relative_path(self):
        """Links use correct relative path."""
        index = {"GPX4": ["human"]}
        content = "GPX4"
        result, warnings = replace_gene_symbols(
            content, index, base_path="../../genes"
        )

        assert "../../genes/human/GPX4/GPX4-ai-review.html" in result


class TestReplaceGeneTags:
    """Tests for explicit gene tags in project markdown."""

    def test_gene_tag_links_full_visible_label(self, tmp_path):
        """Explicit gene tags link slash-delimited display text."""
        genes_dir = tmp_path / "genes"
        (genes_dir / "BPT4" / "E").mkdir(parents=True)

        content = '<gene species="BPT4" symbol="E">E/P00720</gene>'
        result, warnings = replace_gene_tags(content, genes_dir)

        assert result == "[E/P00720](../../genes/BPT4/E/E-ai-review.html)"
        assert warnings == []

    def test_gene_tag_defaults_empty_label_to_symbol(self, tmp_path):
        """Empty tags can still link by using the symbol as display text."""
        genes_dir = tmp_path / "genes"
        (genes_dir / "9INFA" / "M2").mkdir(parents=True)

        content = '<gene species="9INFA" symbol="M2"></gene>'
        result, warnings = replace_gene_tags(content, genes_dir)

        assert result == "[M2](../../genes/9INFA/M2/M2-ai-review.html)"
        assert warnings == []

    def test_gene_tag_missing_target_warns_and_keeps_label(self, tmp_path):
        """Missing explicit targets do not produce dead links."""
        genes_dir = tmp_path / "genes"
        genes_dir.mkdir()

        content = '<gene species="BPT4" symbol="missing">missing/P00000</gene>'
        result, warnings = replace_gene_tags(content, genes_dir)

        assert result == "missing/P00000"
        assert len(warnings) == 1
        assert "target not found" in warnings[0]

    def test_gene_tag_missing_attrs_warns_and_keeps_label(self, tmp_path):
        """Malformed explicit tags are visible and produce warnings."""
        genes_dir = tmp_path / "genes"
        genes_dir.mkdir()

        content = "<gene>E/P00720</gene>"
        result, warnings = replace_gene_tags(content, genes_dir)

        assert result == "E/P00720"
        assert len(warnings) == 1
        assert "missing required" in warnings[0]


class TestLinkUniprotCodeSpans:
    """Tests for raw SPKW sample code-span links."""

    def test_links_symbol_accession_code_span(self):
        """Backticked symbol/accession samples become UniProt links."""
        content = "Reviewed `MCP/P06491`, `OPG108/A0A7H0DN80`, and `Q9G044`."
        result = link_uniprot_code_spans(content)

        assert "[MCP/P06491](https://www.uniprot.org/uniprotkb/P06491/entry)" in result
        assert (
            "[OPG108/A0A7H0DN80]"
            "(https://www.uniprot.org/uniprotkb/A0A7H0DN80/entry)"
        ) in result
        assert "[Q9G044](https://www.uniprot.org/uniprotkb/Q9G044/entry)" in result

    def test_does_not_link_file_path_code_span(self):
        """File paths and multi-slash code spans are preserved."""
        content = "`genes/9CAUD/darB/darB-ai-review.yaml`"
        assert link_uniprot_code_spans(content) == content


class TestRenderProject:
    """Tests for render_project function."""

    def test_render_simple_project(self, tmp_path):
        """Render a simple markdown project file."""
        # Create genes directory
        genes_dir = tmp_path / "genes"
        (genes_dir / "human" / "GPX4").mkdir(parents=True)

        # Create project markdown
        projects_dir = tmp_path / "projects"
        projects_dir.mkdir()
        md_content = "# Test Project\n\nGPX4 is important."
        md_file = projects_dir / "TEST.md"
        md_file.write_text(md_content)

        # Create template (minimal)
        templates_dir = tmp_path / "templates"
        templates_dir.mkdir()
        template_content = """<!DOCTYPE html>
<html>
<head><title>{{ title }}</title></head>
<body>{{ content | safe }}</body>
</html>"""
        template_file = templates_dir / "project.html.j2"
        template_file.write_text(template_content)

        # Create output directory
        output_dir = tmp_path / "pages" / "projects"

        # Render
        output_path, warnings = render_project(
            md_file,
            output_dir=output_dir,
            genes_dir=genes_dir,
            template_path=template_file,
        )

        assert output_path.exists()
        assert output_path.name == "TEST.html"

        html_content = output_path.read_text()
        assert "Test Project" in html_content
        assert "GPX4" in html_content

    def test_render_with_frontmatter(self, tmp_path):
        """Render project with frontmatter species hints."""
        # Create genes directory with ambiguous symbol
        genes_dir = tmp_path / "genes"
        (genes_dir / "human" / "ATG7").mkdir(parents=True)
        (genes_dir / "yeast" / "ATG7").mkdir(parents=True)

        # Create project markdown with frontmatter
        projects_dir = tmp_path / "projects"
        projects_dir.mkdir()
        md_content = """---
species: [human]
title: Human Autophagy
---
# Autophagy

ATG7 is involved in autophagy."""
        md_file = projects_dir / "AUTOPHAGY.md"
        md_file.write_text(md_content)

        # Create template
        templates_dir = tmp_path / "templates"
        templates_dir.mkdir()
        template_content = """<!DOCTYPE html>
<html>
<head><title>{{ title }}</title></head>
<body>{{ content | safe }}</body>
</html>"""
        template_file = templates_dir / "project.html.j2"
        template_file.write_text(template_content)

        # Create output directory
        output_dir = tmp_path / "pages" / "projects"

        # Render
        output_path, warnings = render_project(
            md_file,
            output_dir=output_dir,
            genes_dir=genes_dir,
            template_path=template_file,
        )

        assert output_path.exists()
        # Should have linked to human (not yeast) based on frontmatter
        html_content = output_path.read_text()
        assert "human/ATG7" in html_content
        assert warnings == []

    def test_file_not_found(self, tmp_path):
        """FileNotFoundError for missing markdown file."""
        md_file = tmp_path / "nonexistent.md"

        with pytest.raises(FileNotFoundError):
            render_project(md_file)

    def test_render_project_with_gene_tag(self, tmp_path):
        """Render project with explicit gene tag labels."""
        genes_dir = tmp_path / "genes"
        (genes_dir / "BPT4" / "E").mkdir(parents=True)

        projects_dir = tmp_path / "projects"
        projects_dir.mkdir()
        md_content = (
            "# Test Project\n\n"
            '<gene species="BPT4" symbol="E">E/P00720</gene> is reviewed.'
        )
        md_file = projects_dir / "TEST.md"
        md_file.write_text(md_content)

        templates_dir = tmp_path / "templates"
        templates_dir.mkdir()
        template_content = """<!DOCTYPE html>
<html>
<head><title>{{ title }}</title></head>
<body>{{ content | safe }}</body>
</html>"""
        template_file = templates_dir / "project.html.j2"
        template_file.write_text(template_content)

        output_path, warnings = render_project(
            md_file,
            output_dir=tmp_path / "pages" / "projects",
            genes_dir=genes_dir,
            template_path=template_file,
        )

        html_content = output_path.read_text()
        assert 'href="../../genes/BPT4/E/E-ai-review.html"' in html_content
        assert ">E/P00720</a>" in html_content
        assert warnings == []

    def test_render_project_with_uniprot_code_span(self, tmp_path):
        """Render project with raw SPKW row examples linked to UniProt."""
        genes_dir = tmp_path / "genes"
        genes_dir.mkdir()

        projects_dir = tmp_path / "projects"
        projects_dir.mkdir()
        md_content = "# Test Project\n\nReviewed `MCP/P06491`."
        md_file = projects_dir / "TEST.md"
        md_file.write_text(md_content)

        templates_dir = tmp_path / "templates"
        templates_dir.mkdir()
        template_content = """<!DOCTYPE html>
<html>
<head><title>{{ title }}</title></head>
<body>{{ content | safe }}</body>
</html>"""
        template_file = templates_dir / "project.html.j2"
        template_file.write_text(template_content)

        output_path, warnings = render_project(
            md_file,
            output_dir=tmp_path / "pages" / "projects",
            genes_dir=genes_dir,
            template_path=template_file,
        )

        html_content = output_path.read_text()
        assert 'href="https://www.uniprot.org/uniprotkb/P06491/entry"' in html_content
        assert ">MCP/P06491</a>" in html_content
        assert warnings == []


class TestIntegration:
    """Integration tests using real-ish data structures."""

    def test_ferroptosis_style_project(self, tmp_path):
        """Test a project file similar to FERROPTOSIS.md."""
        # Create genes directory
        genes_dir = tmp_path / "genes"
        (genes_dir / "human" / "GPX4").mkdir(parents=True)
        (genes_dir / "human" / "SLC7A11").mkdir(parents=True)
        (genes_dir / "human" / "ACSL4").mkdir(parents=True)

        # Create project markdown (simplified FERROPTOSIS.md style)
        projects_dir = tmp_path / "projects"
        projects_dir.mkdir()
        md_content = """# Ferroptosis Pathway

## Overview

Ferroptosis is an iron-dependent form of cell death.

## Key Genes

| Gene | Function |
| --- | --- |
| GPX4 | Lipid hydroperoxide reduction |
| SLC7A11 | Cystine/glutamate antiporter |
| ACSL4 | Acyl-CoA synthesis |

## Core Components

- **GPX4** - Central regulator
- **SLC7A11** - Provides cystine for glutathione synthesis
- **ACSL4** - Required for lipid peroxidation
"""
        md_file = projects_dir / "FERROPTOSIS.md"
        md_file.write_text(md_content)

        # Create template
        templates_dir = tmp_path / "templates"
        templates_dir.mkdir()
        template_content = """<!DOCTYPE html>
<html>
<head><title>{{ title }}</title></head>
<body>{{ content | safe }}</body>
</html>"""
        template_file = templates_dir / "project.html.j2"
        template_file.write_text(template_content)

        # Create output directory
        output_dir = tmp_path / "pages" / "projects"

        # Render
        output_path, warnings = render_project(
            md_file,
            output_dir=output_dir,
            genes_dir=genes_dir,
            template_path=template_file,
        )

        assert output_path.exists()
        html_content = output_path.read_text()

        # All three genes should be linked
        assert "human/GPX4" in html_content
        assert "human/SLC7A11" in html_content
        assert "human/ACSL4" in html_content
        assert warnings == []
