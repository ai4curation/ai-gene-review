#!/usr/bin/env python3
"""Resolve the effective AI model for an agentic workflow from agent-config.yaml.

Read at run time by the ``resolve-agent-config`` composite action. Two modes:

* default: print the single resolved model id for ``--workflow``.
  Resolution order: ``--override`` (if non-empty) > per-workflow ``model:`` >
  ``default_model``.
* ``--matrix``: print the workflow's ``matrix:`` list as a JSON array, for a job
  that fans out via ``strategy.matrix``.

Kept dependency-light (PyYAML only) and side-effect free so it can be unit
tested directly; the composite action does the ``$GITHUB_ENV`` / ``$GITHUB_OUTPUT``
plumbing.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import yaml

# A model id is a bare token. The resolved value is written to $GITHUB_ENV as
# `AGENT_MODEL=<value>` (no heredoc delimiter) and then interpolated into
# `--model ${{ env.AGENT_MODEL }}`, so an embedded newline would inject extra
# environment variables and an embedded space would inject extra CLI flags.
# Reject anything that is not a plain token, at the one place both paths pass
# through.
MODEL_ID_RE = re.compile(r"^[A-Za-z0-9._-]+$")


class ConfigError(RuntimeError):
    """Raised when the config cannot satisfy the request."""


def _validate_model(model: str, source: str) -> str:
    if not MODEL_ID_RE.match(model):
        raise ConfigError(
            f"{source} is not a valid model id: {model!r} (expected only "
            f"letters, digits, '.', '_' and '-')"
        )
    return model


def load_config(path: Path) -> dict:
    if not path.exists():
        raise ConfigError(f"agent config not found: {path}")
    data = yaml.safe_load(path.read_text()) or {}
    if not isinstance(data, dict):
        raise ConfigError(f"agent config must be a mapping: {path}")
    return data


def _workflow_entry(config: dict, workflow: str) -> dict:
    entry = (config.get("workflows") or {}).get(workflow)
    if entry is None:
        raise ConfigError(
            f"workflow '{workflow}' is not defined under 'workflows:' in the "
            f"agent config"
        )
    if not isinstance(entry, dict):
        raise ConfigError(f"workflow '{workflow}' entry must be a mapping")
    return entry


def resolve_model(config: dict, workflow: str, override: str | None = None) -> str:
    """Return the effective single model id for ``workflow``."""
    if override and override.strip():
        return _validate_model(override.strip(), "model override")
    entry = _workflow_entry(config, workflow)
    model = entry.get("model")
    if model and entry.get("matrix"):
        raise ConfigError(
            f"workflow '{workflow}' defines both 'model:' and 'matrix:'; "
            f"exactly one is allowed"
        )
    if model:
        return _validate_model(str(model), f"workflow '{workflow}' model")
    if entry.get("matrix"):
        raise ConfigError(
            f"workflow '{workflow}' defines a 'matrix:', not a single 'model:'; "
            f"use --matrix"
        )
    default = config.get("default_model")
    if not default:
        raise ConfigError(
            f"workflow '{workflow}' has no 'model:' and no top-level "
            f"'default_model' is set"
        )
    return _validate_model(str(default), "default_model")


def resolve_matrix(config: dict, workflow: str) -> list[dict]:
    """Return the workflow's ``matrix:`` list (for ``strategy.matrix.include``).

    Each entry is a mapping (e.g. ``{effort, model, selector}``) and must include
    a ``model``.
    """
    entry = _workflow_entry(config, workflow)
    matrix = entry.get("matrix")
    if not matrix:
        raise ConfigError(
            f"workflow '{workflow}' has no 'matrix:' list; use single-model mode"
        )
    if not isinstance(matrix, list) or not matrix:
        raise ConfigError(f"workflow '{workflow}' 'matrix:' must be a non-empty list")
    for item in matrix:
        if isinstance(item, dict) and item.get("model"):
            _validate_model(str(item["model"]), f"workflow '{workflow}' matrix model")
        if not isinstance(item, dict) or not item.get("model"):
            raise ConfigError(
                f"workflow '{workflow}' matrix entries must be mappings with a "
                f"'model:'"
            )
    return matrix


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--workflow", required=True)
    parser.add_argument("--override", default="")
    parser.add_argument(
        "--matrix",
        action="store_true",
        help="print the workflow's models: list as a JSON array",
    )
    args = parser.parse_args(argv)

    try:
        config = load_config(args.config)
        if args.matrix:
            print(json.dumps(resolve_matrix(config, args.workflow)))
        else:
            print(resolve_model(config, args.workflow, args.override))
    except ConfigError as exc:
        print(f"resolve-agent-config: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
