# ego-1 (G5EBQ3) review notes

## Provenance / process
- Data fetched with `just fetch-gene worm G5EBQ3 --alias ego-1` (TrEMBL G5EBQ3, 1632 aa, WormBase F26A3.3; same accession as `modules/c_elegans_mutator_22g_rna_amplification.yaml`).
- Deep research (`just deep-research-falcon worm ego-1 --fallback perplexity-lite`) FAILED: falcon timed out (exit 137) and the perplexity fallback provider is not configured. No deep-research file was written. The review relies on cached publications and PubMed searches.

## Key findings
- EGO-1 is an RdRP-family protein required for germline development and for RNAi of germline genes [PMID:10704412 "For a number of germ-line-expressed genes, ego-1 mutants were resistant to a form of PTGS called RNA interference."].
- It produces mRNA-templated triphosphorylated antisense small RNAs [PMID:21396820 "Our data support the conclusion that EGO-1 produces triphosphorylated small RNAs derived from mRNA templates"]. No direct in vitro RdRP assay of EGO-1 was found; RRF-1 accounted for most RdRP activity in the Aoki cell-free system [PMID:18007599].
- RdRP complexes contain DRH-3 [PMID:19800275 "DRH-3 is a core component of RNA-dependent RNA polymerase (RdRP) complexes essential for several distinct 22G-RNA systems."].
- CSR-1 pathway: EGO-1 is on chromosomes and needed for segregation [PMID:19804758 "the RNA-dependent RNA polymerase EGO-1, the Dicer-related helicase DRH-3, and the Tudor-domain protein EKL-1 localize to chromosomes and are required for proper chromosome segregation"].
- Meiotic silencing: [PMID:16271877 "Among C. elegans RdRPs, we find that only EGO-1 is required for H3K9me2 enrichment on unpaired chromosomal regions during meiosis."].
- EGO-1 may make some 22G-RNAs independently of pUG RNAs [PMID:32499657 "Thus, EGO-1 may also produce some 22G siRNAs via a pUG RNA-independent mechanism."].

## Curation decisions
- Nuclear pore localization and P granule assembly (IMP) were marked as over-annotated. They are indirect consequences, because EGO-1 targets include nuclear pore assembly genes [PMID:21396820].
- Germ cell development, oogenesis and spermatogenesis were kept as non-core.
- For the module curator: EGO-1 is mainly the CSR-1 22G-RNA RdRP, and the module's contrast with Mutator/RRF-1 is consistent with the literature. It also contributes partially to WAGO 22G-RNAs.
