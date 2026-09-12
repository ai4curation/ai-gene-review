"""Tests for the module-node `conforms_to` / `Conformance` schema construct.

These exercise the schema addition that lets a sub-bundle node declare it is an
instance of a reusable template motif (e.g. the three-tier MAP kinase relay),
optionally recording deviations. Offline: pure pydantic + SchemaView.
"""

from pathlib import Path

import pytest
from pydantic import ValidationError

from ai_gene_review.datamodel.gene_review_model import (
    Conformance,
    ConformanceStatusEnum,
    ModuleNode,
)

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SCHEMA = PROJECT_ROOT / "src" / "ai_gene_review" / "schema" / "gene_review.yaml"


def test_conformance_requires_template():
    with pytest.raises(ValidationError):
        Conformance()  # template is required


def test_conformance_minimal_one_liner():
    c = Conformance(template="mapk_relay")
    assert c.template == "mapk_relay"
    assert c.status is None
    assert c.deviations is None


def test_conformance_with_deviations_and_notes():
    c = Conformance(
        template="mapk_relay#map2k",
        status=ConformanceStatusEnum.WITH_DEVIATIONS,
        deviations=["single MAP2K rather than the MEK1/MEK2 pair"],
        notes="single MAP2K paralog in this organism",
    )
    assert c.status == ConformanceStatusEnum.WITH_DEVIATIONS
    assert c.deviations == ["single MAP2K rather than the MEK1/MEK2 pair"]


def test_conformance_status_enum_values():
    assert {e.value for e in ConformanceStatusEnum} == {
        "EXACT",
        "WITH_DEVIATIONS",
        "EXTENDS",
    }


def test_module_node_carries_conforms_to_list():
    """A bundle node groups its tiers in `parts` and conforms to a motif."""
    node = ModuleNode(
        id="erk_relay",
        label="ERK kinase relay",
        conforms_to=[Conformance(template="mapk_relay")],
    )
    assert len(node.conforms_to) == 1
    assert node.conforms_to[0].template == "mapk_relay"


def test_module_node_conforms_to_defaults_none():
    node = ModuleNode(id="n", label="bare node")
    assert node.conforms_to is None


def test_schema_defines_conformance_on_module_node():
    """conforms_to is a multivalued slot of ModuleNode ranged on Conformance."""
    from linkml_runtime.utils.schemaview import SchemaView  # type: ignore[import-untyped]

    sv = SchemaView(str(SCHEMA))
    slots = {s.name: s for s in sv.class_induced_slots("ModuleNode")}
    assert "conforms_to" in slots
    ct = slots["conforms_to"]
    assert ct.multivalued is True
    assert ct.range == "Conformance"
