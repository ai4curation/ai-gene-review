"""An exemplar must fit the process its module asserts, not only the activity.

The motivating case: a "Gq-coupled receptor" annoton in a PLC-activating GPCR
module used ADRB2, a Gs-coupled receptor. Its molecular function (GPCR activity)
was correct, so the function check passed; only the process was wrong.
"""

from pathlib import Path

import pytest
import yaml

from ai_gene_review.module_process_conformance import (
    GoProcessGraph,
    load_goa_process_rows,
    module_process_conformance,
)

ROOT = "GO:0008150"
GPCR = "GO:0007186"
PLC = "GO:0007200"
CAMP = "GO:0007189"
ADRENERGIC_CAMP = "GO:0071880"
UNRELATED = "GO:0006915"
COMPLEX = "GO:0005834"
RECEPTOR_ROOT = "GO:0038023"
GPCR_ACTIVITY = "GO:0004930"
KINASE = "GO:0004674"

# A toy is-a hierarchy: child -> direct parents.
PARENTS = {
    GPCR: {ROOT},
    PLC: {GPCR},
    CAMP: {GPCR},
    ADRENERGIC_CAMP: {CAMP},
    UNRELATED: {ROOT},
    COMPLEX: set(),
    GPCR_ACTIVITY: {RECEPTOR_ROOT},
    KINASE: set(),
}


def ancestors(curie: str) -> frozenset[str]:
    """Transitive closure over the toy hierarchy, excluding the term itself."""
    seen: set[str] = set()
    todo = list(PARENTS.get(curie, ()))
    while todo:
        term = todo.pop()
        if term not in seen:
            seen.add(term)
            todo.extend(PARENTS.get(term, ()))
    return frozenset(seen)


GRAPH = GoProcessGraph(
    ancestors=ancestors, parents=lambda curie: frozenset(PARENTS.get(curie, ()))
)

HEADER = (
    "GENE PRODUCT DB\tGENE PRODUCT ID\tSYMBOL\tQUALIFIER\tGO TERM\tGO NAME\t"
    "GO ASPECT\tECO ID\tGO EVIDENCE CODE\tREFERENCE\tWITH/FROM\tTAXON ID\t"
    "TAXON NAME\tASSIGNED BY\tGENE NAME\tDATE\n"
)


def write_gene(
    tmp_path: Path, accession: str, rows: list[tuple[str, str, str]]
) -> dict:
    """Write a review stub and a GOA file of (qualifier, term, evidence) rows."""
    gene_dir = tmp_path / accession
    gene_dir.mkdir()
    review = gene_dir / f"{accession}-ai-review.yaml"
    review.write_text(f"id: {accession}\n")
    lines = [
        f"UniProtKB\t{accession}\tSYM\t{qualifier}\t{term}\tname\t"
        f"biological_process\tECO:0\t{evidence}\tPMID:1\t\t9606\tHomo sapiens\tX\tname\t2025\n"
        for qualifier, term, evidence in rows
    ]
    (gene_dir / f"{accession}-goa.tsv").write_text(HEADER + "".join(lines))
    return {accession: review}


def module(
    accession: str = "P1",
    *,
    concept: str | None = PLC,
    processes=None,
    function: str | None = GPCR_ACTIVITY,
) -> dict:
    """A one-annoton module whose root concept is ``concept``."""
    annoton: dict = {
        "id": "receptor",
        **({"function": {"term": {"id": function}}} if function else {}),
        "participant": {
            "selector_type": "FAMILY",
            "family": {
                "preferred_term": "receptors",
                "representative_members": [
                    {"preferred_term": "X", "term": {"id": f"UniProtKB:{accession}"}}
                ],
            },
        },
    }
    if processes:
        annoton["processes"] = [{"term": {"id": term}} for term in processes]
    root: dict = {
        "id": "root",
        "parts": [{"node": {"id": "step", "annotons": [annoton]}}],
    }
    if concept:
        root["concepts"] = [{"term": {"id": concept}}]
    return {"module": root}


def status(doc: dict, index: dict) -> list[str]:
    """Statuses of every row the check reports."""
    rows = module_process_conformance(doc, gene_index=index, graph=GRAPH)["rows"]
    return [row["status"] for row in rows]


@pytest.mark.parametrize(
    "rows,expected",
    [
        # Annotated to the module process itself, or below it.
        ([("involved_in", PLC, "IMP")], "PROCESS_SUPPORTED"),
        # The ADRB2 shape: nothing under PLC, experimental data under a sibling.
        ([("involved_in", ADRENERGIC_CAMP, "IDA")], "SIBLING_PROCESS_ONLY"),
        # A sibling known only by prediction is not grounds for a warning.
        ([("involved_in", ADRENERGIC_CAMP, "IBA")], "PROCESS_NOT_ANNOTATED"),
        # An annotation elsewhere in GO says nothing about the choice.
        ([("involved_in", UNRELATED, "IDA")], "PROCESS_NOT_ANNOTATED"),
        # The parent of the module process neither supports nor disputes it.
        ([("involved_in", GPCR, "IDA")], "PROCESS_NOT_ANNOTATED"),
        # Experimental support for both branches is support.
        (
            [("involved_in", ADRENERGIC_CAMP, "IDA"), ("involved_in", PLC, "IBA")],
            "PROCESS_SUPPORTED",
        ),
        # A NOT row is not support.
        ([("NOT|involved_in", PLC, "IDA")], "PROCESS_NOT_ANNOTATED"),
    ],
)
def test_exemplar_process_status(tmp_path, rows, expected):
    index = write_gene(tmp_path, "P1", rows)
    assert status(module(), index) == [expected]


def test_sibling_only_is_a_warning_and_names_the_sibling(tmp_path):
    index = write_gene(tmp_path, "P1", [("involved_in", ADRENERGIC_CAMP, "IDA")])
    row = module_process_conformance(module(), gene_index=index, graph=GRAPH)["rows"][0]
    assert row["severity"] == "warning"
    assert row["annoton_id"] == "receptor"
    assert row["participant_id"] == "UniProtKB:P1"
    assert row["expected_process_ids"] == [PLC]
    assert row["sibling_process_ids"] == [ADRENERGIC_CAMP]
    assert ADRENERGIC_CAMP in row["message"]


@pytest.mark.parametrize("function", [KINASE, None])
def test_sibling_only_is_informational_off_the_receptor_tier(tmp_path, function):
    """A shared downstream component annotated to a sibling pathway is expected."""
    index = write_gene(tmp_path, "P1", [("involved_in", ADRENERGIC_CAMP, "IDA")])
    doc = module(function=function)
    row = module_process_conformance(doc, gene_index=index, graph=GRAPH)["rows"][0]
    assert (row["status"], row["severity"]) == ("SIBLING_PROCESS_ONLY", "info")


@pytest.mark.parametrize(
    "review",
    [
        # A proposed NEW annotation, or any retained row.
        {"existing_annotations": [{"term": {"id": PLC}, "review": {"action": "NEW"}}]},
        # A MODIFY whose replacement is the expected process.
        {
            "existing_annotations": [
                {
                    "term": {"id": GPCR},
                    "review": {
                        "action": "MODIFY",
                        "proposed_replacement_terms": [{"id": PLC}],
                    },
                }
            ]
        },
        # A core function placed in the process.
        {"core_functions": [{"directly_involved_in": [{"id": PLC}]}]},
    ],
)
def test_the_gene_review_can_supply_the_missing_process(tmp_path, review):
    """GOA lags our own reviews; a process the review asserts is not a gap."""
    index = write_gene(tmp_path, "P1", [("involved_in", ADRENERGIC_CAMP, "IDA")])
    index["P1"].write_text(yaml.safe_dump({"id": "P1", **review}))
    row = module_process_conformance(module(), gene_index=index, graph=GRAPH)["rows"][0]
    assert (row["status"], row["severity"]) == ("PROCESS_SUPPORTED_BY_REVIEW", "info")


@pytest.mark.parametrize(
    "review",
    [
        # A removed or negated row is not an assertion that the process holds.
        {
            "existing_annotations": [
                {"term": {"id": PLC}, "review": {"action": "REMOVE"}}
            ]
        },
        {
            "existing_annotations": [
                {"term": {"id": PLC}, "negated": True, "review": {"action": "ACCEPT"}}
            ]
        },
        # The term being replaced is not what the review asserts.
        {
            "existing_annotations": [
                {
                    "term": {"id": PLC},
                    "review": {
                        "action": "MODIFY",
                        "proposed_replacement_terms": [{"id": CAMP}],
                    },
                }
            ]
        },
    ],
)
def test_a_review_that_does_not_assert_the_process_changes_nothing(tmp_path, review):
    index = write_gene(tmp_path, "P1", [("involved_in", ADRENERGIC_CAMP, "IDA")])
    index["P1"].write_text(yaml.safe_dump({"id": "P1", **review}))
    assert status(module(), index) == ["SIBLING_PROCESS_ONLY"]


def test_other_statuses_are_informational(tmp_path):
    index = write_gene(tmp_path, "P1", [("involved_in", UNRELATED, "IDA")])
    row = module_process_conformance(module(), gene_index=index, graph=GRAPH)["rows"][0]
    assert row["severity"] == "info"


def test_annoton_process_overrides_the_inherited_concept(tmp_path):
    """An annoton that states its own process is judged against that process."""
    index = write_gene(tmp_path, "P1", [("involved_in", ADRENERGIC_CAMP, "IDA")])
    assert status(module(processes=[CAMP]), index) == ["PROCESS_SUPPORTED"]


def test_no_goa_file_and_no_process_are_not_judged(tmp_path):
    index = write_gene(tmp_path, "P1", [("involved_in", ADRENERGIC_CAMP, "IDA")])
    # Exemplar with no local gene folder: nothing to compare.
    assert status(module("P2"), index) == ["GOA_UNAVAILABLE"]
    # No process stated anywhere above the annoton: nothing is asserted.
    assert status(module(concept=None), index) == []
    # A cellular-component concept (a complex module) is not a process claim.
    assert status(module(concept=COMPLEX), index) == []


def test_load_goa_process_rows_keeps_only_positive_process_rows(tmp_path):
    index = write_gene(
        tmp_path,
        "P1",
        [("involved_in", PLC, "IMP"), ("NOT|involved_in", CAMP, "IDA")],
    )
    goa = index["P1"].parent / "P1-goa.tsv"
    with goa.open("a") as handle:
        handle.write(
            "UniProtKB\tP1\tSYM\tenables\tGO:0004930\tname\tmolecular_function\t"
            "ECO:0\tIDA\tPMID:1\t\t9606\tHomo sapiens\tX\tname\t2025\n"
        )
    assert load_goa_process_rows(goa) == ((PLC, "IMP"),)


@pytest.mark.integration
def test_adrb2_is_flagged_against_plc_activating_signaling():
    """The real case, against the local GO snapshot and the ADRB2 GOA file."""
    genes = Path(__file__).resolve().parents[1] / "genes"
    review = genes / "human" / "ADRB2" / "ADRB2-ai-review.yaml"
    if not review.exists():
        pytest.skip("ADRB2 gene folder not present")
    result = module_process_conformance(module("P07550"), gene_index={"P07550": review})
    assert [(row["status"], row["severity"]) for row in result["rows"]] == [
        ("SIBLING_PROCESS_ONLY", "warning")
    ]
