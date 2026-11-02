# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83", "requests"]
# ///
"""Compare LITAFD (A0A1B0GVX0) with LITAF (Q99732) and CDIP1 (Q9H305).

Fetches sequences and feature annotations live from UniProt REST, then:
  1. locally aligns LITAFD to each parent's LITAF domain (BLOSUM62);
  2. lists CXXC motifs in each sequence;
  3. maps each parent's annotated Zn(2+)-binding residues onto LITAFD;
  4. reports the longest Kyte-Doolittle hydrophobic window in each LITAF domain
     and maps the parent's annotated membrane-binding region onto LITAFD.
Nothing is hardcoded except accessions and standard scales.
Run: uv run --script litaf_domain_compare.py
"""
import re
import requests
from Bio.Align import PairwiseAligner, substitution_matrices

TARGET = "A0A1B0GVX0"
PARENTS = {"LITAF": "Q99732", "CDIP1": "Q9H305"}
KD = {"A": 1.8, "R": -4.5, "N": -3.5, "D": -3.5, "C": 2.5, "Q": -3.5, "E": -3.5,
      "G": -0.4, "H": -3.2, "I": 4.5, "L": 3.8, "K": -3.9, "M": 1.9, "F": 2.8,
      "P": -1.6, "S": -0.8, "T": -0.7, "W": -0.9, "Y": -1.3, "V": 4.2}


def entry(acc):
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.json", timeout=60)
    r.raise_for_status()
    return r.json()


def features(js, ftype):
    out = []
    for f in js.get("features", []):
        if f["type"] == ftype:
            out.append((f["location"]["start"]["value"], f["location"]["end"]["value"],
                        f.get("description", ""), (f.get("ligand") or {}).get("name", "")))
    return out


def best_kd_window(seq, w=19):
    best = None
    for i in range(len(seq) - w + 1):
        s = sum(KD.get(a, 0) for a in seq[i:i + w]) / w
        if best is None or s > best[0]:
            best = (s, i + 1, i + w)
    return best


def mapping(aln):
    """Return dict parent_pos(1-based) -> target_pos(1-based) for aligned pairs."""
    m = {}
    t_blocks, p_blocks = aln.aligned  # target=LITAFD (seqA), query=parent (seqB)
    for (ts, te), (ps, pe) in zip(t_blocks, p_blocks):
        for k in range(te - ts):
            m[ps + k + 1] = ts + k + 1
    return m


def main():
    aligner = PairwiseAligner()
    aligner.mode = "local"
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5

    tjs = entry(TARGET)
    tseq = tjs["sequence"]["value"]
    print(f"# Target {TARGET} LITAFD, length {len(tseq)}, PE: {tjs.get('proteinExistence')}")
    print(f"CXXC motifs in LITAFD: {[(x.start() + 1, tseq[x.start():x.start() + 4]) for x in re.finditer(r'(?=C..C)', tseq)]}")
    kd = best_kd_window(tseq)
    print(f"LITAFD best 19-aa KD window: {kd[1]}-{kd[2]} mean={kd[0]:.2f} {tseq[kd[1]-1:kd[2]]}")
    print(f"LITAFD Zn-binding features: {features(tjs, 'Binding site')}")
    print(f"LITAFD regions: {features(tjs, 'Region')}")

    for name, acc in PARENTS.items():
        js = entry(acc)
        pseq = js["sequence"]["value"]
        doms = [d for d in features(js, "Domain") if "LITAF" in d[2]]
        print(f"\n## {name} {acc} length {len(pseq)}; LITAF domain feature(s): {doms}")
        aln = aligner.align(tseq, pseq)[0]
        ident = sum(1 for (ts, te), (ps, pe) in zip(*aln.aligned)
                    for k in range(te - ts) if tseq[ts + k] == pseq[ps + k])
        alen = sum(te - ts for ts, te in aln.aligned[0])
        print(f"local alignment score {aln.score:.1f}; aligned pairs {alen}; identities {ident} "
              f"({100 * ident / alen:.1f}% of aligned pairs)")
        print(aln)
        m = mapping(aln)
        print(f"CXXC motifs in {name}: {[(x.start() + 1, pseq[x.start():x.start() + 4]) for x in re.finditer(r'(?=C..C)', pseq)]}")
        zn = [f for f in features(js, "Binding site") if "Zn" in f[3]]
        print(f"{name} annotated Zn(2+) ligands -> LITAFD residue:")
        for s, e, d, lig in zn:
            tp = m.get(s)
            print(f"  {name} {pseq[s-1]}{s} -> " + (f"LITAFD {tseq[tp-1]}{tp}" if tp else "unaligned"))
        for s, e, d, lig in features(js, "Region"):
            if "membrane" in d.lower() or "amphipathic" in d.lower() or "hydrophobic" in d.lower():
                ts = [m[p] for p in range(s, e + 1) if p in m]
                print(f"{name} region {s}-{e} '{d}': {pseq[s-1:e]} -> LITAFD "
                      + (f"{min(ts)}-{max(ts)} {tseq[min(ts)-1:max(ts)]}" if ts else "unaligned"))
        if doms:
            ds, de = doms[0][0], doms[0][1]
            kd = best_kd_window(pseq[ds - 1:de])
            print(f"{name} LITAF-domain best 19-aa KD window: {kd[1]+ds-1}-{kd[2]+ds-1} mean={kd[0]:.2f}")


if __name__ == "__main__":
    main()
