# SMAD5 manual review notes

Automated deep research was attempted with Falcon and the configured
`perplexity-lite` fallback, but both provider calls failed before any literature
analysis because `agentapi` was not available in the shared runtime. This manual
review therefore used the seeded GOA-derived rows, the cached primary
publications and Reactome records, the UniProtKB Q99717 record, the sibling
SMAD1 review, `modules/bmp_signaling.yaml`, and the cached GO-CAM review for
`gomodel:66e382fb00001232`.

## Core function

SMAD5 is a receptor-regulated SMAD in the BMP branch of TGF-beta superfamily
signaling. BMP-family type I receptors phosphorylate its C-terminal SXS motif,
after which SMAD5 joins SMAD4-containing complexes, accumulates in the nucleus,
binds BMP-responsive cis-regulatory DNA through its MH1 domain, and regulates
RNA polymerase II transcription. This is the SMAD5 activity represented in the
BMP4 GO-CAM.

SMAD5 agrees with GO-CAM 66e382fb00001232 at the depicted level: a
BMP-regulated nuclear RNA polymerase II DNA-binding transcription-factor
activity in the BMP signaling pathway. The GO-CAM edge from BMPR1A to SMAD5 is
biologically consistent with the BMP module, but its cited PMID:9136927 tests
Smad1 directly and does not itself test SMAD5; the GO-CAM review already records
that source-specific caveat.

PMID:28675158 establishes a second, BMP-independent cytoplasmic role for SMAD5:
non-phosphorylated SMAD5 senses intracellular pH, binds HK1, promotes
glycolysis, and supports mitochondrial respiration. SMAD5-deficient human ES
cells had glycolytic defects that could be rescued by cytoplasmic SMAD5
[PMID:28675158 "the glycolysis rate in Smad5 KO hES cells could be rescued"],
so the cytoplasm and cytosol rows are not only pre- or post-BMP-transit
locations even though the BMP transcriptional relay remains the GO-CAM-aligned
nuclear function.

## Annotation decisions

The BMP/SMAD transcriptional function is the core function. Osteoblast
differentiation, stem-cell differentiation, anti-Mullerian hormone signaling,
hepcidin regulation, ureteric bud development, Mullerian duct regression,
embryonic patterning, cardiac conduction, and granulosa-cell Fas/apoptosis rows
are retained as contextual outputs or marked as less informative parents.

SMAD5 has a reported mitochondrial localization in unstimulated human
chondroprogenitor cells. This is kept as a non-core root-organelle localization:
the assay supports the mitochondrion and UniProt propagates the same location,
but it does not establish a mitochondrial subcompartment or make mitochondrion
the place where the BMP R-SMAD transcriptional function acts.

The HK1/glycolysis activity in PMID:28675158 supports new annotations to kinase
binding, enzyme activator activity, and positive regulation of glycolysis. The
same study also reports long-term mitochondrial respiration phenotypes after
SMAD5 loss, but the immediate mechanistic evidence is strongest for cytoplasmic
HK1-linked glycolysis.

All `GO:0005515 protein binding` rows were removed under the project bare
protein-binding policy. Specific binding rows that name a regulatory function,
such as DDX5/DEAD-box helicase binding and ubiquitin-protein-ligase binding, are
kept as non-core because they identify separable regulation of pri-miRNA
processing or SMAD turnover.
