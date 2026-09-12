---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-04T20:09:32.119944'
end_time: '2026-07-04T20:28:12.708027'
duration_seconds: 1120.59
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: worm
  gene_id: mksr-1
  gene_symbol: mksr-1
  uniprot_accession: Q21191
  protein_description: 'RecName: Full=B9 domain-containing protein 1 {ECO:0000256|ARBA:ARBA00039274};'
  gene_info: Name=mksr-1 {ECO:0000313|EMBL:CCD62862.1, ECO:0000313|WormBase:K03E6.4};
    ORFNames=CELE_K03E6.4 {ECO:0000313|EMBL:CCD62862.1}, K03E6.4 {ECO:0000313|WormBase:K03E6.4};
  organism_full: Caenorhabditis elegans.
  protein_family: Belongs to the B9D family. .
  protein_domains: C2_B9-type_dom. (IPR010796); B9-C2 (PF07162)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 32
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: mksr-1-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: mksr-1-deep-research-falcon_artifacts/artifact-01.md
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
- **UniProt Accession:** Q21191
- **Protein Description:** RecName: Full=B9 domain-containing protein 1 {ECO:0000256|ARBA:ARBA00039274};
- **Gene Information:** Name=mksr-1 {ECO:0000313|EMBL:CCD62862.1, ECO:0000313|WormBase:K03E6.4}; ORFNames=CELE_K03E6.4 {ECO:0000313|EMBL:CCD62862.1}, K03E6.4 {ECO:0000313|WormBase:K03E6.4};
- **Organism (full):** Caenorhabditis elegans.
- **Protein Family:** Belongs to the B9D family. .
- **Key Domains:** C2_B9-type_dom. (IPR010796); B9-C2 (PF07162)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "mksr-1" matches the protein description above**
2. **Verify the organism is correct:** Caenorhabditis elegans.
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'mksr-1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **mksr-1** (gene ID: mksr-1, UniProt: Q21191) in worm.

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
- **UniProt Accession:** Q21191
- **Protein Description:** RecName: Full=B9 domain-containing protein 1 {ECO:0000256|ARBA:ARBA00039274};
- **Gene Information:** Name=mksr-1 {ECO:0000313|EMBL:CCD62862.1, ECO:0000313|WormBase:K03E6.4}; ORFNames=CELE_K03E6.4 {ECO:0000313|EMBL:CCD62862.1}, K03E6.4 {ECO:0000313|WormBase:K03E6.4};
- **Organism (full):** Caenorhabditis elegans.
- **Protein Family:** Belongs to the B9D family. .
- **Key Domains:** C2_B9-type_dom. (IPR010796); B9-C2 (PF07162)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "mksr-1" matches the protein description above**
2. **Verify the organism is correct:** Caenorhabditis elegans.
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'mksr-1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **mksr-1** (gene ID: mksr-1, UniProt: Q21191) in worm.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Comprehensive Research Report: *mksr-1* (B9 Domain-Containing Protein 1) in *Caenorhabditis elegans*

## 1. Gene and Protein Identity

The gene *mksr-1* (MKS1-Related, also designated K03E6.4) encodes a B9 domain-containing protein 1 (UniProt: Q21191) in *Caenorhabditis elegans*. The name "MKSR" stands for Meckel Syndrome 1-Related, reflecting its evolutionary and functional relationship to the ciliopathy-associated protein MKS1. MKSR-1 is the *C. elegans* ortholog of mammalian B9D1 (also known as MKS9), a soluble protein containing a single B9 domain that spans nearly the entire length of the protein (bialas2009functionalinteractionsbetween pages 5-6, okazaki2020formationofthe pages 5-7). MKSR-1 belongs to a small family of three B9 domain-containing proteins—MKS-1, MKSR-1, and MKSR-2 (ortholog of B9D2)—that are evolutionarily conserved across ciliated organisms and always co-occur in the proteome, suggesting they function as an obligate complex (zhang2010identificationofnovel pages 8-9, bialas2009functionalinteractionsbetween pages 5-6).

The following table summarizes the key molecular and functional properties of MKSR-1/B9D1:

| Property | Summary |
|---|---|
| Gene / protein name | **C. elegans:** **mksr-1** (MKSR-1), UniProt Q21191, annotated as **B9 domain-containing protein 1**; **human ortholog:** **B9D1** (also called MKS9 in some literature) (bialas2009functionalinteractionsbetween pages 5-6, li2016mks5andcep290 pages 9-11, okazaki2020formationofthe pages 1-5) |
| Protein family / domain | Member of the **B9 domain protein family**; contains a **B9-C2 / C2_B9-type domain**, a specialized C2-domain family associated with ciliary proteins and inferred membrane/lipid interaction functions (zhang2010identificationofnovel pages 8-9, zhang2010identificationofnovel pages 5-6, okazaki2020formationofthe pages 1-5) |
| Subcellular localization | Localizes specifically to the **ciliary transition zone (TZ)** at the base of **sensory cilia** in *C. elegans* amphid and phasmid neurons; mammalian B9D1 is also a TZ protein (bialas2009functionalinteractionsbetween pages 5-6, li2016mks5andcep290 pages 9-11, bialas2009functionalinteractionsbetween pages 3-5) |
| Molecular complex | Core component of the **MKS/B9 transition-zone complex**; in vertebrates the B9 subcomplex is organized as **MKS1–B9D2–B9D1**, with B9D2 bridging MKS1 and B9D1 (okazaki2020formationofthe pages 1-5, okazaki2020formationofthe pages 5-7, okazaki2020formationofthe pages 21-27) |
| Functional role | Functions in **ciliary gate / diffusion barrier** activity at the TZ, helping maintain selective ciliary membrane protein composition and compartmentalization rather than acting as a classical enzyme or transporter; broadly supports TZ organization and ciliary signaling homeostasis (okazaki2020formationofthe pages 1-5, jensen2015formationofthe pages 14-15, jensen2015formationofthe pages 12-14) |
| Genetic / pathway module | Belongs to the **MKS module** of TZ proteins; specifically behaves as a **core MKS module protein** in the hierarchical assembly pathway downstream of **MKS-5/RPGRIP1L** and **CEP-290**, and is genetically separable from the **NPHP module** while functionally redundant with it during ciliogenesis/barrier formation (li2016mks5andcep290 pages 18-20, li2016mks5andcep290 pages 9-11, li2016mks5andcep290 pages 16-18, li2016mks5andcep290 pages 3-5) |
| Key interacting partners | Strongly linked with **MKSR-2/B9D2** and **MKS-1** through interdependent localization in worms; mammalian interaction mapping supports a linear **MKS1–B9D2–B9D1** arrangement. As a core MKS protein, its proper TZ localization also depends on **CEP-290** and upstream **MKS-5**-dependent assembly. Core/peripheral MKS relationships place it functionally alongside **MKS-2/TMEM216**, **TMEM-231**, **TMEM-17**, **TMEM-67**, **TMEM-218**, and **TMEM-237** (bialas2009functionalinteractionsbetween pages 5-6, okazaki2020formationofthe pages 5-7, li2016mks5andcep290 pages 18-20, li2016mks5andcep290 pages 9-11, li2016mks5andcep290 pages 16-18) |
| Single-mutant phenotype in *C. elegans* | **mksr-1 single mutants** are generally **non-Dyf** (no obvious dye-filling defect) and do not show major defects in gross ciliogenesis, intraflagellar transport, or chemosensation, indicating MKSR-1 is not absolutely required for basal cilium assembly on its own (bialas2009functionalinteractionsbetween pages 1-2, bialas2009functionalinteractionsbetween pages 6-7, bialas2009functionalinteractionsbetween pages 7-9, warburtonpitt2012ciliogenesisincaenorhabditis pages 3-4) |
| Double-mutant / synthetic phenotype | Stronger phenotypes emerge in combination with other TZ genes. **MKS/NPHP double mutants** reveal redundant function in ciliogenesis and membrane anchoring, with synthetic defects including **dye-filling defects**, **loss of TZ ultrastructure/Y-links**, **axoneme malformations**, **cilium shortening**, and **TZ displacement**. Genetic interactions are especially evident with **nphp-1**, **nphp-4**, and sensillum-specific interactions with **nphp-2** (jensen2015formationofthe pages 1-2, li2016mks5andcep290 pages 18-20, jensen2015formationofthe pages 14-15, bialas2009functionalinteractionsbetween pages 7-9, warburtonpitt2012ciliogenesisincaenorhabditis pages 4-6, warburtonpitt2015theciliopathygene pages 95-99) |
| Assembly-dependence / localization dependencies | MKSR-1 localization is **interdependent** with other core MKS proteins and is disrupted when **MKSR-2**, **MKS-1**, or **CEP-290** are absent; **MKS-5** acts further upstream as a foundational TZ assembly factor (bialas2009functionalinteractionsbetween pages 5-6, li2016mks5andcep290 pages 18-20, li2016mks5andcep290 pages 9-11, li2016mks5andcep290 pages 16-18, li2016mks5andcep290 pages 3-5) |
| Human disease associations of ortholog | **B9D1** is associated with **Meckel syndrome / Meckel syndrome type 9** and **Joubert syndrome / Joubert syndrome 27** in human disease databases and primary literature (OpenTargets Search: -B9D1) |


*Table: This table summarizes the main molecular, cellular, genetic, and disease-related properties of C. elegans MKSR-1 and its human ortholog B9D1. It is useful as a compact reference linking transition-zone localization, MKS-module function, mutant phenotypes, and ciliopathy associations.*

## 2. Structural and Domain Features

MKSR-1 contains a single **B9 domain** (IPR010796; PF07162), which is classified as a specialized member of the **C2 domain superfamily** based on profile-profile comparisons and fold recognition analyses (zhang2010identificationofnovel pages 8-9, zhang2010identificationofnovel pages 5-6). C2 domains are typically β-sandwich structures that mediate calcium-dependent or calcium-independent membrane binding through interactions with phospholipids. The B9-type C2 domain, however, represents a distinct evolutionary branch: it occurs as a standalone domain (i.e., not fused with other functional domains) and contains conserved hydrophobic residues on its β-sheet that create a concave ligand-binding surface, consistent with lipid interaction capability (zhang2010identificationofnovel pages 8-9). Structural analyses of related ciliary C2 domains indicate that B9 domains are not expected to bind Ca²⁺ and instead may function primarily as protein-protein interaction modules within the transition zone (zhang2010identificationofnovel pages 8-9).

Studies on the related B9 domain protein B9D2 have demonstrated strong binding affinity to specific phosphoinositides, including PI4P and PI(3,4,5)P3, with lesser binding to PI(4,5)P2 (caenenbraz2024newfunctionsof pages 8-10). Given the high structural similarity within the B9 family, MKSR-1's B9 domain is inferred to possess analogous lipid-interaction properties, which may facilitate its anchoring to specific membrane microdomains at the ciliary transition zone.

## 3. Primary Function: Structural Component of the Ciliary Transition Zone Gate

MKSR-1 is **not an enzyme, transporter, or classical signaling molecule**. Rather, it functions as a **structural/adapter protein** within the ciliary transition zone (TZ), where it serves as a core component of the **MKS (Meckel syndrome) module**—a multiprotein complex that constitutes part of the **ciliary diffusion barrier or "gate"** (jensen2015formationofthe pages 1-2, okazaki2020formationofthe pages 1-5).

### 3.1 The Transition Zone as a Ciliary Gate

The transition zone is a specialized ~0.8 μm region at the base of the cilium, located between the basal body and the axoneme proper. It contains characteristic Y-shaped linkers that connect the axonemal microtubule doublets to the ciliary membrane and functions as a selective barrier controlling which proteins and lipids can enter or exit the ciliary compartment (jensen2015formationofthe pages 14-15, jensen2015formationofthe pages 1-2, jensen2015formationofthe pages 2-4). This barrier is essential for maintaining the unique protein and lipid composition of cilia, which is required for their sensory and signaling functions.

### 3.2 The B9 Protein Complex as a Diffusion Barrier

In mammalian cells, the three B9 domain proteins form a linear tripartite complex with the interaction mode **MKS1–B9D2–B9D1**, where B9D2 serves as a bridge between MKS1 and B9D1, as demonstrated by visible immunoprecipitation and three-hybrid assays (okazaki2020formationofthe pages 5-7, okazaki2020formationofthe pages 21-27). MKS1 and B9D1 do not directly interact with each other (okazaki2020formationofthe pages 5-7). The formation of this complex is essential for creating a functional diffusion barrier for ciliary membrane proteins: loss of MKS1 or B9D2 results in failure of transmembrane proteins (such as GPCRs GPR161 and Smoothened) and lipidated membrane proteins (ARL13B, INPP5E) to properly localize to the ciliary membrane (okazaki2020formationofthe pages 5-7, okazaki2020formationofthe pages 21-27). Importantly, the B9 proteins are involved in, but not absolutely essential for, normal cilia biogenesis; rather, their complex formation is specifically crucial for the barrier/gating function (okazaki2020formationofthe pages 1-5).

### 3.3 Recent Advances: B9 Complex Interactions with TMEM67 and Microtubule Modifications

Recent work has revealed additional functions of the B9 complex beyond its role as a passive diffusion barrier. The B9D1-B9D2-MKS1 complex interacts with and anchors the transmembrane protein TMEM67 to the TZ membrane. Disruption of this B9-TMEM67 complex reduces posttranslational modifications (acetylation and polyglutamylation) of axonemal microtubules due to deregulation of tubulin-modifying enzymes within cilia (he2026ciliopathyrelatedb9protein pages 1-2, he2026ciliopathyrelatedb9protein pages 4-5). Furthermore, B9 proteins have been found to localize to centrioles prior to ciliogenesis, where they facilitate initiation of ciliary assembly by promoting membrane vesicle docking to distal appendages and CP110 removal from the mother centriole (he2026ciliopathyrelatedb9protein pages 2-4, he2026ciliopathyrelatedb9protein pages 1-2).

## 4. Subcellular Localization

In *C. elegans*, MKSR-1 localizes specifically to the **transition zone at the base of sensory cilia** in ciliated neurons. Fluorescent reporter studies have demonstrated MKSR-1 localization at transition zones of amphid cilia near the head and phasmid cilia near the tail (bialas2009functionalinteractionsbetween pages 3-5, bialas2009functionalinteractionsbetween pages 5-6). This localization pattern is shared with MKS-1 and MKSR-2, and the three B9 proteins show **co-dependent localization**: when any one is mutated, the other two show reduced or mislocalized signals at transition zones, with abnormal accumulations in dendrites (bialas2009functionalinteractionsbetween pages 5-6, bialas2009functionalinteractionsbetween pages 6-7). MKSR-1 localization also depends on CEP-290 and MKS-5, the upstream assembly factors of the TZ (li2016mks5andcep290 pages 9-11).

## 5. Transition Zone Assembly Hierarchy and Module Architecture

The ciliary TZ in *C. elegans* assembles through a well-characterized hierarchical pathway. MKSR-1 occupies a defined position within this hierarchy as a **core MKS module protein**:

| Level in hierarchy | Protein(s) | Module assignment | Dependence (what it requires for TZ localization) | Role in TZ |
|---|---|---|---|---|
| 1 (most upstream) | MKS-5 / RPGRIP1L | Master TZ assembly factor / scaffold linking MKS and NPHP branches | Localizes independently of CEP-290; required for localization of essentially all tested TZ proteins, including CEP-290, MKS-module, and NPHP-module proteins (li2016mks5andcep290 pages 9-11, li2016mks5andcep290 pages 3-5, jensen2015formationofthe pages 1-2, jensen2015formationofthe pages 8-9) | Foundational organizer of TZ formation; establishes TZ ultrastructure, supports Y-link formation, and helps create the ciliary zone of exclusion/barrier (li2016mks5andcep290 pages 3-5, jensen2015formationofthe pages 1-2, jensen2015formationofthe pages 7-8, jensen2015formationofthe pages 4-5) |
| 2A | NPHP-1, NPHP-4 | NPHP module | Assemble in the MKS-5-dependent branch; localization does not require CEP-290 (li2016mks5andcep290 pages 11-12, li2016mks5andcep290 pages 16-18, li2016mks5andcep290 pages 3-5) | Parallel TZ branch that works redundantly with the MKS branch to seal the ciliary compartment, maintain membrane attachments, and support ciliogenesis/barrier function (li2016mks5andcep290 pages 16-18, jensen2015formationofthe pages 1-2, jensen2015formationofthe pages 7-8, jensen2015formationofthe pages 2-4) |
| 2B | CEP-290 | CEP-290-dependent MKS assembly branch | Requires MKS-5 for TZ localization; acts downstream of MKS-5 and upstream of MKS-module proteins (li2016mks5andcep290 pages 9-11, li2016mks5andcep290 pages 11-12, li2016mks5andcep290 pages 16-18, li2016mks5andcep290 pages 3-5) | Core assembly factor for the MKS pathway; required for Y-links/apical ring integrity and ciliary gate function, and specifically recruits/organizes MKS-module proteins at the TZ (li2016mks5andcep290 pages 18-20, li2016mks5andcep290 pages 9-11, li2016mks5andcep290 pages 11-12) |
| 3 (core MKS layer) | MKS-1, MKSR-1/B9D1, MKSR-2/B9D2, MKS-2/TMEM216, TMEM-231 | Core MKS module | Require CEP-290 and MKS-5 for TZ localization; core members are interdependent with one another for proper localization (li2016mks5andcep290 pages 18-20, li2016mks5andcep290 pages 9-11, li2016mks5andcep290 pages 16-18, li2016mks5andcep290 pages 7-9) | Principal MKS gate components; organize the membrane-proximal barrier, support TZ ultrastructure, and are necessary for proper ciliary compartmentalization/gate function (li2016mks5andcep290 pages 18-20, li2016mks5andcep290 pages 16-18, jensen2015formationofthe pages 14-15, jensen2015formationofthe pages 2-4) |
| 4 (peripheral MKS layer) | TMEM-17, TMEM-67, TMEM-218, TMEM-237 | Peripheral MKS module | Require CEP-290, MKS-5, and intact core MKS proteins for TZ localization; do not control localization of core MKS proteins (li2016mks5andcep290 pages 18-20, li2016mks5andcep290 pages 16-18, li2016mks5andcep290 pages 7-9) | Downstream effectors/accessory MKS components that elaborate TZ composition and contribute to mature gate/barrier function rather than initiating core assembly (li2016mks5andcep290 pages 18-20, li2016mks5andcep290 pages 16-18, jensen2015formationofthe pages 2-4) |


*Table: This table summarizes the hierarchical assembly of the C. elegans ciliary transition zone, placing MKSR-1/B9D1 within the CEP-290-dependent core MKS module. It is useful for understanding which proteins act upstream versus downstream in building the transition-zone barrier.*

**MKS-5/RPGRIP1L** serves as the foundational scaffold, localizing independently of all other TZ proteins and being required for localization of essentially all known TZ components (li2016mks5andcep290 pages 3-5, jensen2015formationofthe pages 1-2, jensen2015formationofthe pages 7-8). Downstream of MKS-5, the pathway bifurcates into two genetically separable branches: the **NPHP module** (NPHP-1, NPHP-4) and the **CEP-290-dependent MKS module** (li2016mks5andcep290 pages 11-12, li2016mks5andcep290 pages 16-18). CEP-290 requires MKS-5 for its own TZ localization and is in turn required for proper localization of all MKS module components, including MKSR-1 (li2016mks5andcep290 pages 9-11, li2016mks5andcep290 pages 3-5).

Within the MKS module, MKSR-1 is classified as a **core component**, along with MKS-1, MKSR-2, MKS-2/TMEM216, and TMEM-231. These core proteins show interdependent localization—removal of any one disrupts TZ localization of the others (li2016mks5andcep290 pages 18-20, li2016mks5andcep290 pages 16-18). Peripheral MKS module proteins (TMEM-17, TMEM-67, TMEM-218, TMEM-237) depend on the core proteins for their TZ localization but do not influence core protein assembly (li2016mks5andcep290 pages 18-20, li2016mks5andcep290 pages 16-18).

## 6. Genetic Interactions and Functional Redundancy

A hallmark of MKSR-1 function is its **genetic redundancy with NPHP module proteins**. Single *mksr-1* mutants (*ok2092*) are **non-Dyf** (no dye-filling defect) and display no overt defects in cilium formation, intraflagellar transport (IFT), or chemosensory behaviors (bialas2009functionalinteractionsbetween pages 1-2, bialas2009functionalinteractionsbetween pages 6-7, warburtonpitt2012ciliogenesisincaenorhabditis pages 3-4). However, when *mksr-1* mutations are combined with mutations in NPHP module genes (*nphp-1* or *nphp-4*), severe **synthetic phenotypes** emerge, including dye-filling defects, loss of basal body-TZ membrane anchoring, disruption of TZ ultrastructure and Y-links, and axoneme malformations (jensen2015formationofthe pages 1-2, bialas2009functionalinteractionsbetween pages 7-9, warburtonpitt2012ciliogenesisincaenorhabditis pages 4-6). These synthetic interactions define the genetic separability of the MKS and NPHP modules while demonstrating their functional redundancy in establishing the ciliary gate.

Additionally, *nphp-2;mksr-1* double mutants exhibit sensillum-specific dye-filling defects and abnormal TZ spread in amphid neurons, as well as shortened phasmid dendritic length indicative of TZ displacement (warburtonpitt2012ciliogenesisincaenorhabditis pages 4-6, warburtonpitt2015theciliopathygene pages 95-99).

## 7. Role in Ciliary Signaling and the Ciliary Zone of Exclusion (CIZE)

The TZ, to which MKSR-1 localizes, establishes a **ciliary zone of exclusion (CIZE)** that compartmentalizes signaling proteins and controls phosphoinositide abundance within the cilium (jensen2015formationofthe pages 14-15, jensen2015formationofthe pages 1-2, jensen2015formationofthe pages 12-14). The CIZE model, developed primarily from *C. elegans* studies, demonstrates that PIP2 is highly concentrated at the periciliary membrane but is excluded from the distal ciliary compartment in an MKS-5-dependent manner (jensen2015formationofthe pages 14-15, jensen2015formationofthe pages 12-14). The TZ barrier also prevents inappropriate entry of non-ciliary membrane proteins and retains ciliary residents like ARL-13 within the cilium (jensen2015formationofthe pages 12-14).

While MKSR-1 single mutants do not show gross signaling defects, double mutant analysis with other B9 family members (*mksr-1;mksr-2*) revealed increased lifespan, suggesting MKSR-1 functions upstream of the **DAF-2/DAF-16 insulin-IGF-I signaling pathway** to regulate longevity specification, likely through its role in cilia-dependent sensory signaling (bialas2009functionalinteractionsbetween pages 9-10, bialas2009functionalinteractionsbetween pages 10-11).

## 8. Evolutionary Conservation and Disease Relevance

The B9 protein family is highly conserved across ciliated eukaryotes. Phylogenetic analysis shows that all three B9 domain proteins (MKS1, B9D1/MKSR-1, B9D2/MKSR-2) strictly co-occur in organisms that possess cilia and are independently lost in non-ciliated lineages such as land plants, amoebozoans, and dikaryan fungi (zhang2010identificationofnovel pages 8-9, bialas2009functionalinteractionsbetween pages 5-6).

The human ortholog **B9D1** is a causative gene for **Meckel syndrome type 9** (MKS9), a severe autosomal recessive lethal ciliopathy characterized by occipital encephalocele, cystic kidneys, and polydactyly (OpenTargets Search: -B9D1). B9D1 mutations have also been identified in patients with **Joubert syndrome 27** (JBTS27), a milder ciliopathy characterized by the "molar tooth sign" cerebellar malformation (OpenTargets Search: -B9D1). This spectrum of disease severity from the same gene—ranging from lethal MKS to mild JBTS—reflects the functional complexity of the B9 complex in maintaining ciliary gate function across different tissues and developmental contexts.

## 9. Summary

MKSR-1 (B9D1) is a non-enzymatic, non-transporter structural/adapter protein that functions as a core component of the ciliary transition zone diffusion barrier in *C. elegans*. Its primary role is to form part of the B9 protein complex (MKS1–MKSR-2–MKSR-1), which is essential for maintaining selective ciliary membrane composition by preventing non-selective diffusion of proteins and lipids across the transition zone. MKSR-1 localizes specifically to the transition zone of sensory cilia, where it participates in the MKS module—a multiprotein assembly that works redundantly with the NPHP module to establish the ciliary gate. The protein assembles hierarchically downstream of MKS-5 and CEP-290, and its localization is interdependent with other core MKS components. Through its role in ciliary compartmentalization, MKSR-1 indirectly supports multiple signaling pathways that depend on proper ciliary function, including insulin-IGF signaling and sensory perception. Mutations in the human ortholog B9D1 cause the ciliopathies Meckel syndrome and Joubert syndrome, underscoring the critical importance of this protein in ciliary biology.

References

1. (bialas2009functionalinteractionsbetween pages 5-6): Nathan J. Bialas, Peter N. Inglis, Chunmei Li, Jon F. Robinson, Jeremy D. K. Parker, Michael P. Healey, Erica E. Davis, Chrystal D. Inglis, Tiina Toivonen, David C. Cottell, Oliver E. Blacque, Lynne M. Quarmby, Nicholas Katsanis, and Michel R. Leroux. Functional interactions between the ciliopathy-associated meckel syndrome 1 (mks1) protein and two novel mks1-related (mksr) proteins. Journal of Cell Science, 122:611-624, Mar 2009. URL: https://doi.org/10.1242/jcs.028621, doi:10.1242/jcs.028621. This article has 98 citations and is from a domain leading peer-reviewed journal.

2. (okazaki2020formationofthe pages 5-7): Misato Okazaki, Takuya Kobayashi, Shuhei Chiba, Ryota Takei, Luxiaoxue Liang, Kazuhisa Nakayama, and Yohei Katoh. Formation of the b9-domain protein complex mks1–b9d2–b9d1 is essential as a diffusion barrier for ciliary membrane proteins. Molecular Biology of the Cell, 31:2259-2268, Sep 2020. URL: https://doi.org/10.1091/mbc.e20-03-0208, doi:10.1091/mbc.e20-03-0208. This article has 32 citations and is from a domain leading peer-reviewed journal.

3. (zhang2010identificationofnovel pages 8-9): Dapeng Zhang and L. Aravind. Identification of novel families and classification of the c2 domain superfamily elucidate the origin and evolution of membrane targeting activities in eukaryotes. Gene, 469 1-2:18-30, Dec 2010. URL: https://doi.org/10.1016/j.gene.2010.08.006, doi:10.1016/j.gene.2010.08.006. This article has 169 citations and is from a peer-reviewed journal.

4. (li2016mks5andcep290 pages 9-11): Chunmei Li, Victor L. Jensen, Kwangjin Park, Julie Kennedy, Francesc R. Garcia-Gonzalo, Marta Romani, Roberta De Mori, Ange-Line Bruel, Dominique Gaillard, Bérénice Doray, Estelle Lopez, Jean-Baptiste Rivière, Laurence Faivre, Christel Thauvin-Robinet, Jeremy F. Reiter, Oliver E. Blacque, Enza Maria Valente, and Michel R. Leroux. Mks5 and cep290 dependent assembly pathway of the ciliary transition zone. PLOS Biology, 14:e1002416, Mar 2016. URL: https://doi.org/10.1371/journal.pbio.1002416, doi:10.1371/journal.pbio.1002416. This article has 176 citations and is from a highest quality peer-reviewed journal.

5. (okazaki2020formationofthe pages 1-5): Misato Okazaki, Takuya Kobayashi, Shuhei Chiba, Ryota Takei, Luxiaoxue Liang, Kazuhisa Nakayama, and Yohei Katoh. Formation of the b9-domain protein complex mks1–b9d2–b9d1 is essential as a diffusion barrier for ciliary membrane proteins. Molecular Biology of the Cell, 31:2259-2268, Sep 2020. URL: https://doi.org/10.1091/mbc.e20-03-0208, doi:10.1091/mbc.e20-03-0208. This article has 32 citations and is from a domain leading peer-reviewed journal.

6. (zhang2010identificationofnovel pages 5-6): Dapeng Zhang and L. Aravind. Identification of novel families and classification of the c2 domain superfamily elucidate the origin and evolution of membrane targeting activities in eukaryotes. Gene, 469 1-2:18-30, Dec 2010. URL: https://doi.org/10.1016/j.gene.2010.08.006, doi:10.1016/j.gene.2010.08.006. This article has 169 citations and is from a peer-reviewed journal.

7. (bialas2009functionalinteractionsbetween pages 3-5): Nathan J. Bialas, Peter N. Inglis, Chunmei Li, Jon F. Robinson, Jeremy D. K. Parker, Michael P. Healey, Erica E. Davis, Chrystal D. Inglis, Tiina Toivonen, David C. Cottell, Oliver E. Blacque, Lynne M. Quarmby, Nicholas Katsanis, and Michel R. Leroux. Functional interactions between the ciliopathy-associated meckel syndrome 1 (mks1) protein and two novel mks1-related (mksr) proteins. Journal of Cell Science, 122:611-624, Mar 2009. URL: https://doi.org/10.1242/jcs.028621, doi:10.1242/jcs.028621. This article has 98 citations and is from a domain leading peer-reviewed journal.

8. (okazaki2020formationofthe pages 21-27): Misato Okazaki, Takuya Kobayashi, Shuhei Chiba, Ryota Takei, Luxiaoxue Liang, Kazuhisa Nakayama, and Yohei Katoh. Formation of the b9-domain protein complex mks1–b9d2–b9d1 is essential as a diffusion barrier for ciliary membrane proteins. Molecular Biology of the Cell, 31:2259-2268, Sep 2020. URL: https://doi.org/10.1091/mbc.e20-03-0208, doi:10.1091/mbc.e20-03-0208. This article has 32 citations and is from a domain leading peer-reviewed journal.

9. (jensen2015formationofthe pages 14-15): Victor L Jensen, Chunmei Li, Rachel V Bowie, Lara Clarke, Swetha Mohan, Oliver E Blacque, and Michel R Leroux. Formation of the transition zone by mks5/rpgrip1l establishes a ciliary zone of exclusion (cize) that compartmentalises ciliary signalling proteins and controls pip2 ciliary abundance. The EMBO Journal, 34:2537-2556, Oct 2015. URL: https://doi.org/10.15252/embj.201488044, doi:10.15252/embj.201488044. This article has 164 citations.

10. (jensen2015formationofthe pages 12-14): Victor L Jensen, Chunmei Li, Rachel V Bowie, Lara Clarke, Swetha Mohan, Oliver E Blacque, and Michel R Leroux. Formation of the transition zone by mks5/rpgrip1l establishes a ciliary zone of exclusion (cize) that compartmentalises ciliary signalling proteins and controls pip2 ciliary abundance. The EMBO Journal, 34:2537-2556, Oct 2015. URL: https://doi.org/10.15252/embj.201488044, doi:10.15252/embj.201488044. This article has 164 citations.

11. (li2016mks5andcep290 pages 18-20): Chunmei Li, Victor L. Jensen, Kwangjin Park, Julie Kennedy, Francesc R. Garcia-Gonzalo, Marta Romani, Roberta De Mori, Ange-Line Bruel, Dominique Gaillard, Bérénice Doray, Estelle Lopez, Jean-Baptiste Rivière, Laurence Faivre, Christel Thauvin-Robinet, Jeremy F. Reiter, Oliver E. Blacque, Enza Maria Valente, and Michel R. Leroux. Mks5 and cep290 dependent assembly pathway of the ciliary transition zone. PLOS Biology, 14:e1002416, Mar 2016. URL: https://doi.org/10.1371/journal.pbio.1002416, doi:10.1371/journal.pbio.1002416. This article has 176 citations and is from a highest quality peer-reviewed journal.

12. (li2016mks5andcep290 pages 16-18): Chunmei Li, Victor L. Jensen, Kwangjin Park, Julie Kennedy, Francesc R. Garcia-Gonzalo, Marta Romani, Roberta De Mori, Ange-Line Bruel, Dominique Gaillard, Bérénice Doray, Estelle Lopez, Jean-Baptiste Rivière, Laurence Faivre, Christel Thauvin-Robinet, Jeremy F. Reiter, Oliver E. Blacque, Enza Maria Valente, and Michel R. Leroux. Mks5 and cep290 dependent assembly pathway of the ciliary transition zone. PLOS Biology, 14:e1002416, Mar 2016. URL: https://doi.org/10.1371/journal.pbio.1002416, doi:10.1371/journal.pbio.1002416. This article has 176 citations and is from a highest quality peer-reviewed journal.

13. (li2016mks5andcep290 pages 3-5): Chunmei Li, Victor L. Jensen, Kwangjin Park, Julie Kennedy, Francesc R. Garcia-Gonzalo, Marta Romani, Roberta De Mori, Ange-Line Bruel, Dominique Gaillard, Bérénice Doray, Estelle Lopez, Jean-Baptiste Rivière, Laurence Faivre, Christel Thauvin-Robinet, Jeremy F. Reiter, Oliver E. Blacque, Enza Maria Valente, and Michel R. Leroux. Mks5 and cep290 dependent assembly pathway of the ciliary transition zone. PLOS Biology, 14:e1002416, Mar 2016. URL: https://doi.org/10.1371/journal.pbio.1002416, doi:10.1371/journal.pbio.1002416. This article has 176 citations and is from a highest quality peer-reviewed journal.

14. (bialas2009functionalinteractionsbetween pages 1-2): Nathan J. Bialas, Peter N. Inglis, Chunmei Li, Jon F. Robinson, Jeremy D. K. Parker, Michael P. Healey, Erica E. Davis, Chrystal D. Inglis, Tiina Toivonen, David C. Cottell, Oliver E. Blacque, Lynne M. Quarmby, Nicholas Katsanis, and Michel R. Leroux. Functional interactions between the ciliopathy-associated meckel syndrome 1 (mks1) protein and two novel mks1-related (mksr) proteins. Journal of Cell Science, 122:611-624, Mar 2009. URL: https://doi.org/10.1242/jcs.028621, doi:10.1242/jcs.028621. This article has 98 citations and is from a domain leading peer-reviewed journal.

15. (bialas2009functionalinteractionsbetween pages 6-7): Nathan J. Bialas, Peter N. Inglis, Chunmei Li, Jon F. Robinson, Jeremy D. K. Parker, Michael P. Healey, Erica E. Davis, Chrystal D. Inglis, Tiina Toivonen, David C. Cottell, Oliver E. Blacque, Lynne M. Quarmby, Nicholas Katsanis, and Michel R. Leroux. Functional interactions between the ciliopathy-associated meckel syndrome 1 (mks1) protein and two novel mks1-related (mksr) proteins. Journal of Cell Science, 122:611-624, Mar 2009. URL: https://doi.org/10.1242/jcs.028621, doi:10.1242/jcs.028621. This article has 98 citations and is from a domain leading peer-reviewed journal.

16. (bialas2009functionalinteractionsbetween pages 7-9): Nathan J. Bialas, Peter N. Inglis, Chunmei Li, Jon F. Robinson, Jeremy D. K. Parker, Michael P. Healey, Erica E. Davis, Chrystal D. Inglis, Tiina Toivonen, David C. Cottell, Oliver E. Blacque, Lynne M. Quarmby, Nicholas Katsanis, and Michel R. Leroux. Functional interactions between the ciliopathy-associated meckel syndrome 1 (mks1) protein and two novel mks1-related (mksr) proteins. Journal of Cell Science, 122:611-624, Mar 2009. URL: https://doi.org/10.1242/jcs.028621, doi:10.1242/jcs.028621. This article has 98 citations and is from a domain leading peer-reviewed journal.

17. (warburtonpitt2012ciliogenesisincaenorhabditis pages 3-4): Simon R. F. Warburton-Pitt, Andrew R. Jauregui, Chunmei Li, Juan Wang, M. Leroux, and M. Barr. Ciliogenesis in caenorhabditis elegans requires genetic interactions between ciliary middle segment localized nphp-2 (inversin) and transition zone-associated proteins. Journal of Cell Science, 125:2592-2603, Jun 2012. URL: https://doi.org/10.1242/jcs.095539, doi:10.1242/jcs.095539. This article has 57 citations and is from a domain leading peer-reviewed journal.

18. (jensen2015formationofthe pages 1-2): Victor L Jensen, Chunmei Li, Rachel V Bowie, Lara Clarke, Swetha Mohan, Oliver E Blacque, and Michel R Leroux. Formation of the transition zone by mks5/rpgrip1l establishes a ciliary zone of exclusion (cize) that compartmentalises ciliary signalling proteins and controls pip2 ciliary abundance. The EMBO Journal, 34:2537-2556, Oct 2015. URL: https://doi.org/10.15252/embj.201488044, doi:10.15252/embj.201488044. This article has 164 citations.

19. (warburtonpitt2012ciliogenesisincaenorhabditis pages 4-6): Simon R. F. Warburton-Pitt, Andrew R. Jauregui, Chunmei Li, Juan Wang, M. Leroux, and M. Barr. Ciliogenesis in caenorhabditis elegans requires genetic interactions between ciliary middle segment localized nphp-2 (inversin) and transition zone-associated proteins. Journal of Cell Science, 125:2592-2603, Jun 2012. URL: https://doi.org/10.1242/jcs.095539, doi:10.1242/jcs.095539. This article has 57 citations and is from a domain leading peer-reviewed journal.

20. (warburtonpitt2015theciliopathygene pages 95-99): Simon R. F. Warburton-Pitt. The ciliopathy gene nphp 2 functions in multiple gene networks and regulates ciliogenesis in c. elegans. ArXiv, Jan 2015. URL: https://doi.org/10.7282/t3v40wx3, doi:10.7282/t3v40wx3. This article has 0 citations.

21. (OpenTargets Search: -B9D1): Open Targets Query (-B9D1, 8 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

22. (caenenbraz2024newfunctionsof pages 8-10): Chloe Caenen-Braz, Latifa Bouzhir, and Pascale Dupuis-Williams. New functions of b9d2 in tight junctions and epithelial polarity. Scientific Reports, Oct 2024. URL: https://doi.org/10.1038/s41598-024-75577-w, doi:10.1038/s41598-024-75577-w. This article has 4 citations and is from a peer-reviewed journal.

23. (jensen2015formationofthe pages 2-4): Victor L Jensen, Chunmei Li, Rachel V Bowie, Lara Clarke, Swetha Mohan, Oliver E Blacque, and Michel R Leroux. Formation of the transition zone by mks5/rpgrip1l establishes a ciliary zone of exclusion (cize) that compartmentalises ciliary signalling proteins and controls pip2 ciliary abundance. The EMBO Journal, 34:2537-2556, Oct 2015. URL: https://doi.org/10.15252/embj.201488044, doi:10.15252/embj.201488044. This article has 164 citations.

24. (he2026ciliopathyrelatedb9protein pages 1-2): Ruida He, Yan Li, Minjun Jin, Huike Jiao, Yue Shen, Qize Han, Xilang Pan, Suning Wang, Zaisheng Lin, Jingshi Li, Chao Lu, Dan Meng, Zongfu Cao, Qing Shang, Nan Lv, Kai Wan, Huafang Gao, Xu Ma, Haiyan Yin, Haishuang Chang, Liang Wang, Minna Luo, Junmin Pan, Chengtian Zhao, and Muqing Cao. Ciliopathy-related b9 protein complex regulates ciliary axonemal microtubule posttranslational modifications and initiation of ciliogenesis. Journal of Clinical Investigation, Oct 2026. URL: https://doi.org/10.1172/jci196365, doi:10.1172/jci196365. This article has 0 citations and is from a highest quality peer-reviewed journal.

25. (he2026ciliopathyrelatedb9protein pages 4-5): Ruida He, Yan Li, Minjun Jin, Huike Jiao, Yue Shen, Qize Han, Xilang Pan, Suning Wang, Zaisheng Lin, Jingshi Li, Chao Lu, Dan Meng, Zongfu Cao, Qing Shang, Nan Lv, Kai Wan, Huafang Gao, Xu Ma, Haiyan Yin, Haishuang Chang, Liang Wang, Minna Luo, Junmin Pan, Chengtian Zhao, and Muqing Cao. Ciliopathy-related b9 protein complex regulates ciliary axonemal microtubule posttranslational modifications and initiation of ciliogenesis. Journal of Clinical Investigation, Oct 2026. URL: https://doi.org/10.1172/jci196365, doi:10.1172/jci196365. This article has 0 citations and is from a highest quality peer-reviewed journal.

26. (he2026ciliopathyrelatedb9protein pages 2-4): Ruida He, Yan Li, Minjun Jin, Huike Jiao, Yue Shen, Qize Han, Xilang Pan, Suning Wang, Zaisheng Lin, Jingshi Li, Chao Lu, Dan Meng, Zongfu Cao, Qing Shang, Nan Lv, Kai Wan, Huafang Gao, Xu Ma, Haiyan Yin, Haishuang Chang, Liang Wang, Minna Luo, Junmin Pan, Chengtian Zhao, and Muqing Cao. Ciliopathy-related b9 protein complex regulates ciliary axonemal microtubule posttranslational modifications and initiation of ciliogenesis. Journal of Clinical Investigation, Oct 2026. URL: https://doi.org/10.1172/jci196365, doi:10.1172/jci196365. This article has 0 citations and is from a highest quality peer-reviewed journal.

27. (jensen2015formationofthe pages 8-9): Victor L Jensen, Chunmei Li, Rachel V Bowie, Lara Clarke, Swetha Mohan, Oliver E Blacque, and Michel R Leroux. Formation of the transition zone by mks5/rpgrip1l establishes a ciliary zone of exclusion (cize) that compartmentalises ciliary signalling proteins and controls pip2 ciliary abundance. The EMBO Journal, 34:2537-2556, Oct 2015. URL: https://doi.org/10.15252/embj.201488044, doi:10.15252/embj.201488044. This article has 164 citations.

28. (jensen2015formationofthe pages 7-8): Victor L Jensen, Chunmei Li, Rachel V Bowie, Lara Clarke, Swetha Mohan, Oliver E Blacque, and Michel R Leroux. Formation of the transition zone by mks5/rpgrip1l establishes a ciliary zone of exclusion (cize) that compartmentalises ciliary signalling proteins and controls pip2 ciliary abundance. The EMBO Journal, 34:2537-2556, Oct 2015. URL: https://doi.org/10.15252/embj.201488044, doi:10.15252/embj.201488044. This article has 164 citations.

29. (jensen2015formationofthe pages 4-5): Victor L Jensen, Chunmei Li, Rachel V Bowie, Lara Clarke, Swetha Mohan, Oliver E Blacque, and Michel R Leroux. Formation of the transition zone by mks5/rpgrip1l establishes a ciliary zone of exclusion (cize) that compartmentalises ciliary signalling proteins and controls pip2 ciliary abundance. The EMBO Journal, 34:2537-2556, Oct 2015. URL: https://doi.org/10.15252/embj.201488044, doi:10.15252/embj.201488044. This article has 164 citations.

30. (li2016mks5andcep290 pages 11-12): Chunmei Li, Victor L. Jensen, Kwangjin Park, Julie Kennedy, Francesc R. Garcia-Gonzalo, Marta Romani, Roberta De Mori, Ange-Line Bruel, Dominique Gaillard, Bérénice Doray, Estelle Lopez, Jean-Baptiste Rivière, Laurence Faivre, Christel Thauvin-Robinet, Jeremy F. Reiter, Oliver E. Blacque, Enza Maria Valente, and Michel R. Leroux. Mks5 and cep290 dependent assembly pathway of the ciliary transition zone. PLOS Biology, 14:e1002416, Mar 2016. URL: https://doi.org/10.1371/journal.pbio.1002416, doi:10.1371/journal.pbio.1002416. This article has 176 citations and is from a highest quality peer-reviewed journal.

31. (li2016mks5andcep290 pages 7-9): Chunmei Li, Victor L. Jensen, Kwangjin Park, Julie Kennedy, Francesc R. Garcia-Gonzalo, Marta Romani, Roberta De Mori, Ange-Line Bruel, Dominique Gaillard, Bérénice Doray, Estelle Lopez, Jean-Baptiste Rivière, Laurence Faivre, Christel Thauvin-Robinet, Jeremy F. Reiter, Oliver E. Blacque, Enza Maria Valente, and Michel R. Leroux. Mks5 and cep290 dependent assembly pathway of the ciliary transition zone. PLOS Biology, 14:e1002416, Mar 2016. URL: https://doi.org/10.1371/journal.pbio.1002416, doi:10.1371/journal.pbio.1002416. This article has 176 citations and is from a highest quality peer-reviewed journal.

32. (bialas2009functionalinteractionsbetween pages 9-10): Nathan J. Bialas, Peter N. Inglis, Chunmei Li, Jon F. Robinson, Jeremy D. K. Parker, Michael P. Healey, Erica E. Davis, Chrystal D. Inglis, Tiina Toivonen, David C. Cottell, Oliver E. Blacque, Lynne M. Quarmby, Nicholas Katsanis, and Michel R. Leroux. Functional interactions between the ciliopathy-associated meckel syndrome 1 (mks1) protein and two novel mks1-related (mksr) proteins. Journal of Cell Science, 122:611-624, Mar 2009. URL: https://doi.org/10.1242/jcs.028621, doi:10.1242/jcs.028621. This article has 98 citations and is from a domain leading peer-reviewed journal.

33. (bialas2009functionalinteractionsbetween pages 10-11): Nathan J. Bialas, Peter N. Inglis, Chunmei Li, Jon F. Robinson, Jeremy D. K. Parker, Michael P. Healey, Erica E. Davis, Chrystal D. Inglis, Tiina Toivonen, David C. Cottell, Oliver E. Blacque, Lynne M. Quarmby, Nicholas Katsanis, and Michel R. Leroux. Functional interactions between the ciliopathy-associated meckel syndrome 1 (mks1) protein and two novel mks1-related (mksr) proteins. Journal of Cell Science, 122:611-624, Mar 2009. URL: https://doi.org/10.1242/jcs.028621, doi:10.1242/jcs.028621. This article has 98 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](mksr-1-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](mksr-1-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. zhang2010identificationofnovel pages 8-9
2. caenenbraz2024newfunctionsof pages 8-10
3. okazaki2020formationofthe pages 5-7
4. okazaki2020formationofthe pages 1-5
5. jensen2015formationofthe pages 12-14
6. bialas2009functionalinteractionsbetween pages 5-6
7. zhang2010identificationofnovel pages 5-6
8. bialas2009functionalinteractionsbetween pages 3-5
9. okazaki2020formationofthe pages 21-27
10. jensen2015formationofthe pages 14-15
11. bialas2009functionalinteractionsbetween pages 1-2
12. bialas2009functionalinteractionsbetween pages 6-7
13. bialas2009functionalinteractionsbetween pages 7-9
14. warburtonpitt2012ciliogenesisincaenorhabditis pages 3-4
15. jensen2015formationofthe pages 1-2
16. warburtonpitt2012ciliogenesisincaenorhabditis pages 4-6
17. warburtonpitt2015theciliopathygene pages 95-99
18. jensen2015formationofthe pages 2-4
19. jensen2015formationofthe pages 8-9
20. jensen2015formationofthe pages 7-8
21. jensen2015formationofthe pages 4-5
22. bialas2009functionalinteractionsbetween pages 9-10
23. bialas2009functionalinteractionsbetween pages 10-11
24. https://doi.org/10.1242/jcs.028621,
25. https://doi.org/10.1091/mbc.e20-03-0208,
26. https://doi.org/10.1016/j.gene.2010.08.006,
27. https://doi.org/10.1371/journal.pbio.1002416,
28. https://doi.org/10.15252/embj.201488044,
29. https://doi.org/10.1242/jcs.095539,
30. https://doi.org/10.7282/t3v40wx3,
31. https://doi.org/10.1038/s41598-024-75577-w,
32. https://doi.org/10.1172/jci196365,