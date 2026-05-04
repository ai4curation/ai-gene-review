---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-03T14:31:33.192589'
end_time: '2026-05-03T14:40:50.669503'
duration_seconds: 557.48
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: mouse
  gene_id: App
  gene_symbol: App
  uniprot_accession: P12023
  protein_description: 'RecName: Full=Amyloid-beta precursor protein {ECO:0000250|UniProtKB:P05067};
    AltName: Full=ABPP; Short=APP; AltName: Full=Alzheimer disease amyloid A4 protein
    homolog; AltName: Full=Alzheimer disease amyloid protein; AltName: Full=Amyloid
    precursor protein {ECO:0000305}; AltName: Full=Amyloid-beta (A4) precursor protein
    {ECO:0000312|MGI:MGI:88059}; AltName: Full=Amyloid-beta A4 protein {ECO:0000250|UniProtKB:P08592};
    AltName: Full=Amyloidogenic glycoprotein; Short=AG; Contains: RecName: Full=N-APP;
    Contains: RecName: Full=Soluble APP-alpha; Short=S-APP-alpha; Contains: RecName:
    Full=Soluble APP-beta; Short=S-APP-beta; Contains: RecName: Full=C99; AltName:
    Full=APP-C99; AltName: Full=Beta-secretase C-terminal fragment; Short=Beta-CTF;
    Contains: RecName: Full=Amyloid-beta protein 42; Short=Abeta42; AltName: Full=Beta-APP42;
    Contains: RecName: Full=Amyloid-beta protein 40; Short=Abeta40; AltName: Full=Beta-APP40;
    Contains: RecName: Full=C83; AltName: Full=Alpha-secretase C-terminal fragment;
    Short=Alpha-CTF; Contains: RecName: Full=P3(42); Contains: RecName: Full=P3(40);
    Contains: RecName: Full=C80; Contains: RecName: Full=Gamma-secretase C-terminal
    fragment 59; AltName: Full=APP-C59; AltName: Full=Amyloid intracellular domain
    59; Short=AID(59); AltName: Full=Gamma-CTF(59); Contains: RecName: Full=Gamma-secretase
    C-terminal fragment 57; AltName: Full=APP-C57; AltName: Full=Amyloid intracellular
    domain 57; Short=AID(57); AltName: Full=Gamma-CTF(57); Contains: RecName: Full=Gamma-secretase
    C-terminal fragment 50; AltName: Full=Amyloid intracellular domain 50; Short=AID(50);
    AltName: Full=Gamma-CTF(50); Contains: RecName: Full=C31; Flags: Precursor;'
  gene_info: Name=App {ECO:0000312|MGI:MGI:88059}; Synonyms=A4 {ECO:0000250|UniProtKB:P05067},
    AD1 {ECO:0000250|UniProtKB:P05067};
  organism_full: Mus musculus (Mouse).
  protein_family: Belongs to the APP family. {ECO:0000255|PROSITE-
  protein_domains: Amyloid_Cu-bd_sf. (IPR036669); Amyloid_glyco. (IPR008155); Amyloid_glyco_Abeta.
    (IPR013803); Amyloid_glyco_Cu-bd. (IPR011178); Amyloid_glyco_E2_domain. (IPR024329)
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 23
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P12023
- **Protein Description:** RecName: Full=Amyloid-beta precursor protein {ECO:0000250|UniProtKB:P05067}; AltName: Full=ABPP; Short=APP; AltName: Full=Alzheimer disease amyloid A4 protein homolog; AltName: Full=Alzheimer disease amyloid protein; AltName: Full=Amyloid precursor protein {ECO:0000305}; AltName: Full=Amyloid-beta (A4) precursor protein {ECO:0000312|MGI:MGI:88059}; AltName: Full=Amyloid-beta A4 protein {ECO:0000250|UniProtKB:P08592}; AltName: Full=Amyloidogenic glycoprotein; Short=AG; Contains: RecName: Full=N-APP; Contains: RecName: Full=Soluble APP-alpha; Short=S-APP-alpha; Contains: RecName: Full=Soluble APP-beta; Short=S-APP-beta; Contains: RecName: Full=C99; AltName: Full=APP-C99; AltName: Full=Beta-secretase C-terminal fragment; Short=Beta-CTF; Contains: RecName: Full=Amyloid-beta protein 42; Short=Abeta42; AltName: Full=Beta-APP42; Contains: RecName: Full=Amyloid-beta protein 40; Short=Abeta40; AltName: Full=Beta-APP40; Contains: RecName: Full=C83; AltName: Full=Alpha-secretase C-terminal fragment; Short=Alpha-CTF; Contains: RecName: Full=P3(42); Contains: RecName: Full=P3(40); Contains: RecName: Full=C80; Contains: RecName: Full=Gamma-secretase C-terminal fragment 59; AltName: Full=APP-C59; AltName: Full=Amyloid intracellular domain 59; Short=AID(59); AltName: Full=Gamma-CTF(59); Contains: RecName: Full=Gamma-secretase C-terminal fragment 57; AltName: Full=APP-C57; AltName: Full=Amyloid intracellular domain 57; Short=AID(57); AltName: Full=Gamma-CTF(57); Contains: RecName: Full=Gamma-secretase C-terminal fragment 50; AltName: Full=Amyloid intracellular domain 50; Short=AID(50); AltName: Full=Gamma-CTF(50); Contains: RecName: Full=C31; Flags: Precursor;
- **Gene Information:** Name=App {ECO:0000312|MGI:MGI:88059}; Synonyms=A4 {ECO:0000250|UniProtKB:P05067}, AD1 {ECO:0000250|UniProtKB:P05067};
- **Organism (full):** Mus musculus (Mouse).
- **Protein Family:** Belongs to the APP family. {ECO:0000255|PROSITE-
- **Key Domains:** Amyloid_Cu-bd_sf. (IPR036669); Amyloid_glyco. (IPR008155); Amyloid_glyco_Abeta. (IPR013803); Amyloid_glyco_Cu-bd. (IPR011178); Amyloid_glyco_E2_domain. (IPR024329)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "App" matches the protein description above**
2. **Verify the organism is correct:** Mus musculus (Mouse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'App' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **App** (gene ID: App, UniProt: P12023) in mouse.

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
- **UniProt Accession:** P12023
- **Protein Description:** RecName: Full=Amyloid-beta precursor protein {ECO:0000250|UniProtKB:P05067}; AltName: Full=ABPP; Short=APP; AltName: Full=Alzheimer disease amyloid A4 protein homolog; AltName: Full=Alzheimer disease amyloid protein; AltName: Full=Amyloid precursor protein {ECO:0000305}; AltName: Full=Amyloid-beta (A4) precursor protein {ECO:0000312|MGI:MGI:88059}; AltName: Full=Amyloid-beta A4 protein {ECO:0000250|UniProtKB:P08592}; AltName: Full=Amyloidogenic glycoprotein; Short=AG; Contains: RecName: Full=N-APP; Contains: RecName: Full=Soluble APP-alpha; Short=S-APP-alpha; Contains: RecName: Full=Soluble APP-beta; Short=S-APP-beta; Contains: RecName: Full=C99; AltName: Full=APP-C99; AltName: Full=Beta-secretase C-terminal fragment; Short=Beta-CTF; Contains: RecName: Full=Amyloid-beta protein 42; Short=Abeta42; AltName: Full=Beta-APP42; Contains: RecName: Full=Amyloid-beta protein 40; Short=Abeta40; AltName: Full=Beta-APP40; Contains: RecName: Full=C83; AltName: Full=Alpha-secretase C-terminal fragment; Short=Alpha-CTF; Contains: RecName: Full=P3(42); Contains: RecName: Full=P3(40); Contains: RecName: Full=C80; Contains: RecName: Full=Gamma-secretase C-terminal fragment 59; AltName: Full=APP-C59; AltName: Full=Amyloid intracellular domain 59; Short=AID(59); AltName: Full=Gamma-CTF(59); Contains: RecName: Full=Gamma-secretase C-terminal fragment 57; AltName: Full=APP-C57; AltName: Full=Amyloid intracellular domain 57; Short=AID(57); AltName: Full=Gamma-CTF(57); Contains: RecName: Full=Gamma-secretase C-terminal fragment 50; AltName: Full=Amyloid intracellular domain 50; Short=AID(50); AltName: Full=Gamma-CTF(50); Contains: RecName: Full=C31; Flags: Precursor;
- **Gene Information:** Name=App {ECO:0000312|MGI:MGI:88059}; Synonyms=A4 {ECO:0000250|UniProtKB:P05067}, AD1 {ECO:0000250|UniProtKB:P05067};
- **Organism (full):** Mus musculus (Mouse).
- **Protein Family:** Belongs to the APP family. {ECO:0000255|PROSITE-
- **Key Domains:** Amyloid_Cu-bd_sf. (IPR036669); Amyloid_glyco. (IPR008155); Amyloid_glyco_Abeta. (IPR013803); Amyloid_glyco_Cu-bd. (IPR011178); Amyloid_glyco_E2_domain. (IPR024329)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "App" matches the protein description above**
2. **Verify the organism is correct:** Mus musculus (Mouse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'App' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **App** (gene ID: App, UniProt: P12023) in mouse.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Research report: functional annotation of mouse **App** (UniProt **P12023**) / amyloid precursor protein (APP)

### 1) Target verification and gene/protein identity (critical disambiguation)
The target is **Mus musculus App** encoding **amyloid precursor protein (APP)**, a **type I single-pass transmembrane glycoprotein**; this matches the UniProt description provided (P12023) and the mouse-focused literature discussing App/APP as the precursor of amyloid-β (Aβ) peptides. (dunot2023spatiotemporalinsightsof pages 1-3, wang2024advancesinthe pages 2-4)

### 2) Key concepts and definitions (current understanding)

#### 2.1 APP as a receptor-like scaffold/adaptor hub (not an enzyme)
Current reviews describe APP as having **no intrinsic enzymatic activity**, but acting as a **receptor-like scaffold** whose functions depend on developmental stage, cell type, interaction partners, and proteolytic processing. (dunot2023spatiotemporalinsightsof pages 1-3)

Key structural/functional concepts include:
- **Isoforms**: major splice isoforms include **APP695** as the predominant neuronal isoform. (dunot2023spatiotemporalinsightsof pages 1-3, wang2024advancesinthe pages 2-4)
- **Extracellular/luminal region**: contains E1/E2 regions enabling **cis/trans dimerization** and ligand/adhesion-like interactions; proteolytic processing can antagonize dimerization. (dunot2023spatiotemporalinsightsof pages 1-3)
- **Cytosolic tail**: contains the **YENPTY motif**, which binds adaptor proteins and regulates **endocytosis, intracellular trafficking, and signaling**. (dunot2023spatiotemporalinsightsof pages 1-3, wang2024advancesinthe pages 4-6)

#### 2.2 Proteolytic processing pathways and core fragment definitions
APP is constitutively cleaved through pathways typically framed as:
- **Non-amyloidogenic**: **α-secretase** cleavage generates **sAPPα** and a membrane C-terminal fragment **C83 (CTFα)**; subsequent **γ-secretase** cleavage yields **p3** plus the intracellular fragment **AICD**. (wang2024advancesinthe pages 2-4, wang2024advancesinthe media 161deba7)
- **Amyloidogenic**: **β-secretase (BACE1)** cleavage generates **sAPPβ** and **C99 (CTFβ)**; subsequent **γ-secretase** cleavage yields **Aβ peptides** plus **AICD**. (wang2024advancesinthe pages 2-4, wang2024advancesinthe media 161deba7)

In neurons, **ADAM10** is emphasized as the physiologically relevant α-secretase, while **BACE1** initiates amyloidogenic processing. (wang2024advancesinthe pages 21-22, wang2024advancesinthe pages 2-4)

A 2024 review also synthesizes additional secretase activities and their intracellular localizations (e.g., δ-, ε-, η-secretase) as a broader “secretase landscape” for APP cleavage. (yang2024secretasepromotesad pages 1-2)

#### 2.3 AICD (APP intracellular domain): definition and conceptual role
**AICD** is the intracellular fragment released by γ-secretase following α- or β-cleavage. It is widely discussed as a **signaling-competent fragment** that can form nuclear complexes (e.g., with **FE65 and Tip60**) and regulate transcriptional programs impacting neuronal survival/stress responses and potentially neurodegeneration. (ng2024theaicdinteractome pages 7-8)

### 3) Molecular function and pathways (mechanistic functional annotation)

#### 3.1 Core molecular “function”: a trafficking- and cleavage-regulated signaling hub
A convergent mechanistic view across recent reviews is that APP function emerges from:
1) **Compartmentalized trafficking** that determines which proteases/partners APP meets, and
2) **Proteolytic processing** that generates bioactive extracellular and intracellular fragments. (dunot2023spatiotemporalinsightsof pages 3-5, wang2024advancesinthe pages 4-6, wang2024advancesinthe pages 2-4)

Accordingly, APP is often functionally annotated less as a single “reaction,” and more as a **membrane hub that integrates adhesion-like interactions, endocytosis/trafficking, and fragment-mediated signaling**. (dunot2023spatiotemporalinsightsof pages 1-3, wang2024advancesinthe pages 2-4)

#### 3.2 Fragment-mediated physiological functions highlighted in recent synthesis
Recent expert synthesis emphasizes that APP and/or its fragments contribute to synaptic regulation, including:
- **Excitatory synapses**: APP is described as abundant at glutamatergic presynapses and organized in nanoscale synaptic domains; C-terminal interactions regulate NMDA receptor function. (dunot2023spatiotemporalinsightsof pages 3-5)
- **Age-dependent NMDA receptor regulation**: in mouse hippocampal synapses, APP processing shifts with aging toward β/γ processing, and a dual mechanism has been reported in which **full-length APP** regulates **GluN2B** activity in infant mice, while **AICD** regulates GluN2B activity in aged mice. (dunot2023spatiotemporalinsightsof pages 3-5)
- **Inhibitory system links**: APP has been reported to interact with **KCC2** (limiting its phosphorylation/ubiquitination and degradation) and to influence GABAB receptor-related presynaptic regulation via soluble APP fragments, though some of these mechanisms remain debated in the field. (dunot2023spatiotemporalinsightsof pages 3-5)

#### 3.3 AICD-centered expert view (2024)
A 2024 review of the AICD “interactome” argues that AICD engages a dynamic interaction network implicated in:
- **Transcriptional regulation** (including AICD–FE65–Tip60 complexes)
- **Cytoskeletal dynamics / neuronal growth**
- **APP processing feedback and apoptosis/stress programs**

It also summarizes evidence that AICD overexpression in transgenic mice can produce **AD-like phenotypes** (e.g., tau hyperphosphorylation linked to GSK-3β activity, age-dependent hippocampal neuron loss, and excitotoxic susceptibility), supporting the concept that APP biology relevant to neurodegeneration can extend beyond extracellular Aβ alone. (ng2024theaicdinteractome pages 7-8)

### 4) Subcellular localization and trafficking (where APP acts)

#### 4.1 Canonical itinerary and key sorting logic
A 2024 trafficking-focused review synthesizes a consensus itinerary:
- APP is synthesized in the **ER**, matures through **Golgi/TGN**, and is sorted to the **plasma membrane** and/or **endosomes**.
- APP can be retrieved from endosomes back to the **TGN** via **retromer-mediated transport**.
- APP distribution is governed by cytosolic sorting motifs (including **YENPTY**) and phosphorylation, which influence routing between TGN–plasma membrane and TGN–endosome/lysosome pathways.

Because **APP and secretases are transmembrane proteins**, regulated co-localization in the same compartment/subdomain is necessary for cleavage and thus fragment output. (wang2024advancesinthe pages 4-6, wang2024advancesinthe pages 2-4)

#### 4.2 Visual evidence: processing and trafficking schematics
The following figure panels from the 2024 trafficking review schematize (i) non-amyloidogenic vs amyloidogenic processing and (ii) compartmentalized trafficking routes that control where APP meets BACE1/γ-secretase (Golgi/TGN, early/recycling/late endosomes, lysosomes, plasma membrane). (wang2024advancesinthe media 161deba7, wang2024advancesinthe media f594d735)

### 5) Recent developments and latest research (prioritizing 2023–2024)

#### 5.1 2023: spatiotemporal framing of APP function in mouse brain
A 2023 expert review emphasizes that APP functions are strongly **spatiotemporally contextual** (development vs aging; synapse type; processing state) and highlights strategies needed to disentangle full-length APP functions from fragment actions, including cell-specific genetic perturbations and fragment rescue approaches. (dunot2023spatiotemporalinsightsof pages 3-5, dunot2023spatiotemporalinsightsof pages 1-3)

#### 5.2 2024: cell-type-specific amyloidogenic contribution in App knock-in mice (quantitative)
A 2024 primary study used **heterozygous AppNL−G−F/wt knock-in mice** (an endogenous-locus APP/Aβ pathology model) and tested **oligodendrocyte-specific Bace1 deletion**. Key quantitative findings at **12 months**:
- Amyloid plaques were reduced by approximately **33% in hippocampus** and **29% in cortex**.
- Insoluble **Aβ1–40 and Aβ1–42** were reduced comparably.
- Myelination effects were subtle and compartment-specific: optic nerve g-ratio increased (**0.74±0.005 vs 0.71±0.007**, P=5.3×10−7; N=65 vs 69 axons), while corpus callosum myelin thickness was unchanged.
- Hippocampal synaptic plasticity was not detectably impaired: LTP **160.8±8.09% vs 156.21±7.26%**, P>0.05.

Mechanistically, isolated oligodendrocytes showed reduced BACE1 and increased full-length APP, consistent with reduced β-cleavage within that lineage, while bulk hippocampal BACE1/APP levels appeared unchanged (consistent with cell-type specificity). (ishii2024contributionofamyloid pages 11-12, ishii2024contributionofamyloid pages 1-2)

### 6) Current applications and real-world implementations

#### 6.1 Applications in mouse-model design and interpretation
APP biology is operationalized in vivo through:
- **Transgenic APP overexpression models** (e.g., APP/PS1) and increasingly through **APP knock-in models** (e.g., AppNL−G−F), which aim to place APP/Aβ pathology under endogenous regulatory control.
- Cell-type-specific perturbations of APP processing (e.g., Bace1 deletion in oligodendrocytes) to separate physiological roles of processing enzymes from pathology-driving Aβ production. (ishii2024contributionofamyloid pages 1-2)

#### 6.2 Therapeutic concept space (as reflected in 2024 reviews)
Two major therapeutic implementation spaces are emphasized:
- **Secretase-targeting strategies**: a 2024 review synthesizes secretase subtype localizations, cleavage products, and inhibitors/modulators across α-, β-, γ- and additional secretase classes, framing APP and Notch as shared substrates that create safety constraints for secretase inhibition. (yang2024secretasepromotesad pages 1-2)
- **Anti-Aβ strategies and clearance approaches**: a 2024 dissertation-style synthesis notes that multiple anti-Aβ monoclonal antibodies have advanced clinically and frames a therapeutic “consensus” that reducing Aβ spread/accumulation could prevent neurodegeneration, while also emphasizing the field’s increasing focus on soluble oligomeric Aβ as a key toxic species. (johansson2024theimpactof pages 22-25)

### 7) Expert opinions and interpretive analysis (authoritative synthesis)

#### 7.1 APP functional pleiotropy as a core translational constraint
Recent expert reviews converge on the view that APP’s physiological functions are **broad and context-dependent** (synapses, development, immune/endothelial/metabolic roles), and that the field still faces a major challenge in attributing phenotypes to **full-length APP versus specific fragments** (sAPPα, Aβ, AICD, CTFs). This is repeatedly flagged as a reason to use conditional genetics, temporal perturbations, and fragment-specific rescue/inhibition strategies rather than global perturbations alone. (dunot2023spatiotemporalinsightsof pages 3-5, dunot2023spatiotemporalinsightsof pages 1-3, dunot2023spatiotemporalinsightsof pages 5-7)

#### 7.2 AICD as a potentially important (and risky) signaling node
The 2024 AICD interactome review positions AICD as a signaling node that can modulate transcriptional stress and apoptosis programs in neurons and argues that AICD dysregulation may contribute to neurodegeneration via networks extending beyond extracellular amyloid deposition. (ng2024theaicdinteractome pages 7-8)

### 8) Summary table (functional annotation at a glance)
| Aspect | Key points | Best recent sources (with year) |
|---|---|---|
| identity/structure | Mouse target is **App** encoding the amyloid precursor protein (APP), a **type I single-pass transmembrane glycoprotein**. Major isoforms include **APP695** as the predominant neuronal form. APP has a large luminal/extracellular N-terminus, E1/E2 regions involved in dimerization/adhesion, and a short cytoplasmic tail containing the **YENPTY** motif for adaptor binding, endocytosis, and signaling; APP has no intrinsic enzymatic activity and behaves as a receptor-like scaffold with many interactors. (dunot2023spatiotemporalinsightsof pages 1-3, wang2024advancesinthe pages 2-4) | Dunot et al., 2023; Wang et al., 2024 |
| processing | APP undergoes **non-amyloidogenic** cleavage by **α-secretase** to generate **sAPPα + C83**, then **γ-secretase** generates **p3 + AICD**. In the **amyloidogenic** pathway, **BACE1/β-secretase** generates **sAPPβ + C99**, and γ-secretase generates **Aβ peptides + AICD**. Additional **η-secretase** processing yields ηCTF/Aη species. ADAM10 is highlighted as the major neuronal α-secretase; BACE1 is the initiating β-secretase for amyloidogenic processing. (wang2024advancesinthe pages 21-22, yang2024secretasepromotesad pages 1-2, wang2024advancesinthe pages 2-4, wang2024advancesinthe media 161deba7) | Wang et al., 2024; Yang et al., 2024; Afram et al., 2023 |
| localization/trafficking | APP is synthesized in the **ER**, matures in **Golgi/TGN**, and traffics to the **plasma membrane** and **endosomes**; retromer can return APP to the TGN. Processing is strongly compartment-dependent because APP must co-localize with secretases. Somatic APP is enriched in **Golgi and endosomal compartments** and appears as puncta in axons/dendrites; synaptically, APP is abundant in presynaptic nanodomains. β-cleavage is favored in acidic endosomal compartments; APP-derived ηCTF localizes to **Golgi, endosomes, and extracellular vesicles**. (dunot2023spatiotemporalinsightsof pages 3-5, wang2024advancesinthe pages 4-6, wang2024advancesinthe pages 2-4, wang2024advancesinthe media 161deba7) | Dunot et al., 2023; Wang et al., 2024; Afram et al., 2023 |
| physiological roles | APP contributes to **developmental and synaptic function**, including neurite outgrowth, synaptogenesis, excitatory and inhibitory transmission, and receptor regulation. Reported roles include regulation of **GluN2B-containing NMDA receptor** activity, **kainate receptor** signaling, interaction with **KCC2** to limit degradation, and effects of soluble APP fragments on **GABABR1a**-linked presynaptic function. Reviews also note roles in cholesterol homeostasis, innate immune responses, endothelial physiology, and trophic signaling by sAPPα. (dunot2023spatiotemporalinsightsof pages 3-5, wang2024advancesinthe pages 21-22, dunot2023spatiotemporalinsightsof pages 5-7) | Dunot et al., 2023; Wang et al., 2024 |
| mouse genetic evidence | Full **App knockout** is viable with relatively mild cognitive phenotypes, but **APP/APLP double or triple knockouts** can be postnatally lethal, supporting redundancy within the APP family. Conditional forebrain glutamatergic neuron App loss causes earlier excitatory plasticity deficits than full KO. In utero knockdown reduced **GluN2B currents at P7–9**, rescued by **AICD** peptide, supporting a fragment-specific signaling role. Aging in mice shifts processing toward the **β/γ-secretase** pathway, and APP-FL versus AICD can differentially regulate synaptic GluN2B across age. (dunot2023spatiotemporalinsightsof pages 1-3, dunot2023spatiotemporalinsightsof pages 3-5) | Dunot et al., 2023 |
| 2024 quantitative data | In **12-month** heterozygous **AppNL-G-F/wt** mice, **oligodendrocyte-specific Bace1 deletion** reduced plaque burden by about **33% in hippocampus** and **29% in cortex**, with comparable decreases in insoluble **Aβ1-40/Aβ1-42**; hippocampal LTP was unchanged, while optic nerve g-ratio increased from **0.71±0.007 to 0.74±0.005**. More detailed electrophysiology showed LTP **160.8±8.09% vs 156.21±7.26% (P>0.05)**. New in vivo imaging work also established NIR-FRET recording of **γ-secretase activity** in individual neurons of living mouse brain. (ishii2024contributionofamyloid pages 11-12, ishii2024contributionofamyloid pages 1-2) | Ishii et al., 2024; Hou et al., 2024 |
| applications/translation cautions | APP biology is central to **AD mouse models**, biomarker logic, and therapeutic strategies targeting **secretases**, APP trafficking, or Aβ clearance. Recent work supports cell-type-specific intervention concepts (for example oligodendrocyte BACE1 contribution), while reviews emphasize that APP has broad physiological functions beyond Aβ generation, so indiscriminate modulation may be harmful. Experts caution that many AD mouse models overemphasize amyloid pathways and incompletely capture human disease complexity; APP-focused interventions should consider full-length APP and bioactive fragments, not just Aβ. (johansson2024theimpactof pages 22-25, dunot2023spatiotemporalinsightsof pages 5-7, ishii2024contributionofamyloid pages 1-2) | Sirisi et al., 2024; Granzotto et al., 2024; Ishii et al., 2024 |


*Table: This table concisely summarizes the functional annotation of mouse App/APP from the gathered evidence, covering structure, processing, localization, physiological roles, genetics, quantitative 2024 findings, and translational considerations.*

### 9) Source details (URLs and publication dates)
- Dunot J. et al. **“Spatiotemporal insights of APP function.”** *Current Opinion in Neurobiology* (Oct **2023**). https://doi.org/10.1016/j.conb.2023.102754 (dunot2023spatiotemporalinsightsof pages 1-3, dunot2023spatiotemporalinsightsof pages 3-5)
- Wang J. et al. **“Advances in the cell biology of the trafficking and processing of amyloid precursor protein: impact of familial Alzheimer's disease mutations.”** *Biochemical Journal* (Sep **2024**). https://doi.org/10.1042/bcj20240056 (wang2024advancesinthe pages 2-4, wang2024advancesinthe pages 4-6, wang2024advancesinthe pages 21-22)
- Yang K.-F. et al. **“Secretase promotes AD progression: simultaneously cleave Notch and APP.”** *Frontiers in Aging Neuroscience* (Nov **2024**). https://doi.org/10.3389/fnagi.2024.1445470 (yang2024secretasepromotesad pages 1-2)
- Ishii A. et al. **“Contribution of amyloid deposition from oligodendrocytes in a mouse model of Alzheimer’s disease.”** *Molecular Neurodegeneration* (Nov **2024**). https://doi.org/10.1186/s13024-024-00759-z (ishii2024contributionofamyloid pages 1-2, ishii2024contributionofamyloid pages 11-12)
- Ng L.L.-H. et al. **“The AICD interactome: implications in neurodevelopment and neurodegeneration.”** *Biochemical Society Transactions* (Dec **2024**). https://doi.org/10.1042/bst20241510 (ng2024theaicdinteractome pages 7-8)
- Johansson L. **“The Impact of Endosomes, Autophagy and Extracellular Vesicles on Alzheimer’s Disease.”** Linköping University Medical Dissertations (Nov **2024**). https://doi.org/10.3384/9789180757560 (johansson2024theimpactof pages 22-25)

### 10) Notes on evidence limits
The report focuses on recent 2023–2024 sources retrieved and mined for full-text evidence. Several broader claims common in APP biology (e.g., specific copper-binding residues/domains; full catalog of extracellular ligands; many classic APP knockout phenotypes) are not repeated here unless directly supported by the retrieved evidence excerpts.

References

1. (dunot2023spatiotemporalinsightsof pages 1-3): Jade Dunot, Aurore Ribera, Paula A. Pousinha, and Hélène Marie. Spatiotemporal insights of app function. Current Opinion in Neurobiology, 82:102754, Oct 2023. URL: https://doi.org/10.1016/j.conb.2023.102754, doi:10.1016/j.conb.2023.102754. This article has 20 citations and is from a peer-reviewed journal.

2. (wang2024advancesinthe pages 2-4): Jingqi Wang, Lou Fourriere, and Paul A. Gleeson. Advances in the cell biology of the trafficking and processing of amyloid precursor protein: impact of familial alzheimer's disease mutations. Biochemical Journal, 481:1297-1325, Sep 2024. URL: https://doi.org/10.1042/bcj20240056, doi:10.1042/bcj20240056. This article has 19 citations and is from a domain leading peer-reviewed journal.

3. (wang2024advancesinthe pages 4-6): Jingqi Wang, Lou Fourriere, and Paul A. Gleeson. Advances in the cell biology of the trafficking and processing of amyloid precursor protein: impact of familial alzheimer's disease mutations. Biochemical Journal, 481:1297-1325, Sep 2024. URL: https://doi.org/10.1042/bcj20240056, doi:10.1042/bcj20240056. This article has 19 citations and is from a domain leading peer-reviewed journal.

4. (wang2024advancesinthe media 161deba7): Jingqi Wang, Lou Fourriere, and Paul A. Gleeson. Advances in the cell biology of the trafficking and processing of amyloid precursor protein: impact of familial alzheimer's disease mutations. Biochemical Journal, 481:1297-1325, Sep 2024. URL: https://doi.org/10.1042/bcj20240056, doi:10.1042/bcj20240056. This article has 19 citations and is from a domain leading peer-reviewed journal.

5. (wang2024advancesinthe pages 21-22): Jingqi Wang, Lou Fourriere, and Paul A. Gleeson. Advances in the cell biology of the trafficking and processing of amyloid precursor protein: impact of familial alzheimer's disease mutations. Biochemical Journal, 481:1297-1325, Sep 2024. URL: https://doi.org/10.1042/bcj20240056, doi:10.1042/bcj20240056. This article has 19 citations and is from a domain leading peer-reviewed journal.

6. (yang2024secretasepromotesad pages 1-2): Ke-Fan Yang, Jing-Yi Zhang, Mei Feng, Kuo Yao, Yue-Yang Liu, Ming-Sheng Zhou, and Hui Jia. Secretase promotes ad progression: simultaneously cleave notch and app. Frontiers in Aging Neuroscience, Nov 2024. URL: https://doi.org/10.3389/fnagi.2024.1445470, doi:10.3389/fnagi.2024.1445470. This article has 8 citations and is from a peer-reviewed journal.

7. (ng2024theaicdinteractome pages 7-8): Laura Lok-Haang Ng, Jessica Chow, and Kwok-Fai Lau. The aicd interactome: implications in neurodevelopment and neurodegeneration. Biochemical Society Transactions, 52:2539-2556, Dec 2024. URL: https://doi.org/10.1042/bst20241510, doi:10.1042/bst20241510. This article has 6 citations and is from a peer-reviewed journal.

8. (dunot2023spatiotemporalinsightsof pages 3-5): Jade Dunot, Aurore Ribera, Paula A. Pousinha, and Hélène Marie. Spatiotemporal insights of app function. Current Opinion in Neurobiology, 82:102754, Oct 2023. URL: https://doi.org/10.1016/j.conb.2023.102754, doi:10.1016/j.conb.2023.102754. This article has 20 citations and is from a peer-reviewed journal.

9. (wang2024advancesinthe media f594d735): Jingqi Wang, Lou Fourriere, and Paul A. Gleeson. Advances in the cell biology of the trafficking and processing of amyloid precursor protein: impact of familial alzheimer's disease mutations. Biochemical Journal, 481:1297-1325, Sep 2024. URL: https://doi.org/10.1042/bcj20240056, doi:10.1042/bcj20240056. This article has 19 citations and is from a domain leading peer-reviewed journal.

10. (ishii2024contributionofamyloid pages 11-12): Akihiro Ishii, Joseph A. Pathoulas, Omar MoustafaFathy Omar, Yingying Ge, Annie Y. Yao, Tressa Pantalena, Neeraj Singh, John Zhou, Wanxia He, Patrick Murphy, Riqiang Yan, and Xiangyou Hu. Contribution of amyloid deposition from oligodendrocytes in a mouse model of alzheimer’s disease. Molecular Neurodegeneration, Nov 2024. URL: https://doi.org/10.1186/s13024-024-00759-z, doi:10.1186/s13024-024-00759-z. This article has 25 citations and is from a highest quality peer-reviewed journal.

11. (ishii2024contributionofamyloid pages 1-2): Akihiro Ishii, Joseph A. Pathoulas, Omar MoustafaFathy Omar, Yingying Ge, Annie Y. Yao, Tressa Pantalena, Neeraj Singh, John Zhou, Wanxia He, Patrick Murphy, Riqiang Yan, and Xiangyou Hu. Contribution of amyloid deposition from oligodendrocytes in a mouse model of alzheimer’s disease. Molecular Neurodegeneration, Nov 2024. URL: https://doi.org/10.1186/s13024-024-00759-z, doi:10.1186/s13024-024-00759-z. This article has 25 citations and is from a highest quality peer-reviewed journal.

12. (johansson2024theimpactof pages 22-25): Lovisa Johansson. The impact of endosomes, autophagy and extracellular vesicles on alzheimer’s disease. Linköping University Medical Dissertations, Nov 2024. URL: https://doi.org/10.3384/9789180757560, doi:10.3384/9789180757560. This article has 1 citations.

13. (dunot2023spatiotemporalinsightsof pages 5-7): Jade Dunot, Aurore Ribera, Paula A. Pousinha, and Hélène Marie. Spatiotemporal insights of app function. Current Opinion in Neurobiology, 82:102754, Oct 2023. URL: https://doi.org/10.1016/j.conb.2023.102754, doi:10.1016/j.conb.2023.102754. This article has 20 citations and is from a peer-reviewed journal.

## Citations

1. dunot2023spatiotemporalinsightsof pages 1-3
2. yang2024secretasepromotesad pages 1-2
3. ng2024theaicdinteractome pages 7-8
4. dunot2023spatiotemporalinsightsof pages 3-5
5. ishii2024contributionofamyloid pages 1-2
6. johansson2024theimpactof pages 22-25
7. wang2024advancesinthe pages 2-4
8. wang2024advancesinthe pages 4-6
9. wang2024advancesinthe pages 21-22
10. ishii2024contributionofamyloid pages 11-12
11. dunot2023spatiotemporalinsightsof pages 5-7
12. https://doi.org/10.1016/j.conb.2023.102754
13. https://doi.org/10.1042/bcj20240056
14. https://doi.org/10.3389/fnagi.2024.1445470
15. https://doi.org/10.1186/s13024-024-00759-z
16. https://doi.org/10.1042/bst20241510
17. https://doi.org/10.3384/9789180757560
18. https://doi.org/10.1016/j.conb.2023.102754,
19. https://doi.org/10.1042/bcj20240056,
20. https://doi.org/10.3389/fnagi.2024.1445470,
21. https://doi.org/10.1042/bst20241510,
22. https://doi.org/10.1186/s13024-024-00759-z,
23. https://doi.org/10.3384/9789180757560,