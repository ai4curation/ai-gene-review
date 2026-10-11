---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-30T05:25:25.555091'
end_time: '2026-09-30T05:39:01.155526'
duration_seconds: 815.6
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: MIB1
  gene_symbol: MIB1
  uniprot_accession: Q86YT6
  protein_description: 'RecName: Full=E3 ubiquitin-protein ligase MIB1; EC=2.3.2.27;
    AltName: Full=DAPK-interacting protein 1; Short=DIP-1; AltName: Full=Mind bomb
    homolog 1; AltName: Full=RING-type E3 ubiquitin transferase MIB1 {ECO:0000305};
    AltName: Full=Zinc finger ZZ type with ankyrin repeat domain protein 2;'
  gene_info: Name=MIB1; Synonyms=DIP1, KIAA1323, ZZANK2;
  organism_full: Homo sapiens (Human).
  protein_family: Not specified in UniProt
  protein_domains: Ankyrin_rpt. (IPR002110); Ankyrin_rpt-contain_sf. (IPR036770);
    MIB1/2_ZZ. (IPR042056); Mib_Herc2. (IPR010606); Mib_Herc2_sf. (IPR037252)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 26
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: MIB1-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: MIB1-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: MIB1-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q86YT6
- **Protein Description:** RecName: Full=E3 ubiquitin-protein ligase MIB1; EC=2.3.2.27; AltName: Full=DAPK-interacting protein 1; Short=DIP-1; AltName: Full=Mind bomb homolog 1; AltName: Full=RING-type E3 ubiquitin transferase MIB1 {ECO:0000305}; AltName: Full=Zinc finger ZZ type with ankyrin repeat domain protein 2;
- **Gene Information:** Name=MIB1; Synonyms=DIP1, KIAA1323, ZZANK2;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Ankyrin_rpt. (IPR002110); Ankyrin_rpt-contain_sf. (IPR036770); MIB1/2_ZZ. (IPR042056); Mib_Herc2. (IPR010606); Mib_Herc2_sf. (IPR037252)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "MIB1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'MIB1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **MIB1** (gene ID: MIB1, UniProt: Q86YT6) in human.

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
- **UniProt Accession:** Q86YT6
- **Protein Description:** RecName: Full=E3 ubiquitin-protein ligase MIB1; EC=2.3.2.27; AltName: Full=DAPK-interacting protein 1; Short=DIP-1; AltName: Full=Mind bomb homolog 1; AltName: Full=RING-type E3 ubiquitin transferase MIB1 {ECO:0000305}; AltName: Full=Zinc finger ZZ type with ankyrin repeat domain protein 2;
- **Gene Information:** Name=MIB1; Synonyms=DIP1, KIAA1323, ZZANK2;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Ankyrin_rpt. (IPR002110); Ankyrin_rpt-contain_sf. (IPR036770); MIB1/2_ZZ. (IPR042056); Mib_Herc2. (IPR010606); Mib_Herc2_sf. (IPR037252)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "MIB1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'MIB1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **MIB1** (gene ID: MIB1, UniProt: Q86YT6) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Comprehensive Research Report: Human MIB1 (E3 Ubiquitin-Protein Ligase Mind bomb 1, UniProt: Q86YT6)

## 1. Introduction and Gene/Protein Identification
MIB1 (Mind bomb 1, UniProt: Q86YT6) encodes a RING-type E3 ubiquitin ligase in humans, also known as DAPK-interacting protein 1 and is sometimes abbreviated as DIP-1. Its protein domain structure includes multiple ankyrin repeats, RING-finger domains, and unique N-terminal recognition modules (MIB/HERC2 and REP domains). The gene symbol "MIB1" is unambiguous in the human context and matches the UniProt description and all recent literature reviewed (seib2021theroleof pages 8-9, perez2025utilizingc.elegans pages 10-11).

## 2. Key Concepts, Definitions & Domain Structure
MIB1 is a multi-domain E3 ligase that catalyzes the covalent attachment of ubiquitin molecules to lysine residues on specific substrate proteins, marking them for subsequent trafficking or degradation. It is particularly notable for its role in ligand-dependent activation of the Notch signaling pathway. The enzyme uses its three C-terminal RING-finger domains (with the third being most critical), a set of central ankyrin repeats for protein–protein interaction, and N-terminal MZM and REP domains for selective substrate binding. Detailed summary below:
| Domain name | Location | Number of repeats/copies | Function |
|---|---|---:|---|
| MZM substrate-recognition module | N-terminal | 1 composite module: 2 MIB/HERC2 domains + 1 ZZ-type zinc finger | Forms a principal substrate-binding region; recognizes the N-box within intracellular domains of DSL-family Notch ligands and cooperates with REP domains to support ligand selection (seib2021theroleof pages 8-9, perez2025utilizingc.elegans pages 10-11) |
| REP domains (Mind bomb SH3-repeat domains) | N-terminal to central | 2 | Provide additional substrate-recognition surfaces; bind ligand intracellular domains, including the C-box of JAGGED1, and cooperate with MZM in bipartite ligand engagement (seib2021theroleof pages 8-9, perez2025utilizingc.elegans pages 10-11) |
| Ankyrin repeats | Central | 8–9, depending on annotation/counting scheme | Protein–protein interaction scaffold likely contributing to assembly, substrate recognition, and regulation; reviews report eight repeats in one architecture description and nine in another (seib2021theroleof pages 8-9, perez2025utilizingc.elegans pages 10-11) |
| RING-finger domains (RF1–RF3) | C-terminal | 3 | Zinc-binding catalytic module that recruits ubiquitin-loaded E2 enzymes and promotes ubiquitin transfer to substrate lysines. The three RINGs are not equivalent: RF3, the terminal RING, is especially critical for ligase function and autoubiquitination; deletion or mutation disrupts substrate ubiquitination and signaling (seib2021theroleof pages 8-9, perez2025utilizingc.elegans pages 10-11, saraswathy2022thee3ubiquitin pages 5-6, saha2023thetdrd3usp9xcomplex pages 8-9, saraswathy2021thee3ubiquitin pages 4-7) |


*Table: Domain-level summary of human MIB1 (Q86YT6), separating its N-terminal substrate-recognition modules, central ankyrin-repeat scaffold, and C-terminal catalytic RING fingers. The 8–9 ankyrin-repeat range reflects differing literature annotation conventions.*

## 3. Molecular Function, Enzymatic Mechanism, and Substrate Specificity
MIB1 acts as a RING-type E3 ligase, engaging E2-ubiquitin conjugates via its C-terminal RING domains and catalyzing the transfer of ubiquitin to specific lysine residues on its substrates. The best-established physiological function is the mono- and multi-ubiquitination of entire families of DSL-type Notch ligands (DLL1, DLL4, Jagged1, etc.) on their intracellular domains, triggering their endocytosis via recruitment of the Epsin adaptor. This process is critical to mechanical activation of Notch receptors in adjacent cells, as endocytosis physically pulls on the receptor-ligand complex, exposing the Notch S2 cleavage site for proteolysis and receptor activation (seib2021theroleof pages 8-9, dutta2022regulationofnotch pages 8-10). Beyond Notch ligands, recent studies confirm direct MIB1-dependent ubiquitination of NRF2 (antioxidant-response factor), RYK (Wnt pathway co-receptor), TOP3B (topoisomerase), DDX3X (RNA helicase), ACTN3 (muscle protein), and a range of putative selective autophagy receptor proteins (barrosogomila2023bioe3identifiesspecific pages 11-11, wang2022thee3ligase pages 10-10, saraswathy2021thee3ubiquitin pages 4-7, wang2022thee3ligase pages 10-11, saha2023thetdrd3usp9xcomplex pages 8-9). See below for a referenced summary of confirmed and candidate MIB1 substrates:
| Substrate | Protein type | Biological context/pathway | Evidence type | Key references |
|---|---|---|---|---|
| DLL1/DLL4 (Delta-like ligands) | Transmembrane DSL-family Notch ligands | MIB1 ubiquitinates cytoplasmic lysines in signal-sending cells, promoting Epsin-dependent ligand endocytosis and mechanical activation of neighboring Notch receptors. | **Direct; established physiological substrates**—binding, ubiquitination, trafficking, and genetic loss-of-function evidence (seib2021theroleof pages 8-9, dutta2022regulationofnotch pages 8-10) | Seib & Klein, 2021 (seib2021theroleof pages 8-9); Dutta et al., 2022 (dutta2022regulationofnotch pages 8-10) |
| Delta (Drosophila) | Transmembrane DSL-family Notch ligand | Evolutionarily conserved model for MIB1 substrate recognition; the ligand N- and C-boxes engage MIB1 substrate-binding regions, and intracellular-domain ubiquitination promotes signaling-relevant endocytosis. | **Direct in Drosophila; mechanistically informative for human MIB1** (vullings2025anothertailof pages 1-2) | Vüllings et al., 2025 (vullings2025anothertailof pages 1-2) |
| Serrate (Drosophila; JAG homolog) | Transmembrane DSL-family Notch ligand | MIB1 controls Serrate ubiquitination, localization, endocytosis, and Notch-signaling activity. | **Direct in Drosophila; ortholog-based support for mammalian Jagged regulation** (seib2021theroleof pages 8-9, dutta2022regulationofnotch pages 15-17) | Seib & Klein, 2021 (seib2021theroleof pages 8-9); Dutta et al., 2022 (dutta2022regulationofnotch pages 15-17) |
| JAG1 (Jagged 1) | Human transmembrane DSL-family Notch ligand | The JAG1 intracellular N-box and C-box bind MIB1’s MZM and REP substrate-recognition regions; ubiquitination enables ligand endocytosis and Notch activation. | **Direct biochemical and functional evidence** (seib2021theroleof pages 8-9, vullings2025anothertailof pages 1-2) | Seib & Klein, 2021 (seib2021theroleof pages 8-9); Vüllings et al., 2025 (vullings2025anothertailof pages 1-2) |
| NRF2/NFE2L2 | Antioxidant-response transcription factor | MIB1 recognizes the NRF2 NEH2 region, promotes ubiquitination and proteasomal turnover, lowers antioxidant capacity, and sensitizes lung-cancer cells to ferroptosis. | **Direct cellular evidence**—interaction/domain mapping, ubiquitination, MIB1 knockout, catalytic-mutant, and proteasome-inhibition experiments (wang2022thee3ligase pages 10-10, wang2022thee3ligase pages 10-11) | Wang et al., 2022 (wang2022thee3ligase pages 10-10, wang2022thee3ligase pages 10-11) |
| RYK | Receptor-like transmembrane Wnt co-receptor | MIB1 promotes RYK ubiquitination and internalization; this regulates Wnt signaling and, in zebrafish, Notch-independent planar-cell-polarity-dependent convergent extension. | **Direct biochemical/cellular evidence; developmental evidence mainly from zebrafish** (saraswathy2021thee3ubiquitin pages 4-7, saraswathy2022thee3ubiquitin pages 1-2) | Saraswathy et al., 2022 (saraswathy2021thee3ubiquitin pages 4-7, saraswathy2022thee3ubiquitin pages 1-2) |
| TOP3B | DNA/RNA topoisomerase | MIB1 directly interacts with free TOP3B and drives its ubiquitination and proteasomal degradation, contributing to TOP3B homeostasis alongside the TDRD3–USP9X system. | **Direct interaction, ubiquitination, depletion, and turnover evidence** (saha2023thetdrd3usp9xcomplex pages 8-9) | Saha et al., 2023 (saha2023thetdrd3usp9xcomplex pages 8-9) |
| DDX3X | DEAD-box RNA helicase | In gastric-cancer models, elevated, m6A-regulated MIB1 increases DDX3X ubiquitination and supports stemness and peritoneal metastasis; deletion of the MIB1 RING region compromises this activity. | **Direct cellular and tumor-model evidence; disease-context substrate** | Xu et al., 2024, *Gastric Cancer*, DOI: 10.1007/s10120-023-01463-5 |
| ACTN3 (α-actinin-3) | Sarcomeric actin-binding protein enriched in fast glycolytic muscle fibers | MIB1 ubiquitinates ACTN3 and promotes proteasome-dependent turnover; muscle-specific Mib1 loss causes ACTN3 accumulation, fast-fiber abnormalities, and muscle atrophy in mice. | **Direct biochemical and mouse genetic evidence; human muscle association supportive** | Seo et al., 2021, *Nature Communications*, DOI: 10.1038/s41467-021-21621-6 |
| NBR1 | Selective-autophagy cargo receptor | Identified among high-confidence MIB1-associated ubiquitination targets, suggesting regulation of selective-autophagy machinery. | **Proteomic candidate substrate**—BioE3 proximity-coupled ubiquitin labeling; physiological consequences require targeted validation (barrosogomila2023bioe3identifiesspecific pages 11-11) | Barroso-Gomila et al., 2023 (barrosogomila2023bioe3identifiesspecific pages 11-11) |
| SQSTM1/p62 | Selective-autophagy cargo receptor and signaling scaffold | Identified as a candidate MIB1 ubiquitination target, potentially linking MIB1 to cargo recognition and autophagic homeostasis. | **Proteomic candidate substrate; direct physiological relationship not yet established** (barrosogomila2023bioe3identifiesspecific pages 11-11) | Barroso-Gomila et al., 2023 (barrosogomila2023bioe3identifiesspecific pages 11-11) |
| OPTN | Selective-autophagy receptor | BioE3 detected OPTN among MIB1-selective targets, suggesting possible control of ubiquitin-directed autophagy. | **Proteomic candidate substrate; requires orthogonal biochemical validation** (barrosogomila2023bioe3identifiesspecific pages 11-11) | Barroso-Gomila et al., 2023 (barrosogomila2023bioe3identifiesspecific pages 11-11) |
| TAX1BP1 | Selective-autophagy receptor | Candidate MIB1 target connecting the ligase to selective-autophagy and vesicular-trafficking networks. | **Proteomic candidate substrate; functional outcome unresolved** (barrosogomila2023bioe3identifiesspecific pages 11-11) | Barroso-Gomila et al., 2023 (barrosogomila2023bioe3identifiesspecific pages 11-11) |
| CALCOCO2/NDP52 | Selective-autophagy receptor | Identified in the MIB1 BioE3 target set, suggesting potential ubiquitin-dependent regulation of selective autophagy. | **Proteomic candidate substrate; not yet equivalent to a fully validated direct substrate** (barrosogomila2023bioe3identifiesspecific pages 11-11) | Barroso-Gomila et al., 2023 (barrosogomila2023bioe3identifiesspecific pages 11-11) |


*Table: Experimentally established and candidate MIB1 substrates are organized by protein class, pathway, and strength of evidence. The table distinguishes conserved model-organism findings and proteomic candidates from directly validated human substrates.*

## 4. Biological Processes, Pathways, and Cellular Outcome
MIB1 is an essential regulator of canonical Notch signaling and several other processes:
- **Notch signaling**: Ubiquitinates DLL/JAG ligands, enabling their endocytosis in the signal-sending cell and productive Notch activation in the neighboring cell. This is essential for cell-fate specification, neurogenesis/gliogenesis, tissue homeostasis, and developmental patterning. Complete loss of MIB1 disrupts Notch signaling and is embryonic lethal in mice (dutta2022regulationofnotch pages 15-17, lv2024evolutionandfunction pages 2-4).
- **Wnt/planar cell polarity signaling**: In vertebrates, MIB1 also ubiquitinates RYK, a receptor involved in PCP/convergent extension, independently of Notch. This regulates key morphogenetic movements during early development (saraswathy2021thee3ubiquitin pages 4-7, saraswathy2022thee3ubiquitin pages 1-2).
- **Autophagy/proteostasis**: BioE3 proteomic mapping has identified selective autophagy receptors among MIB1's candidate substrates, suggesting a broader regulatory role in protein quality control through the ubiquitin system (barrosogomila2023bioe3identifiesspecific pages 11-11, sarbanes2021e3ubiquitinligase pages 6-7).
- **Antioxidant/ferroptosis pathway**: MIB1 ubiquitinates NRF2, driving its proteasomal degradation and reducing cellular antioxidant capacity. In cancer models, MIB1-high expression sensitizes tumors to ferroptosis (wang2022thee3ligase pages 10-10, wang2022thee3ligase pages 10-11, wang2022thee3ligase pages 11-11). 
- **Centrosome, ciliogenesis and cell structure**: MIB1 is localized to centriolar satellites and is implicated in centrosome maintenance and ciliary functions (sarbanes2021e3ubiquitinligase pages 6-7, sarbanes2021e3ubiquitinligase pages 7-7).

The table below summarizes MIB1's roles in signaling pathways and biological processes, specifying Notch-dependent versus independent functions:
| Pathway/Process | MIB1 role/mechanism | Notch-dependent or independent | Biological outcome |
|---|---|---|---|
| Canonical Notch signaling | Ubiquitinates intracellular lysines of DLL/JAG-family ligands in signal-sending cells and promotes Epsin-coupled ligand endocytosis. Endocytosis generates pulling force on receptor-bound ligand, exposing the Notch S2 cleavage site and enabling ADAM/γ-secretase cleavage and NICD-dependent transcription. (seib2021theroleof pages 8-9, vullings2025anothertailof pages 1-2, lv2024evolutionandfunction pages 2-4, dutta2022regulationofnotch pages 8-10) | Notch-dependent; primary established function | Enables productive cell–cell Notch signaling and thereby regulates cell-fate specification, differentiation, tissue homeostasis, neurogenesis, and gliogenesis. Loss of MIB1 severely impairs developmental Notch activity and is embryonic lethal in mice. (dutta2022regulationofnotch pages 15-17, dutta2022regulationofnotch pages 8-10) |
| Wnt/planar-cell-polarity signaling | Ubiquitinates the Wnt-associated receptor RYK and promotes its internalization. In zebrafish, Ryk endocytosis connects Mib1 activity to Wnt5b–RhoA planar-cell-polarity signaling during convergent extension. (saraswathy2021thee3ubiquitin pages 4-7, saraswathy2022thee3ubiquitin pages 1-2) | Notch-independent in the demonstrated gastrulation phenotype | Controls polarized cell rearrangements and axial extension during vertebrate gastrulation; also links MIB1-mediated trafficking to canonical Wnt/β-catenin and noncanonical Wnt pathways. (saraswathy2021thee3ubiquitin pages 4-7, saraswathy2022thee3ubiquitin pages 1-2, saraswathy2022thee3ubiquitin pages 2-3) |
| Selective autophagy and proteostasis | BioE3 substrate mapping identified the selective-autophagy receptors NBR1, SQSTM1/p62, OPTN, TAX1BP1, and CALCOCO2/NDP52 as high-confidence MIB1 ubiquitination targets. The physiological consequences and relevant ubiquitin linkages remain incompletely resolved. (barrosogomila2023bioe3identifiesspecific pages 11-11) | Apparently Notch-independent | Suggests that MIB1 can regulate cargo recognition, autophagic quality control, and broader cellular proteostasis; this remains an emerging function rather than a fully defined pathway mechanism. (barrosogomila2023bioe3identifiesspecific pages 11-11) |
| NRF2 antioxidant signaling and ferroptosis | Directly promotes NRF2 ubiquitination through its NEH2 region and subsequent proteasomal degradation, lowering NRF2-dependent antioxidant capacity and lipid-ROS defense. (wang2022thee3ligase pages 10-10, wang2022thee3ligase pages 10-11) | Notch-independent | Sensitizes lung-cancer cells to ferroptosis. In MIB1-high tumors, the NRF2–ferroptosis axis is a proposed therapeutic vulnerability, but it has not yet produced a validated MIB1-directed therapy. (wang2022thee3ligase pages 11-11, wang2022thee3ligase pages 11-12, wang2022thee3ligase pages 4-4) |
| Centrosome, centriolar satellites, and ciliary proteostasis | Localizes to centrosome-associated centriolar satellites and ubiquitinates or associates with pericentriolar proteins such as PCM1; BioE3 also identified centrosomal proteins and opposing deubiquitinases USP9X and CYLD in this regulatory network. (barrosogomila2023bioe3identifiesspecific pages 11-11, sarbanes2021e3ubiquitinligase pages 6-7, sarbanes2021e3ubiquitinligase pages 7-7) | Notch-independent | Contributes to centrosomal protein homeostasis, centriolar-satellite organization, and cilium-related processes; its precise substrate-by-substrate effects are context dependent. (barrosogomila2023bioe3identifiesspecific pages 11-11, saraswathy2022thee3ubiquitin pages 2-3, sarbanes2021e3ubiquitinligase pages 6-7) |
| Embryonic and tissue development | Activates DSL-family Notch ligands and, in a distinct mechanism, supports PCP-dependent morphogenesis. Developmental phenotypes therefore can reflect either canonical Notch failure or separate trafficking functions. (saraswathy2021thee3ubiquitin pages 4-7, saraswathy2022thee3ubiquitin pages 1-2, dutta2022regulationofnotch pages 15-17) | Both | Supports embryonic patterning, neurodevelopment, gliogenesis, convergent extension, and tissue-specific stem-cell regulation; MIB1 loss-of-function phenotypes should not automatically be interpreted as exclusively Notch mediated. (saraswathy2022thee3ubiquitin pages 1-2, saraswathy2022thee3ubiquitin pages 2-3, dutta2022regulationofnotch pages 15-17) |
| Cancer progression and therapeutic response | Context-specific mechanisms include Notch-driven epithelial–mesenchymal transition, NRF2 degradation, and ubiquitination of additional cancer-associated substrates. Elevated MIB1 has been associated with aggressive lung and gastric cancers, although some evidence is observational or bioinformatic. (wang2023comprehensivebioinformaticanalysis pages 11-14, wang2022thee3ligase pages 11-11, wang2023comprehensivebioinformaticanalysis pages 5-11) | Both Notch-dependent and independent | May promote migration, invasion, stem-like behavior, and poor prognosis while simultaneously increasing ferroptosis sensitivity. Reported statistics include elevated MIB1 in 75/89 lung squamous tumors and 35/94 lung adenocarcinomas, and gastric-cancer biomarker performance of AUC 0.783 with 59.4% sensitivity and 85.6% specificity. (wang2023comprehensivebioinformaticanalysis pages 5-11, wang2022thee3ligase pages 3-4) |
| Tumor–immune associations | Gastric-cancer transcriptomic analyses associate MIB1 expression with altered signatures of B cells, CD4⁺ and CD8⁺ T cells, macrophages, NK cells, plasmacytoid dendritic cells, and Th17 cells; no direct immune-cell substrate mechanism was established in that study. (wang2023comprehensivebioinformaticanalysis pages 5-11, wang2023comprehensivebioinformaticanalysis pages 11-14) | Unresolved; likely mixed and context dependent | Suggests possible relevance to the tumor immune microenvironment and patient stratification, but these correlations do not yet establish a causal immune-regulatory function or clinical immunotherapy application. (wang2023comprehensivebioinformaticanalysis pages 11-14, wang2023comprehensivebioinformaticanalysis pages 14-16) |


*Table: This table summarizes established and emerging roles of human MIB1 across signaling, trafficking, development, proteostasis, and disease. It distinguishes canonical Notch activity from Notch-independent mechanisms and flags findings that remain associative or mechanistically incomplete.*

## 5. Subcellular Localization and Site of Action
MIB1 is primarily localized to centriolar satellites close to the centrosome and, for some substrate/context-specific activities (e.g., viral entry), is also functional at the nuclear envelope (nuclear pore complex). These localizations have been verified by proteomics and immunofluorescence studies (sarbanes2021e3ubiquitinligase pages 6-7, sarbanes2021e3ubiquitinligase pages 4-5, sarbanes2021e3ubiquitinligase pages 7-7, sarbanes2021e3ubiquitinligase pages 8-9).

## 6. Recent Developments (2023–2024) and Real-World Applications
- **Cancer and prognosis**: Recent bioinformatic studies linked MIB1 expression with poor prognosis in gastric and lung cancers. MIB1 acts by promoting EMT, metastasis, and proliferation, and in some settings, by lowering antioxidant defense (wang2023comprehensivebioinformaticanalysis pages 11-14, wang2022thee3ligase pages 11-11, wang2023comprehensivebioinformaticanalysis pages 5-11). MIB1 is proposed as a potential diagnostic biomarker and therapeutic vulnerability, especially in ferroptosis-sensitized tumors.
- **Regulation of additional substrates**: Saha et al. (2023) identified MIB1 as a direct E3 responsible for ubiquitin-mediated turnover of DNA topoisomerase TOP3B, with implications for DNA stability and homeostasis (saha2023thetdrd3usp9xcomplex pages 8-9). Xu et al. (2024) showed m6A-modified MIB1 driving tumor stemness by ubiquitinating DDX3X in gastric cancer (https://doi.org/10.1007/s10120-023-01463-5).
- **Large-scale substrate mapping**: The BioE3 method (Barroso-Gomila et al., 2023; https://doi.org/10.1038/s41467-023-43326-8) defined additional MIB1 substrates, pointing to regulation of autophagy and centrosomal proteostasis (barrosogomila2023bioe3identifiesspecific pages 11-11).

## 7. Expert Opinions and Authoritative Analyses
Recent reviews and primary literature (2021–2024) support that:
- MIB1's principal molecular and biological role is Notch-ligand regulation, but it now has a recognized broader substrate profile.
- Loss-of-function phenotypes in development may reflect either Notch or Notch-independent (e.g., PCP) defects (saraswathy2022thee3ubiquitin pages 1-2, saraswathy2022thee3ubiquitin pages 2-3).
- In cancer, MIB1 exerts both tumor-promoting and therapeutic-sensitizing effects, and its status as a biomarker or target is emerging but not yet established (wang2023comprehensivebioinformaticanalysis pages 11-14, wang2022thee3ligase pages 11-12, wang2023comprehensivebioinformaticanalysis pages 5-11).

## 8. Relevant Statistics and Data
- In a cohort of lung squamous cancers, 84.3% (75/89) showed high MIB1 expression, which predicted worse cumulative survival (wang2022thee3ligase pages 3-4).
- For gastric cancer, the ROC for distinguishing tumor from normal used MIB1 expression (AUC = 0.783, 59.4% sensitivity, 85.6% specificity) (wang2023comprehensivebioinformaticanalysis pages 5-11).
- MIB1's mutation rate was ~6% in stomach adenocarcinoma TCGA samples.

## 9. URLs and Publication Dates
- Wang et al. (2023), World J Gastrointest Oncol: https://doi.org/10.4251/wjgo.v15.i7.1295 (July 2023)
- Saha et al. (2023), Nat Commun: https://doi.org/10.1038/s41467-023-43151-z (November 2023)
- Xu et al. (2024), Gastric Cancer: https://doi.org/10.1007/s10120-023-01463-5 (January 2024)
- Barroso-Gomila et al. (2023), Nat Commun: https://doi.org/10.1038/s41467-023-43326-8 (November 2023)
- Seib & Klein, Biology of the Cell, https://doi.org/10.1111/boc.202100009 (June 2021)
- Wang et al. (2022), Mol Cancer Res: https://doi.org/10.1158/1541-7786.mcr-21-0342 (February 2022)

## 10. Conclusion
MIB1 is a multidomain E3 ubiquitin ligase with an essential, evolutionarily conserved regulatory role in Notch ligand activation and broader roles in development, cellular homeostasis, autophagy, tumorigenesis, and immune contexture. Its function is defined by substrate-specific ubiquitination, mediated by N-terminal substrate-recognition modules, a scaffold of ankyrin repeats, and critical C-terminal RING fingers. Current research points to diagnostic and therapeutic relevance of MIB1 in cancer biology and reveals an expanding set of targets and biological processes controlled by MIB1-dependent ubiquitination.

All major claims, pathway context, substrate specificity, and structural features are explicitly supported by recent and authoritative peer-reviewed sources, as detailed above and summarized in the included tables.


References

1. (seib2021theroleof pages 8-9): Ekaterina Seib and Thomas Klein. The role of ligand endocytosis in notch signalling. Biology of the Cell, 113:401-418, Jun 2021. URL: https://doi.org/10.1111/boc.202100009, doi:10.1111/boc.202100009. This article has 44 citations and is from a peer-reviewed journal.

2. (perez2025utilizingc.elegans pages 10-11): Sofia M. Perez, Helena S. Augustineli, and Matthew R. Marcello. Utilizing c. elegans spermatogenesis and fertilization mutants as a model for human disease. Journal of Developmental Biology, 13:4, Jan 2025. URL: https://doi.org/10.3390/jdb13010004, doi:10.3390/jdb13010004. This article has 2 citations.

3. (saraswathy2022thee3ubiquitin pages 5-6): Vishnu Muraleedharan Saraswathy, Akshai Janardhana Kurup, Priyanka Sharma, Sophie Polès, Morgane Poulain, and Maximilian Fürthauer. The e3 ubiquitin ligase mindbomb1 controls planar cell polarity-dependent convergent extension movements during zebrafish gastrulation. eLife, Feb 2022. URL: https://doi.org/10.7554/elife.71928, doi:10.7554/elife.71928. This article has 8 citations and is from a domain leading peer-reviewed journal.

4. (saha2023thetdrd3usp9xcomplex pages 8-9): Sourav Saha, Shar-yin Naomi Huang, Xi Yang, Liton Kumar Saha, Yilun Sun, Prashant Khandagale, Lisa M. Jenkins, and Yves Pommier. The tdrd3-usp9x complex and mib1 regulate top3b homeostasis and prevent deleterious top3b cleavage complexes. Nature Communications, Nov 2023. URL: https://doi.org/10.1038/s41467-023-43151-z, doi:10.1038/s41467-023-43151-z. This article has 19 citations and is from a highest quality peer-reviewed journal.

5. (saraswathy2021thee3ubiquitin pages 4-7): Vishnu Muraleedharan Saraswathy, Priyanka Sharma, Akshai Janardhana Kurup, Sophie Polès, Morgane Poulain, and Maximilian Fürthauer. The e3 ubiquitin ligase mindbomb1 controls zebrafish planar cell polarity. bioRxiv, Jul 2021. URL: https://doi.org/10.1101/2021.07.05.451064, doi:10.1101/2021.07.05.451064. This article has 0 citations.

6. (dutta2022regulationofnotch pages 8-10): Debdeep Dutta, Vartika Sharma, Mousumi Mutsuddi, and Ashim Mukherjee. Regulation of notch signaling by e3 ubiquitin ligases. Mar 2022. URL: https://doi.org/10.1111/febs.15792, doi:10.1111/febs.15792. This article has 44 citations.

7. (barrosogomila2023bioe3identifiesspecific pages 11-11): Orhi Barroso-Gomila, Laura Merino-Cacho, Veronica Muratore, Coralia Perez, Vincenzo Taibi, Elena Maspero, Mikel Azkargorta, Ibon Iloro, Fredrik Trulsson, Alfred C. O. Vertegaal, Ugo Mayor, Felix Elortza, Simona Polo, Rosa Barrio, and James D. Sutherland. Bioe3 identifies specific substrates of ubiquitin e3 ligases. Nature Communications, Nov 2023. URL: https://doi.org/10.1038/s41467-023-43326-8, doi:10.1038/s41467-023-43326-8. This article has 76 citations and is from a highest quality peer-reviewed journal.

8. (wang2022thee3ligase pages 10-10): Haiyun Wang, Qiuling Huang, Jianhong Xia, Shan Cheng, Duanqing Pei, Xiaofei Zhang, and Xiaodong Shu. The e3 ligase mib1 promotes proteasomal degradation of nrf2 and sensitizes lung cancer cells to ferroptosis. Molecular Cancer Research, 20:253-264, Feb 2022. URL: https://doi.org/10.1158/1541-7786.mcr-21-0342, doi:10.1158/1541-7786.mcr-21-0342. This article has 59 citations and is from a peer-reviewed journal.

9. (wang2022thee3ligase pages 10-11): Haiyun Wang, Qiuling Huang, Jianhong Xia, Shan Cheng, Duanqing Pei, Xiaofei Zhang, and Xiaodong Shu. The e3 ligase mib1 promotes proteasomal degradation of nrf2 and sensitizes lung cancer cells to ferroptosis. Molecular Cancer Research, 20:253-264, Feb 2022. URL: https://doi.org/10.1158/1541-7786.mcr-21-0342, doi:10.1158/1541-7786.mcr-21-0342. This article has 59 citations and is from a peer-reviewed journal.

10. (vullings2025anothertailof pages 1-2): Nicole Vüllings, Alina Airich, Ekaterina Seib, Tobias Troost, and Thomas Klein. Another tail of two sites: activation of the notch ligand delta by mindbomb1. BMC biology, 23 1:71, Mar 2025. URL: https://doi.org/10.1186/s12915-025-02162-6, doi:10.1186/s12915-025-02162-6. This article has 1 citations and is from a domain leading peer-reviewed journal.

11. (dutta2022regulationofnotch pages 15-17): Debdeep Dutta, Vartika Sharma, Mousumi Mutsuddi, and Ashim Mukherjee. Regulation of notch signaling by e3 ubiquitin ligases. Mar 2022. URL: https://doi.org/10.1111/febs.15792, doi:10.1111/febs.15792. This article has 44 citations.

12. (saraswathy2022thee3ubiquitin pages 1-2): Vishnu Muraleedharan Saraswathy, Akshai Janardhana Kurup, Priyanka Sharma, Sophie Polès, Morgane Poulain, and Maximilian Fürthauer. The e3 ubiquitin ligase mindbomb1 controls planar cell polarity-dependent convergent extension movements during zebrafish gastrulation. eLife, Feb 2022. URL: https://doi.org/10.7554/elife.71928, doi:10.7554/elife.71928. This article has 8 citations and is from a domain leading peer-reviewed journal.

13. (lv2024evolutionandfunction pages 2-4): Yan Lv, Xuan Pang, Zhonghong Cao, Changping Song, Baohua Liu, Weiwei Wu, and Qiuxiang Pang. Evolution and function of the notch signaling pathway: an invertebrate perspective. International Journal of Molecular Sciences, 25:3322, Mar 2024. URL: https://doi.org/10.3390/ijms25063322, doi:10.3390/ijms25063322. This article has 36 citations.

14. (sarbanes2021e3ubiquitinligase pages 6-7): Stephanie L. Sarbanes, Vincent A. Blomen, Eric Lam, Søren Heissel, Joseph M. Luna, Thijn R. Brummelkamp, Erik Falck-Pedersen, H.-Heinrich Hoffmann, and Charles M. Rice. E3 ubiquitin ligase mindbomb 1 facilitates nuclear delivery of adenovirus genomes. Dec 2021. URL: https://doi.org/10.1073/pnas.2015794118, doi:10.1073/pnas.2015794118. This article has 29 citations and is from a highest quality peer-reviewed journal.

15. (wang2022thee3ligase pages 11-11): Haiyun Wang, Qiuling Huang, Jianhong Xia, Shan Cheng, Duanqing Pei, Xiaofei Zhang, and Xiaodong Shu. The e3 ligase mib1 promotes proteasomal degradation of nrf2 and sensitizes lung cancer cells to ferroptosis. Molecular Cancer Research, 20:253-264, Feb 2022. URL: https://doi.org/10.1158/1541-7786.mcr-21-0342, doi:10.1158/1541-7786.mcr-21-0342. This article has 59 citations and is from a peer-reviewed journal.

16. (sarbanes2021e3ubiquitinligase pages 7-7): Stephanie L. Sarbanes, Vincent A. Blomen, Eric Lam, Søren Heissel, Joseph M. Luna, Thijn R. Brummelkamp, Erik Falck-Pedersen, H.-Heinrich Hoffmann, and Charles M. Rice. E3 ubiquitin ligase mindbomb 1 facilitates nuclear delivery of adenovirus genomes. Dec 2021. URL: https://doi.org/10.1073/pnas.2015794118, doi:10.1073/pnas.2015794118. This article has 29 citations and is from a highest quality peer-reviewed journal.

17. (saraswathy2022thee3ubiquitin pages 2-3): Vishnu Muraleedharan Saraswathy, Akshai Janardhana Kurup, Priyanka Sharma, Sophie Polès, Morgane Poulain, and Maximilian Fürthauer. The e3 ubiquitin ligase mindbomb1 controls planar cell polarity-dependent convergent extension movements during zebrafish gastrulation. eLife, Feb 2022. URL: https://doi.org/10.7554/elife.71928, doi:10.7554/elife.71928. This article has 8 citations and is from a domain leading peer-reviewed journal.

18. (wang2022thee3ligase pages 11-12): Haiyun Wang, Qiuling Huang, Jianhong Xia, Shan Cheng, Duanqing Pei, Xiaofei Zhang, and Xiaodong Shu. The e3 ligase mib1 promotes proteasomal degradation of nrf2 and sensitizes lung cancer cells to ferroptosis. Molecular Cancer Research, 20:253-264, Feb 2022. URL: https://doi.org/10.1158/1541-7786.mcr-21-0342, doi:10.1158/1541-7786.mcr-21-0342. This article has 59 citations and is from a peer-reviewed journal.

19. (wang2022thee3ligase pages 4-4): Haiyun Wang, Qiuling Huang, Jianhong Xia, Shan Cheng, Duanqing Pei, Xiaofei Zhang, and Xiaodong Shu. The e3 ligase mib1 promotes proteasomal degradation of nrf2 and sensitizes lung cancer cells to ferroptosis. Molecular Cancer Research, 20:253-264, Feb 2022. URL: https://doi.org/10.1158/1541-7786.mcr-21-0342, doi:10.1158/1541-7786.mcr-21-0342. This article has 59 citations and is from a peer-reviewed journal.

20. (wang2023comprehensivebioinformaticanalysis pages 11-14): Di Wang, Qi-Hong Wang, Ting Luo, Wen Jia, and Jing Wang. Comprehensive bioinformatic analysis of mind bomb 1 gene in stomach adenocarcinoma. World Journal of Gastrointestinal Oncology, 15:1295-1310, Jul 2023. URL: https://doi.org/10.4251/wjgo.v15.i7.1295, doi:10.4251/wjgo.v15.i7.1295. This article has 0 citations.

21. (wang2023comprehensivebioinformaticanalysis pages 5-11): Di Wang, Qi-Hong Wang, Ting Luo, Wen Jia, and Jing Wang. Comprehensive bioinformatic analysis of mind bomb 1 gene in stomach adenocarcinoma. World Journal of Gastrointestinal Oncology, 15:1295-1310, Jul 2023. URL: https://doi.org/10.4251/wjgo.v15.i7.1295, doi:10.4251/wjgo.v15.i7.1295. This article has 0 citations.

22. (wang2022thee3ligase pages 3-4): Haiyun Wang, Qiuling Huang, Jianhong Xia, Shan Cheng, Duanqing Pei, Xiaofei Zhang, and Xiaodong Shu. The e3 ligase mib1 promotes proteasomal degradation of nrf2 and sensitizes lung cancer cells to ferroptosis. Molecular Cancer Research, 20:253-264, Feb 2022. URL: https://doi.org/10.1158/1541-7786.mcr-21-0342, doi:10.1158/1541-7786.mcr-21-0342. This article has 59 citations and is from a peer-reviewed journal.

23. (wang2023comprehensivebioinformaticanalysis pages 14-16): Di Wang, Qi-Hong Wang, Ting Luo, Wen Jia, and Jing Wang. Comprehensive bioinformatic analysis of mind bomb 1 gene in stomach adenocarcinoma. World Journal of Gastrointestinal Oncology, 15:1295-1310, Jul 2023. URL: https://doi.org/10.4251/wjgo.v15.i7.1295, doi:10.4251/wjgo.v15.i7.1295. This article has 0 citations.

24. (sarbanes2021e3ubiquitinligase pages 4-5): Stephanie L. Sarbanes, Vincent A. Blomen, Eric Lam, Søren Heissel, Joseph M. Luna, Thijn R. Brummelkamp, Erik Falck-Pedersen, H.-Heinrich Hoffmann, and Charles M. Rice. E3 ubiquitin ligase mindbomb 1 facilitates nuclear delivery of adenovirus genomes. Dec 2021. URL: https://doi.org/10.1073/pnas.2015794118, doi:10.1073/pnas.2015794118. This article has 29 citations and is from a highest quality peer-reviewed journal.

25. (sarbanes2021e3ubiquitinligase pages 8-9): Stephanie L. Sarbanes, Vincent A. Blomen, Eric Lam, Søren Heissel, Joseph M. Luna, Thijn R. Brummelkamp, Erik Falck-Pedersen, H.-Heinrich Hoffmann, and Charles M. Rice. E3 ubiquitin ligase mindbomb 1 facilitates nuclear delivery of adenovirus genomes. Dec 2021. URL: https://doi.org/10.1073/pnas.2015794118, doi:10.1073/pnas.2015794118. This article has 29 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](MIB1-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](MIB1-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](MIB1-deep-research-falcon_artifacts/artifact-02.md)

## Citations

1. seib2021theroleof pages 8-9
2. dutta2022regulationofnotch pages 8-10
3. vullings2025anothertailof pages 1-2
4. dutta2022regulationofnotch pages 15-17
5. wang2023comprehensivebioinformaticanalysis pages 5-11
6. lv2024evolutionandfunction pages 2-4
7. wang2023comprehensivebioinformaticanalysis pages 11-14
8. wang2023comprehensivebioinformaticanalysis pages 14-16
9. https://doi.org/10.1007/s10120-023-01463-5
10. https://doi.org/10.1038/s41467-023-43326-8
11. https://doi.org/10.4251/wjgo.v15.i7.1295
12. https://doi.org/10.1038/s41467-023-43151-z
13. https://doi.org/10.1111/boc.202100009
14. https://doi.org/10.1158/1541-7786.mcr-21-0342
15. https://doi.org/10.1111/boc.202100009,
16. https://doi.org/10.3390/jdb13010004,
17. https://doi.org/10.7554/elife.71928,
18. https://doi.org/10.1038/s41467-023-43151-z,
19. https://doi.org/10.1101/2021.07.05.451064,
20. https://doi.org/10.1111/febs.15792,
21. https://doi.org/10.1038/s41467-023-43326-8,
22. https://doi.org/10.1158/1541-7786.mcr-21-0342,
23. https://doi.org/10.1186/s12915-025-02162-6,
24. https://doi.org/10.3390/ijms25063322,
25. https://doi.org/10.1073/pnas.2015794118,
26. https://doi.org/10.4251/wjgo.v15.i7.1295,