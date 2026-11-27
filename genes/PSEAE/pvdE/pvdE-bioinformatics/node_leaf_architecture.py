"""Domain architecture of the leaves that receive the PTN000656738 IBA.

Reads the PANTHER leaf IBA GAF cached by projects/PSEUDOCAP/build_iba_seed_worklist.py
(.cache/paint/leaf.gaf.gz), selects the leaf IBAs propagated from PTN000656738 for
GO:0042626, then fetches each leaf's UniProt record (length, TRANSMEM features,
Pfam xrefs) from rest.uniprot.org and classifies its architecture:

  FULL_TMD_NBD : has ABC_membrane (PF00664) or >=4 TM helices AND ABC_tran (PF00005)
  NBD_ONLY     : ABC_tran present, no TM helices, no ABC_membrane
  OTHER        : anything else

Usage: uv run python node_leaf_architecture.py [path/to/leaf.gaf.gz] > leaf_architecture.tsv
"""
import csv
import gzip
import io
import sys
import urllib.parse
import urllib.request
from collections import Counter

NODE = "PTN000656738"
TERM = "GO:0042626"


def leaves(path):
    out = {}
    with gzip.open(path, "rt") as fh:
        for line in fh:
            if NODE not in line:
                continue
            f = line.rstrip("\n").split("\t")
            if len(f) > 7 and f[4] == TERM and NODE in f[7]:
                out[f[1]] = (f[2], f[12])
    return out


def fetch(accs):
    rows = {}
    accs = list(accs)
    for i in range(0, len(accs), 50):
        q = " OR ".join(f"accession:{a}" for a in accs[i : i + 50])
        url = (
            "https://rest.uniprot.org/uniprotkb/search?"
            + urllib.parse.urlencode(
                {
                    "query": q,
                    "fields": "accession,protein_name,length,ft_transmem,xref_pfam",
                    "format": "tsv",
                    "size": 500,
                }
            )
        )
        with urllib.request.urlopen(url, timeout=120) as r:
            for row in csv.DictReader(io.StringIO(r.read().decode()), delimiter="\t"):
                rows[row["Entry"]] = row
    return rows


def classify(row):
    pf = row.get("Pfam", "") or ""
    ntm = (row.get("Transmembrane", "") or "").count("TRANSMEM")
    nbd = "PF00005" in pf
    tmd = "PF00664" in pf or ntm >= 4
    if nbd and tmd:
        return "FULL_TMD_NBD", ntm
    if nbd and ntm == 0 and "PF00664" not in pf:
        return "NBD_ONLY", ntm
    return "OTHER", ntm


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else ".cache/paint/leaf.gaf.gz"
    lv = leaves(path)
    up = fetch(lv)
    counts = Counter()
    w = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    w.writerow(["accession", "symbol", "taxon", "protein_name", "length", "n_tm", "pfam", "architecture"])
    for acc, (sym, taxon) in sorted(lv.items(), key=lambda x: x[1][0]):
        row = up.get(acc)
        if row is None:
            arch, ntm, name, length, pf = "NOT_FOUND", "", "", "", ""
        else:
            arch, ntm = classify(row)
            name, length, pf = row["Protein names"], row["Length"], row.get("Pfam", "")
        counts[arch] += 1
        w.writerow([acc, sym, taxon, name, length, ntm, pf, arch])
    print(f"# total leaves: {len(lv)}; " + "; ".join(f"{k}={v}" for k, v in sorted(counts.items())), file=sys.stderr)


if __name__ == "__main__":
    main()
