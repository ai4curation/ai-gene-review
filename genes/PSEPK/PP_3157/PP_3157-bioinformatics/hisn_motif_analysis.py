#!/usr/bin/env python
"""Classify PP_3157 (Q88I44) within the IMPase superfamily.

Reproducible analysis, run from the repository root:

    python genes/PSEPK/PP_3157/PP_3157-bioinformatics/hisn_motif_analysis.py \
        --cache-dir <dir for downloads>

Steps (all inputs downloaded at run time; nothing is hard-coded except identifiers):
1. NCBIfam HMMs TIGR02067 (his_9_HisN, histidinol-phosphatase) and TIGR01331 (bisphos_cysQ)
   are searched (pyhmmer hmmsearch) against the complete UniProt proteomes of P. putida
   KT2440 (UP000000556) and P. aeruginosa PAO1 (UP000002438). Hits are compared with each
   model's trusted cutoff (TC line in the HMM file).
2. The HisN-discriminating residues defined by Kulis-Horn et al. 2017 (PMID:28720084) are read
   off local alignments (BLOSUM62) of each query to C. glutamicum HisN (Q8NS80), whose own
   residue numbering the paper uses. A control row checks that Q8NS80 itself carries the
   residues the paper names, so the numbering assumption is tested, not assumed.
Requires biopython and pyhmmer. Writes RESULTS.md and results/*.tsv next to this script.
"""
import argparse
import io
import urllib.request
from pathlib import Path

import pyhmmer
from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

HERE = Path(__file__).resolve().parent
HMM_URL = "https://ftp.ncbi.nlm.nih.gov/hmm/current/hmm_PGAP.HMM/{}.HMM"
PROTEOME_URL = "https://rest.uniprot.org/uniprotkb/stream?query=proteome:{}&format=fasta"
SEQ_URL = "https://rest.uniprot.org/uniprotkb/{}.fasta"
HMMS = ["TIGR02067.1", "TIGR01331.1"]
PROTEOMES = {"KT2440": "UP000000556", "PAO1": "UP000002438"}
REFERENCE = "Q8NS80"  # C. glutamicum HisN
QUERIES = {
    "Q8NS80": "C. glutamicum HisN (control, experimentally validated HolPase)",
    "Q6NPM8": "A. thaliana HISN7 (experimentally validated IMPase-like HolPase)",
    "Q88I44": "P. putida PP_3157 (query)",
    "Q88R73": "P. putida CysQ PP_0261",
    "Q88PL2": "P. putida SuhB PP_0838",
    "P22255": "E. coli CysQ",
    "P0ADG4": "E. coli SuhB",
}
# Positions (HisN_Cg numbering) and the expectation stated in PMID:28720084 for HisN orthologs.
MOTIF_POSITIONS = {
    36: ("motif 1", "K"), 38: ("motif 1", "D"), 41: ("motif 1", "P"), 42: ("motif 1", "V"),
    68: ("motif 2", "G (S in CysQ)"), 69: ("motif 2", "E"), 70: ("motif 2", "E"),
    85: ("motif 3", "D"), 87: ("motif 3", "I"), 88: ("motif 3", "D"), 90: ("motif 3", "T"),
    91: ("motif 3", "K preferred"),
    96: ("motif 4", "G"), 98: ("motif 4", "P"), 100: ("motif 4", "aromatic"),
    102: ("motif 4", "T"), 103: ("motif 4", "L"),
    187: ("motif 5", "R (V/L in some alphaproteobacteria)"), 188: ("motif 5", "aromatic or small"),
    189: ("motif 5", "aromatic or small"), 190: ("motif 5", "G"),
    191: ("motif 5", "D (E in some Gammaproteobacteria)"), 193: ("motif 5", "aromatic"),
    195: ("motif 5", "aromatic or H"),
    215: ("motif 6", "D"), 219: ("motif 6", "not G (G in Cg0911/SuhB/ImpA, P in CysQ)"),
}
# Residues the paper names explicitly for HisN_Cg / HisN orthologs, used as the numbering control.
CONTROL = {36: "K", 38: "D", 41: "P", 42: "V", 68: "G", 69: "E", 70: "E", 85: "D", 87: "I",
           88: "D", 90: "T", 96: "G", 98: "P", 102: "T", 103: "L", 187: "R", 190: "G",
           191: "D", 215: "D"}


def fetch(url, path):
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        with urllib.request.urlopen(url) as r:
            path.write_bytes(r.read())
    return path


def hmm_search(cache):
    rows = []
    alphabet = pyhmmer.easel.Alphabet.amino()
    for name, up in PROTEOMES.items():
        fa = fetch(PROTEOME_URL.format(up), cache / f"{up}.fasta")
        with pyhmmer.easel.SequenceFile(str(fa), digital=True, alphabet=alphabet) as sf:
            seqs = sf.read_block()
        for acc in HMMS:
            hp = fetch(HMM_URL.format(acc), cache / f"{acc}.HMM")
            with pyhmmer.plan7.HMMFile(str(hp)) as hf:
                hmm = hf.read()
            tc = hmm.cutoffs.trusted[0]
            for hits in pyhmmer.hmmsearch([hmm], seqs, E=1e-5):
                for h in hits:
                    nm = h.name.decode() if isinstance(h.name, bytes) else h.name
                    rows.append((name, acc, hmm.name.decode() if isinstance(hmm.name, bytes) else hmm.name,
                                 nm, f"{h.score:.1f}", f"{tc:.2f}", "yes" if h.score >= tc else "no"))
    return rows


def motif_table(cache):
    seqs = {}
    for acc in QUERIES:
        p = fetch(SEQ_URL.format(acc), cache / f"{acc}.fasta")
        seqs[acc] = str(next(SeqIO.parse(str(p), "fasta")).seq)
    al = PairwiseAligner(mode="local")
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score, al.extend_gap_score = -10, -0.5
    ref = seqs[REFERENCE]
    out = {}
    for acc, s in seqs.items():
        aln = al.align(ref, s)[0]
        mapping, ident, cols = {}, 0, 0
        for (rs, re_), (qs, qe) in zip(*aln.aligned):
            for i, j in zip(range(rs, re_), range(qs, qe)):
                mapping[i + 1] = (s[j], j + 1)
                cols += 1
                ident += ref[i] == s[j]
        out[acc] = (mapping, ident / cols if cols else 0.0, aln.score)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache-dir", type=Path, required=True)
    args = ap.parse_args()
    (HERE / "results").mkdir(exist_ok=True)
    hits = hmm_search(args.cache_dir)
    with open(HERE / "results" / "hmm_hits.tsv", "w") as f:
        f.write("proteome\thmm\thmm_name\ttarget\tbitscore\ttrusted_cutoff\tabove_tc\n")
        for r in hits:
            f.write("\t".join(r) + "\n")
    mt = motif_table(args.cache_dir)
    with open(HERE / "results" / "motif_residues.tsv", "w") as f:
        f.write("position_HisNCg\tmotif\texpected_in_HisN\t" + "\t".join(QUERIES) + "\n")
        for pos, (motif, exp) in MOTIF_POSITIONS.items():
            cells = []
            for acc in QUERIES:
                r = mt[acc][0].get(pos)
                cells.append(f"{r[0]}{r[1]}" if r else "-")
            f.write(f"{pos}\t{motif}\t{exp}\t" + "\t".join(cells) + "\n")
    ctrl = mt[REFERENCE][0]
    ctrl_ok = [p for p, aa in CONTROL.items() if ctrl.get(p, ("?",))[0] == aa]
    lines = ["# PP_3157 (Q88I44) HisN classification - generated by hisn_motif_analysis.py", "",
             "Generated output; do not edit by hand. Re-run the script to regenerate.", "",
             "## Numbering control", "",
             f"C. glutamicum HisN (Q8NS80) carries the paper-named residue at {len(ctrl_ok)} of "
             f"{len(CONTROL)} control positions in its own numbering.", "",
             "## HMM searches against complete proteomes", "",
             "| proteome | HMM | target | bitscore | trusted cutoff | above TC |", "|---|---|---|---|---|---|"]
    for r in hits:
        lines.append(f"| {r[0]} | {r[1]} {r[2]} | {r[3]} | {r[4]} | {r[5]} | {r[6]} |")
    lines += ["", "## Pairwise local alignment to C. glutamicum HisN (Q8NS80)", "",
              "| accession | description | identity over aligned columns | score |", "|---|---|---|---|"]
    for acc, d in QUERIES.items():
        lines.append(f"| {acc} | {d} | {mt[acc][1]:.3f} | {mt[acc][2]:.0f} |")
    lines += ["", "## HisN-discriminating positions (HisN_Cg numbering; residue+own position)", "",
              "| pos | motif | expected in HisN | " + " | ".join(QUERIES) + " |",
              "|---" * (3 + len(QUERIES)) + "|"]
    for pos, (motif, exp) in MOTIF_POSITIONS.items():
        cells = []
        for acc in QUERIES:
            r = mt[acc][0].get(pos)
            cells.append(f"{r[0]}{r[1]}" if r else "-")
        lines.append(f"| {pos} | {motif} | {exp} | " + " | ".join(cells) + " |")
    q = mt["Q88I44"][0]
    def res(p):
        r = q.get(p)
        return r[0] if r else "-"
    lines += ["", "## Key PP_3157 calls (computed)", "",
              f"- PP_3157 motif 5 position 191: {res(191)}; position 190: {res(190)}; position 187: {res(187)}.",
              f"- PP_3157 motif 6 position 219: {res(219)} (HisN orthologs: not G; CysQ: P).",
              f"- PP_3157 motif 2 position 68: {res(68)} (HisN: G; CysQ: S)."]
    for prot in PROTEOMES:
        above = [r for r in hits if r[0] == prot and r[6] == "yes"]
        for acc in HMMS:
            names = [r[3] for r in above if r[1] == acc]
            lines.append(f"- {prot}: proteins above the {acc} trusted cutoff: {', '.join(names) or 'none'}.")
    (HERE / "RESULTS.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
