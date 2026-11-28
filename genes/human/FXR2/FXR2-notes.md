# FXR2 curation notes

## Evidence synthesis

- `just fetch-gene human FXR2` returned 171 GOA rows; the GOA file is not header-only.
- Direct human FXR2 biology is much thinner than FXR1 and FMR1. PMID:7489725 cloned FXR2, showed that it has KH domains, can bind RNA and can form homomers and heteromers with FMR1 and FXR1. PMID:9259278 observed FXR2 in the cytoplasm of differentiated human neurons.
- The stress-granule IDA row cites PMID:12417522, whose visible abstract describes FMRP-containing granules and does not mention FXR2. Because the cached record lacks full text, the FXR2 stress-granule rows were kept `UNDECIDED` rather than removed as a wrong-gene row.
- PMID:32706158 directly examined all three FXR-family proteins in human cells and showed that FXR2, like FXR1 and FMRP, can localize to the nuclear envelope and that depletion of FXR2 can promote cytoplasmic Nup granules. A conservative `NEW` nuclear-envelope row captures the direct localization result.
- Mouse Fxr2 supports dentate-gyrus and NOG mRNA-stability contexts through curated UniProt similarity. These were kept as non-core or inherited rows, not treated as direct human FXR2 experiments.
- Bare `GO:0005515` protein-binding rows were removed under `src/ai_gene_review/validation/protein_binding_policy.py`, while the more specific FXR2 self-association rows were modified to homodimerization.

## PAINT

- FXR2 inherits the PTHR10603 family-root rows for mRNA binding, mRNA stability, positive regulation of translation and animal organ development. Those rows are plausible as broad FMR/FXR-family properties but rely mostly on FMR1/FXR1/model-organism evidence.
- The FXR2 stress-granule IBA includes UniProtKB:P51116 as a seed; because that direct seed could not be verified from the visible PMID:12417522 abstract, the family node and FXR2 rows remain unresolved rather than accepted.
- The Bilateria positive long-term-plasticity and presynaptic-translation rows should be kept as non-core inherited neuronal contexts. Their local PAINT rows each have one rat Fmr1 seed, but a single curated seed is not weak by count.
- The `GO_REF:0000108` `GO:0098793 presynapse` row is a logical cellular-component assertion derived from `GO:0099577 regulation of translation at presynapse, modulating synaptic transmission`. Keep `GO:0098793` with the same non-core status as the PAINT presynaptic-translation row.
