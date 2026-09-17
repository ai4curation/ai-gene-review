"""Rule index coverage and safe rendering."""
from pathlib import Path
import yaml
from ai_gene_review.render_rules import render_rules_index


def test_index_includes_every_review_and_missing_confidence(tmp_path: Path) -> None:
    for identifier in ('ARBA00000001', 'ARBA00000002'):
        folder = tmp_path / identifier
        folder.mkdir()
        (folder / f'{identifier}-review.yaml').write_text(yaml.safe_dump({
            'id': identifier, 'description': 'A < B & C', 'status': 'IN_PROGRESS',
            'rule': {'go_annotations': []},
        }))
    output = render_rules_index(tmp_path)
    html = output.read_text()
    assert '<strong>2</strong> rule reviews' in html
    for identifier in ('ARBA00000001', 'ARBA00000002'):
        assert f'{identifier}/{identifier}-review.html' in html
    assert 'A &lt; B &amp; C' in html
    assert 'IN_PROGRESS' in html
    assert 'Not recorded' in html
    assert '/ai-gene-review/assets/favicon.svg' in html


def test_legacy_condition_count_renders_without_changing_source(tmp_path: Path) -> None:
    from ai_gene_review.etl.rule_analysis import render_rule_review_html

    identifier = 'ARBA00000003'
    folder = tmp_path / identifier
    folder.mkdir()
    source = folder / f'{identifier}-review.yaml'
    content = yaml.safe_dump({'id': identifier, 'rule': {'condition_sets': 17}})
    source.write_text(content)
    page = render_rule_review_html(identifier, tmp_path)
    assert '<div class="stat-value">17</div>' in page.read_text()
    assert source.read_text() == content
    assert '<td>17</td>' in render_rules_index(tmp_path).read_text()
