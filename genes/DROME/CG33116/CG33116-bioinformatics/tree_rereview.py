"""Re-review phylogeny for CG33116 (Q9VIU4) within PTHR10414.

Fetches sequences from UniProt, aligns with MAFFT, builds a neighbour-joining
tree (BLOSUM62 identity distance) with 100 bootstrap replicates, and reports
pairwise identities to Q9VIU4 plus the PANTHER subfamily of each sequence.
Usage: uv run --with biopython --with requests python tree_rereview.py
"""
import subprocess
import random
import requests
from io import StringIO
from Bio import AlignIO, Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
from Bio.Phylo.Consensus import majority_consensus
from Bio.Align import MultipleSeqAlignment

ACCS = {
    "Q9VIU4": "Dmel_CG33116",
    "O44732": "Cele_ept-1",
    "A0A9D4BI59": "Dpoly_mollusc",
    "A0A913YBA7": "Ediaph_cnidarian",
    "Q9C0D9": "Hsap_SELENOI",
    "A0A8M1PAB3": "Drer_selenoi",
    "Q9Y6K0": "Hsap_CEPT1",
    "Q8WUD6": "Hsap_CHPT1",
    "A1Z9E0": "Dmel_bbc_CG6016",
    "Q8T0S3": "Dmel_cpt_CG7149",
    "P22140": "Scer_EPT1",
    "P17898": "Scer_CPT1",
    "O82567": "Atha_AAPT1",
}

def fetch(acc):
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}?format=json&fields=sequence,xref_panther")
    r.raise_for_status()
    j = r.json()
    sfs = [x["id"] for x in j.get("uniProtKBCrossReferences", []) if x["database"] == "PANTHER" and ":SF" in x["id"]]
    return j["sequence"]["value"], ";".join(sfs)

def main():
    fasta, sf = [], {}
    for acc, name in ACCS.items():
        seq, s = fetch(acc)
        sf[name] = s
        # selenocysteine (U, SELENOI C-terminus) recoded as C for MAFFT
        fasta.append(f">{name}\n{seq.replace('U', 'C')}\n")
    open("rereview_seqs.fasta", "w").write("".join(fasta))
    aln_txt = subprocess.run(["mafft", "--auto", "--quiet", "rereview_seqs.fasta"], capture_output=True, text=True, check=True).stdout
    open("rereview_aln.fasta", "w").write(aln_txt)
    aln = AlignIO.read(StringIO(aln_txt), "fasta")
    calc = DistanceCalculator("identity")
    dm = calc.get_distance(aln)
    print("PANTHER subfamily and % identity (alignment-based) to Dmel_CG33116:")
    names = [r.id for r in aln]
    for n in names:
        print(f"  {n:20s} {sf[n]:20s} {100*(1-dm[n,'Dmel_CG33116']):.1f}")
    cons = DistanceTreeConstructor(calc, "nj")
    tree = cons.build_tree(aln)
    tree.root_with_outgroup("Atha_AAPT1")
    print("\nNJ tree (rooted on Arabidopsis AAPT1):")
    Phylo.draw_ascii(tree)
    random.seed(1)
    L = aln.get_alignment_length()
    reps = []
    for _ in range(100):
        cols = [random.randrange(L) for _ in range(L)]
        recs = []
        for r in aln:
            rr = r[:0]
            s = "".join(str(r.seq)[c] for c in cols)
            from Bio.SeqRecord import SeqRecord
            from Bio.Seq import Seq
            recs.append(SeqRecord(Seq(s), id=r.id))
        reps.append(cons.build_tree(MultipleSeqAlignment(recs)))
    ct = majority_consensus(reps, 0.5)
    ct.root_with_outgroup("Atha_AAPT1")
    print("\nMajority-rule bootstrap consensus (100 replicates; clade confidences = % support):")
    Phylo.draw_ascii(ct)
    Phylo.write(ct, "rereview_consensus.nwk", "newick")

if __name__ == "__main__":
    main()
