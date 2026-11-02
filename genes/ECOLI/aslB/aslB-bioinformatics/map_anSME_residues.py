"""Map the experimentally defined cluster ligands, SAM-binding residues and
catalytic base of the Cys-type anSME from Clostridium perfringens (anSMEcpe,
UniProt Q0TTH1; crystal structures PDB 4K36/4K37/4K38/4K39) onto E. coli AslB
(P25550) and YdeM (P76134), and onto the Ser-type anSME AtsB of Klebsiella
pneumoniae (Q9X758) as a second characterised reference.

Feature positions are parsed at run time from the UniProt flat file of Q0TTH1
(BINDING and ACT_SITE lines), sequences are fetched from UniProt REST, and
pairwise global alignments (BLOSUM62, gap open -10, extend -0.5) are computed
with Biopython. Nothing is hardcoded except accessions.

Usage: uv run python map_anSME_residues.py > map_anSME_residues.out
"""
import re
import sys
import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices

REF = "Q0TTH1"
TARGETS = {"P25550": "AslB (E. coli K-12)", "P76134": "YdeM (E. coli K-12)",
           "Q9X758": "AtsB (K. pneumoniae, Ser-type anSME)"}


def fetch(url):
    with urllib.request.urlopen(url, timeout=60) as r:
        return r.read().decode()


def seq_of(acc):
    fa = fetch(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta")
    return "".join(l.strip() for l in fa.splitlines() if not l.startswith(">"))


def ref_features(acc):
    txt = fetch(f"https://rest.uniprot.org/uniprotkb/{acc}.txt")
    feats = []
    cur = None
    for line in txt.splitlines():
        m = re.match(r"FT   (BINDING|ACT_SITE)\s+(\d+)$", line)
        if m:
            cur = {"type": m.group(1), "pos": int(m.group(2)), "ligand": "", "label": ""}
            feats.append(cur)
            continue
        if line.startswith("FT   ") and not line.startswith("FT    "):
            cur = None
            continue
        if cur is not None:
            for key, pat in (("ligand", r'/ligand="([^"]+)"'), ("label", r'/ligand_label="([^"]+)"'),
                             ("ligand", r'/note="([^"]+)"')):
                mm = re.search(pat, line)
                if mm and not cur[key]:
                    cur[key] = mm.group(1)
    return feats


def aligner():
    a = Align.PairwiseAligner()
    a.mode = "global"
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    return a


def map_positions(aln):
    """Return dict ref_pos(1-based) -> target_pos(1-based) for aligned pairs."""
    mp = {}
    for (rs, re_), (ts, te) in zip(*aln.aligned):
        for i in range(re_ - rs):
            mp[rs + i + 1] = ts + i + 1
    return mp


def identity(aln):
    ident = pairs = 0
    s1, s2 = aln.target, aln.query
    for (rs, re_), (ts, te) in zip(*aln.aligned):
        for i in range(re_ - rs):
            pairs += 1
            ident += s1[rs + i] == s2[ts + i]
    return ident, pairs


def main():
    ref = seq_of(REF)
    feats = ref_features(REF)
    a = aligner()
    print(f"Reference {REF} (anSMEcpe), length {len(ref)}; {len(feats)} BINDING/ACT_SITE features parsed")
    motif = re.search(r"C...C..C", ref)
    print(f"Reference CxxxCxxC motif: {motif.group(0)} at {motif.start()+1}")
    print()
    for acc, name in TARGETS.items():
        tgt = seq_of(acc)
        aln = a.align(ref, tgt)[0]
        mp = map_positions(aln)
        ident, pairs = identity(aln)
        m = re.search(r"C...C..C", tgt)
        print(f"== {acc} {name}, length {len(tgt)}")
        print(f"   identity to {REF}: {ident}/{pairs} aligned pairs = {100*ident/pairs:.1f}%")
        print(f"   first CxxxCxxC motif: {m.group(0) + ' at ' + str(m.start()+1) if m else 'NONE'}")
        print(f"   total Cys: {tgt.count('C')}")
        cons = 0
        for f in feats:
            rres = ref[f["pos"] - 1]
            tpos = mp.get(f["pos"])
            tres = tgt[tpos - 1] if tpos else "-"
            same = tres == rres
            cons += same
            lab = f"{f['type']} {f['ligand']}" + (f" cluster {f['label']}" if f['label'] else "")
            print(f"   {REF} {rres}{f['pos']:<4d} -> {tres}{tpos if tpos else '':<4} {'conserved' if same else 'CHANGED'}  [{lab}]")
        print(f"   conserved: {cons}/{len(feats)} reference features")
        print()
    print("== Pairwise identities among targets")
    seqs = {acc: seq_of(acc) for acc in TARGETS}
    accs = list(TARGETS)
    for i in range(len(accs)):
        for j in range(i + 1, len(accs)):
            aln = a.align(seqs[accs[i]], seqs[accs[j]])[0]
            ident, pairs = identity(aln)
            print(f"   {accs[i]} vs {accs[j]}: {ident}/{pairs} = {100*ident/pairs:.1f}%")


if __name__ == "__main__":
    sys.exit(main())
