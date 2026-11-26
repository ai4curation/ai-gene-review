# CARS1 manual review notes

Seeded CARS1 from the current GOA file and reviewed 27 annotation rows. The GOA
file is populated, not header-only.

Key evidence:

- PMID:11347887 cloned and expressed the full-length human cytoplasmic CysRS cDNA
  and showed that the full-length and alternative products "were active in
  aminoacylation of human cytoplasmic tRNA(Cys) with cysteine".
- PMID:10908348 identified an exon-2-containing testis isoform. The inserted
  peptide bound EF-1 gamma, while "CRS containing the exon 2-encoded peptide
  retained catalytic activity comparable to that lacking this peptide".
- PMID:17303165 directly dissected human CysRS tRNA recognition and reports that
  "the C-terminal extension enhances stable binding of human CysRS to its
  cognate tRNA during aminoacylation". It also found the full-length enzyme and a
  C-terminal truncation to behave as dimers by gel filtration and light
  scattering.
- PMID:30824121 links recessive CARS1 variants to reduced cytosolic tRNA(Cys)
  charging: "Compared to control cells and those isolated from the unaffected
  mother in family 1, each subject showed significantly reduced CARS activity".
- Reactome:R-HSA-379887 places CARS1 in the cytosolic cysteine + tRNA(Cys) +
  ATP reaction.

Annotation decisions:

- Kept the cysteine-tRNA ligase, ATP binding, tRNA binding, cytosol, and
  identical protein binding rows.
- Marked `GO:0005737` cytoplasm too general because all four rows are true but
  imprecise beside the accepted cytosol rows.
- Marked generic nucleotide binding and aminoacyl-tRNA ligase activity too
  general beside ATP binding and cysteine-tRNA ligase activity.
- Modified all obsolete `GO:0006423` rows to the live
  `GO:0006418` tRNA aminoacylation for protein translation term; cysteine
  specificity is already carried by the molecular function rows.
- Removed only the bare `GO:0005515` protein binding row. The EEF1G interaction
  in PMID:10908348 is real, but the GO term is the project-level
  uninformative-binding exception.
- Left the Ensembl-transferred response to mechanical stimulus row undecided
  because this review did not verify the rat donor mechanism and did not find
  direct human CARS1 evidence for that process.
- GOA `GO:0009612` cites `GO_REF:0000107` with
  `UniProtKB:A0A8I5Y9V4|ensembl:ENSRNOP00000078006`; this rat donor was not
  verified during the CARS1/PTHR10890 family pass.

PANTHER:

- CARS1 is the cytosolic animal subclade under `PANTHER:PTN000854715`, which
  carries the cytosol IBD. The family-root cysteine-tRNA ligase, obsolete
  cysteinyl-tRNA aminoacylation, and cytoplasm IBDs also reach CARS1 and CARS2.
