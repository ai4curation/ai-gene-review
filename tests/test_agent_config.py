"""Tests for the centralized agent-config model resolution.

`.github/agent-config.yaml` is the single source of truth for which Claude model
backs each agentic workflow. These tests pin the resolver's behaviour and, more
importantly, keep the config honest: every key must map to a real workflow that
actually sources its model from the config, and no workflow may re-hardcode a
`--model claude-...` inline (a stale hardcoded ID silently no-ops a run into a
phantom green check).
"""

import importlib.util
import re
import sys
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
ACTION_DIR = REPO_ROOT / ".github" / "actions" / "resolve-agent-config"
CONFIG_PATH = REPO_ROOT / ".github" / "agent-config.yaml"
WORKFLOW_DIR = REPO_ROOT / ".github" / "workflows"

_SPEC = importlib.util.spec_from_file_location(
    "resolve_agent_config", ACTION_DIR / "resolve_agent_config.py"
)
assert _SPEC is not None and _SPEC.loader is not None
resolver = importlib.util.module_from_spec(_SPEC)
sys.modules[_SPEC.name] = resolver
_SPEC.loader.exec_module(resolver)


@pytest.fixture
def config() -> dict:
    return resolver.load_config(CONFIG_PATH)


def test_single_model_resolves_from_config(config):
    assert resolver.resolve_model(config, "pr-shepherd") == "claude-opus-5"


def test_override_wins(config):
    assert (
        resolver.resolve_model(config, "pr-shepherd", "claude-sonnet-5")
        == "claude-sonnet-5"
    )
    # whitespace-only override is treated as no override
    assert resolver.resolve_model(config, "pr-shepherd", "  ") == "claude-opus-5"


def test_default_model_fallback():
    cfg = {"default_model": "claude-opus-5", "workflows": {"x": {}}}
    assert resolver.resolve_model(cfg, "x") == "claude-opus-5"


def test_unknown_workflow_errors(config):
    with pytest.raises(resolver.ConfigError):
        resolver.resolve_model(config, "does-not-exist")


def test_missing_model_and_default_errors():
    cfg = {"workflows": {"x": {}}}
    with pytest.raises(resolver.ConfigError):
        resolver.resolve_model(cfg, "x")


def test_matrix_mode_round_trips():
    cfg = {
        "workflows": {
            "fan-out": {
                "matrix": [
                    {"effort": "low_effort", "model": "claude-haiku-4-5-20251001"},
                    {"effort": "high_effort", "model": "claude-opus-5"},
                ]
            }
        }
    }
    matrix = resolver.resolve_matrix(cfg, "fan-out")
    assert [entry["model"] for entry in matrix] == [
        "claude-haiku-4-5-20251001",
        "claude-opus-5",
    ]


def test_single_model_mode_rejects_matrix_workflow():
    cfg = {"workflows": {"fan-out": {"matrix": [{"model": "claude-opus-5"}]}}}
    with pytest.raises(resolver.ConfigError):
        resolver.resolve_model(cfg, "fan-out")


def test_every_config_workflow_file_exists(config):
    """Each key under workflows: must map to a real workflow file."""
    for stem in config["workflows"]:
        candidates = [WORKFLOW_DIR / f"{stem}.yml", WORKFLOW_DIR / f"{stem}.yaml"]
        assert any(c.exists() for c in candidates), f"no workflow file for '{stem}'"


def _workflow_texts() -> dict[str, str]:
    return {path.stem: path.read_text() for path in WORKFLOW_DIR.glob("*.y*ml")}


# Workflows not yet migrated onto the central config. Delete an entry when its
# workflow starts resolving its model from .github/agent-config.yaml; the list
# must only ever shrink. Anything NOT listed here that hardcodes a model fails.
UNMIGRATED_MODEL_HARDCODES = {
    "go-annotation-scanner",
    "weekly-compliance",
}


def test_no_workflow_hardcodes_a_model_inline():
    """No workflow should pin a claude-* model on a `--model` invocation line;
    models must come from the resolve-agent-config action. A stale hardcoded ID
    silently no-ops a run into a phantom green check.

    A workflow_dispatch `model:` dropdown may still *list* models as choices, so
    only `--model` lines are flagged.
    """
    offenders = {}
    # Covers every current and anticipated Claude model family (haiku/sonnet/
    # opus/fable) so a future hardcoded model is also caught.
    model_family = re.compile(r"claude-(haiku|sonnet|opus|fable)-")
    for stem, text in _workflow_texts().items():
        for line in text.splitlines():
            if "--model" in line and model_family.search(line):
                offenders.setdefault(stem, []).append(line.strip())

    new = {stem: lines for stem, lines in offenders.items()
           if stem not in UNMIGRATED_MODEL_HARDCODES}
    assert not new, "hardcoded --model found (should use AGENT_MODEL):\n" + "\n".join(
        f"{stem}: {line}" for stem, lines in new.items() for line in lines
    )

    stale = UNMIGRATED_MODEL_HARDCODES - set(offenders)
    assert not stale, (
        "these workflows no longer hardcode a model; drop them from "
        f"UNMIGRATED_MODEL_HARDCODES: {sorted(stale)}"
    )


def test_managed_workflows_use_the_resolver_action():
    """Every workflow in agent-config.yaml must actually source its model from
    the config: single-model workflows `uses:` the composite action; matrix
    workflows instead call the resolver script from a setup job."""
    config = yaml.safe_load(CONFIG_PATH.read_text())
    texts = _workflow_texts()
    for stem, entry in config["workflows"].items():
        text = texts.get(stem, "")
        if isinstance(entry, dict) and entry.get("matrix"):
            assert (
                "resolve-agent-config/resolve_agent_config.py" in text
                and "--matrix" in text
            ), f"matrix workflow '{stem}' does not emit its matrix from the config"
        else:
            assert "uses: ./.github/actions/resolve-agent-config" in text, (
                f"workflow '{stem}' is in agent-config.yaml but does not `uses:` "
                f"the resolve-agent-config action"
            )
