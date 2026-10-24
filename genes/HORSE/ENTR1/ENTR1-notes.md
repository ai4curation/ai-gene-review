# ENTR1 (horse, A0A5F5Q1J2) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Benchmark target for the DONKEY40_HORSE_PARTNER cohort. No previous review existed; the folder
was created with `just fetch-gene HORSE A0A5F5Q1J2 --alias ENTR1` (stub id confirmed as
A0A5F5Q1J2). ProtNLM2 output was not opened or used.

### Deep research

`just deep-research-falcon HORSE ENTR1 --fallback perplexity-lite` failed: falcon returned
"Failed to authenticate" and the perplexity fallback returned HTTP 401 (insufficient quota). No
deep-research file was produced. The review relies on the cached primary literature on human
ENTR1 (PMID:23108400 abstract only; PMID:25278552 and PMID:27767179 full text), the human and
horse UniProt records, QuickGO annotation lists for human Q96C92 and mouse A2AIW0, and the
sequence analysis below.

### Identity of the benchmark accession

- Unreviewed TrEMBL entry, 459 aa, PE 3, PANTHER PTHR31259:SF3; Pfam ENTR1 coiled-coil region
  (PF29363) at 281-450 [file:HORSE/ENTR1/ENTR1-uniprot.txt "Belongs to the ENTR1 family."].
- It is the Ensembl-canonical product (ENSECAT00000070964) of horse ENTR1
  (ENSECAG00000010463). Two other unreviewed models of the same gene exist: F6QT44 (448 aa)
  and A0A3Q2H8N2 (360 aa); both are 100% identical to the target where they align and differ
  only in N-terminal alternative exons
  [file:HORSE/ENTR1/ENTR1-bioinformatics/RESULTS.md "F6QT44 (448 aa) is identical to the target over all 410 paired residues"].
- Versus human ENTR1 Q96C92 (435 aa): 85.82% identity over 409 paired residues. The target
  lacks the exon equivalent to human residues 75-97 (the segment absent in human isoform 2,
  VSP_032177) and carries a 37-residue Gly/Arg-rich insertion (24-60) inside the disordered
  N-terminus. 77 of the human 1-100 residues align, 64 identical
  [file:HORSE/ENTR1/ENTR1-bioinformatics/RESULTS.md "77 of 100 human residues are paired with horse residues, 64 of them identical."].
- Conclusion: not a fragment. It is a full-length, canonical gene product whose splice pattern
  resembles human isoform 2 in the N-terminal disordered region. The conserved coiled-coil
  region is intact, and most of the human N-terminal basal-body/IFT88-binding region is
  conserved.

### Evolutionary grounding

- Mammalian ENTR1 is single-copy; horse, mouse and human ENTR1 are one-to-one orthologs.
- PANTHER places horse and mouse ENTR1 in PTHR31259:SF3 but human ENTR1 in SF6
  [file:HORSE/ENTR1/ENTR1-bioinformatics/RESULTS.md "Horse and mouse ENTR1 are in subfamily SF3, while human ENTR1 is assigned to SF6."].
  The split separates orthologs (human vs other mammals), which looks like an HMM-scoring
  artifact rather than a biological paralog boundary. The IBA nodes used here sit above it:
  PTN002039065 (endosome, centrosome, midbody, cytokinesis) and PTN004793274 (basal body,
  cilium assembly, ciliary protein localization) are both seeded by human Q96C92 and propagate
  to SF3 members including horse and mouse, so the PAINT curator judged these functions to be
  inherited across the split.
- PAINT did NOT propagate human ENTR1's IMP `GO:0032456 endocytic recycling` or the IDA
  `colocalizes_with GO:0030904 retromer complex`. Horse receives both only via Ensembl Compara
  (GO_REF:0000107). Following the campaign rule, the PAINT omission is treated as deliberate:
  these rows are kept as non-core rather than promoted to core.

### Human literature (donor evidence)

- Endosomal protein of early/recycling endosomes; midbody accumulation in cytokinesis;
  over-expression and depletion both cause multinucleate cells; complex with PTPN13 and GIT1
  [PMID:23108400 "SDCCAG3 is a novel endosomal protein, primarily localized at the early/recycling endosomal compartment"].
- VPS35 interactome hit; colocalizes with retromer-decorated endosomes; depletion reduces
  surface GLUT1, with only minor effects on other cargo (CD97)
  [PMID:25278552 "Suppression of SDCCAG3 led to a decrease in GLUT1 surface expression and a reduction in whole-cell levels"].
- Basal body localization, IFT88 binding via aa 1-100, required for ciliary length/number and
  polycystin-2 ciliary localization
  [PMID:27767179 "we demonstrate that SDCCAG3 is important for ciliary localization of the membrane protein Polycystin-2"].
- Mouse: required for TNFRSF1A surface presentation (PMID:16332174, not cached; via mouse
  UniProt only). Not used as support.
- No molecular activity has been defined for ENTR1 in any species; it is an adaptor-like
  coiled-coil protein. No MF term is proposed.

### Decisions

- early endosome, recycling endosome (IBA + IEA): ACCEPT (core location).
- endosome (IEA): MODIFY to early endosome / recycling endosome (both already on the gene).
- centrosome, midbody, ciliary basal body (IBA + IEA): KEEP_AS_NON_CORE.
- regulation of cytokinesis (IBA + IEA): ACCEPT; human IDA, PAINT-propagated.
- positive regulation of cilium assembly, positive regulation of protein localization to
  cilium (IBA + IEA): ACCEPT; human IMP, PAINT-propagated at PTN004793274.
- endocytic recycling (IEA): KEEP_AS_NON_CORE (PAINT omission, cargo-selective knockdown
  effect).
- retromer complex colocalizes_with (IEA): KEEP_AS_NON_CORE; qualifier respected, ENTR1 is not
  a retromer subunit.
- No NEW annotations.

### Relative for next review

Human ENTR1 (Q96C92), the PAINT donor and the only experimentally characterized ortholog.
No `genes/human/ENTR1` review exists. The donkey ENTR1 (genes/EQUAS/ENTR1) is the cohort partner
and is reviewed separately.

### Modules

No module in `modules/` includes ENTR1, and ENTR1 is absent from `gocams/index.tsv`.
`modules/dmel_retromer.yaml` and `modules/intraflagellar_transport.yaml` cover related
machinery, but ENTR1 is not a part of either.
