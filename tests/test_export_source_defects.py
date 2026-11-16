"""Tests for the source-defect exporter (upstream reporting of source-record errors)."""

import csv
import json
import random
from pathlib import Path

import pytest

from ai_gene_review.tools.export_source_defects import (
    COLUMNS,
    SEVERITY_BANDS,
    SEVERITY_ORDER,
    _describe_change,
    collect,
    group_defects,
    rank,
    render_report,
    render_worklist,
    write_outputs,
)

GENE_REVIEW = """
id: P42760
gene_symbol: GSTF6
existing_annotations:
- term:
    id: GO:2001147
    label: camalexin binding
  evidence_type: IDA
  original_reference_id: PMID:21631432
  qualifier: enables
  review:
    summary: s
    action: UNDECIDED
    source_defects:
    - defect_type: WRONG_GENE_PRODUCT
      resource: TAIR
      asserted_value: UniProtKB:P42760
      corrected_value: UniProtKB:Q9SLM6
      corrected_label: GSTF3
      cause: LEGACY_ALIAS
      confidence: PROBABLE
      explanation: Legacy alias mapped to the wrong locus.
      supported_by:
      - reference_id: PMID:21631432
        supporting_text: GSTF2 and GSTF3
- term:
    id: GO:0005737
    label: cytoplasm
  evidence_type: IDA
  original_reference_id: PMID:1
  review:
    summary: s
    action: ACCEPT
"""

GOCAM_REVIEW = """
id: gomodel:1
activity_reviews:
- activity_id: gomodel:1/2
  gene_product: AGI_LocusCode:AT2G45160
  molecular_function: GO:0043995
  source_defects:
  - defect_type: WRONG_GENE_PRODUCT
    resource: GO_CAM
    asserted_value: AGI_LocusCode:AT2G45160
    corrected_value: AGI_LocusCode:AT5G64610
    confidence: CONFIRMED
    explanation: Symbol collision.
    report_status: FIXED
  - defect_type: WRONG_GENE_PRODUCT
    resource: GO_CAM
    slot: has_input
    requested_change: DELETE_VALUE
    asserted_value: AGI_LocusCode:AT2G45160
    confidence: CONFIRMED
    explanation: Drop the input.
"""


@pytest.fixture
def repo(tmp_path: Path) -> Path:
    gene = tmp_path / "genes" / "ARATH" / "GSTF6"
    gene.mkdir(parents=True)
    (gene / "GSTF6-ai-review.yaml").write_text(GENE_REVIEW, encoding="utf-8")
    other = tmp_path / "genes" / "ARATH" / "NONE"
    other.mkdir(parents=True)
    (other / "NONE-ai-review.yaml").write_text("id: X\n", encoding="utf-8")
    model = tmp_path / "gocams" / "1"
    model.mkdir(parents=True)
    (model / "1-review.yaml").write_text(GOCAM_REVIEW, encoding="utf-8")
    return tmp_path


def test_collect_reads_gene_and_gocam_defects(repo: Path) -> None:
    rows = collect(repo)
    assert [r["resource"] for r in rows] == ["GO_CAM", "GO_CAM", "TAIR"]
    gocam, _, tair = rows
    assert gocam["record"] == "gomodel:1/2"
    assert gocam["subject_id"] == "AGI_LocusCode:AT2G45160"
    assert tair["subject_id"] == "UniProtKB:P42760"
    assert tair["term_id"] == "GO:2001147"
    assert tair["original_reference_id"] == "PMID:21631432"
    assert tair["report_status"] == "NOT_REPORTED"


def test_report_omits_fixed_defects(repo: Path) -> None:
    rows = collect(repo)
    gocam_md = render_report("GO_CAM", [r for r in rows if r["resource"] == "GO_CAM"])
    assert "1 open defect(s)" in gocam_md
    assert "remove AGI_LocusCode:AT2G45160 from has_input" in gocam_md
    assert "**Subject:** AGI_LocusCode:AT2G45160" in gocam_md
    tair_md = render_report("TAIR", [r for r in rows if r["resource"] == "TAIR"])
    assert "UniProtKB:P42760 → UniProtKB:Q9SLM6 (GSTF3)" in tair_md
    assert "> GSTF2 and GSTF3" in tair_md


def test_write_outputs_writes_tsv_and_one_report_per_resource(repo: Path) -> None:
    tsv = repo / "out" / "d.tsv"
    report_dir = repo / "out" / "reports"
    write_outputs(repo, tsv, report_dir)
    with tsv.open(encoding="utf-8") as fh:
        assert len(list(csv.DictReader(fh, delimiter="\t"))) == 3
    # WORKLIST.md is the cross-resource ranked queue, written beside the reports.
    assert sorted(p.name for p in report_dir.iterdir()) == [
        "GO_CAM.md",
        "TAIR.md",
        "WORKLIST.md",
    ]


@pytest.mark.parametrize(
    "change,corrected,expected",
    [
        ("", "", "A:1 (no replacement value; see explanation)"),
        ("", "A:2", "A:1 → A:2"),
        ("REPOINT", "A:2", "A:1 → A:2"),
        ("DELETE_ROW", "", "delete the record asserting A:1"),
        ("CHECK", "", "check A:1 (alternatives in the explanation)"),
    ],
)
def test_change_line(change: str, corrected: str, expected: str) -> None:
    rows = [{**{c: "" for c in COLUMNS}, "resource": "TAIR", "report_status": "NOT_REPORTED",
             "defect_type": "OTHER", "confidence": "SUSPECTED", "asserted_value": "A:1",
             "corrected_value": corrected, "requested_change": change, "supported_by": "[]"}]
    assert f"**Change:** {expected}" in render_report("TAIR", rows)


@pytest.mark.parametrize(
    "evidence",
    [
        {"reference_id": "PMID:1"},
        {"reference_id": "PMID:1", "supporting_text": None},
        {"reference_id": "PMID:1", "supporting_text": ""},
        {"reference_id": "PMID:1", "supporting_text": " \n\t "},
    ],
)
def test_reference_only_evidence_is_not_rendered_as_a_quote(evidence: dict) -> None:
    row = {**{c: "" for c in COLUMNS}, "supported_by": json.dumps([evidence])}
    before = row.copy()
    rendered = render_report("TAIR", [row])
    assert rendered.endswith("\n- **Evidence reference:** PMID:1\n")
    assert not any(line.startswith(">") for line in rendered.splitlines())
    assert row == before


def test_mixed_evidence_preserves_reference_order_and_quoted_format() -> None:
    # Synthetic text tests formatting only; it is not a publication excerpt.
    evidence = [
        {"reference_id": "PMID:1"},
        {"reference_id": "PMID:2", "supporting_text": "  example\nquoted\ttext  "},
        {"reference_id": "https://example.org/evidence"},
    ]
    row = {**{c: "" for c in COLUMNS}, "supported_by": json.dumps(evidence)}
    rendered = render_report("TAIR", [row])
    assert rendered.endswith(
        "\n- **Evidence reference:** PMID:1\n"
        "\n> example quoted text\n> — PMID:2\n"
        "\n- **Evidence reference:** https://example.org/evidence\n"
    )
    assert json.loads(row["supported_by"]) == evidence


def test_reference_only_export_preserves_tsv_evidence_and_source(repo: Path) -> None:
    source = repo / "genes" / "ARATH" / "GSTF6" / "GSTF6-ai-review.yaml"
    source.write_text(GENE_REVIEW.replace("        supporting_text: GSTF2 and GSTF3\n", ""), encoding="utf-8")
    before = source.read_bytes()
    tsv = repo / "reference-only.tsv"
    report_dir = repo / "reference-only-reports"
    rows = write_outputs(repo, tsv, report_dir)
    with tsv.open(encoding="utf-8") as stream:
        saved_rows = list(csv.DictReader(stream, delimiter="\t"))
    assert saved_rows == rows
    tair = next(row for row in saved_rows if row["resource"] == "TAIR")
    assert json.loads(tair["supported_by"]) == [{"reference_id": "PMID:21631432"}]
    report = (report_dir / "TAIR.md").read_text(encoding="utf-8")
    assert "- **Evidence reference:** PMID:21631432" in report
    assert not any(line.startswith(">") for line in report.splitlines())
    assert source.read_bytes() == before


ISOFORM_REVIEW = """
id: Q96PV0
gene_symbol: SYNGAP1
functional_isoforms:
- id: SYNGAP1_ALPHA1
  name: SynGAP-alpha1
  type: SPLICE_CLASS
  description: d
  source_defects:
  - defect_type: MISSING_ISOFORM
    resource: UNIPROT
    record: UniProtKB:Q96PV0
    requested_change: ADD
    asserted_value: UniProtKB:Q96PV0
    corrected_value: RefSeq:NP_001123538.1
    confidence: CONFIRMED
    explanation: The alpha1 C-terminus is not among the entry's isoforms.
"""


def test_collect_reads_functional_isoform_defects(tmp_path: Path) -> None:
    """A defect in UniProt's isoform list is exported against the functional isoform."""
    gene = tmp_path / "genes" / "human" / "SYNGAP1"
    gene.mkdir(parents=True)
    (gene / "SYNGAP1-ai-review.yaml").write_text(ISOFORM_REVIEW, encoding="utf-8")
    (row,) = collect(tmp_path)
    assert row["resource"] == "UNIPROT"
    assert row["defect_type"] == "MISSING_ISOFORM"
    assert row["requested_change"] == "ADD"
    assert row["subject_id"] == "UniProtKB:Q96PV0"
    assert row["term_id"] == "SYNGAP1_ALPHA1"
    assert row["record"] == "UniProtKB:Q96PV0"
    assert row["corrected_value"] == "RefSeq:NP_001123538.1"
    assert "add RefSeq:NP_001123538.1 to UniProtKB:Q96PV0" in render_report("UNIPROT", [row])


REFERENCE_DEFECT_REVIEW = """
id: G5EDF7
gene_symbol: lgg-2
references:
- id: file:worm/lgg-2/lgg-2-deep-research-wormbase.md
  title: WormBase gene description for lgg-2 (worm)
  reference_review:
    relevance: MEDIUM
    correctness: DISPUTED
    source_defects:
    - defect_type: OUTDATED_STATEMENT
      resource: WORMBASE
      record: WB:WBGene00002981
      slot: MOD_provided_gene_description
      requested_change: CHECK
      asserted_value: LGG-2 has no obvious function in RNAi assays
      confidence: CONFIRMED
      explanation: The description says LGG-2 has no obvious function in RNAi assays.
"""


def test_collect_reads_reference_review_defects(tmp_path: Path) -> None:
    """A defect in a cited source's free text is exported against that reference."""
    gene = tmp_path / "genes" / "worm" / "lgg-2"
    gene.mkdir(parents=True)
    (gene / "lgg-2-ai-review.yaml").write_text(REFERENCE_DEFECT_REVIEW, encoding="utf-8")
    (row,) = collect(tmp_path)
    assert row["resource"] == "WORMBASE"
    assert row["defect_type"] == "OUTDATED_STATEMENT"
    assert row["slot"] == "MOD_provided_gene_description"
    assert row["subject_id"] == "UniProtKB:G5EDF7"
    assert row["original_reference_id"] == "file:worm/lgg-2/lgg-2-deep-research-wormbase.md"
    assert row["record"] == "WB:WBGene00002981"
    assert row["asserted_value"] == "LGG-2 has no obvious function in RNAi assays"
    report = render_report("WORMBASE", [row])
    assert 'revise "LGG-2 has no obvious function in RNAi assays" in MOD_provided_gene_description' in report


def test_missing_statement_add_renders_without_corrected_value() -> None:
    """An ADD for missing free text has no corrected value; the explanation carries it."""
    row = {"asserted_value": "WB:WBGene1", "corrected_value": "", "corrected_label": "",
           "slot": "MOD_provided_gene_description", "requested_change": "ADD",
           "defect_type": "MISSING_STATEMENT"}
    assert _describe_change(row) == (
        "add the content described in the explanation to WB:WBGene1 (MOD_provided_gene_description)"
    )


# --- docs/source_defects.md must list the enum values the schema defines -------
#
# docs/source_defects.md tabulates the permissible values of SourceDefectTypeEnum
# and SourceDefectCauseEnum. Those rows were generated from the schema, but
# "generated once" is not "cannot drift": before this test the defect_type row
# had silently fallen three values behind (WRONG_STATEMENT, OUTDATED_STATEMENT,
# MISSING_STATEMENT). This asserts the invariant instead of claiming it.

SCHEMA_PATH = Path(__file__).resolve().parents[1] / "src/ai_gene_review/schema/gene_review.yaml"
DOCS_PATH = Path(__file__).resolve().parents[1] / "docs/source_defects.md"


def _schema_enum_values(enum_name: str) -> list[str]:
    import yaml

    schema = yaml.safe_load(SCHEMA_PATH.read_text(encoding="utf-8"))
    return list(schema["enums"][enum_name]["permissible_values"])


def _docs_table_row(field: str) -> str:
    for line in DOCS_PATH.read_text(encoding="utf-8").splitlines():
        if line.startswith(f"| `{field}` |"):
            return line
    raise AssertionError(f"no table row for `{field}` in {DOCS_PATH.name}")


@pytest.mark.parametrize(
    ("field", "enum_name"),
    [
        ("defect_type", "SourceDefectTypeEnum"),
        ("cause", "SourceDefectCauseEnum"),
    ],
)
def test_docs_table_lists_every_schema_enum_value(field: str, enum_name: str) -> None:
    """Every permissible value appears in the docs row for that field."""
    row = _docs_table_row(field)
    missing = [v for v in _schema_enum_values(enum_name) if f"`{v}`" not in row]
    assert not missing, (
        f"docs/source_defects.md `{field}` row is missing {missing}; "
        f"regenerate it from {enum_name} rather than editing it by hand"
    )


def test_docs_table_invents_no_enum_values() -> None:
    """The docs rows name no value the schema does not define."""
    import re

    for field, enum_name in [
        ("defect_type", "SourceDefectTypeEnum"),
        ("cause", "SourceDefectCauseEnum"),
    ]:
        row = _docs_table_row(field)
        quoted = set(re.findall(r"`([A-Z][A-Z_]+)`", row))
        unknown = quoted - set(_schema_enum_values(enum_name))
        assert not unknown, f"docs `{field}` row names non-schema values {sorted(unknown)}"


def test_source_resource_enum_has_the_pipeline_values_reports_route_on() -> None:
    """The resources that the largest defect groups name are nameable.

    export_source_defects keys one report per `resource` string, so a resource
    with no enum value gets no report. InterPro and PANTHER are pipelines whose
    defects affect every protein inheriting a mapping, which is why they are
    distinct from the MOD values and from GO_CENTRAL.
    """
    values = set(_schema_enum_values("SourceResourceEnum"))
    for expected in ("INTERPRO", "PANTHER", "COMPLEX_PORTAL", "GOC"):
        assert expected in values, f"SourceResourceEnum lost {expected}"
    assert "GO_CENTRAL" in values, "PANTHER must not have replaced GO_CENTRAL"


# --- grouping: one item per real upstream defect ------------------------------
#
# 2554 recorded instances collapse to ~1800 distinct fixes, because the same fix
# is recorded independently by many reviews. The grouping key is the *fix* --
# who must change what, in which field, from what, to what -- and not the
# annotation context (gene, GO term, evidence code), which varies across the
# instances of one fix. These tests pin both halves of that.


def _instance(**over: str) -> dict:
    """Build one exported defect row, overriding the fields a test cares about."""
    row = {c: "" for c in COLUMNS}
    row.update(
        {
            "resource": "TAIR",
            "report_status": "NOT_REPORTED",
            "defect_type": "WRONG_TERM",
            "confidence": "PROBABLE",
            "asserted_value": "GO:1",
            "explanation": "Mapped to the wrong term.",
            "supported_by": "[]",
            "source_path": "genes/ARATH/A/A-ai-review.yaml",
        }
    )
    row.update(over)
    return row


def test_one_fix_recorded_by_several_reviews_is_one_group() -> None:
    """The annotation context differs per instance; the fix is the same."""
    rows = [
        _instance(term_id="GO:9", gene_symbol="A", evidence_type="IDA"),
        _instance(
            term_id="GO:8",
            gene_symbol="B",
            evidence_type="IBA",
            source_path="genes/ARATH/B/B-ai-review.yaml",
        ),
    ]
    (group,) = group_defects(rows)
    assert group.count == 2
    assert group.source_paths == (
        "genes/ARATH/A/A-ai-review.yaml",
        "genes/ARATH/B/B-ai-review.yaml",
    )


@pytest.mark.parametrize(
    ("field", "other_value"),
    [
        ("resource", "MGI"),
        ("defect_type", "WRONG_QUALIFIER"),
        ("record", "gomodel:1/2"),
        ("slot", "has_input"),
        ("asserted_value", "GO:3"),
        ("corrected_value", "GO:2"),
        ("requested_change", "DELETE_ROW"),
    ],
)
def test_a_different_fix_is_a_different_group(field: str, other_value: str) -> None:
    """Every field of the key names part of the fix, so changing one splits."""
    assert len(group_defects([_instance(), _instance(**{field: other_value})])) == 2


def test_two_wrong_references_on_one_record_are_two_groups() -> None:
    """`record` does not displace `asserted_value`: one activity, two bad PMIDs."""
    rows = [
        _instance(record="gomodel:1/2", defect_type="WRONG_REFERENCE", asserted_value="PMID:1"),
        _instance(record="gomodel:1/2", defect_type="WRONG_REFERENCE", asserted_value="PMID:2"),
    ]
    assert len(group_defects(rows)) == 2


def test_competing_corrections_stay_apart() -> None:
    """Two reviews proposing different replacements disagree; merging would hide it."""
    rows = [_instance(corrected_value="GO:2"), _instance(corrected_value="GO:3")]
    assert {g.corrected_value for g in group_defects(rows)} == {"GO:2", "GO:3"}


def test_group_id_depends_only_on_the_key() -> None:
    """A group's id is stable, so it can be used to join the TSV across runs."""
    alone = group_defects([_instance()])[0].id
    with_others = next(
        g.id for g in group_defects([_instance(), _instance(resource="MGI")]) if g.resource == "TAIR"
    )
    assert alone == with_others
    assert alone != group_defects([_instance(resource="MGI")])[0].id


def test_closed_instances_are_dropped_before_grouping() -> None:
    """FIXED and DECLINED rows leave the worklist, as they leave the resource reports."""
    rows = [
        _instance(report_status="FIXED"),
        _instance(report_status="DECLINED", source_path="genes/ARATH/B/B-ai-review.yaml"),
        _instance(resource="MGI"),
    ]
    assert [g.resource for g in group_defects(rows)] == ["MGI"]


# --- reasons: named, independently true, printed beside the item --------------


@pytest.mark.parametrize(
    ("resource", "propagates"),
    [
        ("INTERPRO", True),
        ("PANTHER", True),
        ("GOC", True),
        ("GO_CENTRAL", False),
        ("GOA_EBI", False),
        ("UNIPROT", False),
        ("TAIR", False),
    ],
)
def test_only_pipeline_and_ontology_resources_propagate_by_resource(
    resource: str, propagates: bool
) -> None:
    """GO_CENTRAL is PAINT curation, not a pipeline (docs/source_defects.md)."""
    (group,) = group_defects([_instance(resource=resource)])
    assert group.propagates is propagates


@pytest.mark.parametrize("cause", ["OVER_PROPAGATION", "SCOPE_OVER_REACH"])
def test_a_propagating_cause_marks_any_resource(cause: str) -> None:
    """A defect whose own cause says it spread is a one-fix-many-rows defect."""
    (group,) = group_defects([_instance(resource="GO_CENTRAL", cause=cause)])
    assert group.propagates


def test_an_instance_that_named_no_cause_does_not_block_propagation() -> None:
    """Silence is not disagreement; nor is UNKNOWN, which identifies no mechanism."""
    for silent in ("", "UNKNOWN"):
        rows = [
            _instance(cause=silent),
            _instance(cause="OVER_PROPAGATION", source_path="genes/ARATH/B/B-ai-review.yaml"),
        ]
        (group,) = group_defects(rows)
        assert group.propagates, silent


def test_a_competing_identified_cause_withdraws_the_propagation_claim() -> None:
    """The corpus's largest group is 55 row-level fixes whose mechanism is disputed.

    5 of its instances say SCOPE_OVER_REACH and 27 name other mechanisms. One fix
    does not correct all 55, so the group must not claim that it does.
    """
    rows = [
        _instance(cause="SCOPE_OVER_REACH"),
        _instance(cause="OTHER", source_path="genes/ARATH/B/B-ai-review.yaml"),
    ]
    (group,) = group_defects(rows)
    assert not group.propagates


def test_a_competing_cause_cannot_demote_a_pipeline_resource() -> None:
    """INTERPRO records are inherited whatever mechanism put the term there."""
    rows = [
        _instance(resource="INTERPRO", cause="SCOPE_OVER_REACH"),
        _instance(resource="INTERPRO", cause="OTHER", source_path="genes/ARATH/B/B-ai-review.yaml"),
    ]
    (group,) = group_defects(rows)
    assert group.propagates


@pytest.mark.parametrize(
    ("defect_type", "misattributed"),
    [
        ("WRONG_GENE_PRODUCT", True),
        ("MISSING_NEGATION", True),
        ("WRONG_TERM", False),
        ("WRONG_QUALIFIER", False),
        ("WRONG_EVIDENCE_CODE", False),
    ],
)
def test_misattributed_covers_the_wrong_entity_and_the_inverted_sense(
    defect_type: str, misattributed: bool
) -> None:
    (group,) = group_defects([_instance(defect_type=defect_type)])
    assert group.misattributed is misattributed


def test_confidence_is_the_strongest_instance() -> None:
    """One review verifying the defect is enough to file it as a correction."""
    rows = [
        _instance(confidence="SUSPECTED"),
        _instance(confidence="CONFIRMED", source_path="genes/ARATH/B/B-ai-review.yaml"),
    ]
    (group,) = group_defects(rows)
    assert group.confidence == "CONFIRMED"
    assert group.confirmed


def test_the_instances_reason_appears_only_above_one() -> None:
    (single,) = group_defects([_instance()])
    assert not [r for r in single.reasons if r.token.startswith("instances")]
    (several,) = group_defects(
        [_instance(), _instance(source_path="genes/ARATH/B/B-ai-review.yaml")]
    )
    assert "instances: 2" in [r.token for r in several.reasons]


def test_every_reason_states_why_it_is_true_of_this_item() -> None:
    """A rank is only explainable if each reason carries its own ground."""
    (group,) = group_defects(
        [
            _instance(
                resource="INTERPRO",
                defect_type="WRONG_GENE_PRODUCT",
                confidence="CONFIRMED",
                cause="SCOPE_OVER_REACH",
            ),
            _instance(
                resource="INTERPRO",
                defect_type="WRONG_GENE_PRODUCT",
                confidence="CONFIRMED",
                cause="SCOPE_OVER_REACH",
                source_path="genes/ARATH/B/B-ai-review.yaml",
            ),
        ]
    )
    assert [r.token for r in group.reasons] == [
        "propagates",
        "instances: 2",
        "misattributed",
        "confirmed",
    ]
    assert all(reason.because for reason in group.reasons)


# --- ranking: lexicographic over the named reasons, no weighted score ---------


def _ranked_ids(rows: list[dict]) -> list[str]:
    return [g.id for g in rank(group_defects(rows))]


def test_ranking_precedence_is_breadth_then_kind_then_certainty() -> None:
    """propagates > instances > misattributed > confirmed, each independently true."""
    propagating = _instance(resource="INTERPRO")
    systematic = [
        _instance(asserted_value="GO:20"),
        _instance(asserted_value="GO:20", source_path="genes/ARATH/B/B-ai-review.yaml"),
        _instance(asserted_value="GO:20", source_path="genes/ARATH/C/C-ai-review.yaml"),
    ]
    misattributed = _instance(defect_type="WRONG_GENE_PRODUCT")
    confirmed = _instance(asserted_value="GO:30", confidence="CONFIRMED")
    plain = _instance(asserted_value="GO:40")
    rows = [plain, confirmed, misattributed, *systematic, propagating]
    ranked = rank(group_defects(rows))
    assert [(g.resource, g.defect_type, g.count, g.confidence) for g in ranked] == [
        ("INTERPRO", "WRONG_TERM", 1, "PROBABLE"),
        ("TAIR", "WRONG_TERM", 3, "PROBABLE"),
        ("TAIR", "WRONG_GENE_PRODUCT", 1, "PROBABLE"),
        ("TAIR", "WRONG_TERM", 1, "CONFIRMED"),
        ("TAIR", "WRONG_TERM", 1, "PROBABLE"),
    ]


def test_ranking_does_not_depend_on_input_order() -> None:
    """Same corpus, any read order, same worklist."""
    rows = [
        _instance(resource="INTERPRO"),
        _instance(resource="MGI", defect_type="MISSING_NEGATION"),
        _instance(resource="UNIPROT", confidence="CONFIRMED"),
        _instance(resource="SGD", asserted_value="GO:7"),
        _instance(resource="SGD", asserted_value="GO:7", source_path="genes/ARATH/B/B-ai-review.yaml"),
    ]
    expected = _ranked_ids(rows)
    for seed in range(5):
        shuffled = rows[:]
        random.Random(seed).shuffle(shuffled)
        assert _ranked_ids(shuffled) == expected


def test_ranking_is_total_for_groups_alike_in_every_reason() -> None:
    """Two groups with identical reasons are ordered by their key, not by chance."""
    rows = [_instance(asserted_value="GO:9"), _instance(asserted_value="GO:2")]
    assert [g.asserted_value for g in rank(group_defects(rows))] == ["GO:2", "GO:9"]


# --- severity: the curator-set axis the reasons cannot derive -----------------


def test_severity_band_table_covers_every_schema_value_and_the_unset_case() -> None:
    """A schema value the ranker does not know would raise at rank time."""
    assert set(_schema_enum_values("SourceDefectSeverityEnum")) <= set(SEVERITY_BANDS)
    assert "" in SEVERITY_BANDS, "an unassessed defect must still have a band"


def test_severity_enum_has_exactly_three_values() -> None:
    assert len(_schema_enum_values("SourceDefectSeverityEnum")) == 3


def test_severity_order_matches_the_schema_worst_first() -> None:
    """The group takes the worst severity, so the code's order must be the schema's.

    A value missing from SEVERITY_ORDER raises in `GroupedDefect.severity`, and a
    reordering would silently pick the wrong one.
    """
    assert SEVERITY_ORDER == tuple(_schema_enum_values("SourceDefectSeverityEnum"))


def test_a_curator_severity_overrides_the_derived_position() -> None:
    """MISLEADING lifts a one-off above a propagating defect; COSMETIC sinks one."""
    propagating = _instance(resource="INTERPRO")
    misleading = _instance(resource="TAIR", severity="MISLEADING")
    cosmetic = _instance(resource="PANTHER", severity="COSMETIC")
    ranked = rank(group_defects([propagating, misleading, cosmetic]))
    assert [g.resource for g in ranked] == ["TAIR", "INTERPRO", "PANTHER"]


def test_imprecise_records_an_assessment_without_moving_the_item() -> None:
    """IMPRECISE is the default band, so it changes no position."""
    rows = [_instance(resource="INTERPRO"), _instance(resource="TAIR")]
    without = [g.resource for g in rank(group_defects(rows))]
    with_imprecise = [
        g.resource
        for g in rank(
            group_defects([_instance(resource="INTERPRO", severity="IMPRECISE"), _instance(resource="TAIR")])
        )
    ]
    assert without == with_imprecise == ["INTERPRO", "TAIR"]
    (group,) = group_defects([_instance(severity="IMPRECISE")])
    assert group.severity == "IMPRECISE"


def test_the_worst_curator_severity_in_a_group_wins() -> None:
    rows = [
        _instance(severity="COSMETIC"),
        _instance(severity="MISLEADING", source_path="genes/ARATH/B/B-ai-review.yaml"),
    ]
    (group,) = group_defects(rows)
    assert group.severity == "MISLEADING"


# --- the worklist -------------------------------------------------------------


def test_worklist_lists_groups_worst_first_with_their_reasons() -> None:
    rows = [
        _instance(resource="TAIR", asserted_value="GO:40"),
        _instance(resource="INTERPRO", cause="SCOPE_OVER_REACH"),
    ]
    worklist = render_worklist(rank(group_defects(rows)))
    headings = [line for line in worklist.splitlines() if line.startswith("## ")]
    assert headings[0].startswith("## 1. INTERPRO")
    assert headings[1].startswith("## 2. TAIR")
    assert "propagates" in worklist
    assert "SCOPE_OVER_REACH" in worklist


def test_worklist_shows_the_change_the_explanation_and_the_reviews() -> None:
    rows = [
        _instance(
            resource="MGI",
            asserted_value="GO:1",
            corrected_value="GO:2",
            corrected_label="better term",
            requested_change="REPOINT",
            explanation="The mapped term names a different reaction.",
            gene_symbol="Abc1",
            term_id="GO:1",
            term_label="old term",
            evidence_type="IEA",
        ),
        _instance(
            resource="MGI",
            asserted_value="GO:1",
            corrected_value="GO:2",
            corrected_label="better term",
            requested_change="REPOINT",
            explanation="The mapped term names a different reaction.",
            gene_symbol="Abc2",
            source_path="genes/mouse/Abc2/Abc2-ai-review.yaml",
        ),
    ]
    worklist = render_worklist(rank(group_defects(rows)))
    assert "GO:1 → GO:2 (better term)" in worklist
    assert "The mapped term names a different reaction." in worklist
    assert "genes/ARATH/A/A-ai-review.yaml" in worklist
    assert "genes/mouse/Abc2/Abc2-ai-review.yaml" in worklist


def test_worklist_says_what_a_group_spans() -> None:
    """A GAF-row defect has no record id, so a group of them is a class of asks.

    The spans line is how a reader tells one upstream edit from a table of
    row-level asks that happen to request the same change.
    """
    rows = [
        _instance(subject_id="UniProtKB:P1", term_id="GO:7", term_label="a"),
        _instance(
            subject_id="UniProtKB:P2",
            term_id="GO:8",
            term_label="b",
            source_path="genes/ARATH/B/B-ai-review.yaml",
        ),
    ]
    worklist = render_worklist(rank(group_defects(rows)))
    assert "- **Spans:** 2 gene products and 2 annotated terms" in worklist
    single = render_worklist(rank(group_defects([_instance(subject_id="UniProtKB:P1")])))
    assert "**Spans:**" not in single


def test_worklist_distinguishes_two_defective_rows_of_one_gene() -> None:
    """Two rows of one review differ by reference, not by path, so name both."""
    rows = [
        _instance(term_id="GO:7", term_label="a", evidence_type="EXP", original_reference_id="PMID:1"),
        _instance(term_id="GO:7", term_label="a", evidence_type="EXP", original_reference_id="PMID:2"),
    ]
    worklist = render_worklist(rank(group_defects(rows)))
    assert "(EXP, PMID:1)" in worklist and "(EXP, PMID:2)" in worklist


def test_worklist_reports_when_the_instances_explain_the_defect_differently() -> None:
    rows = [
        _instance(explanation="One reading."),
        _instance(explanation="Another reading.", source_path="genes/ARATH/B/B-ai-review.yaml"),
    ]
    worklist = render_worklist(rank(group_defects(rows)))
    assert "2 distinct explanations" in worklist


def test_worklist_marks_a_severity_as_curator_set() -> None:
    worklist = render_worklist(rank(group_defects([_instance(severity="MISLEADING")])))
    assert "- **Severity:** MISLEADING (curator-set)" in worklist
    unset = render_worklist(rank(group_defects([_instance()])))
    assert "- **Severity:** not assessed" in unset
    assert "(curator-set)" not in unset


def test_worklist_sections_filed_defects_below_the_queue() -> None:
    """A filed defect needs chasing, not filing, so it does not dilute the queue."""
    rows = [
        _instance(resource="MGI", report_status="REPORTED", report_url="https://example.org/1"),
        _instance(resource="TAIR"),
    ]
    worklist = render_worklist(rank(group_defects(rows)))
    assert worklist.index("## 1. TAIR") < worklist.index("Already filed")
    assert worklist.index("Already filed") < worklist.index("MGI")
    assert "https://example.org/1" in worklist


# --- exported artifacts -------------------------------------------------------


def test_tsv_carries_the_group_and_rank_columns(repo: Path) -> None:
    tsv = repo / "out" / "d.tsv"
    write_outputs(repo, tsv, repo / "out" / "reports")
    with tsv.open(encoding="utf-8") as stream:
        rows = list(csv.DictReader(stream, delimiter="\t"))
    for column in ("group_id", "group_rank", "group_size", "group_reasons", "severity"):
        assert column in rows[0]
    open_gocam = next(r for r in rows if r["resource"] == "GO_CAM" and r["report_status"] != "FIXED")
    assert open_gocam["group_size"] == "1"
    assert int(open_gocam["group_rank"]) >= 1
    fixed = next(r for r in rows if r["report_status"] == "FIXED")
    assert fixed["group_id"] and fixed["group_rank"] == ""


def test_write_outputs_writes_a_ranked_worklist(repo: Path) -> None:
    report_dir = repo / "out" / "reports"
    write_outputs(repo, repo / "out" / "d.tsv", report_dir)
    worklist = (report_dir / "WORKLIST.md").read_text(encoding="utf-8")
    assert worklist.startswith("# Source-record defect worklist")
    assert "## 1. " in worklist
    assert sorted(p.name for p in report_dir.iterdir()) == ["GO_CAM.md", "TAIR.md", "WORKLIST.md"]


# --- every document kind that can carry a defect is accounted for -------------
#
# source_defects sits on four classes; a defect recorded in a document kind the
# exporter does not glob is invisible to every report. These derive the set of
# top-level document classes that can reach the slot from the schema itself, so
# a new one is noticed rather than assumed.

COLLECTED_DOCUMENT_CLASSES = {"GeneReview", "GoCamReview"}
UNCOLLECTED_DOCUMENT_CLASSES = {
    # Each reaches source_defects only through references[].reference_review.
    "ModuleReview": ("modules/*.yaml",),
    "PredictionReview": ("genes/*/*/*-predictions-review.yaml",),
    "RuleReview": ("rules/*/*-review.yaml", "rules/*/*/*-review.yaml"),
    "CuratedRule": ("rules/curated/*.yaml",),
}


def _document_classes_reaching(slot_name: str) -> set[str]:
    """Top-level classes (referenced by no other class) that can reach ``slot_name``."""
    import yaml

    schema = yaml.safe_load(SCHEMA_PATH.read_text(encoding="utf-8"))
    classes, slots = schema["classes"], schema.get("slots", {})
    subclasses: dict[str, list[str]] = {}
    for name, body in classes.items():
        if body.get("is_a"):
            subclasses.setdefault(body["is_a"], []).append(name)

    def declarations(name: str) -> set[tuple[str, str | None]]:
        """Every (slot name, range) pair the class declares or inherits."""
        inherited: list[str] = []
        cursor: str | None = name
        while cursor:
            inherited.append(cursor)
            cursor = classes[cursor].get("is_a")
        found: set[tuple[str, str | None]] = set()
        for ancestor in inherited:
            body = classes[ancestor]
            for declared in body.get("slots") or []:
                found.add((declared, (slots.get(declared) or {}).get("range")))
            for declared, definition in (body.get("attributes") or {}).items():
                found.add((declared, (definition or {}).get("range")))
        return found

    def descendants(name: str) -> set[str]:
        """``name`` and every class that inherits from it."""
        seen, stack = {name}, [name]
        while stack:
            for child in subclasses.get(stack.pop(), []):
                if child not in seen:
                    seen.add(child)
                    stack.append(child)
        return seen

    holders = {
        name for name in classes if any(declared == slot_name for declared, _ in declarations(name))
    }
    referenced_by: dict[str, set[str]] = {}
    for name in classes:
        for _, target in declarations(name):
            if target is not None and target in classes:
                for concrete in descendants(target):
                    referenced_by.setdefault(concrete, set()).add(name)
    reaching, frontier = set(holders), list(holders)
    while frontier:
        for parent in referenced_by.get(frontier.pop(), set()):
            if parent not in reaching:
                reaching.add(parent)
                frontier.append(parent)
    return {name for name in reaching if not referenced_by.get(name)}


def test_the_schema_permits_source_defects_in_exactly_the_known_document_kinds() -> None:
    """A new document kind able to carry a defect must be collected or listed here."""
    assert _document_classes_reaching("source_defects") == (
        COLLECTED_DOCUMENT_CLASSES | set(UNCOLLECTED_DOCUMENT_CLASSES)
    )


def test_family_reviews_cannot_carry_source_defects() -> None:
    """family_review.yaml is standalone and its Reference has no reference_review."""
    import yaml

    family = yaml.safe_load(
        (SCHEMA_PATH.parent / "family_review.yaml").read_text(encoding="utf-8")
    )
    assert "gene_review" not in str(family.get("imports", []))
    assert set(family["classes"]["Reference"]["slots"]) == {"id", "title"}


def test_no_uncollected_document_kind_has_source_defects_to_lose() -> None:
    """If this fails, that kind's defects are invisible: give collect() its glob."""
    repo = SCHEMA_PATH.resolve().parents[3]
    carrying = [
        str(path.relative_to(repo))
        for globs in UNCOLLECTED_DOCUMENT_CLASSES.values()
        for pattern in globs
        for path in repo.glob(pattern)
        if "source_defects:" in path.read_text(encoding="utf-8")
    ]
    assert not carrying, f"source_defects recorded in uncollected documents: {carrying}"


# --- docs must document the new fields ----------------------------------------


def test_docs_table_lists_every_severity_value() -> None:
    row = _docs_table_row("severity")
    missing = [v for v in _schema_enum_values("SourceDefectSeverityEnum") if f"`{v}`" not in row]
    assert not missing, f"docs/source_defects.md `severity` row is missing {missing}"


def test_docs_distinguish_severity_from_confidence() -> None:
    """The one thing a curator must not get wrong about the new field."""
    docs = DOCS_PATH.read_text(encoding="utf-8")
    assert "## Severity is not confidence" in docs


def test_docs_name_every_ranking_reason() -> None:
    """Every reason the ranker can emit is explained in the docs, derived from the code."""
    import re

    docs = DOCS_PATH.read_text(encoding="utf-8")
    rows = [
        _instance(resource="INTERPRO", defect_type="WRONG_GENE_PRODUCT", confidence="CONFIRMED"),
        _instance(
            resource="INTERPRO",
            defect_type="WRONG_GENE_PRODUCT",
            confidence="CONFIRMED",
            source_path="genes/ARATH/B/B-ai-review.yaml",
        ),
    ]
    (group,) = group_defects(rows)
    assert {r.token for r in group.reasons} == {
        "propagates",
        "instances: 2",
        "misattributed",
        "confirmed",
    }
    for reason in group.reasons:
        word = reason.token.split(":")[0]
        assert re.search(rf"`{word}(`|:)", docs), f"docs do not name the `{word}` reason"
