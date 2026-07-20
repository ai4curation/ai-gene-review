"""Tests that long-running provider timeouts reach deep-research-client."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_script(name: str):
    scripts_dir = ROOT / "scripts"
    if str(scripts_dir) not in sys.path:
        sys.path.insert(0, str(scripts_dir))
    path = scripts_dir / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_gene_wrapper_propagates_openscientist_timeout(tmp_path):
    wrapper = load_script("deep_research_wrapper")

    cmd = wrapper._build_cmd(
        organism="PSEPK",
        gene_id="argE",
        provider="openscientist",
        gene_symbol="argE",
        output_path=tmp_path / "argE-deep-research-openscientist.md",
        provider_timeout=7200,
    )

    assert cmd[cmd.index("--provider") + 1] == "openscientist"
    assert "timeout=7200" in cmd


def test_module_pathway_wrapper_propagates_openscientist_timeout(tmp_path):
    wrapper = load_script("module_pathway_taxon_deep_research_wrapper")

    cmd = wrapper.build_command(
        variables={"module_title": "Arginine biosynthesis"},
        provider="openscientist",
        output_path=tmp_path / "report.md",
        template=Path("templates/module_pathway_taxon_research.md.j2"),
        extra_args=None,
        provider_timeout=7200,
    )

    assert cmd[cmd.index("--provider") + 1] == "openscientist"
    assert "timeout=7200" in cmd
