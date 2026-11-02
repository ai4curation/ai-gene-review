# LITAFD LITAF-domain comparison with LITAF and CDIP1

Script: `litaf_domain_compare.py` (run with `uv run --script litaf_domain_compare.py`;
raw output in `results.txt`). Sequences and feature tables are fetched live from the
UniProt REST API; the script does a BLOSUM62 local alignment (gap open -10, extend -0.5)
of LITAFD (A0A1B0GVX0, 72 aa) to LITAF (Q99732, 161 aa) and CDIP1 (Q9H305, 208 aa),
maps each parent's annotated Zn(2+) ligands and membrane-binding region onto LITAFD,
and computes the best 19-residue Kyte-Doolittle window.

## Results

- LITAFD consists of the LITAF domain and nothing else. It aligns over 71 residues to
  LITAF residues 90-161 (33 identities, 46.5%) and to CDIP1 residues 136-207
  (26 identities, 36.6%). It has no counterpart of the proline-rich N-terminal regions
  of LITAF (residues 1-89) or CDIP1 (residues 1-135).
- Both CXXC zinc-knuckle motifs are present: C7-P-Y-C10 and C59-P-V-C62.
- All four annotated Zn(2+) ligands of LITAF (C96, C99, C148, C151) and of CDIP1
  (C142, C145, C194, C197) align to LITAFD C7, C10, C59 and C62.
- The LITAF membrane-binding amphipathic helix (residues 111-134,
  AGALTWLSCGSLCLLGCIAGCCFI) aligns without gaps to LITAFD 22-45
  (PGALTWLLCTTLFLFGYVLGCCFL), with the GALTWL motif identical.
- The best 19-aa Kyte-Doolittle window has a mean hydropathy of 2.17 in LITAFD (28-46),
  2.15 in the LITAF domain of LITAF (120-138) and 2.16 in that of CDIP1 (162-180).

## Interpretation

The zinc-binding site and the hydrophobic membrane-insertion region that the LITAF
domain requires for monotopic membrane integration (shown experimentally for LITAF and
CDIP1 in PMID:27582497) are fully conserved in LITAFD. Nothing in the sequence suggests
loss of zinc binding or of membrane association. LITAFD lacks every sequence outside
the domain, so properties that may depend on the LITAF N-terminus (PPxY/PSAP-type
motifs, proposed nuclear and transcription-regulatory roles) have no sequence basis
here. This analysis is sequence-only: it does not show that the protein is made, where
it localises, or what it does.

Supplementary observation (Ensembl REST homology endpoint, queried during the review,
not part of the script): Ensembl reports one-to-one orthologues in mouse
(ENSMUSG00000107252) and cow, and orthologues in many other mammals and teleost fish,
so LITAFD is a conserved vertebrate gene rather than a recent primate duplicate.
