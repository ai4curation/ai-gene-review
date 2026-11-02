---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-30T06:40:55.965516'
end_time: '2026-09-30T06:53:49.002977'
duration_seconds: 773.04
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: DROME
  gene_id: Myd88
  gene_symbol: Myd88
  uniprot_accession: A1Z7T8
  protein_description: 'SubName: Full=Myd88, isoform A {ECO:0000313|EMBL:AAF58953.1};
    SubName: Full=Myd88, isoform B {ECO:0000313|EMBL:AGB93354.1}; SubName: Full=Myd88,
    isoform C {ECO:0000313|EMBL:AHN56044.1};'
  gene_info: Name=Myd88 {ECO:0000313|EMBL:AAF58953.1}; Synonyms=Dmel\CG2078 {ECO:0000313|EMBL:AAF58953.1},
    DMMYD88 {ECO:0000313|EMBL:AAF58953.1}, DmMyD88 {ECO:0000313|EMBL:AAF58953.1},
    DmMyd88 {ECO:0000313|EMBL:AAF58953.1}, dMYd88 {ECO:0000313|EMBL:AAF58953.1}, dMyD88
    {ECO:0000313|EMBL:AAF58953.1}, dMyd88 {ECO:0000313|EMBL:AAF58953.1}, dsMyD88 {ECO:0000313|EMBL:AAF58953.1},
    EP(2)2535 {ECO:0000313|EMBL:AAF58953.1}, Kra {ECO:0000313|EMBL:AAF58953.1}, kra
    {ECO:0000313|EMBL:AAF58953.1}, LD20892 {ECO:0000313|EMBL:AAF58953.1}, MyD8 {ECO:0000313|EMBL:AAF58953.1},
    MYD88 {ECO:0000313|EMBL:AAF58953.1}, MyD88 {ECO:0000313|EMBL:AAF58953.1}, myd88
    {ECO:0000313|EMBL:AAF58953.1}, Myd88F {ECO:0000313|EMBL:AAF58953.1}; ORFNames=CG2078
    {ECO:0000313|EMBL:AAF58953.1}, Dmel_CG2078 {ECO:0000313|EMBL:AAF58953.1};
  organism_full: Drosophila melanogaster (Fruit fly).
  protein_family: Not specified in UniProt
  protein_domains: DEATH-like_dom_sf. (IPR011029); Myelin_different_resp_MyD88. (IPR017281);
    TIR_dom. (IPR000157); Toll_tir_struct_dom_sf. (IPR035897); TIR_2 (PF13676)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 35
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Myd88-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** A1Z7T8
- **Protein Description:** SubName: Full=Myd88, isoform A {ECO:0000313|EMBL:AAF58953.1}; SubName: Full=Myd88, isoform B {ECO:0000313|EMBL:AGB93354.1}; SubName: Full=Myd88, isoform C {ECO:0000313|EMBL:AHN56044.1};
- **Gene Information:** Name=Myd88 {ECO:0000313|EMBL:AAF58953.1}; Synonyms=Dmel\CG2078 {ECO:0000313|EMBL:AAF58953.1}, DMMYD88 {ECO:0000313|EMBL:AAF58953.1}, DmMyD88 {ECO:0000313|EMBL:AAF58953.1}, DmMyd88 {ECO:0000313|EMBL:AAF58953.1}, dMYd88 {ECO:0000313|EMBL:AAF58953.1}, dMyD88 {ECO:0000313|EMBL:AAF58953.1}, dMyd88 {ECO:0000313|EMBL:AAF58953.1}, dsMyD88 {ECO:0000313|EMBL:AAF58953.1}, EP(2)2535 {ECO:0000313|EMBL:AAF58953.1}, Kra {ECO:0000313|EMBL:AAF58953.1}, kra {ECO:0000313|EMBL:AAF58953.1}, LD20892 {ECO:0000313|EMBL:AAF58953.1}, MyD8 {ECO:0000313|EMBL:AAF58953.1}, MYD88 {ECO:0000313|EMBL:AAF58953.1}, MyD88 {ECO:0000313|EMBL:AAF58953.1}, myd88 {ECO:0000313|EMBL:AAF58953.1}, Myd88F {ECO:0000313|EMBL:AAF58953.1}; ORFNames=CG2078 {ECO:0000313|EMBL:AAF58953.1}, Dmel_CG2078 {ECO:0000313|EMBL:AAF58953.1};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** DEATH-like_dom_sf. (IPR011029); Myelin_different_resp_MyD88. (IPR017281); TIR_dom. (IPR000157); Toll_tir_struct_dom_sf. (IPR035897); TIR_2 (PF13676)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Myd88" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Myd88' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Myd88** (gene ID: Myd88, UniProt: A1Z7T8) in DROME.

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
- **UniProt Accession:** A1Z7T8
- **Protein Description:** SubName: Full=Myd88, isoform A {ECO:0000313|EMBL:AAF58953.1}; SubName: Full=Myd88, isoform B {ECO:0000313|EMBL:AGB93354.1}; SubName: Full=Myd88, isoform C {ECO:0000313|EMBL:AHN56044.1};
- **Gene Information:** Name=Myd88 {ECO:0000313|EMBL:AAF58953.1}; Synonyms=Dmel\CG2078 {ECO:0000313|EMBL:AAF58953.1}, DMMYD88 {ECO:0000313|EMBL:AAF58953.1}, DmMyD88 {ECO:0000313|EMBL:AAF58953.1}, DmMyd88 {ECO:0000313|EMBL:AAF58953.1}, dMYd88 {ECO:0000313|EMBL:AAF58953.1}, dMyD88 {ECO:0000313|EMBL:AAF58953.1}, dMyd88 {ECO:0000313|EMBL:AAF58953.1}, dsMyD88 {ECO:0000313|EMBL:AAF58953.1}, EP(2)2535 {ECO:0000313|EMBL:AAF58953.1}, Kra {ECO:0000313|EMBL:AAF58953.1}, kra {ECO:0000313|EMBL:AAF58953.1}, LD20892 {ECO:0000313|EMBL:AAF58953.1}, MyD8 {ECO:0000313|EMBL:AAF58953.1}, MYD88 {ECO:0000313|EMBL:AAF58953.1}, MyD88 {ECO:0000313|EMBL:AAF58953.1}, myd88 {ECO:0000313|EMBL:AAF58953.1}, Myd88F {ECO:0000313|EMBL:AAF58953.1}; ORFNames=CG2078 {ECO:0000313|EMBL:AAF58953.1}, Dmel_CG2078 {ECO:0000313|EMBL:AAF58953.1};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** DEATH-like_dom_sf. (IPR011029); Myelin_different_resp_MyD88. (IPR017281); TIR_dom. (IPR000157); Toll_tir_struct_dom_sf. (IPR035897); TIR_2 (PF13676)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Myd88" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Myd88' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Myd88** (gene ID: Myd88, UniProt: A1Z7T8) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Comprehensive Research Report: Drosophila melanogaster Myd88 (UniProt A1Z7T8)

## Gene Identity Verification

The gene Myd88 (CG2078) in *Drosophila melanogaster* encodes the fly ortholog of MyD88, a conserved intracellular adaptor protein in Toll signaling pathways. This protein is distinct from mammalian MYD88 and other similarly named insect proteins, though it shares fundamental structural and functional features with vertebrate TLR pathway adaptors (lima2021evolutionoftoll pages 1-2, lima2021evolutionoftoll pages 19-19). The UniProt entry A1Z7T8 describes three isoforms (A, B, and C), though isoform-specific functional differences have not been experimentally resolved in the available literature.

## Primary Molecular Function

Drosophila Myd88 functions as a **non-enzymatic signaling adaptor and scaffold protein** that couples activated Toll-family receptors to downstream signaling components. Unlike enzymes, Myd88 has no catalytic activity, substrate specificity, or reaction mechanism; instead, it organizes multi-protein signaling complexes through protein-protein interactions (zhang2024maintainingtollsignaling pages 3-6, kietz2023drosophilacaspasesas pages 3-4, lima2021evolutionoftoll pages 1-2). Following Toll receptor activation by the ligand Spätzle, Myd88 binds to the cytoplasmic Toll/interleukin-1 receptor (TIR) domain of the receptor and recruits the adaptor protein Tube and the serine/threonine kinase Pelle, forming the canonical Myd88-Tube-Pelle signaling complex (zhang2024maintainingtollsignaling pages 3-6, lima2021evolutionoftoll pages 1-2, kietz2023drosophilacaspasesas pages 3-4).

This adaptor function is the defining molecular role of Myd88 in *Drosophila*. The protein serves as a scaffold that enables Pelle kinase activity, which in turn phosphorylates the IκB-like inhibitor Cactus, targeting it for proteasomal degradation. This releases the NF-κB-family transcription factors Dif (Dorsal-related immunity factor) and Dorsal from cytoplasmic sequestration, allowing their nuclear translocation and activation of immune-response genes (kietz2023drosophilacaspasesas pages 3-4, cammaratamouchtouris2022dynamicregulationof pages 4-6, lima2021evolutionoftoll pages 1-2).

## Protein Structure and Domains

### TIR Domain

Myd88 contains a C-terminal Toll/interleukin-1 receptor (TIR) domain, which is the signature feature of this protein family (toshchakov2020asurveyof pages 2-3, toshchakov2020asurveyof pages 1-2). The TIR domain mediates interactions with the activated Toll receptor's cytoplasmic TIR region and potentially with other TIR-domain-containing proteins. Structurally, TIR domains adopt a conserved fold consisting of a central five-stranded parallel β-sheet surrounded by α-helices (toshchakov2020asurveyof pages 1-2, lou2025tirdomainproteins pages 5-6). The domain contains three conserved functional motifs (Box 1, Box 2, and Box 3) that are critical for protein-protein interactions and signaling specificity. While full-length *Drosophila* Myd88 structures have not been experimentally determined, comparative analysis indicates that the fly protein's TIR domain shares the fundamental architecture and conserved residues seen across arthropod and vertebrate TIR-containing adaptors (toshchakov2020asurveyof pages 2-3, liu2021identificationofcore pages 5-9).

### Death Domain

The N-terminal region of Myd88 contains a death domain (DD), an approximately 80-amino-acid protein-interaction module that is essential for organizing the downstream signaling complex (toshchakov2020asurveyof pages 2-3, toshchakov2020asurveyof pages 1-2, lou2025tirdomainproteins pages 5-6). The death domain mediates heterotrimeric complex formation with Tube and Pelle through death-domain interactions, creating a signaling platform that enables Toll pathway signal transduction (lima2021evolutionoftoll pages 1-2). This domain architecture—combining an N-terminal death domain with a C-terminal TIR domain—is characteristic of arthropod Myd88-like proteins and distinguishes them from other TIR-domain protein families (toshchakov2020asurveyof pages 2-3).

### Localization Domain

Comparative sequence analysis suggests that arthropod Myd88 proteins, including the *Drosophila* ortholog, contain an additional C-terminal localization domain beyond the TIR region (toshchakov2020asurveyof pages 2-3). The precise boundaries and functional role of this domain in the fly protein remain incompletely characterized, though studies have demonstrated that *Drosophila* Myd88 can bind phosphoinositides, which may facilitate its recruitment to cellular membranes during signaling (lima2021evolutionoftoll pages 19-19).

## Subcellular Localization

Myd88 is an **intracellular, predominantly cytoplasmic** adaptor protein (lima2021evolutionoftoll pages 1-2, zhang2024maintainingtollsignaling pages 3-6). It is not a transmembrane receptor or secreted protein; rather, it operates on the cytosolic face of activated Toll receptors. The protein exhibits regulated membrane association through phosphoinositide binding, which controls its recruitment to signaling-competent receptor complexes and modulates antibacterial immune responses (lima2021evolutionoftoll pages 19-19). This dual localization—freely cytoplasmic in resting cells but transiently recruited to membrane-associated receptor complexes upon activation—is characteristic of many signaling adaptors and enables rapid signal transmission following pathogen recognition.

Recent work has also identified Myd88 expression in neuronal populations, particularly PAM dopaminergic neurons, and in glial cells contributing to the blood-brain barrier, suggesting tissue-specific roles beyond classical immune tissues like the fat body (singh2025toll1dependentimmuneevasion pages 18-19, singh2025toll1dependentimmuneevasion pages 16-18).

## Signaling Pathways and Biochemical Mechanisms

### Canonical Toll Pathway Signaling

The primary signaling role of Myd88 is in the **Toll innate immune pathway**, which is essential for defense against fungal and Gram-positive bacterial infections (kietz2023drosophilacaspasesas pages 8-8, hardiyanti2026drosophilaasa pages 1-2). The pathway operates through the following molecular sequence:

1. **Pathogen recognition and receptor activation**: Recognition of fungal β-1,3-glucan by GNBP3 or activation of the Persephone protease cascade leads to proteolytic processing and activation of Spätzle, the ligand for Toll receptors (hardiyanti2026drosophilaasa pages 2-4).

2. **Myd88 recruitment**: Activated Spätzle binds to the extracellular domain of Toll receptors (particularly Toll-1), inducing a conformational change that enables Myd88 binding to the receptor's cytoplasmic TIR domain (zhang2024maintainingtollsignaling pages 3-6, lima2021evolutionoftoll pages 1-2, kietz2023drosophilacaspasesas pages 3-4).

3. **Signaling complex assembly**: Myd88 recruits Tube and Pelle through death-domain interactions, forming the Myd88-Tube-Pelle signaling complex (kietz2023drosophilacaspasesas pages 3-4, lima2021evolutionoftoll pages 1-2).

4. **Cactus phosphorylation and degradation**: The assembled complex enables Pelle kinase activity, leading to phosphorylation of the IκB-like inhibitor Cactus, which is then targeted for proteasomal degradation (kietz2023drosophilacaspasesas pages 3-4).

5. **NF-κB activation**: Degradation of Cactus releases the NF-κB transcription factors Dif and Dorsal, which translocate to the nucleus (zhang2024maintainingtollsignaling pages 3-6, kietz2023drosophilacaspasesas pages 3-4, cammaratamouchtouris2022dynamicregulationof pages 4-6, lima2021evolutionoftoll pages 1-2).

6. **Immune gene expression**: Nuclear Dif and Dorsal activate transcription of antimicrobial peptide genes, including *Drosomycin* (*Drs*), *Metchnikowin*, and context-dependent *Defensin* expression (zhang2024maintainingtollsignaling pages 3-6, cammaratamouchtouris2022dynamicregulationof pages 4-6).

### Receptor Specificity

Recent studies have revealed important receptor-specific differences in Myd88 dependence (zhang2024maintainingtollsignaling pages 3-6, zhang2024maintainingtollsignaling pages 6-8). While Toll-1-mediated signaling strongly depends on Myd88 for multiple outputs, Toll-7 signaling shows more complex Myd88 dependence:

- **Toll-1 signaling**: Myd88 is required for Toll-1-induced expression of autophagy-related genes (*DmAtg8a*, *DmInR*) and antimicrobial peptides (*Drs*) (zhang2024maintainingtollsignaling pages 3-6, zhang2024maintainingtollsignaling pages 6-8).

- **Toll-7 signaling**: Toll-7 can activate *Drs* expression through a pathway that requires Myd88, but Toll-7-mediated autophagy gene expression and some other outputs occur independently of Myd88 (zhang2024maintainingtollsignaling pages 3-6, zhang2024maintainingtollsignaling pages 6-8, zhang2024maintainingtollsignaling pages 10-12).

This receptor specificity suggests that different Toll-family receptors can engage distinct downstream mechanisms, with Toll-7 potentially utilizing alternative adaptors or direct TIR-domain interactions to bypass Myd88 for certain signaling outputs.

### Autophagy Regulation

A major recent discovery is that Myd88 functions in **Toll-1-dependent autophagy regulation** (zhang2024maintainingtollsignaling pages 6-8, zhang2024maintainingtollsignaling pages 1-2, zhang2024maintainingtollsignaling pages 3-6). In cultured Drosophila S2 cells, RNAi-mediated knockdown of Myd88 suppresses Toll-1-induced expression of autophagy-related genes, prevents the associated increase in LC3-II (the lipidated form of Atg8), reduces P62 degradation, and inhibits Toll-1-induced PP2A phosphatase activity (zhang2024maintainingtollsignaling pages 6-8). This Toll-1/Myd88-dependent autophagy pathway is important for maintaining basal autophagy in the adult *Drosophila* brain and appears critical for dopaminergic neuron survival (zhang2024maintainingtollsignaling pages 6-8, zhang2024maintainingtollsignaling pages 1-2, zhang2024maintainingtollsignaling pages 8-10).

However, Myd88 is not universally required for all Toll-mediated autophagy. Both Toll-1 and Toll-7 signaling converge on Tube, Pelle, and PP2A to promote autophagy, but Toll-7 can activate autophagy-related gene expression through a largely Myd88-independent mechanism (zhang2024maintainingtollsignaling pages 10-12). This indicates parallel or redundant pathways for autophagy regulation within the Toll signaling network.

## Biological Processes and Functions

### Innate Immunity

The primary biological function of Myd88 is as a **critical component of humoral innate immunity**, particularly in responses to fungal infections and Gram-positive bacterial challenges (kietz2023drosophilacaspasesas pages 8-8, hardiyanti2026drosophilaasa pages 1-2, maasdorp2026ibinaandibinb pages 12-13). Genetic studies have established that Myd88 is required for effective immune responses to these pathogens, connecting pathogen detection by Toll receptors to the production of antimicrobial effectors. The pathway regulates expression of antimicrobial peptides including:

- **Drosomycin**: The principal antifungal peptide, strongly induced by Toll/Myd88 signaling (hardiyanti2026drosophilaasa pages 2-4, maasdorp2026ibinaandibinb pages 12-13, zhang2024maintainingtollsignaling pages 3-6)
- **Metchnikowin**: Another antifungal effector (cammaratamouchtouris2022dynamicregulationof pages 4-6)
- **Defensin**: Induced in certain contexts (cammaratamouchtouris2022dynamicregulationof pages 4-6)
- **Bomanins**: Toll-regulated effector proteins involved in antifungal responses (hardiyanti2026drosophilaasa pages 1-2, hardiyanti2026drosophilaasa pages 6-6)

Myd88-dependent Toll signaling also contributes to melanization responses, resistance to fungal mycotoxins, and coordinated tissue-level immune responses (maasdorp2026ibinaandibinb pages 21-21, hardiyanti2026drosophilaasa pages 6-6).

### Neuronal Function and Survival

Emerging evidence indicates that Myd88 has important functions beyond classical immunity, particularly in **neuronal maintenance and survival** (zhang2024maintainingtollsignaling pages 6-8, zhang2024maintainingtollsignaling pages 1-2, singh2025toll1dependentimmuneevasion pages 16-18, zhang2024maintainingtollsignaling pages 8-10). Myd88 is expressed in PAM dopaminergic neurons, where Toll-1/Myd88-dependent autophagy appears to support neuronal quality control (singh2025toll1dependentimmuneevasion pages 16-18). Disruption of Toll-1 or related pathway components leads to accumulation of P62 and ubiquitinated proteins, loss of dopaminergic neurons, and impaired locomotor function in adult flies (zhang2024maintainingtollsignaling pages 6-8, zhang2024maintainingtollsignaling pages 1-2, zhang2024maintainingtollsignaling pages 10-12).

While direct in vivo evidence that Myd88 loss alone causes dopaminergic neuron death is limited, the protein's established role in Toll-1-dependent autophagy strongly implicates it in the maintenance of neuronal homeostasis (zhang2024maintainingtollsignaling pages 6-8, zhang2024maintainingtollsignaling pages 3-6, zhang2024maintainingtollsignaling pages 8-10). This represents a significant expansion of Myd88 function beyond its canonical immune role.

### Developmental and Tissue Homeostasis Roles

The broader Toll/NF-κB pathway has well-established roles in embryonic dorsal-ventral patterning and tissue homeostasis during development (brutscher2025functionsofdrosophila pages 1-2, lima2021evolutionoftoll pages 19-19, lima2021evolutionoftoll pages 1-2). While Myd88 is a conserved component of Toll signaling and is cited in developmental contexts, direct experimental evidence establishing Myd88-specific requirements for embryonic development, neurogenesis, or developmental pattern formation is limited in the available literature. The protein's involvement in these processes remains to be fully characterized through loss-of-function studies targeting Myd88 specifically rather than upstream Toll receptors or downstream effectors.

## Experimental Evidence

### Genetic and RNAi Studies

The most direct experimental evidence for Myd88 function comes from RNAi knockdown experiments:

1. **Cell culture studies**: In Drosophila S2 cells stably expressing Toll receptor intracellular domains, dsRNA-mediated Myd88 knockdown suppresses Toll-1-induced expression of autophagy genes (*DmAtg8a*, *DmInR*) and antimicrobial peptide genes (*Drs*), demonstrating Myd88's requirement for specific Toll-1 outputs (zhang2024maintainingtollsignaling pages 3-6, zhang2024maintainingtollsignaling pages 6-8).

2. **Tissue-specific knockdown**: Fat-body-specific Myd88 RNAi (using C564>Myd88-IR) has been employed as a Toll-pathway-deficient control in fungal infection experiments, supporting its role in antifungal immunity (maasdorp2026ibinaandibinb pages 12-13).

3. **Requirement for immune responses**: Early genetic studies established that Myd88 is required for responses to fungal and Gram-positive bacterial infections, though the specific experimental approaches (mutants vs. knockdown) used in these foundational studies are cited indirectly in recent reviews (kietz2023drosophilacaspasesas pages 8-8).

### Biochemical Evidence

Biochemical studies have demonstrated:

- **Phosphoinositide binding**: Drosophila Myd88 binds phosphoinositides, a property that regulates its membrane recruitment and controls antibacterial responses (lima2021evolutionoftoll pages 19-19).

- **Death-domain interactions**: The Myd88-Tube-Pelle complex is organized through death-domain-mediated protein-protein interactions, forming a heterotrimeric signaling platform (lima2021evolutionoftoll pages 1-2).

- **TIR-domain interactions**: Myd88 associates with activated Toll receptor TIR domains, linking receptor engagement to downstream signaling (zhang2024maintainingtollsignaling pages 3-6, kietz2023drosophilacaspasesas pages 3-4).

### Structural Evidence

While no experimentally determined full-length structure of *Drosophila* Myd88 is available, structural understanding derives from:

- **Comparative domain analysis**: The TIR domain architecture, death domain organization, and overall modular structure can be inferred from comparative studies of arthropod and mammalian TIR-domain proteins (toshchakov2020asurveyof pages 2-3, toshchakov2020asurveyof pages 1-2, lou2025tirdomainproteins pages 5-6).

- **Conserved motifs**: Analysis of TIR domain sequences identifies conserved Box 1, Box 2, and Box 3 motifs that are critical for signaling function (lou2025tirdomainproteins pages 5-6, liu2021identificationofcore pages 5-9).

## Evolutionary Conservation

Myd88 is an **ancient and broadly conserved intracellular component** of Toll/TLR signaling pathways (lima2021evolutionoftoll pages 10-13, lima2021evolutionoftoll pages 5-7, lima2021evolutionoftoll pages 1-2). A comprehensive survey of 39 insect genomes identified 60 MyD88 sequences, with most insect species possessing a single Myd88 gene, though 11 genomes showed lineage-specific duplications (lima2021evolutionoftoll pages 10-13, lima2021evolutionoftoll pages 13-14, lima2021evolutionoftoll pages 2-3). The median sequence identity among insect Myd88 proteins was 36.88%, indicating moderate conservation across diverse insect lineages (lima2021evolutionoftoll pages 5-7).

The presence of Myd88 in the crustacean *Daphnia pulex* suggests the gene was already present in the ancestral pancrustacean lineage, and the conserved modular architecture of Toll signaling extends to vertebrate TLR pathways, where mammalian MyD88 serves analogous adaptor functions (lima2021evolutionoftoll pages 10-13, lima2021evolutionoftoll pages 1-2, lima2021evolutionoftoll pages 19-19). However, differences in receptor repertoires, copy numbers, and potentially in functional specialization mean that insights from *Drosophila* Myd88 should be cautiously extrapolated to other species.

## Summary Table

| Category | Functional annotation for *Drosophila melanogaster* Myd88 (A1Z7T8) | Evidence and interpretation |
|---|---|---|
| Identity | *Myd88* / CG2078 encodes the *D. melanogaster* MyD88 ortholog, not mammalian MYD88 or a similarly named protein from another insect. Its established function and domain architecture agree with the supplied UniProt record. | Comparative studies identify fly Myd88 as a conserved intracellular Toll-pathway adaptor (lima2021evolutionoftoll pages 1-2, toshchakov2020asurveyof pages 2-3). |
| Primary molecular function | Nonenzymatic signaling adaptor and scaffold coupling activated Toll receptors to the Tube–Pelle module. Because it is not an enzyme, it has no catalytic reaction or substrate specificity. | Myd88 associates with the intracellular Toll-1 TIR region and organizes a Myd88–Tube–Pelle complex (zhang2024maintainingtollsignaling pages 3-6, lima2021evolutionoftoll pages 1-2). |
| TIR domain | Mediates receptor–adaptor and other TIR–TIR associations. The canonical TIR fold has a central five-stranded parallel β-sheet surrounded by α-helices; exposed loops and conserved motifs confer interaction specificity. | Supported by comparative TIR-domain analysis; no experimentally determined full-length fly-Myd88 structure was identified (toshchakov2020asurveyof pages 1-2). |
| Death domain | Protein-interaction module involved in assembly with downstream death-domain proteins, particularly Tube and Pelle. | The Myd88–Tube–Pelle complex is organized through death-domain interactions (lima2021evolutionoftoll pages 1-2). |
| C-terminal localization region | Comparative analysis describes an additional C-terminal localization region in arthropod Myd88-like proteins. Its precise boundaries and isoform-specific conservation in A1Z7T8 remain incompletely characterized. | This is comparative domain inference rather than evidence from a resolved fly-Myd88 structure (toshchakov2020asurveyof pages 2-3). |
| Toll-receptor interaction | After Spätzle-dependent Toll-1 activation, Myd88 associates with the receptor's cytoplasmic TIR domain. Toll-7 can use Myd88 for some outputs, including *Drs* induction, while its autophagy-related signaling is substantially Myd88-independent. | Receptor-specific RNAi experiments distinguish Toll-1 and Toll-7 outputs (zhang2024maintainingtollsignaling pages 3-6, zhang2024maintainingtollsignaling pages 6-8). |
| Tube and Pelle | Myd88 recruits Tube, a signaling scaffold, and Pelle, a serine/threonine kinase related to mammalian IRAKs, forming the principal intracellular Toll signaling complex. | Supported by recent pathway reviews and experimental studies (kietz2023drosophilacaspasesas pages 3-4, zhang2024maintainingtollsignaling pages 3-6). |
| Canonical signaling mechanism | Toll activation → Myd88–Tube–Pelle assembly → Pelle-dependent phosphorylation and degradation of the IκB-like inhibitor Cactus → release and nuclear translocation of Dif and Dorsal. | Myd88 acts upstream of Cactus degradation rather than directly modifying the transcription factors (kietz2023drosophilacaspasesas pages 3-4, cammaratamouchtouris2022dynamicregulationof pages 4-6, lima2021evolutionoftoll pages 1-2). |
| Downstream transcription factors | Dif and Dorsal are the principal downstream NF-κB-family factors; their relative contributions vary by tissue and biological context. | Both are released from Cactus-mediated cytoplasmic inhibition following Toll signaling (zhang2024maintainingtollsignaling pages 3-6, kietz2023drosophilacaspasesas pages 3-4). |
| Innate immunity | Receptor-proximal component of humoral Toll immunity, especially responses to fungi and Gram-positive bacteria. It connects Spätzle–Toll activation to systemic immune-gene expression. | Loss-of-function literature establishes a requirement in fungal and Gram-positive bacterial responses (kietz2023drosophilacaspasesas pages 8-8). |
| Antimicrobial outputs | Promotes expression of *Drosomycin* (*Drs*); broader Toll/NF-κB outputs include *Metchnikowin* and context-dependent *Defensin*. These genes are downstream transcriptional outputs, not direct Myd88-binding partners. | Myd88 RNAi reduces *Drs* induction, while broader Toll target programs include these antimicrobial genes (zhang2024maintainingtollsignaling pages 3-6, cammaratamouchtouris2022dynamicregulationof pages 4-6). |
| Autophagy | Selectively transmits Toll-1 signals that increase *DmAtg8a* and *DmInR* expression and promote autophagic responses. Toll-7 activates related outputs through a substantially Myd88-independent mechanism. | In S2 cells, Myd88 RNAi suppresses Toll-1-induced gene expression, LC3-II accumulation, P62 reduction, and associated autophagy responses (zhang2024maintainingtollsignaling pages 3-6, zhang2024maintainingtollsignaling pages 6-8). |
| Neuronal survival | Toll-dependent autophagy supports adult dopaminergic neurons and locomotor function. Myd88 is implicated through Toll-1, but direct in-vivo evidence that Myd88 loss alone causes dopamine-neuron death is weaker than the receptor- and PP2A-level evidence. | Toll-1, Toll-7, or PP2A disruption causes P62 accumulation, dopamine-neuron loss, and locomotor defects (zhang2024maintainingtollsignaling pages 6-8, zhang2024maintainingtollsignaling pages 1-2, zhang2024maintainingtollsignaling pages 8-10). |
| Subcellular localization | Intracellular, predominantly cytoplasmic adaptor operating on the cytosolic face of activated Toll receptors. It can be recruited to phosphoinositide-containing membranes but is not an integral membrane or secreted protein. | Functional localization follows from receptor-TIR binding; phosphoinositide binding supports regulated membrane association (lima2021evolutionoftoll pages 1-2, lima2021evolutionoftoll pages 19-19, zhang2024maintainingtollsignaling pages 3-6). |
| RNAi evidence | dsRNA depletion in S2 cells reduces Toll-1-dependent autophagy-related expression and suppresses *Drs* induction downstream of TIR-1 and TIR-7. Fat-body Myd88 RNAi has also served as a Toll-deficient control in fungal-infection experiments. | Direct perturbational evidence shows that Myd88 dependence varies with receptor and output (zhang2024maintainingtollsignaling pages 3-6, maasdorp2026ibinaandibinb pages 12-13). |
| Biochemical and structural evidence | TIR-mediated receptor association, death-domain complex formation, and phosphoinositide-dependent recruitment support a scaffold mechanism. Structural conclusions remain largely comparative. | Evidence integrates TIR-fold analysis with signaling-complex and membrane-recruitment studies (toshchakov2020asurveyof pages 2-3, toshchakov2020asurveyof pages 1-2, lima2021evolutionoftoll pages 19-19). |
| Evolution | Myd88 is an ancient, broadly conserved intracellular Toll-pathway component. A survey of 39 insect genomes recovered 60 candidate Myd88 proteins; median identity among analyzed insect Myd88 sequences was 36.88%, and 11 genomes showed expansions. | Conservation supports the core adaptor annotation, although lineage-specific duplication cautions against transferring every fly function to other insects (lima2021evolutionoftoll pages 10-13, lima2021evolutionoftoll pages 5-7, lima2021evolutionoftoll pages 2-3). |
| Isoforms and uncertainty | UniProt A1Z7T8 reports isoforms A, B, and C, but the reviewed literature did not resolve isoform-specific localization, partners, or functions. Current conclusions should therefore be applied to Myd88 generally rather than to an individual isoform. | No isoform-specific experimental evidence was recovered in the reviewed sources. |


*Table: This table summarizes the identity, molecular function, domains, interaction network, localization, biological roles, and experimental support for Drosophila melanogaster Myd88 (A1Z7T8). It also distinguishes well-supported functions from comparative inferences and unresolved isoform-specific questions.*

## Current Understanding and Research Gaps

The current literature provides strong evidence for Myd88's core function as a Toll pathway adaptor coupling receptor activation to downstream NF-κB signaling and antimicrobial peptide production. Recent work has significantly expanded understanding by revealing receptor-specific signaling requirements and a new role in autophagy regulation and neuronal maintenance.

Key remaining questions include:

1. **Isoform-specific functions**: The three annotated isoforms (A, B, C) have not been functionally characterized; their tissue distribution, interaction partners, and biological roles remain unknown.

2. **Structural biology**: A full-length experimentally determined structure would clarify domain organization, interaction surfaces, and conformational changes during signaling.

3. **Developmental roles**: While the broader Toll pathway functions in development, Myd88-specific requirements in embryonic patterning, neurogenesis, or tissue homeostasis need direct experimental validation.

4. **Molecular mechanisms of receptor specificity**: The basis for differential Myd88 dependence between Toll-1 and Toll-7 signaling, and the identity of potential alternative adaptors, requires further investigation.

5. **In vivo neuronal function**: Direct assessment of neuronal phenotypes in Myd88 loss-of-function animals would strengthen conclusions about its role in dopaminergic neuron survival.

## Publication Dates and Sources

This report draws primarily on authoritative peer-reviewed publications from 2020-2026, including:

- Zhang et al. (2024), iScience: Toll signaling and autophagy in dopamine neuron survival
- Singh et al. (2025), PLOS Biology: Toll-1-dependent immune responses and neurodegeneration  
- Maasdorp et al. (2026), BMC Biology: Toll pathway regulation by Ibin proteins
- Kietz & Meinander (2023), Cell Death and Differentiation: Drosophila caspases in host-microbe interactions
- Lima et al. (2021), BMC Genomics: Evolution of Toll, Spatzle and MyD88 in insects
- Toshchakov & Neuwald (2020), Immunogenetics: Survey of TIR domain divergence
- Multiple recent reviews on Toll/NF-κB signaling, TIR domain proteins, and Drosophila immunity (2020-2026)

These sources represent high-quality peer-reviewed research from journals including Cell Death and Differentiation, BMC Biology, iScience, PLOS Biology, Frontiers in Immunology, and other domain-leading publications, ensuring the reliability and currency of the functional annotations provided.

References

1. (lima2021evolutionoftoll pages 1-2): Letícia Ferreira Lima, André Quintanilha Torres, Rodrigo Jardim, Rafael Dias Mesquita, and Renata Schama. Evolution of toll, spatzle and myd88 in insects: the problem of the diptera bias. BMC Genomics, Jul 2021. URL: https://doi.org/10.1186/s12864-021-07886-7, doi:10.1186/s12864-021-07886-7. This article has 39 citations and is from a peer-reviewed journal.

2. (lima2021evolutionoftoll pages 19-19): Letícia Ferreira Lima, André Quintanilha Torres, Rodrigo Jardim, Rafael Dias Mesquita, and Renata Schama. Evolution of toll, spatzle and myd88 in insects: the problem of the diptera bias. BMC Genomics, Jul 2021. URL: https://doi.org/10.1186/s12864-021-07886-7, doi:10.1186/s12864-021-07886-7. This article has 39 citations and is from a peer-reviewed journal.

3. (zhang2024maintainingtollsignaling pages 3-6): Jie Zhang, Ting Tang, Ruonan Zhang, Liang Wen, Xiaojuan Deng, Xiaoxia Xu, Wanying Yang, Fengliang Jin, Yang Cao, Yuzhen Lu, and Xiao-Qiang Yu. Maintaining toll signaling in drosophila brain is required to sustain autophagy for dopamine neuron survival. iScience, 27:108795, Feb 2024. URL: https://doi.org/10.1016/j.isci.2024.108795, doi:10.1016/j.isci.2024.108795. This article has 15 citations and is from a peer-reviewed journal.

4. (kietz2023drosophilacaspasesas pages 3-4): Christa Kietz and Annika Meinander. Drosophila caspases as guardians of host-microbe interactions. Cell Death and Differentiation, 30:227-236, Jul 2023. URL: https://doi.org/10.1038/s41418-022-01038-4, doi:10.1038/s41418-022-01038-4. This article has 24 citations and is from a domain leading peer-reviewed journal.

5. (cammaratamouchtouris2022dynamicregulationof pages 4-6): Alexandre Cammarata-Mouchtouris, Adrian Acker, Akira Goto, Di Chen, Nicolas Matt, and Vincent Leclerc. Dynamic regulation of nf-κb response in innate immunity: the case of the imd pathway in drosophila. Biomedicines, 10:2304, Sep 2022. URL: https://doi.org/10.3390/biomedicines10092304, doi:10.3390/biomedicines10092304. This article has 48 citations.

6. (toshchakov2020asurveyof pages 2-3): Vladimir Y. Toshchakov and Andrew F. Neuwald. A survey of tir domain sequence and structure divergence. Immunogenetics, 72:181-203, Jan 2020. URL: https://doi.org/10.1007/s00251-020-01157-7, doi:10.1007/s00251-020-01157-7. This article has 65 citations and is from a peer-reviewed journal.

7. (toshchakov2020asurveyof pages 1-2): Vladimir Y. Toshchakov and Andrew F. Neuwald. A survey of tir domain sequence and structure divergence. Immunogenetics, 72:181-203, Jan 2020. URL: https://doi.org/10.1007/s00251-020-01157-7, doi:10.1007/s00251-020-01157-7. This article has 65 citations and is from a peer-reviewed journal.

8. (lou2025tirdomainproteins pages 5-6): Jiatian Lou, Chenlei Gong, Xiaotao Gao, Jiaren Zhou, Qiyuan Wu, Xiaoliang Zheng, and Liyan Cheng. Tir domain proteins: regulatory mechanisms in the tumor immune microenvironment, clinical translation strategies, and prospects for precision therapy applications. Frontiers in Immunology, Dec 2025. URL: https://doi.org/10.3389/fimmu.2025.1695754, doi:10.3389/fimmu.2025.1695754. This article has 4 citations and is from a peer-reviewed journal.

9. (liu2021identificationofcore pages 5-9): Long Liu, Yu-Shan Wei, and Dun Wang. Identification of core genes of toll-like receptor pathway from lymantria dispar and induced expression upon immune stimulant. Sep 2021. URL: https://doi.org/10.3390/insects12090827, doi:10.3390/insects12090827. This article has 6 citations.

10. (singh2025toll1dependentimmuneevasion pages 18-19): Deepanshu N. D. Singh, Abigail R. E. Roberts, Xiaocui Wang, Guiyi Li, Enrique Quesada Moraga, David Alliband, Elizabeth Ballou, Hung-Ji Tsai, and Alicia Hidalgo. Toll-1-dependent immune evasion induced by fungal infection leads to cell loss in the drosophila brain. Feb 2025. URL: https://doi.org/10.1371/journal.pbio.3003020, doi:10.1371/journal.pbio.3003020. This article has 10 citations and is from a highest quality peer-reviewed journal.

11. (singh2025toll1dependentimmuneevasion pages 16-18): Deepanshu N. D. Singh, Abigail R. E. Roberts, Xiaocui Wang, Guiyi Li, Enrique Quesada Moraga, David Alliband, Elizabeth Ballou, Hung-Ji Tsai, and Alicia Hidalgo. Toll-1-dependent immune evasion induced by fungal infection leads to cell loss in the drosophila brain. Feb 2025. URL: https://doi.org/10.1371/journal.pbio.3003020, doi:10.1371/journal.pbio.3003020. This article has 10 citations and is from a highest quality peer-reviewed journal.

12. (kietz2023drosophilacaspasesas pages 8-8): Christa Kietz and Annika Meinander. Drosophila caspases as guardians of host-microbe interactions. Cell Death and Differentiation, 30:227-236, Jul 2023. URL: https://doi.org/10.1038/s41418-022-01038-4, doi:10.1038/s41418-022-01038-4. This article has 24 citations and is from a domain leading peer-reviewed journal.

13. (hardiyanti2026drosophilaasa pages 1-2): Widya Hardiyanti, Muhammad Rasul Pratama, Emil Salim, and Firzan Nainu. Drosophila as a host model to investigate toll-mediated innate immune evasion of human pathogenic fungi. Frontiers in Cellular and Infection Microbiology, Jul 2026. URL: https://doi.org/10.3389/fcimb.2026.1853190, doi:10.3389/fcimb.2026.1853190. This article has 0 citations.

14. (hardiyanti2026drosophilaasa pages 2-4): Widya Hardiyanti, Muhammad Rasul Pratama, Emil Salim, and Firzan Nainu. Drosophila as a host model to investigate toll-mediated innate immune evasion of human pathogenic fungi. Frontiers in Cellular and Infection Microbiology, Jul 2026. URL: https://doi.org/10.3389/fcimb.2026.1853190, doi:10.3389/fcimb.2026.1853190. This article has 0 citations.

15. (zhang2024maintainingtollsignaling pages 6-8): Jie Zhang, Ting Tang, Ruonan Zhang, Liang Wen, Xiaojuan Deng, Xiaoxia Xu, Wanying Yang, Fengliang Jin, Yang Cao, Yuzhen Lu, and Xiao-Qiang Yu. Maintaining toll signaling in drosophila brain is required to sustain autophagy for dopamine neuron survival. iScience, 27:108795, Feb 2024. URL: https://doi.org/10.1016/j.isci.2024.108795, doi:10.1016/j.isci.2024.108795. This article has 15 citations and is from a peer-reviewed journal.

16. (zhang2024maintainingtollsignaling pages 10-12): Jie Zhang, Ting Tang, Ruonan Zhang, Liang Wen, Xiaojuan Deng, Xiaoxia Xu, Wanying Yang, Fengliang Jin, Yang Cao, Yuzhen Lu, and Xiao-Qiang Yu. Maintaining toll signaling in drosophila brain is required to sustain autophagy for dopamine neuron survival. iScience, 27:108795, Feb 2024. URL: https://doi.org/10.1016/j.isci.2024.108795, doi:10.1016/j.isci.2024.108795. This article has 15 citations and is from a peer-reviewed journal.

17. (zhang2024maintainingtollsignaling pages 1-2): Jie Zhang, Ting Tang, Ruonan Zhang, Liang Wen, Xiaojuan Deng, Xiaoxia Xu, Wanying Yang, Fengliang Jin, Yang Cao, Yuzhen Lu, and Xiao-Qiang Yu. Maintaining toll signaling in drosophila brain is required to sustain autophagy for dopamine neuron survival. iScience, 27:108795, Feb 2024. URL: https://doi.org/10.1016/j.isci.2024.108795, doi:10.1016/j.isci.2024.108795. This article has 15 citations and is from a peer-reviewed journal.

18. (zhang2024maintainingtollsignaling pages 8-10): Jie Zhang, Ting Tang, Ruonan Zhang, Liang Wen, Xiaojuan Deng, Xiaoxia Xu, Wanying Yang, Fengliang Jin, Yang Cao, Yuzhen Lu, and Xiao-Qiang Yu. Maintaining toll signaling in drosophila brain is required to sustain autophagy for dopamine neuron survival. iScience, 27:108795, Feb 2024. URL: https://doi.org/10.1016/j.isci.2024.108795, doi:10.1016/j.isci.2024.108795. This article has 15 citations and is from a peer-reviewed journal.

19. (maasdorp2026ibinaandibinb pages 12-13): Matthew K. Maasdorp, Susanna Valanne, Laura Vesala, Petra Vornanen, Elina Haukkavaara, Tea Tuomela, Aino Malin, Tiina S. Salminen, Dan Hultmark, and Mika Rämet. Ibina and ibinb regulate the toll pathway-mediated immune response in drosophila melanogaster. BMC Biology, Jan 2026. URL: https://doi.org/10.1186/s12915-025-02501-7, doi:10.1186/s12915-025-02501-7. This article has 3 citations and is from a domain leading peer-reviewed journal.

20. (hardiyanti2026drosophilaasa pages 6-6): Widya Hardiyanti, Muhammad Rasul Pratama, Emil Salim, and Firzan Nainu. Drosophila as a host model to investigate toll-mediated innate immune evasion of human pathogenic fungi. Frontiers in Cellular and Infection Microbiology, Jul 2026. URL: https://doi.org/10.3389/fcimb.2026.1853190, doi:10.3389/fcimb.2026.1853190. This article has 0 citations.

21. (maasdorp2026ibinaandibinb pages 21-21): Matthew K. Maasdorp, Susanna Valanne, Laura Vesala, Petra Vornanen, Elina Haukkavaara, Tea Tuomela, Aino Malin, Tiina S. Salminen, Dan Hultmark, and Mika Rämet. Ibina and ibinb regulate the toll pathway-mediated immune response in drosophila melanogaster. BMC Biology, Jan 2026. URL: https://doi.org/10.1186/s12915-025-02501-7, doi:10.1186/s12915-025-02501-7. This article has 3 citations and is from a domain leading peer-reviewed journal.

22. (brutscher2025functionsofdrosophila pages 1-2): Fabienne Brutscher and Konrad Basler. Functions of drosophila toll/nf-κb signaling in imaginal tissue homeostasis and cancer. Frontiers in Cell and Developmental Biology, Mar 2025. URL: https://doi.org/10.3389/fcell.2025.1559753, doi:10.3389/fcell.2025.1559753. This article has 4 citations.

23. (lima2021evolutionoftoll pages 10-13): Letícia Ferreira Lima, André Quintanilha Torres, Rodrigo Jardim, Rafael Dias Mesquita, and Renata Schama. Evolution of toll, spatzle and myd88 in insects: the problem of the diptera bias. BMC Genomics, Jul 2021. URL: https://doi.org/10.1186/s12864-021-07886-7, doi:10.1186/s12864-021-07886-7. This article has 39 citations and is from a peer-reviewed journal.

24. (lima2021evolutionoftoll pages 5-7): Letícia Ferreira Lima, André Quintanilha Torres, Rodrigo Jardim, Rafael Dias Mesquita, and Renata Schama. Evolution of toll, spatzle and myd88 in insects: the problem of the diptera bias. BMC Genomics, Jul 2021. URL: https://doi.org/10.1186/s12864-021-07886-7, doi:10.1186/s12864-021-07886-7. This article has 39 citations and is from a peer-reviewed journal.

25. (lima2021evolutionoftoll pages 13-14): Letícia Ferreira Lima, André Quintanilha Torres, Rodrigo Jardim, Rafael Dias Mesquita, and Renata Schama. Evolution of toll, spatzle and myd88 in insects: the problem of the diptera bias. BMC Genomics, Jul 2021. URL: https://doi.org/10.1186/s12864-021-07886-7, doi:10.1186/s12864-021-07886-7. This article has 39 citations and is from a peer-reviewed journal.

26. (lima2021evolutionoftoll pages 2-3): Letícia Ferreira Lima, André Quintanilha Torres, Rodrigo Jardim, Rafael Dias Mesquita, and Renata Schama. Evolution of toll, spatzle and myd88 in insects: the problem of the diptera bias. BMC Genomics, Jul 2021. URL: https://doi.org/10.1186/s12864-021-07886-7, doi:10.1186/s12864-021-07886-7. This article has 39 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Myd88-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. lima2021evolutionoftoll pages 1-2
2. toshchakov2020asurveyof pages 2-3
3. lima2021evolutionoftoll pages 19-19
4. hardiyanti2026drosophilaasa pages 2-4
5. kietz2023drosophilacaspasesas pages 3-4
6. zhang2024maintainingtollsignaling pages 6-8
7. zhang2024maintainingtollsignaling pages 10-12
8. cammaratamouchtouris2022dynamicregulationof pages 4-6
9. maasdorp2026ibinaandibinb pages 12-13
10. kietz2023drosophilacaspasesas pages 8-8
11. lima2021evolutionoftoll pages 5-7
12. toshchakov2020asurveyof pages 1-2
13. zhang2024maintainingtollsignaling pages 3-6
14. lou2025tirdomainproteins pages 5-6
15. liu2021identificationofcore pages 5-9
16. hardiyanti2026drosophilaasa pages 1-2
17. zhang2024maintainingtollsignaling pages 1-2
18. zhang2024maintainingtollsignaling pages 8-10
19. hardiyanti2026drosophilaasa pages 6-6
20. maasdorp2026ibinaandibinb pages 21-21
21. brutscher2025functionsofdrosophila pages 1-2
22. lima2021evolutionoftoll pages 10-13
23. lima2021evolutionoftoll pages 13-14
24. lima2021evolutionoftoll pages 2-3
25. https://doi.org/10.1186/s12864-021-07886-7,
26. https://doi.org/10.1016/j.isci.2024.108795,
27. https://doi.org/10.1038/s41418-022-01038-4,
28. https://doi.org/10.3390/biomedicines10092304,
29. https://doi.org/10.1007/s00251-020-01157-7,
30. https://doi.org/10.3389/fimmu.2025.1695754,
31. https://doi.org/10.3390/insects12090827,
32. https://doi.org/10.1371/journal.pbio.3003020,
33. https://doi.org/10.3389/fcimb.2026.1853190,
34. https://doi.org/10.1186/s12915-025-02501-7,
35. https://doi.org/10.3389/fcell.2025.1559753,