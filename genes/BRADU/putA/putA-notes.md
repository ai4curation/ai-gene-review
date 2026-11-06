# PutA evidence review — 2026-11-06

## Identity and experimental scope

Accession Q89E26 is the 999-residue protein from Bradyrhizobium diazoefficiens USDA 110. RCSB 3HAZ polymer entity 1 contains the entire frozen UniProt sequence exactly, with an N-terminal `GH` construct remnant. SIFTS independently maps the same accession at full reference coverage. The reproducible sequence hashes and official API URL are in [identity.yaml](putA-source-analysis/identity.yaml). These establish protein identity, not a native-culture phenotype.

PMID:20133651 identifies BjPutA, the 999-residue protein historically named Bradyrhizobium japonicum; current Q89E26 taxonomy is Bradyrhizobium diazoefficiens USDA110. Primary structure and solution/kinetic evidence support the two catalytic activities, channeling and self-association. Main text was independently readable at https://pmc.ncbi.nlm.nih.gov/articles/PMC2840367/; direct programmatic access returned a browser challenge and EuropePMC XML returned HTTP500. The cached publication remains untouched and abstract-only; supporting quotations from that cache are flagged accordingly. The inaccessible supplemental methods prevent assigning the exact acceptor to every original kinetic trace. Quinone coupling is supported by the established reaction-class synthesis in PMID:28712849; FAD alone is not evidence of terminal acceptor identity. The later review reports active engineered dimers, so the native requirement for tetramerization remains open.

## Annotation judgments

Both catalytic activities and direct proline-catabolic participation are retained. Generic oxidoreductase activity is refined to both existing specific activities. The active cytoplasmic membrane face is retained as mechanistic inference from peripheral-membrane PutA chemistry, not claimed as a target localization assay. No uptake, growth, stress-response or transcriptional-regulatory activity is manufactured from the fused enzyme. IPR025703 regulatory mappings are marked over-annotated because the characterized type A/B architecture lacks the type C RHH domain; this is not a demonstrated evolutionary loss or a universal negative DNA-binding assay. Proline biosynthesis is a direction/pathway error: sharing P5C/GSAL with a biosynthetic pathway does not mean this enzyme performs its work. No NEW rows were added.

## Research and reproducibility

The required default Falcon request genuinely failed with HTTP403 (authentication/access); no provider report was created. Manual research used the primary papers and full comparative reviews PMID:28712849 and PMID:28990412. QuickGO definitions were retrieved on 2026-11-06: GO:0004657 explicitly names quinone/quinol, GO:0003842 explicitly NAD+/NADH, and GO:0055129 denotes formation of L-proline. Original annotation payloads/order and raw UniProt/GOA files are protected by the pre-edit seed baseline.

PAINT lineage check: `just paint-losses BRADU putA` reported no IRD or IKR loss. The accepted IBA catalytic and catabolic functions are independently supported by target biochemistry; no donor-count argument was used.
