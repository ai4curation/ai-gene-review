#!/usr/bin/env python3
"""Tabulate results/<ORG>/<source>/summary.json side by side (markdown)."""
import json
import sys
from pathlib import Path

ROWS = [
    ("genes_with_rhea_reactions", "Enzymes with reactions"),
    ("distinct_reactions", "Distinct Rhea reactions"),
    ("network_edges", "Edges"),
    ("giant_component_size", "Giant component"),
    ("isolated_enzymes", "Isolated enzymes"),
    ("enzymes_without_metabolic_bp", "Enzymes with no metabolic BP"),
    ("edge_share_specific_bp", "Linked pairs sharing specific BP"),
    ("same_step_edges", "Same-step edges (shared reaction)"),
    ("same_step_share_specific_bp", "…sharing specific BP"),
    ("handoff_edges", "Handoff edges (no shared reaction)"),
    ("handoff_share_specific_bp", "…sharing specific BP"),
    ("specific_handoff_edges", "Handoffs via a non-hub chemical (≤5 enzymes)"),
    ("specific_handoff_share_specific_bp", "…sharing specific BP"),
    ("random_pair_share_specific_bp", "…random pairs"),
    ("bp_terms_tested", "BP terms tested"),
    ("bp_terms_more_connected_than_random_p<0.05", "BP terms connected > random"),
    ("louvain_communities", "Communities"),
    ("communities_best_bp_f1>=0.5", "Communities ≈ a BP term (F1≥0.5)"),
]
ORDER = ["reviews", "uniprot-rhea-reviewedset", "goa-all-reviewedset", "goa-exp-reviewedset",
         "uniprot-rhea", "goa-all", "goa-noiea", "goa-exp"]

for org in sys.argv[1:]:
    base = Path(__file__).parent / "results" / org
    srcs = [s for s in ORDER if (base / s / "summary.json").exists()]
    S = {s: json.loads((base / s / "summary.json").read_text()) for s in srcs}
    print(f"\n### {org}\n\n| Metric | " + " | ".join(srcs) + " |\n|---|" + "---:|" * len(srcs))
    for k, lab in ROWS:
        print(f"| {lab} | " + " | ".join(str(S[s].get(k, "")) for s in srcs) + " |")
    for k in ("edge_share_specific_bp",):
        print("| Enrichment over random | " + " | ".join(
            f"{S[s][k] / S[s]['random_pair_share_specific_bp']:.1f}×" if S[s]["random_pair_share_specific_bp"] else ""
            for s in srcs) + " |")
