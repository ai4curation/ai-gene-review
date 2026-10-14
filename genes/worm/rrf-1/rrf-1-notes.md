# rrf-1 (G5ECM1) review notes

## Provenance / process
- Fetched with `just fetch-gene worm G5ECM1 --alias rrf-1`. UniProt has three unreviewed rrf-1 entries (G5ECM1 1601 aa, Q7JLA0 1601 aa, G3MU40 1520 aa). G5ECM1 is the one cross-referenced to WormBase F26A3.8a and is the one used in `modules/c_elegans_mutator_22g_rna_amplification.yaml`.
- Deep research FAILED (falcon timeout; perplexity fallback not configured). No deep-research file was written. The review uses cached publications and PubMed.

## Key findings
- Biochemical RdRP: [PMID:18007599 "The RRF-1 complex is predominantly responsible for the RdRP activity, and synthesizes secondary-type siRNA molecules in a Dicer-independent manner."]
- Mutator foci: [PMID:22713602 "The RdRP RRF-1 colocalizes with MUT-16 at Mutator foci, suggesting a role for Mutator foci in siRNA amplification."]; purified mutator complexes make siRNAs in vitro [PMID:24684932].
- pUG templates: [PMID:32499657 "Together, these data show that the RdRP RRF-1 interacts with UG repeat RNAs"].
- Soma: [PMID:21396820 "The secondary step involves the activity of the RdRP RRF-1 in the soma"].

## Curation decisions
- Protein binding (DRH-3) was modified to DEAD/H-box RNA helicase binding. Nucleotidyltransferase activity was modified to RNA-directed RNA polymerase activity.
- The nuclear RDRC (GO:0031380) IBA was marked as over-annotated. The RRF-1 complex acts in cytoplasmic Mutator foci, and among the RdRPs only EGO-1 is needed for meiotic H3K9me2 [PMID:16271877].
