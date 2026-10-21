# sec11 notes

## Deep research

No `sec11-deep-research-*.md` provider file was present in the sparse
`genes/NEUCR/sec11/` checkout. I did not write a synthetic provider file; the
manual literature and PAINT synthesis for this review is recorded here instead.

## Literature search

Searches for `Neurospora crassa sec11`, `NCU04519`, `Q7RY44`, and
`Neurospora signal peptidase` found the genome paper that supplied the OR74A
gene model [PMID:12712197], but no paper directly assaying NCU04519/sec11
signal-peptidase activity, essentiality, or localization.

The functional evidence comes from conserved fungal and eukaryotic Sec11/SPC
work:

- Budding yeast `SEC11` was cloned by complementation of the `sec11-7`
  temperature-sensitive secretion mutant; `sec11` cells accumulated
  core-glycosylated invertase and acid phosphatase with intact signal peptides,
  and a null allele at the `SEC11` locus was lethal [PMID:3283143].
- Yeast signal peptidase purification recovered Sec11 as a component of the
  ER signal peptidase complex [PMID:1846444].
- Yeast mutational analysis showed that conserved Ser, His, and Asp residues
  in Sec11 are important for ER signal peptidase activity [PMID:10206957].
- Human cryo-EM structures resolved SPC-A and SPC-C complexes with SEC11A or
  SEC11C catalytic subunits and placed the active site at the ER
  membrane-proximal transmembrane window [PMID:34388369].
- The 2024 yeast Spc2 work used a yeast SPC AlphaFold2-Multimer model and
  in vivo cleavage assays to show that accessory subunits tune the substrate
  and cleavage-site specificity of the Sec11-containing complex
  [PMID:39565596].
- A 2026 substrate-bound human SPC-A structure directly visualized how Sec11A
  engages a signal peptide c-region in a hydrophobic binding groove while the
  h-region sits in the transmembrane window [PMID:42173868].
- A 2026 yeast Sec11 study mapped the C-terminal short helix of Sec11 as a
  membrane-spanning segment that helps stabilize internal signal sequences
  during productive SPC engagement [PMID:42586426].

## PAINT and PANTHER

Q7RY44 is in `PTHR10806:SF6`, the fungal Sec11 subfamily that also contains
*S. cerevisiae* SEC11/P15367. That supports the ISS transfers from the budding
yeast protein and argues against any metazoan-paralog-specific interpretation.

The PTHR10806 PAINT export has three IBD rows:

- `PTN000086749` at the PTHR10806 root: `GO:0008233 peptidase activity`.
  This deliberately shallow root assertion spans bacterial, archaeal, and
  eukaryotic type I signal peptidase relatives. For Q7RY44 the term is true
  but too general because `GO:0009003 signal peptidase activity` is already
  supported.
- `PTN000086750` at Eukaryota: `GO:0005787 signal peptidase complex`.
  This is the correct depth for the ER SPC complex claim.
- `PTN000086750` at Eukaryota: `GO:0051604 protein maturation`.
  This is the conservative process assertion for eukaryotic Sec11-mediated
  signal peptide removal. The historically tempting `GO:0006465 signal
  peptide processing` process term is obsolete, so no replacement process
  term was proposed.

## Annotation decisions

The core conserved annotations are accepted: `signal peptidase activity`,
`signal peptidase complex`, `endoplasmic reticulum membrane`, broad
`endoplasmic reticulum`, and `protein maturation`.

`GO:0004252 serine-type endopeptidase activity` is correct but less specific
than the supported Sec11 catalytic activity, so it is modified to
`GO:0009003 signal peptidase activity`.

Both `GO:0008233 peptidase activity` rows and the `GO:0016020 membrane` row
are true but too general beside accepted specific activity and ER membrane
terms.

`GO:0045047 protein targeting to ER` is removed. The SPC catalytic subunit
cleaves signal peptides once nascent chains have engaged or crossed the ER
translocon; it is not one of the factors that direct proteins toward the ER.
