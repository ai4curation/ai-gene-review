#!/usr/bin/env python
"""Resolve gluconeogenesis satisfiability across liver lobule ZONES (not tissues).

Same circuit engine as the tissue resolver, but the context is now the nine layers
of the liver lobule (Halpern 2017 reconstructed zonation), so the question becomes
intra-organ: *within* the liver, which hepatocyte zone can run gluconeogenesis?

An atom "holds" in a layer iff its gene's relative zonation profile (normalised to
its own peak) is at or above a threshold there. The porto-central orientation is
inferred from landmark genes, so "periportal/pericentral" labels are derived, not
assumed.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from module_logic import compile_module_file, enumerate_routes, core_atoms, is_satisfied
from zonation_oracle import (
    load_profiles, relative_profile, portal_pole, zone_label, N_LAYERS,
    PERICENTRAL_LANDMARKS,
)

# Human module symbols -> mouse symbols used in Halpern Table S3.
HUMAN_TO_MOUSE = {
    "PC": "Pcx", "PCK1": "Pck1", "PCK2": "Pck2", "FBP1": "Fbp1",
    "FBP2": "Fbp2", "G6PC1": "G6pc", "SLC37A4": "Slc37a4",
}


def resolve(module_path: str, threshold: float) -> dict:
    circuit = compile_module_file(module_path)
    profiles = load_profiles()
    rel = {g: relative_profile(p) for g, p in profiles.items()}
    pp = portal_pole(profiles)

    def holds_in_layer(atom, layer_idx):
        if not atom.gene_symbol:
            return True
        mouse = HUMAN_TO_MOUSE.get(atom.gene_symbol)
        if mouse is None or mouse not in rel:
            return False
        return rel[mouse][layer_idx] >= threshold

    routes = enumerate_routes(circuit)
    gate = core_atoms(circuit)

    layers = []
    for li in range(N_LAYERS):
        holds = lambda a, _li=li: holds_in_layer(a, _li)
        sat = is_satisfied(circuit, holds)
        missing = [a.gene_symbol for a in gate if not holds(a)]
        layers.append({
            "layer": li + 1,
            "zone": zone_label(li, pp),
            "satisfiable": sat,
            "missing_gate": missing,
        })
    return {
        "periportal_pole_layer": pp + 1,
        "gate": [a.gene_symbol for a in gate],
        "routes": len(routes),
        "layers": layers,
    }


def format_report(result: dict, threshold: float) -> str:
    L = result["layers"]
    lines = []
    lines.append(f"Periportal pole inferred at Layer {result['periportal_pole_layer']} "
                 f"(opposite end = pericentral; from landmark genes)")
    lines.append(f"Gate atoms (required by all {result['routes']} routes): {result['gate']}")
    lines.append(f"Relative-expression threshold: profile/peak >= {threshold}\n")
    lines.append("layer  zone         gluconeogenesis  missing-gate")
    for row in L:
        flag = "SATISFIABLE" if row["satisfiable"] else "blocked    "
        lines.append(f"  L{row['layer']}   {row['zone']:11s}  {flag}      {row['missing_gate']}")
    sat_zones = sorted({r["zone"] for r in L if r["satisfiable"]})
    blk_zones = sorted({r["zone"] for r in L if not r["satisfiable"]})
    lines.append(f"\nSatisfiable zones: {sat_zones}")
    lines.append(f"Blocked zones:     {blk_zones}")
    # Validation: pericentral pole must be blocked, periportal pole satisfiable.
    pole = next(r for r in L if r["layer"] == result["periportal_pole_layer"])
    central = next(r for r in L if r["layer"] == (1 if result["periportal_pole_layer"] > 1 else N_LAYERS))
    lines.append("\n== Validation ==")
    lines.append(f"  periportal pole (L{pole['layer']}) satisfiable: {pole['satisfiable']}  (expect True)")
    lines.append(f"  pericentral pole (L{central['layer']}) satisfiable: {central['satisfiable']}  (expect False)")
    return "\n".join(lines) + "\n"


def sweep(module_path: str, thresholds) -> str:
    lines = ["\n== Threshold sweep: satisfiable layers (L1=pericentral .. L9=periportal) =="]
    for t in thresholds:
        res = resolve(module_path, t)
        bar = "".join("#" if r["satisfiable"] else "." for r in res["layers"])
        sat = [r["layer"] for r in res["layers"] if r["satisfiable"]]
        lines.append(f"  rel>={t:<4}  {bar}   layers={sat}")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("module", nargs="?",
                    default=str(Path(__file__).parents[2] / "gluconeogenesis_human.yaml"))
    ap.add_argument("--threshold", type=float, default=0.5)
    args = ap.parse_args()
    print(format_report(resolve(args.module, args.threshold), args.threshold))
    print(sweep(args.module, [0.3, 0.5, 0.7, 0.9]))
