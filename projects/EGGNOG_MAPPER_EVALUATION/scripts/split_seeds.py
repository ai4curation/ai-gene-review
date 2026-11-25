#!/usr/bin/env python3
"""Split an emapper .seed_orthologs file by the species taxid of each query
(from cohort_species_taxa.yaml) into OUT_DIR/<taxid>.seed_orthologs.

Queries whose taxon is absent from eggNOG's taxonomy (``not_resolved``) are
grouped under the seed ortholog's own taxon instead, which still removes the
query's own eggNOG record from transfer.

Usage: split_seeds.py SEEDS OUT_DIR [BASE_DIR]  (BASE_DIR holds cohort_species_taxa.yaml)"""
import os
import sys

import yaml

HERE = sys.argv[3] if len(sys.argv) > 3 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
meta = yaml.safe_load(open(os.path.join(HERE, "cohort_species_taxa.yaml")))
sp, unresolved = meta["species_taxid"], set(meta["not_resolved"])
seeds, out_dir = sys.argv[1], sys.argv[2]
os.makedirs(out_dir, exist_ok=True)
header, groups = [], {}
for line in open(seeds):
    if line.startswith("#"):
        header.append(line)
        continue
    query, seed = line.split("\t", 2)[:2]
    taxid = int(seed.split(".", 1)[0]) if query in unresolved else sp[query]
    groups.setdefault(taxid, []).append(line)
for taxid, lines in groups.items():
    with open(os.path.join(out_dir, f"{taxid}.seed_orthologs"), "w") as fh:
        fh.writelines(header + lines)
print(len(groups), "species files")
