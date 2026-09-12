# GRHPR (Q9UBQ7) review notes

Human glyoxylate reductase/hydroxypyruvate reductase (GRHPR; HGNC:4570; gene 9380 on chr9).
D-isomer-specific 2-hydroxyacid dehydrogenase family. 328 aa, ~35.7 kDa, homodimer.

Deep research: falcon provider was OUT OF CREDITS (HTTP 402), so no
`-deep-research-falcon.md` was generated. Review is grounded in the UniProt record,
the seeded GOA, and cached `publications/PMID_*.md` (mostly abstract-only).

## Core biology (verified)
- Cytosolic NADPH-dependent reductase of glyoxylate detoxification.
- Reduces glyoxylate -> glycolate (EC 1.1.1.79) and hydroxypyruvate -> D-glycerate
  (EC 1.1.1.81); also oxidizes D-glycerate -> hydroxypyruvate. Prefers glyoxylate and
  hydroxypyruvate, not pyruvate [PMID:16756993].
- Function is to remove the metabolic by-product glyoxylate in the liver, keeping it
  from being oxidised to oxalate [PMID:16756993 "plays a critical role in the removal
  of the metabolic by-product glyoxylate from within the liver"].
- Deficiency causes primary hyperoxaluria type 2 (PH2): elevated urinary oxalate and
  L-glycerate, calcium-oxalate nephrolithiasis, nephrocalcinosis, renal failure
  [PMID:10484776; UniProt DISEASE].

## Localization
- GOA/UniProt: cytosol (IBA GO:0005829), cytoplasm (IDA, LIFEdb).
- Reactome annotates a peroxisomal-matrix location (TAS) and calls the enzyme
  peroxisomal; the enzyme is predominantly cytosolic (no PTS1/PTS2 in the 328-aa
  sequence; ends "...ELKL"). Peroxisomal location is disputed/minor -> KEEP_AS_NON_CORE.
- Mitochondrion (HTP, PMID:34800366 large-scale MS) and extracellular exosome
  (HDA, several proteomics screens) are high-throughput localizations, not the site of
  catalytic action -> KEEP_AS_NON_CORE / MARK_AS_OVER_ANNOTATED.

## MF term choices in GOA
- GO:0030267 glyoxylate reductase (NADPH) activity  -- primary MF (IBA + IDA x2 + IEA + Reactome TAS)
- GO:0016618 hydroxypyruvate reductase [NAD(P)H] activity -- IDA x3 + IEA
- GO:0120509 hydroxypyruvate reductase (NADPH) activity -- EXP x2 + IEA
- GO:0008465 hydroxypyruvate reductase (NADH) activity -- IBA + IDA + IEA
- GO:0106345 glyoxylate reductase activity (parent) -- ARBA IEA
- GO:0016616 (parent oxidoreductase) -- InterPro IEA
- NAD/NADP/NADPH binding, carboxylic acid binding -- cofactor/substrate binding, accept as non-core molecular detail.

## Interactions / complex
- GO:0005515 protein binding IPI (PMID:23599041, with SLC23A1/hSVCT1). Bare protein
  binding -> MARK_AS_OVER_ANNOTATED (uninformative term; keep record of SLC23A1 interaction).
- GO:0042803 protein homodimerization activity (IDA, PMID:16756993) -- ACCEPT; enzyme is a homodimer.
- GO:0070402 NADPH binding (IDA, PMID:16756993) -- ACCEPT cofactor binding, non-core.
- GO:1902494 catalytic complex (part_of, IDA PMID:16756993) -- the "complex" is the
  catalytic homodimer; generic term -> KEEP_AS_NON_CORE (homodimerization better captures it).

## Core functions (for core_functions block)
1. MF GO:0030267 glyoxylate reductase (NADPH) activity, directly_involved_in
   BP GO:0046487 glyoxylate metabolic process, located_in GO:0005829 cytosol.
2. MF GO:0016618 hydroxypyruvate reductase [NAD(P)H] activity (serine/glycerate branch).
