---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-27T15:53:07.144285'
end_time: '2026-09-27T16:01:44.940153'
duration_seconds: 517.8
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: worm
  gene_id: unc-2
  gene_symbol: unc-2
  uniprot_accession: G5EFB0
  protein_description: 'RecName: Full=Voltage-dependent calcium channel type A subunit
    alpha-1 {ECO:0000256|ARBA:ARBA00069462};'
  gene_info: Name=unc-2 {ECO:0000313|EMBL:CCD74384.2, ECO:0000313|WormBase:T02C5.5a};
    ORFNames=CELE_T02C5.5 {ECO:0000313|EMBL:CCD74384.2}, T02C5.5 {ECO:0000313|WormBase:T02C5.5a};
  organism_full: Caenorhabditis elegans.
  protein_family: Belongs to the calcium channel alpha-1 subunit
  protein_domains: EF_hand_dom. (IPR002048); GPHH_dom. (IPR031649); Ion_trans_dom.
    (IPR005821); VDCC_a1su_IQ. (IPR014873); VDCC_alpha-1_subunit. (IPR050599)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 38
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: unc-2-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** G5EFB0
- **Protein Description:** RecName: Full=Voltage-dependent calcium channel type A subunit alpha-1 {ECO:0000256|ARBA:ARBA00069462};
- **Gene Information:** Name=unc-2 {ECO:0000313|EMBL:CCD74384.2, ECO:0000313|WormBase:T02C5.5a}; ORFNames=CELE_T02C5.5 {ECO:0000313|EMBL:CCD74384.2}, T02C5.5 {ECO:0000313|WormBase:T02C5.5a};
- **Organism (full):** Caenorhabditis elegans.
- **Protein Family:** Belongs to the calcium channel alpha-1 subunit
- **Key Domains:** EF_hand_dom. (IPR002048); GPHH_dom. (IPR031649); Ion_trans_dom. (IPR005821); VDCC_a1su_IQ. (IPR014873); VDCC_alpha-1_subunit. (IPR050599)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "unc-2" matches the protein description above**
2. **Verify the organism is correct:** Caenorhabditis elegans.
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'unc-2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **unc-2** (gene ID: unc-2, UniProt: G5EFB0) in worm.

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
- **UniProt Accession:** G5EFB0
- **Protein Description:** RecName: Full=Voltage-dependent calcium channel type A subunit alpha-1 {ECO:0000256|ARBA:ARBA00069462};
- **Gene Information:** Name=unc-2 {ECO:0000313|EMBL:CCD74384.2, ECO:0000313|WormBase:T02C5.5a}; ORFNames=CELE_T02C5.5 {ECO:0000313|EMBL:CCD74384.2}, T02C5.5 {ECO:0000313|WormBase:T02C5.5a};
- **Organism (full):** Caenorhabditis elegans.
- **Protein Family:** Belongs to the calcium channel alpha-1 subunit
- **Key Domains:** EF_hand_dom. (IPR002048); GPHH_dom. (IPR031649); Ion_trans_dom. (IPR005821); VDCC_a1su_IQ. (IPR014873); VDCC_alpha-1_subunit. (IPR050599)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "unc-2" matches the protein description above**
2. **Verify the organism is correct:** Caenorhabditis elegans.
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'unc-2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **unc-2** (gene ID: unc-2, UniProt: G5EFB0) in worm.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation report: *C. elegans unc-2* / UNC-2 (UniProt G5EFB0)

## Executive conclusion

The requested identity is verified. **G5EFB0 corresponds to *Caenorhabditis elegans unc-2* (T02C5.5), not to an unrelated same-symbol gene.** The literature consistently identifies UNC-2 as the worm’s sole **CaV2-family voltage-gated calcium-channel α1 subunit**, distinct from EGL-19/CaV1 and CCA-1/CaV3. Its primary function is to form the voltage-sensing, Ca²⁺-selective pore of a presynaptic channel complex. Neuronal depolarization opens UNC-2-containing channels; inward Ca²⁺ then triggers synaptic-vesicle exocytosis, particularly from vesicles docked beside the active-zone dense projection. Thus, UNC-2 is best annotated as a **presynaptic excitation–secretion coupling channel**, rather than an enzyme, structural protein, or transporter of an organic substrate. (mathews2009molecularandgenetic pages 202-206, saheki2009presynapticcav2calcium pages 1-3, mathews2009molecularandgenetic pages 132-136)

| Topic | Current conclusion | Strongest evidence/method | Key quantitative result | Source/date/DOI URL |
|---|---|---|---|---|
| Identity and architecture | G5EFB0 is the *Caenorhabditis elegans* UNC-2/T02C5.5 voltage-gated Ca²⁺-channel α1 subunit. It has four homologous six-transmembrane repeats, S4 voltage sensors, S5–S6 pore loops, a β-subunit-binding region, and a C-terminal EF-hand-like region. “N/P/Q-like” denotes CaV2 homology and function, not an experimentally established vertebrate pharmacological subtype. | Molecular cloning, conserved-motif analysis, sequence comparison, and mutant characterization. | Predicted protein: 1,992 aa and approximately 227 kDa; gene spans approximately 25 kb and 28 exons. | Mathews et al., 2003/2009 (mathews2009molecularandgenetic pages 202-206, mathews2009molecularandgenetic pages 132-136, mathews2009molecularandgenetic pages 196-202); [DOI](https://doi.org/10.1523/JNEUROSCI.23-16-06537.2003) |
| Primary molecular function | UNC-2 is the pore-forming component of a high-voltage-activated CaV2 channel. Depolarization opens it, permitting inward Ca²⁺ flux that triggers presynaptic vesicle exocytosis. | Sequence and pore-mutant analysis, calcium-current measurements, synaptic electrophysiology, and loss- and gain-of-function genetics. | Pore-dead D726A produced evoked responses comparable to an *unc-2* null at 1 mM extracellular Ca²⁺. | Huang et al., 2019; Xiong et al., August 2024 (huang2019gainoffunctionmutationsin pages 16-18, xiong2024presynapticneuronsselftune pages 4-4); [2019 DOI](https://doi.org/10.7554/eLife.45905); [2024 DOI](https://doi.org/10.1073/pnas.2404969121) |
| Localization | UNC-2 is predominantly neuronal and is enriched in the presynaptic plasma membrane at active zones of sensory, cholinergic, and GABAergic neurons. | Functional GFP-tagged rescue, endogenous CRISPR tagging, colocalization, and super-resolution imaging. | CaV2 clusters were approximately 297 nm in diameter and spaced 1.10 ± 0.16 μm apart. | Saheki and Bargmann, August 2009; Mueller et al., February 2023 (saheki2009presynapticcav2calcium pages 1-3, mueller2023cav1andcav2 pages 9-10, mueller2023cav1andcav2 pages 10-12); [2009 DOI](https://doi.org/10.1038/nn.2383); [2023 DOI](https://doi.org/10.7554/eLife.81407) |
| Trafficking and auxiliary subunits | CALF-1 promotes ER exit. CCB-1/β and UNC-36/α2δ are not obligatory for UNC-2 ER exit or active-zone delivery: low levels arrive without them, after which auxiliary subunits stabilize and expand the complex. In *unc-36* mutants, unstable UNC-2 undergoes endophilin-dependent endocytic degradation. | ER-retention experiments, inducible trafficking, endogenous tagging, auxiliary-subunit mutants, and degradation/endocytosis perturbations. | UNC-2 remained detectable at active zones without CCB-1 or UNC-36; blocking endocytosis partially restored channel puncta in *unc-36* mutants. | Saheki and Bargmann, August 2009; Oh et al., May 2023 (saheki2009presynapticcav2calcium pages 1-3, oh2023activezonetrafficking pages 1-2, oh2023activezonetrafficking pages 10-11); [2009 DOI](https://doi.org/10.1038/nn.2383); [2023 DOI](https://doi.org/10.1523/JNEUROSCI.2264-22.2023) |
| Active-zone scaffolds | UNC-10/RIM is a major determinant of UNC-2 clustering. SYD-2/Liprin-α organizes UNC-10, RIMB-1/RIM-BP, and ELKS-1, which provide partially redundant channel-localization routes. | Forward genetics, endogenous tagging, quantitative imaging, combinatorial mutants, and domain-deletion rescue. | UNC-10 abundance was comparable to UNC-2; SYD-2 and ELKS-1 were approximately twofold and RIMB-1 approximately fourfold more abundant at active zones. | Kushibiki et al., September 2019; Oh et al., 2021 (oh2021unc2cav2channel pages 1-5, oh2021unc2cav2channel pages 8-11, kushibiki2019rimb1rimbindingproteinand pages 1-2); [2019 DOI](https://doi.org/10.1523/JNEUROSCI.0506-19.2019) |
| Distinct vesicle pools | UNC-2/CaV2 clusters with UNC-13L at the dense projection and releases a tightly coupled central vesicle pool. EGL-19/CaV1 is dispersed laterally, associates with UNC-13S, and relies more strongly on ryanodine-receptor signaling. | Super-resolution imaging, electrophysiology, optogenetic stimulation, and high-pressure-freeze electron microscopy. | Estimated 101 ± 16 UNC-2 channels per synapse; 99.7% of CaV2 localizations were within 100 nm of UNC-13; direct fusion occurred within 33 nm of the dense projection, with store-amplified effects extending to 165 nm. | Mueller et al., February 2023 (mueller2023cav1andcav2 pages 12-15, mueller2023cav1andcav2 pages 15-18, mueller2023cav1andcav2 pages 7-9, mueller2023cav1andcav2 pages 1-2); [DOI](https://doi.org/10.7554/eLife.81407) |
| GABA_A-receptor retrograde feedback | Clustered postsynaptic UNC-49/GABA_A receptors provide input-specific retrograde feedback that recruits or stabilizes presynaptic UNC-2 at GABAergic neuromuscular junctions. | Cell-specific deletion, endogenous imaging, neuronal voltage clamp, and receptor-clustering mutants. | Loss of muscle UNC-49 reduced both UNC-2 current and punctum intensity by 32%, without changing potassium current, resting potential, or input resistance. | Zhao et al., October 2023 (zhao2023postsynapticgabaareceptors pages 5-7, zhao2023postsynapticgabaareceptors pages 1-3); [DOI](https://doi.org/10.1016/j.celrep.2023.113161) |
| Homeostatic abundance regulation | UNC-2 abundance varies inversely with channel activity and vesicle-exocytosis efficiency. WWP-1, a HECT E3 ubiquitin ligase, promotes UNC-2 ubiquitination and limits presynaptic abundance. | GFP-calibrated endogenous imaging, pore-dead and gain-of-function knock-ins, electrophysiology, forward genetics, and ubiquitination analysis. | Approximately 100 UNC-2 channels per synapse; D726A increased punctum intensity, whereas gain-of-function S240L decreased it; several comparisons had p < 0.0001. | Xiong et al., August 2024 (xiong2024presynapticneuronsselftune pages 2-3, xiong2024presynapticneuronsselftune pages 4-4); [DOI](https://doi.org/10.1073/pnas.2404969121) |


*Table: Evidence table summarizing the verified identity, molecular function, localization, regulation, and recent mechanistic findings for *C. elegans* UNC-2. It distinguishes homology-based channel classification from experimentally demonstrated properties.*

## 1. Identity, nomenclature, and structural class

The supplied UniProt identifiers—G5EFB0, *unc-2*, CELE_T02C5.5/T02C5.5, and *C. elegans*—are mutually consistent with the research literature. Molecular work assigns *unc-2* to a roughly 25-kb, 28-exon locus encoding a predicted 1,992-residue, approximately 227-kDa protein. UNC-2 has the canonical α1-subunit organization of voltage-gated calcium channels: four homologous repeats (I–IV), each with six membrane-spanning segments; positively charged S4 voltage sensors; S5–S6 pore-forming regions; conserved pore glutamates supporting Ca²⁺ selectivity; an intracellular β-subunit-interaction region; and a C-terminal EF-hand-like regulatory region. These features agree with the supplied Ion_trans, VDCC α1, IQ/EF-hand, and related domain annotations. (mathews2009molecularandgenetic pages 202-206, mathews2009molecularandgenetic pages 132-136, mathews2009molecularandgenetic pages 196-202)

Phylogenetic and functional evidence places UNC-2 among high-voltage-activated, non-L-type CaV2 channels related to vertebrate N-, P/Q-, and R-type channels. It is often called “P/Q-type” or “N/P/Q-type” in worm papers, but that wording should be interpreted as **orthology and functional-class shorthand**, not proof that the worm channel has exactly one vertebrate pharmacological subtype. UNC-2 lacks key L-type dihydropyridine-binding determinants. EGL-19 is the principal worm CaV1/L-type channel, whereas CCA-1 is CaV3/T-type and low-voltage activated. (mathews2009molecularandgenetic pages 202-206, saheki2009presynapticcav2calcium pages 1-3, mathews2009molecularandgenetic pages 196-202, frøkjærjensen2003cameleonimagingof pages 6-11)

## 2. Primary molecular function

UNC-2 is the **pore-forming α1 component of a voltage-gated Ca²⁺ channel**. Its transported substrate is the calcium ion. Membrane depolarization moves the S4 voltage sensors, opens the pore, and allows extracellular Ca²⁺ to enter the presynaptic terminal down its electrochemical gradient. This local Ca²⁺ signal activates the vesicle-fusion machinery and couples neuronal electrical activity to neurotransmitter secretion. The four conserved pore-loop glutamates and overall CaV architecture provide strong structural evidence for calcium selectivity; genetic, calcium-current, and synaptic electrophysiology experiments provide functional support. (mathews2009molecularandgenetic pages 132-136, frøkjærjensen2003cameleonimagingof pages 6-11)

UNC-2 is high-voltage activated rather than a low-threshold pacemaker channel. Gain-of-function variants can activate at more negative potentials and inactivate less, increasing Ca²⁺ entry. Conversely, the pore-domain D726A loss-of-function variant produces evoked responses comparable to an *unc-2* null at 1 mM extracellular Ca²⁺. These findings directly link channel conductance to presynaptic output. (huang2019gainoffunctionmutationsin pages 16-18, xiong2024presynapticneuronsselftune pages 4-4)

## 3. Cellular and subcellular localization

UNC-2 acts predominantly in neurons. Functional GFP-tagged UNC-2 rescues mutant locomotion and localizes with synaptic markers in sensory neurons, cholinergic motor neurons, and GABAergic motor neurons. Endogenous tagging and super-resolution imaging place it in the **presynaptic plasma membrane at active zones**, rather than diffusely throughout the neuron. (saheki2009presynapticcav2calcium pages 1-3, oh2021unc2cav2channel pages 1-5)

At neuromuscular junctions, UNC-2 forms compact clusters associated with the dense projection. One 2023 analysis measured clusters approximately 297 nm in diameter, spaced 1.10 ± 0.16 μm apart; ELKS clusters were approximately 294 nm across. Fluorescence calibration independently estimated about 100–101 UNC-2 molecules per synapse, although abundance varies among synapses. UNC-2 is therefore concentrated into active-zone channel assemblies rather than uniformly distributed over the bouton. (xiong2024presynapticneuronsselftune pages 2-3, mueller2023cav1andcav2 pages 15-18, mueller2023cav1andcav2 pages 9-10, mueller2023cav1andcav2 pages 10-12)

A minor role outside canonical neuronal active zones cannot be excluded, and *unc-2* expression has been reported in additional excitable cells. Nevertheless, the strongest direct functional and localization evidence supports presynaptic neuronal active zones as its principal site of action.

## 4. Channel biogenesis, trafficking, and auxiliary subunits

UNC-2 functions in a multiprotein channel complex that includes the β subunit CCB-1 and α2δ subunit UNC-36. Earlier work showed that CALF-1, an ER-localized neuronal membrane protein, and UNC-36 promote efficient UNC-2 export from the ER: in *calf-1* mutants, UNC-2 is retained in the ER while synaptic vesicles and other active-zone components still reach synapses. Acute CALF-1 expression mobilizes pre-existing UNC-2, supporting a direct trafficking role. (saheki2009presynapticcav2calcium pages 1-3)

A 2023 endogenous-tagging study refined this model. CCB-1 and UNC-36 are **not absolutely required** for UNC-2 to leave the ER, travel down the axon, or reach active zones: reduced amounts of UNC-2 still arrive in either auxiliary-subunit mutant. Neither auxiliary subunit obligatorily coassembles with UNC-2 in the ER. Instead, UNC-2 can traffic first and subsequently recruit CCB-1 and UNC-36 at terminals, where they stabilize and expand the channel complex. In *unc-36* mutants, unstable presynaptic UNC-2 undergoes endophilin-dependent endocytic degradation; disrupting endocytosis partially restores UNC-2 puncta. Thus, auxiliary subunits increase functional channel abundance and stability more than they serve as indispensable transport escorts. (oh2023activezonetrafficking pages 1-2, oh2023activezonetrafficking pages 10-11)

These results reconcile the earlier and newer observations: CALF-1 and UNC-36 strongly improve efficient maturation and accumulation, but the α1 subunit retains some autonomous trafficking capacity.

## 5. Active-zone anchoring and molecular partners

UNC-2 localization is organized by a redundant active-zone scaffold rather than one unique tether:

- **UNC-10/RIM** is a major determinant of channel clustering; *unc-10* mutants have fewer and dimmer UNC-2 puncta.
- **SYD-2/Liprin-α** is a central organizer that promotes the localization of UNC-10, RIMB-1/RIM-binding protein, and ELKS-1.
- **RIMB-1 and ELKS-1** provide partially overlapping routes that become especially important in combined mutants.
- **UNC-104/KIF1A** supports axonal delivery of UNC-2 and active-zone proteins.

Quantitative endogenous imaging found UNC-10 abundance similar to UNC-2, SYD-2 and ELKS-1 approximately twice as abundant, and RIMB-1 approximately four times as abundant at active zones. RIMB-1 and UNC-10 act redundantly, while the RIMB-1 C-terminal SH3 domain is functionally important for UNC-2 localization. The relationship is partly bidirectional because UNC-2 also helps refine RIMB-1 localization. (oh2021unc2cav2channel pages 1-5, oh2021unc2cav2channel pages 8-11, kushibiki2019rimb1rimbindingproteinand pages 1-2, oh2021unc2cav2channel pages 37-39)

## 6. Synaptic-vesicle pathway and precise physiological role

The clearest mechanistic pathway is:

**axonal depolarization → UNC-2 opening → local Ca²⁺ influx → Ca²⁺-sensor/SNARE activation → fusion of primed synaptic vesicles → neurotransmitter release.**

At the neuromuscular junction, UNC-2/CaV2 colocalizes with the long priming-protein isoform UNC-13L and controls a central vesicle pool docked beside the dense projection. In 2023, 99.7% of CaV2 localizations were reported within 100 nm of an UNC-13 localization. Direct UNC-2-dependent fusion occurs for vesicles within approximately 33 nm of the dense projection, consistent with tight, rapid channel–vesicle coupling. Ryanodine-receptor-mediated release from internal stores can amplify the signal and extend fusion into an intermediate 33–165-nm zone. (mueller2023cav1andcav2 pages 12-15, mueller2023cav1andcav2 pages 15-18, mueller2023cav1andcav2 pages 7-9, mueller2023cav1andcav2 pages 1-2)

This pathway differs from EGL-19/CaV1. EGL-19 is dispersed more broadly in synaptic varicosities, associates with UNC-13S, and drives a more lateral vesicle pool that depends strongly on ryanodine-receptor amplification. The CaV1/CaV2 double mutant shows no stimulation-induced change in docked-vesicle distribution, indicating that together these channel classes account for the examined evoked release pathways. (mueller2023cav1andcav2 pages 1-2, mueller2023cav1andcav2 pages 9-10, mueller2023cav1andcav2 pages 10-12)

UNC-2 supports both cholinergic excitation and GABAergic inhibition. Loss-of-function animals are sluggish and uncoordinated, show impaired backward movement and egg laying, resist aldicarb, and retain relatively normal postsynaptic levamisole sensitivity—evidence that their major defect is reduced presynaptic acetylcholine secretion rather than loss of muscle acetylcholine receptors. Defecation-circuit and GABAergic phenotypes further support a role in inhibitory release. Residual release in null mutants reflects contribution from other calcium channels rather than an absence of UNC-2’s central role. (mathews2009molecularandgenetic pages 209-213, mathews2009molecularandgenetic pages 206-209)

## 7. Recent developments, 2023–2024

### 7.1 Distinct CaV2 and CaV1 release modules — February 2023

Mueller and colleagues combined super-resolution localization, electrophysiology, optogenetic stimulation, and high-pressure-freeze electron microscopy. They resolved an UNC-2/UNC-13L central release module and a spatially separate EGL-19/UNC-13S lateral module. Their estimates included 101 ± 16 UNC-2 channels per synapse, approximately 297-nm channel clusters, and direct fusion from vesicles within 33 nm of the dense projection. This provides the most precise current description of what UNC-2-dependent Ca²⁺ influx actually releases. DOI: https://doi.org/10.7554/eLife.81407. (mueller2023cav1andcav2 pages 15-18, mueller2023cav1andcav2 pages 1-2, mueller2023cav1andcav2 pages 9-10)

### 7.2 Revised auxiliary-subunit trafficking model — May 2023

Oh and colleagues showed that CCB-1/β and UNC-36/α2δ are dispensable for low-level α1-subunit delivery but crucial for terminal stabilization and signalosome abundance. This shifts the prevailing model from obligatory ER coassembly to **partly independent trafficking followed by terminal recruitment and stabilization**. DOI: https://doi.org/10.1523/JNEUROSCI.2264-22.2023. (oh2023activezonetrafficking pages 1-2, oh2023activezonetrafficking pages 10-11)

### 7.3 Target-derived GABAergic feedback — October 2023

At GABAergic neuromuscular junctions, clustered postsynaptic UNC-49/GABA_A receptors feed back across the synapse to increase presynaptic UNC-2. Removing muscle UNC-49 reduced both UNC-2 current and UNC-2 punctum intensity by 32%, without changing resting potential, input resistance, or potassium current. Eliminating vesicular GABA release did not reproduce the effect, and cholinergic UNC-2 was unaffected, demonstrating receptor-cluster-dependent, input-specific retrograde regulation rather than a generic response to reduced transmission. DOI: https://doi.org/10.1016/j.celrep.2023.113161. (zhao2023postsynapticgabaareceptors pages 5-7, zhao2023postsynapticgabaareceptors pages 1-3)

### 7.4 Presynaptic self-tuning — August 2024

Xiong and colleagues found that UNC-2 abundance varies inversely with channel activity and vesicle-exocytosis efficiency. Pore-impaired UNC-2 D726A accumulated at active zones, whereas gain-of-function S240L showed reduced punctum intensity. Their screen identified **WWP-1**, a HECT E3 ubiquitin ligase, as a negative regulator: WWP-1 promotes UNC-2 ubiquitination and constrains presynaptic channel abundance. Postsynaptic acetylcholine-receptor mutations did not alter UNC-2 puncta, arguing that this mechanism is presynaptic and distinct from canonical postsynaptic homeostatic potentiation. DOI: https://doi.org/10.1073/pnas.2404969121. (xiong2024presynapticneuronsselftune pages 2-3, xiong2024presynapticneuronsselftune pages 4-4)

Together, these studies establish that UNC-2 abundance is dynamic: it is governed by intrinsic channel/release activity, ubiquitination, auxiliary-subunit stabilization, active-zone scaffolds, and—in GABAergic synapses—postsynaptic receptor-derived feedback.

## 8. Gain-of-function signaling and excitation–inhibition balance

The *unc-2(zf35)* gain-of-function allele alters a conserved region between repeats III and IV. Analogous mammalian-channel experiments showed activation at more negative voltages and reduced inactivation, predicting increased Ca²⁺ influx. Worms exhibit hyperactivity and seizure-like behavior, whereas loss-of-function mutants are sluggish. Human familial hemiplegic migraine substitutions introduced into UNC-2 similarly cause hyperactivity, making the system useful for testing conserved CaV2 disease mechanisms. (huang2019gainoffunctionmutationsin pages 16-18)

Excess UNC-2 activity raises cholinergic transmission while reducing effective GABAergic signaling. Increased muscle excitation activates TAX-6/calcineurin-dependent remodeling and decreases postsynaptic UNC-49/GABA_A-receptor fluorescence, even when presynaptic GABAergic markers remain normal. This is a downstream consequence of excessive channel activity rather than UNC-2’s primary transport function, but it illustrates how presynaptic Ca²⁺ entry can alter circuit excitation–inhibition balance. (huang2019gainoffunctionmutationsin pages 16-18)

## 9. Current applications and translational relevance

UNC-2 is used experimentally as:

1. **A genetically tractable model of mammalian CaV2/CACNA1A channel biology.** Conserved gain-of-function substitutions can be assessed from channel gating through whole-animal behavior.
2. **An endogenous reporter of active-zone assembly.** CRISPR-tagged UNC-2 provides a quantitative readout for RIM, Liprin-α, RIM-BP, ELKS, kinesin, and auxiliary-subunit function.
3. **A model for excitation–secretion coupling.** Transparent animals permit channel localization, calcium imaging, electrophysiology, electron microscopy, and behavioral measurements in the same genetic system.
4. **A platform for studying synaptic homeostasis and transsynaptic signaling.** The WWP-1 pathway and GABA_A-receptor-dependent recruitment show how channel abundance is adjusted by both presynaptic performance and target-cell organization.

The work has translational relevance to human CaV2 channelopathies and to drug mechanisms acting on α2δ subunits, but UNC-2 itself is a research model rather than a clinically implemented therapeutic target. Species-specific pharmacology must not be inferred solely from CaV2 homology.

## 10. Evidence assessment and remaining uncertainties

**High-confidence conclusions** are the identity of UNC-2 as the worm CaV2 α1 subunit, Ca²⁺ as its transported ion, presynaptic active-zone enrichment, and its role in neurotransmitter release. These are supported by molecular architecture, rescue, endogenous localization, electrophysiology, ultrastructure, and loss-/gain-of-function genetics. (saheki2009presynapticcav2calcium pages 1-3, mathews2009molecularandgenetic pages 132-136, mueller2023cav1andcav2 pages 15-18, oh2023activezonetrafficking pages 1-2)

**Moderate-confidence refinements** concern the relative contribution of CALF-1 and auxiliary subunits at different biogenesis stages. Newer endogenous-tagging results demonstrate residual trafficking without CCB-1 or UNC-36, refining—not simply invalidating—earlier evidence that UNC-36 promotes ER exit and maturation. (saheki2009presynapticcav2calcium pages 1-3, oh2023activezonetrafficking pages 1-2, oh2023activezonetrafficking pages 10-11)

**Remaining uncertainties** include the complete neuron-by-neuron expression map, possible tissue-specific splice or regulatory variants, exact native gating and pharmacology of the fully assembled worm channel, and how universal the GABA_A-receptor feedback mechanism is outside the examined neuromuscular synapses. The designation “P/Q-type” should therefore remain secondary to the more defensible annotation **CaV2-family, high-voltage-activated presynaptic calcium-channel α1 subunit**.

## Final annotation

**UNC-2/G5EFB0 is a neuronal, presynaptic, high-voltage-activated CaV2 α1 subunit. It forms the Ca²⁺-selective pore of a voltage-gated channel complex at active zones. Depolarization-induced Ca²⁺ influx through UNC-2 triggers fusion of UNC-13L-primed vesicles positioned near the dense projection, thereby controlling fast cholinergic and GABAergic neurotransmission. Its delivery and abundance are regulated by CALF-1, CCB-1, UNC-36, UNC-10/RIM, SYD-2/Liprin-α, RIMB-1, ELKS-1, WWP-1-dependent ubiquitination, and synapse-specific retrograde signals.**

References

1. (mathews2009molecularandgenetic pages 202-206): Eleanor Alexandra Mathews. Molecular and genetic analysis of the unc-2 voltage-gated calcium channel in caenorhabditis elegans. ArXiv, Jan 2009. URL: https://doi.org/10.14288/1.0089882, doi:10.14288/1.0089882. This article has 0 citations.

2. (saheki2009presynapticcav2calcium pages 1-3): Yasunori Saheki and Cornelia I Bargmann. Presynaptic cav2 calcium channel traffic requires calf-1 and the α2δ subunit unc-36. Aug 2009. URL: https://doi.org/10.1038/nn.2383, doi:10.1038/nn.2383. This article has 110 citations and is from a highest quality peer-reviewed journal.

3. (mathews2009molecularandgenetic pages 132-136): Eleanor Alexandra Mathews. Molecular and genetic analysis of the unc-2 voltage-gated calcium channel in caenorhabditis elegans. ArXiv, Jan 2009. URL: https://doi.org/10.14288/1.0089882, doi:10.14288/1.0089882. This article has 0 citations.

4. (mathews2009molecularandgenetic pages 196-202): Eleanor Alexandra Mathews. Molecular and genetic analysis of the unc-2 voltage-gated calcium channel in caenorhabditis elegans. ArXiv, Jan 2009. URL: https://doi.org/10.14288/1.0089882, doi:10.14288/1.0089882. This article has 0 citations.

5. (huang2019gainoffunctionmutationsin pages 16-18): Yung-Chi Huang, Jennifer K Pirri, Diego Rayes, Shangbang Gao, Ben Mulcahy, Jeff Grant, Yasunori Saheki, Michael M Francis, Mei Zhen, and Mark J Alkema. Gain-of-function mutations in the unc-2/cav2α channel lead to excitation-dominant synaptic transmission in caenorhabditis elegans. Aug 2019. URL: https://doi.org/10.7554/elife.45905, doi:10.7554/elife.45905. This article has 46 citations and is from a domain leading peer-reviewed journal.

6. (xiong2024presynapticneuronsselftune pages 4-4): Ame Xiong, Janet E. Richmond, and Hongkyun Kim. Presynaptic neurons self-tune by inversely coupling neurotransmitter release with the abundance of cav2 voltage-gated ca2+ channels. Proceedings of the National Academy of Sciences of the United States of America, Aug 2024. URL: https://doi.org/10.1073/pnas.2404969121, doi:10.1073/pnas.2404969121. This article has 5 citations and is from a highest quality peer-reviewed journal.

7. (mueller2023cav1andcav2 pages 9-10): Brian D Mueller, Sean A Merrill, Shigeki Watanabe, Ping Liu, Longgang Niu, Anish Singh, Pablo Maldonado-Catala, Alex Cherry, Matthew S Rich, Malan Silva, Andres Villu Maricq, Zhao-Wen Wang, and Erik M Jorgensen. Cav1 and cav2 calcium channels mediate the release of distinct pools of synaptic vesicles. Feb 2023. URL: https://doi.org/10.7554/elife.81407, doi:10.7554/elife.81407. This article has 42 citations and is from a domain leading peer-reviewed journal.

8. (mueller2023cav1andcav2 pages 10-12): Brian D Mueller, Sean A Merrill, Shigeki Watanabe, Ping Liu, Longgang Niu, Anish Singh, Pablo Maldonado-Catala, Alex Cherry, Matthew S Rich, Malan Silva, Andres Villu Maricq, Zhao-Wen Wang, and Erik M Jorgensen. Cav1 and cav2 calcium channels mediate the release of distinct pools of synaptic vesicles. Feb 2023. URL: https://doi.org/10.7554/elife.81407, doi:10.7554/elife.81407. This article has 42 citations and is from a domain leading peer-reviewed journal.

9. (oh2023activezonetrafficking pages 1-2): Kelly H. Oh, Ame Xiong, Jun-yong Choe, Janet E. Richmond, and Hongkyun Kim. Active zone trafficking of cav2/unc-2 channels is independent of β/ccb-1 and α2δ/unc-36 subunits. May 2023. URL: https://doi.org/10.1523/jneurosci.2264-22.2023, doi:10.1523/jneurosci.2264-22.2023. This article has 8 citations.

10. (oh2023activezonetrafficking pages 10-11): Kelly H. Oh, Ame Xiong, Jun-yong Choe, Janet E. Richmond, and Hongkyun Kim. Active zone trafficking of cav2/unc-2 channels is independent of β/ccb-1 and α2δ/unc-36 subunits. May 2023. URL: https://doi.org/10.1523/jneurosci.2264-22.2023, doi:10.1523/jneurosci.2264-22.2023. This article has 8 citations.

11. (oh2021unc2cav2channel pages 1-5): Kelly H. Oh, Mia Krout, Janet E. Richmond, and Hongkyun Kim. Unc-2 cav2 channel localization at presynaptic active zones depends on unc-10/rim and syd-2/liprin-α in caenorhabditis elegans. The Journal of Neuroscience, 41:4782-4794, Jan 2021. URL: https://doi.org/10.1101/2021.01.27.428454, doi:10.1101/2021.01.27.428454. This article has 38 citations.

12. (oh2021unc2cav2channel pages 8-11): Kelly H. Oh, Mia Krout, Janet E. Richmond, and Hongkyun Kim. Unc-2 cav2 channel localization at presynaptic active zones depends on unc-10/rim and syd-2/liprin-α in caenorhabditis elegans. The Journal of Neuroscience, 41:4782-4794, Jan 2021. URL: https://doi.org/10.1101/2021.01.27.428454, doi:10.1101/2021.01.27.428454. This article has 38 citations.

13. (kushibiki2019rimb1rimbindingproteinand pages 1-2): Yuto Kushibiki, Toshiharu Suzuki, Yishi Jin, and Hidenori Taru. Rimb-1/rim-binding protein and unc-10/rim redundantly regulate presynaptic localization of the voltage-gated calcium channel in caenorhabditis elegans. The Journal of Neuroscience, 39:8617-8631, Sep 2019. URL: https://doi.org/10.1523/jneurosci.0506-19.2019, doi:10.1523/jneurosci.0506-19.2019. This article has 59 citations.

14. (mueller2023cav1andcav2 pages 12-15): Brian D Mueller, Sean A Merrill, Shigeki Watanabe, Ping Liu, Longgang Niu, Anish Singh, Pablo Maldonado-Catala, Alex Cherry, Matthew S Rich, Malan Silva, Andres Villu Maricq, Zhao-Wen Wang, and Erik M Jorgensen. Cav1 and cav2 calcium channels mediate the release of distinct pools of synaptic vesicles. Feb 2023. URL: https://doi.org/10.7554/elife.81407, doi:10.7554/elife.81407. This article has 42 citations and is from a domain leading peer-reviewed journal.

15. (mueller2023cav1andcav2 pages 15-18): Brian D Mueller, Sean A Merrill, Shigeki Watanabe, Ping Liu, Longgang Niu, Anish Singh, Pablo Maldonado-Catala, Alex Cherry, Matthew S Rich, Malan Silva, Andres Villu Maricq, Zhao-Wen Wang, and Erik M Jorgensen. Cav1 and cav2 calcium channels mediate the release of distinct pools of synaptic vesicles. Feb 2023. URL: https://doi.org/10.7554/elife.81407, doi:10.7554/elife.81407. This article has 42 citations and is from a domain leading peer-reviewed journal.

16. (mueller2023cav1andcav2 pages 7-9): Brian D Mueller, Sean A Merrill, Shigeki Watanabe, Ping Liu, Longgang Niu, Anish Singh, Pablo Maldonado-Catala, Alex Cherry, Matthew S Rich, Malan Silva, Andres Villu Maricq, Zhao-Wen Wang, and Erik M Jorgensen. Cav1 and cav2 calcium channels mediate the release of distinct pools of synaptic vesicles. Feb 2023. URL: https://doi.org/10.7554/elife.81407, doi:10.7554/elife.81407. This article has 42 citations and is from a domain leading peer-reviewed journal.

17. (mueller2023cav1andcav2 pages 1-2): Brian D Mueller, Sean A Merrill, Shigeki Watanabe, Ping Liu, Longgang Niu, Anish Singh, Pablo Maldonado-Catala, Alex Cherry, Matthew S Rich, Malan Silva, Andres Villu Maricq, Zhao-Wen Wang, and Erik M Jorgensen. Cav1 and cav2 calcium channels mediate the release of distinct pools of synaptic vesicles. Feb 2023. URL: https://doi.org/10.7554/elife.81407, doi:10.7554/elife.81407. This article has 42 citations and is from a domain leading peer-reviewed journal.

18. (zhao2023postsynapticgabaareceptors pages 5-7): Jian Zhao, Luna Gao, Stephen Nurrish, and Joshua M. Kaplan. Post-synaptic gabaa receptors potentiate transmission by recruiting cav2 channels to their inputs. Oct 2023. URL: https://doi.org/10.1016/j.celrep.2023.113161, doi:10.1016/j.celrep.2023.113161. This article has 12 citations and is from a highest quality peer-reviewed journal.

19. (zhao2023postsynapticgabaareceptors pages 1-3): Jian Zhao, Luna Gao, Stephen Nurrish, and Joshua M. Kaplan. Post-synaptic gabaa receptors potentiate transmission by recruiting cav2 channels to their inputs. Oct 2023. URL: https://doi.org/10.1016/j.celrep.2023.113161, doi:10.1016/j.celrep.2023.113161. This article has 12 citations and is from a highest quality peer-reviewed journal.

20. (xiong2024presynapticneuronsselftune pages 2-3): Ame Xiong, Janet E. Richmond, and Hongkyun Kim. Presynaptic neurons self-tune by inversely coupling neurotransmitter release with the abundance of cav2 voltage-gated ca2+ channels. Proceedings of the National Academy of Sciences of the United States of America, Aug 2024. URL: https://doi.org/10.1073/pnas.2404969121, doi:10.1073/pnas.2404969121. This article has 5 citations and is from a highest quality peer-reviewed journal.

21. (frøkjærjensen2003cameleonimagingof pages 6-11): C Frøkjær-Jensen. Cameleon imaging of calcium transients in cultured mechanosensory neurons in caenorhabditis elegans. Unknown journal, 2003.

22. (oh2021unc2cav2channel pages 37-39): Kelly H. Oh, Mia Krout, Janet E. Richmond, and Hongkyun Kim. Unc-2 cav2 channel localization at presynaptic active zones depends on unc-10/rim and syd-2/liprin-α in caenorhabditis elegans. The Journal of Neuroscience, 41:4782-4794, Jan 2021. URL: https://doi.org/10.1101/2021.01.27.428454, doi:10.1101/2021.01.27.428454. This article has 38 citations.

23. (mathews2009molecularandgenetic pages 209-213): Eleanor Alexandra Mathews. Molecular and genetic analysis of the unc-2 voltage-gated calcium channel in caenorhabditis elegans. ArXiv, Jan 2009. URL: https://doi.org/10.14288/1.0089882, doi:10.14288/1.0089882. This article has 0 citations.

24. (mathews2009molecularandgenetic pages 206-209): Eleanor Alexandra Mathews. Molecular and genetic analysis of the unc-2 voltage-gated calcium channel in caenorhabditis elegans. ArXiv, Jan 2009. URL: https://doi.org/10.14288/1.0089882, doi:10.14288/1.0089882. This article has 0 citations.

## Artifacts

- [Edison artifact artifact-00](unc-2-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. huang2019gainoffunctionmutationsin pages 16-18
2. mathews2009molecularandgenetic pages 202-206
3. mathews2009molecularandgenetic pages 132-136
4. mathews2009molecularandgenetic pages 196-202
5. xiong2024presynapticneuronsselftune pages 4-4
6. oh2023activezonetrafficking pages 1-2
7. oh2023activezonetrafficking pages 10-11
8. zhao2023postsynapticgabaareceptors pages 5-7
9. zhao2023postsynapticgabaareceptors pages 1-3
10. xiong2024presynapticneuronsselftune pages 2-3
11. mathews2009molecularandgenetic pages 209-213
12. mathews2009molecularandgenetic pages 206-209
13. DOI
14. 2019 DOI
15. 2024 DOI
16. 2009 DOI
17. 2023 DOI
18. https://doi.org/10.1523/JNEUROSCI.23-16-06537.2003
19. https://doi.org/10.7554/eLife.45905
20. https://doi.org/10.1073/pnas.2404969121
21. https://doi.org/10.1038/nn.2383
22. https://doi.org/10.7554/eLife.81407
23. https://doi.org/10.1523/JNEUROSCI.2264-22.2023
24. https://doi.org/10.1523/JNEUROSCI.0506-19.2019
25. https://doi.org/10.1016/j.celrep.2023.113161
26. https://doi.org/10.7554/eLife.81407.
27. https://doi.org/10.1523/JNEUROSCI.2264-22.2023.
28. https://doi.org/10.1016/j.celrep.2023.113161.
29. https://doi.org/10.1073/pnas.2404969121.
30. https://doi.org/10.14288/1.0089882,
31. https://doi.org/10.1038/nn.2383,
32. https://doi.org/10.7554/elife.45905,
33. https://doi.org/10.1073/pnas.2404969121,
34. https://doi.org/10.7554/elife.81407,
35. https://doi.org/10.1523/jneurosci.2264-22.2023,
36. https://doi.org/10.1101/2021.01.27.428454,
37. https://doi.org/10.1523/jneurosci.0506-19.2019,
38. https://doi.org/10.1016/j.celrep.2023.113161,