---
provider: falcon
model: Edison Scientific Literature
cached: true
start_time: '2026-09-30T05:30:56.804512'
end_time: '2026-09-30T05:30:56.813527'
duration_seconds: 0.01
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: DROME
  gene_id: Ser
  gene_symbol: Ser
  uniprot_accession: P18168
  protein_description: 'RecName: Full=Protein serrate {ECO:0000303|PubMed:1840519,
    ECO:0000312|FlyBase:FBgn0004197}; AltName: Full=Delta-like protein {ECO:0000255|RuleBase:RU280815};
    AltName: Full=Protein beaded {ECO:0000303|PubMed:1840519, ECO:0000312|FlyBase:FBgn0004197};
    Flags: Precursor;'
  gene_info: Name=Ser {ECO:0000303|PubMed:1840519, ECO:0000312|FlyBase:FBgn0004197};
    Synonyms=Bd {ECO:0000303|PubMed:1840519, ECO:0000312|FlyBase:FBgn0004197}, Rpw
    {ECO:0000312|FlyBase:FBgn0004197}; ORFNames=CG6127 {ECO:0000312|FlyBase:FBgn0004197};
  organism_full: Drosophila melanogaster (Fruit fly).
  protein_family: Not specified in UniProt
  protein_domains: DSL. (IPR001774); EGF. (IPR000742); EGF-like_Ca-bd_dom. (IPR001881);
    EGF-like_CS. (IPR013032); EGF-type_Asp/Asn_hydroxyl_site. (IPR000152)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 43
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: Ser-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: Ser-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P18168
- **Protein Description:** RecName: Full=Protein serrate {ECO:0000303|PubMed:1840519, ECO:0000312|FlyBase:FBgn0004197}; AltName: Full=Delta-like protein {ECO:0000255|RuleBase:RU280815}; AltName: Full=Protein beaded {ECO:0000303|PubMed:1840519, ECO:0000312|FlyBase:FBgn0004197}; Flags: Precursor;
- **Gene Information:** Name=Ser {ECO:0000303|PubMed:1840519, ECO:0000312|FlyBase:FBgn0004197}; Synonyms=Bd {ECO:0000303|PubMed:1840519, ECO:0000312|FlyBase:FBgn0004197}, Rpw {ECO:0000312|FlyBase:FBgn0004197}; ORFNames=CG6127 {ECO:0000312|FlyBase:FBgn0004197};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** DSL. (IPR001774); EGF. (IPR000742); EGF-like_Ca-bd_dom. (IPR001881); EGF-like_CS. (IPR013032); EGF-type_Asp/Asn_hydroxyl_site. (IPR000152)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Ser" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Ser' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Ser** (gene ID: Ser, UniProt: P18168) in DROME.

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
- **UniProt Accession:** P18168
- **Protein Description:** RecName: Full=Protein serrate {ECO:0000303|PubMed:1840519, ECO:0000312|FlyBase:FBgn0004197}; AltName: Full=Delta-like protein {ECO:0000255|RuleBase:RU280815}; AltName: Full=Protein beaded {ECO:0000303|PubMed:1840519, ECO:0000312|FlyBase:FBgn0004197}; Flags: Precursor;
- **Gene Information:** Name=Ser {ECO:0000303|PubMed:1840519, ECO:0000312|FlyBase:FBgn0004197}; Synonyms=Bd {ECO:0000303|PubMed:1840519, ECO:0000312|FlyBase:FBgn0004197}, Rpw {ECO:0000312|FlyBase:FBgn0004197}; ORFNames=CG6127 {ECO:0000312|FlyBase:FBgn0004197};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** DSL. (IPR001774); EGF. (IPR000742); EGF-like_Ca-bd_dom. (IPR001881); EGF-like_CS. (IPR013032); EGF-type_Asp/Asn_hydroxyl_site. (IPR000152)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Ser" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Ser' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Ser** (gene ID: Ser, UniProt: P18168) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Comprehensive Research Report: Serrate (Ser) Gene in *Drosophila melanogaster*

## Gene Identity and Overview

The gene **Serrate** (Ser; also known as **beaded**, Bd; UniProt accession P18168; FlyBase ID FBgn0004197) encodes a canonical transmembrane ligand of the Notch signaling pathway in *Drosophila melanogaster* (lv2024evolutionandfunction pages 2-4, seib2025theintracellulardomains pages 1-2, sachan2023notchsignallingmultifaceted pages 2-2). Serrate is the founding member of the Serrate/Jagged class of Delta-Serrate-LAG-2 (DSL) family ligands, which are distinguished from the Delta class by the presence of a cysteine-rich domain (feng2024thestructuraland pages 40-44, handford2018structuralinsightsinto pages 4-6). This highly conserved protein plays essential roles in cell-fate determination, tissue patterning, and organogenesis throughout *Drosophila* development (lv2024evolutionandfunction pages 2-4, chen2023notchsignalingin pages 18-20).

## Primary Molecular Function and Mechanism

### Core Function as a Notch Ligand

Serrate functions primarily as a membrane-associated ligand that activates the Notch receptor on adjacent cells through a process termed **trans-activation** (lv2024evolutionandfunction pages 2-4, seib2025theintracellulardomains pages 1-2, feng2024thestructuraland pages 21-25). The molecular mechanism proceeds through several essential steps. First, Serrate on a signal-sending cell binds to the extracellular domain of Notch on a neighboring signal-receiving cell through interactions mediated by its DSL domain and surrounding regions (lv2024evolutionandfunction pages 2-4, handford2018structuralinsightsinto pages 6-9). This binding initiates a mechanotransduction cascade that is fundamental to Notch pathway activation (lv2024evolutionandfunction pages 2-4, seib2025theintracellulardomains pages 1-2).

### Mechanotransduction and Notch Activation

Following ligand-receptor engagement, Serrate undergoes endocytosis in the signal-sending cell (seib2025theintracellulardomains pages 1-2). This endocytic event is not merely for ligand turnover; rather, it generates a mechanical pulling force on the bound Notch receptor that induces a conformational change in Notch (lv2024evolutionandfunction pages 2-4, feng2024thestructuraland pages 21-25). This force-dependent conformational change exposes the normally masked S2 cleavage site within Notch's negative regulatory region (lv2024evolutionandfunction pages 2-4, feng2024thestructuraland pages 21-25). ADAM-family metalloproteases (specifically Kuzbanian/ADAM10 in *Drosophila*) then cleave Notch at the S2 site, generating the Notch extracellular truncation (NEXT) fragment (lv2024evolutionandfunction pages 2-4, sachan2023notchsignallingmultifaceted pages 2-2). Subsequently, the γ-secretase complex performs a second cleavage at the S3 site, releasing the Notch intracellular domain (NICD) from the membrane (lv2024evolutionandfunction pages 2-4, seib2025theintracellulardomains pages 1-2, feng2024thestructuraland pages 21-25).

The liberated NICD translocates to the nucleus, where it forms a transcriptional activation complex with the DNA-binding protein Suppressor of Hairless [Su(H), the *Drosophila* ortholog of mammalian RBPJ/CSL] and the coactivator Mastermind (lv2024evolutionandfunction pages 2-4, seib2025theintracellulardomains pages 1-2). This complex displaces transcriptional repressors and recruits coactivators to drive expression of Notch target genes, including members of the Enhancer of split [E(spl)] complex and other context-dependent targets (lv2024evolutionandfunction pages 2-4, feng2024thestructuraland pages 21-25).

### Cis-Inhibition: A Regulatory Counterbalance

In addition to trans-activation, Serrate can also interact with Notch receptors expressed in the same cell, a phenomenon termed **cis-inhibition** (seib2025theintracellulardomains pages 1-2, vazquezulloa2022reversibleandbidirectional pages 5-7). When Serrate and Notch are co-expressed on the same cell surface, their cis-interaction sequesters Notch in an inactive complex, preventing it from being activated by ligands on neighboring cells (seib2025theintracellulardomains pages 1-2, feng2024thestructuraland pages 25-28). These cis-complexes can be internalized and degraded, providing mutual inactivation of both receptor and ligand (feng2024thestructuraland pages 25-28, vazquezulloa2022reversibleandbidirectional pages 5-7). Cis-inhibition serves as a critical regulatory mechanism that helps establish directional signaling, sharpens boundaries between cell populations, and contributes to cell-fate decisions by biasing cells toward sender versus receiver states (seib2025theintracellulardomains pages 1-2, sprinzak2021biophysicsofnotch pages 6-7).

## Protein Structure and Domain Organization

Serrate is a type I single-pass transmembrane protein with a large extracellular region, a single transmembrane domain, and a cytoplasmic tail (deliconstantinos2021translationalcontrolof pages 1-4, seib2025theintracellulardomains pages 1-2). Detailed structural and biochemical analyses have revealed a modular domain architecture that underpins its function.

| Domain Name | Location | Structural Features | Functional Role |
|---|---|---|---|
| N-terminal C2 domain (formerly MNNL) | Extracellular N-terminus, preceding the DSL domain | Approximately 100-residue C2 fold with exposed β1–2 and β5–6 loops; conserved among canonical Notch ligands. Serrate C2-containing constructs bind membrane-mimetic liposomes, although lipid specificity and loop dependence differ from Delta. | Supports phospholipid or membrane association and helps orient the ligand for productive receptor engagement; contributes to robust Notch signaling rather than constituting the principal receptor-binding site. (martins2021deltac2domain pages 1-4, martins2021deltac2domain pages 26-31, martins2021deltac2domain pages 23-26) |
| DSL domain | Extracellular, immediately C-terminal to the C2 domain | Conserved Delta/Serrate/LAG-2 module with a compact, disulfide-stabilized fold and exposed receptor-contact surface. Mutation of a conserved Serrate phenylalanine corresponding to F257 abolishes Notch binding. | Principal determinant of Notch recognition; supports both **trans** binding to Notch on an adjacent cell and **cis** binding to Notch in the same cell. (handford2018structuralinsightsinto pages 6-9, handford2018structuralinsightsinto pages 4-6) |
| EGF-like repeats (14 total) | Extracellular region following the DSL domain | Fourteen tandem EGF-like repeats, including predicted calcium-binding and non-calcium-binding forms; together they form an extended extracellular scaffold. The first repeats can enhance binding by supplementing or stabilizing the DSL-mediated interface. | Project and position the N-terminal receptor-binding module away from the plasma membrane, support productive Notch interaction, and may provide supplementary receptor contacts. (handford2018structuralinsightsinto pages 6-9, handford2018structuralinsightsinto pages 4-6, deliconstantinos2021translationalcontrolof pages 1-4) |
| Serrate/Jagged-family cysteine-rich domain | Membrane-proximal extracellular region, downstream of the EGF-like repeats | Cysteine-rich module characteristic of Serrate/Jagged ligands and absent from canonical Delta-like ligands. | Distinguishes the Serrate/Jagged structural class; its precise independent function in *Drosophila* Serrate is less firmly established than those of the C2 and DSL domains, but it likely contributes to extracellular architecture or ligand-specific regulation. (feng2024thestructuraland pages 40-44, handford2018structuralinsightsinto pages 4-6) |
| Transmembrane domain | Single membrane-spanning segment between extracellular and cytoplasmic regions | Hydrophobic segment defining Serrate as a single-pass, type-I transmembrane protein, with a large extracellular N-terminus and cytoplasmic C-terminal tail. | Anchors Serrate at the sender-cell plasma membrane, enabling contact-dependent binding to Notch on neighboring cells and coupling extracellular receptor engagement to intracellular endocytic machinery. (deliconstantinos2021translationalcontrolof pages 1-4, seib2025theintracellulardomains pages 1-2) |
| Intracellular domain (cytoplasmic tail) | Cytoplasmic C-terminus, following the transmembrane segment | Contains conserved motifs and ten lysines that can support ubiquitylation; Mindbomb1-dependent ubiquitylation requires at least five conserved lysines for Serrate activation, while six or more support its full trafficking behavior. | Recruits ubiquitylation and endocytic machinery. Its regulated internalization generates the pulling force needed for Notch trans-activation; it also controls Serrate turnover, localization, and the balance between productive trans-signaling and cis-inhibition. (seib2025theintracellulardomains pages 1-2) |


*Table: Structural and functional map of the major domains in Drosophila Serrate, from its extracellular receptor-binding modules to its signaling-regulated cytoplasmic tail.*

### Detailed Domain Functions

**C2 Domain:** The N-terminal C2 domain (formerly called the MNNL module) is an approximately 100-amino-acid phospholipid-binding module conserved among canonical Notch ligands (feng2024thestructuraland pages 44-49, martins2021deltac2domain pages 1-4). Structural studies show that Serrate's C2 domain adopts the characteristic C2 fold with exposed apical loops, particularly the β1-2 and β5-6 loops, which vary in length and sequence among different ligands (martins2021deltac2domain pages 1-4, martins2021deltac2domain pages 26-31). Biochemical experiments demonstrate that purified Serrate constructs containing the C2 domain can bind to membrane-mimetic liposomes, supporting a role in phospholipid recognition (martins2021deltac2domain pages 4-8, martins2021deltac2domain pages 23-26). The C2 domain contributes to robust Notch signaling by helping orient the ligand at the cell membrane for optimal receptor engagement, rather than serving as the primary receptor-binding interface (martins2021deltac2domain pages 4-8, martins2021deltac2domain pages 1-4).

**DSL Domain:** The DSL (Delta-Serrate-LAG-2) domain is a compact, disulfide-stabilized module that constitutes the principal determinant of Notch receptor recognition (feng2024thestructuraland pages 44-49, handford2018structuralinsightsinto pages 6-9, handford2018structuralinsightsinto pages 4-6). Mutagenesis studies have demonstrated that conserved surface-exposed residues within the DSL domain are essential for Notch binding; for example, mutation of a conserved phenylalanine (corresponding to F257 in Serrate or F207 in human Jagged-1) to alanine abolishes Notch binding (handford2018structuralinsightsinto pages 6-9). The DSL domain mediates both trans-activation of Notch in adjacent cells and cis-inhibition of Notch in the same cell, making it central to bidirectional signaling regulation (handford2018structuralinsightsinto pages 6-9, handford2018structuralinsightsinto pages 4-6).

**EGF-like Repeats:** Serrate contains 14 tandem epidermal growth factor (EGF)-like repeats in its extracellular region (deliconstantinos2021translationalcontrolof pages 1-4). These repeats include both calcium-binding and non-calcium-binding forms and together form an extended, near-linear scaffold that projects the N-terminal receptor-binding modules away from the plasma membrane (handford2018structuralinsightsinto pages 6-9, deliconstantinos2021translationalcontrolof pages 1-4). The first EGF repeats can enhance Notch binding by supplementing or stabilizing the DSL-mediated interface, and the extended architecture may help position the ligand for productive trans-interactions (handford2018structuralinsightsinto pages 6-9, handford2018structuralinsightsinto pages 4-6).

**Cysteine-Rich Domain:** Downstream of the EGF-like repeats lies a cysteine-rich domain (CRD) characteristic of the Serrate/Jagged family and absent from Delta-like ligands (feng2024thestructuraland pages 40-44, handford2018structuralinsightsinto pages 4-6). This domain distinguishes Serrate/Jagged ligands structurally and may contribute to ligand-specific regulation or extracellular architecture, although its precise independent function is less firmly established than those of the C2 and DSL domains (feng2024thestructuraland pages 40-44).

**Intracellular Domain:** The cytoplasmic tail of Serrate contains conserved motifs and ten lysine residues that can be ubiquitylated (seib2025theintracellulardomains pages 1-2). This domain recruits E3 ubiquitin ligases and endocytic machinery, and its regulated internalization is essential for generating the mechanical force needed for Notch trans-activation (seib2025theintracellulardomains pages 1-2, feng2024thestructuraland pages 21-25). At least five conserved lysines are required for Mindbomb1 (Mib1)-mediated activation of Serrate, while six or more lysines support its full trafficking behavior, including bulk endocytosis (seib2025theintracellulardomains pages 1-2).

## Subcellular Localization

Serrate is primarily localized at the plasma membrane/cell surface, where its extracellular domain is available for interaction with Notch receptors on adjacent cells (deliconstantinos2021translationalcontrolof pages 1-4, seib2025theintracellulardomains pages 1-2, sachan2023notchsignallingmultifaceted pages 2-2). As a single-pass transmembrane protein, Serrate contains a signal peptide that directs it into the secretory pathway (deliconstantinos2021translationalcontrolof pages 5-7), and the mature protein is anchored in the membrane with its large extracellular region projecting outward and its cytoplasmic tail extending into the cell (deliconstantinos2021translationalcontrolof pages 1-4, seib2025theintracellulardomains pages 1-2).

Following Notch binding, Serrate undergoes endocytosis and can be found in endocytic compartments (seib2025theintracellulardomains pages 1-2). Importantly, Mib1-dependent ubiquitylation channels a small fraction of Serrate into a rare, Epsin-dependent endocytic pathway that is specifically relevant for signaling, while the bulk of endocytosed Serrate enters pathways that primarily support trafficking or turnover (seib2025theintracellulardomains pages 1-2). When Mib1 is absent or inactive, Serrate strongly accumulates at the plasma membrane, demonstrating that its surface presentation is dynamically regulated by ubiquitylation-dependent internalization (seib2025theintracellulardomains pages 1-2).

## Regulation by Ubiquitylation and E3 Ligases

A distinguishing feature of Serrate biology is its strong dependence on the E3 ubiquitin ligase Mindbomb1 (Mib1) for signaling activity (seib2025theintracellulardomains pages 1-2). Mib1 recognizes motifs in the Serrate intracellular domain and ubiquitylates lysine residues, initiating endocytosis (seib2025theintracellulardomains pages 1-2). Unlike Delta, which retains substantial Mib1-independent and ubiquitylation-independent signaling activity, Serrate signaling is reported to depend completely on Mib1-mediated ubiquitylation (seib2025theintracellulardomains pages 1-2). Experiments with a Serrate variant in which all intracellular lysines are replaced by arginine (SerK2R) demonstrate that this mutant has severely impaired or abolished activity, confirming the essential role of lysine ubiquitylation (seib2025theintracellulardomains pages 1-2).

The related E3 ligase Neuralized (Neur) can also recognize Serrate through conserved NxxN motifs in its intracellular domain (seib2021theroleof pages 8-9), but current evidence emphasizes Mib1 as the principal activator of Serrate in most non-neural developmental contexts examined (seib2025theintracellulardomains pages 1-2, seib2021theroleof pages 8-9). In contrast, Neur plays a more prominent role in activating Delta during neural precursor selection and can support Delta signaling even without ubiquitylation, possibly acting as an endocytic co-adaptor in addition to its E3 ligase function (seib2025theintracellulardomains pages 1-2, troost2023themeaningof pages 1-2).

## Comparison with Delta

Serrate and Delta are the two canonical Notch ligands in *Drosophila*, and while they share the core DSL ligand architecture and both mediate trans-activation and cis-inhibition, they differ significantly in their regulation, mechanistic requirements, and developmental deployment (seib2025theintracellulardomains pages 1-2, troost2023themeaningof pages 1-2).

| Feature/property | Serrate (Ser) | Delta (Dl) |
|---|---|---|
| Core identity | Canonical Serrate/Jagged-class DSL ligand and type-I single-pass transmembrane protein. Its extracellular region includes C2, DSL, EGF-like, and Serrate/Jagged-specific cysteine-rich modules. (feng2024thestructuraland pages 40-44, deliconstantinos2021translationalcontrolof pages 1-4) | Canonical Delta-class DSL ligand and type-I transmembrane protein; it shares the C2–DSL–EGF core architecture but lacks the Serrate/Jagged-specific cysteine-rich region. (martins2021deltac2domain pages 1-4, feng2024thestructuraland pages 40-44) |
| Primary signaling action | Activates Notch **in trans** on an adjacent cell and inhibits Notch **in cis** when ligand and receptor are coexpressed in the same cell. (seib2025theintracellulardomains pages 1-2, vazquezulloa2022reversibleandbidirectional pages 5-7) | Also mediates trans-activation and cis-inhibition; Delta cis-inhibition helps suppress basal Notch activity during cell-fate selection. (troost2023themeaningof pages 1-2, sprinzak2021biophysicsofnotch pages 6-7) |
| Dependence on Mindbomb1 (Mib1) | Strong: Serrate signaling is reported to depend completely on Mib1-mediated ubiquitylation; its endocytosis is almost abolished without Mib1. (seib2025theintracellulardomains pages 1-2) | Partial and context-dependent: Mib1-dependent processes require ubiquitylation for full Delta activity, but Delta retains Mib1- and ubiquitylation-independent signaling modes. (seib2025theintracellulardomains pages 1-2, troost2023themeaningof pages 1-2) |
| Relationship to Neuralized (Neur) | Neur can recognize Serrate through intracellular motifs, but available evidence emphasizes Mib1 as the principal activator of Serrate in the examined non-neural contexts. (seib2025theintracellulardomains pages 1-2, seib2021theroleof pages 8-9) | Neur has a prominent role in neural precursor contexts and can activate Delta without ligand ubiquitylation, probably also acting as an endocytic co-adaptor. (seib2025theintracellulardomains pages 1-2, troost2023themeaningof pages 1-2) |
| Intracellular lysines and ubiquitylation | At least five conserved cytoplasmic lysines are required for Mib1-mediated activation; six or more of ten lysines support full trafficking behavior, including bulk endocytosis. (seib2025theintracellulardomains pages 1-2) | Cytoplasmic lysines contribute to full activity and regulation of cis-inhibition, but lysine-free Delta retains weak biologically meaningful signaling through ubiquitylation-independent modes. (seib2025theintracellulardomains pages 1-2, troost2023themeaningof pages 1-2) |
| Signaling-relevant endocytosis | Mib1-dependent ubiquitylation channels a small Serrate fraction into a rare, Epsin-dependent signaling route that generates force; bulk internalization mainly supports trafficking or turnover. (seib2025theintracellulardomains pages 1-2) | Epsin-dependent endocytosis is required across the identified ubiquitylation-dependent and -independent Delta signaling modes and generates the force needed to activate Notch. (troost2023themeaningof pages 1-2) |
| Fringe effect on Notch responsiveness | Fringe glycosylation of Notch generally suppresses productive Serrate responsiveness in *Drosophila*, restricting Serrate activation to adjacent Fringe-negative cells. (chen2023notchsignalingin pages 5-6, sprinzak2021biophysicsofnotch pages 3-4) | Fringe generally enhances Notch responsiveness and binding to Delta, favoring Delta signaling into Fringe-positive cells. (chen2023notchsignalingin pages 5-6, sprinzak2021biophysicsofnotch pages 3-4) |
| Wing dorsoventral boundary | Dorsally expressed Serrate activates non-Fringe-modified Notch in neighboring ventral boundary cells. (chen2023notchsignalingin pages 5-6, sprinzak2021biophysicsofnotch pages 3-4) | Ventrally expressed Delta activates Fringe-modified Notch in neighboring dorsal boundary cells. (chen2023notchsignalingin pages 5-6, sprinzak2021biophysicsofnotch pages 3-4) |
| Other developmental emphasis | Especially prominent in wing-boundary and wing-vein patterning; it also cooperates with Delta in leg segmentation and is required for aspects of embryonic ectodermal and nervous-system development. (martins2021deltac2domain pages 4-8, lv2024evolutionandfunction pages 25-26, chen2023notchsignalingin pages 21-22) | Prominent in neural precursor selection, lateral inhibition, eye and bristle patterning, while also contributing to wing and appendage development. (seib2025theintracellulardomains pages 1-2, seib2025theintracellulardomains pages 22-22, troost2023themeaningof pages 1-2) |
| Overall mechanistic distinction | A comparatively strict Mib1–ubiquitin–endocytosis coupling makes Serrate activity highly dependent on its cytoplasmic tail and regulated trafficking. (seib2025theintracellulardomains pages 1-2) | Delta uses more mechanistically diverse routes: Mib1-dependent signaling, Neur-supported signaling, and residual ubiquitylation-independent—but Epsin-dependent—activity. (seib2025theintracellulardomains pages 1-2, troost2023themeaningof pages 1-2) |


*Table: Comparison of the two canonical Drosophila Notch ligands, emphasizing their distinct E3-ligase and ubiquitylation requirements, Fringe responses, endocytic mechanisms, and developmental deployment.*

The most striking molecular difference is the degree of dependence on ubiquitylation: Serrate is strictly Mib1- and ubiquitylation-dependent, whereas Delta uses more mechanistically diverse routes, including Mib1-dependent signaling, Neuralized-supported signaling, and residual ubiquitylation-independent (but Epsin-dependent) activity (seib2025theintracellulardomains pages 1-2, troost2023themeaningof pages 1-2). This difference likely reflects distinct intracellular regulatory mechanisms and may contribute to their complementary developmental functions (seib2025theintracellulardomains pages 1-2, seib2025theintracellulardomains pages 22-22).

## Regulation by Fringe Glycosyltransferase

A key regulator of Serrate function is the glycosyltransferase Fringe (Fng), which modifies O-fucose residues on Notch EGF-like repeats by adding β-1,3-N-acetylglucosamine (GlcNAc) (sprinzak2021biophysicsofnotch pages 3-4, feng2024thestructuraland pages 56-60, handford2018structuralinsightsinto pages 4-6). This modification has opposite effects on the two ligand classes: Fringe glycosylation enhances Notch responsiveness to Delta while suppressing Notch responsiveness to Serrate (chen2023notchsignalingin pages 5-6, sprinzak2021biophysicsofnotch pages 3-4, sprinzak2021biophysicsofnotch pages 4-6).

Biochemical studies using mammalian Notch1 and Jagged-1 (the Serrate homolog) have revealed complex effects. Some reports indicate that Fringe-mediated addition of GlcNAc to O-fucose at Notch residue T466 (in EGF12) increases the intrinsic binding affinity for Jagged-1 by approximately 9-fold relative to the monosaccharide-modified form (handford2018structuralinsightsinto pages 4-6, handford2018structuralinsightsinto pages 1-4). However, despite increased binding, Fringe reduces productive Jagged-1-mediated Notch activation (kuintzle2025diversityinnotch pages 10-11, sprinzak2021biophysicsofnotch pages 4-6). This suggests that Fringe uncouples ligand binding from receptor activation, potentially allowing Serrate/Jagged to occupy Notch and competitively inhibit activation by other ligands (kuintzle2025diversityinnotch pages 10-11). 

In *Drosophila* developmental contexts, Fringe glycosylation generally restricts Serrate's ability to activate Notch, confining Serrate-mediated activation to cells lacking Fringe or to interfaces between Fringe-positive and Fringe-negative compartments (chen2023notchsignalingin pages 5-6, sprinzak2021biophysicsofnotch pages 3-4, feng2024thestructuraland pages 56-60). Fringe also differentially affects cis-inhibition: glycosylated Notch shows reduced cis-interaction with Serrate/Jagged, allowing cells to simultaneously receive Delta signals (in trans) while sending Jagged/Serrate signals, thereby expanding the possible signaling states (sprinzak2021biophysicsofnotch pages 6-7, sprinzak2021biophysicsofnotch pages 7-9).

## Biological Processes and Developmental Roles

### Wing Development and the Dorsal-Ventral Boundary

The most extensively characterized role of Serrate is in patterning the *Drosophila* wing imaginal disc, particularly at the dorsal-ventral (D/V) compartment boundary (chen2023notchsignalingin pages 18-20, chen2023notchsignalingin pages 5-6, chen2023notchsignalingin pages 17-18, seib2025theintracellulardomains pages 22-22). The dorsal compartment is specified by expression of the LIM-homeodomain transcription factor Apterous (Ap), which activates both Serrate and Fringe (chen2023notchsignalingin pages 5-6). Serrate expressed in dorsal cells activates Notch in adjacent ventral boundary cells that lack Fringe modification (chen2023notchsignalingin pages 5-6, sprinzak2021biophysicsofnotch pages 3-4). Conversely, Delta expressed in ventral cells activates Fringe-modified Notch in neighboring dorsal boundary cells (chen2023notchsignalingin pages 5-6, sprinzak2021biophysicsofnotch pages 3-4). This complementary ligand-receptor signaling establishes and maintains the D/V boundary.

Notch activation at the boundary induces expression of key downstream targets including *wingless* (wg), *cut*, and *vestigial* (vg) (chen2023notchsignalingin pages 18-20, chen2023notchsignalingin pages 5-6). Wingless acts as a morphogen and helps establish a signaling organizer that coordinates wing growth and patterning (chen2023notchsignalingin pages 18-20, chen2023notchsignalingin pages 17-18). Vestigial is a wing selector gene required for wing formation, and its expression is cooperatively induced by Serrate-mediated Notch signaling and Wingless (chen2023notchsignalingin pages 18-20). Cut is expressed at high levels along the D/V boundary and contributes to wing margin identity (chen2023notchsignalingin pages 18-20, martins2021deltac2domain pages 4-8). Disruption of Serrate function impairs D/V compartment organization, reduces wing margin formation, and can cause wing notching or vein patterning defects (chen2023notchsignalingin pages 18-20, martins2021deltac2domain pages 4-8).

### Leg Development and Appendage Segmentation

Beyond the wing, Serrate cooperates with Delta to establish leg segments and contribute to proximodistal patterning of the leg imaginal disc (chen2023notchsignalingin pages 21-22, seib2025theintracellulardomains pages 22-22). Serrate and Delta expression in the tarsus is regulated by developmental transcription factors including dAP-2 and defective proventriculus (chen2023notchsignalingin pages 21-22). Notch signaling downstream of these ligands regulates tarsal joint formation and morphogenesis, indicating that Serrate participates in the segmentation and joint specification that are evolutionarily conserved features of arthropod appendage development (chen2023notchsignalingin pages 21-22, seib2025theintracellulardomains pages 22-22).

### Embryonic Development and Nervous System

Serrate is expressed in multiple embryonic tissues, with particularly regulated expression in the ventral nerve cord and brain hemispheres (supra-esophageal ganglia) (lv2024evolutionandfunction pages 25-26). Embryonic lethal Serrate mutations produce both epidermal and neuronal defects, including loss of substantial dorsal or ventral cuticle and disrupted longitudinal connections between segmental ganglia (lv2024evolutionandfunction pages 25-26). These phenotypes demonstrate that Serrate-mediated Notch signaling contributes to coordinated development of neural and ectodermal cell lineages during embryogenesis (lv2024evolutionandfunction pages 25-26, lv2024evolutionandfunction pages 35-36).

Serrate is also implicated in eye and bristle development, processes involving Notch-mediated lateral inhibition and cell-fate specification (seib2025theintracellulardomains pages 22-22). However, the precise Serrate-specific contributions to neurogenesis and sensory organ development are less fully characterized than its roles in wing and appendage patterning, and in many neural contexts Delta appears to be the predominant ligand (seib2025theintracellulardomains pages 1-2, seib2025theintracellulardomains pages 22-22, troost2023themeaningof pages 1-2).

### Integration with Other Signaling Pathways

Serrate function is integrated with multiple other developmental signaling pathways. The interaction with Wingless (Wnt) signaling at the wing D/V boundary exemplifies pathway crosstalk: Serrate-mediated Notch activation induces Wingless expression, which in turn cooperates with Notch to activate downstream targets like Vestigial (chen2023notchsignalingin pages 18-20, chen2023notchsignalingin pages 17-18). Recent work has also identified interactions between Serrate-Notch signaling and EGFR signaling in the regulation of blood progenitor cell fate in the *Drosophila* lymph gland, where CSN-mediated regulation of Serrate activation controls the balance between plasmatocytes and crystal cells (rai2026cop9signalosomeregulates pages 7-9). These examples illustrate that Serrate does not function in isolation but rather as part of integrated signaling networks that coordinate cell fate, proliferation, and patterning.

## Recent Developments (2023-2025)

Recent publications have significantly advanced our understanding of Serrate biology:

1. **Intracellular Domain Functional Differences (2025):** Seib et al. demonstrated that the intracellular domains of Serrate and Delta provide different activities, with Serrate showing complete dependence on Mib1-mediated ubiquitylation while Delta retains ubiquitylation-independent signaling modes (seib2025theintracellulardomains pages 1-2). This study established that at least five conserved lysines in Serrate's cytoplasmic tail are required for Mib1-mediated activation (seib2025theintracellulardomains pages 1-2).

2. **Ligand-Receptor Interaction Diversity (2025):** Kuintzle et al. systematically characterized trans-activation, cis-inhibition, and cis-activation across different ligand-receptor pairs, revealing that each ligand exhibits a unique profile of interactions and Fringe-dependence (kuintzle2025diversityinnotch pages 10-11). This work demonstrated that Fringe can increase Jagged/Serrate binding to Notch while simultaneously weakening activation, uncoupling binding from productive signaling (kuintzle2025diversityinnotch pages 10-11).

3. **Comprehensive Reviews (2023-2024):** Recent reviews by Sachan et al. (2024), Chen et al. (2023), and Lv et al. (2024) have synthesized current understanding of Notch signaling mechanisms and highlighted Serrate's multifaceted roles in development and disease (lv2024evolutionandfunction pages 2-4, sachan2023notchsignallingmultifaceted pages 2-2, chen2023notchsignalingin pages 18-20). These authoritative reviews emphasize the conserved nature of Serrate/Jagged-Notch signaling across metazoans and its relevance to human pathologies (lv2024evolutionandfunction pages 2-4, sachan2023notchsignallingmultifaceted pages 2-2).

4. **Mechanistic Insights into Ligand Activation (2023):** Troost et al. clarified the meaning of Delta ubiquitylation and identified three modes of ligand signaling that are either ubiquitylation-dependent or -independent (troost2023themeaningof pages 1-2). While focused on Delta, this work provided crucial context for understanding the more stringent ubiquitylation requirement of Serrate (troost2023themeaningof pages 1-2).

## Conclusion

Serrate is a canonical transmembrane Notch ligand whose primary molecular function is to activate Notch receptors on adjacent cells through a mechanotransduction mechanism involving ligand-receptor binding, endocytosis-mediated mechanical force, and sequential proteolytic cleavage. Structurally, Serrate comprises an N-terminal C2 domain for membrane association, a DSL domain for receptor recognition, 14 EGF-like repeats, a Serrate/Jagged-specific cysteine-rich domain, a transmembrane segment, and a cytoplasmic tail that recruits ubiquitylation and endocytic machinery. 

Serrate is localized at the cell surface and functions at sites of cell-cell contact, where it mediates both trans-activation of Notch in neighboring cells and cis-inhibition of Notch in the same cell. Its activity is stringently regulated by Mindbomb1-mediated ubiquitylation and is modulated by Fringe glycosylation of the Notch receptor. Developmentally, Serrate plays essential roles in wing imaginal disc patterning (particularly at the dorsal-ventral boundary), leg segmentation, and embryonic ectodermal and neural development. It cooperates with Delta and integrates with other signaling pathways including Wingless and EGFR to coordinate cell-fate decisions and tissue patterning.

Recent research has illuminated the molecular distinctions between Serrate and Delta, particularly their differential dependence on E3 ubiquitin ligases and ubiquitylation, and has revealed the complex ways in which Fringe glycosylation can uncouple ligand binding from receptor activation. These advances provide a foundation for understanding how two ligands acting through the same receptor can produce diverse and context-dependent developmental outcomes.

References

1. (lv2024evolutionandfunction pages 2-4): Yan Lv, Xuan Pang, Zhonghong Cao, Changping Song, Baohua Liu, Weiwei Wu, and Qiuxiang Pang. Evolution and function of the notch signaling pathway: an invertebrate perspective. International Journal of Molecular Sciences, 25:3322, Mar 2024. URL: https://doi.org/10.3390/ijms25063322, doi:10.3390/ijms25063322. This article has 36 citations.

2. (seib2025theintracellulardomains pages 1-2): Ekaterina Seib, Maya Schmid, Hideyuki Shimizu, Tobias Troost, Sunday Faith Oyelere, Biswajit Chakraborty, Martin Baron, and Thomas Klein. The intracellular domains of the dsl ligands serrate and delta provide different activities. Cell Communication and Signaling, Oct 2025. URL: https://doi.org/10.1186/s12964-025-02472-w, doi:10.1186/s12964-025-02472-w. This article has 0 citations and is from a peer-reviewed journal.

3. (sachan2023notchsignallingmultifaceted pages 2-2): Nalani Sachan, Vartika Sharma, Mousumi Mutsuddi, and Ashim Mukherjee. Notch signalling: multifaceted role in development and disease. The FEBS Journal, 291:3030-3059, May 2024. URL: https://doi.org/10.1111/febs.16815, doi:10.1111/febs.16815. This article has 124 citations.

4. (feng2024thestructuraland pages 40-44): X Feng. The structural and functional significance of lipid-binding properties of human notch ligands. Unknown journal, 2024.

5. (handford2018structuralinsightsinto pages 4-6): Penny A. Handford, Boguslawa Korona, Richard Suckling, Christina Redfield, and Susan M. Lea. Structural insights into notch receptor-ligand interactions. Advances in experimental medicine and biology, 1066:33-46, Jan 2018. URL: https://doi.org/10.1007/978-3-319-89512-3\_2, doi:10.1007/978-3-319-89512-3\_2. This article has 25 citations and is from a peer-reviewed journal.

6. (chen2023notchsignalingin pages 18-20): Yao Chen, Haomiao Li, Tian-Ci Yi, Jie Shen, and Junzheng Zhang. Notch signaling in insect development: a simple pathway with diverse functions. International Journal of Molecular Sciences, 24:14028, Sep 2023. URL: https://doi.org/10.3390/ijms241814028, doi:10.3390/ijms241814028. This article has 35 citations.

7. (feng2024thestructuraland pages 21-25): X Feng. The structural and functional significance of lipid-binding properties of human notch ligands. Unknown journal, 2024.

8. (handford2018structuralinsightsinto pages 6-9): Penny A. Handford, Boguslawa Korona, Richard Suckling, Christina Redfield, and Susan M. Lea. Structural insights into notch receptor-ligand interactions. Advances in experimental medicine and biology, 1066:33-46, Jan 2018. URL: https://doi.org/10.1007/978-3-319-89512-3\_2, doi:10.1007/978-3-319-89512-3\_2. This article has 25 citations and is from a peer-reviewed journal.

9. (vazquezulloa2022reversibleandbidirectional pages 5-7): Elenaé Vázquez-Ulloa, Kai-Lan Lin, Marcela Lizano, and Cecilia Sahlgren. Reversible and bidirectional signaling of notch ligands. Critical Reviews in Biochemistry and Molecular Biology, 57:377-398, Jul 2022. URL: https://doi.org/10.1080/10409238.2022.2113029, doi:10.1080/10409238.2022.2113029. This article has 29 citations and is from a peer-reviewed journal.

10. (feng2024thestructuraland pages 25-28): X Feng. The structural and functional significance of lipid-binding properties of human notch ligands. Unknown journal, 2024.

11. (sprinzak2021biophysicsofnotch pages 6-7): David Sprinzak and Stephen C. Blacklow. Biophysics of notch signaling. Annual Review of Biophysics, 50:157-189, May 2021. URL: https://doi.org/10.1146/annurev-biophys-101920-082204, doi:10.1146/annurev-biophys-101920-082204. This article has 280 citations and is from a domain leading peer-reviewed journal.

12. (deliconstantinos2021translationalcontrolof pages 1-4): GEORGIA DELICONSTANTINOS, KONSTANTINA KALODIMOU, and CHRISTOS DELIDAKIS. Translational control of serrate expression in drosophila cells. In Vivo, 35:859-869, Jan 2021. URL: https://doi.org/10.21873/invivo.12326, doi:10.21873/invivo.12326. This article has 1 citations and is from a peer-reviewed journal.

13. (martins2021deltac2domain pages 1-4): Torcato Martins, Yao Meng, Boguslawa Korona, Richard Suckling, Steven Johnson, Penny Handford, Susan M. Lea, and Sarah Bray. Delta c2 domain β1-2 loop contributes to robust notch signalling. bioRxiv, Feb 2021. URL: https://doi.org/10.1101/2021.02.16.431397, doi:10.1101/2021.02.16.431397. This article has 0 citations.

14. (martins2021deltac2domain pages 26-31): Torcato Martins, Yao Meng, Boguslawa Korona, Richard Suckling, Steven Johnson, Penny Handford, Susan M. Lea, and Sarah Bray. Delta c2 domain β1-2 loop contributes to robust notch signalling. bioRxiv, Feb 2021. URL: https://doi.org/10.1101/2021.02.16.431397, doi:10.1101/2021.02.16.431397. This article has 0 citations.

15. (martins2021deltac2domain pages 23-26): Torcato Martins, Yao Meng, Boguslawa Korona, Richard Suckling, Steven Johnson, Penny Handford, Susan M. Lea, and Sarah Bray. Delta c2 domain β1-2 loop contributes to robust notch signalling. bioRxiv, Feb 2021. URL: https://doi.org/10.1101/2021.02.16.431397, doi:10.1101/2021.02.16.431397. This article has 0 citations.

16. (feng2024thestructuraland pages 44-49): X Feng. The structural and functional significance of lipid-binding properties of human notch ligands. Unknown journal, 2024.

17. (martins2021deltac2domain pages 4-8): Torcato Martins, Yao Meng, Boguslawa Korona, Richard Suckling, Steven Johnson, Penny Handford, Susan M. Lea, and Sarah Bray. Delta c2 domain β1-2 loop contributes to robust notch signalling. bioRxiv, Feb 2021. URL: https://doi.org/10.1101/2021.02.16.431397, doi:10.1101/2021.02.16.431397. This article has 0 citations.

18. (deliconstantinos2021translationalcontrolof pages 5-7): GEORGIA DELICONSTANTINOS, KONSTANTINA KALODIMOU, and CHRISTOS DELIDAKIS. Translational control of serrate expression in drosophila cells. In Vivo, 35:859-869, Jan 2021. URL: https://doi.org/10.21873/invivo.12326, doi:10.21873/invivo.12326. This article has 1 citations and is from a peer-reviewed journal.

19. (seib2021theroleof pages 8-9): Ekaterina Seib and Thomas Klein. The role of ligand endocytosis in notch signalling. Biology of the Cell, 113:401-418, Jun 2021. URL: https://doi.org/10.1111/boc.202100009, doi:10.1111/boc.202100009. This article has 44 citations and is from a peer-reviewed journal.

20. (troost2023themeaningof pages 1-2): Tobias Troost, Ekaterina Seib, Alina Airich, Nicole Vüllings, Aleksandar Necakov, Stefano De Renzis, and Thomas Klein. The meaning of ubiquitylation of the dsl ligand delta for the development of drosophila. BMC Biology, Nov 2023. URL: https://doi.org/10.1186/s12915-023-01759-z, doi:10.1186/s12915-023-01759-z. This article has 9 citations and is from a domain leading peer-reviewed journal.

21. (chen2023notchsignalingin pages 5-6): Yao Chen, Haomiao Li, Tian-Ci Yi, Jie Shen, and Junzheng Zhang. Notch signaling in insect development: a simple pathway with diverse functions. International Journal of Molecular Sciences, 24:14028, Sep 2023. URL: https://doi.org/10.3390/ijms241814028, doi:10.3390/ijms241814028. This article has 35 citations.

22. (sprinzak2021biophysicsofnotch pages 3-4): David Sprinzak and Stephen C. Blacklow. Biophysics of notch signaling. Annual Review of Biophysics, 50:157-189, May 2021. URL: https://doi.org/10.1146/annurev-biophys-101920-082204, doi:10.1146/annurev-biophys-101920-082204. This article has 280 citations and is from a domain leading peer-reviewed journal.

23. (lv2024evolutionandfunction pages 25-26): Yan Lv, Xuan Pang, Zhonghong Cao, Changping Song, Baohua Liu, Weiwei Wu, and Qiuxiang Pang. Evolution and function of the notch signaling pathway: an invertebrate perspective. International Journal of Molecular Sciences, 25:3322, Mar 2024. URL: https://doi.org/10.3390/ijms25063322, doi:10.3390/ijms25063322. This article has 36 citations.

24. (chen2023notchsignalingin pages 21-22): Yao Chen, Haomiao Li, Tian-Ci Yi, Jie Shen, and Junzheng Zhang. Notch signaling in insect development: a simple pathway with diverse functions. International Journal of Molecular Sciences, 24:14028, Sep 2023. URL: https://doi.org/10.3390/ijms241814028, doi:10.3390/ijms241814028. This article has 35 citations.

25. (seib2025theintracellulardomains pages 22-22): Ekaterina Seib, Maya Schmid, Hideyuki Shimizu, Tobias Troost, Sunday Faith Oyelere, Biswajit Chakraborty, Martin Baron, and Thomas Klein. The intracellular domains of the dsl ligands serrate and delta provide different activities. Cell Communication and Signaling, Oct 2025. URL: https://doi.org/10.1186/s12964-025-02472-w, doi:10.1186/s12964-025-02472-w. This article has 0 citations and is from a peer-reviewed journal.

26. (feng2024thestructuraland pages 56-60): X Feng. The structural and functional significance of lipid-binding properties of human notch ligands. Unknown journal, 2024.

27. (sprinzak2021biophysicsofnotch pages 4-6): David Sprinzak and Stephen C. Blacklow. Biophysics of notch signaling. Annual Review of Biophysics, 50:157-189, May 2021. URL: https://doi.org/10.1146/annurev-biophys-101920-082204, doi:10.1146/annurev-biophys-101920-082204. This article has 280 citations and is from a domain leading peer-reviewed journal.

28. (handford2018structuralinsightsinto pages 1-4): Penny A. Handford, Boguslawa Korona, Richard Suckling, Christina Redfield, and Susan M. Lea. Structural insights into notch receptor-ligand interactions. Advances in experimental medicine and biology, 1066:33-46, Jan 2018. URL: https://doi.org/10.1007/978-3-319-89512-3\_2, doi:10.1007/978-3-319-89512-3\_2. This article has 25 citations and is from a peer-reviewed journal.

29. (kuintzle2025diversityinnotch pages 10-11): Rachael Kuintzle, Leah A Santat, and Michael B Elowitz. Diversity in notch ligand-receptor signaling interactions. Jan 2025. URL: https://doi.org/10.7554/elife.91422, doi:10.7554/elife.91422. This article has 52 citations and is from a domain leading peer-reviewed journal.

30. (sprinzak2021biophysicsofnotch pages 7-9): David Sprinzak and Stephen C. Blacklow. Biophysics of notch signaling. Annual Review of Biophysics, 50:157-189, May 2021. URL: https://doi.org/10.1146/annurev-biophys-101920-082204, doi:10.1146/annurev-biophys-101920-082204. This article has 280 citations and is from a domain leading peer-reviewed journal.

31. (chen2023notchsignalingin pages 17-18): Yao Chen, Haomiao Li, Tian-Ci Yi, Jie Shen, and Junzheng Zhang. Notch signaling in insect development: a simple pathway with diverse functions. International Journal of Molecular Sciences, 24:14028, Sep 2023. URL: https://doi.org/10.3390/ijms241814028, doi:10.3390/ijms241814028. This article has 35 citations.

32. (lv2024evolutionandfunction pages 35-36): Yan Lv, Xuan Pang, Zhonghong Cao, Changping Song, Baohua Liu, Weiwei Wu, and Qiuxiang Pang. Evolution and function of the notch signaling pathway: an invertebrate perspective. International Journal of Molecular Sciences, 25:3322, Mar 2024. URL: https://doi.org/10.3390/ijms25063322, doi:10.3390/ijms25063322. This article has 36 citations.

33. (rai2026cop9signalosomeregulates pages 7-9): Gayatri Rai, Deepak Maurya, Debleena Mandal, and Bama Charan Mondal. Cop9 signalosome regulates egfr and notch signaling during myeloid-type progenitor cell fate decision in drosophila. Jul 2026. URL: https://doi.org/10.1038/s44319-026-00862-w, doi:10.1038/s44319-026-00862-w. This article has 0 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Ser-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](Ser-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. seib2025theintracellulardomains pages 1-2
2. handford2018structuralinsightsinto pages 6-9
3. deliconstantinos2021translationalcontrolof pages 1-4
4. feng2024thestructuraland pages 40-44
5. deliconstantinos2021translationalcontrolof pages 5-7
6. seib2021theroleof pages 8-9
7. troost2023themeaningof pages 1-2
8. kuintzle2025diversityinnotch pages 10-11
9. chen2023notchsignalingin pages 5-6
10. chen2023notchsignalingin pages 18-20
11. chen2023notchsignalingin pages 21-22
12. lv2024evolutionandfunction pages 25-26
13. seib2025theintracellulardomains pages 22-22
14. lv2024evolutionandfunction pages 2-4
15. sachan2023notchsignallingmultifaceted pages 2-2
16. handford2018structuralinsightsinto pages 4-6
17. feng2024thestructuraland pages 21-25
18. vazquezulloa2022reversibleandbidirectional pages 5-7
19. feng2024thestructuraland pages 25-28
20. sprinzak2021biophysicsofnotch pages 6-7
21. feng2024thestructuraland pages 44-49
22. sprinzak2021biophysicsofnotch pages 3-4
23. feng2024thestructuraland pages 56-60
24. sprinzak2021biophysicsofnotch pages 4-6
25. handford2018structuralinsightsinto pages 1-4
26. sprinzak2021biophysicsofnotch pages 7-9
27. chen2023notchsignalingin pages 17-18
28. lv2024evolutionandfunction pages 35-36
29. Su(H), the *Drosophila* ortholog of mammalian RBPJ/CSL
30. E(spl)
31. https://doi.org/10.3390/ijms25063322,
32. https://doi.org/10.1186/s12964-025-02472-w,
33. https://doi.org/10.1111/febs.16815,
34. https://doi.org/10.1007/978-3-319-89512-3\_2,
35. https://doi.org/10.3390/ijms241814028,
36. https://doi.org/10.1080/10409238.2022.2113029,
37. https://doi.org/10.1146/annurev-biophys-101920-082204,
38. https://doi.org/10.21873/invivo.12326,
39. https://doi.org/10.1101/2021.02.16.431397,
40. https://doi.org/10.1111/boc.202100009,
41. https://doi.org/10.1186/s12915-023-01759-z,
42. https://doi.org/10.7554/elife.91422,
43. https://doi.org/10.1038/s44319-026-00862-w,