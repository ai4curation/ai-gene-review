"""Compare Svil isoform AG/AH (M9MRN1) with the domain-bearing Svil isoform AE
(X2JAM4) and with human supervillin (O95425).

Reproducible: fetches sequences and InterPro features from UniProt REST at run time.
Usage: python compare_isoforms.py
"""
import json
import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices

UNIPROT = "https://rest.uniprot.org/uniprotkb/{}?format=json"


def fetch(acc):
    with urllib.request.urlopen(UNIPROT.format(acc), timeout=60) as r:
        return json.load(r)


def seq_of(rec):
    return rec["sequence"]["value"]


def domain_features(rec):
    out = []
    for f in rec.get("features", []):
        if f["type"] in ("Domain", "Repeat", "Transmembrane", "Coiled coil"):
            loc = f["location"]
            out.append((f["type"], f.get("description", ""),
                        loc["start"]["value"], loc["end"]["value"]))
    return out


def xrefs(rec, db):
    return [x["id"] for x in rec.get("uniProtKBCrossReferences", []) if x["database"] == db]


def exact_blocks(a, b, k=30):
    """Return maximal exact-match blocks (a_start, b_start, length) of >= k residues, 1-based."""
    index = {}
    for i in range(len(b) - k + 1):
        index.setdefault(b[i:i + k], []).append(i)
    blocks = []
    i = 0
    while i <= len(a) - k:
        hits = index.get(a[i:i + k])
        if not hits:
            i += 1
            continue
        best = (0, None)
        for j in hits:
            n = k
            while i + n < len(a) and j + n < len(b) and a[i + n] == b[j + n]:
                n += 1
            if n > best[0]:
                best = (n, j)
        blocks.append((i + 1, best[1] + 1, best[0]))
        i += best[0]
    return blocks


def main():
    recs = {acc: fetch(acc) for acc in ("M9MRN1", "X2JAM4", "O95425")}
    for acc, rec in recs.items():
        print(f"{acc}\tlength={len(seq_of(rec))}\tInterPro={','.join(xrefs(rec, 'InterPro')) or 'none'}"
              f"\tPfam={','.join(xrefs(rec, 'Pfam')) or 'none'}")
        for feat in domain_features(rec):
            print(f"  feature\t{acc}\t{feat[0]}\t{feat[1]}\t{feat[2]}-{feat[3]}")

    m, x, h = (seq_of(recs[a]) for a in ("M9MRN1", "X2JAM4", "O95425"))
    print("\n# Exact shared blocks (>=30 aa) of M9MRN1 within X2JAM4")
    blocks = exact_blocks(m, x)
    covered = sum(b[2] for b in blocks)
    for b in blocks:
        print(f"  M9MRN1 {b[0]}-{b[0]+b[2]-1}\tX2JAM4 {b[1]}-{b[1]+b[2]-1}\tlen={b[2]}")
    print(f"  M9MRN1 residues in shared blocks: {covered}/{len(m)} ({100*covered/len(m):.1f}%)")
    last_x = max((b[1] + b[2] - 1 for b in blocks), default=0)
    print(f"  Furthest X2JAM4 residue covered by a shared block: {last_x} of {len(x)}")

    aligner = Align.PairwiseAligner()
    aligner.mode = "local"
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -11
    aligner.extend_gap_score = -1
    for name, target in (("O95425 (human SVIL)", h),):
        aln = aligner.align(m, target)[0]
        ident = aligned = 0
        for (qs, qe), (ts, te) in zip(*aln.aligned):
            for qi, ti in zip(range(qs, qe), range(ts, te)):
                aligned += 1
                ident += m[qi] == target[ti]
        q0, q1 = aln.aligned[0][0][0] + 1, aln.aligned[0][-1][1]
        t0, t1 = aln.aligned[1][0][0] + 1, aln.aligned[1][-1][1]
        print(f"\n# Local alignment M9MRN1 vs {name}")
        print(f"  score={aln.score:.0f}\tM9MRN1 {q0}-{q1}\ttarget {t0}-{t1}"
              f"\taligned_pairs={aligned}\tidentity={100*ident/max(aligned,1):.1f}%")


if __name__ == "__main__":
    main()
