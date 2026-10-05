"""Align human ASPDH (A6ND91) to two structurally characterized L-aspartate
dehydrogenases, Thermotoga maritima (Q9X1X6) and Archaeoglobus fulgidus (O28440),
and report which of their active-site and NAD(+)-binding residues are conserved
in ASPDH, using the residue annotations in the live UniProt entries.

Sequences and features are fetched from UniProt at run time.
"""
import json
import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices

TGT = "A6ND91"
REFS = ["Q9X1X6", "O28440"]


def get(url: str) -> str:
    with urllib.request.urlopen(url) as r:
        return r.read().decode()


def seq(acc: str) -> str:
    return "".join(get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta").splitlines()[1:])


def sites(acc: str) -> list[tuple[str, int, int, str]]:
    d = json.loads(get(f"https://rest.uniprot.org/uniprotkb/{acc}.json"))
    out = []
    for f in d.get("features", []):
        if f["type"] in ("Active site", "Binding site"):
            s = f["location"]["start"]["value"]
            e = f["location"]["end"]["value"]
            lig = (f.get("ligand") or {}).get("name", f.get("description", ""))
            out.append((f["type"], s, e, lig))
    return out


def main() -> None:
    tgt = seq(TGT)
    al = Align.PairwiseAligner()
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score, al.extend_gap_score = -10, -0.5
    al.mode = "global"
    print(f"ASPDH ({TGT}) length {len(tgt)}")
    for ref_acc in REFS:
        ref = seq(ref_acc)
        best = al.align(ref, tgt)[0]
        m = {}
        for (rs, re_), (ts, _) in zip(*best.aligned):
            for k in range(re_ - rs):
                m[rs + k + 1] = (ts + k + 1, tgt[ts + k])
        ident = sum(1 for p, (_, aa) in m.items() if ref[p - 1] == aa)
        print(f"\n{ref_acc} length {len(ref)}; {len(m)} aligned positions, {ident} identical ({100*ident/len(m):.1f}%)")
        for typ, s, e, lig in sites(ref_acc):
            for pos in range(s, e + 1):
                hit = m.get(pos)
                if hit:
                    flag = "conserved" if hit[1] == ref[pos - 1] else "substituted"
                    state = f"ASPDH {hit[1]}{hit[0]} ({flag})"
                else:
                    state = "gap in ASPDH"
                print(f"  {typ:12s} {ref_acc} {ref[pos-1]}{pos} ({lig}): {state}")


if __name__ == "__main__":
    main()


def window(ref_acc: str, center: int, flank: int = 8) -> None:
    """Print the pairwise alignment around a reference position."""
    ref, tgt = seq(ref_acc), seq(TGT)
    al = Align.PairwiseAligner()
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score, al.extend_gap_score = -10, -0.5
    al.mode = "global"
    best = al.align(ref, tgt)[0]
    m = {}
    for (rs, re_), (ts, _) in zip(*best.aligned):
        for k in range(re_ - rs):
            m[rs + k + 1] = ts + k + 1
    lo, hi = center - flank, center + flank
    r = "".join(ref[p - 1] for p in range(lo, hi + 1))
    t = "".join(tgt[m[p] - 1] if p in m else "-" for p in range(lo, hi + 1))
    print(f"{ref_acc} {lo}-{hi}: {r}")
    print(f"ASPDH aligned : {t}")


def quinolinate_synthase_in_mammals() -> None:
    """The bacterial aspartate route to NAD+ needs quinolinate synthase (NadA, EC 2.5.1.72)
    downstream of L-aspartate dehydrogenase/oxidase. Count UniProt entries with that EC
    in human and in mammals."""
    for label, q in [("E. coli K-12 (positive control)", "organism_id:83333"), ("human", "organism_id:9606"), ("Mammalia", "taxonomy_id:40674")]:
        url = f"https://rest.uniprot.org/uniprotkb/search?query=(ec:2.5.1.72)+AND+({q})&fields=accession&format=tsv&size=500"
        n = len([l for l in get(url).splitlines()[1:] if l.strip()])
        print(f"UniProt entries with EC 2.5.1.72 (quinolinate synthase) in {label}: {n}")


if __name__ == "__main__":
    print()
    quinolinate_synthase_in_mammals()
    print("\nWindows around the annotated catalytic histidine:")
    window("Q9X1X6", 193)
    window("O28440", 189)
