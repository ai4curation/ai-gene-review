---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-30T13:34:59.425114'
end_time: '2026-09-30T13:55:17.826191'
duration_seconds: 1218.4
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: ZAP70
  gene_symbol: ZAP70
  uniprot_accession: P43403
  protein_description: 'RecName: Full=Tyrosine-protein kinase ZAP-70; EC=2.7.10.2
    {ECO:0000269|PubMed:15292186}; AltName: Full=70 kDa zeta-chain associated protein;
    AltName: Full=Syk-related tyrosine kinase;'
  gene_info: Name=ZAP70; Synonyms=SRK;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the protein kinase superfamily. Tyr protein
  protein_domains: Kinase-like_dom_sf. (IPR011009); Kinase_SYK/ZAP-70_inter-SH2_sf.
    (IPR023420); Non-receptor_tyrosine_kinases. (IPR050198); Prot_kinase_dom. (IPR000719);
    Protein_kinase_ATP_BS. (IPR017441)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 29
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: ZAP70-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: ZAP70-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: ZAP70-deep-research-falcon_artifacts/artifact-02.md
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
- **UniProt Accession:** P43403
- **Protein Description:** RecName: Full=Tyrosine-protein kinase ZAP-70; EC=2.7.10.2 {ECO:0000269|PubMed:15292186}; AltName: Full=70 kDa zeta-chain associated protein; AltName: Full=Syk-related tyrosine kinase;
- **Gene Information:** Name=ZAP70; Synonyms=SRK;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the protein kinase superfamily. Tyr protein
- **Key Domains:** Kinase-like_dom_sf. (IPR011009); Kinase_SYK/ZAP-70_inter-SH2_sf. (IPR023420); Non-receptor_tyrosine_kinases. (IPR050198); Prot_kinase_dom. (IPR000719); Protein_kinase_ATP_BS. (IPR017441)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ZAP70" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ZAP70' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ZAP70** (gene ID: ZAP70, UniProt: P43403) in human.

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
- **UniProt Accession:** P43403
- **Protein Description:** RecName: Full=Tyrosine-protein kinase ZAP-70; EC=2.7.10.2 {ECO:0000269|PubMed:15292186}; AltName: Full=70 kDa zeta-chain associated protein; AltName: Full=Syk-related tyrosine kinase;
- **Gene Information:** Name=ZAP70; Synonyms=SRK;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the protein kinase superfamily. Tyr protein
- **Key Domains:** Kinase-like_dom_sf. (IPR011009); Kinase_SYK/ZAP-70_inter-SH2_sf. (IPR023420); Non-receptor_tyrosine_kinases. (IPR050198); Prot_kinase_dom. (IPR000719); Protein_kinase_ATP_BS. (IPR017441)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ZAP70" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ZAP70' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ZAP70** (gene ID: ZAP70, UniProt: P43403) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Comprehensive Research Report: ZAP70 Gene Function and Annotation

## Gene Identity Verification

The gene ZAP70 (UniProt: P43403) encodes the tyrosine-protein kinase ZAP-70 (zeta-chain associated protein kinase 70), a 70 kDa cytoplasmic tyrosine kinase that is a member of the Syk family of protein tyrosine kinases (fernandezaguilar2023astoryof pages 5-7, aktas2024chroniclymphocyticleukemia pages 114-117). ZAP70 belongs to the protein kinase superfamily and contains characteristic Tyr protein kinase domains, tandem SH2 domains, and the Syk/ZAP-70 inter-SH2 structural feature (fernandezaguilar2023astoryof pages 5-7, hobbs2021differencesinthe pages 1-3). The gene is expressed primarily in T cells and natural killer cells in humans (fernandezaguilar2023astoryof pages 5-7).

## Structural Organization and Domains

ZAP70 exhibits a modular architecture consisting of an N-terminal regulatory region and a C-terminal catalytic domain (fernandezaguilar2023astoryof pages 5-7, hobbs2021differencesinthe pages 1-3). The regulatory module comprises two tandem Src homology 2 (SH2) domains—an N-terminal SH2 domain (N-SH2) and a C-terminal SH2 domain (C-SH2)—connected by a helical linker known as interdomain A (gangopadhyay2020anallosterichot pages 1-4, hobbs2021differencesinthe pages 1-3). These tandem SH2 domains cooperatively recognize and bind doubly phosphorylated immunoreceptor tyrosine-based activation motifs (ITAMs) with high affinity and specificity (gangopadhyay2020anallosterichot pages 1-4, ashouri2022zap70toolittle pages 2-3).

Between the C-terminal SH2 domain and the kinase domain lies interdomain B, a flexible regulatory linker containing important tyrosine residues Y292, Y315, and Y319 that become phosphorylated following T-cell receptor (TCR) activation and regulate ZAP70 enzymatic activity (fernandezaguilar2023astoryof pages 5-7, fernandezaguilar2023astoryof pages 7-9). The C-terminal kinase domain contains the catalytic machinery and includes activation loop tyrosines Y492 and Y493, whose phosphorylation is essential for enzymatic activation (fernandezaguilar2023astoryof pages 7-9, anto2023cyclophilinaassociates pages 1-2).

| Domain/Region | Location | Structure | Function |
|---|---|---|---|
| N-terminal SH2 domain (N-SH2) | N-terminal regulatory module | One half of the tandem-SH2 (tSH2) module; connected to C-SH2 by helical interdomain A. It contains a phosphotyrosine-binding site that cooperates with C-SH2 to recognize biphosphorylated immunoreceptor tyrosine-based activation motifs (ITAMs). | Engages one ITAM phosphotyrosine and helps convert the separated, autoinhibitory SH2 arrangement into the compact ITAM-bound conformation. Cooperative two-site binding confers high avidity and specificity for doubly phosphorylated CD3 and TCR-ζ ITAMs, recruiting ZAP70 to the receptor complex. (gangopadhyay2020anallosterichot pages 1-4, hobbs2021differencesinthe pages 1-3, ashouri2022zap70toolittle pages 2-3) |
| Interdomain A (inter-SH2 linker) | Between N-SH2 and C-SH2 | Predominantly helical linker that structurally couples the two SH2 domains and permits their relative reorientation. | Transmits the conformational effect of phospho-ITAM binding. In inactive ZAP70, the SH2 domains occupy a separated, L-shaped arrangement; biphosphorylated ITAM binding drives formation of a compact, Y-shaped tandem-SH2 conformation that partially releases kinase autoinhibition. This transition contributes a kinetic and thermodynamic checkpoint to TCR ligand discrimination. (gangopadhyay2020anallosterichot pages 1-4, hobbs2021differencesinthe pages 1-3, gangopadhyay2021anevolutionarydivergent pages 13-17) |
| C-terminal SH2 domain (C-SH2) | C-terminal half of the tandem-SH2 regulatory module, immediately before interdomain B | SH2 fold containing a phosphotyrosine-binding pocket that works cooperatively with N-SH2. Structural evidence supports initial formation of an encounter complex through one ITAM phosphotyrosine, followed by engagement of the second phosphotyrosine and tandem-SH2 closure. | Initiates and stabilizes recognition of doubly phosphorylated ITAMs in CD3 and TCR-ζ. Together with N-SH2, it determines receptor docking, activation-dependent plasma-membrane recruitment, and allosteric relief of autoinhibition. Pathogenic substitutions affecting its phosphotyrosine-binding pocket impair TCR-ζ binding and can cause combined immunodeficiency. (gangopadhyay2020anallosterichot pages 1-4, anto2023cyclophilinaassociates pages 2-4, fernandezaguilar2023astoryof pages 5-7) |
| Interdomain B — Y292 | Between C-SH2 and the kinase domain | Flexible regulatory linker participating in intramolecular contacts that stabilize autoinhibited ZAP70; Y292 is a phosphorylation-dependent signaling site. | Phosphorylation of Y292 is predominantly inhibitory and promotes negative regulation of TCR signaling. Preventing its phosphorylation with a Y292F substitution increases TCR signaling and T-cell proliferation, showing that this site helps constrain signal magnitude. (anto2023cyclophilinaassociates pages 1-2, fernandezaguilar2023astoryof pages 7-9) |
| Interdomain B — Y315 | Between C-SH2 and the kinase domain | Regulatory tyrosine exposed following ITAM-dependent conformational opening; phosphorylation helps destabilize the closed state and creates an SH2-binding interface. | Supports release of autoinhibition and stabilization of active ZAP70. Phospho-Y315 recruits signaling partners including Vav and CrkII, coupling activated ZAP70 to cytoskeletal and downstream signaling machinery. (ashouri2022zap70toolittle pages 2-3, anto2023cyclophilinaassociates pages 1-2) |
| Interdomain B — Y319 | Between C-SH2 and the kinase domain | Regulatory phosphotyrosine and docking site for the LCK SH2 domain. | Promotes further LCK-dependent phosphorylation and stabilizes productive kinase–receptor signaling. Y319F disrupts LCK association and markedly reduces LAT and SLP-76 phosphorylation, NFAT activation, and IL-2 production; increasing SH2-binding affinity around Y319 enhances basal and early TCR signaling. (fernandezaguilar2023astoryof pages 14-16, anto2023cyclophilinaassociates pages 1-2) |
| Protein-tyrosine kinase domain — activation loop Y492/Y493 | C-terminal catalytic region | Bilobed protein-kinase fold containing the ATP-binding and catalytic machinery. In inactive ZAP70 it adopts a restrained Src/CDK-like conformation; the activation loop contains adjacent regulatory tyrosines Y492 and Y493. | Catalyzes ATP-dependent transfer of phosphate to tyrosine residues, principally on LAT and SLP-76 in canonical TCR signaling. Activation-loop phosphorylation—especially LCK-mediated phosphorylation of Y493—stabilizes a catalytically competent conformation; Y492 also modulates activation-loop behavior. Combined disruption of Y492/Y493 blocks downstream signaling. (ashouri2022zap70toolittle pages 3-5, fernandezaguilar2023astoryof pages 7-9, fernandezaguilar2023astoryof pages 14-16, anto2023cyclophilinaassociates pages 1-2) |


*Table: This table maps ZAP70’s tandem SH2 regulatory module, linker regions, and catalytic domain to their roles in phospho-ITAM recognition, autoinhibition, activation, and phosphorylation-dependent signaling.*

## Primary Enzymatic Function and Substrate Specificity

ZAP70 functions as a protein tyrosine kinase that catalyzes the ATP-dependent transfer of phosphate groups to tyrosine residues on downstream signaling proteins (ashouri2022zap70toolittle pages 2-3, fernandezaguilar2023astoryof pages 7-9, aktas2024chroniclymphocyticleukemia pages 114-117). The primary substrates of ZAP70 are the adaptor proteins LAT (linker for activation of T cells) and SLP-76 (also known as LCP2) (ashouri2022zap70toolittle pages 3-5, ashouri2022zap70toolittle pages 2-3, fernandezaguilar2023astoryof pages 7-9, anto2023cyclophilinaassociates pages 12-14).

Following its activation, ZAP70 phosphorylates multiple tyrosine residues on LAT, with five functionally important sites reported in the literature (ashouri2022zap70toolittle pages 3-5, ashouri2022zap70toolittle pages 2-3). Phosphorylated LAT serves as a crucial scaffold that recruits PLCγ1, GRB2-SOS complexes, and through GADS, connects to SLP-76, thereby assembling the LAT signalosome (ashouri2022zap70toolittle pages 2-3, fernandezaguilar2023astoryof pages 7-9).

ZAP70 also phosphorylates SLP-76, creating docking sites for additional signaling proteins including GADS, ITK, VAV, NCK, and PLCγ1 (ashouri2022zap70toolittle pages 3-5, fernandezaguilar2023astoryof pages 7-9). The phosphorylation of LAT and SLP-76 initiates the formation of signaling complexes that propagate TCR signals to downstream effector pathways (fernandezaguilar2023astoryof pages 14-16, fernandezaguilar2023astoryof pages 7-9).

ZAP70 exhibits substrate specificity distinct from other kinases. Its kinase domain contains an unusually basic substrate-binding region that preferentially recognizes substrate sequences enriched in acidic residues, particularly an acidic residue immediately N-terminal to the target tyrosine (ashouri2022zap70toolittle pages 3-5). This electrostatic filtering mechanism contributes to ZAP70's selective phosphorylation of LAT and SLP-76 rather than other tyrosine-containing proteins (ashouri2022zap70toolittle pages 3-5).

Importantly, ZAP70 does not phosphorylate TCR ITAMs; this initial phosphorylation is performed by the Src-family kinase Lck (ashouri2022zap70toolittle pages 3-5, ashouri2022zap70toolittle pages 2-3). ZAP70 also undergoes autophosphorylation on regulatory tyrosines as part of its activation process (anto2023cyclophilinaassociates pages 1-2, anto2023cyclophilinaassociates pages 12-14).

| Substrate or target | Phosphorylation sites (if known) | Function | Downstream effects |
|---|---|---|---|
| **LAT (linker for activation of T cells)** | Multiple tyrosines; five functionally important sites are reported, with human Y132, Y171, Y191, and Y226 among the principal signalosome-forming sites | Major direct ZAP70 substrate and transmembrane scaffold. Phosphorylated LAT recruits PLCγ1 and GRB2–SOS and, through GADS, connects to SLP-76 (ashouri2022zap70toolittle pages 3-5, ashouri2022zap70toolittle pages 2-3) | Assembles the LAT signalosome; activates PLCγ1–Ca²⁺–NFAT, DAG–PKC, and Ras–MAPK/ERK pathways, leading to cytoskeletal remodeling, IL-2 production, proliferation, and differentiation (fernandezaguilar2023astoryof pages 14-16, ashouri2022zap70toolittle pages 2-3, fernandezaguilar2023astoryof pages 7-9) |
| **SLP-76 / LCP2** | Principal human regulatory sites include Y113, Y128, and Y145 | Direct or closely coupled ZAP70-pathway substrate and cytosolic scaffold; phosphorylated SLP-76 organizes complexes containing GADS, ITK, VAV, NCK, and PLCγ1 (ashouri2022zap70toolittle pages 3-5, fernandezaguilar2023astoryof pages 7-9) | Supports PLCγ1 activation and calcium mobilization, actin reorganization, immune-synapse formation, MAPK signaling, NFAT activation, and cytokine production (fernandezaguilar2023astoryof pages 14-16, ashouri2022zap70toolittle pages 2-3, anto2023cyclophilinaassociates pages 1-2) |
| **VAV-family signaling proteins** | Multiple regulatory tyrosines; no single ZAP70-selective site established in the cited evidence | Reported phosphorylation target or ZAP70-associated effector in activated TCR complexes; VAV can also dock through phosphorylated ZAP70 Y315, so direct versus complex-mediated phosphorylation is context-dependent (aktas2024chroniclymphocyticleukemia pages 114-117, anto2023cyclophilinaassociates pages 1-2) | Activates Rho-family GTPases and promotes actin remodeling, immune-synapse organization, adhesion, and transcriptional signaling (aktas2024chroniclymphocyticleukemia pages 114-117, anto2023cyclophilinaassociates pages 1-2) |
| **ZAP70 itself** | Regulatory tyrosines Y292, Y315, Y319, Y492, and Y493; autophosphorylation contributes after upstream LCK-dependent activation | ZAP70 is both an LCK substrate and an autophosphorylation target. Y493 in the activation loop promotes catalysis; Y315/Y319 stabilize signaling interactions; Y292 provides negative regulation (fernandezaguilar2023astoryof pages 7-9, anto2023cyclophilinaassociates pages 1-2, anto2023cyclophilinaassociates pages 12-14) | Tunes catalytic activity, LCK docking, recruitment of VAV/CrkII, and subsequent LAT/SLP-76 phosphorylation; site-specific modification sets TCR signaling strength and duration (fernandezaguilar2023astoryof pages 14-16, anto2023cyclophilinaassociates pages 1-2) |


*Table: This table distinguishes ZAP70’s principal downstream substrates from associated or self-phosphorylation targets and links each modification to proximal T-cell receptor signaling outcomes.*

## Cellular Localization and Membrane Recruitment

In resting T cells, ZAP70 is predominantly localized in the cytoplasm, where it exists in a non-phosphorylated, autoinhibited state (anto2023cyclophilinaassociates pages 12-14, anto2023cyclophilinaassociates pages 4-7, anto2023cyclophilinaassociates pages 2-4, ashouri2022zap70toolittle pages 2-3, anto2023cyclophilinaassociates pages 1-2). ZAP70 does not possess transmembrane domains or lipid anchors and is not constitutively membrane-associated (fernandezaguilar2023astoryof pages 7-9, fernandezaguilar2023astoryof pages 5-7, aktas2024chroniclymphocyticleukemia pages 114-117).

Following TCR engagement by peptide-MHC complexes, ZAP70 undergoes stimulus-dependent translocation to the plasma membrane through a well-defined mechanism (anto2023cyclophilinaassociates pages 12-14, anto2023cyclophilinaassociates pages 4-7, ashouri2022zap70toolittle pages 2-3). The Src-family kinase Lck, which is associated with the CD4 or CD8 coreceptors, first phosphorylates the ITAM motifs in the cytoplasmic tails of CD3 subunits and the TCR ζ-chain (anto2023cyclophilinaassociates pages 12-14, ashouri2022zap70toolittle pages 2-3, fernandezaguilar2023astoryof pages 7-9, fernandezaguilar2023astoryof pages 5-7).

These doubly phosphorylated ITAMs serve as high-affinity docking sites for ZAP70's tandem SH2 domains (anto2023cyclophilinaassociates pages 12-14, anto2023cyclophilinaassociates pages 2-4, ashouri2022zap70toolittle pages 2-3). The N-SH2 and C-SH2 domains cooperatively bind to the two phosphotyrosine residues within the ITAM, recruiting ZAP70 from the cytoplasm to the membrane-proximal TCR signaling complex (gangopadhyay2020anallosterichot pages 1-4, anto2023cyclophilinaassociates pages 12-14, fernandezaguilar2023astoryof pages 5-7). This recruitment localizes ZAP70 to the immunological synapse, the specialized membrane region formed at the T cell-antigen presenting cell interface (anto2023cyclophilinaassociates pages 12-14, anto2023cyclophilinaassociates pages 4-7, anto2023cyclophilinaassociates pages 1-2).

## Activation Mechanism and Regulation

ZAP70 exists in a tightly autoinhibited conformation in resting cells (hobbs2021differencesinthe pages 1-3, gangopadhyay2020anallosterichot pages 1-4, ashouri2022zap70toolittle pages 2-3). In this inactive state, the two SH2 domains adopt a separated, L-shaped arrangement, and the kinase domain assumes an inactive Cdk/Src-like conformation (gangopadhyay2020anallosterichot pages 1-4, hobbs2021differencesinthe pages 1-3).

Activation proceeds through multiple sequential steps. First, Lck phosphorylates ITAM tyrosines, creating the docking sites that recruit ZAP70 (ashouri2022zap70toolittle pages 2-3, fernandezaguilar2023astoryof pages 5-7). Binding to doubly phosphorylated ITAMs induces a biphasic conformational transition: the C-SH2 domain initially forms an encounter complex with one phosphotyrosine, followed by engagement of the second phosphotyrosine and reorientation of the SH2 domains into a compact Y-shaped conformation (gangopadhyay2020anallosterichot pages 1-4). This conformational change partially relieves kinase autoinhibition (ashouri2022zap70toolittle pages 2-3, fernandezaguilar2023astoryof pages 14-16).

However, ITAM binding alone is generally insufficient for full activation (ashouri2022zap70toolittle pages 2-3). Sustained TCR engagement, particularly with agonist peptide-MHC, allows coreceptor-associated Lck to phosphorylate key regulatory tyrosines on ZAP70, including Y315, Y319, and Y493 (ashouri2022zap70toolittle pages 2-3, fernandezaguilar2023astoryof pages 14-16). These phosphorylation events further relieve autoinhibition and activate the kinase domain (ashouri2022zap70toolittle pages 2-3, fernandezaguilar2023astoryof pages 14-16, anto2023cyclophilinaassociates pages 12-14).

Recent studies have identified an "evolutionary divergent thermodynamic brake" in ZAP70's tandem SH2 domain that imposes an energetic barrier to the final conformational transition required for full ITAM binding and activation (gangopadhyay2021anevolutionarydivergent pages 13-17, gangopadhyay2021anevolutionarydivergent pages 1-5). This brake helps maintain ZAP70 in an open, inactive conformation in resting cells and contributes to kinetic proofreading by imposing additional time delays before ZAP70 activation (gangopadhyay2021anevolutionarydivergent pages 13-17, gangopadhyay2021anevolutionarydivergent pages 1-5).

| Phosphorylation Site | Kinase Responsible | Regulatory Effect | Mechanism |
|---|---|---|---|
| **Y292** — interdomain B | Lck/Src-family kinases are upstream; ZAP-70 autophosphorylation may also contribute | **Inhibitory / negative feedback** | Creates a negative-regulatory phosphotyrosine interface associated with signal attenuation. Preventing phosphorylation with Y292F enhances TCR signaling and T-cell proliferation, indicating that pY292 limits ZAP-70 pathway output. (anto2023cyclophilinaassociates pages 1-2, fernandezaguilar2023astoryof pages 7-9) |
| **Y315** — interdomain B | Primarily **Lck** following phospho-ITAM recruitment | **Activating / scaffolding** | Helps relieve autoinhibition and stabilize active ZAP-70. Phosphorylated Y315 also recruits SH2-containing effectors such as Vav and CrkII, coupling ZAP-70 to cytoskeletal and downstream signaling pathways. (ashouri2022zap70toolittle pages 2-3, anto2023cyclophilinaassociates pages 1-2) |
| **Y319** — interdomain B | Primarily **Lck**, with phosphorylation reinforced through Lck–ZAP-70 docking | **Activating / signal-amplifying** | pY319 binds the Lck SH2 domain, stabilizing productive Lck–ZAP-70 association and promoting further phosphorylation. Y319F markedly reduces LAT and SLP-76 phosphorylation, NFAT activation, and IL-2 production; increasing SH2-binding affinity around this site enhances basal and TCR-induced signaling. (fernandezaguilar2023astoryof pages 14-16, anto2023cyclophilinaassociates pages 1-2) |
| **Y492** — kinase-domain activation loop | **Lck/Src-family kinase input**, with possible contribution from ZAP-70 autophosphorylation | **Context-dependent; generally regulatory** | Activation-loop phosphorylation alters kinase-domain conformation. Some summaries group Y492 with Y493 as necessary for full activity, although site-specific literature has reported more complex—and sometimes restraining—effects for Y492; it should not be interpreted as equivalent to the strongly activating Y493 site. (fernandezaguilar2023astoryof pages 7-9, fernandezaguilar2023astoryof pages 14-16) |
| **Y493** — kinase-domain activation loop | Primarily **Lck** | **Strongly activating** | Phosphorylation reorganizes the activation loop into a catalytically competent conformation, increasing kinase activity toward LAT and SLP-76. Loss of Y493 phosphorylation impairs downstream TCR signaling, whereas increased pY493 tracks with enhanced proximal signaling. (anto2023cyclophilinaassociates pages 1-2, ashouri2022zap70toolittle pages 2-3, schultz2022acysteineresidue pages 7-10) |


*Table: Key ZAP-70 phosphotyrosines have distinct activating, inhibitory, and scaffolding effects. The table summarizes their likely upstream kinase, location, and consequences for proximal T-cell receptor signaling.*

## Kinetic Proofreading and Ligand Discrimination

ZAP70 plays a central role in kinetic proofreading, a mechanism that allows T cells to discriminate between self and foreign antigens based on TCR-peptide-MHC binding duration (gangopadhyay2021anevolutionarydivergent pages 13-17, goyette2020regulatedunbindingof pages 1-3, gangopadhyay2021anevolutionarydivergent pages 1-5, goyette2020regulatedunbindingof pages 3-4, ashouri2022zap70toolittle pages 2-3). TCR signaling proceeds through sequential, time-dependent phosphorylation and recruitment steps—ITAM phosphorylation, ZAP70 recruitment, and ZAP70 phosphorylation—each acting as a temporal checkpoint (goyette2020regulatedunbindingof pages 1-3, goyette2020regulatedunbindingof pages 3-4, ashouri2022zap70toolittle pages 2-3).

Self-peptide-MHC typically produces brief TCR interactions that phosphorylate ITAMs and recruit ZAP70 but dissociate before Lck can adequately phosphorylate and activate ZAP70 (ashouri2022zap70toolittle pages 2-3). In contrast, agonist peptide-MHC generates longer-lasting interactions that allow completion of the phosphorylation cascade, leading to full ZAP70 activation and downstream signaling (goyette2020regulatedunbindingof pages 1-3, ashouri2022zap70toolittle pages 2-3).

The multi-step activation of ZAP70—involving ITAM binding, conformational changes, and phosphorylation at multiple regulatory sites—provides multiple kinetic checkpoints that enhance ligand selectivity (gangopadhyay2021anevolutionarydivergent pages 13-17, gangopadhyay2021anevolutionarydivergent pages 1-5). Recent work demonstrates that ZAP70 binds doubly phosphorylated ITAMs through a biphasic mechanism with fast and slow kinetic phases, with the slow phase reflecting the thermodynamic brake mentioned above (gangopadhyay2021anevolutionarydivergent pages 13-17, gangopadhyay2021anevolutionarydivergent pages 1-5). This brake is unique to ZAP70 and absent in its paralog Syk, explaining ZAP70's greater ligand selectivity and lower basal activity compared to Syk (gangopadhyay2021anevolutionarydivergent pages 13-17, gangopadhyay2021anevolutionarydivergent pages 1-5).

ZAP70's tandem SH2 domains also exhibit regulated unbinding: phosphatases such as CD45 can accelerate ZAP70 dissociation from the TCR when the extracellular TCR-peptide-MHC interaction ends, allowing rapid signal termination for short-lived ligands while preserving sustained signaling for long-lived interactions (goyette2020regulatedunbindingof pages 1-3, goyette2020regulatedunbindingof pages 3-4). This kinetic avidity mechanism couples intracellular ZAP70 residence time to extracellular ligand dwell time, preserving the fidelity of kinetic proofreading (goyette2020regulatedunbindingof pages 1-3, goyette2020regulatedunbindingof pages 21-23).

## Signaling Pathways and Biological Processes

ZAP70 is essential for TCR signal transduction and couples proximal receptor activation to multiple downstream signaling pathways (fernandezaguilar2023astoryof pages 14-16, ashouri2022zap70toolittle pages 2-3, fernandezaguilar2023astoryof pages 7-9, aktas2024chroniclymphocyticleukemia pages 114-117, anto2023cyclophilinaassociates pages 1-2). Following ZAP70-mediated phosphorylation of LAT and SLP-76, these scaffolds recruit and organize downstream effector molecules that activate several major signaling branches (ashouri2022zap70toolittle pages 2-3, fernandezaguilar2023astoryof pages 7-9).

**Calcium Signaling**: Phosphorylated LAT and SLP-76 recruit and activate phospholipase C-γ1 (PLCγ1), which hydrolyzes phosphatidylinositol 4,5-bisphosphate to generate inositol 1,4,5-trisphosphate (IP3) and diacylglycerol (DAG) (ashouri2022zap70toolittle pages 2-3, fernandezaguilar2023astoryof pages 7-9). IP3 triggers calcium release from intracellular stores, leading to activation of the transcription factor NFAT (nuclear factor of activated T cells) (fernandezaguilar2023astoryof pages 14-16, ashouri2022zap70toolittle pages 2-3, anto2023cyclophilinaassociates pages 1-2).

**MAPK/ERK Pathway**: ZAP70-dependent phosphorylation events activate the Ras-MAPK/ERK signaling cascade through recruitment of GRB2-SOS complexes to phosphorylated LAT (fernandezaguilar2023astoryof pages 14-16, ashouri2022zap70toolittle pages 2-3, fernandezaguilar2023astoryof pages 7-9, anto2023cyclophilinaassociates pages 1-2). This pathway controls transcriptional responses and cell proliferation (fernandezaguilar2023astoryof pages 14-16, ashouri2022zap70toolittle pages 2-3).

**PKC Activation**: DAG generated downstream of ZAP70 signaling activates protein kinase C (PKC) family members, which contribute to transcriptional activation and cytoskeletal remodeling (ashouri2022zap70toolittle pages 2-3, anto2023cyclophilinaassociates pages 1-2).

**Cytoskeletal Remodeling**: ZAP70 signaling promotes activation of VAV family proteins, which function as guanine nucleotide exchange factors for Rho-family GTPases, leading to actin reorganization, immune synapse formation, and adhesion (ashouri2022zap70toolittle pages 2-3, aktas2024chroniclymphocyticleukemia pages 114-117, anto2023cyclophilinaassociates pages 1-2).

These coordinated signaling pathways ultimately drive T-cell activation, proliferation, differentiation into effector cells, and cytokine production including IL-2 (fernandezaguilar2023astoryof pages 14-16, fernandezaguilar2023astoryof pages 7-9, aktas2024chroniclymphocyticleukemia pages 114-117, anto2023cyclophilinaassociates pages 1-2). ZAP70 is also essential for T-cell development, with its activity controlling thymic selection processes that establish central tolerance (ashouri2022zap70toolittle pages 2-3, fernandezaguilar2023astoryof pages 7-9).

## Regulatory Mechanisms

ZAP70 activity is regulated through multiple mechanisms beyond ITAM-dependent recruitment and Lck-mediated phosphorylation. Recent research has identified cyclophilin A (CypA) as a negative regulator of ZAP70 (anto2023cyclophilinaassociates pages 1-2). Following TCR stimulation, CypA associates transiently with ZAP70's interdomain B region in an Lck-dependent manner and is recruited to the immunological synapse (anto2023cyclophilinaassociates pages 1-2). Enzymatically active CypA reduces ZAP70 catalytic activity, both through direct inhibition and by affecting ZAP70 autophosphorylation (anto2023cyclophilinaassociates pages 12-14, anto2023cyclophilinaassociates pages 1-2). Cyclosporin A, which blocks CypA, can enhance early ZAP70 activity, identifying CypA as a modulatory brake on TCR signaling (anto2023cyclophilinaassociates pages 12-14, anto2023cyclophilinaassociates pages 1-2).

Phosphorylation at different sites produces distinct regulatory effects. Y493 phosphorylation in the activation loop strongly promotes catalytic activity (anto2023cyclophilinaassociates pages 1-2, ashouri2022zap70toolittle pages 2-3). Y315 and Y319 phosphorylation stabilize the active conformation and create docking sites for effector proteins: pY319 recruits Lck, amplifying signal propagation, while pY315 recruits VAV and CrkII (anto2023cyclophilinaassociates pages 1-2, fernandezaguilar2023astoryof pages 14-16). In contrast, Y292 phosphorylation provides negative feedback, as preventing its phosphorylation enhances TCR signaling (anto2023cyclophilinaassociates pages 1-2).

## Recent Developments (2023-2024)

Recent studies have expanded understanding of ZAP70 function beyond canonical TCR signaling. A 2024 study by Chen et al. demonstrated that in chronic lymphocytic leukemia (CLL), particularly IGHV-unmutated disease, ZAP70 enhances constitutive tonic B-cell receptor signaling rather than ligand-dependent signaling (chen2024zap70augmentstonic pages 7-8, chen2024zap70augmentstonic pages 4-5). ZAP70 constitutively associates with cytoskeletal proteins and regulates actin remodeling, BCR mobility, and receptor clustering (chen2024zap70augmentstonic pages 7-8). ZAP70 also amplifies CCR7 signaling and chemotaxis toward CCL19 and CCL21 through enhanced PI3K-AKT activation and LCP1 phosphorylation, contributing to CLL cell trafficking and aggressive disease biology (chen2024zap70augmentstonic pages 4-5).

A 2023 study identified novel pathogenic variants in ZAP70's C-terminal SH2 domain that cause combined immunodeficiency (mongellaz2023combinedimmunodeficiencycaused pages 13-13, mongellaz2023combinedimmunodeficiencycaused pages 12-13). These mutations disrupt the phosphotyrosine-binding pocket required for TCR-ζ recognition, impairing ZAP70 recruitment and T-cell development (mongellaz2023combinedimmunodeficiencycaused pages 13-13, mongellaz2023combinedimmunodeficiencycaused pages 12-13).

Additional 2023 work characterized the cyclophilin A regulatory mechanism described above, identifying a novel post-translational control point for ZAP70 activity (anto2023cyclophilinaassociates pages 1-2). This discovery adds to understanding of how ZAP70 activity is dynamically tuned during T-cell activation.

## Clinical and Disease Significance

Loss-of-function mutations in ZAP70 cause severe combined immunodeficiency characterized by absent or non-functional CD8+ T cells and impaired CD4+ T-cell function (fernandezaguilar2023astoryof pages 7-9, mongellaz2023combinedimmunodeficiencycaused pages 13-13, mongellaz2023combinedimmunodeficiencycaused pages 12-13). The severity reflects ZAP70's essential role in TCR signaling and T-cell development.

Conversely, gain-of-function mutations that weaken ZAP70 autoinhibition can cause autoimmune disease by enhancing T-cell responses to weak or self-ligands that would normally be ignored (ashouri2022zap70toolittle pages 2-3, mongellaz2023combinedimmunodeficiencycaused pages 12-13). Both hypoactive and hyperactive ZAP70 can thus lead to autoimmunity through distinct mechanisms: hypoactive ZAP70 compromises negative selection and peripheral tolerance, while hyperactive ZAP70 increases sensitivity to self-antigens (ashouri2022zap70toolittle pages 2-3).

In hematologic malignancies, ZAP70 expression is an important prognostic marker. High ZAP70 expression in CLL associates with IGHV-unmutated disease, more aggressive clinical course, and shorter treatment-free survival (chen2024zap70augmentstonic pages 7-8, aktas2024chroniclymphocyticleukemia pages 114-117). ZAP70's role in enhancing tonic BCR signaling, PI3K-AKT activation, and chemotaxis contributes to disease progression (chen2024zap70augmentstonic pages 7-8, chen2024zap70augmentstonic pages 4-5).

## Summary

ZAP70 is a 70 kDa cytoplasmic tyrosine kinase that serves as a critical signal transducer immediately downstream of the T-cell receptor. Its primary enzymatic function is to phosphorylate the adaptor proteins LAT and SLP-76 on specific tyrosine residues, initiating assembly of signaling complexes that propagate TCR signals to calcium mobilization, MAPK activation, and transcriptional responses. ZAP70 resides in the cytoplasm of resting T cells and translocates to the plasma membrane through SH2-domain-mediated recognition of Lck-phosphorylated ITAMs in the TCR complex. Its multi-step activation mechanism, involving ITAM binding, conformational changes, and phosphorylation at multiple regulatory sites, implements kinetic proofreading that allows T cells to discriminate foreign antigens from self-peptides based on binding duration. Recent work has identified novel regulatory mechanisms including cyclophilin A-mediated inhibition and characterized ZAP70's role in B-cell malignancies beyond its canonical T-cell function. Dysregulation of ZAP70—whether through loss of function, gain of function, or aberrant expression—contributes to immunodeficiency, autoimmunity, and hematologic malignancies, underscoring its central importance in adaptive immunity.

References

1. (fernandezaguilar2023astoryof pages 5-7): Luis M. Fernández-Aguilar, Inmaculada Vico-Barranco, Mikel M. Arbulo-Echevarria, and Enrique Aguado. A story of kinases and adaptors: the role of lck, zap-70 and lat in switch panel governing t-cell development and activation. Biology, 12:1163, Aug 2023. URL: https://doi.org/10.3390/biology12091163, doi:10.3390/biology12091163. This article has 65 citations.

2. (aktas2024chroniclymphocyticleukemia pages 114-117): Esin Çetin Aktaş, Murat Koşer, Suzan Çınar, Günnur Deniz, and Nilgün Işıksaçan. Chronic Lymphocytic Leukemia Cytokine Content: Relationship with Zap70 Expression, pages 105-125. Istanbul University Press, Dec 2024. URL: https://doi.org/10.26650/b/ls17ls30.2025.006, doi:10.26650/b/ls17ls30.2025.006. This article has 0 citations.

3. (hobbs2021differencesinthe pages 1-3): Helen T. Hobbs, Neel H. Shah, Jean M. Badroos, Christine L. Gee, Susan Marqusee, and John Kuriyan. Differences in the dynamics of the <scp>tandem‐sh2</scp> modules of the syk and <scp>zap</scp>‐70 tyrosine kinases. Protein Science, 30:2373-2384, Oct 2021. URL: https://doi.org/10.1002/pro.4199, doi:10.1002/pro.4199. This article has 23 citations and is from a peer-reviewed journal.

4. (gangopadhyay2020anallosterichot pages 1-4): Kaustav Gangopadhyay, Bharat Manna, Swarnendu Roy, Sunitha Kumari, Olivia Debnath, Subhankar Chowdhury, Amit Ghosh, and Rahul Das. An allosteric hot spot in the tandem-sh2 domain of zap-70 regulates t-cell signaling. bioRxiv, Nov 2020. URL: https://doi.org/10.1101/842534, doi:10.1101/842534. This article has 21 citations.

5. (ashouri2022zap70toolittle pages 2-3): Judith F. Ashouri, Wan‐Lin Lo, Trang T. T. Nguyen, Lin Shen, and Arthur Weiss. Zap70, too little, too much can lead to autoimmunity. Immunological Reviews, 307:145-160, Dec 2022. URL: https://doi.org/10.1111/imr.13058, doi:10.1111/imr.13058. This article has 55 citations and is from a domain leading peer-reviewed journal.

6. (fernandezaguilar2023astoryof pages 7-9): Luis M. Fernández-Aguilar, Inmaculada Vico-Barranco, Mikel M. Arbulo-Echevarria, and Enrique Aguado. A story of kinases and adaptors: the role of lck, zap-70 and lat in switch panel governing t-cell development and activation. Biology, 12:1163, Aug 2023. URL: https://doi.org/10.3390/biology12091163, doi:10.3390/biology12091163. This article has 65 citations.

7. (anto2023cyclophilinaassociates pages 1-2): Nikhil Ponnoor Anto, Awadhesh Kumar Arya, Amitha Muraleedharan, Jakeer Shaik, Pulak Ranjan Nath, Etta Livneh, Zuoming Sun, Alex Braiman, and Noah Isakov. Cyclophilin a associates with and regulates the activity of zap70 in tcr/cd3-stimulated t cells. Dec 2023. URL: https://doi.org/10.1007/s00018-022-04657-9, doi:10.1007/s00018-022-04657-9. This article has 19 citations and is from a domain leading peer-reviewed journal.

8. (gangopadhyay2021anevolutionarydivergent pages 13-17): Kaustav Gangopadhyay, Arnab Roy, Athira C. Chandradasan, Swarnendu Roy, Olivia Debnath, Soumee SenGupta, Subhankar Chowdhury, Dipjyoti Das, and Rahul Das. An evolutionary divergent thermodynamic brake in zap-70 fine-tunes the kinetic proofreading in t cell. BioRxiv, Nov 2021. URL: https://doi.org/10.1101/2021.11.09.467998, doi:10.1101/2021.11.09.467998. This article has 1 citations.

9. (anto2023cyclophilinaassociates pages 2-4): Nikhil Ponnoor Anto, Awadhesh Kumar Arya, Amitha Muraleedharan, Jakeer Shaik, Pulak Ranjan Nath, Etta Livneh, Zuoming Sun, Alex Braiman, and Noah Isakov. Cyclophilin a associates with and regulates the activity of zap70 in tcr/cd3-stimulated t cells. Dec 2023. URL: https://doi.org/10.1007/s00018-022-04657-9, doi:10.1007/s00018-022-04657-9. This article has 19 citations and is from a domain leading peer-reviewed journal.

10. (fernandezaguilar2023astoryof pages 14-16): Luis M. Fernández-Aguilar, Inmaculada Vico-Barranco, Mikel M. Arbulo-Echevarria, and Enrique Aguado. A story of kinases and adaptors: the role of lck, zap-70 and lat in switch panel governing t-cell development and activation. Biology, 12:1163, Aug 2023. URL: https://doi.org/10.3390/biology12091163, doi:10.3390/biology12091163. This article has 65 citations.

11. (ashouri2022zap70toolittle pages 3-5): Judith F. Ashouri, Wan‐Lin Lo, Trang T. T. Nguyen, Lin Shen, and Arthur Weiss. Zap70, too little, too much can lead to autoimmunity. Immunological Reviews, 307:145-160, Dec 2022. URL: https://doi.org/10.1111/imr.13058, doi:10.1111/imr.13058. This article has 55 citations and is from a domain leading peer-reviewed journal.

12. (anto2023cyclophilinaassociates pages 12-14): Nikhil Ponnoor Anto, Awadhesh Kumar Arya, Amitha Muraleedharan, Jakeer Shaik, Pulak Ranjan Nath, Etta Livneh, Zuoming Sun, Alex Braiman, and Noah Isakov. Cyclophilin a associates with and regulates the activity of zap70 in tcr/cd3-stimulated t cells. Dec 2023. URL: https://doi.org/10.1007/s00018-022-04657-9, doi:10.1007/s00018-022-04657-9. This article has 19 citations and is from a domain leading peer-reviewed journal.

13. (anto2023cyclophilinaassociates pages 4-7): Nikhil Ponnoor Anto, Awadhesh Kumar Arya, Amitha Muraleedharan, Jakeer Shaik, Pulak Ranjan Nath, Etta Livneh, Zuoming Sun, Alex Braiman, and Noah Isakov. Cyclophilin a associates with and regulates the activity of zap70 in tcr/cd3-stimulated t cells. Dec 2023. URL: https://doi.org/10.1007/s00018-022-04657-9, doi:10.1007/s00018-022-04657-9. This article has 19 citations and is from a domain leading peer-reviewed journal.

14. (gangopadhyay2021anevolutionarydivergent pages 1-5): Kaustav Gangopadhyay, Arnab Roy, Athira C. Chandradasan, Swarnendu Roy, Olivia Debnath, Soumee SenGupta, Subhankar Chowdhury, Dipjyoti Das, and Rahul Das. An evolutionary divergent thermodynamic brake in zap-70 fine-tunes the kinetic proofreading in t cell. BioRxiv, Nov 2021. URL: https://doi.org/10.1101/2021.11.09.467998, doi:10.1101/2021.11.09.467998. This article has 1 citations.

15. (schultz2022acysteineresidue pages 7-10): Annika Schultz, Marvin Schnurra, Ali El-Bizri, Nadine M. Woessner, Sara Hartmann, Roland Hartig, Susana Minguet, Burkhart Schraven, and Luca Simeoni. A cysteine residue within the kinase domain of zap70 regulates lck activity and proximal tcr signaling. Cells, 11:2723, Sep 2022. URL: https://doi.org/10.3390/cells11172723, doi:10.3390/cells11172723. This article has 21 citations.

16. (goyette2020regulatedunbindingof pages 1-3): Jesse Goyette, David Depoil, Zhengmin Yang, Samuel A. Isaacson, Jun Allard, P. Anton van der Merwe, Katharina Gaus, Michael L Dustin, and Omer Dushek. Regulated unbinding of zap70 at the t cell receptor by kinetic avidity. bioRxiv, Feb 2020. URL: https://doi.org/10.1101/2020.02.12.945170, doi:10.1101/2020.02.12.945170. This article has 7 citations.

17. (goyette2020regulatedunbindingof pages 3-4): Jesse Goyette, David Depoil, Zhengmin Yang, Samuel A. Isaacson, Jun Allard, P. Anton van der Merwe, Katharina Gaus, Michael L Dustin, and Omer Dushek. Regulated unbinding of zap70 at the t cell receptor by kinetic avidity. bioRxiv, Feb 2020. URL: https://doi.org/10.1101/2020.02.12.945170, doi:10.1101/2020.02.12.945170. This article has 7 citations.

18. (goyette2020regulatedunbindingof pages 21-23): Jesse Goyette, David Depoil, Zhengmin Yang, Samuel A. Isaacson, Jun Allard, P. Anton van der Merwe, Katharina Gaus, Michael L Dustin, and Omer Dushek. Regulated unbinding of zap70 at the t cell receptor by kinetic avidity. bioRxiv, Feb 2020. URL: https://doi.org/10.1101/2020.02.12.945170, doi:10.1101/2020.02.12.945170. This article has 7 citations.

19. (chen2024zap70augmentstonic pages 7-8): Jingyu Chen, Vijitha Sathiaseelan, Chandra Sekkar Reddy Chilamakuri, Valar Nila Roamio Franklin, Constanze A. Jakwerth, Clive D’Santos, and Ingo Ringshausen. Zap-70 augments tonic b-cell receptor and ccr7 signaling in <i>ighv–</i> unmutated chronic lymphocytic leukemia. Blood Advances, 8(5):1167-1178, Mar 2024. URL: https://doi.org/10.1182/bloodadvances.2022009557, doi:10.1182/bloodadvances.2022009557. This article has 13 citations and is from a peer-reviewed journal.

20. (chen2024zap70augmentstonic pages 4-5): Jingyu Chen, Vijitha Sathiaseelan, Chandra Sekkar Reddy Chilamakuri, Valar Nila Roamio Franklin, Constanze A. Jakwerth, Clive D’Santos, and Ingo Ringshausen. Zap-70 augments tonic b-cell receptor and ccr7 signaling in <i>ighv–</i> unmutated chronic lymphocytic leukemia. Blood Advances, 8(5):1167-1178, Mar 2024. URL: https://doi.org/10.1182/bloodadvances.2022009557, doi:10.1182/bloodadvances.2022009557. This article has 13 citations and is from a peer-reviewed journal.

21. (mongellaz2023combinedimmunodeficiencycaused pages 13-13): Cédric Mongellaz, Rita Vicente, Lenora M. Noroski, Nelly Noraz, Valérie Courgnaud, Javier Chinen, Emilia Faria, Valérie S. Zimmermann, and Naomi Taylor. Combined immunodeficiency caused by pathogenic variants in the zap70 c-terminal sh2 domain. Frontiers in Immunology, May 2023. URL: https://doi.org/10.3389/fimmu.2023.1155883, doi:10.3389/fimmu.2023.1155883. This article has 11 citations and is from a peer-reviewed journal.

22. (mongellaz2023combinedimmunodeficiencycaused pages 12-13): Cédric Mongellaz, Rita Vicente, Lenora M. Noroski, Nelly Noraz, Valérie Courgnaud, Javier Chinen, Emilia Faria, Valérie S. Zimmermann, and Naomi Taylor. Combined immunodeficiency caused by pathogenic variants in the zap70 c-terminal sh2 domain. Frontiers in Immunology, May 2023. URL: https://doi.org/10.3389/fimmu.2023.1155883, doi:10.3389/fimmu.2023.1155883. This article has 11 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](ZAP70-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](ZAP70-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](ZAP70-deep-research-falcon_artifacts/artifact-02.md)

## Citations

1. fernandezaguilar2023astoryof pages 5-7
2. gangopadhyay2020anallosterichot pages 1-4
3. anto2023cyclophilinaassociates pages 1-2
4. aktas2024chroniclymphocyticleukemia pages 114-117
5. hobbs2021differencesinthe pages 1-3
6. fernandezaguilar2023astoryof pages 7-9
7. gangopadhyay2021anevolutionarydivergent pages 13-17
8. anto2023cyclophilinaassociates pages 2-4
9. fernandezaguilar2023astoryof pages 14-16
10. anto2023cyclophilinaassociates pages 12-14
11. anto2023cyclophilinaassociates pages 4-7
12. gangopadhyay2021anevolutionarydivergent pages 1-5
13. schultz2022acysteineresidue pages 7-10
14. goyette2020regulatedunbindingof pages 1-3
15. goyette2020regulatedunbindingof pages 3-4
16. goyette2020regulatedunbindingof pages 21-23
17. mongellaz2023combinedimmunodeficiencycaused pages 13-13
18. mongellaz2023combinedimmunodeficiencycaused pages 12-13
19. https://doi.org/10.3390/biology12091163,
20. https://doi.org/10.26650/b/ls17ls30.2025.006,
21. https://doi.org/10.1002/pro.4199,
22. https://doi.org/10.1101/842534,
23. https://doi.org/10.1111/imr.13058,
24. https://doi.org/10.1007/s00018-022-04657-9,
25. https://doi.org/10.1101/2021.11.09.467998,
26. https://doi.org/10.3390/cells11172723,
27. https://doi.org/10.1101/2020.02.12.945170,
28. https://doi.org/10.1182/bloodadvances.2022009557,
29. https://doi.org/10.3389/fimmu.2023.1155883,