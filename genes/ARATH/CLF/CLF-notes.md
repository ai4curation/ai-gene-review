# CLF curation notes

## Session 2026-10-06 (vernalization_flc_silencing module follow-up)

- P93831, At2g23380. Fetched by accession. Deep research was not run because falcon is unavailable in this environment.
- Catalytic E(z) subunit: [PMID:17881378 "Disrupted ATX1 or CLF function results in misexpression of AG, recognizable phenotypes and loss of H3K4me3 or H3K27me3 histone H3-tail marks, respectively."]
- In vivo complexes: [PMID:26642436 "confirming that CLF occurs in both VRN2-PRC2 and EMF2-PRC2 complexes in vivo."]
- Vernalization spreading: [PMID:40858112 "the stable spread H3K27me3 state in mutants defective in one of the PRC2 methyltransferases genes, CURLY LEAF (CLF) or LIKE HETEROCHROMATIN PROTEIN 1, required to maintain long-term silencing."]

## Decisions
- All 25 protein-binding rows -> REMOVE (uninformative; complex membership captured by NEW ESC/E(Z) complex).
- Transcription corepressor binding (AG partner) -> MODIFY to DNA-binding TF binding, matching VRN2/FIE/MSI1.
- Transcription initiation-coupled chromatin remodeling (MEA imprinting) -> MODIFY to GO:0045814.
- Developmental, ABA, callus, transformation and endosperm phenotypes -> KEEP_AS_NON_CORE. COLDAIR ssRNA binding -> non-core.
