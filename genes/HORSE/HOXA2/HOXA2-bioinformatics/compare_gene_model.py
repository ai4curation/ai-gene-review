# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.81", "requests"]
# ///
"""Compare the horse Ensembl HOXA2 model (F7DP63) with the horse RefSeq model
(XP_001499478.2), donkey A0A9L0JBM7, human O43364 and mouse P31245.

Fetches sequences live from UniProt REST and NCBI efetch, then reports global
alignment identity, the N-terminal divergent region of F7DP63, and conservation
of the YPWM hexapeptide and the homeodomain (human 143-202).
"""
import requests
from Bio import Align
from Bio.Align import substitution_matrices

UNIPROT = {"F7DP63": "horse_ensembl", "A0A9L0JBM7": "donkey", "O43364": "human", "P31245": "mouse"}


def uniprot_seq(acc: str) -> str:
    txt = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60).text
    return "".join(txt.splitlines()[1:])


def ncbi_seq(acc: str) -> str:
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    txt = requests.get(url, params={"db": "protein", "id": acc, "rettype": "fasta"}, timeout=60).text
    return "".join(l for l in txt.splitlines()[1:] if l.strip())


def aligner() -> Align.PairwiseAligner:
    a = Align.PairwiseAligner()
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    a.mode = "global"
    return a


def identity(aln) -> tuple[int, int]:
    s1, s2 = aln[0], aln[1]
    cols = [(x, y) for x, y in zip(s1, s2) if x != "-" and y != "-"]
    return sum(x == y for x, y in cols), len(cols)


def main() -> None:
    seqs = {name: uniprot_seq(acc) for acc, name in UNIPROT.items()}
    seqs["horse_refseq_XP_001499478.2"] = ncbi_seq("XP_001499478.2")
    for k, v in seqs.items():
        print(f"{k}\tlength={len(v)}")
    al = aligner()
    target = seqs["horse_ensembl"]
    for k, v in seqs.items():
        if k == "horse_ensembl":
            continue
        aln = al.align(target, v)[0]
        ident, cols = identity(aln)
        print(f"F7DP63 vs {k}: {ident}/{cols} identical aligned columns")
    human = seqs["human"]
    # longest common suffix-anchored shared region: find first position where human tail matches F7DP63
    anchor = "TIPSLNPGSHPRHG"
    hi, ti = human.find(anchor), target.find(anchor)
    print(f"anchor {anchor}: human position {hi + 1}, F7DP63 position {ti + 1}")
    print(f"F7DP63 N-terminal segment 1-{ti} (not in human/mouse/RefSeq horse): {target[:ti]}")
    print(f"human N-terminal segment 1-{hi} absent from F7DP63: {human[:hi]}")
    print(f"F7DP63 N-terminal segment found in human HOXA2: {target[:ti] in human}")
    for motif in ["YPWM"]:
        print(f"{motif}: human pos {human.find(motif) + 1}, F7DP63 pos {target.find(motif) + 1}")
    hd = human[142:202]
    pos = target.find(hd)
    print(f"human homeodomain 143-202 found verbatim in F7DP63: {pos >= 0} (F7DP63 start {pos + 1})")
    tail_ref = seqs["horse_refseq_XP_001499478.2"][hi:]
    tail_ens = target[ti:]
    ident = sum(a == b for a, b in zip(tail_ref, tail_ens))
    print(f"F7DP63 {ti + 1}-end vs RefSeq {hi + 1}-end: lengths {len(tail_ens)}/{len(tail_ref)}, identical positions {ident}")


if __name__ == "__main__":
    main()
