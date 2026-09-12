#!/usr/bin/env python
"""Abduction: reconcile pathway satisfiability with independent activity evidence.

The genome resolver asks "can the engine reconstruct methionine biosynthesis from the
encoded orthologs?". Abduction adds a second, *independent* input: is the organism
actually known to make methionine (does it grow without it)? Crossing the two yields
the GapMind-style payoff:

* found + prototroph    -> CONSISTENT (pathway explained)
* gap   + auxotroph     -> CONSISTENT (engine correctly predicts the auxotrophy)
* gap   + prototroph    -> ABDUCTION TARGET: the organism makes methionine yet a step
                           has no known candidate -> a reviewable hypothesis (novel /
                           unannotated enzyme, or an unmodelled route)
* found + auxotroph     -> OVERPREDICTION (encoded but not realised)

The activity column is independent of the ortholog oracle: it is the organism's
documented growth phenotype on defined media, not anything derived from the gene set.
"""

from __future__ import annotations

from pathlib import Path

from ai_gene_review.module_logic import compile_module_file, abduce
from kegg_oracle import load_cache, ORGANISMS

MODULE = Path(__file__).parents[2] / "methionine_biosynthesis.yaml"

# Independent activity ground truth: can the organism synthesise methionine?
# Basis is the documented growth phenotype on defined media (NOT the gene content),
# so a gap found against it is a genuine prediction rather than a circular restatement.
ACTIVITY = {
    "eco": (True, "prototroph; grows on glucose-minimal (M9) medium without methionine"),
    "bsu": (True, "prototroph; grows on defined minimal medium without methionine"),
    "cgl": (True, "prototroph; industrial amino-acid producer, grows on minimal medium"),
    "syn": (True, "obligate photoautotroph; grows in BG-11 mineral medium (no amino acids)"),
    "mja": (True, "chemolithoautotroph; grows on H2 + CO2 mineral medium (synthesises all amino acids)"),
    "rpr": (False, "obligate intracellular methionine auxotroph; imports methionine from the host"),
    # buc/hin omitted: methionine requirement is contested / host-complemented; not asserted here.
}


def resolve() -> dict:
    circuit = compile_module_file(MODULE)
    matrix = load_cache()
    out = {}
    for org, (active, basis) in ACTIVITY.items():
        present = matrix.get(org, {})

        def holds(atom, _p=present):
            return bool(atom.gene_symbol) and _p.get(atom.gene_symbol, False)

        ab = abduce(circuit, holds, asserted_active=active)
        out[org] = {"abduction": ab, "basis": basis}
    return out


def format_report(result: dict) -> str:
    lines = ["Abduction: engine satisfiability x independent methionine-requirement phenotype\n"]
    order = ["CONSISTENT_ACTIVE", "ABDUCTION_TARGET", "CONSISTENT_INACTIVE", "OVERPREDICTION"]
    for cls in order:
        rows = [(o, r) for o, r in result.items() if r["abduction"].classification == cls]
        if not rows:
            continue
        lines.append(f"== {cls} ==")
        for org, r in rows:
            ab = r["abduction"]
            lines.append(f"  {org}  {ORGANISMS.get(org, org)}")
            lines.append(f"      evidence: {r['basis']}")
            lines.append(f"      engine: satisfiable={ab.satisfiable}  gaps={ab.gap_steps}")
            if ab.classification == "ABDUCTION_TARGET":
                for step, cands in ab.gap_candidates.items():
                    lines.append(f"      PREDICTION @ step '{step}': organism makes methionine but none of "
                                 f"the known candidates {cands} are encoded ->")
                    lines.append("        an unannotated/non-orthologous enzyme (or unmodelled route) must fill it.")
        lines.append("")

    targets = [o for o, r in result.items() if r["abduction"].classification == "ABDUCTION_TARGET"]
    lines.append("== Summary ==")
    lines.append(f"  abduction targets (make methionine but have a pathway gap): {targets}")
    lines.append("  These are the GapMind-style leads for novel/under-annotated enzymes; the")
    lines.append("  gap+auxotroph cases instead show the engine correctly predicting an auxotrophy.")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    print(format_report(resolve()))
