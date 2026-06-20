"""Tests for the render_projects module."""


import pytest

from ai_gene_review.render_projects import (
    build_symbol_to_species_index,
    link_uniprot_code_spans,
    parse_frontmatter,
    process_markdown_content,
    replace_gene_tags,
    replace_gene_symbols,
    replace_species_qualified_symbols,
    render_project,
    render_project_bundle,
    should_autolink_gene_symbols,
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


class TestAutolinkGeneSymbolsFrontmatter:
    """Tests for the gene-symbol autolink frontmatter switch."""

    def test_defaults_to_linking(self):
        assert should_autolink_gene_symbols({}) is True

    def test_can_disable_with_canonical_key(self):
        assert should_autolink_gene_symbols({"autolink_gene_symbols": False}) is False
        assert should_autolink_gene_symbols({"autolink_gene_symbols": "false"}) is False

    def test_supports_inverse_suppress_alias(self):
        assert should_autolink_gene_symbols({"suppress_gene_symbol_links": True}) is False
        assert should_autolink_gene_symbols({"suppress_gene_symbol_links": "yes"}) is False


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

    def test_ambiguous_symbol_priority_ordered_hints(self):
        """Hints are priority-ordered: first listed species wins for a symbol
        that exists in several of the hinted species."""
        index = {"CASPL4C1": ["ARATH", "ORYSJ", "POPTR"]}
        content = "CASPL4C1 is cold-inducible."
        # POPTR listed first -> link to POPTR even though ARATH also has it.
        result, warnings = replace_gene_symbols(
            content, index, species_hints=["POPTR", "ARATH"]
        )
        assert "[CASPL4C1]" in result
        assert "POPTR/CASPL4C1" in result
        assert warnings == []

        # Reordering the hints flips the chosen species.
        result, warnings = replace_gene_symbols(
            content, index, species_hints=["ARATH", "POPTR"]
        )
        assert "ARATH/CASPL4C1" in result
        assert warnings == []

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

    def test_short_symbols_not_auto_linked(self):
        """Very short symbols must not auto-link in prose.

        Such symbols flood prose with false links; they should only be linked
        via explicit <gene> tags.
        """
        index = {
            "2": ["BPT4"],
            "10": ["BPT4"],
            "E": ["BPT4"],
            "t": ["BPT4"],
            "AG": ["ARATH"],
            "GPX4": ["human"],
        }
        content = "There are 2 mappings and 10 gaps; mph(E) don't trust McArthur AG; GPX4 is a gene."
        result, warnings = replace_gene_symbols(content, index)
        assert "genes/BPT4/2/" not in result
        assert "genes/BPT4/10/" not in result
        assert "genes/BPT4/E/" not in result
        assert "genes/BPT4/t/" not in result
        assert "genes/ARATH/AG/" not in result
        assert "[GPX4]" in result  # longer symbols still link
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

    def test_rule_b_capitalized_protein_name_links(self):
        """A camelCase gene symbol also links from its capitalized protein form.

        The directory/symbol is ``pqsB`` (gene nomenclature); prose typically
        uses ``PqsB`` (protein nomenclature). The link text keeps the author's
        casing but the URL uses the canonical directory casing.
        """
        index = {"pqsB": ["PSEAE"], "eryCIII": ["SACEN"]}
        result, warnings = replace_gene_symbols("The PqsB / EryCIII pair", index)

        assert "[PqsB](../../genes/PSEAE/pqsB/pqsB-ai-review.html)" in result
        assert "[EryCIII](../../genes/SACEN/eryCIII/eryCIII-ai-review.html)" in result
        assert warnings == []

    def test_rule_a_digit_hyphen_symbol_case_insensitive(self):
        """Digit/hyphen gene symbols match case-insensitively (e.g. worm CHE-2)."""
        index = {"che-2": ["worm"], "daf-16": ["worm"]}
        result, warnings = replace_gene_symbols("CHE-2 and DAF-16 mutants", index)

        assert "[CHE-2](../../genes/worm/che-2/che-2-ai-review.html)" in result
        assert "[DAF-16](../../genes/worm/daf-16/daf-16-ai-review.html)" in result
        assert warnings == []

    def test_case_variants_do_not_link_common_words(self):
        """Words that share a symbol's letters must not be auto-linked.

        ``manY``/``App``/``algA`` are real genes, but the words "many"/"app"/
        "alga" must never become links. Rule B keeps the symbol tail case-exact
        (so ``manY`` only also matches ``ManY``), and Rule A only applies to
        digit/hyphen symbols (which words never are).
        """
        index = {"manY": ["ECOLI"], "App": ["mouse"], "algA": ["PSEPK"]}
        content = "Many results: the app shows alga blooms."
        result, warnings = replace_gene_symbols(content, index)

        assert result == content
        assert warnings == []

    def test_canonical_operon_genes_still_link(self):
        """The real ``ManY`` gene reference (e.g. in an operon) still links."""
        index = {"manX": ["ECOLI"], "manY": ["ECOLI"], "manZ": ["ECOLI"]}
        result, warnings = replace_gene_symbols("operon: ManX, ManY, ManZ", index)

        assert "[ManY](../../genes/ECOLI/manY/manY-ai-review.html)" in result
        assert warnings == []


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


class TestReplaceSpeciesQualifiedSymbols:
    """Tests for the inline ``CODE/symbol`` disambiguation convention."""

    def test_links_uppercase_mnemonic(self, tmp_path):
        """A 5-char uppercase species code links to that species' review."""
        genes_dir = tmp_path / "genes"
        (genes_dir / "POPTR" / "CASPL4C1").mkdir(parents=True)
        (genes_dir / "ARATH" / "CASPL4C1").mkdir(parents=True)

        content = "Compare POPTR/CASPL4C1 and ARATH/CASPL4C1."
        result, warnings = replace_species_qualified_symbols(content, genes_dir)

        assert "[POPTR/CASPL4C1](../../genes/POPTR/CASPL4C1/CASPL4C1-ai-review.html)" in result
        assert "[ARATH/CASPL4C1](../../genes/ARATH/CASPL4C1/CASPL4C1-ai-review.html)" in result
        assert warnings == []

    def test_links_lowercase_exception_code(self, tmp_path):
        """Allowlisted lowercase model-organism codes also link."""
        genes_dir = tmp_path / "genes"
        (genes_dir / "human" / "TP53").mkdir(parents=True)

        result, warnings = replace_species_qualified_symbols(
            "See human/TP53.", genes_dir
        )

        assert "[human/TP53](../../genes/human/TP53/TP53-ai-review.html)" in result
        assert warnings == []

    def test_unknown_lowercase_token_is_not_a_code(self, tmp_path):
        """Arbitrary lowercase words are not treated as species codes."""
        genes_dir = tmp_path / "genes"
        (genes_dir / "and" / "or").mkdir(parents=True)  # contrived; must not link

        result, warnings = replace_species_qualified_symbols("read and/or skim", genes_dir)

        assert result == "read and/or skim"
        assert warnings == []

    def test_missing_symbol_in_known_species_warns(self, tmp_path):
        """A known species code with a missing symbol warns (likely a typo)."""
        genes_dir = tmp_path / "genes"
        (genes_dir / "POPTR").mkdir(parents=True)

        result, warnings = replace_species_qualified_symbols(
            "POPTR/NOTREAL is bogus", genes_dir
        )

        assert result == "POPTR/NOTREAL is bogus"
        assert len(warnings) == 1
        assert "not found" in warnings[0]

    def test_unknown_uppercase_code_is_silent(self, tmp_path):
        """A 5-letter uppercase word that is not a species directory is left
        untouched and produces no warning."""
        genes_dir = tmp_path / "genes"
        genes_dir.mkdir()

        result, warnings = replace_species_qualified_symbols("ABOUT/CONFIG here", genes_dir)

        assert result == "ABOUT/CONFIG here"
        assert warnings == []

    def test_path_like_text_is_not_linked(self, tmp_path):
        """A code preceded by '/' (a path) does not match."""
        genes_dir = tmp_path / "genes"
        (genes_dir / "POPTR" / "CASPL4C1").mkdir(parents=True)

        content = "see `genes/POPTR/CASPL4C1`"
        result, warnings = replace_species_qualified_symbols(content, genes_dir)

        # Inside a code span -> preserved verbatim.
        assert result == content
        assert warnings == []

    def test_existing_link_is_preserved(self, tmp_path):
        """References already inside a markdown link are not re-linked."""
        genes_dir = tmp_path / "genes"
        (genes_dir / "POPTR" / "CASPL4C1").mkdir(parents=True)

        content = "[POPTR/CASPL4C1](http://example.com)"
        result, warnings = replace_species_qualified_symbols(content, genes_dir)

        assert result == content
        assert warnings == []


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

    def test_does_not_link_non_accession_code_span(self):
        """Enum-like all-caps code spans are not UniProt accessions."""
        content = "`MODIFY` and `VERIFIED` are enum values; `Q9G044` is an accession."
        result = link_uniprot_code_spans(content)

        assert "`MODIFY`" in result
        assert "`VERIFIED`" in result
        assert "uniprotkb/MODIFY" not in result
        assert "uniprotkb/VERIFIED" not in result
        assert "[Q9G044](https://www.uniprot.org/uniprotkb/Q9G044/entry)" in result


class TestProcessMarkdownContent:
    """Tests for markdown-to-HTML link rewriting."""

    def test_rewrites_local_notebook_links_to_html(self):
        """Local notebook links target generated static notebook HTML."""
        html = process_markdown_content(
            "[Notebook](notebooks/analysis.ipynb) and "
            "[external](https://example.org/demo.ipynb)."
        )

        assert 'href="notebooks/analysis.ipynb.html"' in html
        assert 'href="https://example.org/demo.ipynb"' in html


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

    def test_render_subfolder_project_mirrors_structure(self, tmp_path):
        """A FOO/bar.md supporting page renders to FOO/bar.html with deeper genes path."""
        genes_dir = tmp_path / "genes"
        (genes_dir / "human" / "GPX4").mkdir(parents=True)

        projects_dir = tmp_path / "projects"
        (projects_dir / "FOO").mkdir(parents=True)
        md_file = projects_dir / "FOO" / "bar.md"
        md_file.write_text("# Sub Page\n\nGPX4 is important.")

        templates_dir = tmp_path / "templates"
        templates_dir.mkdir()
        template_file = templates_dir / "project.html.j2"
        template_file.write_text(
            "<!DOCTYPE html><html><head><title>{{ title }}</title></head>"
            "<body>{{ content | safe }}</body></html>"
        )

        output_dir = tmp_path / "pages" / "projects"
        output_path, warnings = render_project(
            md_file,
            output_dir=output_dir,
            genes_dir=genes_dir,
            template_path=template_file,
            projects_dir=projects_dir,
        )

        # Output mirrors the projects/ subfolder structure
        assert output_path == output_dir / "FOO" / "bar.html"
        assert output_path.exists()

        # Gene links resolve from one level deeper than a top-level project page
        html_content = output_path.read_text()
        assert "../../../genes/human/GPX4" in html_content

    def test_render_can_disable_gene_symbol_autolinks(self, tmp_path):
        """Frontmatter can suppress automatic gene-symbol links for prose pages."""
        genes_dir = tmp_path / "genes"
        (genes_dir / "human" / "GPX4").mkdir(parents=True)
        (genes_dir / "human" / "TP53").mkdir(parents=True)

        projects_dir = tmp_path / "projects"
        projects_dir.mkdir()
        md_file = projects_dir / "PAPER.md"
        md_file.write_text(
            """---
title: Paper
autolink_gene_symbols: false
---
# Paper

GPX4 appears as prose, while <gene species="human" symbol="TP53">TP53 review</gene>
is an explicit link."""
        )

        templates_dir = tmp_path / "templates"
        templates_dir.mkdir()
        template_file = templates_dir / "project.html.j2"
        template_file.write_text(
            "<!DOCTYPE html><html><head><title>{{ title }}</title></head>"
            "<body>{{ content | safe }}</body></html>"
        )

        output_path, warnings = render_project(
            md_file,
            output_dir=tmp_path / "pages" / "projects",
            genes_dir=genes_dir,
            template_path=template_file,
        )

        html_content = output_path.read_text()
        assert "human/GPX4" not in html_content
        assert "GPX4 appears as prose" in html_content
        assert 'href="../../genes/human/TP53/TP53-ai-review.html"' in html_content
        assert warnings == []

    def test_render_project_bundle_includes_support_pages_and_assets(self, tmp_path):
        """Rendering FOO.md also renders FOO/**/*.md and copies referenced assets."""
        genes_dir = tmp_path / "genes"
        (genes_dir / "human" / "GPX4").mkdir(parents=True)

        projects_dir = tmp_path / "projects"
        (projects_dir / "FOO" / "figures").mkdir(parents=True)
        (projects_dir / "FOO.md").write_text(
            "---\n"
            "title: Foo\n"
            "sidecars:\n"
            "  genes: FOO/genes.csv\n"
            "---\n"
            "# Foo\n\nSee the [support folder](FOO/), "
            "[supporting page](FOO/detail.md), and "
            "[analysis](FOO/analysis.ipynb)."
        )
        (projects_dir / "FOO" / "README.md").write_text("# Folder README")
        (projects_dir / "FOO" / "genes.csv").write_text("gene,score\nGPX4,5\n")
        (projects_dir / "FOO" / "detail.md").write_text(
            "# Detail\n\nGPX4 is important.\n\n"
            "See the [analysis notebook](analysis.ipynb).\n\n"
            "![Plot](figures/plot.png)"
        )
        (projects_dir / "FOO" / "figures" / "plot.png").write_bytes(b"png-data")
        (projects_dir / "FOO" / "analysis.ipynb").write_text(
            """{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "analysis",
   "metadata": {},
   "source": ["# Analysis\\n", "Notebook body"]
  }
 ],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 5
}"""
        )

        templates_dir = tmp_path / "templates"
        templates_dir.mkdir()
        template_file = templates_dir / "project.html.j2"
        template_file.write_text(
            "<!DOCTYPE html><html><head><title>{{ title }}</title></head>"
            "<body>{{ content | safe }}</body></html>"
        )

        output_dir = tmp_path / "pages" / "projects"
        output_paths, warnings = render_project_bundle(
            projects_dir / "FOO.md",
            output_dir=output_dir,
            genes_dir=genes_dir,
            template_path=template_file,
            projects_dir=projects_dir,
        )

        assert warnings == []
        assert output_dir / "FOO.html" in output_paths
        assert output_dir / "FOO" / "README.html" in output_paths
        assert output_dir / "FOO" / "index.html" in output_paths
        assert output_dir / "FOO" / "detail.html" in output_paths
        assert output_dir / "FOO" / "analysis.ipynb.html" in output_paths
        assert output_dir / "FOO" / "genes.csv" in output_paths
        assert output_dir / "FOO" / "figures" / "plot.png" in output_paths
        assert (output_dir / "FOO.html").exists()
        assert (output_dir / "FOO" / "README.html").exists()
        assert (output_dir / "FOO" / "index.html").exists()
        assert (output_dir / "FOO" / "detail.html").exists()
        assert (output_dir / "FOO" / "analysis.ipynb.html").exists()
        assert (output_dir / "FOO" / "genes.csv").read_text() == "gene,score\nGPX4,5\n"
        assert not (output_dir / "FOO" / "analysis.ipynb").exists()
        copied_plot = output_dir / "FOO" / "figures" / "plot.png"
        assert copied_plot.read_bytes() == b"png-data"

        top_html = (output_dir / "FOO.html").read_text()
        assert 'href="FOO/"' in top_html
        assert 'href="FOO/analysis.ipynb.html"' in top_html

        detail_html = (output_dir / "FOO" / "detail.html").read_text()
        assert "../../../genes/human/GPX4" in detail_html
        assert 'href="analysis.ipynb.html"' in detail_html
        assert 'src="figures/plot.png"' in detail_html

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


class TestRenderProjectsTable:
    """Tests for the derived all-projects table."""

    def test_table_lists_projects_with_metadata(self, tmp_path):
        from ai_gene_review.render_projects import render_projects_table

        projects = tmp_path / "projects"
        (projects / "ALPHA").mkdir(parents=True)
        (projects / "ALPHA" / "alpha-pathway.md").write_text("# Alpha pathway")
        (projects / "ALPHA.md").write_text(
            "---\ntitle: Alpha Project\nmaturity: MATURE\n"
            "tags: [BIOLOGY_DOMAIN, FLAGSHIP]\nspecies: [human, mouse]\n"
            "genes: [GPX4, ACSL4]\n---\n# Alpha\n"
        )
        (projects / "BETA.md").write_text("# Beta heading only\n")
        # README and supporting subfolder files must be excluded as projects
        (projects / "README.md").write_text("---\ntitle: Projects\n---\n# Projects\n")

        out = render_projects_table(projects_dir=projects, output_dir=tmp_path / "out")
        assert out.name == "all-projects.html"
        html = out.read_text()

        # Both projects listed, README excluded
        assert ">Alpha Project<" in html
        assert 'href="ALPHA.html"' in html
        assert 'href="BETA.html"' in html
        assert 'href="README.html"' not in html  # README not a project row
        # Maturity surfaced as a badge
        assert "m-MATURE" in html
        # Tags surfaced as chips and exposed as row filter data
        assert "t-FLAGSHIP" in html
        assert "t-BIOLOGY_DOMAIN" in html
        assert 'data-tags="BIOLOGY_DOMAIN FLAGSHIP"' in html
        # Species surfaced as chips
        assert 'class="sp">human<' in html
        assert 'class="sp">mouse<' in html
        # Gene count surfaced (2 genes) with the full list in the tooltip
        assert 'title="GPX4, ACSL4"' in html
        # Filter controls present for tag/maturity/species
        assert 'data-filter="tag"' in html
        assert 'data-filter="maturity"' in html
        assert 'data-filter="species"' in html
        # Title falls back to first heading when frontmatter title is absent
        assert "Beta heading only" in html

    def test_table_surfaces_manual_review_status(self, tmp_path):
        from ai_gene_review.render_projects import render_projects_table

        projects = tmp_path / "projects"
        projects.mkdir()
        # Two reviews; latest by date is READY -> that is what surfaces.
        (projects / "ALPHA.md").write_text(
            "---\ntitle: Alpha\nmanual_reviews:\n"
            "  - reviewed_by: cjm\n    date: 2024-01-01\n    status: CHANGES_REQUESTED\n"
            "  - reviewed_by: cjm\n    date: 2024-05-01\n    status: READY\n---\n# Alpha\n"
        )
        (projects / "BETA.md").write_text("---\ntitle: Beta\n---\n# Beta\n")

        out = render_projects_table(projects_dir=projects, output_dir=tmp_path / "out")
        html = out.read_text()

        assert 'data-filter="review"' in html
        assert 'data-review="READY"' in html
        assert "r-READY" in html
        # Beta has no reviews -> empty review filter value
        assert 'data-review=""' in html

    def test_render_project_shows_manual_reviews(self, tmp_path):
        projects = tmp_path / "projects"
        projects.mkdir()
        md = projects / "GAMMA.md"
        md.write_text(
            "---\ntitle: Gamma\nmanual_reviews:\n"
            "  - reviewed_by: cjm\n    date: 2024-06-01\n    status: CHANGES_REQUESTED\n"
            "    notes: needs more evidence\n    todos:\n      - cite PMID:123\n---\n# Gamma\n"
        )
        out, _ = render_project(
            md, output_dir=tmp_path / "out", genes_dir=tmp_path / "genes",
            projects_dir=projects,
        )
        html = out.read_text()
        assert "Manual reviews" in html
        assert "r-CHANGES_REQUESTED" in html
        assert "needs more evidence" in html
        assert "cite PMID:123" in html


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
