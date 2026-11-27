# MORN5 (human, Q5VZ52) review notes

## 2026-11-26: review started from literature-scan issue 7138

The trigger paper is PMID:43076034 (MORN5 is required for sperm mitochondrial homeostasis and male
fertility; J Mol Cell Biol 2026).

### Deep research and literature search

Deep research did not run: falcon returned 403 and the perplexity-lite fallback returned 401
(quota). I searched PubMed for `MORN5 OR "MORN repeat containing 5"` and got 8 hits. The primary
MORN5 papers are:

- PMID:28742876: mouse sperm-tail proteins. Morn5 is detergent-insoluble, associated with the
  flagellar cytoskeleton, and found in human sperm.
- PMID:27630576: chick craniofacial expression and a BMP link.
- PMID:43076034: the trigger paper. Only the abstract is available; Europe PMC lists no open full
  text.

### What the trigger paper adds

These are the first loss-of-function data for MORN5. Two mouse KO lines are male-infertile, and
heterozygotes show intermediate defects. The KO sperm have:

- mitochondrial sheath defects;
- lower membrane potential and ATP;
- lower complex II/III activity;
- more ROS.

Morn5 is enriched in mitochondrial fractions and associates with respiratory-chain and
quality-control proteins. In infertile men there are rare variants, including a destabilising
frameshift.

### Why no NEW rows

- Process (flagellated sperm motility, or sperm mitochondrial sheath assembly): the abstract shows
  that MORN5 is necessary, but not which step it performs. The precedents for a sperm-motility ISS
  NEW, such as ANKEF1, rest on full text showing that the protein is part of the motile machinery.
  Here the defect is energetic and mitochondrial, and could be a consequence of MORN5 loss rather
  than MORN5 participating in motility or sheath assembly.
- Location (mitochondrion): one abstract-level line of evidence, a "mitochondrial fraction" from
  mouse tissue that may not have been checked against other compartments. My own reading of the
  161-aa sequence shows MORN repeats from residue 8, an acidic N-terminus (MEYTGSKYIGEY) with no
  amphipathic presequence, and no TM segment, so I see no import signal. The organelle policy needs
  two independent lines before adding a location, and this is one.

When the full text is available, revisit with the localisation figures. A NEW sperm-motility or
mitochondrion ISS row from mouse may then be justified.

### Annotation decisions

- REMOVE: nine bare GO:0005515 HuRI rows.
- ACCEPT: motile cilium and sperm flagellum (PMID:28742876).

## 2026-11-27: changes after the PR #7148 review

- Motile cilium is now TOO_GENERAL. The evidence is sperm-only, so the term adds nothing beyond sperm flagellum.
- Correction to the localisation note above. The organelle policy's two-line threshold applies to adding a sub-compartment term, not to the root organelle. A root `mitochondrion` row is still not justified, because the abstract-level crude-fraction result cannot be checked for contamination and the full text is unavailable.
- Leads for the MF_DARK gap: three of the HuRI partners, ENKD1, GAS2L2 and MISP, are cilium or cytoskeleton proteins. They would be worth testing as direct partners.
- PMID:43076034 is now flagged `full_text_unavailable: true`.
