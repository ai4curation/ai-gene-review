# DNMT3A (horse A0A9L0TK01): gene-model re-review, 2026-10-20

Independent of the ProtNLM2 predictions. Two new scripts, both fetching live data
(no hardcoded results):

- `compare_isoforms_rereview.py` aligns all seven horse DNMT3A UniProt models to human
  Q9Y6K1 (output: `RESULTS-rereview-alignment.txt`).
- `compare_exons_rereview.py` compares Ensembl exon structures of the benchmark
  transcript, a sibling horse transcript and the human canonical transcript
  (output: `RESULTS-rereview-exons.txt`).

## Findings

1. A0A9L0TK01 (873 aa) aligns end-to-end to human Q9Y6K1 (912 aa) at 97.3% identity.
   The only human residues without a counterpart are 1-3 (start difference) and 339-374.
2. Human 339-374 corresponds exactly to one 108-nt in-frame exon. The benchmark transcript ENSECAT00000098563 has 22 exons; it lacks exon 9 (71716828-71716935, 108 nt) of the sibling horse transcript ENSECAT00000027101, and the human canonical transcript ENST00000321117 carries a 108-nt exon at the same position (exon 9).
3. So A0A9L0TK01 is an exon-9-skipping alternative splice model of horse DNMT3A, not a fragment. Whether this splice form is expressed in horse tissues has not been tested.
4. The skipped segment falls inside the PWWP chromatin-reader region (UniProt PWWP domain 292-350 in human; 47/59 of those residues aligned). The aromatic-cage residue W330 and D333 are retained (horse W327, D330). The rest of the domain downstream is lost, so the PWWP fold is expected to be disrupted. This is a structural inference that has not been tested experimentally.
5. The ADD domain (133/133) and the C-terminal MTase domain (279/279) are complete. The catalytic PC-motif cysteine (human C710 -> horse C671), ENV-motif E756 -> E717, the CpG-recognition TRD R836 -> R797 and the tetramer-interface R882 -> R843 are all conserved.
6. None of the seven horse DNMT3A UniProt models is a complete canonical product. A0A3Q2IAR2, F6Q5D1 and A0A9L0TMC0 have altered C-termini (human R882 region absent or diverged). A0A9L0RGD3 lacks human 164-212, A0A9L0T4V1 lacks 286-338 (most of the PWWP), and A0A3Q2HNA6 lacks 2-59 (N-terminus). A0A9L0TK01 is the only model with the complete canonical C-terminal catalytic domain and the complete ADD.

## Interpretation

DNA cytosine-5 methyltransferase activity, CpG recognition, ADD-mediated H3K4me0
reading and tetramerisation should all be retained in this product. PWWP-dependent
properties are not expected to transfer to it: H3K36me2/3 reading and targeting to
pericentric heterochromatin and major-satellite methylation, which were lost on PWWP
disruption in mouse Dnmt3a (PMID:15456878).
