"""Source-relative links survive rendering into a different directory."""

from pathlib import Path

from ai_gene_review.publication_links import rewrite_publication_links, protect_scientific_notation, restore_scientific_html_notation
from ai_gene_review.render import rebase_relative_url


def test_project_links_to_repository_files_and_rendered_subpages(tmp_path: Path):
    source = tmp_path / 'projects/FOO.md'
    source.parent.mkdir()
    source.write_text('# FOO')
    review = tmp_path / 'genes/human/ABC/ABC-ai-review.yaml'
    review.parent.mkdir(parents=True)
    review.write_text('gene_symbol: ABC')
    note = source.parent / 'FOO/note.md'
    note.parent.mkdir()
    note.write_text('# Note')
    output = tmp_path / 'pages/projects/FOO.html'
    text = '<a href="../genes/human/ABC/ABC-ai-review.yaml">YAML</a><a href="FOO/note.html#x">Note</a>'
    result = rewrite_publication_links(text, source, output, tmp_path)
    assert 'href="../../genes/human/ABC/ABC-ai-review.yaml"' in result
    assert 'href="FOO/note.html#x"' in result


def test_external_markdown_is_not_changed_to_nonexistent_html(tmp_path: Path):
    source = tmp_path / 'projects/FOO.md'
    source.parent.mkdir()
    source.write_text('# FOO')
    note = tmp_path / 'modules/README.md'
    note.parent.mkdir()
    note.write_text('# Modules')
    text = '<a href="../modules/README.html">Modules</a>'
    assert 'href="../../modules/README.md"' in rewrite_publication_links(
        text, source, tmp_path / 'pages/projects/FOO.html', tmp_path)


def test_known_site_url_gets_prefix_but_external_and_missing_urls_do_not(tmp_path: Path):
    target = tmp_path / 'genes/human/ABC/analysis.tsv'
    target.parent.mkdir(parents=True)
    target.write_text('data')
    source = target.with_name('report.md')
    text = '<a href="/genes/human/ABC/analysis.tsv?q=1&amp;x=2">Data</a><a href="https://example.org/a">Outside</a><a href="missing.pdf">Missing</a>'
    result = rewrite_publication_links(text, source, source.with_suffix('.html'), tmp_path)
    assert 'href="/ai-gene-review/genes/human/ABC/analysis.tsv?q=1&amp;x=2"' in result
    assert 'href="https://example.org/a"' in result
    assert 'href="missing.pdf"' in result
    home = '<a href="https://ai4curation.io/index.html">Organization</a>'
    (tmp_path / 'index.html').write_text('Project home')
    assert rewrite_publication_links(home, source, source.with_suffix('.html'), tmp_path) == home


def test_bioinformatics_parent_segments_are_preserved():
    assert rebase_relative_url('../ABC-notes.md#x', 'ABC-bioinformatics') == 'ABC-notes.md#x'


def test_scientific_notation_does_not_become_a_file_link():
    import markdown

    content = '[4Fe-4S](2+) and [phosphate](n+1) and [Ca(2+)](i); [notes](notes.md)'
    output = markdown.markdown(protect_scientific_notation(content))
    assert '[4Fe-4S](2+)' in output
    assert '[phosphate](n+1)' in output
    assert '[Ca(2+)](i)' in output
    assert '<a href="notes.md">notes</a>' in output


def test_provider_html_math_is_repaired_but_an_existing_file_is_retained(tmp_path: Path):
    page = tmp_path / 'report.html'
    text = '<a href="2+">4Fe-4S</a> and <a href="n">notes</a>'
    (tmp_path / 'n').write_text('An actual extensionless file')
    assert restore_scientific_html_notation(text, page) == '[4Fe-4S](2+) and <a href="n">notes</a>'


def test_scientific_notation_in_code_is_already_literal():
    text = '`[phosphate](n)`\n\n```text\n[phosphate](n)\n```\n\n    [phosphate](n)\n'
    assert protect_scientific_notation(text) == text


def test_base_url_documents_keep_their_declared_resolution(tmp_path: Path):
    source = tmp_path / 'projects/report.md'
    source.parent.mkdir()
    (source.parent / 'data.tsv').write_text('Local file with the same name')
    document = '<base href="https://example.org/"><a href="/projects/data.tsv">External data</a>'
    assert rewrite_publication_links(document, source, tmp_path / 'pages/projects/report.html', tmp_path) == document


def test_relative_link_escaping_site_prefix_is_repaired_to_existing_source(tmp_path: Path):
    source = tmp_path / 'genes/HORSE/ABC/ABC-notes.md'
    source.parent.mkdir(parents=True)
    data = tmp_path / 'projects/benchmark/data.csv'
    data.parent.mkdir(parents=True)
    data.write_text('actual data')
    text = '<a href="../../../../projects/benchmark/data.csv">Data</a>'
    result = rewrite_publication_links(text, source, source.with_suffix('.html'), tmp_path)
    assert 'href="/ai-gene-review/projects/benchmark/data.csv"' in result
