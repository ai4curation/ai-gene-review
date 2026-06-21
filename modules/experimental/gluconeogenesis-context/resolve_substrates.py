#!/usr/bin/env python
"""Resolve WHICH gluconeogenic precursor each tissue can use, from GTEx.

Uses the precursor-resolved module (gluconeogenesis_human_substrates.yaml), whose
routes diverge by carbon source — lactate and alanine enter via pyruvate (needing
PC + PEPCK), glycerol bypasses both — but converge on the shared FBPase + terminal
G6PC1·SLC37A4 gate. Each route is classified by its precursor; a tissue "can use" a
precursor iff at least one satisfiable route through that precursor exists (i.e. the
entry enzymes AND the shared downstream gate are all expressed).

This answers a question bulk pathway-completeness cannot: not just "can this tissue
make glucose?" but "from what?".
"""

from __future__ import annotations

import argparse
from pathlib import Path

from ai_gene_review.module_logic import (
    compile_module_file, enumerate_routes, core_atoms, is_satisfied,
)
from gtex_oracle import load_cache

MODULE = Path(__file__).parents[2] / "gluconeogenesis_human_substrates.yaml"

# Entry-enzyme isozyme sets per precursor (for the quantitative capacity readout).
PRECURSOR_ENTRY = {
    "lactate": {"any": ["LDHA", "LDHB"]},     # either isozyme suffices
    "alanine": {"any": ["GPT", "GPT2"]},      # either isozyme suffices
    "glycerol": {"all": ["GK", "GPD1"]},      # both required
}


def precursor_of(route_symbols: set[str]) -> str:
    if "GK" in route_symbols:
        return "glycerol"
    if route_symbols & {"LDHA", "LDHB"}:
        return "lactate"
    if route_symbols & {"GPT", "GPT2"}:
        return "alanine"
    return "unknown"


def capacity(precursor: str, tissue: str, matrix) -> float:
    """Entry capacity (median TPM) for a precursor in a tissue.

    For an either-isozyme entry, the best isozyme; for an all-required entry, the
    limiting (minimum) enzyme.
    """
    spec = PRECURSOR_ENTRY[precursor]
    vals = [matrix.get(g, {}).get(tissue, 0.0) for g in next(iter(spec.values()))]
    return max(vals) if "any" in spec else min(vals)


def resolve(threshold: float) -> dict:
    circuit = compile_module_file(MODULE)
    tissues, matrix = load_cache()
    routes = enumerate_routes(circuit)
    gate = [a.gene_symbol for a in core_atoms(circuit)]

    out = {}
    for tissue in tissues:
        def holds(atom, _t=tissue):
            s = atom.gene_symbol
            return s is None or matrix.get(s, {}).get(_t, 0.0) >= threshold

        sat = is_satisfied(circuit, holds)
        usable = sorted({
            precursor_of({a.gene_symbol for a in r})
            for r in routes if all(holds(a) for a in r)
        })
        caps = {p: round(capacity(p, tissue, matrix), 1) for p in ["lactate", "alanine", "glycerol"]}
        gate_ok = all(matrix.get(g, {}).get(tissue, 0.0) >= threshold for g in gate)
        out[tissue] = {"satisfiable": sat, "precursors": usable, "capacity": caps,
                       "gate_ok": gate_ok}
    return {"gate": gate, "routes": len(routes), "tissues": out}


def format_report(result: dict, threshold: float) -> str:
    L = result["tissues"]
    lines = [f"Routes: {result['routes']}   Universal gate (all routes): {result['gate']}",
             f"Threshold: median TPM >= {threshold}", ""]
    sat = {t: r for t, r in L.items() if r["satisfiable"]}
    lines.append(f"== Gluconeogenic tissues and the precursors they can use ({len(sat)}) ==")
    lines.append(f"  {'tissue':34s} precursors                 capacity(lac/ala/gly TPM)")
    for t in sorted(sat):
        r = sat[t]
        cap = r["capacity"]
        lines.append(f"  {t:34s} {','.join(r['precursors']):25s} "
                     f"{cap['lactate']:>6}/{cap['alanine']:>5}/{cap['glycerol']:>5}")
    lines.append("\n== Representative gated tissues (no free-glucose output regardless of precursor) ==")
    for t in ["Muscle_Skeletal", "Brain_Cortex", "Adipose_Subcutaneous"]:
        if t in L and not L[t]["satisfiable"]:
            lines.append(f"  {t:34s} gate_ok={L[t]['gate_ok']} (blocked at terminal G6PC1/SLC37A4)")
    # Validation
    liver = L.get("Liver", {})
    muscle = L.get("Muscle_Skeletal", {})
    lines.append("\n== Validation ==")
    lines.append(f"  Liver uses all three precursors: "
                 f"{set(liver.get('precursors', [])) >= {'lactate', 'alanine', 'glycerol'}} (expect True)")
    lines.append(f"  Muscle satisfiable: {muscle.get('satisfiable')} (expect False)")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--threshold", type=float, default=1.0)
    args = ap.parse_args()
    print(format_report(resolve(args.threshold), args.threshold))
