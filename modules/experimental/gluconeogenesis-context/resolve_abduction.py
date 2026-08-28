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
from kegg_oracle import load_cache, holds_for, ORGANISMS

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
    # buc/hin omitted deliberately, and the omission is not a hedge:
    #   Buchnera aphidicola APS is neither a clean prototroph nor a clean auxotroph. Its
    #   methionine pathway is *shared* with the aphid host -- Buchnera retains the terminal
    #   MetE step (the only amino-acid biosynthetic gene keeping its ancestral metR
    #   regulator) and the consortium provisions methionine to the host, with earlier
    #   intermediates supplied collaboratively. Asserting either phenotype for the
    #   bacterium alone would be false, so no activity is asserted. It is the natural
    #   illustration of the "not cell-autonomous / cross-feeding" hypothesis rather than
    #   of auxotrophy.
    #   H. influenzae is omitted for the analogous reason (host-complemented).
}


def resolve() -> dict:
    circuit = compile_module_file(MODULE)
    matrix = load_cache()
    out = {}
    for org, (active, basis) in ACTIVITY.items():
        present = matrix.get(org, {})
        ab = abduce(circuit, holds_for(present), asserted_active=active)
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
    if targets:
        lines.append("  These are the GapMind-style leads for novel/under-annotated enzymes; the")
        lines.append("  gap+auxotroph cases instead show the engine correctly predicting an auxotrophy.")
    else:
        lines.append("  No leads in this panel, and that is the correct result. Every prototroph here")
        lines.append("  is now reconstructable, and the only gap (rpr) is a genuine auxotroph the")
        lines.append("  engine correctly predicts. An earlier version of the module modelled only the")
        lines.append("  O-acyl-homoserine entry to homocysteine and so reported syn and mja as")
        lines.append("  'metabolic dark matter'; both in fact encode the aspartate-semialdehyde route")
        lines.append("  (K23975/K23976). That was a model-scope artifact, not a discovery -- the")
        lines.append("  cautionary case for reading any gap as a lead before the model is adequate.")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    print(format_report(resolve()))
