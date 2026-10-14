"""Per-photoreceptor-type expression of selected genes in the adult zebrafish
photoreceptor single-cell RNA-seq data of Ogawa & Corbo 2021 (PMID:34462505;
GEO GSE175929, sample GSM5351368).

Usage (from repo root):
    uv run python genes/DANRE/prom1a/prom1a-bioinformatics/photoreceptor_scrna.py \
        prom1a prom1b gnat1 gnat2 > .../scrna_output.txt

What it does (nothing hardcoded except marker-gene choices):
  * downloads the 10x matrix, features and barcodes of GSM5351368 from the GEO
    FTP site into .cache/gse175929/ (gitignored);
  * reports the genomic position of each queried gene in the authors' GTF
    (so the gene names used by the authors can be checked against Ensembl);
  * assigns every barcode with enough opsin reads to one photoreceptor type by
    its dominant opsin group (rod: rho; UV: opn1sw1; blue: opn1sw2;
    green: opn1mw1-4; red: opn1lw1-2), and calls bipolar cells from
    cabp5a/vsx1 reads in opsin-negative barcodes;
  * prints, per type, the number of cells, the fraction of cells with >=1 UMI,
    and the mean counts per 10,000 UMIs (CP10K) for each queried gene.

Caveats: this is a marker-based assignment of all barcodes in the deposited
matrix, not the authors' filtered Seurat clustering (2,186 cells); ambient opsin
RNA and doublets are not removed, so small fractions in the "wrong" type are
expected. The ventral opn1mw4/opn1lw1 cone subpopulation is folded into green
and red cones here.
"""

import gzip
import sys
import urllib.request
from collections import defaultdict
from pathlib import Path

import numpy as np
from scipy.io import mmread

ROOT = Path(__file__).resolve().parents[4]
CACHE = ROOT / ".cache" / "gse175929"
BASE = "https://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5351nnn/GSM5351368/suppl/"
FILES = ["GSM5351368_barcodes.tsv.gz", "GSM5351368_features.tsv.gz",
         "GSM5351368_matrix.mtx.gz", "GSM5351368_v432_dr_adult_eye.gtf.gz"]

OPSIN_GROUPS = {
    "rod": ["rho"],
    "UV cone": ["opn1sw1"],
    "blue cone": ["opn1sw2"],
    "green cone": ["opn1mw1", "opn1mw2", "opn1mw3", "opn1mw4"],
    "red cone": ["opn1lw1", "opn1lw2"],
}
BIPOLAR = ["cabp5a", "vsx1"]
MIN_OPSIN_UMI = 5
MIN_DOMINANCE = 0.8


def fetch(name: str) -> Path:
    CACHE.mkdir(parents=True, exist_ok=True)
    p = CACHE / name
    if not p.exists():
        req = urllib.request.Request(BASE + name, headers={"User-Agent": "ai-gene-review"})
        with urllib.request.urlopen(req, timeout=600) as r, open(p, "wb") as fh:
            fh.write(r.read())
    return p


def main(genes: list[str]) -> None:
    paths = {f: fetch(f) for f in FILES}
    feats = [line.split("\t") for line in gzip.open(paths[FILES[1]], "rt").read().splitlines()]
    names = [f[1] for f in feats]
    ids = [f[0] for f in feats]
    idx = defaultdict(list)
    for i, n in enumerate(names):
        idx[n].append(i)
    print(f"# Photoreceptor scRNA-seq (GSE175929 / PMID:34462505): {' '.join(genes)}\n")
    print("## Gene positions in the authors' GTF\n")
    loci = {}
    with gzip.open(paths[FILES[3]], "rt") as fh:
        for line in fh:
            f = line.split("\t")
            if len(f) < 9 or f[2] != "transcript":
                continue
            for g in genes:
                for i in idx.get(g, []):
                    if f'ref_gene_id "{ids[i]}"' in f[8]:
                        lo = loci.setdefault(g, [f[0], int(f[3]), int(f[4])])
                        lo[1], lo[2] = min(lo[1], int(f[3])), max(lo[2], int(f[4]))
    for g in genes:
        print(f"- {g}: feature ids {[ids[i] for i in idx.get(g, [])]}; locus {loci.get(g, 'not found')}")

    m = mmread(str(paths[FILES[2]])).tocsr()  # genes x cells
    if m.shape[0] != len(names):
        m = m.T.tocsr()
    total = np.asarray(m.sum(axis=0)).ravel()
    print(f"\nmatrix: {m.shape[0]} features x {m.shape[1]} barcodes")

    def gsum(gl):
        rows = [i for g in gl for i in idx.get(g, [])]
        return np.asarray(m[rows, :].sum(axis=0)).ravel() if rows else np.zeros(m.shape[1])

    grp = {k: gsum(v) for k, v in OPSIN_GROUPS.items()}
    ops = np.vstack(list(grp.values()))
    optot = ops.sum(axis=0)
    dom = ops.argmax(axis=0)
    frac = np.divide(ops.max(axis=0), optot, out=np.zeros_like(optot, dtype=float), where=optot > 0)
    labels = np.array(["unassigned"] * m.shape[1], dtype=object)
    keys = list(OPSIN_GROUPS)
    ok = (optot >= MIN_OPSIN_UMI) & (frac >= MIN_DOMINANCE)
    for j in np.where(ok)[0]:
        labels[j] = keys[dom[j]]
    bip = gsum(BIPOLAR)
    labels[(optot == 0) & (bip >= 2)] = "bipolar (cabp5a/vsx1)"
    print(f"assignment: opsin UMI >= {MIN_OPSIN_UMI} and dominant opsin group >= {MIN_DOMINANCE:.0%} of opsin UMI;"
          f" bipolar = no opsin UMI and >= 2 cabp5a+vsx1 UMI\n")
    types = keys + ["bipolar (cabp5a/vsx1)"]
    print("## Fraction of cells with >= 1 UMI / mean CP10K\n")
    print("| gene | " + " | ".join(f"{t} (n={int((labels == t).sum())})" for t in types) + " |")
    print("|---|" + "---|" * len(types))
    for g in genes:
        row = []
        rows = idx.get(g, [])
        if not rows:
            print(f"| {g} | " + " | ".join("absent" for _ in types) + " |")
            continue
        counts = np.asarray(m[rows, :].sum(axis=0)).ravel()
        cp10k = np.divide(counts * 1e4, total, out=np.zeros_like(counts, dtype=float), where=total > 0)
        for t in types:
            sel = labels == t
            n = sel.sum()
            row.append(f"{(counts[sel] > 0).mean():.2f} / {cp10k[sel].mean():.1f}" if n else "NA")
        print(f"| {g} | " + " | ".join(row) + " |")

    # Ambient-RNA yardstick: cone transducin (gnat2) in rods and rod transducin
    # (gnat1) in cones show how much of a type-specific transcript leaks into
    # other types in this matrix. A gene whose rod/cone ratio is similar to
    # gnat2's is not distinguishable from ambient signal in rods.
    ref = {g: idx.get(g, []) for g in ("gnat1", "gnat2")}
    if all(ref.values()):
        print("\n## Mean CP10K ratio rod / mean of cone types (ambient yardstick: gnat2, gnat1)\n")
        for g in dict.fromkeys(genes + ["gnat1", "gnat2"]):
            rows = idx.get(g, [])
            if not rows:
                continue
            counts = np.asarray(m[rows, :].sum(axis=0)).ravel()
            cp10k = np.divide(counts * 1e4, total, out=np.zeros_like(counts, dtype=float), where=total > 0)
            rod = cp10k[labels == "rod"].mean()
            cone = np.mean([cp10k[labels == t].mean() for t in keys[1:]])
            print(f"- {g}: rod {rod:.2f}, cone mean {cone:.2f}, rod/cone = {rod / cone if cone else float('nan'):.2f}")


if __name__ == "__main__":
    main(sys.argv[1:])
