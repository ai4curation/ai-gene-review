# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83", "requests"]
# ///
"""Place NCU09721 (Q7S2Q5) among AP-1/AP-2/AP-3 beta-adaptins.

Fetches sequences from UniProt REST, aligns with MAFFT (must be on PATH),
computes pairwise identity over gap-free aligned columns, builds a
neighbour-joining tree (BLOSUM62 distance) with 100 bootstrap replicates,
and scans the target for short clathrin-box-like motifs. Results are printed
and written to beta_adaptin_phylogeny_rereview.out.txt / .nwk.
"""
import io
import random
import re
import subprocess
from pathlib import Path

import requests
from Bio import AlignIO, Phylo, SeqIO
from Bio.Align import MultipleSeqAlignment
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor

HERE = Path(__file__).parent
SEQS = {
    "Q7S2Q5": "NEUCR_NCU09721_target",
    "Q7S8H6": "NEUCR_NCU05232",
    "Q7S9G9": "NEUCR_NCU06569_AP3b",
    "P36000": "YEAST_APL2_AP1b",
    "P27351": "YEAST_APL1_AP2b",
    "O43079": "SCHPO_apl2_AP1b",
    "O43005": "SCHPO_apl1_AP2b",
    "Q5B8V1": "EMENI_AN3029",
    "C8V3G8": "EMENI_AN5950",
    "V6R9X9": "GIBZE_17533",
    "V6RKE4": "GIBZE_20021",
    "V6RQ48": "GIBZE_26405",
    "Q10567": "HUMAN_AP1B1",
    "P63010": "HUMAN_AP2B1",
    "Q54X82": "DICDI_ap1b1",
    "O00203": "HUMAN_AP3B1_outgroup",
}


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return str(next(SeqIO.parse(io.StringIO(r.text), "fasta")).seq)


def main() -> None:
    out = []
    seqs = {SEQS[a]: fetch(a) for a in SEQS}
    fasta = HERE / "beta_adaptins_rereview.fasta"
    fasta.write_text("".join(f">{k}\n{v}\n" for k, v in seqs.items()))
    aln_txt = subprocess.run(
        ["mafft", "--auto", "--quiet", str(fasta)], capture_output=True, text=True, check=True
    ).stdout
    (HERE / "beta_adaptins_rereview.aln.fasta").write_text(aln_txt)
    aln = AlignIO.read(io.StringIO(aln_txt), "fasta")
    for k, v in seqs.items():
        out.append(f"length {k}: {len(v)}")
    tgt = next(r for r in aln if r.id.endswith("target"))
    out.append("\nPercent identity of target vs others (gap-free columns):")
    rows = []
    for r in aln:
        if r is tgt:
            continue
        pairs = [(a, b) for a, b in zip(str(tgt.seq), str(r.seq)) if a != "-" and b != "-"]
        ident = 100 * sum(a == b for a, b in pairs) / len(pairs)
        rows.append((ident, r.id, len(pairs)))
    for ident, rid, n in sorted(rows, reverse=True):
        out.append(f"  {rid:28s} {ident:5.1f}%  over {n} cols")
    # NJ tree with bootstrap
    calc = DistanceCalculator("blosum62")
    cons = DistanceTreeConstructor(calc, "nj")
    tree = cons.build_tree(aln)
    tree.root_with_outgroup("HUMAN_AP3B1_outgroup")
    random.seed(1)
    ncol = aln.get_alignment_length()
    ref_clades = {
        frozenset(t.name for t in c.get_terminals())
        for c in tree.get_nonterminals()
    }
    support = {c: 0 for c in ref_clades}
    n_boot = 100
    names = [r.id for r in aln]
    for _ in range(n_boot):
        cols = [random.randrange(ncol) for _ in range(ncol)]
        recs = []
        for r in aln:
            s = "".join(r.seq[i] for i in cols)
            rec = r[:0]
            rec = type(r)(type(r.seq)(s), id=r.id, description="")
            recs.append(rec)
        bt = cons.build_tree(MultipleSeqAlignment(recs))
        bt.root_with_outgroup("HUMAN_AP3B1_outgroup")
        bclades = {frozenset(t.name for t in c.get_terminals()) for c in bt.get_nonterminals()}
        for c in ref_clades:
            if c in bclades:
                support[c] += 1
    for c in tree.get_nonterminals():
        key = frozenset(t.name for t in c.get_terminals())
        c.confidence = support.get(key, 0)
    Phylo.write(tree, str(HERE / "beta_adaptins_rereview.nwk"), "newick")
    buf = io.StringIO()
    Phylo.draw_ascii(tree, file=buf)
    out.append("\nNJ tree (rooted on human AP3B1; bootstrap /100 in .nwk):")
    out.append(buf.getvalue())
    out.append("Clades containing the target (smallest first) with bootstrap support:")
    tgt_clades = sorted(
        (c for c in support if tgt.id in c), key=len
    )
    for c in tgt_clades[:4]:
        out.append(f"  {support[c]:3d}/100  {sorted(c)}")
    # motif scan
    s = seqs[tgt.id]
    out.append("\nShort motif scan in target (1-based):")
    for pat in ["LL[DNE][LIVMFG][DEF]", "LLNGF", "LLDID", "L[LI][DE][LI][DE]", "LLGLF"]:
        hits = [(m.start() + 1, m.group()) for m in re.finditer(pat, s)]
        out.append(f"  {pat}: {hits}")
    out.append(f"  C-terminal 30 aa: {s[-30:]}")
    text = "\n".join(out)
    print(text)
    (HERE / "beta_adaptin_phylogeny_rereview.out.txt").write_text(text + "\n")


if __name__ == "__main__":
    main()
