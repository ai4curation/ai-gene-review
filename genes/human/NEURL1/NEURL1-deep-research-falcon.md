---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-30T05:25:23.597072'
end_time: '2026-09-30T05:40:55.064507'
duration_seconds: 931.47
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: NEURL1
  gene_symbol: NEURL1
  uniprot_accession: O76050
  protein_description: 'RecName: Full=E3 ubiquitin-protein ligase NEURL1; EC=2.3.2.27;
    AltName: Full=Neuralized-like protein 1A; Short=h-neu; Short=h-neuralized 1; AltName:
    Full=RING finger protein 67; AltName: Full=RING-type E3 ubiquitin transferase
    NEURL1 {ECO:0000305};'
  gene_info: Name=NEURL1; Synonyms=NEURL, NEURL1A, RNF67;
  organism_full: Homo sapiens (Human).
  protein_family: Not specified in UniProt
  protein_domains: B30.2/SPRY_sf. (IPR043136); Neuralized. (IPR037962); NHR_dom. (IPR006573);
    Znf_RING. (IPR001841); Znf_RING/FYVE/PHD. (IPR013083)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 28
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: NEURL1-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** O76050
- **Protein Description:** RecName: Full=E3 ubiquitin-protein ligase NEURL1; EC=2.3.2.27; AltName: Full=Neuralized-like protein 1A; Short=h-neu; Short=h-neuralized 1; AltName: Full=RING finger protein 67; AltName: Full=RING-type E3 ubiquitin transferase NEURL1 {ECO:0000305};
- **Gene Information:** Name=NEURL1; Synonyms=NEURL, NEURL1A, RNF67;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** B30.2/SPRY_sf. (IPR043136); Neuralized. (IPR037962); NHR_dom. (IPR006573); Znf_RING. (IPR001841); Znf_RING/FYVE/PHD. (IPR013083)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "NEURL1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'NEURL1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **NEURL1** (gene ID: NEURL1, UniProt: O76050) in human.

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
- **UniProt Accession:** O76050
- **Protein Description:** RecName: Full=E3 ubiquitin-protein ligase NEURL1; EC=2.3.2.27; AltName: Full=Neuralized-like protein 1A; Short=h-neu; Short=h-neuralized 1; AltName: Full=RING finger protein 67; AltName: Full=RING-type E3 ubiquitin transferase NEURL1 {ECO:0000305};
- **Gene Information:** Name=NEURL1; Synonyms=NEURL, NEURL1A, RNF67;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** B30.2/SPRY_sf. (IPR043136); Neuralized. (IPR037962); NHR_dom. (IPR006573); Znf_RING. (IPR001841); Znf_RING/FYVE/PHD. (IPR013083)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "NEURL1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'NEURL1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **NEURL1** (gene ID: NEURL1, UniProt: O76050) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Comprehensive Research Report on NEURL1 (E3 Ubiquitin-Protein Ligase NEURL1)

## Gene Identity and Overview

NEURL1 (Neuralized E3 Ubiquitin Protein Ligase 1, also known as NEURL, NEURL1A, or RNF67; UniProt: O76050) encodes a RING-type E3 ubiquitin ligase in humans that regulates multiple cellular processes through substrate-specific ubiquitination (taal2019neuralizedfamilymember pages 1-2). The protein is the mammalian ortholog of Drosophila Neuralized, a well-characterized developmental regulator originally identified for its role in neurogenesis (taal2019neuralizedfamilymember pages 1-2).

## Structural Organization and Catalytic Mechanism

### Domain Architecture

NEURL1 contains a modular domain architecture consisting of two Neuralized Homology Repeat (NHR) domains at the N-terminus and a C3HC4 RING zinc-finger domain at the C-terminus (taal2019neuralizedfamilymember pages 1-2, seib2021theroleof pages 8-9). These domains have distinct and separable functions: the NHR domains (NHR1 and NHR2) mediate substrate recognition and binding, while the RING domain provides the catalytic E3 ubiquitin ligase activity (taal2019neuralizedfamilymember pages 3-4, taal2019neuralizedfamilymember pages 8-9). Both NHR domains can independently interact with substrates such as PDE9A, demonstrating functional redundancy in substrate engagement (taal2019neuralizedfamilymember pages 3-4). The RING domain is essential for enzymatic activity, as RING-mutant forms of NEURL1 lose ubiquitin ligase function despite retaining substrate-binding capability (taal2019neuralizedfamilymember pages 4-6, taal2019neuralizedfamilymember pages 8-9).

The N-terminal region contains a basic polybasic motif (KKIKKR in Drosophila Neuralized) that supports plasma membrane association through phospholipid binding (seib2021theroleof pages 8-9). Additionally, N-myristoylation serves as a post-translational modification that targets NEURL1 to the plasma membrane, though both myristoylated and non-myristoylated forms can associate with cellular membranes (taal2019neuralizedfamilymember pages 2-3).

### Catalytic Mechanism and Substrate Specificity

As a RING-type E3 ubiquitin ligase, NEURL1 catalyzes the transfer of ubiquitin from E2 ubiquitin-conjugating enzymes to lysine residues on target substrates (taal2019neuralizedfamilymember pages 1-2). Importantly, NEURL1 exhibits substrate-specific ubiquitination patterns that determine distinct functional outcomes:

**Substrate Specificity Summary:**

| Substrate name | Ubiquitination type (mono vs. poly) | Ubiquitin linkage type | Functional outcome | Key citation |
|---|---|---|---|---|
| Notch ligand Delta/Delta-like proteins | Predominantly monoubiquitination or multi-monoubiquitination; direct evidence is strongest for Drosophila Neuralized, while mammalian NEURL1-specific evidence is less conclusive | Specific chain linkage not established; lysines in the ligand intracellular domain serve as acceptors | Promotes ligand internalization and force-generating endocytosis in the signal-sending cell, facilitating Notch activation in the adjacent cell. Neuralized can also act as an endocytic adaptor, and its catalytic activity enhances—but may not always be essential for—Delta signaling. | (kalodimou2023separablerolesfor pages 17-19, kalodimou2023separablerolesfor pages 1-2, bray2025modesofnotch pages 27-33, kalodimou2023separablerolesfor pages 14-15) |
| Jagged1 (JAG1), a mammalian Notch ligand | Reported monoubiquitination | Specific acceptor lysine and chain linkage not established | Promotes Jagged1 endocytosis and turnover, thereby modifying Jagged1–Notch1 signaling, Notch intracellular-domain production, and downstream outputs such as **HES1** and **HEY1**. | (chen2022theroleof pages 8-10, dutta2022regulationofnotch pages 15-17, taal2019neuralizedfamilymember pages 10-11) |
| CPEB3 | Monoubiquitination; non-proteolytic | Not applicable as a polyubiquitin-chain linkage; the modified CPEB3 residue is not firmly defined | Switches CPEB3 from basal translational repression toward activation, promoting polyadenylation and translation of **GRIA1/GluA1** and **GRIA2/GluA2** mRNAs and supporting synaptic plasticity and memory-related protein synthesis. | (qu2020roleofcpeb3 pages 4-7, qu2020roleofcpeb3 pages 7-8, lee2020neur1andneur2 pages 1-2) |
| PDE9A | Polyubiquitination | K27-, K29-, and K33-linked chains; K27 appears especially important for degradation | Targets PDE9A for proteasome-mediated degradation rather than lysosomal turnover, potentially decreasing cGMP hydrolysis. Substrate interaction is mediated by NEURL1 NHR domains, whereas ubiquitination requires an intact RING domain. | (taal2019neuralizedfamilymember pages 8-9, taal2019neuralizedfamilymember pages 4-6, taal2019neuralizedfamilymember pages 9-10, taal2019neuralizedfamilymember pages 3-4) |


*Table: Comparison of experimentally reported NEURL1 substrates, ubiquitin modifications, and functional consequences. The table distinguishes direct human or mammalian evidence from findings based chiefly on Drosophila Neuralized.*

The biochemical reaction catalyzed by NEURL1 involves the E2-dependent transfer of activated ubiquitin to substrate proteins, producing either monoubiquitination (single ubiquitin attachment) or polyubiquitination (ubiquitin chain formation) depending on the substrate and cellular context (taal2019neuralizedfamilymember pages 1-2). For PDE9A, NEURL1 specifically promotes polyubiquitin chains linked through lysine residues K27, K29, and K33 of ubiquitin itself, with K27-linked chains being particularly important for proteasomal degradation (taal2019neuralizedfamilymember pages 8-9, taal2019neuralizedfamilymember pages 4-6, taal2019neuralizedfamilymember pages 6-6).

## Subcellular Localization

NEURL1 exhibits a dual subcellular distribution, localizing to both the cytoplasm and plasma membrane (taal2019neuralizedfamilymember pages 2-3, taal2019neuralizedfamilymember pages 8-9). The protein is found predominantly in the cytoplasm, with a smaller fraction associated with cell membranes (taal2019neuralizedfamilymember pages 8-9, taal2019neuralizedfamilymember pages 3-4). This distribution is regulated by N-terminal myristoylation, which promotes membrane targeting (taal2019neuralizedfamilymember pages 2-3, taal2019neuralizedfamilymember pages 1-2).

In neurons, NEURL1 mRNA is specifically targeted to dendrites in the adult rat dentate gyrus, suggesting local protein synthesis and function in dendritic compartments (taal2019neuralizedfamilymember pages 1-2). The subcellular localization appears context-dependent: NEURL1 functions at the plasma membrane when regulating Notch ligands (promoting ligand endocytosis), and in the cytoplasm when ubiquitinating soluble substrates like PDE9A and CPEB3 (taal2019neuralizedfamilymember pages 2-3, taal2019neuralizedfamilymember pages 3-4).

## Primary Functions and Biochemical Pathways

### 1. Notch Signaling Pathway

NEURL1 plays a critical role in Notch signaling by regulating Notch ligand trafficking and activation in the signal-sending cell. The protein ubiquitinates Notch ligands including Delta, Delta-like proteins, and Jagged1, promoting their endocytosis (taal2019neuralizedfamilymember pages 1-2, dutta2022regulationofnotch pages 15-17, bray2025modesofnotch pages 27-33). This ligand endocytosis is mechanistically important because it generates the mechanical pulling force required to expose the Notch receptor's negative regulatory region in the receiving cell, enabling proteolytic activation by ADAM10 and γ-secretase to release the Notch intracellular domain (NICD) (bray2025modesofnotch pages 27-33).

For mammalian NEURL1 specifically, N-myristoylation targets the protein to the plasma membrane where it ubiquitinates Jagged1, promoting Jagged1 endocytosis and degradation, thereby regulating Jagged1-Notch1 signaling and downstream transcriptional targets including HES1 and HEY1 (chen2022theroleof pages 8-10, dutta2022regulationofnotch pages 15-17).

Recent evidence from Drosophila suggests that Neuralized functions both as a ubiquitin ligase and as an endocytic adaptor, with these activities being separable: the Delta-Neuralized interaction and complex formation is essential for signaling, while ubiquitination enhances but is not absolutely required for ligand activation (kalodimou2023separablerolesfor pages 17-19, kalodimou2023separablerolesfor pages 1-2, kalodimou2023separablerolesfor pages 14-15). This dual function may also apply to mammalian NEURL1, though direct evidence is more limited.

### 2. Synaptic Plasticity and Memory Pathway

NEURL1 regulates synaptic plasticity and memory formation through monoubiquitination of CPEB3 (Cytoplasmic Polyadenylation Element Binding Protein 3) (qu2020roleofcpeb3 pages 4-7, qu2020roleofcpeb3 pages 7-8). CPEB3 normally functions as a translational repressor in its basal state, maintaining plasticity-related mRNAs in a dormant, non-translated state. NEURL1-mediated monoubiquitination converts CPEB3 from a translational repressor to an activator (qu2020roleofcpeb3 pages 4-7, kozlov2021theroleof pages 7-9).

The molecular mechanism involves NEURL1 interaction with the N-terminal prion-like domain of CPEB3, inducing ubiquitination that promotes CPEB3 aggregation and association with polysomes (qu2020roleofcpeb3 pages 7-8). Activated CPEB3 then promotes polyadenylation and translation of specific mRNA targets, most notably GRIA1 and GRIA2, which encode the GluA1 and GluA2 subunits of AMPA receptors (qu2020roleofcpeb3 pages 4-7, qu2020roleofcpeb3 pages 7-8). This increases AMPA receptor abundance at synapses, strengthening synaptic transmission and supporting activity-dependent synaptic remodeling.

This modification is activity-dependent: neural activity and NMDA receptor signaling promote CPEB3 aggregation and NEURL1-dependent activation (qu2020roleofcpeb3 pages 4-7, kozlov2021theroleof pages 7-9). The modification also affects dendritic spine formation and synaptic protein composition, providing cellular mechanisms for long-term memory encoding (qu2020roleofcpeb3 pages 7-8, kozlov2021theroleof pages 7-9).

### 3. cGMP Signaling Regulation

NEURL1 regulates intracellular cGMP signaling by controlling the stability of PDE9A (phosphodiesterase 9A), a cGMP-specific phosphodiesterase with the highest affinity for cGMP among known phosphodiesterases (taal2019neuralizedfamilymember pages 3-4, taal2019neuralizedfamilymember pages 1-2). NEURL1 interacts with PDE9A through both NHR domains, binding to both the catalytic and regulatory regions of PDE9A (taal2019neuralizedfamilymember pages 8-9, taal2019neuralizedfamilymember pages 3-4).

Unlike its non-proteolytic monoubiquitination of CPEB3, NEURL1 promotes polyubiquitination of PDE9A, targeting it for proteasome-mediated degradation rather than lysosomal degradation (taal2019neuralizedfamilymember pages 8-9, taal2019neuralizedfamilymember pages 9-10, taal2019neuralizedfamilymember pages 6-8). The polyubiquitin chains are linked through K27, K29, and K33 of ubiquitin, with K27 linkages being particularly important for degradation (taal2019neuralizedfamilymember pages 8-9, taal2019neuralizedfamilymember pages 4-6, taal2019neuralizedfamilymember pages 6-6). This degradation reduces PDE9A protein levels, potentially decreasing cGMP hydrolysis and increasing cellular cGMP availability, though the downstream physiological consequences require further investigation (taal2019neuralizedfamilymember pages 1-2, taal2019neuralizedfamilymember pages 8-9).

NEURL1 also influences PDE9A subcellular distribution, shifting it from predominantly membrane-associated localization toward the cytoplasm (taal2019neuralizedfamilymember pages 8-9, taal2019neuralizedfamilymember pages 3-4).

## Biological Processes and Physiological Roles

### Hippocampus-Dependent Spatial Memory and Long-Term Potentiation

Genetic studies in mice provide strong evidence for NEURL1's role in hippocampus-dependent memory and synaptic plasticity. However, NEURL1 functions redundantly with its paralog NEURL2, such that single knockout of either gene does not produce overt memory deficits (lee2020neur1andneur2 pages 1-2, lee2020neur1andneur2 pages 6-8). Double knockout mice lacking both Neur1 and Neur2 show clear impairments in spatial memory tasks including the Morris water maze and object-location memory, with reduced platform crossings, longer escape latencies, and lower discrimination indices (lee2020neur1andneur2 pages 6-8, lee2020neur1andneur2 pages 2-3).

Electrophysiological studies demonstrate that basal synaptic transmission and early-phase LTP remain intact in double knockout mice, but protein synthesis-dependent late-phase LTP is specifically impaired (lee2020neur1andneur2 pages 1-2, lee2020neur1andneur2 pages 6-8). This selective deficit in late LTP is consistent with NEURL1's role in regulating CPEB3-dependent translation of synaptic proteins. The requirement for both NEURL1 and NEURL2 suggests functional redundancy or compensation between the two paralogs in the hippocampus (lee2020neur1andneur2 pages 1-2, lee2020neur1andneur2 pages 2-3).

### Neurogenesis and Development

Through its regulation of Notch signaling, NEURL1 is implicated in neurogenesis and neural development. In Drosophila, loss of Neuralized causes neural hyperplasia at the expense of epidermal tissue, establishing it as a neurogenic regulator (taal2019neuralizedfamilymember pages 1-2). However, mammalian studies indicate that NEURL1 and NEURL1B are not strictly required for canonical Notch signaling during development, suggesting functional compensation by other E3 ligases such as Mind bomb (Mib1) or context-dependent requirements (taal2019neuralizedfamilymember pages 2-3, taal2019neuralizedfamilymember pages 1-2).

### Expression Patterns

NEURL1 is highly expressed in adult brain regions including the hippocampus, cortex, cerebellum, olfactory bulb, and forebrain (taal2019neuralizedfamilymember pages 8-9). This neuronal expression pattern supports its roles in synaptic plasticity, memory formation, and potentially adult neurogenesis. PDE9A, one of its key substrates, shows overlapping expression in these same neural regions (taal2019neuralizedfamilymember pages 2-3).

## Disease Associations and Clinical Relevance

While NEURL1 has been studied in various disease contexts, definitive causal relationships remain to be fully established. The NEURL1 locus (10q25.1) has been identified in malignant astrocytoma deletion regions, suggesting potential involvement in glioma biology, though direct evidence for tumor suppressor function is limited (taal2019neuralizedfamilymember pages 10-11).

Recent Mendelian randomization studies have identified associations between genetically proxied plasma NEURL1 levels and reduced migraine risk, suggesting protective effects (chen2022theroleof pages 8-10). Studies have also investigated NEURL1 in autism spectrum disorders, particularly in relation to learning and memory dysfunction, though the mechanistic basis requires further clarification (eciroglu2022therelationshipof pages 6-7).

NEURL1 genetic variants have been associated with atrial fibrillation susceptibility in genome-wide association studies, and the protein shows indirect interactions with Notch pathway components through β-catenin and JAG1 or DLL4 (dutta2022regulationofnotch pages 15-17).

## Experimental Evidence and Methodological Approaches

The functional characterization of NEURL1 has employed diverse experimental approaches:

1. **Biochemical studies**: Co-immunoprecipitation, ubiquitination assays with wild-type and mutant ubiquitin constructs, proteasome/lysosome inhibitor experiments, and cycloheximide-chase degradation assays have established substrate specificity and ubiquitin linkage types (taal2019neuralizedfamilymember pages 8-9, taal2019neuralizedfamilymember pages 4-6, taal2019neuralizedfamilymember pages 6-8).

2. **Cell biological approaches**: Subcellular localization studies, protein redistribution analyses, and myristoylation-dependent membrane targeting experiments have defined where NEURL1 functions (taal2019neuralizedfamilymember pages 2-3, taal2019neuralizedfamilymember pages 8-9, taal2019neuralizedfamilymember pages 3-4).

3. **Genetic studies**: Knockout mouse models (single and double knockouts) combined with behavioral testing (Morris water maze, object-location memory, contextual fear conditioning) have demonstrated roles in spatial memory (lee2020neur1andneur2 pages 1-2, lee2020neur1andneur2 pages 6-8, lee2020neur1andneur2 pages 2-3).

4. **Electrophysiological studies**: Field recordings measuring input-output relationships, paired-pulse facilitation, and theta-burst-induced LTP have revealed selective deficits in protein synthesis-dependent late LTP (lee2020neur1andneur2 pages 1-2, lee2020neur1andneur2 pages 6-8).

5. **Comparative and evolutionary studies**: Work in Drosophila Neuralized has provided mechanistic insights into Delta-Neuralized complex formation, endocytosis-dependent Notch activation, and the separability of adaptor versus catalytic functions (kalodimou2023separablerolesfor pages 17-19, kalodimou2023separablerolesfor pages 1-2, kalodimou2023separablerolesfor pages 14-15).

## Current Understanding and Future Directions

NEURL1 functions as a multi-substrate E3 ubiquitin ligase with context-dependent outcomes: it can promote either protein degradation (PDE9A) or functional activation without degradation (CPEB3, Notch ligands). The protein operates at the intersection of three major signaling systems—Notch signaling, synaptic plasticity/AMPA receptor regulation, and cGMP signaling—each with distinct molecular mechanisms and physiological consequences.

The functional redundancy with NEURL2 in the hippocampus highlights the complexity of NEURL family functions and suggests that therapeutic targeting would need to consider both paralogs. The substrate-specific ubiquitination patterns (monoubiquitination vs. polyubiquitination with specific linkages) indicate sophisticated regulatory mechanisms that likely depend on substrate structure, cellular context, and post-translational modifications of NEURL1 itself.

Outstanding questions include: (1) the precise structural determinants of substrate selectivity, (2) the regulation of NEURL1 activity and localization by signaling pathways and cellular states, (3) the full complement of physiological substrates, and (4) the potential for therapeutic intervention in diseases where NEURL1 function is altered. Recent studies (2023-2025) continue to reveal new aspects of Neuralized function in Notch signaling and expand our understanding of context-dependent mechanisms (kalodimou2023separablerolesfor pages 17-19, bray2025modesofnotch pages 27-33).

## Summary

NEURL1 (E3 ubiquitin-protein ligase NEURL1) is a RING-type E3 ubiquitin ligase that catalyzes substrate-specific ubiquitination reactions with diverse functional outcomes. The enzyme contains two NHR domains for substrate recognition and a RING domain for catalysis. It localizes to both the cytoplasm and plasma membrane, functioning in different compartments depending on the substrate. NEURL1 regulates three major pathways: (1) Notch signaling through ubiquitination of Delta and Jagged1 ligands to promote endocytosis-dependent receptor activation; (2) synaptic plasticity through monoubiquitination of CPEB3 to activate translation of AMPA receptor subunits GluA1 and GluA2; and (3) cGMP signaling through polyubiquitination and proteasomal degradation of PDE9A. Genetic studies demonstrate requirements for hippocampus-dependent spatial memory and protein synthesis-dependent long-term potentiation, with functional redundancy with NEURL2. The protein represents a key node connecting ubiquitin-dependent regulation to neuronal signaling, plasticity, and memory formation.

References

1. (taal2019neuralizedfamilymember pages 1-2): Kati Taal, Jürgen Tuvikene, Grete Rullinkov, Marko Piirsoo, Mari Sepp, Toomas Neuman, Richard Tamme, and Tõnis Timmusk. Neuralized family member neurl1 is a ubiquitin ligase for the cgmp-specific phosphodiesterase 9a. Scientific Reports, May 2019. URL: https://doi.org/10.1038/s41598-019-43069-x, doi:10.1038/s41598-019-43069-x. This article has 15 citations and is from a peer-reviewed journal.

2. (seib2021theroleof pages 8-9): Ekaterina Seib and Thomas Klein. The role of ligand endocytosis in notch signalling. Biology of the Cell, 113:401-418, Jun 2021. URL: https://doi.org/10.1111/boc.202100009, doi:10.1111/boc.202100009. This article has 44 citations and is from a peer-reviewed journal.

3. (taal2019neuralizedfamilymember pages 3-4): Kati Taal, Jürgen Tuvikene, Grete Rullinkov, Marko Piirsoo, Mari Sepp, Toomas Neuman, Richard Tamme, and Tõnis Timmusk. Neuralized family member neurl1 is a ubiquitin ligase for the cgmp-specific phosphodiesterase 9a. Scientific Reports, May 2019. URL: https://doi.org/10.1038/s41598-019-43069-x, doi:10.1038/s41598-019-43069-x. This article has 15 citations and is from a peer-reviewed journal.

4. (taal2019neuralizedfamilymember pages 8-9): Kati Taal, Jürgen Tuvikene, Grete Rullinkov, Marko Piirsoo, Mari Sepp, Toomas Neuman, Richard Tamme, and Tõnis Timmusk. Neuralized family member neurl1 is a ubiquitin ligase for the cgmp-specific phosphodiesterase 9a. Scientific Reports, May 2019. URL: https://doi.org/10.1038/s41598-019-43069-x, doi:10.1038/s41598-019-43069-x. This article has 15 citations and is from a peer-reviewed journal.

5. (taal2019neuralizedfamilymember pages 4-6): Kati Taal, Jürgen Tuvikene, Grete Rullinkov, Marko Piirsoo, Mari Sepp, Toomas Neuman, Richard Tamme, and Tõnis Timmusk. Neuralized family member neurl1 is a ubiquitin ligase for the cgmp-specific phosphodiesterase 9a. Scientific Reports, May 2019. URL: https://doi.org/10.1038/s41598-019-43069-x, doi:10.1038/s41598-019-43069-x. This article has 15 citations and is from a peer-reviewed journal.

6. (taal2019neuralizedfamilymember pages 2-3): Kati Taal, Jürgen Tuvikene, Grete Rullinkov, Marko Piirsoo, Mari Sepp, Toomas Neuman, Richard Tamme, and Tõnis Timmusk. Neuralized family member neurl1 is a ubiquitin ligase for the cgmp-specific phosphodiesterase 9a. Scientific Reports, May 2019. URL: https://doi.org/10.1038/s41598-019-43069-x, doi:10.1038/s41598-019-43069-x. This article has 15 citations and is from a peer-reviewed journal.

7. (kalodimou2023separablerolesfor pages 17-19): Konstantina Kalodimou, Margarita Stapountzi, Nicole Vüllings, Ekaterina Seib, Thomas Klein, and Christos Delidakis. Separable roles for neur and ubiquitin in delta signalling in the drosophila cns lineages. Cells, 12:2833, Dec 2023. URL: https://doi.org/10.3390/cells12242833, doi:10.3390/cells12242833. This article has 4 citations.

8. (kalodimou2023separablerolesfor pages 1-2): Konstantina Kalodimou, Margarita Stapountzi, Nicole Vüllings, Ekaterina Seib, Thomas Klein, and Christos Delidakis. Separable roles for neur and ubiquitin in delta signalling in the drosophila cns lineages. Cells, 12:2833, Dec 2023. URL: https://doi.org/10.3390/cells12242833, doi:10.3390/cells12242833. This article has 4 citations.

9. (bray2025modesofnotch pages 27-33): Sarah J. Bray and Anna Bigas. Modes of notch signalling in development and disease. Nature reviews. Molecular cell biology, 26:522-537, Mar 2025. URL: https://doi.org/10.1038/s41580-025-00835-2, doi:10.1038/s41580-025-00835-2. This article has 63 citations.

10. (kalodimou2023separablerolesfor pages 14-15): Konstantina Kalodimou, Margarita Stapountzi, Nicole Vüllings, Ekaterina Seib, Thomas Klein, and Christos Delidakis. Separable roles for neur and ubiquitin in delta signalling in the drosophila cns lineages. Cells, 12:2833, Dec 2023. URL: https://doi.org/10.3390/cells12242833, doi:10.3390/cells12242833. This article has 4 citations.

11. (chen2022theroleof pages 8-10): Xuankun Chen, Li Jiang, Zhesheng Zhou, Bo Yang, Qiaojun He, Chengliang Zhu, and Ji Cao. The role of membrane-associated e3 ubiquitin ligases in cancer. Frontiers in Pharmacology, Jul 2022. URL: https://doi.org/10.3389/fphar.2022.928794, doi:10.3389/fphar.2022.928794. This article has 17 citations.

12. (dutta2022regulationofnotch pages 15-17): Debdeep Dutta, Vartika Sharma, Mousumi Mutsuddi, and Ashim Mukherjee. Regulation of notch signaling by e3 ubiquitin ligases. The FEBS Journal, 289:937-954, Mar 2022. URL: https://doi.org/10.1111/febs.15792, doi:10.1111/febs.15792. This article has 44 citations.

13. (taal2019neuralizedfamilymember pages 10-11): Kati Taal, Jürgen Tuvikene, Grete Rullinkov, Marko Piirsoo, Mari Sepp, Toomas Neuman, Richard Tamme, and Tõnis Timmusk. Neuralized family member neurl1 is a ubiquitin ligase for the cgmp-specific phosphodiesterase 9a. Scientific Reports, May 2019. URL: https://doi.org/10.1038/s41598-019-43069-x, doi:10.1038/s41598-019-43069-x. This article has 15 citations and is from a peer-reviewed journal.

14. (qu2020roleofcpeb3 pages 4-7): Wen Rui Qu, Qi Han Sun, Qian Qian Liu, Hong Juan Jin, Ran Ji Cui, Wei Yang, De Biao Song, and Bing Jin Li. Role of cpeb3 protein in learning and memory: new insights from synaptic plasticity. Aging (Albany NY), 12:15169-15182, Jul 2020. URL: https://doi.org/10.18632/aging.103404, doi:10.18632/aging.103404. This article has 25 citations.

15. (qu2020roleofcpeb3 pages 7-8): Wen Rui Qu, Qi Han Sun, Qian Qian Liu, Hong Juan Jin, Ran Ji Cui, Wei Yang, De Biao Song, and Bing Jin Li. Role of cpeb3 protein in learning and memory: new insights from synaptic plasticity. Aging (Albany NY), 12:15169-15182, Jul 2020. URL: https://doi.org/10.18632/aging.103404, doi:10.18632/aging.103404. This article has 25 citations.

16. (lee2020neur1andneur2 pages 1-2): Jaehyun Lee, Ki‐Jun Yoon, Pojeong Park, Chaery Lee, Min Jung Kim, Dae Hee Han, Ji‐il Kim, Somi Kim, Hye‐Ryeon Lee, Yeseul Lee, Eun‐Hae Jang, Hyoung‐Gon Ko, Young‐Yun Kong, and Bong‐Kiun Kaang. Neur1 and neur2 are required for hippocampus‐dependent spatial memory and synaptic plasticity. Hippocampus, 30:1158-1166, Jul 2020. URL: https://doi.org/10.1002/hipo.23247, doi:10.1002/hipo.23247. This article has 6 citations and is from a peer-reviewed journal.

17. (taal2019neuralizedfamilymember pages 9-10): Kati Taal, Jürgen Tuvikene, Grete Rullinkov, Marko Piirsoo, Mari Sepp, Toomas Neuman, Richard Tamme, and Tõnis Timmusk. Neuralized family member neurl1 is a ubiquitin ligase for the cgmp-specific phosphodiesterase 9a. Scientific Reports, May 2019. URL: https://doi.org/10.1038/s41598-019-43069-x, doi:10.1038/s41598-019-43069-x. This article has 15 citations and is from a peer-reviewed journal.

18. (taal2019neuralizedfamilymember pages 6-6): Kati Taal, Jürgen Tuvikene, Grete Rullinkov, Marko Piirsoo, Mari Sepp, Toomas Neuman, Richard Tamme, and Tõnis Timmusk. Neuralized family member neurl1 is a ubiquitin ligase for the cgmp-specific phosphodiesterase 9a. Scientific Reports, May 2019. URL: https://doi.org/10.1038/s41598-019-43069-x, doi:10.1038/s41598-019-43069-x. This article has 15 citations and is from a peer-reviewed journal.

19. (kozlov2021theroleof pages 7-9): Eugene Kozlov, Yulii V. Shidlovskii, Rudolf Gilmutdinov, Paul Schedl, and Mariya Zhukova. The role of cpeb family proteins in the nervous system function in the norm and pathology. Cell & Bioscience, Mar 2021. URL: https://doi.org/10.1186/s13578-021-00577-6, doi:10.1186/s13578-021-00577-6. This article has 61 citations and is from a peer-reviewed journal.

20. (taal2019neuralizedfamilymember pages 6-8): Kati Taal, Jürgen Tuvikene, Grete Rullinkov, Marko Piirsoo, Mari Sepp, Toomas Neuman, Richard Tamme, and Tõnis Timmusk. Neuralized family member neurl1 is a ubiquitin ligase for the cgmp-specific phosphodiesterase 9a. Scientific Reports, May 2019. URL: https://doi.org/10.1038/s41598-019-43069-x, doi:10.1038/s41598-019-43069-x. This article has 15 citations and is from a peer-reviewed journal.

21. (lee2020neur1andneur2 pages 6-8): Jaehyun Lee, Ki‐Jun Yoon, Pojeong Park, Chaery Lee, Min Jung Kim, Dae Hee Han, Ji‐il Kim, Somi Kim, Hye‐Ryeon Lee, Yeseul Lee, Eun‐Hae Jang, Hyoung‐Gon Ko, Young‐Yun Kong, and Bong‐Kiun Kaang. Neur1 and neur2 are required for hippocampus‐dependent spatial memory and synaptic plasticity. Hippocampus, 30:1158-1166, Jul 2020. URL: https://doi.org/10.1002/hipo.23247, doi:10.1002/hipo.23247. This article has 6 citations and is from a peer-reviewed journal.

22. (lee2020neur1andneur2 pages 2-3): Jaehyun Lee, Ki‐Jun Yoon, Pojeong Park, Chaery Lee, Min Jung Kim, Dae Hee Han, Ji‐il Kim, Somi Kim, Hye‐Ryeon Lee, Yeseul Lee, Eun‐Hae Jang, Hyoung‐Gon Ko, Young‐Yun Kong, and Bong‐Kiun Kaang. Neur1 and neur2 are required for hippocampus‐dependent spatial memory and synaptic plasticity. Hippocampus, 30:1158-1166, Jul 2020. URL: https://doi.org/10.1002/hipo.23247, doi:10.1002/hipo.23247. This article has 6 citations and is from a peer-reviewed journal.

23. (eciroglu2022therelationshipof pages 6-7): Hamiyet ECIROGLU, Elif Funda ŞENER, Didem Behice ÖZTOP, Sevgi ÖZMEN, Dilek KAAN, and Yusuf ÖZKUL. The relationship of learning and memory disfunction with neurl1 and rgs14 genes in patients with autism spectrum disorders. Acta Medica Alanya, 6:207-213, Aug 2022. URL: https://doi.org/10.30565/medalanya.1136820, doi:10.30565/medalanya.1136820. This article has 2 citations.

## Artifacts

- [Edison artifact artifact-00](NEURL1-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. taal2019neuralizedfamilymember pages 1-2
2. taal2019neuralizedfamilymember pages 3-4
3. seib2021theroleof pages 8-9
4. taal2019neuralizedfamilymember pages 2-3
5. bray2025modesofnotch pages 27-33
6. taal2019neuralizedfamilymember pages 8-9
7. taal2019neuralizedfamilymember pages 10-11
8. chen2022theroleof pages 8-10
9. eciroglu2022therelationshipof pages 6-7
10. dutta2022regulationofnotch pages 15-17
11. taal2019neuralizedfamilymember pages 4-6
12. kalodimou2023separablerolesfor pages 17-19
13. kalodimou2023separablerolesfor pages 1-2
14. kalodimou2023separablerolesfor pages 14-15
15. taal2019neuralizedfamilymember pages 9-10
16. taal2019neuralizedfamilymember pages 6-6
17. kozlov2021theroleof pages 7-9
18. taal2019neuralizedfamilymember pages 6-8
19. https://doi.org/10.1038/s41598-019-43069-x,
20. https://doi.org/10.1111/boc.202100009,
21. https://doi.org/10.3390/cells12242833,
22. https://doi.org/10.1038/s41580-025-00835-2,
23. https://doi.org/10.3389/fphar.2022.928794,
24. https://doi.org/10.1111/febs.15792,
25. https://doi.org/10.18632/aging.103404,
26. https://doi.org/10.1002/hipo.23247,
27. https://doi.org/10.1186/s13578-021-00577-6,
28. https://doi.org/10.30565/medalanya.1136820,