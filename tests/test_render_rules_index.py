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

    from markupsafe import escape

    identifier = 'ARBA00000003'
    folder = tmp_path / identifier
    folder.mkdir()
    review = yaml.safe_dump({'id': identifier, 'rule': {'condition_sets': []}})
    (folder / f'{identifier}-review.yaml').write_text(review)
    page = folder / f'{identifier}-review.html'
    # The preserved page is one that renders the review as it now stands.
    content = f'<h2>{heading}</h2><table><tr><td>Evidence</td></tr></table><pre><code>{escape(review)}</code></pre>'
    page.write_text(content)
    assert render_rule_review_html(identifier, tmp_path) == page
    assert page.read_text() == content


@pytest.mark.parametrize('heading', ['Domain Overlap Analysis Table', 'External Mappings (ipr2go)'])
def test_page_for_an_earlier_review_is_not_preserved(tmp_path: Path, heading: str) -> None:
    """A cached-analysis page showing a withdrawn verdict is re-rendered, not kept."""
    from markupsafe import escape

    from ai_gene_review.etl.rule_analysis import render_rule_review_html

    identifier = 'ARBA00000004'
    folder = tmp_path / identifier
    folder.mkdir()
    earlier = yaml.safe_dump({'id': identifier, 'action': 'DEPRECATE', 'rule': {'condition_sets': []}})
    current = yaml.safe_dump({'id': identifier, 'action': 'ACCEPT', 'rule': {'condition_sets': []}})
    (folder / f'{identifier}-review.yaml').write_text(current)
    page = folder / f'{identifier}-review.html'
    page.write_text(
        f'<h2>{heading}</h2><span class="action-badge action-DEPRECATE">DEPRECATE</span>'
        f'<pre><code>{escape(earlier)}</code></pre>'
    )
    render_rule_review_html(identifier, tmp_path)
    html = page.read_text()
    assert 'action-badge action-ACCEPT' in html
    assert 'action-badge action-DEPRECATE' not in html
    assert 'The domain overlap table is not shown' in html
    assert 'Analysis Summary' not in html


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
