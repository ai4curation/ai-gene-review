#!/usr/bin/env python3
"""Concatenate per-species emapper .annotations files into one file
(one header; each run's ``## `` comment lines dropped)."""
import glob
import os
import sys

src, out = sys.argv[1], sys.argv[2]
header, rows = None, []
for path in sorted(glob.glob(os.path.join(src, "*.emapper.annotations"))):
    for line in open(path):
        if line.startswith("#query"):
            header = line
        elif not line.startswith("#"):
            rows.append(line)
with open(out, "w") as fh:
    fh.write("## merged per-species emapper runs (--excluded_taxa = query species)\n")
    fh.write(header)
    fh.writelines(sorted(rows))
print(len(rows), "rows")
