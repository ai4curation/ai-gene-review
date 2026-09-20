# vas2: original ProtNLM2 function paragraph

Source: [preserved XML](vas2-protnlm-source.xml), pre-release `post-processed-2026_02_28k.xml`. The source paragraph is reproduced verbatim. Current sequence and taxonomy are identity checks, not proven prediction-time input.

> Component of the adaptor complexes which link clathrin to receptors in coated vesicles. Clathrin-associated protein complexes are believed to interact with the cytoplasmic tails of membrane proteins, leading to their selection and concentration.

## Atomic claim assessments

### Claim 1: Component of the adaptor complexes

Assessment: **CNN** (score 2). Target pull-downs and subunit deletions establish Aps1 as the sigma subunit of AP-1. The generic plural describes the adaptor-complex class; it is supported for AP-1 and does not establish membership of Vas2 in AP-2 or AP-3.

- [PMID:19624755](https://pubmed.ncbi.nlm.nih.gov/19624755/): "In pull-down assay, Apm1 binds Apl2 even in the absence of Aps1 and Apl4, and Apl4 binds Aps1 even in the absence of Apm1 and Apl2. Consistently, the deletion of any subunit generally caused the disassociation of the heterotetrameric complex from endosomes, although some subunits weakly localized to endosomes. In addition, the deletion of individual subunits caused similar endosomal accumulation of v-SNARE synaptobrevin Syb1. Altogether, results suggest that the four subunits are all essential for the heterotetrameric complex formation and for the AP-1 function in exit transport from endosomes."
### Claim 2: which link clathrin to receptors in coated vesicles.

Assessment: **CNN** (score 2). AP-1 is a conserved clathrin-associated cargo adaptor, and its gamma/sigma hemicomplex recognizes cargo sorting motifs. Target Apl4-Aps1 interaction and endosomal traffic defects establish the corresponding adaptor architecture. The linkage is executed by the assembled complex, not by isolated Vas2 simultaneously supplying all cargo and clathrin contacts.

- [PMID:19624755](https://pubmed.ncbi.nlm.nih.gov/19624755/): "In pull-down assay, Apm1 binds Apl2 even in the absence of Aps1 and Apl4, and Apl4 binds Aps1 even in the absence of Apm1 and Apl2. Consistently, the deletion of any subunit generally caused the disassociation of the heterotetrameric complex from endosomes, although some subunits weakly localized to endosomes. In addition, the deletion of individual subunits caused similar endosomal accumulation of v-SNARE synaptobrevin Syb1. Altogether, results suggest that the four subunits are all essential for the heterotetrameric complex formation and for the AP-1 function in exit transport from endosomes."
- [PMID:17360967](https://pubmed.ncbi.nlm.nih.gov/17360967/): "We report that the gamma/sigma1 or alpha/sigma2 hemicomplexes bound the dileucine-based motifs of several proteins quite strongly, whereas binding by the beta1/mu1 and beta2/mu2 hemicomplexes, and the individual beta or mu subunits, was extremely weak or undetectable."
### Claim 3: Clathrin-associated protein complexes are believed to interact with the cytoplasmic tails of membrane proteins, leading to their selection and concentration.

Assessment: **CNN** (score 2). Mammalian AP-1 gamma/sigma pull-downs establish recognition of cytosolic dileucine cargo motifs. The sigma-specific target family assignment, Apl4-Aps1 association, and Syb1 sorting phenotype support transfer of the shared cargo-selection mechanism. Exact motif preferences or receptor identities in fission yeast are not inferred from mammalian isoform preferences. This complex-level cargo sorting mechanism is already represented by curated clathrin-cargo adaptor and transport annotations.

- [PMID:17360967](https://pubmed.ncbi.nlm.nih.gov/17360967/): "We report that the gamma/sigma1 or alpha/sigma2 hemicomplexes bound the dileucine-based motifs of several proteins quite strongly, whereas binding by the beta1/mu1 and beta2/mu2 hemicomplexes, and the individual beta or mu subunits, was extremely weak or undetectable."
- [PMID:19624755](https://pubmed.ncbi.nlm.nih.gov/19624755/): "In pull-down assay, Apm1 binds Apl2 even in the absence of Aps1 and Apl4, and Apl4 binds Aps1 even in the absence of Apm1 and Apl2. Consistently, the deletion of any subunit generally caused the disassociation of the heterotetrameric complex from endosomes, although some subunits weakly localized to endosomes. In addition, the deletion of individual subunits caused similar endosomal accumulation of v-SNARE synaptobrevin Syb1. Altogether, results suggest that the four subunits are all essential for the heterotetrameric complex formation and for the AP-1 function in exit transport from endosomes."

These are prose-claim assessments; no GO mappings were invented for the paragraph. CNN denotes established equivalent biology, including justified conserved-family inference, and makes no assertion about training-data membership.
