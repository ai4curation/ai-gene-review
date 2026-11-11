"""OAH vs ICL sequence-marker analysis for three fungal PF13714 proteins.

Sequences are fetched live from UniProt / UniParc / RCSB. Each query is globally
aligned to the structurally characterised Cryphonectria parasitica oxaloacetate
acetylhydrolase (UniProtKB:D5LIR7, PDB 3M0J/3M0K; Chen et al. 2010,
PMID:20558740) and to true isocitrate lyases, and we report:

  * percent identity to each reference
  * the residue aligned to every OAH active-site position named in PMID:20558740
  * whether the PROSITE PS00161 (ISOCITRATE_LYASE) pattern KKCGHM/variants is present
  * sequence length (true ICLs are ~530-540 aa, OAH-branch proteins ~320-370 aa)

Only accessions and the reference residue positions are hard-coded; the residue
identities at those positions are read from the fetched D5LIR7 sequence, so a
mismatch with the paper would show up in the output rather than being assumed.

Usage:  uv run python oah_vs_icl_markers.py
"""

import re
import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices

QUERIES = ["A0A5M3MM75", "F8PSW8", "B6HR98"]

REFERENCES = [
    ("D5LIR7", "uniprotkb", "C. parasitica OAH1, structure PMID:20558740"),
    ("UPI00001AA410", "uniparc", "A. niger OahA (ex-UniProtKB:Q7Z986)"),
    ("Q6PNM8", "uniprotkb", "B. cinerea OahA, PMID:17244616"),
    ("Q05957", "uniprotkb", "Dianthus petal death protein, OAH + DMML"),
    ("3FA3", "pdb", "A. niger 2,3-dimethylmalate lyase (DMML)"),
    ("B6HBX9", "uniprotkb", "P. rubens Pc18g05100 paralog, PMID:21549851"),
    ("P28298", "uniprotkb", "A. nidulans isocitrate lyase AcuD"),
    ("P9WKK7", "uniprotkb", "M. tuberculosis isocitrate lyase Icl1"),
    ("P77541", "uniprotkb", "E. coli 2-methylisocitrate lyase PrpB"),
    ("S7Q6Y6", "uniprotkb", "G. trabeum PF13714 protein GLOTRDRAFT_42369"),
    ("S7Q148", "uniprotkb", "G. trabeum PF13714 protein GLOTRDRAFT_78731"),
]

# Active-site / specificity residues named in PMID:20558740, C. parasitica numbering.
MARKERS = [
    (111, "Tyr of the Tyr-His pair (Phe-Phe in PDP)"),
    (113, "H-bond to substrate C(1) carboxylate"),
    (114, "oxyanion hole main-chain amide"),
    (126, "second-shell metal water ligand"),
    (155, "direct Mn2+ ligand"),
    (157, "metal ligand, strained backbone"),
    (182, "His of the Tyr-His pair"),
    (184, "metal water ligand"),
    (190, "invariant gating-loop Lys"),
    (191, "gating-loop Arg, binds partner C-terminus"),
    (192, "catalytic Cys, proton donor to C(3)"),
    (221, "Arg binding C(2)/C(4) carboxylates"),
    (259, "shared-proton Glu"),
    (282, "Asn anchoring Glu-259"),
    (308, "OAH specificity Ser (Pro in DMML and MICL)"),
]

PS00161 = re.compile(r"K[KR]CGH[LMQR]")


def fetch(acc, db):
    if db == "pdb":
        url = f"https://www.rcsb.org/fasta/entry/{acc}"
    else:
        url = f"https://rest.uniprot.org/{db}/{acc}.fasta"
    text = urllib.request.urlopen(url, timeout=120).read().decode()
    record = text.split(">")[1]
    return "".join(record.splitlines()[1:]).strip()


def make_aligner():
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -11
    aligner.extend_gap_score = -1
    aligner.mode = "global"
    aligner.target_end_gap_score = 0.0
    aligner.query_end_gap_score = 0.0
    return aligner


def align(aligner, ref, qry):
    return aligner.align(ref, qry)[0]


def identity(alignment):
    ref, qry = alignment[0], alignment[1]
    aligned = sum(1 for a, b in zip(ref, qry) if a != "-" and b != "-")
    same = sum(1 for a, b in zip(ref, qry) if a == b and a != "-")
    return 100.0 * same / aligned if aligned else 0.0


def column_map(alignment):
    """Map reference (target) residue number -> aligned query residue string."""
    ref, qry = alignment[0], alignment[1]
    mapping = {}
    pos = 0
    for a, b in zip(ref, qry):
        if a != "-":
            pos += 1
            mapping[pos] = b
    return mapping


def main():
    aligner = make_aligner()
    seqs = {acc: fetch(acc, "uniprotkb") for acc in QUERIES}
    for acc, db, _ in REFERENCES:
        seqs[acc] = fetch(acc, db)

    ref_oah = seqs["D5LIR7"]
    print("# sequence lengths and PROSITE PS00161 pattern")
    print("accession\tlength\tPS00161_match")
    for acc in QUERIES + [a for a, _, _ in REFERENCES]:
        m = PS00161.search(seqs[acc])
        print(f"{acc}\t{len(seqs[acc])}\t{m.group(0) + '@' + str(m.start() + 1) if m else 'none'}")

    print()
    print("# percent identity of each query to each reference (global, BLOSUM62)")
    print("query\t" + "\t".join(a for a, _, _ in REFERENCES))
    for q in QUERIES:
        row = [f"{identity(align(aligner, seqs[r], seqs[q])):.1f}" for r, _, _ in REFERENCES]
        print(q + "\t" + "\t".join(row))

    print()
    print("# residues aligned to C. parasitica OAH active-site positions (D5LIR7 numbering)")
    header = ["position", "D5LIR7", "role"] + QUERIES + [a for a, _, _ in REFERENCES if a != "D5LIR7"]
    print("\t".join(header))
    maps = {}
    for acc in QUERIES + [a for a, _, _ in REFERENCES if a != "D5LIR7"]:
        maps[acc] = column_map(align(aligner, ref_oah, seqs[acc]))
    for pos, role in MARKERS:
        row = [f"{ref_oah[pos - 1]}{pos}", ref_oah[pos - 1], role]
        row += [maps[acc].get(pos, "?") for acc in header[3:]]
        print("\t".join(row))

    print()
    print("# aligned windows (reference position +/- 4) guarding against local misalignment")
    print("\t".join(["position", "D5LIR7_window"] + header[3:]))
    for pos, _ in MARKERS:
        lo, hi = max(1, pos - 4), min(len(ref_oah), pos + 4)
        row = [f"{ref_oah[pos - 1]}{pos}", ref_oah[lo - 1:hi]]
        for acc in header[3:]:
            row.append("".join(maps[acc].get(p, "?") for p in range(lo, hi + 1)))
        print("\t".join(row))

    print()
    print("# reference descriptions")
    for acc, _, desc in REFERENCES:
        print(f"{acc}\t{desc}")


if __name__ == "__main__":
    main()
