# SEPTIN14P20 / RBRP (C0HM01): relationship to the parental septin

Script: `align_to_septin14.py` (Biopython local alignment, BLOSUM62, gap open -11 / extend -1;
sequences fetched live from UniProt REST). Raw output: `output.txt`.

## Results (from output.txt)

- RBRP vs human SEPTIN14 (Q6ZU15, 432 aa): RBRP residues 1-47 align to SEPTIN14 residues
  383-429 with 47/47 identities (100%). The remaining RBRP residues 48-71
  (PDPYEFLLLRKIKHPGFNEELSPC) do not align; SEPTIN14 instead ends ...DTKKDKHRKK.
- RBRP vs SEPTIN7 (Q16181): weak, 13/33 identities (39%) over the coiled-coil region,
  i.e. ordinary septin-family similarity.
- RBRP Gly-19, the residue whose G19A mutation abolishes IGF2BP1 binding (PMID:32245947),
  lies in the SEPTIN14-identical segment (it corresponds to SEPTIN14 Gly-401).

## Interpretation

- The RBRP ORF is the retained septin-14 reading frame of the SEPTIN14P20 pseudogene: the
  first two-thirds of the peptide reproduce the C-terminal coiled-coil region of SEPTIN14
  exactly, and only a 24-residue C-terminal tail is unique.
- This contradicts the statement in PMID:32245947 that no matching proteins exist for RBRP.
- Consequence for existence evidence: an antibody or MS peptide confined to residues 1-47
  cannot distinguish RBRP from SEPTIN14 (or a SEPTIN14 fragment). The anti-RBRP antigen
  (TDTKKDKHPDPY, residues 41-52) spans the junction, with 8 SEPTIN14-shared and 4 unique
  residues. Only tryptic peptides from the unique tail (e.g. HPDPYEFLLLR, HPGFNEELSPC) would be
  RBRP-specific; the paper does not list which peptides were observed, and its database search
  was against a custom RBRP database, so cross-identification cannot be ruled out from the text.
- The IGF2BP1-binding determinant (Gly-19) is septin-14 sequence, so the binding surface is not
  novel to RBRP. Whether SEPTIN14's own C-terminal region binds IGF2BP1 is untested.
