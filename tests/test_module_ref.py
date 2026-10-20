"""Tests for ``module_ref``: a module node realized by another module.

An umbrella module (e.g. an organelle lifecycle) composes existing modules by
reference instead of copying their annotons. These tests cover the three places
the reference has meaning:

* the satisfiability engine (``module_logic``), which inlines the referenced
  module so the umbrella is satisfied exactly when the referenced module is;
* QC/validation (``module_qc.module_ref_violations``), which requires that a
  reference resolves, that the referencing node is a pure stand-in, and that
  references do not form cycles;
* the leaf-grounding QC, which must not report a reference node as an
  ungrounded leaf.
"""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from ai_gene_review.datamodel.gene_review_model import ModuleNode
from ai_gene_review.module_boolean import module_to_boolean
from ai_gene_review.module_logic import (
    compile_module,
    compile_module_file,
    core_atoms,
    count_routes,
    enumerate_routes,
    is_satisfied,
    step_id,
    unsatisfied_steps,
)
from ai_gene_review.module_qc import (
    leaf_nodes_missing_representatives,
    module_ref_violations,
)
from ai_gene_review.render_modules import collect_module_ref_hrefs


def _annoton(aid: str, symbol: str) -> dict:
    return {"id": aid, "participant": {"gene": {"preferred_term": symbol}}}


def _write(modules_dir: Path, stem: str, module: dict) -> Path:
    path = modules_dir / f"{stem}.yaml"
    path.write_text(yaml.safe_dump({"id": f"MODULE:{stem}", "module": module}))
    return path


@pytest.fixture
def modules_dir(tmp_path: Path) -> Path:
    """Two leaf modules (fission with two routes, import with one step)."""
    _write(tmp_path, "fission", {"id": "fission", "parts": [
        {"node": {"id": "scission", "variant_sets": [{"id": "route", "variants": [
            {"id": "dynamin", "annotons": [_annoton("drp", "DRP1")]},
            {"id": "ftsz", "annotons": [_annoton("ftz", "FTSZ")]},
        ]}]}},
    ]})
    _write(tmp_path, "import", {"id": "import", "parts": [
        {"node": {"id": "translocase", "annotons": [_annoton("tom", "TOM40")]}},
        {"node": {"id": "receptor", "annotons": [_annoton("rec", "TOM20")]}},
    ]})
    _write(tmp_path, "respiration", {"id": "respiration", "annotons": [_annoton("cox", "COX1")]})
    return tmp_path


def _umbrella(**function_part: object) -> dict:
    return {"module": {"id": "lifecycle", "parts": [
        {"order": 1, "node": {"id": "biogenesis", "module_ref": "import"}},
        {"order": 2, "node": {"id": "division", "module_ref": "fission"}},
        {"order": 3, "node": {"id": "receptor_step", "module_ref": "import#receptor"}},
        {"order": 4, **function_part,
         "node": {"id": "function", "module_ref": "respiration"}},
    ]}}


def test_schema_accepts_module_ref():
    node = ModuleNode(id="division", label="Division", module_ref="fission#scission")
    assert node.module_ref == "fission#scission"


def test_reference_inlines_referenced_atoms(modules_dir: Path):
    circuit = compile_module(_umbrella(), modules_dir=modules_dir)
    assert is_satisfied(circuit, lambda a: a.gene_symbol in {"TOM40", "TOM20", "FTSZ", "COX1"})
    assert not is_satisfied(circuit, lambda a: a.gene_symbol in {"TOM40", "TOM20", "COX1"})


def test_gap_is_reported_at_the_umbrella_step(modules_dir: Path):
    circuit = compile_module(_umbrella(), modules_dir=modules_dir)
    gaps = unsatisfied_steps(circuit, lambda a: a.gene_symbol in {"TOM40", "TOM20", "COX1"})
    assert [step_id(s) for s in gaps] == ["division"]


def test_optional_reference_does_not_gate(modules_dir: Path):
    """A lineage without the referenced function (no COX1) still satisfies the umbrella."""
    holds = {"TOM40", "TOM20", "DRP1"}
    required = compile_module(_umbrella(), modules_dir=modules_dir)
    optional = compile_module(_umbrella(optional=True), modules_dir=modules_dir)
    assert not is_satisfied(required, lambda a: a.gene_symbol in holds)
    assert is_satisfied(optional, lambda a: a.gene_symbol in holds)


def test_referenced_atom_ids_are_namespaced_and_shared(modules_dir: Path):
    """The same referenced step reached twice is one atom, namespaced by module."""
    circuit = compile_module(_umbrella(), modules_dir=modules_dir)
    core_ids = sorted(a.node_id for a in core_atoms(circuit))
    assert core_ids == ["import#rec", "import#tom", "respiration#cox"]


def test_compile_module_file_resolves_against_its_directory(modules_dir: Path):
    path = _write(modules_dir, "lifecycle", _umbrella()["module"])
    circuit = compile_module_file(path)
    assert is_satisfied(circuit, lambda a: a.gene_symbol in {"TOM40", "TOM20", "DRP1", "COX1"})


def test_unresolvable_reference_fails_fast(modules_dir: Path):
    doc = {"module": {"id": "u", "parts": [{"node": {"id": "x", "module_ref": "nope"}}]}}
    with pytest.raises(ValueError, match="nope"):
        compile_module(doc, modules_dir=modules_dir)


def test_reference_cycle_fails_fast(modules_dir: Path):
    _write(modules_dir, "a", {"id": "a", "parts": [{"node": {"id": "x", "module_ref": "b"}}]})
    _write(modules_dir, "b", {"id": "b", "parts": [{"node": {"id": "y", "module_ref": "a"}}]})
    with pytest.raises(ValueError, match="cycle"):
        compile_module_file(modules_dir / "a.yaml")


def test_valid_references_have_no_violations(modules_dir: Path):
    assert module_ref_violations(_umbrella(), modules_dir=modules_dir) == []


@pytest.mark.parametrize(
    ("node", "message"),
    [
        ({"id": "x", "module_ref": "nope"}, "not found"),
        ({"id": "x", "module_ref": "import#nope"}, "not found"),
        ({"id": "x", "module_ref": "import", "annotons": [_annoton("z", "Z")]}, "annotons"),
        ({"id": "x", "module_ref": "import", "parts": [{"node": {"id": "p"}}]}, "parts"),
    ],
)
def test_reference_violations(modules_dir: Path, node: dict, message: str):
    doc = {"module": {"id": "u", "parts": [{"node": node}]}}
    violations = module_ref_violations(doc, modules_dir=modules_dir)
    assert len(violations) == 1
    assert violations[0]["severity"] == "error"
    assert violations[0]["node_id"] == "x"
    assert message in violations[0]["message"]


def test_cycle_violation_names_the_cycle(modules_dir: Path):
    _write(modules_dir, "b", {"id": "b", "parts": [{"node": {"id": "y", "module_ref": "a"}}]})
    doc = {"module": {"id": "a", "parts": [{"node": {"id": "x", "module_ref": "b"}}]}}
    violations = module_ref_violations(doc, modules_dir=modules_dir, self_stem="a")
    assert [v["message"] for v in violations] == ["module_ref cycle: a -> b -> a"]


def test_reference_node_is_not_an_ungrounded_leaf(modules_dir: Path):
    assert leaf_nodes_missing_representatives(_umbrella()) == []


def test_diamond_reference_routes_have_no_duplicate_atoms(modules_dir: Path):
    """Two steps referencing one module: each route lists a shared atom once."""
    doc = {"module": {"id": "u", "parts": [
        {"node": {"id": "first", "module_ref": "fission"}},
        {"node": {"id": "second", "module_ref": "fission"}},
    ]}}
    circuit = compile_module(doc, modules_dir=modules_dir)
    routes = enumerate_routes(circuit)
    assert all(len(r) == len({a.node_id for a in r}) for r in routes)
    # Independent copies still enumerate their branches independently
    # (documented limitation), so mixed-branch routes appear.
    assert sorted(sorted(a.node_id for a in r) for r in routes) == [
        ["fission#drp"], ["fission#drp", "fission#ftz"],
        ["fission#drp", "fission#ftz"], ["fission#ftz"],
    ]


def test_route_count_guard(modules_dir: Path):
    doc = {"module": {"id": "u", "parts": [
        {"node": {"id": f"s{i}", "module_ref": "fission"}} for i in range(3)
    ]}}
    circuit = compile_module(doc, modules_dir=modules_dir)
    assert count_routes(circuit) == 8
    assert len(enumerate_routes(circuit)) == 8
    with pytest.raises(ValueError, match="8 routes"):
        enumerate_routes(circuit, max_routes=4)


def test_core_atoms_does_not_enumerate_routes(modules_dir: Path):
    """core_atoms stays exact for a circuit far past the route-count guard."""
    doc = {"module": {"id": "u", "parts": [
        {"node": {"id": f"s{i}", "module_ref": "fission"}} for i in range(20)
    ] + [{"node": {"id": "imp", "module_ref": "import"}}]}}
    circuit = compile_module(doc, modules_dir=modules_dir)
    assert count_routes(circuit) == 2 ** 20
    assert sorted(a.node_id for a in core_atoms(circuit)) == ["import#rec", "import#tom"]


def test_render_href_resolves_from_the_referencing_file(tmp_path: Path):
    """A module in a subdirectory links to its sibling, as the engine resolves it."""
    sub = tmp_path / "modules" / "experimental"
    sub.mkdir(parents=True)
    _write(sub, "sibling", {"id": "sibling", "annotons": [_annoton("a", "A")]})
    umbrella = _write(sub, "umbrella", {"id": "umbrella", "parts": [
        {"node": {"id": "x", "module_ref": "sibling#a_node"}}]})
    doc = yaml.safe_load(umbrella.read_text())
    out = tmp_path / "pages" / "modules" / "experimental" / "umbrella.html"
    hrefs = collect_module_ref_hrefs(
        doc, umbrella, out, tmp_path / "pages" / "modules", tmp_path / "modules")
    assert hrefs == {"sibling#a_node": "sibling.html#node-a_node"}


def test_boolean_export_warns_on_module_ref():
    doc = {"module": {"id": "u", "parts": [{"node": {"id": "x", "module_ref": "fission"}}]}}
    with pytest.warns(UserWarning, match="module_ref"):
        module_to_boolean(doc)
