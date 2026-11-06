# PutA evidence review — 2026-11-06

## Identity and experimental scope

Accession F7X6I3 is the 1233-residue protein from Sinorhizobium meliloti SM11. RCSB 5KF6 polymer entity 1 contains the entire frozen UniProt sequence exactly, with an N-terminal `SM` construct remnant. SIFTS independently maps the same accession at full reference coverage. The reproducible sequence hashes and official API URL are in [identity.yaml](putA-source-analysis/identity.yaml). These establish protein identity, not a native-culture phenotype.

PMID:27679491 names the 1233-residue construct (RefSeq WP_010968598.1) from the New York Structural Genomics Research Consortium in pNIC28-Bsa4, with a cleavable His6 tag. Its deposited sequence matches F7X6I3/SM11, not the 1224-residue P95629 record. Native SM11 growth, uptake and gene regulation were not assayed. CoQ1 explicitly served as flavin electron acceptor; NAD+ served the separate GSALDH reaction. The extra C-terminal Rossmann fold does not bind NAD+, while the catalytic GSALDH Rossmann domain does. Near-zero coupled-reaction lag compared with a predicted six-minute free-diffusion lag supports channeling; the CTD tunnel-sealing interpretation is structure-based. Concentration-dependent monomer–dimer mixtures do not establish an obligatory dimer.

## Annotation judgments

Both catalytic activities and direct proline-catabolic participation are retained. Generic oxidoreductase activity is refined to both existing specific activities. The active cytoplasmic membrane face is retained as mechanistic inference from peripheral-membrane PutA chemistry, not claimed as a target localization assay. No uptake, growth, stress-response or transcriptional-regulatory activity is manufactured from the fused enzyme. IPR025703 regulatory mappings are marked over-annotated because the characterized type A/B architecture lacks the type C RHH domain; this is not a demonstrated evolutionary loss or a universal negative DNA-binding assay. Proline biosynthesis is a direction/pathway error: sharing P5C/GSAL with a biosynthetic pathway does not mean this enzyme performs its work. No NEW rows were added.

## Research and reproducibility

The required default Falcon request genuinely failed with HTTP403 (authentication/access); no provider report was created. Manual research used the primary papers and full comparative reviews PMID:28712849 and PMID:28990412. QuickGO definitions were retrieved on 2026-11-06: GO:0004657 explicitly names quinone/quinol, GO:0003842 explicitly NAD+/NADH, and GO:0055129 denotes formation of L-proline. Original annotation payloads/order and raw UniProt/GOA files are protected by the pre-edit seed baseline.
