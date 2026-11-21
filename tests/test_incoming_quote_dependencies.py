from pathlib import Path

import yaml

from ai_gene_review.validation.incoming_quote_dependencies import (
    SourceChange,
    check_incoming_quotes,
    format_issue,
    parse_name_status_z,
    reference_ids_for_source,
)
from ai_gene_review.validation.local_source_text import quote_digest
from ai_gene_review.validation.quote_check import Outcome


def _write_yaml(path: Path, data: dict) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")
    return path


def _write_text(path: Path, text: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


def _record(reference_id: str, supporting_text: str) -> dict:
    return {
        "evidence": [
            {
                "source_id": reference_id,
                "supporting_text": supporting_text,
            }
        ]
    }


def test_edit_changed_family_review_rechecks_unchanged_gene_quote(tmp_path: Path):
    source = _write_text(
        tmp_path / "interpro/panther/PTHR43323/PTHR43323-review.yaml",
        "The revised family review no longer contains the old ERG13 sentence.",
    )
    record = _write_yaml(
        tmp_path / "genes/CANAL/ERG13/ERG13-ai-review.yaml",
        _record(
            "file:interpro/panther/PTHR43323/PTHR43323-review.yaml",
            "Every reviewed recipient retains this IBA: ERG13 (yeast), hcs1 (SCHPO).",
        ),
    )

    issues = check_incoming_quotes(
        [SourceChange("M", source.relative_to(tmp_path))],
        project_root=tmp_path,
        citing_files=[record],
        baseline={},
    )

    assert len(issues) == 1
    assert issues[0].record_path == Path("genes/CANAL/ERG13/ERG13-ai-review.yaml")
    assert issues[0].changed_source == Path(
        "interpro/panther/PTHR43323/PTHR43323-review.yaml"
    )
    assert issues[0].result.quote.path == "evidence[0].supporting_text"
    assert issues[0].result.outcome is Outcome.NOT_FOUND
    assert issues[0].blocking
    assert (
        "changed source interpro/panther/PTHR43323/PTHR43323-review.yaml"
        in format_issue(issues[0])
    )


def test_deleted_local_source_reports_the_citing_slot(tmp_path: Path):
    record = _write_yaml(
        tmp_path / "modules/demo.yaml",
        _record("file:genes/human/TP53/TP53-notes.md", "quoted evidence"),
    )

    issues = check_incoming_quotes(
        [SourceChange("D", Path("genes/human/TP53/TP53-notes.md"))],
        project_root=tmp_path,
        citing_files=[record],
        baseline={},
    )

    assert [(i.record_path, i.changed_source, i.result.outcome) for i in issues] == [
        (
            Path("modules/demo.yaml"),
            Path("genes/human/TP53/TP53-notes.md"),
            Outcome.UNRESOLVED,
        )
    ]


def test_renamed_local_source_checks_the_old_and_new_aliases(tmp_path: Path):
    old = Path("interpro/panther/PTHR1/old-review.yaml")
    new = Path("interpro/panther/PTHR1/new-review.yaml")
    _write_text(tmp_path / new, "new quote")
    stale = _write_yaml(
        tmp_path / "modules/stale.yaml", _record(f"file:{old}", "old quote")
    )
    current = _write_yaml(
        tmp_path / "modules/current.yaml", _record(f"file:{new}", "new quote")
    )

    issues = check_incoming_quotes(
        [SourceChange("R100", old, new)],
        project_root=tmp_path,
        citing_files=[stale, current],
        baseline={},
    )

    assert len(issues) == 1
    assert issues[0].record_path == Path("modules/stale.yaml")
    assert issues[0].result.outcome is Outcome.UNRESOLVED


def test_gene_local_file_aliases_match_both_legal_spellings(tmp_path: Path):
    source = _write_text(tmp_path / "genes/human/TP53/TP53-uniprot.txt", "new uniprot")
    short = _write_yaml(
        tmp_path / "modules/short.yaml",
        _record("file:human/TP53/TP53-uniprot.txt", "old uniprot"),
    )
    long = _write_yaml(
        tmp_path / "modules/long.yaml",
        _record("file:genes/human/TP53/TP53-uniprot.txt", "old uniprot"),
    )

    issues = check_incoming_quotes(
        [SourceChange("M", source.relative_to(tmp_path))],
        project_root=tmp_path,
        citing_files=[short, long],
        baseline={},
    )

    assert {issue.record_path for issue in issues} == {
        Path("modules/short.yaml"),
        Path("modules/long.yaml"),
    }
    assert reference_ids_for_source(source, tmp_path) >= {
        "file:human/TP53/TP53-uniprot.txt",
        "file:genes/human/TP53/TP53-uniprot.txt",
    }


def test_publication_and_reactome_cache_changes_use_existing_matchers(tmp_path: Path):
    publication = _write_text(
        tmp_path / "publications/PMID_1234.md",
        "---\nreference_id: PMID:1234\n---\n\nThis is the new abstract.\n",
    )
    reactome = _write_text(
        tmp_path / "reactome/R-HSA-1234.md",
        "# Revised pathway\n\nThis is the revised reaction summary.\n",
    )
    pub_record = _write_yaml(
        tmp_path / "modules/pub.yaml", _record("PMID:1234", "old abstract")
    )
    reactome_record = _write_yaml(
        tmp_path / "modules/reactome.yaml",
        _record("Reactome:R-HSA-1234", "old reaction"),
    )

    issues = check_incoming_quotes(
        [
            SourceChange("M", publication.relative_to(tmp_path)),
            SourceChange("M", reactome.relative_to(tmp_path)),
        ],
        project_root=tmp_path,
        citing_files=[pub_record, reactome_record],
        baseline={},
    )

    assert {(i.record_path, i.changed_source) for i in issues} == {
        (Path("modules/pub.yaml"), Path("publications/PMID_1234.md")),
        (Path("modules/reactome.yaml"), Path("reactome/R-HSA-1234.md")),
    }


def test_noncanonical_reference_id_spellings_are_matched(tmp_path: Path):
    publication = _write_text(
        tmp_path / "publications/PMID_28132884.md",
        "---\nreference_id: PMID:28132884\n---\n\nnew abstract\n",
    )
    reactome = _write_text(
        tmp_path / "reactome/R-HSA-2454264.md",
        "new Reactome pathway",
    )
    pub_record = _write_yaml(
        tmp_path / "gocams/model/model-review.yaml",
        _record("PMID: 28132884", "old abstract"),
    )
    reactome_record = _write_yaml(
        tmp_path / "genes/human/RLBP1/RLBP1-ai-review.yaml",
        _record("reactome:R-HSA-2454264", "old pathway"),
    )

    issues = check_incoming_quotes(
        [
            SourceChange("M", publication.relative_to(tmp_path)),
            SourceChange("M", reactome.relative_to(tmp_path)),
        ],
        project_root=tmp_path,
        citing_files=[pub_record, reactome_record],
        baseline={},
    )

    assert {(i.record_path, i.changed_source) for i in issues} == {
        (Path("gocams/model/model-review.yaml"), Path("publications/PMID_28132884.md")),
        (
            Path("genes/human/RLBP1/RLBP1-ai-review.yaml"),
            Path("reactome/R-HSA-2454264.md"),
        ),
    }


def test_deleted_doi_cache_finds_underscore_alias(tmp_path: Path):
    source = Path("publications/DOI_10.1096_fasebj.25.1_supplement.714.2.md")
    record = _write_yaml(
        tmp_path / "modules/doi.yaml",
        _record("DOI:10.1096/fasebj.25.1_supplement.714.2", "old abstract"),
    )

    issues = check_incoming_quotes(
        [SourceChange("D", source)],
        project_root=tmp_path,
        citing_files=[record],
        baseline={},
    )

    assert len(issues) == 1
    assert issues[0].record_path == Path("modules/doi.yaml")
    assert issues[0].changed_source == source
    assert issues[0].result.outcome is Outcome.UNRESOLVED


def test_deleted_publication_cache_is_not_refetched(tmp_path: Path, monkeypatch):
    class Validator:
        def validate(self, text: str, reference_id: str):  # pragma: no cover
            raise AssertionError(f"refetched {reference_id}: {text}")

    monkeypatch.setattr(
        "ai_gene_review.validation.incoming_quote_dependencies.build_supporting_text_validator",
        lambda publications: (Validator(), publications),
    )
    source = Path("publications/PMID_1234.md")
    record = _write_yaml(
        tmp_path / "modules/pub.yaml",
        _record("PMID:1234", "old abstract"),
    )

    issues = check_incoming_quotes(
        [SourceChange("D", source)],
        project_root=tmp_path,
        citing_files=[record],
        baseline={},
    )

    assert len(issues) == 1
    assert issues[0].result.outcome is Outcome.UNRESOLVED
    assert "deleted cache publications/PMID_1234.md" in issues[0].result.detail


def test_changed_snapshot_source_is_excluded(tmp_path: Path):
    source = _write_text(
        tmp_path / "recapitulation-experiment/source.md",
        "changed",
    )
    record = _write_yaml(
        tmp_path / "modules/affected.yaml",
        _record("file:recapitulation-experiment/source.md", "old"),
    )

    issues = check_incoming_quotes(
        [SourceChange("M", source.relative_to(tmp_path))],
        project_root=tmp_path,
        citing_files=[record],
        baseline={},
    )

    assert issues == []


def test_unaffected_consumers_are_not_rechecked(tmp_path: Path):
    changed = _write_text(tmp_path / "sources/changed.md", "changed")
    unchanged = _write_text(tmp_path / "sources/unchanged.md", "unchanged")
    affected = _write_yaml(
        tmp_path / "modules/affected.yaml",
        _record("file:sources/changed.md", "changed"),
    )
    unrelated_broken = _write_yaml(
        tmp_path / "modules/unrelated.yaml",
        _record("file:sources/unchanged.md", "invented quote"),
    )

    assert (
        check_incoming_quotes(
            [SourceChange("M", changed.relative_to(tmp_path))],
            project_root=tmp_path,
            citing_files=[affected, unrelated_broken],
            baseline={},
        )
        == []
    )
    assert unchanged.read_text() == "unchanged"


def test_baselines_and_snapshot_exclusions_stay_explicit(tmp_path: Path):
    source = _write_text(tmp_path / "sources/changed.md", "changed")
    bad = "invented quote"
    baselined = _write_yaml(
        tmp_path / "modules/baselined.yaml",
        _record("file:sources/changed.md", bad),
    )
    snapshot = _write_yaml(
        tmp_path / "recapitulation-experiment/frozen.yaml",
        _record("file:sources/changed.md", bad),
    )

    issues = check_incoming_quotes(
        [SourceChange("M", source.relative_to(tmp_path))],
        project_root=tmp_path,
        citing_files=[baselined, snapshot],
        baseline={
            "modules/baselined.yaml": {
                "not_found": {quote_digest("file:sources/changed.md", bad)}
            }
        },
    )

    assert len(issues) == 1
    assert issues[0].record_path == Path("modules/baselined.yaml")
    assert not issues[0].blocking


def test_gene_review_local_quote_baseline_marks_known_failure(tmp_path: Path):
    source = _write_text(tmp_path / "genes/human/TP53/TP53-notes.md", "changed notes")
    bad = "old notes"
    record = _write_yaml(
        tmp_path / "genes/human/TP53/TP53-ai-review.yaml",
        _record("file:human/TP53/TP53-notes.md", bad),
    )

    issues = check_incoming_quotes(
        [SourceChange("M", source.relative_to(tmp_path))],
        project_root=tmp_path,
        citing_files=[record],
        baseline={},
        local_baseline={
            "genes/human/TP53/TP53-ai-review.yaml": {
                quote_digest("file:human/TP53/TP53-notes.md", bad)
            }
        },
    )

    assert len(issues) == 1
    assert issues[0].record_path == Path("genes/human/TP53/TP53-ai-review.yaml")
    assert not issues[0].blocking


def test_parse_name_status_z_handles_edit_delete_and_rename():
    changes = parse_name_status_z(
        b"M\0publications/PMID_1.md\0D\0reactome/R-HSA-1.md\0R100\0old.yaml\0new.yaml\0"
    )
    assert changes == [
        SourceChange("M", Path("publications/PMID_1.md")),
        SourceChange("D", Path("reactome/R-HSA-1.md")),
        SourceChange("R100", Path("old.yaml"), Path("new.yaml")),
    ]
