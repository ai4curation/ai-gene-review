# CTPS2 manual notes

`just deep-research-falcon human CTPS2 --fallback perplexity-lite` failed in this checkout: Falcon and Perplexity were unavailable, and only the `claude_code` provider was configured. I reviewed the fetched UniProt and GOA records, the existing human CTPS1 review, the PTHR11550 family review, the de novo pyrimidine synthesis module, the CTPS1 source notes on BioPlex/HuRI/OpenCell/U2OS records, and the cached CTPS2 publications manually.

## Core chemistry and PAINT

CTPS2 is the vertebrate CTPS2 paralog in PTHR11550 and retains the canonical CTP synthase reaction: ATP-dependent amination of UTP to CTP with glutamine as the nitrogen donor. The PTHR11550 root PAINT node PTN000167473 is accepted for `GO:0003883` and `GO:0006241` in the family review, and both CTPS1 and CTPS2 seed that node. The same root has an older `GO:0019856` pyrimidine nucleobase biosynthesis assertion that the family review already flags for removal because CTP synthase converts UTP to the nucleotide CTP rather than making a free pyrimidine nucleobase.

## Homomerization, cytoophidia, and paralog binding

CTPS2 is a homotetrameric enzyme that can polymerize into filaments of stacked tetramers. The CTPS2 cryo-EM paper shows active substrate-bound and inactive product-bound CTPS2 filaments, with conserved intertetramer contacts and H355 required for S-state and P-state polymerization. This supports `GO:0042802` identical protein binding and `GO:0097268` cytoophidium, but neither should be a separate core molecular function beside CTP synthase activity.

PMID:34583994 adds a 2.8-A CTP-bound CTPS2 structure, a second inhibitory CTP site overlapping the ATP site, direct CTPS1-vs-CTPS2 inhibition and activity comparisons, and mouse CTPS2 structures for the R80 inhibitor pocket. Its CTPS1 C-terminal truncation/H355A construct does not make a simple C-terminal tail-swap model sufficient; it points instead to subtler isoform-specific inhibitor and product-bound-state differences. PMID:20739275 was added as an abstract-only cache because UniProt cites it for CTPS2 kinetic values, GTP allostery and CK1-mediated phosphorylation of S568.

Several CTPS2 GOA rows are bare `GO:0005515` protein binding rows. The CTPS1-partner rows can be narrowed to `GO:0019899` enzyme binding, following the CTPS1 review's treatment of the reciprocal edge. The SPG21 rows remain only bare protein-binding evidence and are removed as uninformative.

## Locations and downstream context

UniProt curates CTPS2 as cytosolic and nuclear, with filamentous cytoophidia in both compartments. CTPS2 lacks a mitochondrial targeting annotation, but the single high-throughput MitoCoP mitochondrion row comes from a direct HTP organelle-proteomics assay; following the ORGANELLES policy and the DTYMK/ATP7B precedents, it is kept as non-core rather than overruled without the target supplement.
