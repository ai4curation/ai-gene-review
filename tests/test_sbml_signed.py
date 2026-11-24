"""Tests for reading signed regulatory edges out of SBML kinetic models.

The small models below are real SBML documents built with libsbml, not mocks:
each test writes one to ``tmp_path`` and reads it back through the same code
path used for BioModels files.
"""

from pathlib import Path

import pytest
import yaml

libsbml = pytest.importorskip("libsbml")

from ai_gene_review.module_boolean import SignedEdge  # noqa: E402
from ai_gene_review.sbml_signed import (  # noqa: E402
    SbmlEntityMap,
    compare_module_to_sbml,
    format_comparison,
    require_sbml_dependencies,
    sbml_signed_edges,
)

ROOT = Path(__file__).resolve().parent.parent
KHOLODENKO = ROOT / "models" / "kinetic" / "biomd0000000010"


def test_missing_dependency_names_the_package_and_install_command():
    """A plain install without libsbml/sympy must fail with an actionable message."""
    with pytest.raises(RuntimeError, match="no_such_module_xyz.*install"):
        require_sbml_dependencies(modules={"no_such_module_xyz": "no-such-package"})
    require_sbml_dependencies()  # the real dependencies are present in this environment


def _write_model(
    path: Path,
    species: list[str],
    parameters: dict[str, float],
    reactions: list[tuple[str, list[str], list[str], list[str], str]],
) -> Path:
    """Write an SBML L3V2 model: reactions are (id, reactants, products, modifiers, rate)."""
    doc = libsbml.SBMLDocument(3, 2)
    model = doc.createModel()
    model.setId("test_model")
    comp = model.createCompartment()
    comp.setId("cell")
    comp.setSize(1.0)
    comp.setConstant(True)
    for sid in species:
        s = model.createSpecies()
        s.setId(sid)
        s.setCompartment("cell")
        s.setInitialConcentration(1.0)
        s.setHasOnlySubstanceUnits(False)
        s.setBoundaryCondition(False)
        s.setConstant(False)
    for pid, value in parameters.items():
        p = model.createParameter()
        p.setId(pid)
        p.setValue(value)
        p.setConstant(True)
    for rid, reactants, products, modifiers, rate in reactions:
        r = model.createReaction()
        r.setId(rid)
        r.setReversible(False)
        for sid in reactants:
            ref = r.createReactant()
            ref.setSpecies(sid)
            ref.setStoichiometry(1.0)
            ref.setConstant(True)
        for sid in products:
            ref = r.createProduct()
            ref.setSpecies(sid)
            ref.setStoichiometry(1.0)
            ref.setConstant(True)
        for sid in modifiers:
            r.createModifier().setSpecies(sid)
        law = r.createKineticLaw()
        math = libsbml.parseL3Formula(rate)
        assert math is not None, rate
        law.setMath(math)
    assert libsbml.writeSBMLToFile(doc, str(path)) == 1
    return path


@pytest.fixture
def kinase_model(tmp_path: Path) -> Path:
    """Kinase K phosphorylates substrate S; inhibitor I slows it; S_P is dephosphorylated."""
    return _write_model(
        tmp_path / "kinase.xml",
        species=["K", "S", "S_P", "I"],
        parameters={"k": 1.0, "Km": 0.5, "Ki": 0.2, "V": 0.3, "Kd": 0.4},
        reactions=[
            (
                "phos",
                ["S"],
                ["S_P"],
                ["K", "I"],
                "cell * k * K * S / ((Km + S) * (1 + I / Ki))",
            ),
            ("dephos", ["S_P"], ["S"], [], "cell * V * S_P / (Kd + S_P)"),
        ],
    )


KINASE_MAP = SbmlEntityMap(
    entity_of={"K": "KIN", "S": "SUB", "S_P": "SUB", "I": "INHIBITOR"},
    level_of={"S": 0, "S_P": 1},
)


def test_catalyst_and_inhibitor_signs(kinase_model: Path):
    result = sbml_signed_edges(kinase_model, KINASE_MAP)
    assert result.edges == {
        SignedEdge("KIN", "SUB", "+"),
        SignedEdge("INHIBITOR", "SUB", "-"),
    }


def test_effector_of_a_deactivating_reaction_has_its_sign_flipped(tmp_path: Path):
    """A phosphatase P that speeds up S_P -> S lowers SUB activity, so P -| SUB."""
    model = _write_model(
        tmp_path / "phosphatase.xml",
        species=["S", "S_P", "P"],
        parameters={"V": 1.0, "Kd": 0.4},
        reactions=[
            ("dephos", ["S_P"], ["S"], ["P"], "cell * V * P * S_P / (Kd + S_P)")
        ],
    )
    entity_map = SbmlEntityMap(
        entity_of={"S": "SUB", "S_P": "SUB", "P": "PPASE"}, level_of={"S": 0, "S_P": 1}
    )
    assert sbml_signed_edges(model, entity_map).edges == {
        SignedEdge("PPASE", "SUB", "-")
    }


def test_non_monotone_effector_gets_unknown_sign(tmp_path: Path):
    """An effector that activates at low and inhibits at high concentration is '?'."""
    model = _write_model(
        tmp_path / "biphasic.xml",
        species=["S", "S_P", "X"],
        parameters={"k": 1.0},
        reactions=[("phos", ["S"], ["S_P"], ["X"], "cell * k * S * X / (1 + X^2)")],
    )
    entity_map = SbmlEntityMap(
        entity_of={"S": "SUB", "S_P": "SUB", "X": "EFF"}, level_of={"S": 0, "S_P": 1}
    )
    result = sbml_signed_edges(model, entity_map)
    assert result.edges == {SignedEdge("EFF", "SUB", "?")}


def test_inactive_form_in_rate_law_is_reported_not_counted(tmp_path: Path):
    """An unphosphorylated (level 0) form in a rate law is not an activity effect."""
    model = _write_model(
        tmp_path / "inactive.xml",
        species=["S", "S_P", "K", "K_P"],
        parameters={"k": 1.0},
        reactions=[("phos", ["S"], ["S_P"], ["K", "K_P"], "cell * k * (K + K_P) * S")],
    )
    entity_map = SbmlEntityMap(
        entity_of={"S": "SUB", "S_P": "SUB", "K": "KIN", "K_P": "KIN"},
        level_of={"S": 0, "S_P": 1, "K": 0, "K_P": 1},
    )
    result = sbml_signed_edges(model, entity_map)
    assert result.edges == {SignedEdge("KIN", "SUB", "+")}
    assert any("K" in note and "inactive" in note for note in result.notes)


def test_reaction_that_changes_no_activity_yields_no_edge(tmp_path: Path):
    """Transport of an already-active form between two unmapped pools changes nothing."""
    model = _write_model(
        tmp_path / "nochange.xml",
        species=["A_P", "B_P", "K"],
        parameters={"k": 1.0},
        reactions=[("move", ["A_P"], ["B_P"], ["K"], "cell * k * K * A_P")],
    )
    entity_map = SbmlEntityMap(
        entity_of={"A_P": "ENT", "B_P": "ENT", "K": "KIN"},
        level_of={"A_P": 1, "B_P": 1},
    )
    result = sbml_signed_edges(model, entity_map)
    assert result.edges == set()
    assert any("move" in note for note in result.notes)


def test_enzyme_written_on_both_sides_is_an_effector(tmp_path: Path):
    """One-step catalysis E + S -> E + P: the enzyme's activity is unchanged, so it
    is not a target, but it drives the conversion and must yield E -> SUB."""
    model = _write_model(
        tmp_path / "catalysis.xml",
        species=["E", "S", "S_P"],
        parameters={"k": 1.0},
        reactions=[("cat", ["E", "S"], ["E", "S_P"], [], "cell * k * E * S")],
    )
    entity_map = SbmlEntityMap(
        entity_of={"E": "ENZ", "S": "SUB", "S_P": "SUB"}, level_of={"S": 0, "S_P": 1}
    )
    assert sbml_signed_edges(model, entity_map).edges == {SignedEdge("ENZ", "SUB", "+")}


@pytest.mark.parametrize("base", [2, 10])
def test_two_argument_log_is_base_then_value(tmp_path: Path, base: int):
    """SBML L3 log(b, x) is log base b of x, increasing in x for b > 1.

    libsbml writes base 10 back as ``log10(x)`` and keeps other bases as
    ``log(b, x)``, so the two cases exercise different parsing paths.
    """
    model = _write_model(
        tmp_path / "log.xml",
        species=["S", "S_P", "X"],
        parameters={"k": 1.0},
        reactions=[
            ("phos", ["S"], ["S_P"], ["X"], f"cell * k * S * log({base}, 1 + X)")
        ],
    )
    entity_map = SbmlEntityMap(
        entity_of={"S": "SUB", "S_P": "SUB", "X": "EFF"}, level_of={"S": 0, "S_P": 1}
    )
    assert sbml_signed_edges(model, entity_map).edges == {SignedEdge("EFF", "SUB", "+")}


def test_effector_whose_derivative_never_evaluates_is_reported(tmp_path: Path):
    """If every sample fails, the effector is noted rather than silently dropped."""
    model = _write_model(
        tmp_path / "unevaluable.xml",
        species=["S", "S_P", "X"],
        parameters={"k": 1.0},
        reactions=[("phos", ["S"], ["S_P"], ["X"], "cell * k * S * sqrt(-X)")],
    )
    entity_map = SbmlEntityMap(
        entity_of={"S": "SUB", "S_P": "SUB", "X": "EFF"}, level_of={"S": 0, "S_P": 1}
    )
    result = sbml_signed_edges(model, entity_map)
    assert result.edges == set()
    assert any(
        "X" in note and "could not be evaluated" in note for note in result.notes
    )


def test_undetermined_model_sign_is_flagged_in_the_report(tmp_path: Path):
    """A sampled '?' counts as agreement in the diff, so the report must say so."""
    model = _write_model(
        tmp_path / "biphasic.xml",
        species=["S", "S_P", "X"],
        parameters={"k": 1.0},
        reactions=[("phos", ["S"], ["S_P"], ["X"], "cell * k * S * X / (1 + X^2)")],
    )
    module = tmp_path / "toy.yaml"
    module.write_text(
        yaml.safe_dump(
            {
                "module": {
                    "id": "toy",
                    "parts": [
                        {"node": {"id": "x_node", "label": "Effector"}},
                        {"node": {"id": "s_node", "label": "Substrate"}},
                    ],
                    "connections": [
                        {
                            "source": "x_node",
                            "target": "s_node",
                            "connection_type": "CAUSES",
                        }
                    ],
                }
            }
        )
    )
    mapping = tmp_path / "mapping.yaml"
    mapping.write_text(
        yaml.safe_dump(
            {
                "modules": {"toy": {"EFF": "x_node", "SUB": "s_node"}},
                "external": {"EFF": "X", "SUB": ["S", "S_P"]},
                "activity_levels": {"S": 0, "S_P": 1},
            }
        )
    )
    comparison = compare_module_to_sbml(module, model, mapping, seed=3, samples=32)
    assert {str(e) for e in comparison.diff.agree} == {"EFF -> SUB"}
    report = format_comparison(comparison)
    assert "model sign undetermined" in report
    assert "seed=3" in report and "samples=32" in report


# ---------------------------------------------------------------------------
# Kholodenko 2000 (BIOMD0000000010) against the curated ERK cascade module
# ---------------------------------------------------------------------------


def test_kholodenko_edges_include_the_erk_to_raf_feedback():
    entity_map = SbmlEntityMap.from_mapping_file(KHOLODENKO / "mapping_to_modules.yaml")
    result = sbml_signed_edges(KHOLODENKO / "model.xml", entity_map)
    assert result.edges == {
        SignedEdge("RAF", "MEK", "+"),
        SignedEdge("MEK", "ERK", "+"),
        SignedEdge("ERK", "RAF", "-"),
    }


def test_kholodenko_agrees_with_erk_cascade_module():
    report = compare_module_to_sbml(
        ROOT / "modules" / "erk_cascade.yaml",
        KHOLODENKO / "model.xml",
        KHOLODENKO / "mapping_to_modules.yaml",
    )
    diff = report.diff
    assert {str(e) for e in diff.agree} == {"RAF -> MEK", "MEK -> ERK", "ERK -| RAF"}
    assert not diff.sign_conflict
    assert not diff.right_only
    assert not diff.left_only
