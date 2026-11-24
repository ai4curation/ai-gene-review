"""Tests for function requirement (NOT) rules.

Most tests are offline: rule evaluation, flat-file parsing, and a sweep over real gene
folders in this repository whose misannotations the rules were written to catch. The
acceptance test against GOA needs QuickGO and UniProt and is marked integration.
"""

from pathlib import Path

import pytest

from ai_gene_review.tools.function_requirements import (
    RULES_PATH,
    ProteinFeatures,
    Verdict,
    evaluate,
    load_rules,
    parse_uniprot_flatfile,
    parse_uniprot_tsv,
    sweep_genes,
)

REPO = Path(__file__).resolve().parents[1]
GENES = REPO / "genes"

RULE = {
    "id": "FRR:9999",
    "term": {"id": "GO:0003989", "label": "acetyl-CoA carboxylase activity"},
    "include_descendants": False,
    "qualifiers": ["enables"],
    "requires_any_of": [{"id": "IPR000089", "label": "Biotin/lipoyl attachment"}],
    "excluded_by_any_of": [{"id": "IPR017556", "label": "malonate decarboxylase beta"}],
    "strength": "REQUIRED",
}
TM_RULE = {
    "id": "FRR:9998",
    "term": {"id": "GO:0022857", "label": "transmembrane transporter activity"},
    "include_descendants": False,
    "qualifiers": ["enables"],
    "requires_transmembrane_segment": True,
    "strength": "REQUIRED",
}


def _features(interpro=(), tm=0):
    return ProteinFeatures(
        accession="P00001", interpro=frozenset(interpro), transmembrane_segments=tm
    )


@pytest.mark.parametrize(
    "rule,features,expected",
    [
        (RULE, _features(["IPR000089"]), Verdict.SATISFIED),
        (RULE, _features(["IPR999999"]), Verdict.MISSING_REQUIRED),
        (RULE, _features([]), Verdict.MISSING_REQUIRED),
        (RULE, _features(["IPR000089", "IPR017556"]), Verdict.EXCLUDED),
        (TM_RULE, _features([], tm=2), Verdict.SATISFIED),
        (TM_RULE, _features(["IPR000089"], tm=0), Verdict.MISSING_REQUIRED),
    ],
)
def test_evaluate(rule, features, expected):
    """A rule is satisfied by any required feature, and an excluding feature wins."""
    assert evaluate(rule, features) == expected


def test_parse_uniprot_flatfile():
    """InterPro cross-references and TRANSMEM features are read from a flat file."""
    text = "\n".join(
        [
            "ID   TEST_ECOLI   Reviewed;   100 AA.",
            "AC   P00001; Q00001;",
            "DR   InterPro; IPR000089; Biotin_lipoyl.",
            "DR   Pfam; PF00364; Biotin_lipoyl; 1.",
            "DR   InterPro; IPR011053; Single_hybrid_motif.",
            "FT   TRANSMEM        10..30",
            'FT                   /note="Helical"',
            "FT   TRANSMEM        40..60",
        ]
    )
    f = parse_uniprot_flatfile(text)
    assert f.accession == "P00001"
    assert f.interpro == {"IPR000089", "IPR011053"}
    assert f.transmembrane_segments == 2


def test_parse_uniprot_tsv():
    """UniProt REST TSV rows give the same features as the flat file."""
    tsv = (
        "Entry\tProtein names\tOrganism\tInterPro\tTransmembrane\n"
        "P00001\tTest protein\tE. coli\tIPR000089;IPR011053;\t"
        'TRANSMEM 10..30; /note="Helical"; TRANSMEM 40..60; /note="Helical"\n'
        "P00002\tSoluble\tE. coli\t\t\n"
    )
    rows = parse_uniprot_tsv(tsv)
    assert rows["P00001"][0].interpro == {"IPR000089", "IPR011053"}
    assert rows["P00001"][0].transmembrane_segments == 2
    assert rows["P00001"][1] == {"protein_name": "Test protein", "organism": "E. coli"}
    assert rows["P00002"][0].interpro == frozenset()


def test_rules_file_is_well_formed():
    """Every curated rule has a unique id and well-formed feature ids."""
    rules = load_rules(RULES_PATH)
    ids = [r["id"] for r in rules]
    assert len(ids) == len(set(ids))
    for r in rules:
        assert r.get("requires_any_of") or r.get("requires_transmembrane_segment"), r[
            "id"
        ]
        for f in r.get("requires_any_of", []) + r.get("excluded_by_any_of", []):
            assert f["id"].startswith("IPR") and len(f["id"]) == 9


@pytest.fixture(scope="module")
def sweep_rows():
    """Sweep three real gene folders whose misannotations motivated the pilot rules.

    The rule terms used here have no is_a descendants, so closures are given
    explicitly and the test needs no ontology download.
    """
    rules = [
        r
        for r in load_rules(RULES_PATH)
        if r["id"] in {"FRR:0001", "FRR:0002", "FRR:0006"}
    ]
    closures = {r["id"]: {r["term"]["id"]} for r in rules}
    dirs = [
        GENES / "ECOLI" / "ftsI",
        GENES / "METEA" / "mdcD",
        GENES / "ECOLI" / "traB",
    ]
    return sweep_genes(dirs, rules, closures)


@pytest.mark.parametrize(
    "gene,rule_id,verdict,review_action",
    [
        # FtsI (class B PBP) has no GT51/SEDS domain; the rows were removed by review.
        ("ECOLI/ftsI", "FRR:0001", Verdict.MISSING_REQUIRED, "REMOVE"),
        # MdcD has the carboxyltransferase fold but is a malonate decarboxylase subunit.
        ("METEA/mdcD", "FRR:0002", Verdict.EXCLUDED, "REMOVE"),
        # F-plasmid TraB has no ATPase fold; the IDA belongs to pKM101 TraB.
        ("ECOLI/traB", "FRR:0006", Verdict.MISSING_REQUIRED, "REMOVE"),
    ],
)
def test_sweep_flags_known_misannotations(
    sweep_rows, gene, rule_id, verdict, review_action
):
    """The sweep flags the motivating rows and joins the existing review action."""
    hits = [r for r in sweep_rows if r["gene"] == gene and r["rule_id"] == rule_id]
    assert hits, f"no {rule_id} hit for {gene}"
    assert {r["verdict"] for r in hits} == {verdict.value}
    assert review_action in {r["review_action"] for r in hits}


def test_sweep_skips_contributes_to_and_negated(tmp_path):
    """Rows outside the rule's qualifiers, and NOT rows, are never flagged."""
    gene = tmp_path / "ECOLI" / "xyz"
    gene.mkdir(parents=True)
    (gene / "xyz-uniprot.txt").write_text(
        "AC   P00001;\nDR   InterPro; IPR999999; Other.\n"
    )
    header = "\t".join(
        [
            "GENE PRODUCT DB",
            "GENE PRODUCT ID",
            "SYMBOL",
            "QUALIFIER",
            "GO TERM",
            "GO NAME",
            "GO ASPECT",
            "ECO ID",
            "GO EVIDENCE CODE",
            "REFERENCE",
            "WITH/FROM",
            "TAXON ID",
            "TAXON NAME",
            "ASSIGNED BY",
            "GENE NAME",
            "DATE",
        ]
    )

    def row(qual):
        return "\t".join(
            [
                "UniProtKB",
                "P00001",
                "xyz",
                qual,
                "GO:0003989",
                "x",
                "F",
                "ECO:0000314",
                "IDA",
                "PMID:1",
                "",
                "83333",
                "E. coli",
                "UniProt",
                "x",
                "20200101",
            ]
        )

    (gene / "xyz-goa.tsv").write_text(
        "\n".join([header, row("enables"), row("contributes_to"), row("NOT|enables")])
        + "\n"
    )
    rows = sweep_genes([gene], [RULE], {RULE["id"]: {"GO:0003989"}})
    assert [r["qualifier"] for r in rows] == ["enables"]
    assert rows[0]["review_action"] == ""


@pytest.mark.integration
def test_go_labels_match_ontology():
    """Rule term labels match the current GO label."""
    from oaklib import get_adapter

    go = get_adapter("sqlite:obo:go")
    for r in load_rules(RULES_PATH):
        assert go.label(r["term"]["id"]) == r["term"]["label"], r["id"]


@pytest.mark.integration
def test_exempt_terms_are_removed_from_closure():
    """Primary active transporters are outside the transmembrane transporter rule."""
    from ai_gene_review.tools.function_requirements import term_closures

    rules = [r for r in load_rules(RULES_PATH) if r["id"] == "FRR:0004"]
    closure = term_closures(rules)["FRR:0004"]
    assert "GO:0022857" in closure
    assert "GO:0015293" in closure  # symporter activity stays covered
    assert "GO:0008564" not in closure  # protein-exporting ATPase activity (SecA)
    assert "GO:0046933" not in closure  # ATP synthase activity


@pytest.mark.integration
def test_interpro_ids_and_labels_match_interpro():
    """Every InterPro id in the rules resolves, and its label is InterPro's name.

    A real-looking id with a plausible label is invisible otherwise, and silently
    changes what a rule flags.
    """
    import json
    import urllib.request

    # Keep every (id, label) pair, so a duplicated id with a divergent label is
    # still checked; fetch each id once.
    pairs = {
        (f["id"], f["label"])
        for r in load_rules(RULES_PATH)
        for f in r.get("requires_any_of", []) + r.get("excluded_by_any_of", [])
    }
    names = {}
    for ipr in sorted({ipr for ipr, _ in pairs}):
        url = f"https://www.ebi.ac.uk/interpro/api/entry/interpro/{ipr}/"
        with urllib.request.urlopen(url, timeout=60) as resp:
            names[ipr] = json.load(resp)["metadata"]["name"]["name"]
    mismatches = sorted(
        (ipr, label, names[ipr]) for ipr, label in pairs if names[ipr] != label
    )
    assert not mismatches, mismatches
