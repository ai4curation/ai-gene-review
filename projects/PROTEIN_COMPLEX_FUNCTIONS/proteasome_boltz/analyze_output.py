#!/usr/bin/env python3
"""Analyze proteasome PSMB5:PSMA1 Boltz/BioLM output."""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from pathlib import Path

from Bio.PDB import MMCIFParser, NeighborSearch


@dataclass(frozen=True)
class ChainSpec:
    label: str
    start: int
    end: int


SPECS = {
    "A": ChainSpec("PSMB5_60-263", 60, 263),
    "B": ChainSpec("PSMA1_1-263", 1, 263),
}

PSMB5_ACTIVE_SITE_ORIGINAL = 60


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


def chain_atoms(chain):
    return [
        atom
        for atom in chain.get_atoms()
        if atom.element != "H" and atom.parent.id[0] == " "
    ]


def residue_contacts(chain_a, chain_b, cutoff=5.0):
    atoms_b = chain_atoms(chain_b)
    ns = NeighborSearch(atoms_b)
    contacts = set()
    for atom_a in chain_atoms(chain_a):
        for atom_b in ns.search(atom_a.coord, cutoff, "A"):
            contacts.add((atom_a.parent.id[1], atom_b.parent.id[1]))
    return contacts


def min_active_site_to_psma1_distance(chains) -> tuple[float | None, str]:
    active_ca = atom_coord(chains, "A", PSMB5_ACTIVE_SITE_ORIGINAL, "CA")
    active_og = atom_coord(chains, "A", PSMB5_ACTIVE_SITE_ORIGINAL, "OG1")
    if active_ca is None:
        return None, ""

    best: tuple[float | None, str] = (None, "")
    for residue in chains["B"]:
        if residue.id[0] != " ":
            continue
        for atom_name, active_coord in [("CA", active_ca), ("OG1", active_og)]:
            if active_coord is None or atom_name not in residue:
                continue
            dist = distance(active_coord, residue[atom_name].coord)
            if best[0] is None or dist < best[0]:
                psma1_original = residue.id[1]
                best = (
                    dist,
                    f"PSMB5 T60:{atom_name} - PSMA1 {psma1_original}:{atom_name}",
                )
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
    structure = MMCIFParser(QUIET=True).get_structure("proteasome", str(cif))
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
    pair = pair_iptm(confidence, 0, 1)
    contacts = residue_contacts(chains["A"], chains["B"], cutoff=5.0)
    active_dist, active_pair = min_active_site_to_psma1_distance(chains)

    lines = [
        "# Boltz Proteasome PSMB5:PSMA1 Attribution Analysis",
        "",
        f"Prediction directory: `{pred_dir}`",
        f"Model CIF: `{cif}`",
        "",
        "## Hypothesis",
        "",
        (
            "PSMB5 is a catalytic beta subunit and should retain threonine-type "
            "endopeptidase activity attribution. PSMA1 is an alpha-ring structural "
            "subunit; even if it forms a confident structural interface with PSMB5, "
            "it should not inherit PSMB5 protease activity by complex membership."
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

    lines.extend(
        [
            "",
            "## Attribution Readouts",
            "",
            "| Readout | Value | Notes |",
            "|---|---:|---|",
            f"| PSMB5:PSMA1 pair-chain ipTM | {format_metric(pair) if pair is not None else 'n/a'} | structural-interface confidence |",
            f"| PSMB5:PSMA1 5 A residue contacts | {len(contacts)} | co-complex/interface signal, not activity export |",
            f"| PSMB5 active-site T60 to nearest PSMA1 atom | {active_dist:.2f} A | {active_pair} |",
            "",
            "## Interpretation",
            "",
        ]
    )
    if pair is not None and pair > 0.5:
        lines.append(
            "The predicted PSMB5:PSMA1 interface is plausible, but this supports "
            "proteasome architecture rather than exporting protease molecular "
            "function to PSMA1. The active-site nucleophile is intrinsic to PSMB5."
        )
    else:
        lines.append(
            "The interface confidence is below the provisional pair-chain ipTM > 0.5 "
            "threshold, so this particular prediction should be treated as "
            "hypothesis-generating only. The annotation conclusion is still clear "
            "from UniProt features and proteasome biology: PSMB5 carries the "
            "protease active site; PSMA1 is structural."
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
