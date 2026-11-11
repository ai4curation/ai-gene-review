#!/usr/bin/env python3
"""Draw the manual-adjudication sample from the species-excluded run.

At most one leaf per protein and per category; fixed seed. Writes
batch_<n>.yaml (20 claims each) with empty assessment fields for reviewers."""
import csv
import os
import random

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
SEED = 20261014
QUOTA = {"UNRELATED": 40, "REJECTED": 20, "NARROWER": 20}
rows = list(csv.DictReader(open(os.path.join(HERE, "..", "results",
                                             "species_excluded_leaf_scores.tsv")), delimiter="\t"))
rng = random.Random(SEED)
claims = []
for cat, n in QUOTA.items():
    by_prot = {}
    for r in rows:
        if r["category"] == cat:
            by_prot.setdefault(r["accession"], []).append(r)
    prots = rng.sample(sorted(by_prot), min(n, len(by_prot)))
    for acc in prots:
        r = rng.choice(by_prot[acc])
        claims.append({
            "claim_id": f"{cat[:3]}-{len([c for c in claims if c['category'] == cat]) + 1:02d}",
            "category": cat, "accession": acc, "gene": r["gene"],
            "organism_dir": r["organism_dir"], "aspect": r["aspect"],
            "term": {"id": r["term_id"], "label": r["term_label"]},
            "review_file": f"genes/{r['organism_dir']}/{r['gene']}/{r['gene']}-ai-review.yaml",
            "assessment": None, "error_type": None, "rationale": None, "evidence": None})
rng.shuffle(claims)
for i in range(0, len(claims), 20):
    with open(os.path.join(HERE, f"batch_{i // 20 + 1}.yaml"), "w") as fh:
        yaml.safe_dump({"claims": claims[i:i + 20]}, fh, sort_keys=False, width=100)
print(len(claims), "claims")
