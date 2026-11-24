# Pgam1 notes

## Workflow notes

`just fetch-gene mouse Pgam1` seeded 34 GOA annotations for UniProt Q9DBJ1 and cached the previously missing GOA PMID 2824255. `just fetch-gene-pmids mouse Pgam1` found six PMIDs in the seeded review and confirmed all six were cached.

Generated deep research could not run in this checkout: `just deep-research-falcon mouse Pgam1 --fallback perplexity-lite` reported both `falcon` and `perplexity` unavailable. This manual review therefore used the fetched GOA/UniProt files, the six cached GOA publications, the existing PTHR11931 family review, and the 61e0/62d0 GO-CAM context.

`just paint-losses mouse Pgam1` reported no PAINT IRD/IKR loss on the Pgam1 lineage.

## Functional summary

Pgam1 is the mouse B/brain, broadly expressed phosphoglycerate mutase isoform. Zhang et al. cloned the mouse Pgam1 and Pgam2 cDNAs, showed Pgam1 was expressed in brain, kidney, liver, thyroid, stomach and heart, and showed that COS7 expression of either ORF raised phosphoglycerate mutase activity above vector controls [PMID:11250083, "the enzyme activities of mouse Pgam1 and Pgam2 were detected to be 2.2-2.5 times"]. The UniProt Q9DBJ1 catalytic record assigns the reversible EC 5.4.2.11 reaction, `2-phosphoglycerate = 3-phosphoglycerate`, and the protein is in the PGAM/BPGM histidine-phosphatase family.

PTHR11931 already has a family review. It scopes `GO:0004619 phosphoglycerate mutase activity` to the active PGAM1 and PGAM2 subfamilies and records the Pgam1/PGAM1 subfamily, SF15, as non-diverged. The PAINT IBD node for `GO:0004619` includes mouse Pgam1 itself as a donor, and the cytosol node likewise includes mouse Pgam1 as one of the seeds, so both IBA rows are accepted here. The family review's bisphosphoglycerate mutase term assessment scopes `GO:0004082` to BPGM and PGAM2, not PGAM1. UniProt transfers EC 5.4.2.4 to mouse Pgam1 from human PGAM1, so the review keeps the seeded BPGM-side-activity rows as non-core and explicitly asks whether this activity should remain asserted for the PGAM1 subfamily.

## GO-CAM context

GO-CAMs 61e0e55600001225 and 62d0afa500000298 use Pgam1 for the cytosolic phosphoglycerate mutase step of mouse gluconeogenesis. The model reaction is chemically coherent: in the gluconeogenic direction Pgam1 converts 2-phosphoglycerate to 3-phosphoglycerate for the downstream Pgk1 step. Pgam1 is the correct liver/kidney-expressed isoform for this shared reverse-of-glycolysis step, unlike the muscle isoform Pgam2.

The GOA `GO:0006094 gluconeogenesis` IDA row cites Collino et al. That paper places Pgam1 in a calorie-restriction transcriptomic pattern favoring gluconeogenesis and reports increased hepatic Pgam1 mRNA, but does not directly assay Pgam1 enzyme flux in gluconeogenesis [PMID:24958256, "Pgam1 = 1.6-fold, p = 0.0057"]. The review therefore keeps gluconeogenesis as a real but non-core pathway context, and the GO-CAM review should continue to mention that the enabled_by evidence for the Pgam1 activity is transcriptomic rather than direct.

## Annotation decisions

- `GO:0004619 phosphoglycerate mutase activity` is the core molecular function and is accepted on all evidence lines, including the two mouse IDA rows.
- `GO:0004082 bisphosphoglycerate mutase activity` is kept as non-core because mouse UniProt transfers the side activity from human PGAM1. PTHR11931 does not currently scope the BPGM term to SF15/PGAM1, so this is flagged as the main residual question.
- `GO:0006096 glycolytic process` is accepted as the core process. Obsolete `GO:0061621 canonical glycolysis` rows are modified to `GO:0006096`.
- `GO:0006094 gluconeogenesis` and `GO:0046166 glyceraldehyde-3-phosphate biosynthetic process` are kept as non-core reverse-pathway contexts.
- `GO:0005737 cytoplasm` is too general once the cytosol rows are asserted.
- The propagated `protein kinase binding` rows are left `UNDECIDED`: the claim is not core and no cached mouse or human primary evidence identifies the relevant kinase-binding assay.
- The HDA `myelin sheath` row is left `UNDECIDED` because the cached PMID 17634366 abstract describes a CNS myelin proteome but does not name Pgam1.
- The PGAM4-derived `sperm principal piece` row is marked over-annotated for Pgam1. The remaining specialized locations (`nucleus`, `neuronal cell body`, `ooplasm`) are plausible but non-core cytoplasmic or tissue-context rows; `rough endoplasmic reticulum cisterna` is over-annotated for this soluble cytosolic enzyme.
