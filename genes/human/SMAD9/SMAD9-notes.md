# SMAD9 manual review notes

Automated deep research was attempted with Falcon and the configured
`perplexity-lite` fallback, but both provider calls failed before any literature
analysis because `agentapi` was not available in the shared runtime. This manual
review therefore used the seeded GOA-derived rows, the cached primary
publications and Reactome records, the UniProtKB O15198 record, the sibling
SMAD1 review, `modules/bmp_signaling.yaml`, and the cached GO-CAM review for
`gomodel:66e382fb00001232`.

## Core function

SMAD9 is a receptor-regulated SMAD in the BMP branch of TGF-beta superfamily
signaling. BMP-family type I receptors phosphorylate its C-terminal SXS motif,
after which SMAD9 forms SMAD complexes, accumulates in the nucleus, and binds
BMP-responsive DNA through its MH1 domain. PMID:25534700 directly compared
constitutively active Smad1, Smad5, and Smad9 variants and showed that Smad9
can bind BMP-responsive DNA and enter BMP-regulated SMAD complexes, but that it
has weaker activation potential than Smad1/Smad5 and represses BMP output as a
dominant-negative feedback regulator.

SMAD9 agrees with GO-CAM 66e382fb00001232 at the depicted level: a
BMP-regulated nuclear RNA polymerase II DNA-binding transcription-factor
activity in the BMP signaling pathway. The GO-CAM edge from BMPR1A to SMAD9 is
biologically consistent with the BMP module, but its cited PMID:9136927 tests
Smad1 directly and does not itself test SMAD9; the GO-CAM review already records
that source-specific caveat.

## Annotation decisions

The chromatin, nucleus, nucleoplasm, cytoplasm, and cytosol locations are all
kept. Nucleus/chromatin/nucleoplasm represent the active transcriptional state;
cytoplasm/cytosol represent receptor-proximal shuttling and Reactome pathway
intermediates, so they are non-core.

The broad transcription and developmental process rows are downstream context.
`GO:0030509 BMP signaling pathway`, `GO:0060395 SMAD protein signal
transduction`, and new negative-regulation rows capture the central pathway.
The older `GO:0007179 transforming growth factor beta receptor signaling
pathway` row is kept by curator deference and by analogy with the completed
SMAD1 review, while the direct SMAD9 paper shows BMP-specific induction rather
than TGF-beta1 induction. `GO:0141091 transforming growth factor beta receptor
superfamily signaling pathway`, `GO:0071363 cellular response to growth factor
stimulus`, `GO:0071773 cellular response to BMP stimulus`, and the generic
transcription parents are less informative than child rows present in this
review.

All `GO:0005515 protein binding` rows were removed under the project bare
protein-binding policy. They report useful interactions with LEMD3, SMAD4,
RANBP3L, GRN, KDM1A, PRMT6, or high-throughput partners, but a generic
protein-binding annotation does not name the BMP R-SMAD function that those
interactions regulate.
