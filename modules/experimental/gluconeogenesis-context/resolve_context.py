#!/usr/bin/env python
"""Resolve which gluconeogenesis route is active per tissue, from expression.

Ties the module logic circuit (module_logic) to the GTEx expression oracle
(gtex_oracle): an atom "holds" in a tissue iff its gene's median TPM is at or
above a threshold. For each GTEx tissue we then report whether the pathway is
satisfiable, which route(s) are realised, and -- where it is not satisfiable --
which gate atom (required by every route) is missing.

This is the eukaryotic analogue of GapMind's genomic step-finding: genome
presence is uniform across tissues, so the discriminating variable is expression.
Expression is used asymmetrically and honestly: absence excludes a route (no
enzyme -> no flux), presence only permits it.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from ai_gene_review.module_logic import (
    compile_module_file, enumerate_routes, core_atoms, is_satisfied,
)
from gtex_oracle import load_cache

# Tissues where free-glucose-releasing gluconeogenesis is textbook-active,
# used only to validate the derived result (not as input).
EXPECTED_GLUCONEOGENIC = {"Liver", "Kidney_Cortex", "Small_Intestine_Terminal_Ileum"}


def resolve(module_path: str, threshold: float) -> dict:
    circuit = compile_module_file(module_path)
    tissues, matrix = load_cache()

    def expressed(symbol: str, tissue: str) -> bool:
        return matrix.get(symbol, {}).get(tissue, 0.0) >= threshold

    routes = enumerate_routes(circuit)
    gate = core_atoms(circuit)

    report: dict[str, dict] = {}
    for tissue in tissues:
        holds = lambda atom, _t=tissue: expressed(atom.gene_symbol, _t) if atom.gene_symbol else True
        sat = is_satisfied(circuit, holds)
        active_routes = [
            [a.gene_symbol for a in r if a.gene_symbol]
            for r in routes
            if all(holds(a) for a in r)
        ]
        missing_gate = [a.gene_symbol for a in gate if not holds(a)]
        report[tissue] = {
            "satisfiable": sat,
            "active_routes": active_routes,
            "missing_gate": missing_gate,
        }
    return {"routes": len(routes), "gate": [a.gene_symbol for a in gate], "tissues": report}


def format_report(result: dict, threshold: float) -> str:
    lines: list[str] = []
    sat = {t: r for t, r in result["tissues"].items() if r["satisfiable"]}
    lines.append(f"Routes through the module: {result['routes']}")
    lines.append(f"Gate (atoms required by every route): {result['gate']}")
    lines.append(f"Expression threshold: median TPM >= {threshold}\n")

    lines.append(f"== Tissues where gluconeogenesis is SATISFIABLE ({len(sat)}) ==")
    for t in sorted(sat):
        routes = sat[t]["active_routes"]
        # Summarise the realised variant choices (PEPCK / FBPase).
        choices = sorted({g for r in routes for g in r if g in {"PCK1", "PCK2", "FBP1", "FBP2"}})
        lines.append(f"  {t:38s} routes={len(routes)}  variants={choices}")

    lines.append("\n== Representative NON-gluconeogenic tissues (gate failure) ==")
    for t in ["Muscle_Skeletal", "Brain_Cortex", "Heart_Left_Ventricle", "Whole_Blood",
              "Adipose_Subcutaneous", "Lung"]:
        if t in result["tissues"] and not result["tissues"][t]["satisfiable"]:
            lines.append(f"  {t:38s} missing gate: {result['tissues'][t]['missing_gate']}")

    # Validation against textbook tissue restriction.
    derived = set(sat)
    expected = EXPECTED_GLUCONEOGENIC
    lines.append("\n== Validation vs textbook gluconeogenic tissues ==")
    lines.append(f"  expected: {sorted(expected)}")
    lines.append(f"  recovered (expected ∩ derived): {sorted(expected & derived)}")
    lines.append(f"  additional satisfiable tissues: {sorted(derived - expected)}")
    lines.append(f"  expected but missed: {sorted(expected - derived)}")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("module", nargs="?",
                    default=str(Path(__file__).parents[2] / "gluconeogenesis_human.yaml"))
    ap.add_argument("--threshold", type=float, default=1.0)
    args = ap.parse_args()
    result = resolve(args.module, args.threshold)
    print(format_report(result, args.threshold))
