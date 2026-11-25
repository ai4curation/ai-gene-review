"""Map the UniProt-annotated ligand-binding residues of reviewed KT2440 MoaA
(Q88E69) onto the MoaA-family paralogs Q88K11 (PP_2482) and Q88LG4 (PP_1969)
and onto reviewed E. coli MoaA (P30745), and test the PROSITE PS01305 pattern.

Usage (from repo root):
  uv run --with biopython python genes/PSEPK/PP_1969/PP_1969-bioinformatics/map_moaA_sites.py \
    genes/PSEPK/moaA/moaA-uniprot.txt genes/PSEPK/PP_2482/PP_2482-uniprot.txt \
    genes/PSEPK/PP_1969/PP_1969-uniprot.txt \
    genes/PSEPK/PP_1969/PP_1969-bioinformatics/P30745_Ecoli_MoaA.fasta

Binding-site positions are parsed from the FT BINDING lines of the first
(reference) UniProt file; nothing is hardcoded except the PS01305 pattern,
copied from https://prosite.expasy.org/PS01305.txt
(PA   [LIV]-x(3)-C-[NDP]-[LIVMF]-[DNQRS]-C-x-[FYM]-C.).
"""
import re
import sys
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices

PS01305 = r"[LIV]...C[NDP][LIVMF][DNQRS]C.[FYM]C"


def read_uniprot(path):
    seq, on, sites, cur = [], False, [], None
    lines = Path(path).read_text().splitlines()
    acc = lines[1].split()[1].rstrip(";")
    for line in lines:
        if line.startswith("FT   BINDING"):
            span = line.split()[2]
            a, _, b = span.partition("..")
            cur = (int(a), int(b or a))
        elif cur and line.startswith("FT") and "/ligand=" in line:
            lig = line.split("/ligand=")[1].strip('"')
            for p in range(cur[0], cur[1] + 1):
                sites.append((p, lig))
            cur = None
        if line.startswith("SQ"):
            on = True
            continue
        if line.startswith("//"):
            break
        if on:
            seq.append(line.replace(" ", "").strip())
    return acc, "".join(seq), sites


def read_fasta(path):
    lines = Path(path).read_text().splitlines()
    return lines[0].split("|")[1], "".join(l.strip() for l in lines[1:])


def aligner():
    al = Align.PairwiseAligner()
    al.mode = "global"
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score = -10
    al.extend_gap_score = -0.5
    return al


def mapping(al, a, b):
    aln = al.align(a, b)[0]
    m, same, n = {}, 0, 0
    for (s1, e1), (s2, e2) in zip(*aln.aligned):
        for i, j in zip(range(s1, e1), range(s2, e2)):
            m[i + 1] = j + 1
            n += 1
            same += a[i] == b[j]
    return m, 100 * same / n


def main(ref_path, *others):
    ref_acc, ref_seq, sites = read_uniprot(ref_path)
    seqs = {ref_acc: ref_seq}
    for p in others:
        acc, s = read_fasta(p) if p.endswith((".fasta", ".fa")) else read_uniprot(p)[:2]
        seqs[acc] = s
    al = aligner()
    names = list(seqs)
    print("## Pairwise identity (global BLOSUM62, gap -10/-0.5; identical / aligned pairs)")
    print("seq_a\tseq_b\tpercent_identity")
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            print(f"{names[i]}\t{names[j]}\t{mapping(al, seqs[names[i]], seqs[names[j]])[1]:.2f}")
    print(f"\n## {ref_acc} UniProt binding residues mapped by pairwise alignment")
    print("ref_pos\tligand\t" + "\t".join(names))
    maps = {n: mapping(al, ref_seq, seqs[n])[0] for n in names[1:]}
    conserved = {n: 0 for n in names[1:]}
    for pos, lig in sites:
        row = [str(pos), lig, f"{ref_seq[pos - 1]}{pos}"]
        for n in names[1:]:
            q = maps[n].get(pos)
            row.append(f"{seqs[n][q - 1]}{q}" if q else "-")
            conserved[n] += bool(q) and seqs[n][q - 1] == ref_seq[pos - 1]
        print("\t".join(row))
    print("\n## Identical at annotated binding positions")
    for n in names[1:]:
        print(f"{n}\t{conserved[n]}/{len(sites)}")
    print("\n## PROSITE PS01305 (MOAA_NIFB_PQQE) pattern matches; radical-SAM CxxxCxxC context")
    for n, s in seqs.items():
        hits = [(m.start() + 1, m.group()) for m in re.finditer(PS01305, s)]
        r = re.search(r"C...C..C", s)
        ctx = s[r.start() - 6 : r.end()] if r else "-"
        print(f"{n}\tPS01305={hits or 'no match'}\tCxxxCxxC_context={ctx}")


if __name__ == "__main__":
    main(*sys.argv[1:])
