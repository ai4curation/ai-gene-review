#!/usr/bin/env python3
"""Convert the Boltz YAML input into a BioLM Boltz-2 hosted API payload."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parent
DEFAULT_INPUT = ROOT / "inputs" / "cox2_sco1_sco2_coa6_domains.yaml"
DEFAULT_OUTPUT = ROOT / "inputs" / "cox2_sco1_sco2_coa6_domains_biolm.json"


def load_boltz_yaml(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"Expected a mapping in {path}")
    return data


def to_molecule(entry: dict[str, Any]) -> dict[str, Any]:
    entity_type = next(iter(entry.keys()))
    entity = entry[entity_type]
    if not isinstance(entity, dict):
        raise ValueError(f"Expected a mapping entry, got: {entry}")

    molecule: dict[str, Any] = {
        "id": entity["id"],
        "type": entity_type,
    }
    for key in ("sequence", "smiles", "ccd"):
        if key in entity:
            molecule[key] = entity[key]
    return molecule


def build_payload(args: argparse.Namespace) -> dict[str, Any]:
    data = load_boltz_yaml(args.input)
    sequences = data.get("sequences")
    if not isinstance(sequences, list) or not sequences:
        raise ValueError(f"No sequences found in {args.input}")

    return {
        "items": [
            {
                "molecules": [to_molecule(entry) for entry in sequences],
                "constraints": data.get("constraints", []),
            }
        ],
        "params": {
            "recycling_steps": args.recycling_steps,
            "sampling_steps": args.sampling_steps,
            "diffusion_samples": args.diffusion_samples,
            "step_scale": args.step_scale,
            "potentials": not args.without_potentials,
            "include": args.include,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build a BioLM Boltz-2 hosted API payload from a Boltz YAML input."
    )
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--recycling-steps", type=int, default=3)
    parser.add_argument("--sampling-steps", type=int, default=50)
    parser.add_argument("--diffusion-samples", type=int, default=1)
    parser.add_argument("--step-scale", type=float, default=1.638)
    parser.add_argument("--without-potentials", action="store_true")
    parser.add_argument(
        "--include",
        nargs="*",
        default=["pae", "pde"],
        help="Optional confidence arrays/outputs to request when supported.",
    )
    args = parser.parse_args()

    payload = build_payload(args)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(args.output)


if __name__ == "__main__":
    main()
