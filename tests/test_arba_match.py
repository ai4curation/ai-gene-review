"""Tests for evaluating ARBA rule conditions against proteins.

The fixtures are the two versions of ARBA00086692 seen in 2026: the 2026_03
release served a Glires/fabids-only rule that no bacterium can satisfy, and the
2026_04 release serves the 2026-07-18 edit whose first set has no taxon
condition. Q88KS6 (Pseudomonas putida PP_2213) fails the first and matches the
second.
"""

import json

import pytest
from typer.testing import CliRunner

from ai_gene_review.cli import app
from ai_gene_review.curated_rules import ProteinFeatures
from ai_gene_review.etl.arba import ARBARule
from ai_gene_review.etl.arba_match import (
    UniProtFeatureClient,
    arba_goa_rows,
    check_goa_rows,
    evaluate_rule,
    load_status,
)


def _cond(ctype, value, cv_id=None, negative=False):
    cv = {"value": value, "cvId": cv_id} if cv_id else {"value": value}
    return {"type": ctype, "conditionValues": [cv], "isNegative": negative}


def _rule(rule_id, sets, modified):
    return ARBARule.from_json(
        {
            "uniRuleId": rule_id,
            "mainRule": {
                "conditionSets": [{"conditions": s} for s in sets],
                "annotations": [{"annotationType": "ANNOTATION", "dbReference": {"database": "GO", "id": "GO:0031956"}}],
            },
            "modifiedDate": modified,
        }
    )


RULE_2026_03 = _rule(
    "ARBA00086692",
    [
        [
            _cond("FunFam id", "3.30.300.30:FF:000005"),
            _cond("FunFam id", "3.40.50.12780:FF:000007"),
            _cond("taxon", "Glires", "314147"),
        ],
        [_cond("FunFam id", "3.30.300.30:FF:000008"), _cond("taxon", "fabids", "91835")],
    ],
    "2025-03-21",
)

RULE_2026_04 = _rule(
    "ARBA00086692",
    [
        [_cond("InterPro id", "IPR000873"), _cond("InterPro id", "IPR025110"), _cond("InterPro id", "IPR051087")],
        [
            _cond("FunFam id", "3.30.300.30:FF:000005"),
            _cond("FunFam id", "3.40.50.12780:FF:000007"),
            _cond("taxon", "Eukaryota", "2759"),
        ],
        [_cond("FunFam id", "3.30.300.30:FF:000008"), _cond("taxon", "fabids", "91835")],
    ],
    "2026-07-18",
)


@pytest.fixture
def q88ks6():
    lineage = ["131567", "2", "3379134", "1224", "1236", "72274", "135621", "286", "136845", "303", "160488"]
    return ProteinFeatures(
        signatures={
            "INTERPRO": {"IPR045851", "IPR025110", "IPR020845", "IPR000873", "IPR042099", "IPR051087"},
            "PANTHER": {"PTHR43605", "PTHR43605:SF10"},
            "FUNFAM": {"3.30.300.30:FF:000005"},
        },
        taxon_ids={f"NCBITaxon:{t}" for t in lineage},
    )


def test_old_rule_version_fails_on_taxon(q88ks6):
    match = evaluate_rule(RULE_2026_03, q88ks6)
    assert not match.matched
    assert match.closest_failure == "PARTIAL_SIGNATURE"
    # Set 0 has FF:000005 but not FF:000007, and the taxon fails.
    assert [c.holds for c in match.sets[0].conditions] == [True, False, False]


def test_new_rule_version_matches_via_taxon_free_set(q88ks6):
    match = evaluate_rule(RULE_2026_04, q88ks6)
    assert match.matched
    assert match.matching_sets == [0]


@pytest.mark.parametrize(
    "funfam,lineage,expected",
    [
        ({"3.30.300.30:FF:000008"}, {"NCBITaxon:2"}, "TAXON_ONLY"),
        ({"3.30.300.30:FF:000008"}, {"NCBITaxon:91835"}, None),
        (set(), {"NCBITaxon:91835"}, "NO_SIGNATURE"),
    ],
)
def test_closest_failure_kinds(funfam, lineage, expected):
    rule = _rule("ARBA1", [[_cond("FunFam id", "3.30.300.30:FF:000008"), _cond("taxon", "fabids", "91835")]], "2025-01-01")
    features = ProteinFeatures({"FUNFAM": funfam}, lineage)
    assert evaluate_rule(rule, features).closest_failure == expected


def test_partial_signature():
    rule = _rule("ARBA1", [[_cond("InterPro id", "IPR1"), _cond("InterPro id", "IPR2")]], "2025-01-01")
    features = ProteinFeatures({"INTERPRO": {"IPR1"}}, {"NCBITaxon:1"})
    assert evaluate_rule(rule, features).closest_failure == "PARTIAL_SIGNATURE"


def test_multi_value_condition_needs_any_value():
    rule = ARBARule.from_json(
        {
            "uniRuleId": "ARBA1",
            "mainRule": {
                "conditionSets": [
                    {"conditions": [{"type": "InterPro id", "conditionValues": [{"value": "IPR1"}, {"value": "IPR2"}]}]}
                ],
                "annotations": [],
            },
            "modifiedDate": "2025-01-01",
        }
    )
    assert evaluate_rule(rule, ProteinFeatures({"INTERPRO": {"IPR2"}}, set())).matched


def test_negated_condition_blocks_match():
    rule = _rule("ARBA1", [[_cond("InterPro id", "IPR1"), _cond("PANTHER id", "PTHR9", negative=True)]], "2025-01-01")
    with_family = ProteinFeatures({"INTERPRO": {"IPR1"}, "PANTHER": {"PTHR9", "PTHR9:SF1"}}, {"NCBITaxon:1"})
    without = ProteinFeatures({"INTERPRO": {"IPR1"}, "PANTHER": {"PTHR8"}}, {"NCBITaxon:1"})
    assert not evaluate_rule(rule, with_family).matched
    assert evaluate_rule(rule, without).matched


@pytest.mark.parametrize(
    "rule,load_date,expected",
    [
        (RULE_2026_04, "20260727", "MATCH"),
        (RULE_2026_03, "20260727", "MISMATCH"),
        (RULE_2026_03, "20250101", "RULE_EDITED_SINCE_LOAD"),
    ],
)
def test_load_status(q88ks6, rule, load_date, expected):
    assert load_status(evaluate_rule(rule, q88ks6), load_date) == expected


GOA_HEADER = [
    "GENE PRODUCT DB", "GENE PRODUCT ID", "SYMBOL", "QUALIFIER", "GO TERM", "GO NAME", "GO ASPECT",
    "ECO ID", "GO EVIDENCE CODE", "REFERENCE", "WITH/FROM", "TAXON ID", "TAXON NAME", "ASSIGNED BY",
    "GENE NAME", "DATE",
]


def _goa_row(acc, go, reference, with_from, date):
    return [
        "UniProtKB", acc, "PP_2213", "enables", go, "term", "molecular_function", "ECO:0000256", "IEA",
        reference, with_from, "160488", "Pseudomonas putida", "UniProt", "AMP-binding protein", date,
    ]


@pytest.fixture
def goa_file(tmp_path):
    rows = [
        _goa_row("Q88KS6", "GO:0031956", "GO_REF:0000117", "ARBA:ARBA00086692", "20260727"),
        _goa_row("Q88KS6", "GO:0016405", "GO_REF:0000117", "ARBA:ARBA00099999", "20260616"),
        _goa_row("Q88KS6", "GO:0004321", "GO_REF:0000118", "PANTHER:PTN000644270", "20260727"),
        _goa_row("Q00000", "GO:0005737", "GO_REF:0000117", "ARBA:ARBA00086692", "20260727"),
    ]
    path = tmp_path / "PP_2213-goa.tsv"
    path.write_text("\n".join("\t".join(r) for r in [GOA_HEADER, *rows]) + "\n")
    return path


def test_check_goa_rows(goa_file, q88ks6):
    rows = arba_goa_rows(goa_file)
    assert len(rows) == 3  # the GO_REF:0000118 TreeGrafter row is skipped
    rules = {"ARBA00086692": RULE_2026_04, "ARBA00099999": None}
    checks = check_goa_rows(rows, rules, {"Q88KS6": q88ks6})
    assert [(c.go_id, c.status) for c in checks] == [
        ("GO:0031956", "MATCH"),
        ("GO:0016405", "RULE_NOT_FOUND"),
        ("GO:0005737", "PROTEIN_NOT_FOUND"),
    ]


def test_check_goa_rows_old_rule_is_a_mismatch(goa_file, q88ks6):
    rows = arba_goa_rows(goa_file)[:1]
    [check] = check_goa_rows(rows, {"ARBA00086692": RULE_2026_03}, {"Q88KS6": q88ks6})
    assert check.status == "MISMATCH"
    assert check.matches[0].closest_failure == "PARTIAL_SIGNATURE"


# Integration tests: live UniProt and ARBA, replayed from VCR cassettes.


@pytest.mark.integration
def test_uniprot_features_q88ks6():
    protein = UniProtFeatureClient().proteins(["Q88KS6"])["Q88KS6"]
    assert protein.taxon_id == "160488"
    assert "NCBITaxon:2" in protein.features.taxon_ids  # Bacteria
    assert "IPR051087" in protein.features.signatures["INTERPRO"]
    assert "PTHR43605" in protein.features.signatures["PANTHER"]


def _write_stale_cache(cache_dir):
    """Cache the 2026_03 version of ARBA00086692, which Q88KS6 cannot satisfy."""
    rule_dir = cache_dir / "ARBA00086692"
    rule_dir.mkdir(parents=True)
    (rule_dir / "ARBA00086692.json").write_text(json.dumps(RULE_2026_03.to_json()))


@pytest.mark.integration
def test_cli_arba_check(tmp_path):
    _write_stale_cache(tmp_path)
    result = CliRunner().invoke(
        app, ["arba-check", "Q88KS6", "ARBA00086692", "--cache-dir", str(tmp_path)]
    )
    assert result.exit_code == 0, result.output
    assert "Q88KS6 (taxon 160488" in result.output
    # The stale cached copy is ignored: the current rule matches via its taxon-free set.
    assert "ARBA00086692 (modified 2026-07-18): matches via set 0" in result.output


@pytest.mark.integration
def test_cli_arba_check_goa(goa_file, tmp_path):
    _write_stale_cache(tmp_path)
    result = CliRunner().invoke(app, ["arba-check-goa", str(goa_file), "--cache-dir", str(tmp_path)])
    assert result.exit_code == 0, result.output
    statuses = {
        tuple(line.split()[:3]) for line in result.output.splitlines() if line and not line.startswith(" ")
    }
    # The stale cached copy is ignored, so the July row matches the current rule.
    assert ("MATCH", "Q88KS6", "GO:0031956") in statuses
    assert ("RULE_NOT_FOUND", "Q88KS6", "GO:0016405") in statuses
    assert ("PROTEIN_NOT_FOUND", "Q00000", "GO:0005737") in statuses
