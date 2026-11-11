#!/usr/bin/env python3
"""Round 2 of the manual adjudication: failure-mode examples stratified by GO aspect.

From the species-excluded run, per aspect (MF, BP, CC): 12 UNRELATED, 6 REJECTED
and 6 NARROWER leaves, at most one per protein per aspect, never from a protein
already sampled in round 1. Fixed seed. Writes round2_batch_<n>.yaml (18 claims each)."""
import csv
import glob
import os
import random

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
SEED = 20261018
QUOTA = {"UNRELATED": 12, "REJECTED": 6, "NARROWER": 6}
done = set()
for path in glob.glob(os.path.join(HERE, "batch_*.yaml")):
    done |= {c["accession"] for c in yaml.safe_load(open(path))["claims"]}
rows = [r for r in csv.DictReader(open(os.path.join(HERE, "..", "results",
                                                    "species_excluded_leaf_scores.tsv")), delimiter="\t")
        if r["accession"] not in done]
rng = random.Random(SEED)
claims = []
for aspect in ("MF", "BP", "CC"):
    used = set()
    for cat, n in QUOTA.items():
        by_prot = {}
        for r in rows:
            if r["aspect"] == aspect and r["category"] == cat and r["accession"] not in used:
                by_prot.setdefault(r["accession"], []).append(r)
        for i, acc in enumerate(rng.sample(sorted(by_prot), min(n, len(by_prot))), 1):
            used.add(acc)
            r = rng.choice(by_prot[acc])
            claims.append({
                "claim_id": f"R2-{aspect}-{cat[:3]}-{i:02d}", "category": cat,
                "accession": acc, "gene": r["gene"], "organism_dir": r["organism_dir"],
                "aspect": aspect, "term": {"id": r["term_id"], "label": r["term_label"]},
                "review_file": f"genes/{r['organism_dir']}/{r['gene']}/{r['gene']}-ai-review.yaml",
                "assessment": None, "error_type": None, "rationale": None, "evidence": None})
rng.shuffle(claims)
for i in range(0, len(claims), 18):
    with open(os.path.join(HERE, f"round2_batch_{i // 18 + 1}.yaml"), "w") as fh:
        yaml.safe_dump({"claims": claims[i:i + 18]}, fh, sort_keys=False, width=100)
print(len(claims), "claims")
