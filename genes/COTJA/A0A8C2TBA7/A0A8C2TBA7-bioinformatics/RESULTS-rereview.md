# A0A8C2TBA7 (quail PAM) vs human PAM P19021 — re-review analysis (2026-10-21)

Script: `compare_to_human_pam_rereview.py` (run with
`uv run --with biopython --with requests python compare_to_human_pam_rereview.py`).
Raw output: `RESULTS-rereview-output.txt`. Sequences fetched live from UniProt REST.

Method: global pairwise alignment (BLOSUM62, gap open -10, extend -0.5) of the quail
Ensembl model A0A8C2TBA7 (846 aa) with human PAM canonical isoform P19021-1 (973 aa);
human metal-binding positions taken from the human UniProt BINDING features and mapped
through the alignment. This alignment is used only to describe the domain content of the
quail model. Orthology is established by shared PANTHER subfamily PTHR10680:SF14, not by
this alignment.

## Results

- Identity is 0.750 over 841 aligned pairs; 86.4% of the human sequence is covered.
- None of the 107 residues of the human exon-16 linker (P19021 388-494, VSP_001227, which
  is the segment absent from isoform PAM-2) aligns to quail. The quail model therefore has
  the domain arrangement of PAM-2: PHM and PAL directly joined, with no
  endoprotease-sensitive linker between them.
- All 86 residues of human region 829-914 (VSP_001228) align, so the quail model keeps
  the juxtamembrane, transmembrane and cytosolic segments. It is a membrane form, not the
  soluble PAM-3/PAM-4 type.
- All six PHM copper ligands are conserved (human H102, H103, H167, H237, H239, M309 ->
  quail H103, H104, H168, H238, H240, M310).
- All three PAL zinc ligands are conserved (human H582, H687, H783 -> quail H453, H557,
  H654), as is the calcium-site D784 -> D655.

## Interpretation

A0A8C2TBA7 is a full-length bifunctional PAM gene model that lacks exon 16, which makes it
equivalent to the mammalian PAM-2 splice form. It is not a fragment. Both catalytic cores
and their metal ligands are intact, as are the signal peptide (SignalP 1-21) and the
transmembrane helix (Phobius 734-758). Four other quail PAM models exist in UniProt
(A0A8C2Y9Y4 970 aa, A0A8C2YA38 952 aa, A0A8C2TDQ8 915 aa, A0A8C2TGR3 869 aa). All are
unreviewed, so quail has no reviewed canonical PAM entry.
