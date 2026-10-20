"""Align ASAH2B (P0C7U1) to the full-length neutral ceramidase ASAH2 (Q9NR71) and
report which ASAH2 catalytic and metal-binding residues fall within the aligned
region, using the residue annotations in the live UniProt ASAH2 entry.

Sequences and features are fetched from UniProt at run time.
"""
import json
import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices

REF, TGT = "Q9NR71", "P0C7U1"


def get(url: str) -> str:
    with urllib.request.urlopen(url) as r:
        return r.read().decode()


def seq(acc: str) -> str:
    return "".join(get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta").splitlines()[1:])


def sites(acc: str) -> list[tuple[str, int, str]]:
    d = json.loads(get(f"https://rest.uniprot.org/uniprotkb/{acc}.json"))
    out = []
    for f in d.get("features", []):
        if f["type"] in ("Active site", "Binding site"):
            pos = f["location"]["start"]["value"]
            lig = (f.get("ligand") or {}).get("name", f.get("description", ""))
            out.append((f["type"], pos, lig))
    return out


def main() -> None:
    ref, tgt = seq(REF), seq(TGT)
    al = Align.PairwiseAligner()
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score, al.extend_gap_score = -10, -0.5
    al.mode = "local"
    best = al.align(ref, tgt)[0]
    m = {}
    for (rs, re_), (ts, _) in zip(*best.aligned):
        for k in range(re_ - rs):
            m[rs + k + 1] = (ts + k + 1, tgt[ts + k])
    lo, hi = min(m), max(m)
    ident = sum(1 for p, (_, aa) in m.items() if ref[p - 1] == aa)
    print(f"ASAH2 length {len(ref)}; ASAH2B length {len(tgt)}")
    print(f"Aligned ASAH2 region: {lo}-{hi} ({len(m)} aligned positions, {ident} identical)")
    for typ, pos, lig in sites(REF):
        hit = m.get(pos)
        state = f"aligned to ASAH2B {hit[1]}{hit[0]}" if hit else "outside aligned region"
        print(f"{typ:12s} ASAH2 {ref[pos-1]}{pos} ({lig}): {state}")


if __name__ == "__main__":
    main()
