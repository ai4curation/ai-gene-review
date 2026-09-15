---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-08T17:51:15.971728'
end_time: '2026-09-08T17:58:07.924627'
duration_seconds: 411.95
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: DROME
  gene_id: cdm
  gene_symbol: cdm
  uniprot_accession: Q9VEC5
  protein_description: 'RecName: Full=Importin-13 {ECO:0000256|ARBA:ARBA00016020};'
  gene_info: Name=cdm {ECO:0000313|EMBL:AAF55502.1, ECO:0000313|FlyBase:FBgn0261532};
    Synonyms=3R23 {ECO:0000313|EMBL:AAF55502.1}, Cdm {ECO:0000313|EMBL:AAF55502.1},
    CG 7212 {ECO:0000313|EMBL:AAF55502.1}, Dmel\CG7212 {ECO:0000313|EMBL:AAF55502.1},
    Imp13 {ECO:0000313|EMBL:AAF55502.1}, imp13 {ECO:0000313|EMBL:AAF55502.1}, sd-5
    {ECO:0000313|EMBL:AAF55502.1}; ORFNames=CG7212 {ECO:0000313|EMBL:AAF55502.1, ECO:0000313|FlyBase:FBgn0261532},
    Dmel_CG7212 {ECO:0000313|EMBL:AAF55502.1};
  organism_full: Drosophila melanogaster (Fruit fly).
  protein_family: Belongs to the importin beta family.
  protein_domains: ARM-like. (IPR011989); ARM-type_fold. (IPR016024); Exportin-1/Importin-b-like.
    (IPR013598); Importin-beta_N. (IPR001494); Importin_beta-like_NTR. (IPR051345)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 6
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: cdm-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q9VEC5
- **Protein Description:** RecName: Full=Importin-13 {ECO:0000256|ARBA:ARBA00016020};
- **Gene Information:** Name=cdm {ECO:0000313|EMBL:AAF55502.1, ECO:0000313|FlyBase:FBgn0261532}; Synonyms=3R23 {ECO:0000313|EMBL:AAF55502.1}, Cdm {ECO:0000313|EMBL:AAF55502.1}, CG 7212 {ECO:0000313|EMBL:AAF55502.1}, Dmel\CG7212 {ECO:0000313|EMBL:AAF55502.1}, Imp13 {ECO:0000313|EMBL:AAF55502.1}, imp13 {ECO:0000313|EMBL:AAF55502.1}, sd-5 {ECO:0000313|EMBL:AAF55502.1}; ORFNames=CG7212 {ECO:0000313|EMBL:AAF55502.1, ECO:0000313|FlyBase:FBgn0261532}, Dmel_CG7212 {ECO:0000313|EMBL:AAF55502.1};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the importin beta family.
- **Key Domains:** ARM-like. (IPR011989); ARM-type_fold. (IPR016024); Exportin-1/Importin-b-like. (IPR013598); Importin-beta_N. (IPR001494); Importin_beta-like_NTR. (IPR051345)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "cdm" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'cdm' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **cdm** (gene ID: cdm, UniProt: Q9VEC5) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q9VEC5
- **Protein Description:** RecName: Full=Importin-13 {ECO:0000256|ARBA:ARBA00016020};
- **Gene Information:** Name=cdm {ECO:0000313|EMBL:AAF55502.1, ECO:0000313|FlyBase:FBgn0261532}; Synonyms=3R23 {ECO:0000313|EMBL:AAF55502.1}, Cdm {ECO:0000313|EMBL:AAF55502.1}, CG 7212 {ECO:0000313|EMBL:AAF55502.1}, Dmel\CG7212 {ECO:0000313|EMBL:AAF55502.1}, Imp13 {ECO:0000313|EMBL:AAF55502.1}, imp13 {ECO:0000313|EMBL:AAF55502.1}, sd-5 {ECO:0000313|EMBL:AAF55502.1}; ORFNames=CG7212 {ECO:0000313|EMBL:AAF55502.1, ECO:0000313|FlyBase:FBgn0261532}, Dmel_CG7212 {ECO:0000313|EMBL:AAF55502.1};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the importin beta family.
- **Key Domains:** ARM-like. (IPR011989); ARM-type_fold. (IPR016024); Exportin-1/Importin-b-like. (IPR013598); Importin-beta_N. (IPR001494); Importin_beta-like_NTR. (IPR051345)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "cdm" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'cdm' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **cdm** (gene ID: cdm, UniProt: Q9VEC5) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation report: *Drosophila melanogaster cdm/imp13* (Q9VEC5)

## Executive conclusion

The identity check is positive but requires careful nomenclature. The supplied UniProt entry Q9VEC5 corresponds to *Drosophila melanogaster* **CG7212**, called **imp13/Imp13 (Importin-13)** in the principal functional literature; *cdm* is an alias in the supplied record but is not the preferred symbol in that study. Independent mutations in CG7212—including Q351STOP, Q811STOP, and G875D alleles—plus complementation and genomic rescue establish that CG7212 encodes the studied fly Importin-13. The protein has the characteristic importin-β N-terminal domain, consistent with the supplied ARM-like/importin-β-family annotations. This report does not incorporate findings about unrelated genes called *cdm* in other organisms. (giagtzoglou2009importin13regulates pages 3-5)

The most defensible primary annotation is: **an importin-β-family nucleocytoplasmic transport receptor required for normal synaptic physiology and postsynaptic muscle architecture**. At the larval neuromuscular junction (NMJ), Imp13 acts principally in muscle, in or around muscle nuclei, to support muscle/SSR development and a retrograde mechanism that restrains presynaptic neurotransmitter release. Its exact physiologically relevant Drosophila cargoes, cargo selectivity, and Ran-dependent biochemical cycle have not been identified directly. (giagtzoglou2009importin13regulates pages 8-10, giagtzoglou2009importin13regulates pages 5-6, giagtzoglou2009importin13regulates pages 1-2)

## 1. Identity, terminology, and domain consistency

The definitive fly study identified CG7212 as the Drosophila homolog of Importin-13 and named it *imp13*. Causal assignment was unusually strong: multiple independent molecular lesions were found, strong loss-of-function/null alleles were analyzed, and a tagged genomic construct rescued lethality and associated phenotypes. The study also identified the characteristic N-terminal importin-β domain. These results align with Q9VEC5’s classification in the importin-β family and with its Importin-beta_N, importin-beta-like nuclear-transport-receptor, ARM-like, and ARM-type-fold annotations. (giagtzoglou2009importin13regulates pages 5-6, giagtzoglou2009importin13regulates pages 3-5)

Importin-β-family proteins are soluble karyopherins rather than enzymes or membrane transporters. Accordingly, “substrate” here means a macromolecular cargo bound and moved through nuclear pore complexes, not a small molecule converted in a catalytic reaction. The ARM/HEAT-repeat-like architecture is consistent with an extended, conformationally adaptable cargo-binding scaffold, although no structure of fly Q9VEC5 was identified in the retrieved literature.

## 2. Molecular function: established versus inferred

### Directly established in Drosophila

Fly Imp13 is required for regulated synaptic transmission, muscle growth, and formation of the subsynaptic reticulum. Its concentration in or around nuclei and its importin-β-family domain strongly support a nuclear-transport function, but the fly experiments did **not** identify the transported cargo responsible for the synaptic phenotypes. Consequently, annotation as a nucleocytoplasmic transport receptor is well supported by orthology, domain composition, and localization, whereas a specific Drosophila cargo annotation is not. (giagtzoglou2009importin13regulates pages 5-6, giagtzoglou2009importin13regulates pages 3-5, giagtzoglou2009importin13regulates pages 1-2)

### Conserved mechanism inferred from mammalian Importin-13

The foundational mammalian study showed that Importin-13 is unusual because it can mediate transport in both directions. It imports UBC9, the SUMO-conjugating enzyme, and RBM8/Y14-containing complexes, while exporting translation-initiation factor eIF1A. Import cargo binds preferentially under low-RanGTP cytoplasmic conditions and is released by RanGTP in the nucleus; eIF1A export-complex formation involves RanGTP, and cytoplasmic release is additionally coupled to loading of import cargo. These are authoritative biochemical precedents for the protein family, but they are **not direct demonstrations that Q9VEC5 transports the fly orthologs of UBC9, RBM8/Y14, or eIF1A**. (mingot2001importin13a pages 1-2, mingot2001importin13a pages 2-3)

Thus, the likely pathway is the Ran-regulated nuclear-transport cycle, but the exact fly cargo, direction of transport relevant to synapses, and causal downstream nuclear program remain unresolved. Importantly, actin is not established as a Q9VEC5 cargo in the retrieved fly or foundational mammalian studies. It should not be assigned as an Imp13 substrate without direct binding and transport evidence. (giagtzoglou2009importin13regulates pages 8-10, mingot2001importin13a pages 1-2, mingot2001importin13a pages 2-3)

## 3. Cellular and tissue localization

Imp13 is expressed in and around nuclei in both neurons and muscles. In larval brain it is enriched in neurons and occurs in other cells considered likely to include glia. At the larval NMJ, endogenous Imp13 was detected in **muscle nuclei rather than concentrated at the synaptic membrane**, placing the best-supported site of action in the muscle nucleocytoplasmic/perinuclear compartment. (giagtzoglou2009importin13regulates pages 5-6, giagtzoglou2009importin13regulates pages 1-2)

This localization is important mechanistically: the protein is unlikely to be a structural component of the active zone or postsynaptic receptor complex. Instead, it probably regulates nuclear access or export of factors that influence muscle growth, SSR organization, and release of an unidentified retrograde signal. Dynamic passage through nuclear pores was not directly imaged in flies, so this last step remains a family-based inference.

## 4. Neuromuscular-junction function and pathway placement

Loss of *imp13* reduces muscle growth and disrupts thickness and density of the SSR, the elaborate postsynaptic membrane system surrounding motor-neuron boutons. Major presynaptic structural features are comparatively preserved. Muscle-specific Imp13 expression rescues muscle size and SSR abnormalities, establishing a muscle-autonomous developmental or organizational requirement. (giagtzoglou2009importin13regulates pages 5-6, giagtzoglou2009importin13regulates pages 1-2)

The physiological phenotype is nevertheless presynaptic: *imp13* mutants exhibit increased neurotransmitter-release probability and quantal content. Muscle-specific rescue corrects the excessive release and paired-pulse-depression phenotypes, whereas neuronal rescue does not. The parsimonious model is therefore:

**muscle-nuclear Imp13-dependent transport → postsynaptic transcriptional/biochemical state and SSR organization → unidentified retrograde signal → restraint of presynaptic vesicle release.** (giagtzoglou2009importin13regulates pages 8-10)

This places Imp13 in synaptic homeostasis or trans-synaptic regulation rather than directly in the synaptic-vesicle fusion machinery. The identity of the retrograde signal and the transported cargo upstream of it remain unknown.

## 5. Electrophysiological and quantitative evidence

At low extracellular Ca²⁺, mutants have increased evoked release and quantal content, together with stronger paired-pulse depression, consistent with higher initial release probability. Differences were observed at 0.35–0.5 mM extracellular Ca²⁺, whereas at 2 mM Ca²⁺ EJP amplitudes were similar among genotypes, plausibly because release approaches saturation at the higher concentration. Ca²⁺ cooperativity was not detectably altered. (giagtzoglou2009importin13regulates pages 8-10)

Several controls narrow the mechanism. Miniature EJP amplitude and frequency were normal, cumulative miniature-amplitude distributions were unchanged, and GluRIIA/GluRIIB receptor abundance was not altered. Therefore, neither quantal size nor a gross change in postsynaptic glutamate-receptor content explains the increased evoked response. Bruchpilot-positive active-zone abundance was also not increased. Resting presynaptic bouton Ca²⁺ was modestly elevated and may contribute to enhanced release, although the evidence does not prove it is the initiating consequence of muscle Imp13 loss. (giagtzoglou2009importin13regulates pages 8-10, giagtzoglou2009importin13regulates pages 5-6, giagtzoglou2009importin13regulates pages 10-11)

## 6. Visual-system function

Photoreceptor-restricted *imp13* loss causes absent electroretinogram ON/OFF transients and severely reduced photoreceptor responses. Restricting the defect to photoreceptors reproduces the phenotype seen when both pre- and postsynaptic visual neurons are mutant, supporting a presynaptic requirement in this tissue. Photoreceptor development, R7/R8 targeting, synaptic-cartridge formation, and total synapse number are broadly normal, although capitate projections are shallower. Thus, the visual phenotype primarily reflects defective phototransduction/transmission rather than gross failure of neuronal development. (giagtzoglou2009importin13regulates pages 3-5, giagtzoglou2009importin13regulates pages 3-3)

The contrast between a presynaptic photoreceptor requirement and a postsynaptic muscle requirement at the NMJ indicates that Imp13’s cellular role is context dependent. This is compatible with tissue-specific cargo availability or different nuclear programs, but neither explanation has yet been tested directly.

## 7. Recent developments, 2023–2024

No 2023–2024 primary study directly re-characterizing Drosophila CG7212/Imp13 was identified in the searches. The major recent development is therefore cross-species. Bin and colleagues reported in *Nature Communications* in May 2024 that zebrafish Importin-13b is selectively required for growth of Mauthner-axon diameter. Loss reduced neurofilament number and spacing and slowed conduction in proportion to diameter, without reducing axonal length, neuronal soma size, firing precision, or high-frequency firing. Normal Mauthner axons expanded from approximately 1.0 μm at two days post-fertilization to approximately 3.5 μm at five days. These findings reinforce a conserved connection between Importin-13-family proteins and neuronal morphology/physiology, but they do not establish an axon-caliber function for fly Q9VEC5. (bin2024importin13dependentaxon pages 1-3)

The current expert interpretation should therefore remain conservative: recent vertebrate work broadens the plausible neuronal functions of Importin-13, while the direct Drosophila annotation still rests chiefly on the rigorous 2009 genetic, ultrastructural, localization, and electrophysiological study.

## 8. Applications and real-world implementation

For current research practice, Q9VEC5 is most useful as a genetically tractable model for linking nuclear transport to trans-synaptic homeostasis. Tissue-specific rescue allows investigators to distinguish neuronal from muscle requirements, while larval NMJ electrophysiology provides sensitive readouts of release probability, quantal content, and retrograde signaling. Photoreceptor electroretinography provides a second, mechanistically distinct neuronal assay. These are experimental applications rather than clinical implementations; no therapeutic or commercial implementation specific to Drosophila Q9VEC5 was identified.

The most informative next experiments would be muscle-specific Imp13 interactomics under native expression, compartment-resolved proteomics, direct cargo-binding and nuclear-transport assays, and rescue with cargo-binding- or Ran-interaction-defective Imp13 variants. Candidate cargoes suggested by mammalian work should be tested rather than assumed.

## Evidence and confidence summary

| Claim/topic | Direct Drosophila evidence | Key observation | Interpretation | Confidence/limitation |
|---|---|---|---|---|
| Gene identity | **Yes** | Genetic mapping, independent mutant lesions—including Q351STOP, Q811STOP, and G875D—and genomic rescue identify **CG7212** as *Drosophila melanogaster* **imp13/Importin-13**, corresponding to the supplied Q9VEC5/*cdm* record. (giagtzoglou2009importin13regulates pages 3-5) | Q9VEC5 should be annotated primarily as fly CG7212/Imp13; *cdm* is an alias and must not be conflated with similarly named genes. | **High.** Identity is supported by genetics and rescue. The principal paper uses *imp13*, not *cdm*. |
| Protein family and domain | **Yes; no fly structure reported** | Fly Imp13 contains the characteristic N-terminal importin-β domain and was identified as the fly homolog of Importin-13. (giagtzoglou2009importin13regulates pages 3-5, giagtzoglou2009importin13regulates pages 1-2) | Consistent with the supplied ARM-like/importin-β-family annotations and a role as a karyopherin-type nucleocytoplasmic transport receptor. | **High for family; moderate for mechanistic detail.** Domain homology does not identify fly cargoes or transport direction. |
| Cellular localization | **Yes** | Imp13 is expressed in and around nuclei of neurons and muscles. In larval brain it is enriched in neurons and present in additional cells, probably glia. At the larval NMJ, endogenous protein was detected in muscle nuclei rather than concentrated at the synapse. (giagtzoglou2009importin13regulates pages 5-6, giagtzoglou2009importin13regulates pages 1-2) | The best-supported site of action is the nucleocytoplasmic or perinuclear compartment, especially muscle nuclei at the NMJ. | **High for observed localization.** The glial assignment is tentative, and dynamic nuclear-pore shuttling was not directly measured in flies. |
| NMJ postsynaptic muscle action and retrograde control | **Yes** | Muscle-specific Imp13 expression rescues mutant release and paired-pulse-depression phenotypes, whereas neuronal expression does not. Loss of muscle Imp13 increases presynaptic release probability and quantal content. (giagtzoglou2009importin13regulates pages 8-10) | Imp13 acts postsynaptically in muscle to control a retrograde process that restrains presynaptic neurotransmitter release. | **High for tissue requirement and physiological direction; moderate for pathway mechanism.** The retrograde signal and relevant cargo remain unknown. |
| Muscle growth and subsynaptic reticulum morphology | **Yes** | Mutants have reduced muscle growth and abnormal subsynaptic-reticulum thickness and density, while major presynaptic structural features are preserved. Muscle-specific expression rescues these defects. (giagtzoglou2009importin13regulates pages 5-6, giagtzoglou2009importin13regulates pages 1-2) | Imp13 has a muscle-autonomous role in postsynaptic growth and organization of the SSR, the specialized postsynaptic membrane system. | **High.** The transported molecule linking nuclear transport to SSR architecture was not identified. |
| NMJ electrophysiology | **Yes** | Under low extracellular Ca²⁺, mutants show increased evoked-release probability and quantal content, stronger paired-pulse depression, and modestly elevated resting bouton Ca²⁺. At 2 mM Ca²⁺, EJP amplitude is similar among genotypes, whereas differences appear at 0.35–0.5 mM Ca²⁺. mEJP amplitude and frequency, glutamate-receptor abundance, and Ca²⁺ cooperativity are unchanged. Brp-positive active-zone number is not increased. (giagtzoglou2009importin13regulates pages 8-10, giagtzoglou2009importin13regulates pages 5-6, giagtzoglou2009importin13regulates pages 10-11) | Imp13 normally restrains presynaptic vesicle release without altering quantal size or postsynaptic receptor abundance; the phenotype is strongest when release is not saturated by high Ca²⁺. | **High for phenotype; moderate for mechanism.** Elevated bouton Ca²⁺ may contribute but does not establish the causal retrograde pathway. |
| Visual-system role | **Yes** | Photoreceptor-restricted loss reproduces absent ON/OFF electroretinogram transients and severely reduced photoreceptor responses. Axonal targeting and synapse number are broadly normal, although capitate projections are shallower. (giagtzoglou2009importin13regulates pages 3-5, giagtzoglou2009importin13regulates pages 3-3) | Imp13 is required presynaptically in photoreceptors for normal phototransduction and visual transmission, rather than principally for photoreceptor development or synapse formation. | **High for functional requirement; moderate for mechanism.** This presynaptic requirement differs from the postsynaptic muscle requirement at the NMJ. |
| Fly cargo specificity | **No specific cargo directly established** | The definitive fly study demonstrates physiological and localization phenotypes but does not identify a protein imported or exported by CG7212/Imp13. (giagtzoglou2009importin13regulates pages 8-10, giagtzoglou2009importin13regulates pages 3-5, giagtzoglou2009importin13regulates pages 1-2) | Q9VEC5 is best described as a probable bidirectional nuclear-transport receptor whose biologically decisive fly cargoes remain unknown. | **High confidence that the cited fly evidence does not define cargo specificity.** Mammalian cargo assignments should not be transferred directly to flies. |
| Mammalian cargo precedent | **No; cross-species evidence only** | Mammalian Importin-13 imports UBC9 and RBM8/Y14 and exports eIF1A. (mingot2001importin13a pages 1-2, mingot2001importin13a pages 2-3) | These findings illustrate the receptor family’s ability to transport distinct folded cargoes in opposite directions and provide hypotheses for fly studies. | **Moderate as evolutionary inference; not direct Q9VEC5 annotation.** Orthology does not prove that fly Imp13 transports the same cargoes. |
| Ran-dependent transport mechanism | **Not directly demonstrated for fly Q9VEC5** | In mammalian systems, import cargo binds Importin-13 under low-RanGTP cytoplasmic conditions and is released by nuclear RanGTP. Stable eIF1A export-complex formation involves RanGTP, with cytoplasmic release additionally promoted by import-cargo loading. (mingot2001importin13a pages 1-2, mingot2001importin13a pages 2-3) | Q9VEC5 probably participates in the canonical Ran-gradient-driven karyopherin cycle, but its exact fly transport cycle has not been biochemically tested. | **High for mammalian Importin-13; moderate for fly inference.** This mechanism is inferred rather than experimentally established in *Drosophila*. |
| Recent 2024 neuronal context | **No; zebrafish evidence only** | A 2024 zebrafish study found that *ipo13b* loss selectively reduces Mauthner-axon diameter, neurofilament number and spacing, and conduction speed without reducing axonal length or cell-body size. Normal Mauthner diameter increased from about 1.0 μm at 2 dpf to about 3.5 μm at 5 dpf. (bin2024importin13dependentaxon pages 1-3) | This supports a conserved neuronal-growth role for Importin-13-family proteins but does not demonstrate an axon-caliber function for fly Q9VEC5. | **High for zebrafish; low-to-moderate for fly extrapolation.** No 2023–2024 direct re-characterization of fly CG7212/Imp13 was identified. |
| Actin cargo status | **No** | The direct fly Imp13 study does not identify actin as cargo, and the foundational mammalian study reports other cargoes rather than actin. (giagtzoglou2009importin13regulates pages 8-10, giagtzoglou2009importin13regulates pages 5-6, mingot2001importin13a pages 1-2, mingot2001importin13a pages 2-3) | Actin should **not** be annotated as a demonstrated Q9VEC5/Imp13 substrate on the available evidence. | **High for absence of support in the cited studies.** Evidence involving other actin importins cannot be reassigned to Imp13 without direct validation. |


*Table: This table distinguishes direct Drosophila findings for CG7212/Imp13 from mammalian mechanistic inference and recent zebrafish context. It highlights strong genetic and physiological evidence while identifying unresolved cargo specificity and transport mechanisms.*

## Overall annotation recommendation

**Recommended primary function:** Importin-β-family nucleocytoplasmic transport receptor, probably operating through the Ran gradient and capable in principle of bidirectional cargo transport.

**Best-supported biological role in Drosophila:** In larval muscle nuclei, Imp13 supports muscle growth and SSR architecture and enables a retrograde homeostatic pathway that limits presynaptic neurotransmitter release. It is also required presynaptically for normal photoreceptor function and visual transmission. (giagtzoglou2009importin13regulates pages 8-10, giagtzoglou2009importin13regulates pages 5-6, giagtzoglou2009importin13regulates pages 3-5)

**Localization:** Nuclear/perinuclear in neurons and muscles; directly observed in muscle nuclei at the NMJ rather than as a synapse-enriched structural protein. (giagtzoglou2009importin13regulates pages 5-6, giagtzoglou2009importin13regulates pages 1-2)

**Cargo/substrate specificity:** Unknown for Q9VEC5. Mammalian UBC9 and RBM8/Y14 import and eIF1A export are useful hypotheses, not validated fly cargo assignments. Actin is not a demonstrated cargo. (mingot2001importin13a pages 1-2, mingot2001importin13a pages 2-3)

## Key sources

1. Giagtzoglou N, Lin YQ, Haueter C, Bellen HJ. “Importin 13 Regulates Neurotransmitter Release at the Drosophila Neuromuscular Junction.” *Journal of Neuroscience*. Published April 2009; 29:5628–5639. https://doi.org/10.1523/JNEUROSCI.0794-09.2009. (giagtzoglou2009importin13regulates pages 8-10, giagtzoglou2009importin13regulates pages 3-5)
2. Mingot J-M, Kostka S, Kraft R, Hartmann E, Görlich D. “Importin 13: a novel mediator of nuclear import and export.” *EMBO Journal*. Published July 2001; 20:3685–3694. https://doi.org/10.1093/emboj/20.14.3685. (mingot2001importin13a pages 1-2, mingot2001importin13a pages 2-3)
3. Bin JM et al. “Importin 13-dependent axon diameter growth regulates conduction speeds along myelinated CNS axons.” *Nature Communications*. Published May 2024. Retrieved record URL: https://doi.org/10.1101/2023.05.19.541431. This source concerns zebrafish, not Drosophila. (bin2024importin13dependentaxon pages 1-3)

References

1. (giagtzoglou2009importin13regulates pages 3-5): Nikolaos Giagtzoglou, Yong Qi Lin, Claire Haueter, and Hugo J. Bellen. Importin 13 regulates neurotransmitter release at the drosophila neuromuscular junction. The Journal of Neuroscience, 29:5628-5639, Apr 2009. URL: https://doi.org/10.1523/jneurosci.0794-09.2009, doi:10.1523/jneurosci.0794-09.2009. This article has 31 citations.

2. (giagtzoglou2009importin13regulates pages 8-10): Nikolaos Giagtzoglou, Yong Qi Lin, Claire Haueter, and Hugo J. Bellen. Importin 13 regulates neurotransmitter release at the drosophila neuromuscular junction. The Journal of Neuroscience, 29:5628-5639, Apr 2009. URL: https://doi.org/10.1523/jneurosci.0794-09.2009, doi:10.1523/jneurosci.0794-09.2009. This article has 31 citations.

3. (giagtzoglou2009importin13regulates pages 5-6): Nikolaos Giagtzoglou, Yong Qi Lin, Claire Haueter, and Hugo J. Bellen. Importin 13 regulates neurotransmitter release at the drosophila neuromuscular junction. The Journal of Neuroscience, 29:5628-5639, Apr 2009. URL: https://doi.org/10.1523/jneurosci.0794-09.2009, doi:10.1523/jneurosci.0794-09.2009. This article has 31 citations.

4. (giagtzoglou2009importin13regulates pages 1-2): Nikolaos Giagtzoglou, Yong Qi Lin, Claire Haueter, and Hugo J. Bellen. Importin 13 regulates neurotransmitter release at the drosophila neuromuscular junction. The Journal of Neuroscience, 29:5628-5639, Apr 2009. URL: https://doi.org/10.1523/jneurosci.0794-09.2009, doi:10.1523/jneurosci.0794-09.2009. This article has 31 citations.

5. (mingot2001importin13a pages 1-2): J. Mingot, S. Kostka, R. Kraft, E. Hartmann, and D. Görlich. Importin 13: a novel mediator of nuclear import and export. The EMBO Journal, 20:3685-3694, Jul 2001. URL: https://doi.org/10.1093/emboj/20.14.3685, doi:10.1093/emboj/20.14.3685. This article has 291 citations.

6. (mingot2001importin13a pages 2-3): J. Mingot, S. Kostka, R. Kraft, E. Hartmann, and D. Görlich. Importin 13: a novel mediator of nuclear import and export. The EMBO Journal, 20:3685-3694, Jul 2001. URL: https://doi.org/10.1093/emboj/20.14.3685, doi:10.1093/emboj/20.14.3685. This article has 291 citations.

7. (giagtzoglou2009importin13regulates pages 10-11): Nikolaos Giagtzoglou, Yong Qi Lin, Claire Haueter, and Hugo J. Bellen. Importin 13 regulates neurotransmitter release at the drosophila neuromuscular junction. The Journal of Neuroscience, 29:5628-5639, Apr 2009. URL: https://doi.org/10.1523/jneurosci.0794-09.2009, doi:10.1523/jneurosci.0794-09.2009. This article has 31 citations.

8. (giagtzoglou2009importin13regulates pages 3-3): Nikolaos Giagtzoglou, Yong Qi Lin, Claire Haueter, and Hugo J. Bellen. Importin 13 regulates neurotransmitter release at the drosophila neuromuscular junction. The Journal of Neuroscience, 29:5628-5639, Apr 2009. URL: https://doi.org/10.1523/jneurosci.0794-09.2009, doi:10.1523/jneurosci.0794-09.2009. This article has 31 citations.

9. (bin2024importin13dependentaxon pages 1-3): Jenea M Bin, Daumante Suminaite, Silvia K. Benito-Kwiecinski, Linde Kegel, Maria Rubio-Brotons, Jason J Early, Daniel Soong, Matthew R Livesey, Richard J Poole, and David A Lyons. Importin 13-dependent axon diameter growth regulates conduction speeds along myelinated cns axons. Nature Communications, May 2024. URL: https://doi.org/10.1101/2023.05.19.541431, doi:10.1101/2023.05.19.541431. This article has 30 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](cdm-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. https://doi.org/10.1523/JNEUROSCI.0794-09.2009.
2. https://doi.org/10.1093/emboj/20.14.3685.
3. https://doi.org/10.1101/2023.05.19.541431.
4. https://doi.org/10.1523/jneurosci.0794-09.2009,
5. https://doi.org/10.1093/emboj/20.14.3685,
6. https://doi.org/10.1101/2023.05.19.541431,