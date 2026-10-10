# GCY1 (YOR120W, P14065) notes

Module context: `glycerol_metabolism`, glycerol dehydrogenase step, annoton akr_glycerol_dehydrogenase_activity (GENE_PRODUCT GCY1), MF GO:0047953, BP GO:0019563, cytosol. GCY1 is not in the YeastPathways summary file (no YeastCyc reaction rows, no RCA annotations in GOA). No S. cerevisiae GO-CAM contains GCY1.

## Evidence
- Aldo-keto reductase (AKR3A1), EC 1.1.1.156, cytoplasm [UniProt:P14065].
- In vivo glycerol dehydrogenase: [PMID:22979944 "DHA was not detected in the gcy1 gene-disrupted strain but accumulated 225.91 μmol g DCW(-1) in a DHA kinase gene-deficient strain under micro-aerobic conditions."]; [PMID:22979944 "Metabolic profiling showed that the GCY1 gene product functions as a GLY dehydrogenase in S. cerevisiae, particularly under micro-aerobic conditions."].
- Broad NADPH carbonyl reductase: [PMID:17140678 "In preliminary studies, we showed that Gre3, Ypr1, Gcy1, and human AR, purified as recombinant proteins, have NADPH-dependent aldo-keto reductase activity using aldehyde substrates such as DL-glyceraldehyde and p- nitrobenzaldehyde [ 8 ]."]; Y55F inactive [PMID:17140678 "mutagenesis of the presumptive hydrogen donor to create the Y55F mutant of AKR3A1 (Gcy1) resulted in essentially complete loss of AKR activity."].
- Paralog: [PMID:17140678 "AKR3A1 (Gcy1) and AKR3A2 (Ypr1), which are approximately 65% identical"].
- Xylose/arabinose: [PMID:12271459 "Decreased arabitol formation from L-arabinose indicates that Gre3p, Ypr1p and the protein encoded by YJR096w are the major arabinose reducers in S. cerevisiae."] -> Gcy1 not a major contributor; and S. cerevisiae lacks native pentose catabolism.
- mRNA binding: [PMID:20844764 "DNA microarray analysis of RNAs enriched in association with TAP-tagged Gcy1 and Pcs60 identified specific RNAs associated with each of these proteins"].

## Caveats
- No purified-enzyme kinetics for glycerol oxidation are in the cached abstracts; UniProt's EC assignment cites kinetic papers measured in the reductase direction (DL-glyceraldehyde). The in vivo assignment rests on metabolite profiling. YPR1 (65% identical) may contribute.

## Decisions
- Core MF GO:0047953 in cytosol, BP GO:0019563.
- Pentose catabolism IEA -> REMOVE; IDA -> MARK_AS_OVER_ANNOTATED.
- Aldose reductase / alcohol dehydrogenase (NADP+) / mRNA binding / oxidative stress IGI -> KEEP_AS_NON_CORE.
