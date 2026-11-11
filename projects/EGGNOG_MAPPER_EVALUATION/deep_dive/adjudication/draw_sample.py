#!/usr/bin/env python3
"""Deep-dive adjudication sample, from the default run (for these genomes the
species-excluded run is nearly identical: eggNOG holds almost no GO of their own).

Per genome: P. putida 14 UNRELATED + 5 NARROWER + 5 REJECTED; horse 12 UNRELATED
+ 4 NARROWER; poplar 10 UNRELATED + 6 NARROWER; pennycress every leaf that is not
EXACT (4 genes only). At most one leaf per protein per category; fixed seed.
Writes <ORG>.yaml per genome."""
import csv
import os
import random

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
SEED = 20261018
QUOTA = {"PSEPK": {"UNRELATED": 14, "NARROWER": 5, "REJECTED": 5},
         "HORSE": {"UNRELATED": 12, "NARROWER": 4},
         "POPTR": {"UNRELATED": 10, "NARROWER": 6},
         "THLAR": None}
rows = list(csv.DictReader(open(os.path.join(HERE, "..", "results", "default_leaf_scores.tsv")), delimiter="\t"))
rng = random.Random(SEED)


def claim(r, cid):
    return {"claim_id": cid, "category": r["category"], "accession": r["accession"], "gene": r["gene"],
            "organism_dir": r["organism_dir"], "aspect": r["aspect"],
            "term": {"id": r["term_id"], "label": r["term_label"]},
            "review_file": f"genes/{r['organism_dir']}/{r['gene']}/{r['gene']}-ai-review.yaml",
            "assessment": None, "error_type": None, "rationale": None, "evidence": None}


for org, quota in QUOTA.items():
    org_rows = [r for r in rows if r["organism_dir"] == org]
    claims = []
    if quota is None:
        for i, r in enumerate(sorted((r for r in org_rows if r["category"] != "EXACT"),
                                     key=lambda r: (r["gene"], r["term_id"])), 1):
            claims.append(claim(r, f"{org}-{i:02d}"))
    else:
        for cat, n in quota.items():
            by_prot = {}
            for r in org_rows:
                if r["category"] == cat:
                    by_prot.setdefault(r["accession"], []).append(r)
            picks = rng.sample(sorted(by_prot), min(n, len(by_prot)))
            for i, acc in enumerate(picks, 1):
                claims.append(claim(rng.choice(by_prot[acc]), f"{org}-{cat[:3]}-{i:02d}"))
    with open(os.path.join(HERE, f"{org}.yaml"), "w") as fh:
        yaml.safe_dump({"claims": claims}, fh, sort_keys=False, width=100)
    print(org, len(claims))
