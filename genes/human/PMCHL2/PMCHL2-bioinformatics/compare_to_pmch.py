"""Compare a PMCHL putative product to the parent pro-MCH precursor (PMCH, P20382).

Reproducible: reads the target sequence from the local <GENE>-uniprot.txt and fetches
PMCH (P20382) from the UniProt REST API (feature table included), then:
  1. global/local pairwise alignment (BLOSUM62) of target vs PMCH
  2. maps PMCH features (signal peptide, NGE, NEI, MCH, disulfide) onto the target
  3. reports residue-by-residue comparison inside the NEI and MCH peptides
  4. reports the target N-terminal region not aligned to PMCH and a crude hydropathy
     check (Kyte-Doolittle max 15-residue window mean in the first 35 residues) as a
     proxy for presence/absence of an N-terminal signal peptide.

Usage: uv run python compare_to_pmch.py ../PMCHL1-uniprot.txt
Nothing is hard-coded except the parent accession.
"""
import sys
import re
import urllib.request
from Bio import Align
from Bio.Align import substitution_matrices

PARENT = "P20382"
KD = {'A': 1.8, 'R': -4.5, 'N': -3.5, 'D': -3.5, 'C': 2.5, 'Q': -3.5, 'E': -3.5, 'G': -0.4,
      'H': -3.2, 'I': 4.5, 'L': 3.8, 'K': -3.9, 'M': 1.9, 'F': 2.8, 'P': -1.6, 'S': -0.8,
      'T': -0.7, 'W': -0.9, 'Y': -1.3, 'V': 4.2}


def parse_swiss(text):
    acc = re.search(r"^AC\s+(\w+);", text, re.M).group(1)
    seq = "".join(l.strip().replace(" ", "") for l in text.split("\nSQ ")[1].split("\n")[1:]
                  if l.startswith("     ")).replace("//", "")
    feats = []
    for m in re.finditer(r"^FT   (\w+)\s+(\d+)\.\.(\d+)\n((?:FT {19}.*\n)*)", text, re.M):
        note = re.search(r'/note="([^"]+)"', m.group(4))
        feats.append((m.group(1), int(m.group(2)), int(m.group(3)), note.group(1) if note else ""))
    return acc, seq, feats


def max_kd(seq, start=0, end=35, w=15):
    region = seq[start:end]
    best = max((sum(KD.get(a, 0) for a in region[i:i + w]) / w, i + 1)
               for i in range(0, max(1, len(region) - w + 1)))
    return best


def main(path):
    tacc, tseq, _ = parse_swiss(open(path).read())
    ptext = urllib.request.urlopen(f"https://rest.uniprot.org/uniprotkb/{PARENT}.txt").read().decode()
    pacc, pseq, pfeats = parse_swiss(ptext)
    print(f"Target {tacc} length {len(tseq)}; parent {pacc} (PMCH) length {len(pseq)}\n")

    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score, aligner.extend_gap_score = -10, -0.5
    aligner.mode = "local"
    aln = aligner.align(tseq, pseq)[0]
    print("Local alignment (target top, PMCH bottom):")
    print(aln)
    # position map target->parent
    t2p = {}
    for (ts, te), (ps, pe) in zip(*aln.aligned):
        for k in range(te - ts):
            t2p[ts + k + 1] = ps + k + 1
    p2t = {v: k for k, v in t2p.items()}
    ident = sum(1 for t, p in t2p.items() if tseq[t - 1] == pseq[p - 1])
    print(f"Aligned target span {min(t2p)}-{max(t2p)} <-> PMCH {min(p2t)}-{max(p2t)}; "
          f"identity {ident}/{len(t2p)} = {100*ident/len(t2p):.1f}%")
    print(f"Target residues 1-{min(t2p)-1} do not align to PMCH: {tseq[:min(t2p)-1]}")
    print(f"PMCH residues 1-{min(p2t)-1} have no counterpart in target "
          f"(includes signal peptide and N-terminal pro-region)\n")

    print("PMCH features mapped to target:")
    for ftype, s, e, note in pfeats:
        if ftype not in ("SIGNAL", "PEPTIDE", "DISULFID", "MOD_RES", "CHAIN"):
            continue
        cover = [p2t.get(i) for i in range(s, e + 1)]
        n = sum(1 for c in cover if c)
        print(f"  {ftype:9s} PMCH {s}-{e} {note!r}: {n}/{e-s+1} positions aligned in target")
        if ftype == "PEPTIDE" and n:
            pp = pseq[s - 1:e]
            tt = "".join(tseq[c - 1] if c else "-" for c in cover)
            diffs = [f"{pseq[i-1]}{i}->{tseq[p2t[i]-1]}{p2t[i]}" for i in range(s, e + 1)
                     if p2t.get(i) and pseq[i - 1] != tseq[p2t[i] - 1]]
            print(f"      PMCH  : {pp}\n      target: {tt}\n      substitutions: {diffs or 'none'}")
        if ftype in ("DISULFID", "MOD_RES"):
            for i in sorted({s, e}):
                t = p2t.get(i)
                print(f"      PMCH {pseq[i-1]}{i} -> target {tseq[t-1]+str(t) if t else 'absent'}")
    print()
    kd_t = max_kd(tseq)
    kd_p = max_kd(pseq)
    print(f"Max 15-aa Kyte-Doolittle mean in first 35 aa: target {kd_t[0]:.2f} (start {kd_t[1]}), "
          f"PMCH {kd_p[0]:.2f} (start {kd_p[1]}). Values >~1.6 suggest a hydrophobic signal/TM core.")
    print(f"Target N-terminal 15 aa: {tseq[:15]}; PMCH N-terminal 21 aa (signal): {pseq[:21]}")
    # also check the C-terminal processing site motifs in the target
    for motif in ("KR", "RR", "GRR"):
        print(f"Target occurrences of {motif}: {[m.start()+1 for m in re.finditer(motif, tseq)]}")


if __name__ == "__main__":
    main(sys.argv[1])
