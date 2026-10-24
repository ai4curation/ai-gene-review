"""Rule index coverage and safe rendering."""
from pathlib import Path
import yaml
import pytest
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
    assert '../../assets/favicon.svg' in html



@pytest.mark.parametrize('heading', ['Domain Overlap Analysis Table', 'External Mappings (ipr2go)'])
def test_preserve_analysis_page_without_cache(tmp_path: Path, heading: str) -> None:
    from ai_gene_review.etl.rule_analysis import render_rule_review_html

    identifier = 'ARBA00000003'
    folder = tmp_path / identifier
    folder.mkdir()
    (folder / f'{identifier}-review.yaml').write_text(yaml.safe_dump({
        'id': identifier, 'rule': {'condition_sets': []},
    }))
    page = folder / f'{identifier}-review.html'
    content = f'<h2>{heading}</h2><table><tr><td>Evidence</td></tr></table>'
    page.write_text(content)
    assert render_rule_review_html(identifier, tmp_path) == page
    assert page.read_text() == content


def test_condition_sets_reject_integer(tmp_path: Path) -> None:
    import pytest
    from ai_gene_review.etl.rule_analysis import render_rule_review_html

    identifier = 'ARBA00000004'
    folder = tmp_path / identifier
    folder.mkdir()
    (folder / f'{identifier}-review.yaml').write_text(yaml.safe_dump({
        'id': identifier, 'rule': {'condition_sets': 17},
    }))
    with pytest.raises(TypeError, match='condition_sets must be a list'):
        render_rule_review_html(identifier, tmp_path)


def test_analysis_page_can_refresh_when_caches_exist(tmp_path: Path) -> None:
    from ai_gene_review.etl.rule_analysis import render_rule_review_html

    identifier = 'ARBA00000005'
    folder = tmp_path / identifier
    folder.mkdir()
    (folder / f'{identifier}-review.yaml').write_text(yaml.safe_dump({
        'id': identifier, 'description': 'Updated review',
        'rule': {'condition_sets': []},
    }))
    (folder / f'{identifier}-analysis.json').write_text('{}')
    (folder / f'{identifier}.enriched.json').write_text('{}')
    page = folder / f'{identifier}-review.html'
    page.write_text('<h2>Domain Overlap Analysis Table</h2><h2>External Mappings (ipr2go)</h2>')
    render_rule_review_html(identifier, tmp_path)
    assert 'Updated review' in page.read_text()
    assert 'Recorded condition sets' in page.read_text()
