"""Publication compaction retains content and the browser data contract."""

import gzip
import json
from pathlib import Path

from lxml import html  # type: ignore[import-untyped]

from ai_gene_review.export.browser_payload import encode_browser_data_js
from ai_gene_review.tools.pages_compaction import compact_browser_data, compact_gene_page


def test_gene_compaction_retains_primary_html_and_exact_panel_content(tmp_path: Path):
    page = tmp_path / "genes/human/ABC/ABC-ai-review.html"
    page.parent.mkdir(parents=True)
    content = '<pre><code>  quoted &lt;gene&gt;\n    spaced YAML\n</code></pre>' * 100
    page.write_text('<!doctype html><html><body><h1>ABC</h1><p>Primary evidence.</p>'
                    '<details><summary>Raw YAML</summary><div class="yaml-content">'
                    + content + '</div></details></body></html>')
    before = page.stat().st_size
    compact_gene_page(tmp_path, page)
    tree = html.fromstring(page.read_text())
    assert tree.xpath('//h1/text()') == ['ABC']
    assert tree.xpath('//p/text()')[0] == 'Primary evidence.'
    target = tree.xpath('//*[@data-pages-content]/@data-pages-content')[0]
    assert gzip.decompress((page.parent / target).read_bytes()).decode() == content
    assert '<summary>Raw YAML</summary>' in page.read_text()
    assert page.stat().st_size < before
    assert tree.xpath('//script/@src')


def test_nested_panels_are_not_duplicated_and_active_content_is_left_alone(tmp_path: Path):
    page = tmp_path / 'page.html'
    nested = '<div class="markdown-content"><p>' + 'Evidence. ' * 200 + '</p></div>'
    active = '<script>window.reportReady=true;</script>' + '<p>Report</p>' * 100
    page.write_text('<html><body><div class="collapse-content">' + nested + '</div>'
                    '<div class="markdown-content">' + active + '</div></body></html>')
    compact_gene_page(tmp_path, page)
    tree = html.fromstring(page.read_text())
    assert len(tree.xpath('//*[@data-pages-content]')) == 1
    assert 'window.reportReady=true' in page.read_text()
    payloads = list((tmp_path / '_pages-content').glob('*.gz'))
    assert len(payloads) == 1
    assert gzip.decompress(payloads[0].read_bytes()).decode() == nested


def test_browser_payload_round_trip_keeps_columns_values_and_ready_event(tmp_path: Path):
    page = tmp_path / 'app/data.js'
    page.parent.mkdir()
    rows = [{"gene_symbol": "λABC", "negated": False, "__proto__": "safe", "tags": ["x"]}] * 100
    page.write_text(encode_browser_data_js(rows))
    compact_browser_data(tmp_path)
    data = json.loads(gzip.decompress((page.parent / 'data.json.gz').read_bytes()))
    decoded = [dict(zip(data['columns'], row)) for row in data['rows']]
    assert decoded == rows
    assert 'searchDataReady' in page.read_text()
    assert 'searchDataError' in page.read_text()
    assert 'eval(' not in page.read_text()


def test_unrecognized_browser_script_is_not_reinterpreted(tmp_path: Path):
    page = tmp_path / 'app/data.js'
    page.parent.mkdir()
    page.write_text('window.otherApp=true;')
    assert compact_browser_data(tmp_path) == 0
    assert page.read_text() == 'window.otherApp=true;'


def test_inline_heading_whitespace_and_raw_text_survive_minification(tmp_path: Path):
    page = tmp_path / 'page.html'
    page.write_text('<html><body><div><h3 style="display:inline">Report</h3>\n  <span>(file.md)</span></div>'
                    '<pre>  literal\n    indentation</pre></body></html>')
    compact_gene_page(tmp_path, page)
    tree = html.fromstring(page.read_text())
    assert tree.xpath('//h3')[0].tail == ' '
    assert tree.xpath('//pre/text()') == ['  literal\n    indentation']


def test_loader_is_only_inserted_at_the_document_body_end(tmp_path: Path):
    page = tmp_path / 'page.html'
    original_script = '<script>const example="</body>";</script>'
    page.write_text('<html><body>' + original_script + '<div class="yaml-content">' + 'Review. ' * 200 + '</div></body></html>')
    compact_gene_page(tmp_path, page)
    tree = html.fromstring(page.read_text())
    assert tree.xpath('//script[not(@src)]/text()') == ['const example="</body>";']
    assert len(tree.xpath('//script[@src]')) == 1
