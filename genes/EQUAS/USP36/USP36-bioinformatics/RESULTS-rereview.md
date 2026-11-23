# USP36 (donkey) re-review: is A0A9L0JCH5 the canonical product?

Date: 2026-10-21. This supplements `RESULTS.md` (donkey vs human alignment), which is left unchanged.

## Reproduce

```
cd genes/EQUAS/USP36/USP36-bioinformatics
uv run --script compare_gene_models_rereview.py ../USP36-uniprot.txt A0A9L0I9H9 A0A8C4LEG8 A0A9L0K514 F6W2H6 A0A3Q2LIP2 Q9P275 B1AQJ2 A0A3Q1M0E6
curl -s "https://rest.ensembl.org/lookup/id/ENSEASG00005005026?expand=1;content-type=application/json"   # summarised in ensembl_transcripts_rereview.txt
```

Raw outputs: `compare_gene_models_rereview_output.txt`, `ensembl_transcripts_rereview.txt`.

## Results

- All four long donkey USP36 TrEMBL entries (A0A9L0JCH5 1156 aa, A0A9L0I9H9 1123 aa,
  A0A8C4LEG8 1124 aa, A0A9L0K514 1064 aa) are products of one Ensembl gene, ENSEASG00005005026 (USP36).
- A0A9L0JCH5 (ENSEAST00005074877) is the transcript Ensembl flags as canonical for the gene.
- A0A9L0I9H9 (1123 aa) and A0A8C4LEG8 (1124 aa) are 100% identical to A0A9L0JCH5 over every aligned
  residue; they differ only by lacking the 33-residue segment at donkey 253-285
  (AGERRGASWFQGLETRAGALGPGSLPAPLPSVA). The 1156-aa and 1123-aa transcripts both have 20 exons, so the
  segment is an extension of an existing exon (alternative splice-site use), not an extra exon.
- That segment has no counterpart in horse (F6W2H6, A0A3Q2LIP2; same horse gene ENSECAG00000016116),
  human Q9P275, mouse B1AQJ2 or cattle A0A3Q1M0E6: its best local match in each is 7-13 identical
  residues out of 33, in unrelated positions (around residue 490-980), i.e. background.

## Interpretation

A0A9L0JCH5 is the Ensembl-canonical but atypical splice form of donkey USP36. The 1123-aa donkey product
A0A9L0I9H9 has the same length and domain layout as human USP36 and is the more conventional ortholog
product. The 33-residue Gly/Pro/Ala-rich segment inserted between the Cys-box and His-box of the USP
domain is unique to this donkey transcript among the orthologs tested; whether it is a real
donkey-specific splice form or an annotation artefact cannot be decided from sequence. It does not
remove any catalytic residue (Cys131 and His415 are conserved, see `RESULTS.md`). No donkey USP36 entry is
UniProt-reviewed.
