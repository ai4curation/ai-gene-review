"""Negative evidence needs complete predictions, scoped identity and counterexamples."""
import pytest

from ai_gene_review.tools.function_requirements import ProteinFeatures, load_rules
from ai_gene_review.tools.topology_flags import (
    evidence_state, prediction_features, protein_flags, retained_ld_claims, transporter_flag,
    taxon_flags, intramembrane_flags,
)


def features(tm=1, interpro=()):
    return ProteinFeatures("P00001", frozenset(interpro), tm)


@pytest.mark.parametrize("geometry,verdict", [
    ("NONSPANNING", "CORROBORATED_TOPOLOGY_CONFLICT"),
    ("SPANNING", "PREDICTOR_COUNTEREXAMPLE"),
    ("UNRESOLVED", "REVIEW_CONFLICT"),
])
def test_literature_can_challenge_either_source(geometry, verdict):
    result = protein_flags(features(), {"tm": 0, "surface": 1}, geometry, [])
    assert result[0]["verdict"] == verdict


def test_interfacial_and_spanning_regions_can_coexist():
    assert protein_flags(features(), {"tm": 1, "surface": 1}, "UNRESOLVED", []) == []


def test_human_chloroplast_constraint_does_not_exclude_plant_compartments():
    assert taxon_flags(["9606"], ["Chloroplast outer membrane"])[0]["verdict"] == "TAXON_CONFLICT"
    assert taxon_flags(["3702"], ["Chloroplast outer membrane"]) == []
    assert taxon_flags(["9606"], ["Mitochondrial outer membrane"]) == []
    assert taxon_flags([], ["Chloroplast inner membrane"]) == []


def test_intramembrane_conflict_requires_overlapping_residues():
    regions = [{"start": 10, "end": 30}]
    assert intramembrane_flags(regions, [{"name": "TMhelix", "start": 40, "end": 60}]) == []
    assert intramembrane_flags(regions, [{"name": "interfacial", "start": 12, "end": 25}]) == []
    for name in ("TMhelix", "Beta sheet"):
        flag = intramembrane_flags(regions, [{"name": name, "start": 20, "end": 40}])[0]
        assert flag["rule_id"] == "DTM2:0004"
        assert flag["overlapping_regions"][0]["uniprot_intramembrane"] == regions[0]


def test_no_tm_alone_is_not_a_topology_conflict():
    assert protein_flags(features(), {"tm": 0, "surface": 0}, "UNRESOLVED", []) == []


@pytest.mark.parametrize("name,code,tm", [("Beta sheet", "B", 1), ("TMhelix", "M", 1),
                                           ("interfacial", "F", 0), ("signal", "S", 0)])
def test_alpha_beta_and_nonspanning_predictions(name, code, tm):
    prediction = {"topology_string": code * 3, "segments": [{"name": name, "start": 1, "end": 3}]}
    assert prediction_features(prediction, "AAA")["tm"] == tm


@pytest.mark.parametrize("prediction", [
    {}, {"topology_string": "FF", "segments": [{"name": "interfacial", "start": 1, "end": 2}]},
    {"topology_string": "FFF", "segments": [{"name": "interfacial", "start": 2, "end": 3}]},
    {"topology_string": "MMM", "segments": [{"name": "interfacial", "start": 1, "end": 3}]},
])
def test_missing_partial_and_inconsistent_predictions_are_not_absence(prediction):
    with pytest.raises(ValueError):
        prediction_features(prediction, "AAA")


def test_literature_requires_sequence_identity_and_context():
    entry = dict(sequence_sha256="abc", scope="canonical_chain_in_assayed_context",
                 geometry="NONSPANNING", supported_by=["PMID:1"], context="ER membrane")
    assert evidence_state(entry, "abc") == "NONSPANNING"
    with pytest.raises(ValueError):
        evidence_state(entry, "different isoform")
    with pytest.raises(ValueError):
        evidence_state(dict(entry, context=""), "abc")


def test_lipid_droplet_plus_span_is_context_question():
    claims = [{"reference": "PMID:1"}]
    assert protein_flags(features(0), {"tm": 0, "surface": 1}, "UNRESOLVED", claims) == []
    flags = protein_flags(features(), {"tm": 1, "surface": 1}, "UNRESOLVED", claims)
    assert [f["verdict"] for f in flags] == ["CONTEXT_CHECK"]


@pytest.mark.parametrize("action,qualifier,n", [("ACCEPT", "located_in", 1),
    ("REMOVE", "located_in", 0), ("ACCEPT", "NOT|located_in", 0)])
def test_only_retained_positive_location_claims(action, qualifier, n):
    review = {"existing_annotations": [dict(term={"id": "GO:0005811"},
        qualifier=qualifier, review={"action": action}, original_reference_id="PMID:1", evidence_type="IDA")]}
    assert len(retained_ld_claims(review)) == n


def test_location_qualifier_is_preserved_and_refinement_can_resolve_flag():
    annotation = dict(term={"id": "GO:0005811"}, qualifier="colocalizes_with",
                      review={"action": "ACCEPT"}, original_reference_id="PMID:1", evidence_type="IDA")
    assert retained_ld_claims({"existing_annotations": [annotation]})[0]["qualifier"] == "colocalizes_with"
    annotation["review"] = {"action": "MODIFY", "proposed_replacement_terms": [{"id": "GO:0160259"}]}
    assert retained_ld_claims({"existing_annotations": [annotation]}) == []


def test_transporter_scope_and_family_escape_are_preserved():
    rule = next(r for r in load_rules() if r["id"] == "FRR:0004")
    closure = {"GO:0022857"}  # Caller supplies descendants minus exempt subtrees.
    row = {"QUALIFIER": "enables", "GO TERM": "GO:0022857", "GO NAME": "transporter",
           "REFERENCE": "PMID:1", "GO EVIDENCE CODE": "IDA"}
    pred = {"tm": 0, "surface": 1}
    for qualifier in ("NOT|enables", "contributes_to"):
        assert transporter_flag(rule, closure, dict(row, QUALIFIER=qualifier), features(), pred, "UNRESOLVED") is None
    assert transporter_flag(rule, closure, dict(row, **{"GO TERM": "GO:0015399"}), features(), pred, "UNRESOLVED") is None
    family = rule["requires_any_of"][0]["id"]
    flag = transporter_flag(rule, closure, row, features(0, [family]), pred, "UNRESOLVED")
    assert flag["original_frr_verdict"] == "SATISFIED"
    assert flag["verdict"] == "REVIEW_CONFLICT"
    flag = transporter_flag(rule, closure, row, features(0), pred, "SPANNING")
    assert flag["verdict"] == "PREDICTOR_COUNTEREXAMPLE"
