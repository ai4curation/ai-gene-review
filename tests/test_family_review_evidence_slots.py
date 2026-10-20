"""Every FamilyReview claim class that states a verdict carries checkable quotes.

Node assessments and subfamily divergence calls used to have no ``supported_by``
slot, so their evidence could live only in free-text reasons that the reference
validator never reads. These tests keep the slot on each class that makes a claim.
"""

from pathlib import Path

import pytest
from linkml_runtime.utils.schemaview import SchemaView

SCHEMA = Path(__file__).resolve().parents[1] / "src/ai_gene_review/schema/family_review.yaml"


@pytest.mark.parametrize(
    "class_name",
    ["NodeAssessment", "Subfamily", "TermAssessment", "MemberException", "FunctionRequirement"],
)
def test_claim_classes_have_supported_by(class_name):
    sv = SchemaView(str(SCHEMA))
    assert "supported_by" in sv.class_slots(class_name), class_name


def test_supported_by_is_a_list_of_supporting_text():
    sv = SchemaView(str(SCHEMA))
    slot = sv.induced_slot("supported_by", "NodeAssessment")
    assert slot.range == "SupportingText"
    assert slot.multivalued
