# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython", "requests"]
# ///
"""Compare a pseudogene-derived UniProt entry with its functional parent.

Fetches both sequences from UniProt REST, the parent's annotated functional
features (metal-binding / lipidation sites), aligns the two proteins globally,
and reports whether each parent functional residue is retained in the target.
Optionally fetches the target locus genomic sequence from Ensembl and
translates it, to check whether the reading frame is intact on the genome.

Usage:
    uv run compare_to_parent.py TARGET_ACC PARENT_ACC [ENSEMBL_GENE_ID]
"""
import sys

import requests
from Bio import Align
from Bio.Align import substitution_matrices
from Bio.Seq import Seq

UNIPROT = "https://rest.uniprot.org/uniprotkb/{}.json"
ENSEMBL = "https://rest.ensembl.org"
FEATURE_TYPES = {"Binding site", "Lipidation", "Modified residue", "Propeptide"}


def uniprot(acc):
    r = requests.get(UNIPROT.format(acc), timeout=60)
    r.raise_for_status()
    return r.json()


def features(entry):
    out = []
    for f in entry.get("features", []):
        if f["type"] in FEATURE_TYPES:
            start = f["location"]["start"]["value"]
            end = f["location"]["end"]["value"]
            lig = f.get("ligand", {}).get("name", "")
            out.append((f["type"], start, end, lig or f.get("description", "")))
    return out


def align(a, b):
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.mode = "global"
    aln = aligner.align(a, b)[0]
    # map target positions -> parent positions (1-based)
    t2p, p2t = {}, {}
    for (ts, te), (ps, pe) in zip(*aln.aligned):
        for i in range(te - ts):
            t2p[ts + i + 1] = ps + i + 1
            p2t[ps + i + 1] = ts + i + 1
    return aln, t2p, p2t


def genomic_translation(gene_id):
    r = requests.get(
        f"{ENSEMBL}/lookup/id/{gene_id}?expand=1",
        headers={"Content-Type": "application/json"}, timeout=60)
    r.raise_for_status()
    g = r.json()
    print(f"\nEnsembl {gene_id}: {g.get('display_name')} biotype={g['biotype']} "
          f"{g['seq_region_name']}:{g['start']}-{g['end']}:{g['strand']}")
    for t in g.get("Transcript", []):
        print(f"  transcript {t['id']} biotype={t['biotype']} exons={len(t.get('Exon', []))} "
              f"translation={'yes' if t.get('Translation') else 'no'}")
    r = requests.get(f"{ENSEMBL}/sequence/id/{gene_id}?type=genomic",
                     headers={"Content-Type": "text/plain"}, timeout=60)
    r.raise_for_status()
    dna = r.text.strip()
    best = None
    for frame in range(3):
        sub = dna[frame:]
        sub = sub[: len(sub) - len(sub) % 3]
        prot = str(Seq(sub).translate())
        # longest stop-free stretch starting with M
        for seg in prot.split("*"):
            if "M" in seg:
                orf = seg[seg.index("M"):]
                if best is None or len(orf) > len(best[1]):
                    best = (frame, orf)
    return dna, best


def main():
    target, parent = sys.argv[1], sys.argv[2]
    gene_id = sys.argv[3] if len(sys.argv) > 3 else None
    te, pe = uniprot(target), uniprot(parent)
    ts, ps = te["sequence"]["value"], pe["sequence"]["value"]
    print(f"Target {target} ({te['uniProtkbId']}), PE={te['proteinExistence']}, "
          f"length {len(ts)}, seq version {te['entryAudit']['sequenceVersion']}")
    print(f"Parent {parent} ({pe['uniProtkbId']}), PE={pe['proteinExistence']}, "
          f"length {len(ps)}, seq version {pe['entryAudit']['sequenceVersion']}")
    aln, t2p, p2t = align(ts, ps)
    print("\nGlobal alignment (target top, parent bottom):")
    print(aln)
    ident = sum(1 for t, p in t2p.items() if ts[t - 1] == ps[p - 1])
    print(f"Identical aligned positions: {ident} / {len(ps)} parent residues "
          f"({100 * ident / len(ps):.1f}% of parent length); aligned pairs {len(t2p)}")
    print("\nSubstitutions (target pos/res -> parent pos/res):")
    for t, p in sorted(t2p.items()):
        if ts[t - 1] != ps[p - 1]:
            print(f"  target {ts[t-1]}{t}  parent {ps[p-1]}{p}")
    print("\nParent functional features and their status in the target:")
    for ftype, s, e, desc in features(pe):
        for pos in range(s, e + 1):
            tpos = p2t.get(pos)
            tres = ts[tpos - 1] if tpos else "-"
            status = ("RETAINED" if tres == ps[pos - 1] else
                      "ABSENT" if tres == "-" else "SUBSTITUTED")
            print(f"  {ftype:16s} {desc[:30]:30s} parent {ps[pos-1]}{pos} -> "
                  f"target {tres}{tpos or ''}  {status}")
    print("\nTarget features annotated by UniProt:")
    for ftype, s, e, desc in features(te):
        print(f"  {ftype:16s} {s}-{e} {desc}")
    print(f"\nTarget C-terminal 4 residues: {ts[-4:]}; parent: {ps[-4:]}")
    if gene_id:
        dna, best = genomic_translation(gene_id)
        print(f"Genomic span length {len(dna)} nt")
        if best:
            frame, orf = best
            print(f"Longest Met-initiated stop-free ORF of span (feature orientation): frame {frame}, "
                  f"{len(orf)} aa")
            print(f"  {orf}")
            print(f"  identical to UniProt target sequence: {orf == ts}; "
                  f"target contained in ORF: {ts in orf}")


if __name__ == "__main__":
    main()
