"""Align human ASPHD2 (Q6ICH7) to the catalytic domain of aspartyl/asparaginyl
beta-hydroxylase ASPH (Q12797) and report, for each Fe(II)- and 2-oxoglutarate-
binding residue annotated in the live UniProt ASPH entry, the aligned ASPHD2
residue plus a local sequence window, so that gap-placement offsets are visible.

Sequences and features are fetched from UniProt at run time.
"""
import json
import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices

REF, TGT = "Q12797", "Q6ICH7"


def get(url: str) -> str:
    with urllib.request.urlopen(url) as r:
        return r.read().decode()


def seq(acc: str) -> str:
    return "".join(get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta").splitlines()[1:])


def sites(acc: str) -> list[tuple[int, int, str]]:
    d = json.loads(get(f"https://rest.uniprot.org/uniprotkb/{acc}.json"))
    out = []
    for f in d.get("features", []):
        if f["type"] in ("Active site", "Binding site"):
            lig = (f.get("ligand") or {}).get("name", "")
            if "Ca" in lig:
                continue
            out.append((f["location"]["start"]["value"], f["location"]["end"]["value"], lig))
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
            m[rs + k + 1] = ts + k + 1
    ident = sum(1 for p, t in m.items() if ref[p - 1] == tgt[t - 1])
    print(f"ASPH ({REF}) length {len(ref)}; ASPHD2 ({TGT}) length {len(tgt)}")
    print(f"Local alignment: ASPH {min(m)}-{max(m)} vs ASPHD2 {min(m.values())}-{max(m.values())}; "
          f"{len(m)} aligned positions, {ident} identical ({100*ident/len(m):.1f}%)")
    for s, e, lig in sites(REF):
        for pos in range(s, e + 1):
            t = m.get(pos)
            state = f"ASPHD2 {tgt[t-1]}{t} ({'conserved' if tgt[t-1]==ref[pos-1] else 'substituted'})" if t else "not aligned"
            lo, hi = pos - 6, pos + 6
            rw = ref[lo - 1:hi]
            tw = "".join(tgt[m[p] - 1] if p in m else "-" for p in range(lo, hi + 1))
            print(f"ASPH {ref[pos-1]}{pos} ({lig}): {state}   ASPH {lo}-{hi} {rw} / ASPHD2 {tw}")


if __name__ == "__main__":
    main()
