"""Align dashboard query NZ_CAKNDZ010000038.1_57 to KT2440 PP_0788 (Q88PR0), locate the N-terminal
length difference, and translate the KT2440 genomic sequence upstream of the annotated PP_0788 start
(NC_002947.4, + strand, CDS 903742..905901 per Fitness Browser) in frame to see whether an upstream
in-frame start could give the query's longer N-terminus.
Usage: python fb identity_start.py QUERY_FASTA UNIPROT_TXT OUTDIR"""
import json, os, re, sys, urllib.request
from Bio import Align, SeqIO
from Bio.Align import substitution_matrices
from Bio.Seq import Seq

qfa, uptxt, out = sys.argv[1:4]
os.makedirs(out, exist_ok=True)
query = str(next(SeqIO.parse(qfa, "fasta")).seq)
txt = open(uptxt).read()
subj = re.sub(r"[^A-Z]", "", txt.split("\nSQ ")[1].split("\n", 1)[1].split("//")[0])

al = Align.PairwiseAligner(mode="global", open_gap_score=-10, extend_gap_score=-0.5,
                           substitution_matrix=substitution_matrices.load("BLOSUM62"))
al.end_gap_score = 0
a = al.align(query, subj)[0]
ident = sum(1 for (qs, qe), (ss, se) in zip(*a.aligned) for i in range(qe - qs) if query[qs + i] == subj[ss + i])
pairs = sum(qe - qs for (qs, qe), _ in zip(*a.aligned))
blocks = [[[int(v) for v in qb], [int(v) for v in sb]] for qb, sb in zip(*a.aligned)]
first_q, first_s = int(a.aligned[0][0][0]), int(a.aligned[1][0][0])
ident, pairs = int(ident), int(pairs)

# KT2440 genome region upstream of PP_0788
start, end = 903742, 905901
up = 300  # multiple of 3
url = ("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=NC_002947.4&rettype=fasta"
       f"&seq_start={start - up}&seq_stop={start + 200}")
dna = "".join(urllib.request.urlopen(url, timeout=60).read().decode().split("\n")[1:])
prot_frame = str(Seq(dna).translate())  # frame aligned so codon at index `up` is the annotated start
cds_start_aa = up // 3
upstream_aa = prot_frame[:cds_start_aa]
# last stop codon upstream of annotated start, in frame
last_stop = upstream_aa.rfind("*")
orf_ext = upstream_aa[last_stop + 1:]
res = {
    "query_len": len(query), "subject_len": len(subj), "aligned_pairs": pairs, "identical": ident,
    "pct_id_aligned": round(100 * ident / pairs, 1),
    "first_aligned_query_pos_1based": first_q + 1, "first_aligned_subject_pos_1based": first_s + 1,
    "query_Nterm_before_alignment": query[:first_q], "subject_Nterm_before_alignment": subj[:first_s],
    "aligned_blocks_0based": blocks,
    "kt2440_region": f"NC_002947.4:{start - up}-{start + 200}",
    "annotated_start_codon": dna[up:up + 3],
    "translation_from_annotated_start": prot_frame[cds_start_aa:cds_start_aa + 40],
    "inframe_upstream_translation": upstream_aa,
    "inframe_open_extension_after_last_upstream_stop": orf_ext,
    "upstream_inframe_ATG_GTG_TTG_positions_aa_before_start": [cds_start_aa - i for i in range(last_stop + 1, cds_start_aa)
                                                               if dna[3 * i:3 * i + 3] in ("ATG", "GTG", "TTG")],
}
json.dump(res, open(os.path.join(out, "identity_start.json"), "w"), indent=1)
print(a.format()[:1200])
print(json.dumps({k: v for k, v in res.items() if k != "aligned_blocks_0based"}, indent=1))
