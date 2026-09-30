"""Regression coverage for wrapped UniProt alternative-product fields."""
from ai_gene_review.etl.gene import _extract_alternative_products


def test_atxn2_wrapped_sequence_preserves_all_six_variants():
    # Exact alternative-products section of the normal Q99700 record.
    record = """CC   -!- ALTERNATIVE PRODUCTS:
CC       Event=Alternative splicing; Named isoforms=5;
CC       Name=1;
CC         IsoId=Q99700-1; Sequence=Displayed;
CC       Name=2;
CC         IsoId=Q99700-2; Sequence=VSP_011575, VSP_011577;
CC       Name=3;
CC         IsoId=Q99700-3; Sequence=VSP_011574, VSP_011576, VSP_011578,
CC                                  VSP_011579, VSP_011580, VSP_011581;
CC       Name=4;
CC         IsoId=Q99700-4; Sequence=VSP_011582;
CC       Name=5;
CC         IsoId=Q99700-5; Sequence=VSP_057285, VSP_057286, VSP_057287;
CC   -!- TISSUE SPECIFICITY: Expressed in the brain.
"""
    products = _extract_alternative_products(record, "Q99700")
    assert [p["id"] for p in products] == [f"Q99700-{i}" for i in range(1, 6)]
    assert products[2]["sequence_note"] == (
        "VSP_011574, VSP_011576, VSP_011578, VSP_011579, VSP_011580, VSP_011581"
    )
    assert "sequence_note" not in products[0]
    assert products[3] == {"name": "4", "id": "Q99700-4", "sequence_note": "VSP_011582"}


def test_wrapping_does_not_change_names_synonyms_or_sequence_fields():
    unwrapped = """CC   -!- ALTERNATIVE PRODUCTS:
CC       Event=Alternative splicing; Named isoforms=2;
CC       Name=Long form; Synonyms=alpha, beta;
CC         IsoId=Q99700-1; Sequence=Displayed;
CC       Name=Short form;
CC         IsoId=Q99700-2; Sequence=VSP_011575, VSP_011577;
CC   -!- INTERACTION:
CC       Name=Not an isoform; IsoId=Q99700-99; Sequence=External;
"""
    wrapped = unwrapped.replace("Name=Long form", "Name=Long\nCC       form")
    wrapped = wrapped.replace("Synonyms=alpha, beta", "Synonyms=alpha,\nCC         beta")
    wrapped = wrapped.replace("; Sequence=", ";\nCC         Sequence=")
    expected = [
        {"name": "Long form (alpha, beta)", "id": "Q99700-1"},
        {"name": "Short form", "id": "Q99700-2", "sequence_note": "VSP_011575, VSP_011577"},
    ]
    assert _extract_alternative_products(unwrapped, "Q99700") == expected
    assert _extract_alternative_products(wrapped, "Q99700") == expected


def test_missing_or_single_alternative_product_is_not_reported():
    assert _extract_alternative_products("CC   -!- FUNCTION: Example.\n", "Q99700") == []
    single = """CC   -!- ALTERNATIVE PRODUCTS:
CC       Event=Alternative splicing; Named isoforms=1;
CC       Name=1;
CC         IsoId=Q99700-1; Sequence=Displayed;
"""
    assert _extract_alternative_products(single, "Q99700") == []


def test_unsequenced_isoform_is_retained_without_becoming_displayed():
    record = """CC   -!- ALTERNATIVE PRODUCTS:
CC       Event=Alternative splicing; Named isoforms=2;
CC       Name=1;
CC         IsoId=Q99700-1; Sequence=Displayed;
CC       Name=5 {ECO:0000305};
CC         IsoId=Q99700-5;
CC         Sequence=Not described;
"""
    assert _extract_alternative_products(record, "Q99700")[1] == {
        "name": "5 {ECO:0000305}", "id": "Q99700-5", "sequence_note": "Not described"
    }
