# PutA evidence review — 2026-11-06

## Identity and experimental scope

Accession F7X6I3 is the 1233-residue protein from Sinorhizobium meliloti SM11. RCSB 5KF6 polymer entity 1 contains the entire frozen UniProt sequence exactly, with an N-terminal `SM` construct remnant. SIFTS independently maps the same accession at full reference coverage. The reproducible sequence hashes and official API URL are in [identity.yaml](putA-source-analysis/identity.yaml). These establish protein identity, not a native-culture phenotype.

PMID:27679491 names the 1233-residue construct (RefSeq WP_010968598.1) from the New York Structural Genomics Research Consortium in pNIC28-Bsa4, with a cleavable His6 tag. Its deposited sequence matches F7X6I3/SM11, not the 1224-residue P95629 record. Native SM11 growth, uptake and gene regulation were not assayed. CoQ1 explicitly served as flavin electron acceptor; NAD+ served the separate GSALDH reaction. The extra C-terminal Rossmann fold does not bind NAD+, while the catalytic GSALDH Rossmann domain does. Near-zero coupled-reaction lag compared with a predicted six-minute free-diffusion lag supports channeling; the CTD tunnel-sealing interpretation is structure-based. Concentration-dependent monomer–dimer mixtures do not establish an obligatory dimer.

## Annotation judgments

Both catalytic activities and direct proline-catabolic participation are retained. Generic oxidoreductase activity is refined to both existing specific activities. The active cytoplasmic membrane face is retained as mechanistic inference from peripheral-membrane PutA chemistry, not claimed as a target localization assay. No uptake, growth, stress-response or transcriptional-regulatory activity is manufactured from the fused enzyme. IPR025703 regulatory mappings are marked over-annotated because the characterized type A/B architecture lacks the type C RHH domain; this is not a demonstrated evolutionary loss or a universal negative DNA-binding assay. Proline biosynthesis is a direction/pathway error: sharing P5C/GSAL with a biosynthetic pathway does not mean this enzyme performs its work. No NEW rows were added.

## Research and reproducibility

The required default Falcon request genuinely failed with HTTP403 (authentication/access); no provider report was created. Manual research used the primary papers and full comparative reviews PMID:28712849 and PMID:28990412. QuickGO definitions were retrieved on 2026-11-06: GO:0004657 explicitly names quinone/quinol, GO:0003842 explicitly NAD+/NADH, and GO:0055129 denotes formation of L-proline. Original annotation payloads/order and raw UniProt/GOA files are protected by the pre-edit seed baseline.


## 2026-11-06 PR #6150 review follow-up

The two IPR025703 transcription mappings now use REMOVE, matching BjPutA/GsPutA/CfPutA on the same solved non-RHH architecture criterion. No direct negative DNA-binding assay is claimed. The proline-biosynthesis rejection now leads with the paper's actual separation of the pathways rather than the generic NADH assay methods. [PMID:27679491 "Furthermore, P5C/GSAL is also the intermediate of proline biosynthesis, so channeling provides a mechanism for segregating catabolism and biosynthesis ( 21 )."]

The scoped action ledger and ontology checks are in `analysis/module_audits/bacterial_fused_puta_proline_catabolism/round1-action-reversal-ledger.yaml` and `round1-review-response.md`. Original annotation rows and source fields are retained in order.


## 2026-11-07 PR #6150 round3 follow-up

Removed only the second identical PMID:27679491 channeling quotation from the GO:0055129 review support list. The retained channeling passage and independent coupled NADH-production passage still support the same REMOVE decision on the biosynthetic-pathway mapping. The underlying primary describes segregation of catabolism and biosynthesis and directly assays the proline-consuming coupled reaction. All annotation payloads, actions, core functions, and other evidence are unchanged.
