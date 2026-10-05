---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-02T07:06:01.709174'
end_time: '2026-09-02T07:14:54.760535'
duration_seconds: 533.05
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: HETGA
  gene_id: Trpv1
  gene_symbol: Trpv1
  uniprot_accession: G9DCX1
  protein_description: 'RecName: Full=Transient receptor potential cation channel
    subfamily V member 1 {ECO:0000256|ARBA:ARBA00015942}; AltName: Full=Osm-9-like
    TRP channel 1 {ECO:0000256|ARBA:ARBA00033256}; AltName: Full=Vanilloid receptor
    1 {ECO:0000256|ARBA:ARBA00031766};'
  gene_info: Name=Trpv1 {ECO:0000313|EMBL:AEV53346.1};
  organism_full: Heterocephalus glaber (Naked mole rat).
  protein_family: Belongs to the transient receptor (TC 1.A.4) family. TrpV
  protein_domains: Ankyrin_rpt. (IPR002110); Ankyrin_rpt-contain_sf. (IPR036770);
    Ion_trans_dom. (IPR005821); TRPV. (IPR024862); TrpV1-4. (IPR008347)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 25
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Trpv1-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** G9DCX1
- **Protein Description:** RecName: Full=Transient receptor potential cation channel subfamily V member 1 {ECO:0000256|ARBA:ARBA00015942}; AltName: Full=Osm-9-like TRP channel 1 {ECO:0000256|ARBA:ARBA00033256}; AltName: Full=Vanilloid receptor 1 {ECO:0000256|ARBA:ARBA00031766};
- **Gene Information:** Name=Trpv1 {ECO:0000313|EMBL:AEV53346.1};
- **Organism (full):** Heterocephalus glaber (Naked mole rat).
- **Protein Family:** Belongs to the transient receptor (TC 1.A.4) family. TrpV
- **Key Domains:** Ankyrin_rpt. (IPR002110); Ankyrin_rpt-contain_sf. (IPR036770); Ion_trans_dom. (IPR005821); TRPV. (IPR024862); TrpV1-4. (IPR008347)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Trpv1" matches the protein description above**
2. **Verify the organism is correct:** Heterocephalus glaber (Naked mole rat).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Trpv1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Trpv1** (gene ID: Trpv1, UniProt: G9DCX1) in HETGA.

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
- **UniProt Accession:** G9DCX1
- **Protein Description:** RecName: Full=Transient receptor potential cation channel subfamily V member 1 {ECO:0000256|ARBA:ARBA00015942}; AltName: Full=Osm-9-like TRP channel 1 {ECO:0000256|ARBA:ARBA00033256}; AltName: Full=Vanilloid receptor 1 {ECO:0000256|ARBA:ARBA00031766};
- **Gene Information:** Name=Trpv1 {ECO:0000313|EMBL:AEV53346.1};
- **Organism (full):** Heterocephalus glaber (Naked mole rat).
- **Protein Family:** Belongs to the transient receptor (TC 1.A.4) family. TrpV
- **Key Domains:** Ankyrin_rpt. (IPR002110); Ankyrin_rpt-contain_sf. (IPR036770); Ion_trans_dom. (IPR005821); TRPV. (IPR024862); TrpV1-4. (IPR008347)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Trpv1" matches the protein description above**
2. **Verify the organism is correct:** Heterocephalus glaber (Naked mole rat).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Trpv1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Trpv1** (gene ID: Trpv1, UniProt: G9DCX1) in HETGA.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional Annotation Report: *Trpv1* in the Naked Mole-Rat

## Executive summary

The target is correctly identified as **naked mole-rat (*Heterocephalus glaber*) TRPV1**, gene symbol *Trpv1*, UniProt accession **G9DCX1**. The supplied annotation—transient receptor potential cation channel subfamily V member 1, with ankyrin-repeat, ion-transport, TRPV, and TRPV1–4 domains—is internally consistent with canonical TRPV1. The retrieved species-specific literature also concerns *H. glaber* TRPV1 rather than a different same-symbol gene. However, the experimental papers generally call the protein “naked mole-rat TRPV1” without explicitly linking their experimental material to accession G9DCX1; that accession-level mapping therefore rests on the supplied UniProt record.

The principal function of G9DCX1 is best annotated as a **polymodal, plasma-membrane, nonselective cation channel in nociceptive sensory neurons**. Opening permits principally Na+ and Ca2+ entry, depolarizing the neuron and potentially initiating action potentials. Naked mole-rat TRPV1 itself is functional and responds to capsaicin; species-focused work further reports normal heat-, pH-, voltage-, and capsaicin-gating properties relative to mouse TRPV1. The naked mole-rat’s unusual lack of capsaicin pain and cutaneous acid pain is therefore **not a TRPV1 loss-of-function phenotype**. Instead, sensory output is attenuated downstream through altered spinal connectivity, deficient Substance P/CGRP-associated peptidergic signaling, hypofunctional NGF–TrkA inflammatory sensitization, and—for acid—enhanced proton inhibition of NaV1.7-dependent action-potential generation. (smith2020independentevolutionof pages 5-6, park2008selectiveinflammatorypain pages 9-10, browe2020thenakedmolerat pages 1-2, smith2020independentevolutionof pages 6-8)

## 1. Identity verification and evidence boundaries

### 1.1 Correct gene, protein, and organism

The requested symbol *Trpv1* matches the supplied protein description “transient receptor potential cation channel subfamily V member 1,” also known as vanilloid receptor 1. The organism is the naked mole-rat, *Heterocephalus glaber*. Species-specific primary studies explicitly examine TRPV1-positive sensory neurons, capsaicin-responsive C-fibers, and TRPV1-positive spinal projections in *H. glaber*. No evidence retrieved here concerns an alternative protein sharing the symbol. (park2008selectiveinflammatorypain pages 9-10, park2008selectiveinflammatorypain pages 4-6, smith2020independentevolutionof pages 4-5)

The supplied InterPro assignments—ankyrin repeats, an ion-transport domain, a TRPV-family domain, and TRPV1–4 classification—fit modern structural understanding. Canonical mammalian TRPV1 is an approximately 838-residue channel subunit containing cytoplasmic N-terminal ankyrin repeats, six transmembrane helices, a pore between S5 and S6, and cytoplasmic termini; four subunits assemble into the functional channel. A 2024 review places the selectivity filter at residues 643–646 with the sequence GMGD and reports 51 experimentally determined TRPV1 structures in the Protein Data Bank. These exact residue numbers derive from canonical TRPV1 and should not be assumed to have been independently mapped in G9DCX1. (amayarodriguez2024ajourneyfrom pages 6-8, grigore2024latestinsightsinto pages 3-5)

### 1.2 Evidence categories

Three evidence levels should be distinguished:

1. **Direct naked mole-rat evidence:** capsaicin responses in isolated DRG neurons and ex vivo C-fibers, expression/projections in sensory pathways, behavioral tests, and pathway-rescue experiments.
2. **Species-focused mechanistic synthesis:** normal intrinsic TRPV1 gating, TrkA hypofunction, neuropeptide deficiency, and NaV1.7-mediated acid adaptation, summarized from multiple naked mole-rat experiments.
3. **Canonical-family inference:** tetrameric architecture, preferential Ca2+ permeability, detailed pore geometry, and some lipid/pharmacological mechanisms. These are strongly expected for G9DCX1 from family/domain conservation but were not all measured directly on the G9DCX1 protein.

| Annotation topic | Best-supported conclusion | Evidence type | Key quantitative detail | Confidence/caveat |
|---|---|---|---|---|
| Identity | UniProt G9DCX1 is annotated as **Heterocephalus glaber Trpv1/TRPV1**, and the literature examined here consistently concerns naked mole-rat TRPV1 in nociceptors rather than a different same-symbol gene. Domain/family assignment matches canonical TRPV1 architecture with ankyrin-repeat N-terminus and transmembrane ion-channel core. (park2008selectiveinflammatorypain pages 9-10, amayarodriguez2024ajourneyfrom pages 6-8) | Direct H. glaber experiment + canonical TRPV1 inference | Canonical TRPV1 subunit length reported as **838 aa**; homotetramer with **6 TM segments** per subunit and intracellular ankyrin-repeat domains. (amayarodriguez2024ajourneyfrom pages 6-8) | High confidence for species/gene/family match; moderate caveat that the retrieved papers do not explicitly map their experimental clone to accession **G9DCX1**. |
| Channel function and transported ions | TRPV1 is a **non-selective cation channel** with preferential **Ca2+ permeability**; activation causes **Ca2+ influx** and membrane depolarization that can initiate nociceptor firing. Naked mole-rat TRPV1 is reported as functionally similar to mouse for core gating properties. (amayarodriguez2024ajourneyfrom pages 1-2, smith2020independentevolutionof pages 5-6) | Canonical TRPV1 inference + species-focused synthesis | Lower gate expansion in cryo-EM review from **5.3 Å to 7.6 Å** upon vanilloid-driven conformational change; selectivity filter residues **643–646 (GMGD)**. (amayarodriguez2024ajourneyfrom pages 6-8) | High confidence for general TRPV1 ion-channel function; moderate caveat because ion selectivity/permeability values were not measured directly in the retrieved naked mole-rat primary papers. |
| Activators | Naked mole-rat TRPV1 is activated by **capsaicin** and retains normal **heat, pH/proton, voltage, and capsaicin sensitivity** at the channel level; canonical TRPV1 is also activated by noxious heat and protons. (park2008selectiveinflammatorypain pages 4-6, smith2020independentevolutionof pages 5-6, amayarodriguez2024ajourneyfrom pages 1-2) | Direct H. glaber experiment + species-focused synthesis + canonical TRPV1 inference | In naked mole-rat C-fibers/CMH fibers, about **40%** responded to capsaicin over **10 nM–2 μM**; canonical thermal activation threshold cited as **>42–43°C**. (park2008selectiveinflammatorypain pages 4-6, grigore2024latestinsightsinto pages 3-5) | High confidence that capsaicin activates naked mole-rat TRPV1-positive neurons; caveat that whole-animal pain behavior does not mirror peripheral channel activation. |
| DRG / C-fiber / plasma-membrane / spinal localization | TRPV1 is expressed in naked mole-rat **DRG sensory neurons** and **cutaneous C-fibers**; canonical TRPV1 is mainly a **plasma-membrane** channel. In the spinal cord, naked mole-rat TRPV1-positive afferents project unusually strongly to **deep as well as superficial dorsal horn**. (park2008selectiveinflammatorypain pages 9-10, browe2020thenakedmolerat pages 1-2, amayarodriguez2024ajourneyfrom pages 1-2) | Direct H. glaber experiment + species-focused synthesis + canonical TRPV1 inference | Approx. **50% of deep dorsal horn neurons** receive capsaicin-sensitive input in naked mole-rat; TRPV1-positive profiles are more numerous in deep dorsal horn than in mouse. (park2008selectiveinflammatorypain pages 9-10) | High confidence for DRG/C-fiber/spinal pattern in H. glaber; moderate caveat that direct biochemical plasma-membrane trafficking assays for H. glaber TRPV1 were not retrieved here. |
| Capsaicin paradox | Naked mole-rats are behaviorally insensitive or markedly reduced in response to **capsaicin**, despite having **functionally capsaicin-responsive TRPV1-positive nociceptors**. The best-supported explanation is altered downstream pain circuitry and deficient peptidergic transmission, not loss of TRPV1 channel function. (park2008selectiveinflammatorypain pages 9-10, smith2020independentevolutionof pages 4-5, browe2020thenakedmolerat pages 1-2) | Direct H. glaber experiment + species-focused synthesis | Capsaicin-sensitive fibers robustly excite superficial dorsal horn neurons, yet behavioral capsaicin pain is absent; formalin phase I behavior was about **20% of mouse** in the 2008 study. (park2008selectiveinflammatorypain pages 4-6) | High confidence for the paradox; mechanism is strong but not fully closed—altered spinal connectivity and lack of neuropeptides are both implicated. |
| Acid / Nav1.7 mechanism | Acid insensitivity in naked mole-rat is **not** explained by absent TRPV1-like proton gating alone. Instead, low pH strongly blocks **NaV1.7/voltage-gated sodium channels**, preventing action-potential initiation even though proton-evoked TRPV1-like and ASIC-like inward currents can be present. (smith2020independentevolutionof pages 5-6) | Species-focused synthesis of direct H. glaber experiments | Naked mole-rats showed complete behavioral/cutaneous afferent insensitivity to **pH 6.0–5.0** acid challenge in the 2008 study; low pH was reported to inhibit mechanically evoked firing more strongly than in mice. (park2008selectiveinflammatorypain pages 4-6, smith2020independentevolutionof pages 5-6) | High confidence that enhanced proton block of sodium channels is central; caveat that acid sensing in other tissues (e.g., gut afferents) can differ from skin. |
| NGF–TrkA sensitization | Naked mole-rat TRPV1 fails to undergo normal **NGF/TrkA-dependent sensitization**, explaining loss of inflammatory thermal hyperalgesia despite a functional TRPV1 channel. The defect maps upstream to **hypofunctional TrkA**, not TRPV1 itself. (smith2020independentevolutionof pages 6-8, smith2020independentevolutionof pages 5-6, lewin2020williamd.willis pages 4-5) | Species-focused synthesis of direct H. glaber experiments | Reduced DRG expression versus mouse reported for **Trpv1 (P=0.0003)**, **TrkA/NTRK1 (P=0.0049)**, and **Prdm12 (P=0.0213)**; TrkA defect linked to **1–3 amino-acid substitutions** in the kinase domain. (lewin2020williamd.willis pages 5-7, smith2020independentevolutionof pages 6-8) | High confidence for impaired NGF–TrkA sensitization; caveat that reduced expression and altered signaling likely both contribute. |
| Applications / real-world relevance | Naked mole-rat TRPV1 biology is a valuable **comparative model** for analgesic discovery because it separates **peripheral nociceptor activation** from **pain behavior**. More broadly, TRPV1 remains an active therapeutic target in pain, osteoarthritis, respiratory disease, and neuromodulation. (browe2020thenakedmolerat pages 1-2, amayarodriguez2024ajourneyfrom pages 1-2) | Species-focused synthesis + canonical TRPV1 inference | Recent reviews note **51 TRPV1 structures** in the PDB and highlight therapeutic strategies including **TRPV1 agonists/antagonists**, with agonist-based approaches advancing further clinically because antagonists can cause hyperthermia/thermal hypesthesia. (amayarodriguez2024ajourneyfrom pages 6-8) | Moderate confidence for translational inference: application data are mainly from broader TRPV1 literature, not naked mole-rat intervention studies. |


*Table: This table summarizes the strongest evidence for functional annotation of naked mole-rat TRPV1 (UniProt G9DCX1), separating direct species-specific findings from broader canonical TRPV1 inferences. It is useful for quickly assessing what is experimentally established in H. glaber versus what is inferred from the conserved TRPV1 channel family.*

## 2. Molecular function: a polymodal cation channel

TRPV1 is not an enzyme and catalyzes no chemical reaction. Its primary molecular activity is **stimulus-gated passive transport of cations down their electrochemical gradients**. It is nonselective among cations but preferentially permeable to Ca2+; Na+ entry and Ca2+ entry depolarize the membrane, while Ca2+ also serves as a second messenger. In nociceptor endings, sufficient depolarization recruits voltage-gated channels and generates action potentials that propagate toward the spinal cord. (amayarodriguez2024ajourneyfrom pages 1-2)

Canonical TRPV1 is activated or potentiated by noxious heat—commonly reported above approximately 42–43°C—capsaicin and resiniferatoxin, extracellular protons, membrane voltage, endogenous lipids/endovanilloids, and inflammatory signaling. Capsaicin binds within a transmembrane vanilloid pocket involving S3, S4, and the S4–S5 linker. Structural analyses report lower-gate expansion from approximately 5.3 Å to 7.6 Å during vanilloid-associated activation. (amayarodriguez2024ajourneyfrom pages 6-8, amayarodriguez2024ajourneyfrom pages 1-2, grigore2024latestinsightsinto pages 3-5)

For naked mole-rat TRPV1 specifically, electrophysiology establishes robust capsaicin sensitivity in DRG neurons and polymodal cutaneous C-fibers. Approximately **40% of examined C-fibers/CMH fibers** responded over a capsaicin concentration range of **10 nM–2 μM**, with firing comparable to that evoked by other effective nociceptive stimuli. Later species-focused work concluded that naked mole-rat TRPV1 has essentially normal heat, pH, voltage, and capsaicin sensitivity relative to mouse orthologues. (smith2020independentevolutionof pages 5-6, park2008selectiveinflammatorypain pages 4-6, smith2020independentevolutionof pages 4-5)

Thus, the most defensible molecular annotation is:

> **A polymodal TRPV-family nonselective cation channel that detects capsaicin and noxious physicochemical conditions, producing Na+/Ca2+ influx, sensory-neuron depolarization, and Ca2+-dependent signaling.**

Direct G9DCX1-specific permeability ratios were not available in the retrieved studies; preferential Ca2+ permeability is a high-confidence family-level inference rather than a naked mole-rat-specific measurement.

## 3. Cellular and anatomical localization

### 3.1 Subcellular localization

The functional site is principally the **plasma membrane**, where the pore spans the lipid bilayer and admits extracellular cations. This localization follows directly from TRPV1’s transmembrane architecture and electrophysiological activity. Nevertheless, the retrieved naked mole-rat studies did not provide a dedicated surface-biotinylation or trafficking analysis of G9DCX1, so plasma-membrane localization in this species is supported mainly by functional membrane currents and conserved architecture rather than a G9DCX1-specific biochemical localization assay. (amayarodriguez2024ajourneyfrom pages 6-8, amayarodriguez2024ajourneyfrom pages 1-2)

### 3.2 Tissue and circuit localization

Direct evidence places naked mole-rat TRPV1 in:

- **Dorsal-root-ganglion sensory neurons**, including small nociceptive neurons;
- **Peripheral cutaneous C-fiber/polymodal nociceptor endings**, where capsaicin activates the afferent;
- **Central terminals in the spinal dorsal horn**, where these afferents transmit sensory signals. (park2008selectiveinflammatorypain pages 9-10, smith2020independentevolutionof pages 4-5, browe2020thenakedmolerat pages 1-2)

The spinal projection pattern is unusually important. In mice, TRPV1-positive afferents predominantly contact superficial dorsal-horn circuits. In naked mole-rats, they make substantial connections in both superficial and deep laminae; approximately **50% of sampled deep dorsal-horn neurons** received capsaicin-sensitive input, and TRPV1-positive profiles were more prominent in deep dorsal horn than in mice. This altered wiring is one proposed reason that strong peripheral TRPV1 activation does not produce normal pain behavior. (park2008selectiveinflammatorypain pages 9-10, smith2020independentevolutionof pages 5-6)

Reduced expression may additionally limit pathway gain. Comparative DRG analyses reported lower naked mole-rat expression of *Trpv1* (**P=0.0003**), *Ntrk1/TrkA* (**P=0.0049**), and the nociceptor-development regulator *Prdm12* (**P=0.0213**) than in mouse. These are relative-expression statistics, not evidence that *Trpv1* is absent. (lewin2020williamd.willis pages 5-7)

## 4. Biological processes and signaling pathways

### 4.1 Acute capsaicin nociception: intact receptor, attenuated behavioral output

Naked mole-rats present a striking receptor-to-behavior dissociation. Capsaicin robustly activates isolated DRG neurons and peripheral C-fibers, and capsaicin-sensitive afferents excite superficial dorsal-horn neurons. Nevertheless, capsaicin injection produces little or no typical nocifensive licking and fails to induce the expected thermal hyperalgesia. Therefore, behavioral capsaicin insensitivity cannot be annotated as defective ligand recognition by TRPV1. (park2008selectiveinflammatorypain pages 9-10, smith2020independentevolutionof pages 4-5, park2008selectiveinflammatorypain pages 1-2)

Two downstream mechanisms have the strongest support:

1. **Deficient peptidergic transmission.** Naked mole-rat cutaneous C-fibers have greatly reduced Substance P and CGRP-associated signaling. Intrathecal Substance P can restore capsaicin-evoked nocifensive behavior and thermal hyperalgesia, showing that upstream TRPV1 activation remains competent and that the central NK1 receptor machinery can function when supplied with ligand. NK1 receptors are concentrated in superficial dorsal horn. (browe2020thenakedmolerat pages 1-2, smith2020independentevolutionof pages 5-6, lewin2020williamd.willis pages 4-5)
2. **Altered dorsal-horn connectivity.** TRPV1-positive inputs are distributed unusually between superficial and deep laminae, potentially recruiting circuit interactions that fail to generate—or actively suppress—the normal nociceptive output. This explanation is plausible and experimentally supported anatomically, but the exact interneuronal mechanism remains unresolved. (smith2020independentevolutionof pages 5-6, park2008selectiveinflammatorypain pages 9-10, debus2021modelingmechanismsof pages 41-45)

The 2008 study also found formalin phase-I pain behavior at roughly **20% of mouse levels**, illustrating that the phenotype is selective attenuation rather than global absence of somatosensation. (park2008selectiveinflammatorypain pages 4-6)

### 4.2 Acid sensing: TRPV1 currents can be present, but spikes are blocked downstream

Early skin-nerve studies found complete failure of naked mole-rat cutaneous nociceptors to fire to approximately **pH 6.0–5.0**, paralleling absent acid-evoked pain behavior. Subsequent cellular work refined the mechanism: naked mole-rat DRG neurons can express proton-gated TRPV1-like and ASIC-like inward currents, and TRPV1 itself has normal proton sensitivity. The critical failure occurs because low extracellular pH unusually strongly inhibits voltage-gated sodium currents, especially NaV1.7, preventing receptor potentials from becoming propagated action potentials. Naked mole-rat NaV1.7 contains sequence changes that enhance proton block at physiologically relevant acidic pH. (smith2020independentevolutionof pages 5-6, park2008selectiveinflammatorypain pages 4-6)

Accordingly, G9DCX1 may detect protons at the channel level without causing pain under cutaneous acid challenge. This is an important annotation principle: **TRPV1 activation is necessary input, but neither sufficient for spike generation nor sufficient for behavioral pain in this species.** Acid responses may also differ by organ; therefore, findings in skin should not automatically be transferred to visceral afferents.

### 4.3 NGF–TrkA–TRPV1 inflammatory sensitization

In typical mammalian nociceptors, inflammatory NGF activates TrkA signaling, which increases TRPV1 activity and trafficking and thereby promotes thermal hyperalgesia. Naked mole-rats lack this normal NGF-induced thermal sensitization. Their TRPV1 channel can be sensitized when placed in an appropriate heterologous cellular context, indicating that the defect lies primarily upstream or in the native signaling environment rather than in the channel. (smith2020independentevolutionof pages 6-8, smith2020independentevolutionof pages 5-6, lewin2020williamd.willis pages 4-5)

The principal lesion is a **hypofunctional TrkA intracellular kinase domain**, associated with one to three unusual amino-acid substitutions and reduced activation-dependent phosphopeptide abundance. Cultured naked mole-rat DRG neurons consequently fail to show normal NGF-induced TRPV1 sensitization. This pathway defect, reduced expression of nociceptor-development genes, and adult loss/paucity of cutaneous C-fibers together explain diminished inflammatory thermal pain more convincingly than any intrinsic TRPV1 defect. (smith2020independentevolutionof pages 6-8, lewin2020williamd.willis pages 5-7)

### 4.4 Itch and neurogenic inflammation

TRPV1-positive sensory neurons also participate in histamine itch and neuropeptide release in other mammals. Naked mole-rat histamine-sensitive DRG neurons are frequently capsaicin-sensitive, yet histamine does not normally provoke scratching. Intrathecal Substance P restores histamine-induced scratching, again localizing the functional interruption downstream of peripheral TRPV1-positive afferent activation. (smith2020independentevolutionof pages 5-6)

Canonical TRPV1-mediated Ca2+ entry can drive release of Substance P and CGRP, producing neurogenic inflammation. In the naked mole-rat, the scarcity of these peptides means this usual output is strongly attenuated even though channel opening occurs. (browe2020thenakedmolerat pages 1-2, grigore2024latestinsightsinto pages 3-5)

## 5. Recent developments, 2023–2024

Recent literature has not substantially revised the species-specific conclusion that naked mole-rat TRPV1 is functional and that analgesic adaptations lie largely downstream or upstream in sensitization pathways. Rather, 2023–2024 work has sharpened the broader structural and translational context:

- A January 2024 review integrated cryo-EM structures, ligand pockets, physiology, and computational drug discovery. It emphasized TRPV1’s tetrameric six-transmembrane architecture, preferential Ca2+ permeability, polymodal gating, and the availability of **51 PDB structures**, enabling structure-based and machine-learning approaches to modulator discovery. Publication: Amaya-Rodriguez et al., *Frontiers in Pharmacology*, January 2024; DOI/URL: https://doi.org/10.3389/fphar.2023.1251061. (amayarodriguez2024ajourneyfrom pages 6-8, amayarodriguez2024ajourneyfrom pages 1-2)
- Recent structural work shows that phosphoinositides and inflammatory lipids occupy regulatory sites in the TRPV1 transmembrane core. This supports a modern view of TRPV1 not as a simple heat/capsaicin switch but as an allosteric integrator of thermal, chemical, voltage, and inflammatory inputs. The inference is highly relevant to G9DCX1’s family membership, although naked mole-rat-specific lipid regulation was not tested in the retrieved work. (amayarodriguez2024ajourneyfrom pages 6-8, amayarodriguez2024ajourneyfrom pages 1-2)
- A 2024 synthesis of murine wound-healing studies highlighted TRPV1 expression in keratinocytes and immune cells and its coupling to Ca2+ influx and neuropeptide-mediated inflammation. These non-neuronal roles should **not** yet be assigned confidently to G9DCX1 in naked mole-rat because direct species-specific localization was not retrieved. Publication: Grigore et al., June 2024; DOI/URL: https://doi.org/10.3390/ijms25126753. (grigore2024latestinsightsinto pages 3-5)

Thus, the latest research strengthens structural and drug-discovery interpretation but does not justify transferring every human or mouse tissue function to naked mole-rat TRPV1.

## 6. Applications and expert analysis

### Comparative model for analgesic discovery

The naked mole-rat provides a natural “pathway dissection” model in which a sensory receptor remains functional while pain behavior is selectively suppressed. This reveals several potential analgesic strategies beyond direct TRPV1 blockade:

- Reduce NGF–TrkA-dependent sensitization rather than abolish basal heat detection;
- Interfere selectively with peptidergic transmission from TRPV1-positive nociceptors;
- Reproduce acid-enhanced inhibition of NaV1.7 to prevent acidosis-evoked firing;
- Modulate spinal routing or gain downstream of intact peripheral transduction. (browe2020thenakedmolerat pages 1-2, smith2020independentevolutionof pages 6-8, smith2020independentevolutionof pages 5-6, lewin2020williamd.willis pages 4-5)

This is translationally attractive because conventional TRPV1 antagonists can impair protective heat sensation and disturb thermoregulation. Conversely, strong or prolonged TRPV1 agonism with capsaicin-like molecules can desensitize or defunctionalize nociceptor terminals and is already exploited in pain-directed pharmacology. The naked mole-rat suggests that uncoupling nociceptor activation from central pain transmission may be another route to analgesia without eliminating the receptor’s sensory function. (amayarodriguez2024ajourneyfrom pages 6-8, amayarodriguez2024ajourneyfrom pages 1-2)

### Interpretation of expert opinion

The species-focused consensus is that it is misleading to call naked mole-rat TRPV1 “nonfunctional.” A more precise statement is that **the TRPV1-expressing peptidergic pain pathway is functionally attenuated at the systems level**, while the channel itself retains core gating function. Authors also caution that altered spinal connectivity is not yet a complete mechanistic explanation; peptide deficiency, developmental loss of C-fibers, TrkA hypofunction, and stimulus-specific sodium-channel inhibition all contribute. (debus2021modelingmechanismsof pages 41-45, browe2020thenakedmolerat pages 1-2, smith2020independentevolutionof pages 6-8, smith2020independentevolutionof pages 5-6)

## 7. Recommended functional annotation

**Molecular function:** Polymodal, capsaicin- and noxious-stimulus-gated nonselective cation channel; conducts Na+ and Ca2+, with preferential Ca2+ permeability inferred from canonical TRPV1, causing membrane depolarization and intracellular Ca2+ signaling.

**Biological process:** Peripheral detection of capsaicin, noxious heat, and acidic/inflammatory conditions in nociceptive sensory neurons; contributes to action-potential initiation, spinal sensory transmission, thermal nociception, and inflammatory sensitization. In *H. glaber*, these outputs are strongly modified by NaV1.7 proton block, deficient peptidergic signaling, altered dorsal-horn connectivity, and hypofunctional NGF–TrkA signaling.

**Localization:** Primarily plasma membrane of DRG nociceptors and their peripheral C-fiber endings and central spinal terminals. Direct species evidence is strongest for DRG neurons, cutaneous C-fibers, and superficial/deep dorsal-horn projections; detailed G9DCX1 trafficking and non-neuronal localization remain insufficiently characterized.

**Confidence:** High for identity, family assignment, capsaicin-gated channel activity, and sensory-neuron localization; moderate-to-high for normal intrinsic heat/proton gating based on species-focused experimental synthesis; high for downstream pathway explanations of acid and inflammatory pain attenuation; moderate for exact G9DCX1 pore/permeability details because these are inferred from conserved mammalian TRPV1 rather than measured directly.

## Key references

1. Park TJ et al. “Selective Inflammatory Pain Insensitivity in the African Naked Mole-Rat (*Heterocephalus glaber*).” *PLoS Biology* 6:e13. Published January 2008. https://doi.org/10.1371/journal.pbio.0060013. (park2008selectiveinflammatorypain pages 9-10, park2008selectiveinflammatorypain pages 4-6)
2. Smith ESJ, Park TJ, Lewin GR. “Independent evolution of pain insensitivity in African mole-rats: origins and mechanisms.” *Journal of Comparative Physiology A* 206:313–325. Published March 2020. https://doi.org/10.1007/s00359-020-01414-w. (smith2020independentevolutionof pages 5-6, smith2020independentevolutionof pages 6-8)
3. Browe BM et al. “The naked mole-rat has a functional purinergic pain pathway despite having a non-functional peptidergic pain pathway.” *Neurobiology of Pain* 8:100047. Published May 2020. https://doi.org/10.1016/j.ynpai.2020.100047. (browe2020thenakedmolerat pages 1-2, browe2020thenakedmolerat pages 11-12)
4. Lewin GR. “The evolutionary history of nerve growth factor and nociception.” *Pain* 161:S36–S47. Published September 2020. https://doi.org/10.1097/j.pain.0000000000001889. (lewin2020williamd.willis pages 4-5, lewin2020williamd.willis pages 5-7)
5. Amaya-Rodriguez CA et al. “A journey from molecule to physiology and in silico tools for drug discovery targeting the TRPV1 channel.” *Frontiers in Pharmacology* 14. Published January 2024. https://doi.org/10.3389/fphar.2023.1251061. (amayarodriguez2024ajourneyfrom pages 6-8, amayarodriguez2024ajourneyfrom pages 1-2)
6. Grigore A et al. “Latest Insights into the In Vivo Studies in Murine Regarding the Role of TRP Channels in Wound Healing—A Review.” *International Journal of Molecular Sciences* 25:6753. Published June 2024. https://doi.org/10.3390/ijms25126753. (grigore2024latestinsightsinto pages 3-5)

References

1. (smith2020independentevolutionof pages 5-6): Ewan St. John Smith, Thomas J. Park, and Gary R. Lewin. Independent evolution of pain insensitivity in african mole-rats: origins and mechanisms. Journal of Comparative Physiology. A, Neuroethology, Sensory, Neural, and Behavioral Physiology, 206:313-325, Mar 2020. URL: https://doi.org/10.1007/s00359-020-01414-w, doi:10.1007/s00359-020-01414-w. This article has 28 citations.

2. (park2008selectiveinflammatorypain pages 9-10): Thomas J Park, Ying Lu, René Jüttner, Ewan St. J Smith, Jing Hu, Antje Brand, Christiane Wetzel, Nevena Milenkovic, Bettina Erdmann, Paul A Heppenstall, Charles E Laurito, Steven P Wilson, and Gary R Lewin. Selective inflammatory pain insensitivity in the african naked mole-rat (heterocephalus glaber). PLoS Biology, 6(1):e13, Jan 2008. URL: https://doi.org/10.1371/journal.pbio.0060013, doi:10.1371/journal.pbio.0060013. This article has 159 citations and is from a highest quality peer-reviewed journal.

3. (browe2020thenakedmolerat pages 1-2): Brigitte M Browe, Abigail R Olsen, Cesar Ramirez, Rebecca H Rickman, Ewan St John Smith, and Thomas J Park. The naked mole-rat has a functional purinergic pain pathway despite having a non-functional peptidergic pain pathway. Neurobiology of Pain, May 2020. URL: https://doi.org/10.1016/j.ynpai.2020.100047, doi:10.1016/j.ynpai.2020.100047. This article has 11 citations.

4. (smith2020independentevolutionof pages 6-8): Ewan St. John Smith, Thomas J. Park, and Gary R. Lewin. Independent evolution of pain insensitivity in african mole-rats: origins and mechanisms. Journal of Comparative Physiology. A, Neuroethology, Sensory, Neural, and Behavioral Physiology, 206:313-325, Mar 2020. URL: https://doi.org/10.1007/s00359-020-01414-w, doi:10.1007/s00359-020-01414-w. This article has 28 citations.

5. (park2008selectiveinflammatorypain pages 4-6): Thomas J Park, Ying Lu, René Jüttner, Ewan St. J Smith, Jing Hu, Antje Brand, Christiane Wetzel, Nevena Milenkovic, Bettina Erdmann, Paul A Heppenstall, Charles E Laurito, Steven P Wilson, and Gary R Lewin. Selective inflammatory pain insensitivity in the african naked mole-rat (heterocephalus glaber). PLoS Biology, 6(1):e13, Jan 2008. URL: https://doi.org/10.1371/journal.pbio.0060013, doi:10.1371/journal.pbio.0060013. This article has 159 citations and is from a highest quality peer-reviewed journal.

6. (smith2020independentevolutionof pages 4-5): Ewan St. John Smith, Thomas J. Park, and Gary R. Lewin. Independent evolution of pain insensitivity in african mole-rats: origins and mechanisms. Journal of Comparative Physiology. A, Neuroethology, Sensory, Neural, and Behavioral Physiology, 206:313-325, Mar 2020. URL: https://doi.org/10.1007/s00359-020-01414-w, doi:10.1007/s00359-020-01414-w. This article has 28 citations.

7. (amayarodriguez2024ajourneyfrom pages 6-8): Cesar A. Amaya-Rodriguez, Karina Carvajal-Zamorano, Daniel Bustos, Melissa Alegría-Arcos, and Karen Castillo. A journey from molecule to physiology and in silico tools for drug discovery targeting the transient receptor potential vanilloid type 1 (trpv1) channel. Frontiers in Pharmacology, Jan 2024. URL: https://doi.org/10.3389/fphar.2023.1251061, doi:10.3389/fphar.2023.1251061. This article has 28 citations.

8. (grigore2024latestinsightsinto pages 3-5): Alexandra Grigore, Oana Andreia Coman, Horia Păunescu, Mihnea Costescu, and Ion Fulga. Latest insights into the in vivo studies in murine regarding the role of trp channels in wound healing—a review. Jun 2024. URL: https://doi.org/10.3390/ijms25126753, doi:10.3390/ijms25126753. This article has 7 citations.

9. (amayarodriguez2024ajourneyfrom pages 1-2): Cesar A. Amaya-Rodriguez, Karina Carvajal-Zamorano, Daniel Bustos, Melissa Alegría-Arcos, and Karen Castillo. A journey from molecule to physiology and in silico tools for drug discovery targeting the transient receptor potential vanilloid type 1 (trpv1) channel. Frontiers in Pharmacology, Jan 2024. URL: https://doi.org/10.3389/fphar.2023.1251061, doi:10.3389/fphar.2023.1251061. This article has 28 citations.

10. (lewin2020williamd.willis pages 4-5): Gary R. Lewin. William d. willis, jr, md, phd memorial lecture: the evolutionary history of nerve growth factor and nociception. Sep 2020. URL: https://doi.org/10.1097/j.pain.0000000000001889, doi:10.1097/j.pain.0000000000001889. This article has 10 citations and is from a highest quality peer-reviewed journal.

11. (lewin2020williamd.willis pages 5-7): Gary R. Lewin. William d. willis, jr, md, phd memorial lecture: the evolutionary history of nerve growth factor and nociception. Sep 2020. URL: https://doi.org/10.1097/j.pain.0000000000001889, doi:10.1097/j.pain.0000000000001889. This article has 10 citations and is from a highest quality peer-reviewed journal.

12. (park2008selectiveinflammatorypain pages 1-2): Thomas J Park, Ying Lu, René Jüttner, Ewan St. J Smith, Jing Hu, Antje Brand, Christiane Wetzel, Nevena Milenkovic, Bettina Erdmann, Paul A Heppenstall, Charles E Laurito, Steven P Wilson, and Gary R Lewin. Selective inflammatory pain insensitivity in the african naked mole-rat (heterocephalus glaber). PLoS Biology, 6(1):e13, Jan 2008. URL: https://doi.org/10.1371/journal.pbio.0060013, doi:10.1371/journal.pbio.0060013. This article has 159 citations and is from a highest quality peer-reviewed journal.

13. (debus2021modelingmechanismsof pages 41-45): Karlien Y. Debus. Modeling mechanisms of nociception using the african mole-rat family. ArXiv, Jan 2021. URL: https://doi.org/10.17169/refubium-29110, doi:10.17169/refubium-29110. This article has 0 citations.

14. (browe2020thenakedmolerat pages 11-12): Brigitte M Browe, Abigail R Olsen, Cesar Ramirez, Rebecca H Rickman, Ewan St John Smith, and Thomas J Park. The naked mole-rat has a functional purinergic pain pathway despite having a non-functional peptidergic pain pathway. Neurobiology of Pain, May 2020. URL: https://doi.org/10.1016/j.ynpai.2020.100047, doi:10.1016/j.ynpai.2020.100047. This article has 11 citations.

## Artifacts

- [Edison artifact artifact-00](Trpv1-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. amayarodriguez2024ajourneyfrom pages 6-8
2. park2008selectiveinflammatorypain pages 9-10
3. park2008selectiveinflammatorypain pages 4-6
4. smith2020independentevolutionof pages 5-6
5. amayarodriguez2024ajourneyfrom pages 1-2
6. grigore2024latestinsightsinto pages 3-5
7. browe2020thenakedmolerat pages 1-2
8. smith2020independentevolutionof pages 6-8
9. smith2020independentevolutionof pages 4-5
10. park2008selectiveinflammatorypain pages 1-2
11. debus2021modelingmechanismsof pages 41-45
12. browe2020thenakedmolerat pages 11-12
13. https://doi.org/10.3389/fphar.2023.1251061.
14. https://doi.org/10.3390/ijms25126753.
15. https://doi.org/10.1371/journal.pbio.0060013.
16. https://doi.org/10.1007/s00359-020-01414-w.
17. https://doi.org/10.1016/j.ynpai.2020.100047.
18. https://doi.org/10.1097/j.pain.0000000000001889.
19. https://doi.org/10.1007/s00359-020-01414-w,
20. https://doi.org/10.1371/journal.pbio.0060013,
21. https://doi.org/10.1016/j.ynpai.2020.100047,
22. https://doi.org/10.3389/fphar.2023.1251061,
23. https://doi.org/10.3390/ijms25126753,
24. https://doi.org/10.1097/j.pain.0000000000001889,
25. https://doi.org/10.17169/refubium-29110,