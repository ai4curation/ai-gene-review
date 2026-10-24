# PTS notes

## 2026-10-20 ORGANELLES batch 1 (mitochondrion rows)

- Rows: GO:0005739 IBA (PTN000287347) and IDA (LIFEdb, GO_REF:0000054); both kept KEEP_AS_NON_CORE, reasons rewritten to record the check.
- IBA seed: the GO:0005739 IBD at PTN000287347 (PTHR12589-paint.tsv) is seeded only by Q03393 (human PTS) itself, i.e. by the LIFEdb GFP-fusion row. The IBA adds no independent evidence.
- Evidence against a substantial mitochondrial pool: no curated UniProt subcellular location, no transit peptide or TM feature (145 aa); Human Protein Atlas (proteinatlas.org API, queried 2026-10-20) gives main location Cytosol; the pathway literature treats PTPS as cytosolic [file:human/PTS/PTS-deep-research-falcon.md "Cellular localization: PTPS is a soluble cytosolic enzyme functioning within the cytosolic de novo BH4 synthesis machinery"].
- Decision: the claim is weak but rests on a direct (screen) row that is not overruled; both rows kept non-core rather than splitting IBA to MARK_AS_OVER_ANNOTATED. No sub-compartment. Candidate for curator re-check of the LIFEdb row and the PAINT node.

## 2026-10-24 HPA detail (ORGANELLES)

- Human Protein Atlas subcellular entry for ENSG00000150787 (downloaded 2026-10-24, XML/JSON): antibody HPA001481, passes the protein-array validation; immunofluorescence in A-431, U-251MG and U2OS gives cytosol only; reliability "Approved" (one antibody, no independent second antibody or GFP line). Counterstains are nucleus, microtubules and ER; no mitochondrial marker is used, so a small mitochondrial pool is not excluded but none is seen.
- The only mitochondrial line is the LIFEdb GFP-fusion screen (GO_REF:0000054), which also seeds the PAINT IBD at PTN000287347 alone.
- With one direct but low-resolution screen row for, and one approved antibody row against, neither row can be accepted or overruled: both GO:0005739 rows changed KEEP_AS_NON_CORE -> UNDECIDED. A mitochondrial co-stain or fractionation of endogenous PTPS would settle it.
