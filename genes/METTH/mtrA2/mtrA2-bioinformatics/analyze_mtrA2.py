"""Compare the cytoplasmic MtrA paralog mtrA2 (O27134) with membrane MtrA.

Usage (from this folder): uv run python analyze_mtrA2.py

All sequences and UniProt features are fetched live from the UniProt REST API.
Nothing is hardcoded except the accessions and the reference residue numbers
taken from the literature (His84, Glu54, Ile111 of strain Marburg MtrA, P80184).

Steps
 1. Global alignment (BLOSUM62, open -10, extend -0.5) of O27134 against
    O27227 (mtrA1, Delta H), P80184 (MtrA, strain Marburg), Q58261 (MtrA,
    M. jannaschii) and the M. fervidus MtrA entries (soluble and membrane).
 2. Map the UniProt TRANSMEM features of every sequence onto O27134 through
    the alignment, and report which O27134 residues align to the membrane
    MtrA TRANSMEM segment.
 3. Kyte-Doolittle hydropathy, 19-residue window: maximum window score and
    its position for each sequence (>= 1.6 is the classic TM threshold).
 4. Report the O27134 residue aligned to His84, Glu54 and Ile111 of P80184.
"""
import json
import urllib.request

from Bio.Align import PairwiseAligner, substitution_matrices

TARGET = "O27134"
OTHERS = ["O27227", "P80184", "Q58261"]
FERVIDUS_QUERY = ("https://rest.uniprot.org/uniprotkb/search?"
                  "query=organism_id:523846+AND+gene:mtrA&format=json")
# Residue numbers named in PMID:27324530 / PMID:9461302 (His84 cobalt ligand,
# Glu54 H-bond partner, Ile111 backbone N). Checked on both the strain
# Marburg MtrA and the M. fervidus cytoplasmic homologue (the structure).
REF_RESIDUES = {"His84": 84, "Glu54": 54, "Ile111": 111}
REFS = ["P80184", "E3GWY7"]

KD = {"A": 1.8, "R": -4.5, "N": -3.5, "D": -3.5, "C": 2.5, "Q": -3.5,
      "E": -3.5, "G": -0.4, "H": -3.2, "I": 4.5, "L": 3.8, "K": -3.9,
      "M": 1.9, "F": 2.8, "P": -1.6, "S": -0.8, "T": -0.7, "W": -0.9,
      "Y": -1.3, "V": 4.2}


def get_json(url):
    with urllib.request.urlopen(url) as fh:
        return json.load(fh)


def entry(acc):
    d = get_json(f"https://rest.uniprot.org/uniprotkb/{acc}.json")
    seq = d["sequence"]["value"]
    tms = []
    for f in d.get("features", []):
        if f["type"] == "Transmembrane":
            ev = ";".join(e.get("evidenceCode", "") + "|" + e.get("source", "")
                          + ":" + e.get("id", "") for e in f.get("evidences", []))
            tms.append((f["location"]["start"]["value"],
                        f["location"]["end"]["value"], ev))
    return seq, tms


def kd_max(seq, w=19):
    best = (-99, 0)
    for i in range(len(seq) - w + 1):
        s = sum(KD.get(c, 0) for c in seq[i:i + w]) / w
        if s > best[0]:
            best = (s, i + 1)
    return best


def window_kd(seq, start, end):
    sub = seq[start - 1:end]
    return sum(KD.get(c, 0) for c in sub) / len(sub)


def align(a, b):
    al = PairwiseAligner()
    al.mode = "global"
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score = -10
    al.extend_gap_score = -0.5
    # free end gaps: a C-terminal extension in one sequence is not forced
    # to align a stray residue of the other
    al.end_gap_score = 0
    aln = al.align(a, b)[0]
    amap = {}  # 1-based pos in b -> 1-based pos in a
    ident = cols = 0
    for (s1, e1), (s2, e2) in zip(*aln.aligned):
        for i, j in zip(range(s1, e1), range(s2, e2)):
            amap[j + 1] = i + 1
            cols += 1
            ident += a[i] == b[j]
    return aln, amap, ident, cols


def main():
    seqs, tms = {}, {}
    for acc in [TARGET] + OTHERS:
        seqs[acc], tms[acc] = entry(acc)
    for r in get_json(FERVIDUS_QUERY)["results"]:
        acc = r["primaryAccession"]
        seqs[acc], tms[acc] = entry(acc)
        OTHERS.append(acc)

    t = seqs[TARGET]
    print(f"## Sequences\n")
    for acc, s in seqs.items():
        cls = "cytoplasmic-type (<215 aa)" if len(s) < 215 else "membrane-type"
        km, kp = kd_max(s)
        print(f"{acc}: {len(s)} aa, {cls}; UniProt TRANSMEM={tms[acc] or 'none'}; "
              f"max KD(19)={km:.2f} at {kp}-{kp+18}")

    print("\n## UniProt TRANSMEM on O27134: hydropathy of the segment\n")
    for s, e, ev in tms[TARGET]:
        print(f"O27134 TRANSMEM {s}-{e} ({ev}): {t[s-1:e]}  mean KD={window_kd(t, s, e):.2f}")

    print("\n## Pairwise alignments with O27134\n")
    for acc in OTHERS:
        o = seqs[acc]
        aln, amap, ident, cols = align(t, o)
        last_t = max(amap) if amap else 0
        print(f"### O27134 vs {acc} ({len(o)} aa): identity {ident}/{cols} = "
              f"{100*ident/cols:.1f}% over aligned columns; last {acc} residue "
              f"aligned to O27134 = {last_t}; {acc} residues after it = {len(o)-last_t}")
        for s, e, ev in tms[acc]:
            hit = [amap[p] for p in range(s, e + 1) if p in amap]
            print(f"  {acc} TRANSMEM {s}-{e}: {len(hit)}/{e-s+1} residues aligned to O27134"
                  + (f" (O27134 {min(hit)}-{max(hit)})" if hit else ""))
        rev = {v: k for k, v in amap.items()}
        for s, e, ev in tms[TARGET]:
            hit = [rev[p] for p in range(s, e + 1) if p in rev]
            if hit:
                print(f"  O27134 TRANSMEM {s}-{e} aligns to {acc} {min(hit)}-{max(hit)}: "
                      f"{o[min(hit)-1:max(hit)]}")
        if acc in REFS:
            for name, pos in REF_RESIDUES.items():
                tp = amap.get(pos)
                print(f"  literature {name}: {acc} residue {pos} is {o[pos-1]}; -> O27134 "
                      + (f"{t[tp-1]}{tp}" if tp else "gap"))
        print()
        print(aln)


if __name__ == "__main__":
    main()
