#!/usr/bin/env python
"""Resolve methionine biosynthesis per genome (GapMind-style reconstruction).

Same module satisfiability engine as the tissue/zonation resolvers, but the context
is now a whole genome and the oracle is KEGG ortholog presence. For each organism the
engine reports whether methionine biosynthesis is reconstructable, which route is
encoded (the present branch at each step), and -- when it is not -- which step is the
gap (no candidate present), exactly as GapMind flags missing steps.
"""

from __future__ import annotations

from pathlib import Path

from ai_gene_review.module_logic import (
    compile_module_file, enumerate_routes, active_routes, is_satisfied,
    unsatisfied_steps, step_id,
)
from kegg_oracle import load_cache, holds_for, ORGANISMS, STEP_KO

MODULE = Path(__file__).parents[2] / "methionine_biosynthesis.yaml"


def route_signature(route_symbols: set[str]) -> str:
    """Human-readable route description from the genes actually on the route.

    Every branch is decided by a gene that is *present*, never by an ``else``
    default: an unrecognised combination reports ``(?)`` rather than silently
    borrowing the label of a route the organism does not use.

    >>> route_signature({"metA", "metB", "metC", "metE"})
    'metA(succinyl) | trans-sulfuration(metB+metC) | metE(no-B12)'
    >>> route_signature({"MJ0100", "MJ0099", "metH"})
    'aspartate-semialdehyde sulfurtransfer (MJ0100+MJ0099) | metH(B12)'
    """
    if "MJ0100" in route_symbols:
        homocysteine = "aspartate-semialdehyde sulfurtransfer (MJ0100+MJ0099)"
    else:
        acyl = ("metA(succinyl)" if "metA" in route_symbols
                else "metX(acetyl)" if "metX" in route_symbols
                else "acylation(?)")
        sulfur = ("trans-sulfuration(metB+metC)" if {"metB", "metC"} <= route_symbols
                  else "direct(metY)" if "metY" in route_symbols
                  else "direct(metZ)" if "metZ" in route_symbols
                  else "sulfur-incorporation(?)")
        homocysteine = f"{acyl} | {sulfur}"
    methyl = ("metH(B12)" if "metH" in route_symbols
              else "metE(no-B12)" if "metE" in route_symbols
              else "methylation(?)")
    return f"{homocysteine} | {methyl}"


def resolve() -> dict:
    circuit = compile_module_file(MODULE)
    matrix = load_cache()
    routes = enumerate_routes(circuit)

    out = {}
    for org in ORGANISMS:
        present = matrix.get(org, {})
        holds = holds_for(present)

        found = is_satisfied(circuit, holds)
        ar = active_routes(circuit, holds)
        gaps = [step_id(s) for s in unsatisfied_steps(circuit, holds)]
        sigs = sorted({route_signature({a.gene_symbol for a in r}) for r in ar})
        present_genes = sorted(g for g in STEP_KO if present.get(g))
        out[org] = {"found": found, "n_routes": len(ar), "routes": sigs,
                    "gaps": gaps, "present_genes": present_genes}
    return {"total_routes": len(routes), "organisms": out}


def format_report(result: dict) -> str:
    lines = [f"Module: methionine biosynthesis   "
             f"({result['total_routes']} route combinations enumerated)\n"]
    for org, label in ORGANISMS.items():
        r = result["organisms"][org]
        status = "FOUND" if r["found"] else "GAP"
        lines.append(f"[{status:5s}] {org}  {label}")
        lines.append(f"          present: {r['present_genes']}")
        if r["found"]:
            lines.append(f"          routes ({r['n_routes']}):")
            for s in r["routes"]:
                lines.append(f"            - {s}")
        else:
            lines.append(f"          missing steps (gaps): {r['gaps']}")
        lines.append("")

    # Validation against known biology.
    org = result["organisms"]
    lines.append("== Validation ==")
    lines.append(f"  prototrophs found (eco,bsu,hin,cgl): "
                 f"{all(org[o]['found'] for o in ['eco', 'bsu', 'hin', 'cgl'])} (expect True)")
    lines.append(f"  Buchnera (buc) is a gap: {not org['buc']['found']} (expect True)")
    lines.append(f"  E. coli uses succinyl acylation: "
                 f"{'metA' in org['eco']['present_genes']} (expect True)")
    lines.append(f"  H. influenzae uses acetyl acylation (metX, not metA): "
                 f"{'metX' in org['hin']['present_genes'] and 'metA' not in org['hin']['present_genes']} (expect True)")
    lines.append(f"  C. glutamicum uses direct sulfhydrylation (metY): "
                 f"{'metY' in org['cgl']['present_genes']} (expect True)")
    lines.append(f"  Synechocystis + M. jannaschii found via the homoserine-independent "
                 f"aspartate-semialdehyde route: "
                 f"{all(org[o]['found'] and 'MJ0100' in org[o]['present_genes'] for o in ['syn', 'mja'])}"
                 f" (expect True)")
    lines.append(f"  neither uses a canonical acyltransferase: "
                 f"{not any({'metA', 'metX'} & set(org[o]['present_genes']) for o in ['syn', 'mja'])}"
                 f" (expect True)")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    print(format_report(resolve()))
