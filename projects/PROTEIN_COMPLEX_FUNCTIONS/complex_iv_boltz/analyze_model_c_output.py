#!/usr/bin/env python3
"""Analyze Boltz Model C outputs for COX2/SCO1/SCO2 attribution readouts."""

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


VARIANTS = {
    "full": {
        "A": ChainSpec("MT-CO2_1-227", 1, 227),
        "B": ChainSpec("SCO1_68-301", 68, 301),
        "C": ChainSpec("SCO2_42-266", 42, 266),
    },
    "domains": {
        "A": ChainSpec("MT-CO2_88-227", 88, 227),
        "B": ChainSpec("SCO1_112-301", 112, 301),
        "C": ChainSpec("SCO2_79-266", 79, 266),
    },
    "model_a_domains": {
        "A": ChainSpec("MT-CO2_88-227", 88, 227),
        "B": ChainSpec("SCO1_112-301", 112, 301),
    },
}

MOTIFS = {
    "COX2_CuA": [("A", 196, "CYS"), ("A", 200, "CYS")],
    "SCO1_CxxxC": [("B", 169, "CYS"), ("B", 173, "CYS")],
    "SCO2_CxxxC": [("C", 133, "CYS"), ("C", 137, "CYS")],
}


def input_residue(original_position: int, chain: str, specs: dict[str, ChainSpec]) -> int:
    spec = specs[chain]
    if not spec.start <= original_position <= spec.end:
        raise ValueError(
            f"{chain} residue {original_position} is outside {spec.start}-{spec.end}"
        )
    return original_position - spec.start + 1


def residue(chain, residue_index: int):
    return chain[(" ", residue_index, " ")]


def atom_coord(chain, residue_index: int, atom_name: str):
    res = residue(chain, residue_index)
    if atom_name not in res:
        return None
    return res[atom_name].coord


def distance(a, b) -> float:
    return math.sqrt(float(((a - b) ** 2).sum()))


def min_distance(
    chains,
    specs: dict[str, ChainSpec],
    motif_a: Iterable[tuple[str, int, str]],
    motif_b: Iterable[tuple[str, int, str]],
    atom_name: str,
) -> tuple[float | None, str]:
    best: tuple[float | None, str] = (None, "")
    for chain_a, original_a, _resname_a in motif_a:
        idx_a = input_residue(original_a, chain_a, specs)
        coord_a = atom_coord(chains[chain_a], idx_a, atom_name)
        if coord_a is None:
            continue
        for chain_b, original_b, _resname_b in motif_b:
            idx_b = input_residue(original_b, chain_b, specs)
            coord_b = atom_coord(chains[chain_b], idx_b, atom_name)
            if coord_b is None:
                continue
            dist = distance(coord_a, coord_b)
            if best[0] is None or dist < best[0]:
                best = (
                    dist,
                    f"{chain_a}{original_a}:{atom_name} - {chain_b}{original_b}:{atom_name}",
                )
    return best


def sidechain_sulfur_min_distance(
    chains,
    specs: dict[str, ChainSpec],
    motif_a: Iterable[tuple[str, int, str]],
    motif_b: Iterable[tuple[str, int, str]],
) -> tuple[float | None, str]:
    best: tuple[float | None, str] = (None, "")
    for chain_a, original_a, _resname_a in motif_a:
        idx_a = input_residue(original_a, chain_a, specs)
        coord_a = atom_coord(chains[chain_a], idx_a, "SG")
        if coord_a is None:
            continue
        for chain_b, original_b, _resname_b in motif_b:
            idx_b = input_residue(original_b, chain_b, specs)
            coord_b = atom_coord(chains[chain_b], idx_b, "SG")
            if coord_b is None:
                continue
            dist = distance(coord_a, coord_b)
            if best[0] is None or dist < best[0]:
                best = (dist, f"{chain_a}{original_a}:SG - {chain_b}{original_b}:SG")
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
    structure = MMCIFParser(QUIET=True).get_structure("model_c", str(cif))
    model = next(structure.get_models())
    return cif, {chain.id: chain for chain in model}


def detect_variant(pred_dir: Path) -> str:
    text = str(pred_dir)
    if "model_a" in text or "cox2_sco1" in text:
        return "model_a_domains"
    if "model_c_full" in text:
        return "full"
    if "model_c_domains" in text:
        return "domains"
    return "domains"


def format_metric(value) -> str:
    if isinstance(value, int | float):
        return f"{value:.3f}"
    return str(value)


def pair_iptm(confidence: dict, row: int, col: int) -> float | None:
    matrix = confidence.get("pair_chains_iptm", {})
    try:
        return float(matrix[str(row)][str(col)])
    except (KeyError, TypeError, ValueError):
        return None


def motif_present(motif: Iterable[tuple[str, int, str]], specs: dict[str, ChainSpec]) -> bool:
    return all(chain_id in specs for chain_id, _pos, _resname in motif)


def build_markdown(pred_dir: Path, variant: str) -> str:
    specs = VARIANTS[variant]
    confidence = load_confidence(pred_dir)
    cif, chains = load_structure(pred_dir)
    display_name = {
        "full": "Model C full",
        "domains": "Model C domains",
        "model_a_domains": "Model A domains",
    }.get(variant, variant)

    readouts = [
        ("SCO1 CxxxC to COX2 CuA", "SCO1_CxxxC", "COX2_CuA"),
        ("SCO2 CxxxC to COX2 CuA", "SCO2_CxxxC", "COX2_CuA"),
        ("SCO2 CxxxC to SCO1 CxxxC", "SCO2_CxxxC", "SCO1_CxxxC"),
    ]

    lines = [
        f"# Boltz {display_name} Analysis",
        "",
        f"Prediction directory: `{pred_dir}`",
        f"Model CIF: `{cif}`",
        "",
        "## Chains",
        "",
        "| Chain | Segment |",
        "|---|---|",
    ]
    for chain_id, spec in specs.items():
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

    lines.extend(["", "## Pair-Chain ipTM", "", "| Pair | Value |", "|---|---:|"])
    for label, chain_a, chain_b, row, col in [
        ("MT-CO2:SCO1", "A", "B", 0, 1),
        ("MT-CO2:SCO2", "A", "C", 0, 2),
        ("SCO1:SCO2", "B", "C", 1, 2),
    ]:
        if chain_a not in specs or chain_b not in specs:
            continue
        value = pair_iptm(confidence, row, col)
        if value is not None:
            lines.append(f"| {label} | {format_metric(value)} |")

    lines.extend(
        [
            "",
            "## Attribution Readouts",
            "",
            "| Readout | Min CA distance | Min SG-SG distance | Closest atoms |",
            "|---|---:|---:|---|",
        ]
    )
    for label, motif_a, motif_b in readouts:
        if not (
            motif_present(MOTIFS[motif_a], specs)
            and motif_present(MOTIFS[motif_b], specs)
        ):
            continue
        ca_dist, ca_pair = min_distance(
            chains, specs, MOTIFS[motif_a], MOTIFS[motif_b], "CA"
        )
        sg_dist, sg_pair = sidechain_sulfur_min_distance(
            chains, specs, MOTIFS[motif_a], MOTIFS[motif_b]
        )
        ca_text = f"{ca_dist:.2f} A" if ca_dist is not None else "n/a"
        sg_text = f"{sg_dist:.2f} A" if sg_dist is not None else "n/a"
        pair_text = sg_pair or ca_pair
        lines.append(f"| {label} | {ca_text} | {sg_text} | {pair_text} |")

    iptm = confidence.get("iptm")
    interpretation = (
        "Curation-grade structural support would require reproducible placement with "
        "ipTM > 0.5 and low interface PAE. Distances below the 12 A CA threshold are "
        "hypothesis-generating only when global/interface confidence is low."
    )
    if isinstance(iptm, int | float) and iptm < 0.5:
        interpretation = (
            "This run is below the ipTM > 0.5 threshold, so it should not be used as "
            "curation-grade structural evidence. Treat any short motif distances as "
            "hypotheses to retest with MSA-backed and multi-seed runs."
        )

    lines.extend(["", "## Interpretation", "", interpretation, ""])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("prediction_directory", type=Path)
    parser.add_argument("--variant", choices=sorted(VARIANTS), default=None)
    parser.add_argument("--markdown-out", type=Path, default=None)
    args = parser.parse_args()

    pred_dir = args.prediction_directory
    if pred_dir.is_file():
        pred_dir = pred_dir.parent
    variant = args.variant or detect_variant(pred_dir)
    markdown = build_markdown(pred_dir, variant)

    if args.markdown_out:
        args.markdown_out.write_text(markdown, encoding="utf-8")
    print(markdown)


if __name__ == "__main__":
    main()
