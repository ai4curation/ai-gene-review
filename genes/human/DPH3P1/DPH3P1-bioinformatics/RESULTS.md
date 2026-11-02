# DPH3P1 (Q9H4G8) versus parent DPH3 (Q96FX2)

Scripts (run with `uv run`; inputs are fetched live, nothing is hardcoded):

- `compare_to_parent.py Q9H4G8 Q96FX2 ENSG00000233838` -> `results.txt`
- `gtex_expression.py ENSG00000233838 ENSG00000154813` -> `gtex.txt`

## Locus and transcript

- Ensembl ENSG00000233838 is annotated as biotype processed_pseudogene (20q13.33, one
  exon, 249 nt). Its only transcript, ENST00000486648, is a processed_pseudogene
  transcript with no translation.
- HGNC (REST, fetched 2026-10-04): locus_type `pseudogene`, name "diphthamide
  biosynthesis 3 pseudogene 1", no MANE transcript.
- GTEx v8: GTEx returned no median-expression rows for this gene (ENSG00000233838.5).
  For comparison, parent DPH3 is expressed in all 54 tissues (max median about 28 TPM).
- UniProt: PE 5 (Uncertain), with the CAUTION "Could be the product of a pseudogene".
  The EMBL cross-reference is genomic DNA only, flagged NOT_ANNOTATED_CDS.

## Reading frame

The longest Met-initiated ORF in the pseudogene span (feature orientation) is 78 aa and
identical to the UniProt Q9H4G8 sequence, so the frame is intact on the genome. It ends
four residues before DPH3's C-terminus, so DPH3's terminal LVKC is missing.

## Residue comparison (global alignment, BLOSUM62)

- 70 identical positions over the 82-residue parent (85.4%), 78 aligned pairs.
- Substitutions (target/parent): C24/Y24, E38/D38, G44/D44, M47/T47, G50/S50, A65/V65,
  V72/A72, V75/A75.
- The four DPH3 metal ligands that UniProt annotates (C26, C28, C48, C51; Fe/Zn) are all
  **retained** in DPH3P1, at the same positions. They correspond to yeast Dph3 Cys25, Cys27,
  Cys47 and Cys50, which coordinate the metal.
- DPH3P1 has one extra cysteine (C24) next to the CPC motif.

## Interpretation

The reading frame and the CSL zinc-finger ligands are intact, so a translated product
could plausibly fold and bind metal. However, nothing shows that the locus is
transcribed into a coding RNA or translated. It is a processed (retrotransposed) copy,
with a pseudogene biotype in Ensembl and HGNC, no GTEx expression and PE 5. The
residue data therefore do not argue for loss of function. The open question is whether
a product exists at all. We did not check PeptideAtlas for DPH3P1-unique peptides
(an automated query failed). Most DPH3P1 tryptic peptides would also be shared with, or
one substitution away from, DPH3, so any detection would need peptides that cover the
substituted positions.
