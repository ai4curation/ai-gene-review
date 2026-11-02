#!/usr/bin/env python3
"""Blinded re-check of the claims drawn as REJECTED (anchoring test).

In the original adjudication the reviewer files showed each claim's automatic
category, so the "curators were usually right" result could be anchored on the
label. This re-check takes every adjudicated claim drawn as REJECTED (round 1,
round 2 and the P. putida deep dive) plus an equal number of other adjudicated
claims as distractors (fixed seed), strips the category, gives each an opaque id
and shuffles them into batch_<n>.yaml. The key mapping blind ids to original
claims is written to the path given as the first argument (kept away from the
reviewers until they finish) and is committed afterwards as key.yaml."""
import glob
import os
import random
import sys

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
ADJ = os.path.dirname(HERE)
DEEP = os.path.join(ADJ, "..", "deep_dive", "adjudication")
SEED = 20261019
sources = sorted(glob.glob(os.path.join(ADJ, "batch_*.yaml"))) + \
    sorted(glob.glob(os.path.join(ADJ, "round2_batch_*.yaml"))) + [os.path.join(DEEP, "PSEPK.yaml")]
claims = []
for path in sources:
    for c in yaml.safe_load(open(path))["claims"]:
        c["_source"] = os.path.relpath(path, ADJ)
        claims.append(c)
rejected = [c for c in claims if c["category"] == "REJECTED"]
others = [c for c in claims if c["category"] != "REJECTED"]
rng = random.Random(SEED)
picked = rejected + rng.sample(others, len(rejected))
rng.shuffle(picked)
key, blind = [], []
for i, c in enumerate(picked, 1):
    bid = f"B{i:02d}"
    key.append({"blind_id": bid, "source": c["_source"], "claim_id": c["claim_id"],
                "drawn_as": c["category"], "original_assessment": c["assessment"]})
    blind.append({"blind_id": bid, "accession": c["accession"], "gene": c["gene"],
                  "organism_dir": c["organism_dir"], "aspect": c["aspect"], "term": c["term"],
                  "review_file": c["review_file"],
                  "assessment": None, "error_type": None, "rationale": None, "evidence": None})
n = (len(blind) + 3) // 4
for j in range(0, len(blind), n):
    with open(os.path.join(HERE, f"batch_{j // n + 1}.yaml"), "w") as fh:
        yaml.safe_dump({"claims": blind[j:j + n]}, fh, sort_keys=False, width=100)
with open(sys.argv[1], "w") as fh:
    yaml.safe_dump({"seed": SEED, "key": key}, fh, sort_keys=False)
print(len(rejected), "rejected +", len(picked) - len(rejected), "distractors")
