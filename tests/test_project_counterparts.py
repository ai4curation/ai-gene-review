"""Project cohort changes and YAML edits must flow into the generated reports."""

import csv
import io
from pathlib import Path

import pytest
import yaml

from ai_gene_review.analysis.project_counterparts import (
    collect_assessments,
    main,
    render_csv,
    render_markdown,
)


def write_review(root, species, gene, **fields):
    path = root / 'genes' / species / gene / f'{gene}-ai-review.yaml'
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump({'id': 'P12345', **fields}))
    return path


def write_project(root, genes):
    path = root / 'projects' / 'EXAMPLE.md'
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text('---\n' + yaml.safe_dump({'genes': genes}) + '---\n# Example\n')
    return path


def test_frontmatter_controls_cohort_and_all_assessments_are_retained(tmp_path):
    alternative = {
        'id': 'Q12345', 'relationship': 'REFERENCE_PROTEOME_CANDIDATE',
        'reference_proteome': 'UP000000001', 'reviewed_on': '2026-10-18',
        'reason': 'Unresolved | locus\nNeeds mapping.',
    }
    write_review(tmp_path, 'one', 'shared', alternative_records=[alternative, {
        **alternative, 'id': 'Q54321', 'relationship': 'REFERENCE_PROTEOME_LOCUS_COUNTERPART',
    }])
    write_review(tmp_path, 'two', 'shared')
    write_review(tmp_path, 'one', 'negative', reference_proteome_assessments=[{
        'status': 'NO_SUPPORTED_COUNTERPART',
        'reference_proteomes': ['UP000000001', 'UP000000002'],
        'reason': 'No supported hit.',
    }])
    write_review(tmp_path, 'one', 'excluded')
    project = write_project(tmp_path, ['one/shared', 'two/shared', 'one/negative', 'one/shared'])
    rows = collect_assessments(project, tmp_path)
    assert len(rows) == 4
    assert [r['status'] for r in rows] == [
        'CANDIDATE', 'LOCUS_COUNTERPART', 'NOT_ASSESSED', 'NO_SUPPORTED_COUNTERPART',
    ]
    assert rows[-1]['reference_proteomes'] == 'UP000000001;UP000000002'
    markdown = render_markdown(rows, project, tmp_path, tmp_path / 'report.md')
    assert '3 gene reviews across 2 species directories; 4 assessment rows' in markdown
    assert 'Unresolved &#124; locus Needs mapping.' in markdown
    assert 'genes/one/shared/shared-ai-review.yaml' in markdown
    assert 'excluded' not in markdown
    assert list(csv.DictReader(io.StringIO(render_csv(rows))))[0]['reason'] == alternative['reason']
    project = write_project(tmp_path, ['two/shared'])
    assert len(collect_assessments(project, tmp_path)) == 1


def test_missing_or_ambiguous_frontmatter_genes_fail(tmp_path):
    write_review(tmp_path, 'one', 'shared')
    write_review(tmp_path, 'two', 'shared')
    for genes in [['shared'], ['one/missing'], []]:
        with pytest.raises(ValueError):
            collect_assessments(write_project(tmp_path, genes), tmp_path)


def test_check_detects_yaml_change_and_evidence_links_follow_output_location(tmp_path, monkeypatch):
    source = tmp_path / 'genes' / 'one' / 'shared' / 'evidence.yaml'
    alternative = {
        'id': 'Q12345', 'relationship': 'REFERENCE_PROTEOME_CANDIDATE', 'reason': 'Original',
        'evidence': [{'type': 'CURATION_CONTEXT', 'description': 'Observed context',
                      'supported_by': [{'reference_id': 'file:one/shared/evidence.yaml'}]}],
    }
    path = write_review(tmp_path, 'one', 'shared', alternative_records=[alternative])
    source.write_text('observation: true\n')
    write_project(tmp_path, ['one/shared'])
    args = ['project-counterparts', '--root', str(tmp_path), '--project', 'projects/EXAMPLE.md']
    monkeypatch.setattr('sys.argv', args)
    main()
    output = tmp_path / 'projects/EXAMPLE/COUNTERPARTS.md'
    assert '../../genes/one/shared/evidence.yaml' in output.read_text()
    monkeypatch.setattr('sys.argv', [*args, '--check'])
    main()
    data = yaml.safe_load(path.read_text())
    data['alternative_records'][0]['reason'] = 'Revised conclusion'
    path.write_text(yaml.safe_dump(data))
    with pytest.raises(SystemExit, match='1'):
        main()
    monkeypatch.setattr('sys.argv', args)
    main()
    assert 'Revised conclusion' in output.read_text()
    source.unlink()
    with pytest.raises(ValueError, match='Missing evidence source'):
        render_markdown(collect_assessments(tmp_path / 'projects/EXAMPLE.md', tmp_path),
                        tmp_path / 'projects/EXAMPLE.md', tmp_path, output)


def test_committed_reports_match_current_frontmatter_and_yaml():
    root = Path(__file__).parents[1]
    project = root / 'projects/ORPHAN_CURATED.md'
    rows = collect_assessments(project, root)
    output = project.with_suffix('') / 'COUNTERPARTS.md'
    assert output.read_text() == render_markdown(rows, project, root, output)
    assert (output.parent / 'counterpart-assessments.csv').read_text() == render_csv(rows)
