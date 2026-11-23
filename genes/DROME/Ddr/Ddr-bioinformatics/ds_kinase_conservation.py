"""Conservation of DDR collagen-binding and kinase catalytic residues in Drosophila Ddr.

Downloads canonical sequences from UniProt REST, aligns Drosophila Ddr (Q59DZ7)
against human DDR2 (Q16832) and DDR1 (Q08345) with a global BLOSUM62 alignment,
and reports the fly residue aligned to each human DDR2 residue that lines the
collagen-binding pocket in the DDR2 DS domain-collagen crystal structure
(Carafoli et al. 2009, PMID:20004161), plus canonical kinase motifs.

Run from the repository root:
    uv run python genes/DROME/Ddr/Ddr-bioinformatics/ds_kinase_conservation.py
Nothing is hard-coded except the DDR2 residue list taken from PMID:20004161.
"""
import re
import sys
import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices

ACC = {"fly_Ddr": "Q59DZ7", "human_DDR2": "Q16832", "human_DDR1": "Q08345"}

# Comparators for the residue table (UniProt accessions found by UniProt REST
# search for DDR homologues; unreviewed entries are used only as sequences).
COMPARATORS = {
    "human_DDR1": "Q08345",
    "Dvir_Ddr": "B4LR34",          # Drosophila virilis
    "Agam_DDR": "A0A1S4GZW5",      # Anopheles gambiae
    "Tcas_DDR": "D6WFT6",          # Tribolium castaneum
    "Amel_DDR": "A0A7M7MKP6",      # Apis mellifera
    "Cele_ddr-1": "Q18163",        # C. elegans
    "Cele_ddr-2": "Q95ZV7",        # C. elegans
    "Dmel_Ddr": "Q59DZ7",
}

# Canonical protein-kinase catalytic residues in human DDR2 numbering, located
# here by motif search on the DDR2 sequence (beta3 Lys in VAVK, HRD Asp and the
# catalytic-loop Asn in HRDLATRN, Asp of DFG, DDR activation-loop Tyr triplet).
KINASE_MOTIFS = {"beta3 Lys (VAVK)": (r"VAVK", 3), "HRD Asp": (r"HRDLATRN", 2),
                 "catalytic-loop Asn": (r"HRDLATRN", 7), "DFG Asp": (r"ADFG", 1),
                 "A-loop Tyr 1": (r"YSGDYYR", 0), "A-loop Tyr 2": (r"YSGDYYR", 4),
                 "A-loop Tyr 3": (r"YSGDYYR", 5)}

# DDR2 residues lining the collagen-binding pocket (PMID:20004161, Results).
DDR2_POCKET = {52: "W", 56: "T", 69: "D", 73: "C", 105: "R", 110: "H",
               112: "I", 113: "E", 175: "N", 177: "C"}


def fetch(acc):
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    with urllib.request.urlopen(url, timeout=60) as fh:
        lines = fh.read().decode().splitlines()
    return "".join(l.strip() for l in lines if not l.startswith(">"))


def aligner():
    al = Align.PairwiseAligner()
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score = -10
    al.extend_gap_score = -0.5
    al.mode = "global"
    return al


def position_map(aln):
    """Map 1-based target positions to 1-based query positions (or None)."""
    mapping = {}
    t_idx, q_idx = aln.indices
    for t, q in zip(t_idx, q_idx):
        if t >= 0:
            mapping[t + 1] = (q + 1) if q >= 0 else None
    return mapping


def identity(aln):
    t_idx, q_idx = aln.indices
    pairs = [(t, q) for t, q in zip(t_idx, q_idx) if t >= 0 and q >= 0]
    same = sum(1 for t, q in pairs if aln.target[t] == aln.query[q])
    return same, len(pairs)


def main():
    seqs = {k: fetch(v) for k, v in ACC.items()}
    for k, s in seqs.items():
        print(f"{k} ({ACC[k]}): length {len(s)}")
    al = aligner()
    fly = seqs["fly_Ddr"]
    ddr2 = seqs["human_DDR2"]
    for k in ("DDR2_check",):
        for pos, aa in DDR2_POCKET.items():
            if ddr2[pos - 1] != aa:
                sys.exit(f"DDR2 residue {pos} is {ddr2[pos-1]}, expected {aa}: sequence changed")

    for name in ("human_DDR2", "human_DDR1"):
        aln = al.align(seqs[name], fly)[0]
        same, n = identity(aln)
        print(f"\nGlobal alignment {name} vs fly Ddr: {same}/{n} aligned positions identical "
              f"({100*same/n:.1f}%)")

    # Domain-level identity: DDR2 DS domain (approx. 30-185) and kinase domain (approx. 563-849)
    aln = al.align(ddr2, fly)[0]
    pmap = position_map(aln)
    for label, (a, b) in {"DS domain (DDR2 30-185)": (30, 185),
                          "kinase domain (DDR2 563-849)": (563, 849)}.items():
        same = tot = 0
        for p in range(a, b + 1):
            q = pmap.get(p)
            if q is not None:
                tot += 1
                same += ddr2[p - 1] == fly[q - 1]
        print(f"{label}: {same}/{tot} identical ({100*same/max(tot,1):.1f}%)")

    print("\nDDR2 collagen-pocket residues (PMID:20004161) and aligned fly Ddr residues:")
    conserved = 0
    for pos, aa in DDR2_POCKET.items():
        q = pmap.get(pos)
        fa = fly[q - 1] if q else "-"
        flag = "identical" if fa == aa else "different"
        conserved += fa == aa
        print(f"  DDR2 {aa}{pos} -> fly {fa}{q if q else ''}  [{flag}]")
    print(f"Pocket residues identical: {conserved}/{len(DDR2_POCKET)}")

    print("\nKinase motifs in fly Ddr (regex search):")
    for label, pat in {"VAIK (beta3 Lys)": r"VA[VI]K", "HRD catalytic loop": r"H[RC]D[LV]",
                       "DFG Mg-binding": r"DFG", "APE": r"[AS]PE",
                       "DDR activation-loop YxxxYY": r"Y[A-Z]{3}YY"}.items():
        hits = [(m.start() + 1, m.group()) for m in re.finditer(pat, fly)]
        hits = [h for h in hits if h[0] > 700] if label != "VAIK (beta3 Lys)" else [h for h in hits if h[0] > 700]
        print(f"  {label}: {hits if hits else 'not found'}")


def residue_table():
    al = aligner()
    ddr2 = fetch("Q16832")
    sites = {}
    for pos, aa in DDR2_POCKET.items():
        sites[f"pocket {aa}{pos}"] = pos
    for label, (pat, off) in KINASE_MOTIFS.items():
        mm = re.search(pat, ddr2)
        if mm is None:
            sys.exit(f"motif {pat} not found in DDR2")
        pos = mm.start() + off + 1
        sites[f"{label} {ddr2[pos-1]}{pos}"] = pos
    seqs = {k: fetch(v) for k, v in COMPARATORS.items()}
    maps = {k: position_map(al.align(ddr2, s)[0]) for k, s in seqs.items()}
    names = list(COMPARATORS)
    print("\nResidue table (DDR2 site -> aligned residue in each homologue; global BLOSUM62):")
    print("site\t" + "\t".join(names))
    for label, pos in sites.items():
        row = []
        for k in names:
            q = maps[k].get(pos)
            row.append(f"{seqs[k][q-1]}{q}" if q else "-")
        print(label + "\t" + "\t".join(row))

    # Sequence windows around the aligned beta3-lysine and catalytic-loop positions, and each
    # entry's review status and protein-existence level, so that per-homologue statements in
    # RESULTS.md (e.g. a missing VAxK motif or an HKD loop) can be checked against this output.
    windows = {label: pos for label, pos in sites.items()
               if label.startswith(("beta3 Lys", "HRD Asp", "catalytic-loop Asn", "DFG Asp"))}
    print("\nSequence windows (aligned position marked in brackets; 8 residues either side):")
    for k in names:
        print(f"{k} ({COMPARATORS[k]}; {entry_status(COMPARATORS[k])})")
        for label, pos in windows.items():
            q = maps[k].get(pos)
            if not q:
                print(f"  {label}: -")
                continue
            s = seqs[k]
            lo, hi = max(q - 9, 0), min(q + 8, len(s))
            print(f"  {label}: {lo + 1}-{hi} {s[lo:q-1]}[{s[q-1]}]{s[q:hi]}")


def entry_status(acc):
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.txt"
    with urllib.request.urlopen(url, timeout=60) as fh:
        text = fh.read().decode()
    reviewed = "reviewed" if text.split("\n", 1)[0].split()[2].startswith("Reviewed") else "unreviewed"
    pe = next((l[5:].strip().rstrip(";") for l in text.splitlines() if l.startswith("PE   ")), "PE ?")
    return f"{reviewed}, PE {pe}"


if __name__ == "__main__":
    main()
    residue_table()
