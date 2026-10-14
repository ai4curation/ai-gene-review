#!/usr/bin/env python3
"""Split an emapper .seed_orthologs file by the species taxid of each query
(from cohort_species_taxa.yaml) into OUT_DIR/<taxid>.seed_orthologs."""
import os
import sys

import yaml

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sp = yaml.safe_load(open(os.path.join(HERE, "cohort_species_taxa.yaml")))["species_taxid"]
seeds, out_dir = sys.argv[1], sys.argv[2]
os.makedirs(out_dir, exist_ok=True)
header, groups = [], {}
for line in open(seeds):
    if line.startswith("#"):
        header.append(line)
        continue
    groups.setdefault(sp[line.split("\t", 1)[0]], []).append(line)
for taxid, lines in groups.items():
    with open(os.path.join(out_dir, f"{taxid}.seed_orthologs"), "w") as fh:
        fh.writelines(header + lines)
print(len(groups), "species files")
