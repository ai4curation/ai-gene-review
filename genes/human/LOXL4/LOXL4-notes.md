# LOXL4 review notes

## Research provenance

- Falcon deep research timed out after 600 seconds.
- The Perplexity fallback failed with HTTP 401 (insufficient quota).
- No provider deep-research artifact was created. Literature assessment below is manual and based on the cached primary publications and the reviewed UniProt Q96JB6 text export.

## Direct human biochemical evidence

- Recombinant human LOXL4 expressed in *E. coli* and refolded by stepwise dialysis showed BAPN-inhibitable amine-oxidase activity against benzylamine: [PMID:14551188, "The purified LOXL4 proteins showed beta-aminopropionitrile-inhibitable activity of 0.022-0.032 units/mg toward a nonpeptidyl substrate, benzylamine."] This is direct evidence for enzymatic activity, but the cached paper is abstract-only and does **not** directly show oxidation of collagen, elastin, or protein lysine, copper dependence, extracellular catalysis, or BMP1-dependent activation.
- The paper identifies four SRCR domains and conserved LOX-family catalytic features: [PMID:14551188, "LOXL4 contains four scavenger receptor cysteine-rich domains in addition to the characteristic domains of the LOX family, including the copper-binding domain, the cytokine receptor-like domain, and the residues of the lysyl-tyrosyl quinone cofactor."] Presence of these motifs supports family assignment but should not replace substrate-specific assays.

## Human sequence, secretion, and expression evidence

- Human LOXL4 was cloned as a 756-aa protein with a 24-aa signal peptide, a C-terminal LO domain, and four N-terminal SRCR-like domains: [PMID:11691589, "The predicted polypeptide is 756 amino acids long, including a 24-residue signal peptide. The C-terminal region contains a LO domain similar to those of LOX, LOXL, LOXL2 and LOXL3. The N-terminal region has four subregions similar to scavenger receptor cysteine-rich domains that are highly conserved with LOXL2 and LOXL3."]
- In HT-1080 cells, recombinant human LOXL4 was secreted with no evident proteolytic processing: [PMID:11691589, "Recombinant LOXL4 expressed in HT-1080 cells was secreted into the culture medium with no evident proteolytic processing."] This directly supports secretion and is important negative evidence against describing a demonstrated LOXL4 propeptide-removal mechanism.
- Independent human cloning work identified the conserved copper-binding and LTQ-forming residues and a distinctive insertion in one SRCR domain: [PMID:11691588, "The cDNA and derived amino acid sequence of LOXL4 demonstrates a conserved C-terminal region including the characteristic copper-binding site, lysyl and tyrosyl residues and a cytokine receptor-like domain. One of the four N-terminal SRCR domains contains a 13 amino acid insertion encoded by a short exon not present within the closely homologous LOXL2 and LOXL3 genes."] This is structural prediction from sequence, not an activity assay.
- Human transcript expression was detected in pancreas, testis, fibroblasts, smooth muscle cells, and HOS osteosarcoma cells: [PMID:11691588, "The 3.5-kb LOXL4 mRNA is present in pancreas and testis and at lower levels in several other tissues. Fibroblasts, smooth muscle and osteosarcoma (HOS) cells express LOXL4."] The other cloning paper reported broad expression with highest tested levels in skeletal muscle, testis, and pancreas [PMID:11691589, "The LOXL4 mRNA is approximately 4 kb in size and is expressed in many tissues, the highest levels among the tissues studied being in the skeletal muscle, testis and pancreas."]

## Model-organism and substrate boundaries

- Mouse LOXC (the murine LOXL4 ortholog) showed BAPN-sensitive lysyl-oxidase activity toward chick type I and II collagen in conditioned medium: [PMID:11292829, "The conditioned media of COS-7 cells transfected with the full-length LOXC cDNA showed the lysyl oxidase activity in both type I and type II collagens derived from chick embryos, and these activities of LOXC were inhibited by beta-aminopropionitrile, a specific inhibitor of lysyl oxidase."] This supports conserved collagen-substrate plausibility but is not direct human LOXL4 evidence.
- Mouse LOXC expression increased with chondrogenic differentiation and localized to hypertrophic/calcified growth-plate chondrocytes [PMID:11292829, "In vivo, LOXC gene expression was localized in hypertrophic and calcified chondrocytes of growth plates in adult mice."] Cartilage and growth-plate roles therefore need an explicit model-organism boundary when discussed for human LOXL4.

## Processing and isoform boundaries

- The reviewed UniProt Q96JB6 record annotates signal peptide 1-24 and mature chain 25-756, but no `PROPEP` feature and no `ALTERNATIVE PRODUCTS` section. Accordingly, there are no named reviewed LOXL4 isoforms in this source, and predicted RefSeq/Ensembl alternatives should not be presented as experimentally established isoforms.
- UniProt states that LOXL4 "may be proteolytically cleaved by BMP1" and tags this as inferred. The cached PMID:14551188 abstract does not establish BMP1 cleavage, while PMID:11691589 explicitly reports secretion with no evident processing. Do not describe BMP1 cleavage, propeptide removal, or cleavage-dependent activation as demonstrated LOXL4 biology.

## High-throughput annotation sources

- The interaction papers underlying protein-binding GOA rows are broad Y2H/AP-MS interactome maps. None of the cached searchable article texts names LOXL4 or its reported partner pair. GOA/IntAct provides the pair-level provenance, but these hits do not by themselves establish a physiological interaction, stable complex, or extracellular function.
- PMID:19199708 is a human parotid-exosome proteomic catalog. LOXL4 is not named in the cached searchable article text; the GOA row is dataset-level detection, not evidence that exosome residence is a general or core LOXL4 localization.
- PMID:23382219 studies PX-FERM endosomal cargo recognition and does not mention LOXL4 in the cached full text. The MGI-derived signaling-receptor-complex annotation should not be treated as direct human LOXL4 evidence without identifying the assayed organism/product and experiment in the source data.
- PMID:23962539 is a review of elastic fibers and does not mention LOXL4 in its cached abstract. It is contextual rather than primary evidence for LOXL4 localization to elastic fibers.
