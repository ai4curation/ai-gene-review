#!/usr/bin/env python3
"""Analyze Complex III CYC1:UQCRFS1 Boltz/BioLM outputs."""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from Bio.PDB import MMCIFParser


@dataclass(frozen=True)
class ChainSpec:
    label: str
    start: int
    end: int


SPECS = {
    "A": ChainSpec("CYC1_85-281", 85, 281),
    "B": ChainSpec("UQCRFS1_141-274", 141, 274),
}

CYC1_HEME_RESIDUES = [("A", 121), ("A", 124), ("A", 125), ("A", 244)]
UQCRFS1_RIESKE_RESIDUES = [("B", 217), ("B", 219), ("B", 236), ("B", 239), ("B", 241)]


def input_residue(original_position: int, chain_id: str) -> int:
    spec = SPECS[chain_id]
    if not spec.start <= original_position <= spec.end:
        raise ValueError(
            f"{chain_id} residue {original_position} is outside {spec.start}-{spec.end}"
        )
    return original_position - spec.start + 1


def atom_coord(chains, chain_id: str, original_position: int, atom_name: str):
    chain = chains[chain_id]
    res = chain[(" ", input_residue(original_position, chain_id), " ")]
    if atom_name not in res:
        return None
    return res[atom_name].coord


def distance(a, b) -> float:
    return math.sqrt(float(((a - b) ** 2).sum()))


def min_distance(
    chains,
    residues_a: Iterable[tuple[str, int]],
    residues_b: Iterable[tuple[str, int]],
    atom_name: str,
) -> tuple[float | None, str]:
    best: tuple[float | None, str] = (None, "")
    for chain_a, pos_a in residues_a:
        coord_a = atom_coord(chains, chain_a, pos_a, atom_name)
        if coord_a is None:
            continue
        for chain_b, pos_b in residues_b:
            coord_b = atom_coord(chains, chain_b, pos_b, atom_name)
            if coord_b is None:
                continue
            dist = distance(coord_a, coord_b)
            if best[0] is None or dist < best[0]:
                best = (dist, f"{chain_a}{pos_a}:{atom_name} - {chain_b}{pos_b}:{atom_name}")
    return best


def load_confidence(pred_dir: Path) -> dict:
    confidence = next(pred_dir.glob("confidence_*.json"), None)
    if confidence is not None:
        return json.loads(confidence.read_text())

    biolm_summary = pred_dir / "boltz2_biolm_summary.json"
    if biolm_summary.exists():
        data = json.loads(biolm_summary.read_text())
        results = data.get("results")
        if isinstance(results, list) and results and isinstance(results[0], dict):
            return results[0]
        return data
    return {}


def load_structure(pred_dir: Path):
    cif = next(pred_dir.glob("*_model_0.cif"), None)
    if cif is None:
        cif = next(pred_dir.glob("*.cif"), None)
    if cif is None:
        raise FileNotFoundError(f"No CIF found in {pred_dir}")
    structure = MMCIFParser(QUIET=True).get_structure("complex_iii", str(cif))
    model = next(structure.get_models())
    return cif, {chain.id: chain for chain in model}


def pair_iptm(confidence: dict, row: int, col: int) -> float | None:
    matrix = confidence.get("pair_chains_iptm", {})
    try:
        return float(matrix[str(row)][str(col)])
    except (KeyError, TypeError, ValueError):
        return None


def format_metric(value) -> str:
    if isinstance(value, int | float):
        return f"{value:.3f}"
    return str(value)


def build_markdown(pred_dir: Path) -> str:
    confidence = load_confidence(pred_dir)
    cif, chains = load_structure(pred_dir)
    ca_dist, ca_pair = min_distance(
        chains, CYC1_HEME_RESIDUES, UQCRFS1_RIESKE_RESIDUES, "CA"
    )

    lines = [
        "# Boltz Complex III CYC1:UQCRFS1 Domain Analysis",
        "",
        f"Prediction directory: `{pred_dir}`",
        f"Model CIF: `{cif}`",
        "",
        "## Hypothesis",
        "",
        (
            "CYC1 and UQCRFS1 should behave as active Complex III electron-transfer "
            "subunits if the CYC1 heme-binding region and UQCRFS1 Rieske Fe-S region "
            "form a reproducible, confident interface. This contrasts with structural "
            "core subunits such as UQCRC1/UQCRC2."
        ),
        "",
        "## Chains",
        "",
        "| Chain | Segment |",
        "|---|---|",
    ]
    for chain_id, spec in SPECS.items():
        lines.append(f"| {chain_id} | {spec.label} |")

    lines.extend(["", "## Confidence", "", "| Metric | Value |", "|---|---:|"])
    for key in [
        "confidence_score",
        "ptm",
        "iptm",
        "protein_iptm",
        "complex_plddt",
        "complex_iplddt",
        "complex_pde",
        "complex_ipde",
    ]:
        if key in confidence:
            lines.append(f"| {key} | {format_metric(confidence[key])} |")

    pair = pair_iptm(confidence, 0, 1)
    lines.extend(
        [
            "",
            "## Interface Readout",
            "",
            "| Readout | Value | Closest atoms |",
            "|---|---:|---|",
            f"| CYC1 heme residues to UQCRFS1 Rieske residues, min CA distance | {ca_dist:.2f} A | {ca_pair} |",
            f"| CYC1:UQCRFS1 pair-chain ipTM | {format_metric(pair) if pair is not None else 'n/a'} | n/a |",
            "",
            "## Interpretation",
            "",
        ]
    )
    if pair is not None and pair > 0.5:
        lines.append(
            "The pair-chain ipTM is above the provisional 0.5 interface-confidence "
            "threshold, so this is a plausible structure-prediction signal for an "
            "active electron-transfer interface. It should still be interpreted "
            "with existing Complex III structures and literature, not alone."
        )
    else:
        lines.append(
            "This run does not reach the provisional pair-chain ipTM > 0.5 threshold, "
            "so it should be treated as hypothesis-generating only."
        )
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("prediction_directory", type=Path)
    parser.add_argument("--markdown-out", type=Path, default=None)
    args = parser.parse_args()

    pred_dir = args.prediction_directory
    if pred_dir.is_file():
        pred_dir = pred_dir.parent
    markdown = build_markdown(pred_dir)
    if args.markdown_out:
        args.markdown_out.write_text(markdown, encoding="utf-8")
    print(markdown)


if __name__ == "__main__":
    main()
