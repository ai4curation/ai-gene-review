---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-30T06:41:12.604790'
end_time: '2026-09-30T06:58:49.506650'
duration_seconds: 1056.9
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: worm
  gene_id: tol-1
  gene_symbol: tol-1
  uniprot_accession: Q9N5Z3
  protein_description: 'SubName: Full=TIR domain-containing protein {ECO:0000313|EMBL:CCD63554.1};'
  gene_info: Name=tol-1 {ECO:0000313|EMBL:CCD63554.1, ECO:0000313|WormBase:C07F11.1};
    ORFNames=C07F11.1 {ECO:0000313|WormBase:C07F11.1}, CELE_C07F11.1 {ECO:0000313|EMBL:CCD63554.1};
  organism_full: Caenorhabditis elegans.
  protein_family: Belongs to the Toll-like receptor family.
  protein_domains: Leu-rich_rpt. (IPR001611); Leu-rich_rpt_typical-subtyp. (IPR003591);
    LRR_dom_sf. (IPR032675); LRR_TM_domain-containing. (IPR050541); TIR_dom. (IPR000157)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 38
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: tol-1-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: tol-1-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: tol-1-deep-research-falcon_artifacts/artifact-02.md
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
- **UniProt Accession:** Q9N5Z3
- **Protein Description:** SubName: Full=TIR domain-containing protein {ECO:0000313|EMBL:CCD63554.1};
- **Gene Information:** Name=tol-1 {ECO:0000313|EMBL:CCD63554.1, ECO:0000313|WormBase:C07F11.1}; ORFNames=C07F11.1 {ECO:0000313|WormBase:C07F11.1}, CELE_C07F11.1 {ECO:0000313|EMBL:CCD63554.1};
- **Organism (full):** Caenorhabditis elegans.
- **Protein Family:** Belongs to the Toll-like receptor family.
- **Key Domains:** Leu-rich_rpt. (IPR001611); Leu-rich_rpt_typical-subtyp. (IPR003591); LRR_dom_sf. (IPR032675); LRR_TM_domain-containing. (IPR050541); TIR_dom. (IPR000157)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "tol-1" matches the protein description above**
2. **Verify the organism is correct:** Caenorhabditis elegans.
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'tol-1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **tol-1** (gene ID: tol-1, UniProt: Q9N5Z3) in worm.

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
- **UniProt Accession:** Q9N5Z3
- **Protein Description:** SubName: Full=TIR domain-containing protein {ECO:0000313|EMBL:CCD63554.1};
- **Gene Information:** Name=tol-1 {ECO:0000313|EMBL:CCD63554.1, ECO:0000313|WormBase:C07F11.1}; ORFNames=C07F11.1 {ECO:0000313|WormBase:C07F11.1}, CELE_C07F11.1 {ECO:0000313|EMBL:CCD63554.1};
- **Organism (full):** Caenorhabditis elegans.
- **Protein Family:** Belongs to the Toll-like receptor family.
- **Key Domains:** Leu-rich_rpt. (IPR001611); Leu-rich_rpt_typical-subtyp. (IPR003591); LRR_dom_sf. (IPR032675); LRR_TM_domain-containing. (IPR050541); TIR_dom. (IPR000157)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "tol-1" matches the protein description above**
2. **Verify the organism is correct:** Caenorhabditis elegans.
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'tol-1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **tol-1** (gene ID: tol-1, UniProt: Q9N5Z3) in worm.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Comprehensive Research Report: C. elegans tol-1 Gene (TOL-1 Protein)

## Gene Identity Verification

The gene tol-1 (C07F11.1) in *Caenorhabditis elegans* encodes TOL-1, the sole Toll-like receptor (TLR) in this organism (carmonarosas2025structuralbasisand pages 10-11, carmonarosas2025structuralbasisand pages 1-2). The protein belongs to the Toll-like receptor family and contains leucine-rich repeat (LRR) domains and a Toll/interleukin-1 receptor (TIR) domain, consistent with the UniProt annotation for Q9N5Z3 (carmonarosas2023structuralbasisand pages 6-10, carmonarosas2025structuralbasisand pages 2-3). It is critical to note that TOL-1 is distinct from TIR-1, which is a separate intracellular TIR domain-containing adaptor protein homologous to mammalian SARM1; these are different C. elegans proteins encoded by separate genes (liberati2004requirementfora pages 4-5, liberati2004requirementfora pages 2-2, liberati2004requirementfora pages 1-2).

## Molecular Structure and Domain Organization

TOL-1 is a type-I single-pass transmembrane receptor with a modular architecture consisting of extracellular, transmembrane, and intracellular regions (carmonarosas2025structuralbasisand pages 2-3, carmonarosas2025structuralbasisand pages 1-2). The detailed structural organization is presented in the table below:

| Domain/Region | Location (amino acid positions if known) | Structure/Features | Function |
|---|---|---|---|
| Signal peptide and extracellular region | Signal peptide at the N terminus; ectodomain approximately residues 26–983 | Directs a large, glycosylated LRR-containing ectodomain to the cell surface; establishes the extracellular orientation expected for a single-pass Toll-like receptor (carmonarosas2025structuralbasisand pages 2-3, carmonarosas2025structuralbasisand pages 7-8) | Enables extracellular protein recognition while positioning the C-terminal TIR domain in the cytoplasm for signaling (carmonarosas2025structuralbasisand pages 10-11, carmonarosas2023structuralbasisand pages 40-41) |
| N-terminal LRR domain (N-LRR) | Within the N-terminal portion of the ectodomain | Large semicircular domain containing approximately 23 leucine-rich repeats, bounded by cap regions (carmonarosas2023structuralbasisand pages 6-10) | Provides most of the receptor's extended extracellular scaffold; a specific ligand or partner for this region has not yet been established (carmonarosas2023structuralbasisand pages 6-10, carmonarosas2025structuralbasisand pages 2-3) |
| C-terminal LRR domain (C-LRR; second LRR domain) | Extracellular; contains LAT-1-contacting residues Q712–N715 | Smaller domain containing approximately 5 LRRs and flanking caps; LAT-1 binds its convex surface and N-terminal cap, including a cysteine-rich loop (carmonarosas2023structuralbasisand pages 6-10, carmonarosas2025structuralbasisand pages 5-6) | Directly binds the lectin domain of the adhesion GPCR LAT-1. The wild-type complex has a reported dissociation constant of **K_D = 186 nM** and 1:1 stoichiometry; substitutions Q712A/Y713A/G714A/N715A abolish detectable binding and cause developmental defects (carmonarosas2025structuralbasisand pages 5-6, carmonarosas2023structuralbasisand pages 10-14, carmonarosas2023structuralbasisand pages 6-10) |
| Transmembrane segment | Immediately C-terminal to the ectodomain; exact residue boundaries not established in the cited passages | Single membrane-spanning helix characteristic of Toll-like receptors (carmonarosas2025structuralbasisand pages 2-3, carmonarosas2023structuralbasisand pages 40-41) | Anchors TOL-1 at the plasma membrane, separating its extracellular LRR recognition apparatus from its cytoplasmic signaling region; supports proposed trans-cellular interaction with LAT-1 on neighboring cells (carmonarosas2025structuralbasisand pages 10-11, carmonarosas2025structuralbasisand pages 1-2) |
| Cytoplasmic TIR domain | C-terminal intracellular region; exact residue boundaries not established in the cited passages | Toll/interleukin-1 receptor homology signaling domain (carmonarosas2025structuralbasisand pages 10-11, carmonarosas2025structuralbasisand pages 2-3) | Mediates or organizes intracellular signaling rather than catalysis. It is proposed to cooperate with LAT-1-associated G-protein signaling during development, although the downstream developmental pathway remains unresolved (carmonarosas2025structuralbasisand pages 10-11, carmonarosas2025structuralbasisand pages 11-12) |
| Full-length receptor architecture | Approximately residues 1–1221 overall, based on the reported structural schematic; precise boundaries should be checked against the current UniProt record | Type-I, single-pass cell-surface receptor organized as signal peptide → N-LRR → C-LRR → transmembrane helix → cytoplasmic TIR domain (carmonarosas2025structuralbasisand pages 10-11, carmonarosas2025structuralbasisand pages 1-2) | Integrates extracellular cell–cell recognition with intracellular signaling; experimentally supported roles include LAT-1-dependent embryonic morphogenesis and neuronal signaling (carmonarosas2025structuralbasisand pages 10-11, brandt2015tolllikereceptorsignaling pages 5-6) |


*Table: Structural and functional map of the *C. elegans* TOL-1 receptor, including its two extracellular LRR domains, membrane anchor, cytoplasmic TIR domain, and quantitative LAT-1-binding evidence. Approximate boundaries are distinguished from experimentally resolved interaction residues.*

The extracellular region contains two distinct LRR domains: a large N-terminal LRR (N-LRR) with approximately 23 leucine-rich repeats and a smaller C-terminal LRR (C-LRR) with approximately 5 repeats, both flanked by cap regions (carmonarosas2023structuralbasisand pages 6-10, carmonarosas2025structuralbasisand pages 5-6). Recent structural studies using X-ray crystallography and cryo-EM have revealed that the C-terminal LRR domain serves as the principal binding site for the adhesion GPCR LAT-1 (latrophilin), with the interaction occurring on the convex surface of this domain (carmonarosas2023structuralbasisand pages 6-10, carmonarosas2025structuralbasisand pages 5-6).

## Primary Molecular Function

### Receptor Function and Ligand Binding

The primary molecular function of TOL-1 is to act as a cell-surface receptor that mediates intercellular recognition through direct binding to LAT-1 (carmonarosas2025structuralbasisand pages 10-11, carmonarosas2025structuralbasisand pages 1-2). This interaction has been quantitatively characterized with a binding affinity of KD = 186 nM, forming a stable 1:1 complex between the TOL-1 C-terminal LRR and the LAT-1 lectin domain (carmonarosas2025structuralbasisand pages 5-6, carmonarosas2023structuralbasisand pages 10-14). 

Structure-guided mutagenesis demonstrated that specific residues (Q712, Y713, G714, N715) in the C-terminal LRR are critical for LAT-1 binding; a quadruple substitution at these positions (Q712A/Y713A/G714A/N715A) completely abolished detectable binding in vitro (carmonarosas2025structuralbasisand pages 5-6, carmonarosas2023structuralbasisand pages 10-14). Unlike enzymatic receptors, TOL-1 does not possess intrinsic catalytic activity; rather, it functions as a signaling scaffold through its intracellular TIR domain (carmonarosas2025structuralbasisand pages 10-11, carmonarosas2023structuralbasisand pages 14-18).

### Signaling Mechanism

The intracellular TIR domain is proposed to mediate signal transduction by recruiting adaptor proteins and activating downstream kinase cascades (carmonarosas2025structuralbasisand pages 10-11). In BAG sensory neurons, TOL-1 signals through a well-characterized MAPK pathway involving PIK-1/IRAK, TRF-1/TRAF, MOM-4, and the MAP kinase cascade MKK-4–PMK-3 (brandt2015tolllikereceptorsignaling pages 5-6). An IKB-1-dependent regulatory branch also modulates TOL-1 signaling, as deletion of ikb-1 suppresses defects caused by loss of tol-1 or pmk-3 (brandt2015tolllikereceptorsignaling pages 5-6).

## Biological Processes and Pathways

TOL-1 participates in multiple distinct biological processes, as summarized in the following table:

| Biological Process | Specific Role | Key Findings | Evidence Type | Key References |
|---|---|---|---|---|
| Embryonic development and morphogenesis | TOL-1 acts as a cell-surface binding partner for the adhesion GPCR LAT-1, probably across adjacent cells. The LAT-1 lectin domain binds the C-terminal/second LRR domain of TOL-1, potentially coupling intercellular recognition to TOL-1 TIR-domain and LAT-1 G-protein signaling. | Structural studies resolved a 1:1 LAT-1–TOL-1 ectodomain complex with a reported **K_D of 186 nM**. Structure-guided TOL-1 Q712A/Y713A/G714A/N715A substitutions abolished detectable binding without simply eliminating receptor expression. Genome-edited interface mutants had reduced brood size and embryo viability, embryonic or larval lethality, and anterior/pharyngeal abnormalities resembling aspects of *tol-1* loss of function. Expression in mostly distinct embryonic cells favors interaction in trans; the downstream developmental signaling mechanism remains unresolved. (carmonarosas2025structuralbasisand pages 5-6, carmonarosas2023structuralbasisand pages 10-14, carmonarosas2025structuralbasisand pages 11-12, carmonarosas2025structuralbasisand pages 7-8) | Biochemical binding assays; X-ray crystallography and cryo-EM; structure-guided mutagenesis; CRISPR genome editing; embryo/larva phenotyping; endogenous expression imaging and single-cell transcript analysis | Carmona-Rosas et al., bioRxiv preprint, May 4, 2023, https://doi.org/10.1101/2023.05.04.539414; peer-reviewed version, *Nature Structural & Molecular Biology*, June 2025, https://doi.org/10.1038/s41594-025-01592-8 (carmonarosas2023structuralbasisand pages 10-14, carmonarosas2025structuralbasisand pages 10-11) |
| Sensory-neuron development and function | TOL-1 acts cell-autonomously in BAG chemosensory neurons to establish neuronal morphology, gene expression, and CO₂-sensing competence. Signaling engages PIK-1/TRF-1 and a MOM-4–MKK-4–PMK-3 MAPK branch, with an IKB-1-related regulatory branch. | Approximately **30% of BAG neurons** in *tol-1* mutants had abnormal axonal commissures. Loss of *tol-1* reduced *gcy-33*, increased *gcy-31*, and impaired *flp-19* expression. Activated MKK-4 bypassed *tol-1* or *mom-4* defects but not *pmk-3* loss, placing TOL-1 upstream of PMK-3; deletion of *ikb-1* suppressed avoidance defects caused by *tol-1* or *pmk-3* loss. (brandt2015tolllikereceptorsignaling pages 5-6) | Loss-of-function genetics; BAG-specific rescue; epistasis with activated MAPK components; neuronal morphology and reporter-gene analyses; behavioral assays | Brandt & Ringstad, *Current Biology*, August 31, 2015, https://doi.org/10.1016/j.cub.2015.07.037 (brandt2015tolllikereceptorsignaling pages 5-6) |
| Pathogen-specific innate immunity | TOL-1 contributes selectively to host defense against some bacteria, especially *Salmonella enterica*, rather than serving as a universal pattern-recognition receptor for intestinal or epidermal immunity. It helps limit pharyngeal invasion and supports expression of selected antimicrobial/stress-response genes. | *tol-1(nr2033)* mutants showed markedly increased mortality during live *S. enterica* infection and greater pharyngeal invasion, despite normal pumping and no explanatory avoidance defect. Their lifespan was normal on heat-killed *E. coli*. Susceptibility was pathogen dependent: mutants were not more susceptible to *Enterococcus faecalis*, *Streptococcus pneumoniae*, or several other tested infections. TOL-1 affected expression of ABF-2 and HSP-16.41, but it is not required for AMP induction in every infection and is not established as the upstream activator of the canonical TIR-1–NSY-1–SEK-1–PMK-1 intestinal immune pathway. (tenor2008aconservedtoll‐like pages 2-3, tenor2008aconservedtoll‐like pages 5-6, kim2018signalinginthe pages 12-14, kim2018signalinginthe pages 7-9) | Pathogen-survival assays; microscopy of tissue invasion; feeding and avoidance controls; heat-killed-bacteria controls; immune-effector expression analysis; comparative mutant genetics | Tenor & Aballay, *EMBO Reports*, January 2008, https://doi.org/10.1038/sj.embor.7401104; Kim & Ewbank, *WormBook*, August 2018, https://doi.org/10.1895/wormbook.1.83.2 (tenor2008aconservedtoll‐like pages 2-3, kim2018signalinginthe pages 12-14) |
| Behavioral pathogen avoidance | TOL-1 enables neuronal surveillance and avoidance of *Serratia marcescens* by promoting developmental differentiation of BAG neurons. BAG cells use microbial CO₂ as evidence of metabolically active microbes and integrate it with additional cues; TOL-1 is therefore better supported as a permissive developmental regulator than as an acute microbial ligand sensor in this behavior. | *tol-1* mutants were defective in avoidance of *S. marcescens*. BAG-specific genetic rescue and MAPK epistasis linked the behavior to TOL-1-dependent BAG-neuron function. The phenotype was selective: *S. enterica* did not trigger lawn avoidance in either wild-type or mutant animals, showing that TOL-1-dependent immune susceptibility to Salmonella is mechanistically separable from Serratia avoidance. (brandt2015tolllikereceptorsignaling pages 8-8, brandt2015tolllikereceptorsignaling pages 1-3, brandt2015tolllikereceptorsignaling pages 8-9, tenor2008aconservedtoll‐like pages 2-3) | Pathogen-lawn and CO₂-avoidance assays; neuron-specific rescue; developmental timing experiments; sensory-neuron genetics and gene-expression analysis | Brandt & Ringstad, *Current Biology*, August 31, 2015, https://doi.org/10.1016/j.cub.2015.07.037; Tenor & Aballay, *EMBO Reports*, January 2008, https://doi.org/10.1038/sj.embor.7401104 (brandt2015tolllikereceptorsignaling pages 1-3, tenor2008aconservedtoll‐like pages 2-3) |


*Table: This table summarizes experimentally supported roles of *C. elegans* TOL-1 in development, sensory-neuron differentiation, pathogen-specific immunity, and avoidance behavior. It distinguishes well-established findings from context-dependent or unresolved signaling interpretations.*

### Embryonic Development and Morphogenesis (Major Recent Discovery)

A groundbreaking discovery published in 2023–2025 revealed that TOL-1 functions as an essential developmental receptor through its interaction with LAT-1 (carmonarosas2023structuralbasisand pages 10-14, carmonarosas2025structuralbasisand pages 10-11, carmonarosas2025structuralbasisand pages 1-2). This represents a paradigm shift in understanding TOL-1 function, as it establishes a non-immune developmental role. 

Genome-edited animals carrying interface-disrupting mutations that specifically abolish TOL-1–LAT-1 binding exhibited severe developmental phenotypes including reduced brood size, embryonic lethality (approximately 60% of embryos showed irregular shapes), and larval abnormalities (approximately 80% of L1 larvae displayed head or anterior defects) (carmonarosas2023structuralbasisand pages 10-14, carmonarosas2025structuralbasisand pages 8-9, carmonarosas2025structuralbasisand pages 9-10). These defects resembled tol-1 loss-of-function mutants, demonstrating that the LAT-1 interaction accounts for major TOL-1 developmental functions (carmonarosas2025structuralbasisand pages 10-11, carmonarosas2025structuralbasisand pages 11-12).

Expression analysis revealed that TOL-1 and LAT-1 are typically expressed in different embryonic cells (only 6% of MS-lineage cells and 15% of ABa-lineage cells coexpressed both transcripts), supporting a trans-cellular interaction model where TOL-1 on one cell binds LAT-1 on an adjacent cell during morphogenesis (carmonarosas2025structuralbasisand pages 7-8). The molecular mechanism appears to involve coordinated signaling through the TOL-1 TIR domain and LAT-1 G-protein coupling machinery, though the precise downstream pathway remains to be fully elucidated (carmonarosas2025structuralbasisand pages 10-11, carmonarosas2025structuralbasisand pages 11-12).

### Sensory Neuron Development and Function

TOL-1 functions cell-autonomously in BAG chemosensory neurons to establish neuronal morphology, gene expression programs, and sensory competence (brandt2015tolllikereceptorsignaling pages 8-8, brandt2015tolllikereceptorsignaling pages 1-3, brandt2015tolllikereceptorsignaling pages 5-6). Loss of tol-1 causes abnormal BAG axonal commissures in approximately 30% of neurons, reduced expression of the guanylyl cyclase gene gcy-33, increased expression of gcy-31, and impaired expression of the neuropeptide gene flp-19 (brandt2015tolllikereceptorsignaling pages 5-6).

The developmental role of TOL-1 in BAG neurons is mechanistically distinct from acute pathogen sensing; TOL-1 signaling during development establishes the neuronal machinery that enables BAG cells to detect environmental CO2—a marker of metabolically active microbes—and integrate this information with other sensory cues to distinguish pathogenic from non-pathogenic bacteria (brandt2015tolllikereceptorsignaling pages 8-8, brandt2015tolllikereceptorsignaling pages 1-3, brandt2015tolllikereceptorsignaling pages 8-9).

### Pathogen-Specific Innate Immunity

TOL-1 contributes selectively to defense against certain bacterial pathogens, particularly *Salmonella enterica*, rather than functioning as a universal pattern-recognition receptor (tenor2008aconservedtoll‐like pages 2-3, tenor2008aconservedtoll‐like pages 5-6, kim2018signalinginthe pages 12-14). The tol-1(nr2033) mutant showed markedly increased mortality during live *S. enterica* infection and greater pharyngeal invasion, with susceptibility comparable to mutants defective in p38 MAPK or TGF-β immune signaling (tenor2008aconservedtoll‐like pages 2-3).

Importantly, TOL-1's immune function is pathogen-dependent: mutants were not more susceptible to *Enterococcus faecalis*, *Streptococcus pneumoniae*, *Pseudomonas aeruginosa*, or *Drechmeria coniospora* (tenor2008aconservedtoll‐like pages 2-3, kim2005evolutionaryperspectiveson pages 2-3, tenor2008aconservedtoll‐like pages 5-6). TOL-1 affects expression of specific immune effectors including ABF-2 and HSP-16.41, though it is not required for antimicrobial peptide induction in all infections (tenor2008aconservedtoll‐like pages 5-6, kim2018signalinginthe pages 12-14).

Notably, the canonical Toll signaling pathway involving MyD88 and NF-κB found in mammals and *Drosophila* is not functional in *C. elegans*, as the organism lacks key pathway components (kim2005evolutionaryperspectiveson pages 2-3). Instead, the separate protein TIR-1 (not TOL-1) acts upstream of the PMK-1 p38 MAPK pathway in intestinal immunity (liberati2004requirementfora pages 4-5, liberati2004requirementfora pages 2-2, kim2018signalinginthe pages 7-9).

### Behavioral Pathogen Avoidance

TOL-1 enables behavioral avoidance of the pathogenic bacterium *Serratia marcescens* through its developmental role in BAG neurons (brandt2015tolllikereceptorsignaling pages 8-8, brandt2015tolllikereceptorsignaling pages 1-3, kim2005evolutionaryperspectiveson pages 2-3). This function is mechanistically separable from TOL-1's role in *Salmonella* immunity: *S. enterica* does not trigger avoidance behavior in either wild-type or mutant animals, demonstrating that susceptibility to *Salmonella* reflects failed immune defense rather than defective avoidance (tenor2008aconservedtoll‐like pages 2-3).

BAG neurons integrate CO2 sensing with additional pathogen-specific cues, allowing worms to distinguish metabolically active pathogenic bacteria from attenuated or dead microbes that might serve as food (brandt2015tolllikereceptorsignaling pages 8-8, brandt2015tolllikereceptorsignaling pages 1-3, brandt2015tolllikereceptorsignaling pages 8-9). TOL-1 signaling establishes this sensory integration capacity during neuronal development rather than acting as an acute microbial ligand sensor in adults (brandt2015tolllikereceptorsignaling pages 1-3, brandt2015tolllikereceptorsignaling pages 8-9).

## Subcellular Localization and Tissue Expression

| Developmental Stage/Tissue | Specific Location | Expression Pattern | Function at that Location |
|---|---|---|---|
| Embryogenesis | Developing embryo from approximately the comma stage onward | Endogenous fluorescent reporter shows punctate TOL-1 signal extending along the anterior–posterior axis; expression occurs in multiple embryonic cell types and morphogenetically active regions (carmonarosas2025structuralbasisand pages 9-10, carmonarosas2025structuralbasisand pages 10-10) | Supports embryonic viability and morphogenesis. TOL-1 on one cell probably binds LAT-1 on an adjacent cell, creating a trans-cellular developmental signaling or adhesion complex (carmonarosas2025structuralbasisand pages 10-11, carmonarosas2025structuralbasisand pages 1-2, carmonarosas2025structuralbasisand pages 7-8) |
| Embryonic MS and ABa lineages | Cells that principally generate muscle- and neuronal-lineage derivatives | Most cells express either *tol-1* or *lat-1*, not both; coexpression was detected in only **6% of MS-lineage cells** and **15% of ABa-lineage cells** (carmonarosas2025structuralbasisand pages 7-8) | The largely mutually exclusive expression pattern supports TOL-1–LAT-1 binding in trans between neighboring cells during tissue organization, although cis interactions remain possible where the receptors overlap (carmonarosas2025structuralbasisand pages 10-11, carmonarosas2025structuralbasisand pages 7-8) |
| Embryonic head | Embryonic nerve-ring neurons and head mesodermal cell (HMC) | Transcript and endogenous protein analyses detect TOL-1 in nerve-ring neurons and HMCs; later embryonic signal is particularly prominent in developing head structures (carmonarosas2025structuralbasisand pages 9-10) | Likely contributes to neuronal and anterior/head morphogenesis. TOL-1–LAT-1 interface mutants show irregular embryos and anterior defects (carmonarosas2023structuralbasisand pages 10-14, carmonarosas2025structuralbasisand pages 8-9, carmonarosas2025structuralbasisand pages 9-10) |
| Embryonic pharyngeal region | Pharyngeal–intestinal valve and developing anterior/pharyngeal structures | Punctate TOL-1 reporter signal occurs near the pharyngeal–intestinal valve and persists in this region after embryogenesis (carmonarosas2025structuralbasisand pages 9-10, carmonarosas2025structuralbasisand pages 10-11) | Supports anterior and pharyngeal morphogenesis; disruption of the LAT-1-binding interface or loss of *tol-1* causes pharyngeal and anterior abnormalities (carmonarosas2023structuralbasisand pages 10-14, carmonarosas2023structuralbasisand pages 18-23) |
| Larval stages, including L1 | Anterior body, head, pharynx, nerve ring, valve, and other developing tissues | TOL-1 expression continues throughout larval development, with reporter signal in the nerve ring, pharyngeal structures, valve, gonad, and vulva (carmonarosas2025structuralbasisand pages 9-10, carmonarosas2025structuralbasisand pages 10-10) | Required for postembryonic viability and proper anterior development; approximately **80% of affected L1 larvae** in the reported mutant analysis displayed head or anterior abnormalities (carmonarosas2025structuralbasisand pages 8-9, carmonarosas2025structuralbasisand pages 9-10) |
| Larval and adult nervous system | Nerve-ring neuropil and head neuronal processes | Strong, punctate endogenous TOL-1 signal occurs in the head and nerve-ring neuropil, where processes from numerous neurons bundle together; TOL-1 and LAT-1 can occupy the same neuropil (carmonarosas2025structuralbasisand pages 9-10, carmonarosas2025structuralbasisand pages 10-11, carmonarosas2025structuralbasisand pages 10-10) | Provides a cell-surface platform for neuronal signaling and potentially both trans and cis TOL-1–LAT-1 interactions (carmonarosas2025structuralbasisand pages 9-10, carmonarosas2025structuralbasisand pages 10-11) |
| BAG sensory neurons | Paired head chemosensory neurons and their axonal commissures | TOL-1 is expressed and functions cell-autonomously in BAG neurons; about **30% of BAG neurons** in *tol-1* mutants have abnormal axonal commissures (brandt2015tolllikereceptorsignaling pages 8-8, brandt2015tolllikereceptorsignaling pages 5-6) | Promotes BAG-neuron development, wiring, and expression of sensory genes such as *gcy-33*, *gcy-31*, and *flp-19*. This establishes CO₂-sensing competence and enables avoidance of pathogenic *Serratia marcescens* (brandt2015tolllikereceptorsignaling pages 5-6, brandt2015tolllikereceptorsignaling pages 1-3) |
| URY neurons | URY sensory neurons whose endings extend toward the anterior pharynx | TOL-1 is expressed in URY and several other neural cells; URY endings anatomically approach the anterior end of the pharynx (tenor2008aconservedtoll‐like pages 5-6) | May link neuronal microbial sensing to regulation of pharyngeal or peripheral defenses, although this neuron-to-tissue mechanism remains inferential rather than directly resolved (tenor2008aconservedtoll‐like pages 5-6) |
| Young-adult head | Nerve ring, pharynx/isthmus, terminal bulb, valve cell, and surrounding head region | Endogenous TOL-1::WrmScarlet is distributed throughout the head, with clear signal in the nerve ring and valve; interface mutations do not grossly abolish localization (carmonarosas2025structuralbasisand pages 10-11, carmonarosas2025structuralbasisand pages 10-10) | Supports neuronal and pharyngeal functions independently of receptor trafficking; defects caused by interface substitutions probably reflect loss of LAT-1 communication rather than wholesale TOL-1 mislocalization (carmonarosas2025structuralbasisand pages 10-11) |
| Subcellular localization | Plasma membrane/cell surface | Domain architecture identifies TOL-1 as a type-I single-pass transmembrane receptor: its LRR ectodomain is extracellular, whereas its TIR domain is cytoplasmic (carmonarosas2025structuralbasisand pages 2-3, carmonarosas2025structuralbasisand pages 7-8, carmonarosas2023structuralbasisand pages 40-41) | The extracellular C-terminal LRR domain directly binds LAT-1, while the intracellular TIR domain is positioned to organize signal transduction. No catalytic activity or enzymatic substrate has been demonstrated for TOL-1 (carmonarosas2025structuralbasisand pages 5-6, carmonarosas2025structuralbasisand pages 10-11, carmonarosas2025structuralbasisand pages 11-12) |


*Table: Developmental, tissue, neuronal, and subcellular distribution of TOL-1 in *C. elegans*, together with the functions supported at each location. The table distinguishes direct localization evidence from proposed site-specific roles.*

TOL-1 is localized to the plasma membrane as a type-I transmembrane receptor, with its extracellular LRR domains positioned outside the cell and its TIR domain in the cytoplasm (carmonarosas2025structuralbasisand pages 2-3, carmonarosas2025structuralbasisand pages 7-8, carmonarosas2023structuralbasisand pages 40-41). This orientation enables TOL-1 to mediate intercellular communication by binding LAT-1 on adjacent cells in trans (carmonarosas2025structuralbasisand pages 10-11, carmonarosas2025structuralbasisand pages 1-2).

### Developmental Expression

TOL-1 expression begins during early embryogenesis from approximately the comma stage and continues throughout development (carmonarosas2025structuralbasisand pages 9-10, carmonarosas2025structuralbasisand pages 10-10). During embryogenesis, TOL-1 shows a punctate expression pattern extending along the anterior–posterior axis, with specific detection in embryonic nerve ring neurons, head mesodermal cells, and the pharyngeal–intestinal valve region (carmonarosas2025structuralbasisand pages 9-10).

### Tissue-Specific Expression

In larvae and adults, TOL-1 is prominently expressed in the nervous system, particularly in the nerve ring neuropil where neuronal processes from many cells converge (carmonarosas2025structuralbasisand pages 9-10, carmonarosas2025structuralbasisand pages 10-11, carmonarosas2025structuralbasisand pages 10-10). Additional expression sites include the pharynx, pharyngeal–intestinal valve, gonad, and vulva (carmonarosas2025structuralbasisand pages 9-10, carmonarosas2025structuralbasisand pages 10-10).

Specific neuronal populations expressing TOL-1 include BAG chemosensory neurons and URY sensory neurons (tenor2008aconservedtoll‐like pages 5-6, brandt2015tolllikereceptorsignaling pages 8-8, brandt2015tolllikereceptorsignaling pages 5-6). URY neuron endings extend to the anterior pharynx, providing a potential anatomical link between neuronal pathogen sensing and pharyngeal immune regulation (tenor2008aconservedtoll‐like pages 5-6).

## Recent Developments (2023–2025)

### Structural Biology Breakthrough

The most significant recent advance was the structural determination of the TOL-1–LAT-1 complex by Carmona-Rosas and colleagues, published in *Nature Structural & Molecular Biology* in 2025 (with a 2023 preprint) (carmonarosas2023structuralbasisand pages 10-14, carmonarosas2025structuralbasisand pages 10-11). This work provided:

1. High-resolution crystal structure and cryo-EM density map of the LAT-1–TOL-1 ectodomain complex (carmonarosas2023structuralbasisand pages 10-14, carmonarosas2023structuralbasisand pages 6-10)
2. Quantitative binding affinity (KD = 186 nM) and 1:1 stoichiometry (carmonarosas2025structuralbasisand pages 5-6, carmonarosas2023structuralbasisand pages 10-14)
3. Structure-guided functional validation demonstrating that the TOL-1–LAT-1 interaction is essential for embryonic development, morphogenesis, fertility, and survival (carmonarosas2023structuralbasisand pages 10-14, carmonarosas2025structuralbasisand pages 10-11)
4. Evidence for trans-cellular interaction between receptors on adjacent cells during development (carmonarosas2025structuralbasisand pages 10-11, carmonarosas2025structuralbasisand pages 1-2, carmonarosas2025structuralbasisand pages 7-8)

This discovery established a previously unknown developmental receptor–ligand axis and demonstrated that TOL-1 functions beyond its roles in immunity and neuronal behavior.

### Related TIR Domain Research

While not directly about TOL-1, important parallel discoveries have been made regarding TIR-1/SARM1, the separate TIR domain protein often confused with TOL-1. These include mechanistic insights into TIR-1 phase transition and NAD+ glycohydrolase activity in immune and neurodegenerative contexts, though these findings apply to TIR-1, not TOL-1.

## Conclusion

TOL-1 (gene tol-1, C07F11.1) is a multifunctional cell-surface receptor in *C. elegans* with three principal roles: (1) an essential developmental function as the binding partner for LAT-1 adhesion GPCR, mediating intercellular signaling required for embryonic morphogenesis, (2) a developmental regulator of BAG sensory neurons that establishes pathogen-detection and avoidance capabilities, and (3) a pathogen-specific contributor to innate immunity against select bacteria such as *Salmonella enterica*.

At the molecular level, TOL-1 functions as a non-catalytic signaling receptor that uses its extracellular C-terminal LRR domain to bind LAT-1 with high affinity (KD = 186 nM) and its intracellular TIR domain to organize downstream signaling through MAPK cascades and potentially NF-κB-related pathways. The receptor is localized to the plasma membrane and is expressed from early embryogenesis through adulthood in neurons, head structures, pharynx, and developing tissues where it mediates trans-cellular interactions.

Recent structural biology advances (2023–2025) have transformed our understanding of TOL-1 by revealing its critical developmental function, which appears to be at least as important as its immune and behavioral roles. Unlike canonical TLRs in mammals and flies, TOL-1 does not function primarily as a pathogen pattern-recognition receptor but rather integrates developmental, neuronal, and selective immune functions in a context-dependent manner.

References

1. (carmonarosas2025structuralbasisand pages 10-11): Gabriel Carmona-Rosas, Jing-Xian Li, Jayson J. Smith, Wioletta I. Nawrocka, Shou-Qiang Cheng, Elana E. Baltrusaitis, Minglei Zhao, D. Araç, Paschalis Kratsios, and E. Özkan. Structural basis and functional roles for toll-like receptor binding to latrophilin in c. elegans development. Nature structural & molecular biology, 32:1683-1696, Jun 2025. URL: https://doi.org/10.1038/s41594-025-01592-8, doi:10.1038/s41594-025-01592-8. This article has 6 citations and is from a highest quality peer-reviewed journal.

2. (carmonarosas2025structuralbasisand pages 1-2): Gabriel Carmona-Rosas, Jing-Xian Li, Jayson J. Smith, Wioletta I. Nawrocka, Shou-Qiang Cheng, Elana E. Baltrusaitis, Minglei Zhao, D. Araç, Paschalis Kratsios, and E. Özkan. Structural basis and functional roles for toll-like receptor binding to latrophilin in c. elegans development. Nature structural & molecular biology, 32:1683-1696, Jun 2025. URL: https://doi.org/10.1038/s41594-025-01592-8, doi:10.1038/s41594-025-01592-8. This article has 6 citations and is from a highest quality peer-reviewed journal.

3. (carmonarosas2023structuralbasisand pages 6-10): Gabriel Carmona-Rosas, Jingxian Li, Jayson J. Smith, Shouqiang Cheng, Elana Baltrusaitis, Wioletta I. Nawrocka, Minglei Zhao, Paschalis Kratsios, Demet Araç, and Engin Özkan. Structural basis and functional roles for toll-like receptor binding to latrophilin adhesion-gpcr in embryo development. bioRxiv, May 2023. URL: https://doi.org/10.1101/2023.05.04.539414, doi:10.1101/2023.05.04.539414. This article has 1 citations.

4. (carmonarosas2025structuralbasisand pages 2-3): Gabriel Carmona-Rosas, Jing-Xian Li, Jayson J. Smith, Wioletta I. Nawrocka, Shou-Qiang Cheng, Elana E. Baltrusaitis, Minglei Zhao, D. Araç, Paschalis Kratsios, and E. Özkan. Structural basis and functional roles for toll-like receptor binding to latrophilin in c. elegans development. Nature structural & molecular biology, 32:1683-1696, Jun 2025. URL: https://doi.org/10.1038/s41594-025-01592-8, doi:10.1038/s41594-025-01592-8. This article has 6 citations and is from a highest quality peer-reviewed journal.

5. (liberati2004requirementfora pages 4-5): Nicole T. Liberati, Katherine A. Fitzgerald, Dennis H. Kim, Rhonda Feinbaum, Douglas T. Golenbock, and Frederick M. Ausubel. Requirement for a conserved toll/interleukin-1 resistance domain protein in the caenorhabditis elegans immune response. Proceedings of the National Academy of Sciences of the United States of America, 101 17:6593-8, Apr 2004. URL: https://doi.org/10.1073/pnas.0308625101, doi:10.1073/pnas.0308625101. This article has 315 citations and is from a highest quality peer-reviewed journal.

6. (liberati2004requirementfora pages 2-2): Nicole T. Liberati, Katherine A. Fitzgerald, Dennis H. Kim, Rhonda Feinbaum, Douglas T. Golenbock, and Frederick M. Ausubel. Requirement for a conserved toll/interleukin-1 resistance domain protein in the caenorhabditis elegans immune response. Proceedings of the National Academy of Sciences of the United States of America, 101 17:6593-8, Apr 2004. URL: https://doi.org/10.1073/pnas.0308625101, doi:10.1073/pnas.0308625101. This article has 315 citations and is from a highest quality peer-reviewed journal.

7. (liberati2004requirementfora pages 1-2): Nicole T. Liberati, Katherine A. Fitzgerald, Dennis H. Kim, Rhonda Feinbaum, Douglas T. Golenbock, and Frederick M. Ausubel. Requirement for a conserved toll/interleukin-1 resistance domain protein in the caenorhabditis elegans immune response. Proceedings of the National Academy of Sciences of the United States of America, 101 17:6593-8, Apr 2004. URL: https://doi.org/10.1073/pnas.0308625101, doi:10.1073/pnas.0308625101. This article has 315 citations and is from a highest quality peer-reviewed journal.

8. (carmonarosas2025structuralbasisand pages 7-8): Gabriel Carmona-Rosas, Jing-Xian Li, Jayson J. Smith, Wioletta I. Nawrocka, Shou-Qiang Cheng, Elana E. Baltrusaitis, Minglei Zhao, D. Araç, Paschalis Kratsios, and E. Özkan. Structural basis and functional roles for toll-like receptor binding to latrophilin in c. elegans development. Nature structural & molecular biology, 32:1683-1696, Jun 2025. URL: https://doi.org/10.1038/s41594-025-01592-8, doi:10.1038/s41594-025-01592-8. This article has 6 citations and is from a highest quality peer-reviewed journal.

9. (carmonarosas2023structuralbasisand pages 40-41): Gabriel Carmona-Rosas, Jingxian Li, Jayson J. Smith, Shouqiang Cheng, Elana Baltrusaitis, Wioletta I. Nawrocka, Minglei Zhao, Paschalis Kratsios, Demet Araç, and Engin Özkan. Structural basis and functional roles for toll-like receptor binding to latrophilin adhesion-gpcr in embryo development. bioRxiv, May 2023. URL: https://doi.org/10.1101/2023.05.04.539414, doi:10.1101/2023.05.04.539414. This article has 1 citations.

10. (carmonarosas2025structuralbasisand pages 5-6): Gabriel Carmona-Rosas, Jing-Xian Li, Jayson J. Smith, Wioletta I. Nawrocka, Shou-Qiang Cheng, Elana E. Baltrusaitis, Minglei Zhao, D. Araç, Paschalis Kratsios, and E. Özkan. Structural basis and functional roles for toll-like receptor binding to latrophilin in c. elegans development. Nature structural & molecular biology, 32:1683-1696, Jun 2025. URL: https://doi.org/10.1038/s41594-025-01592-8, doi:10.1038/s41594-025-01592-8. This article has 6 citations and is from a highest quality peer-reviewed journal.

11. (carmonarosas2023structuralbasisand pages 10-14): Gabriel Carmona-Rosas, Jingxian Li, Jayson J. Smith, Shouqiang Cheng, Elana Baltrusaitis, Wioletta I. Nawrocka, Minglei Zhao, Paschalis Kratsios, Demet Araç, and Engin Özkan. Structural basis and functional roles for toll-like receptor binding to latrophilin adhesion-gpcr in embryo development. bioRxiv, May 2023. URL: https://doi.org/10.1101/2023.05.04.539414, doi:10.1101/2023.05.04.539414. This article has 1 citations.

12. (carmonarosas2025structuralbasisand pages 11-12): Gabriel Carmona-Rosas, Jing-Xian Li, Jayson J. Smith, Wioletta I. Nawrocka, Shou-Qiang Cheng, Elana E. Baltrusaitis, Minglei Zhao, D. Araç, Paschalis Kratsios, and E. Özkan. Structural basis and functional roles for toll-like receptor binding to latrophilin in c. elegans development. Nature structural & molecular biology, 32:1683-1696, Jun 2025. URL: https://doi.org/10.1038/s41594-025-01592-8, doi:10.1038/s41594-025-01592-8. This article has 6 citations and is from a highest quality peer-reviewed journal.

13. (brandt2015tolllikereceptorsignaling pages 5-6): Julia P. Brandt and Niels Ringstad. Toll-like receptor signaling promotes development and function of sensory neurons required for a c. elegans pathogen-avoidance behavior. Current Biology, 25:2228-2237, Aug 2015. URL: https://doi.org/10.1016/j.cub.2015.07.037, doi:10.1016/j.cub.2015.07.037. This article has 138 citations and is from a highest quality peer-reviewed journal.

14. (carmonarosas2023structuralbasisand pages 14-18): Gabriel Carmona-Rosas, Jingxian Li, Jayson J. Smith, Shouqiang Cheng, Elana Baltrusaitis, Wioletta I. Nawrocka, Minglei Zhao, Paschalis Kratsios, Demet Araç, and Engin Özkan. Structural basis and functional roles for toll-like receptor binding to latrophilin adhesion-gpcr in embryo development. bioRxiv, May 2023. URL: https://doi.org/10.1101/2023.05.04.539414, doi:10.1101/2023.05.04.539414. This article has 1 citations.

15. (tenor2008aconservedtoll‐like pages 2-3): Jennifer L. Tenor and Alejandro Aballay. A conserved toll‐like receptor is required for caenorhabditis elegans innate immunity. EMBO reports, Jan 2008. URL: https://doi.org/10.1038/sj.embor.7401104, doi:10.1038/sj.embor.7401104. This article has 251 citations and is from a highest quality peer-reviewed journal.

16. (tenor2008aconservedtoll‐like pages 5-6): Jennifer L. Tenor and Alejandro Aballay. A conserved toll‐like receptor is required for caenorhabditis elegans innate immunity. EMBO reports, Jan 2008. URL: https://doi.org/10.1038/sj.embor.7401104, doi:10.1038/sj.embor.7401104. This article has 251 citations and is from a highest quality peer-reviewed journal.

17. (kim2018signalinginthe pages 12-14): Dennis H. Kim and J. Ewbank. Signaling in the innate immune response. WormBook, pages 1-35, Aug 2018. URL: https://doi.org/10.1895/wormbook.1.83.2, doi:10.1895/wormbook.1.83.2. This article has 184 citations.

18. (kim2018signalinginthe pages 7-9): Dennis H. Kim and J. Ewbank. Signaling in the innate immune response. WormBook, pages 1-35, Aug 2018. URL: https://doi.org/10.1895/wormbook.1.83.2, doi:10.1895/wormbook.1.83.2. This article has 184 citations.

19. (brandt2015tolllikereceptorsignaling pages 8-8): Julia P. Brandt and Niels Ringstad. Toll-like receptor signaling promotes development and function of sensory neurons required for a c. elegans pathogen-avoidance behavior. Current Biology, 25:2228-2237, Aug 2015. URL: https://doi.org/10.1016/j.cub.2015.07.037, doi:10.1016/j.cub.2015.07.037. This article has 138 citations and is from a highest quality peer-reviewed journal.

20. (brandt2015tolllikereceptorsignaling pages 1-3): Julia P. Brandt and Niels Ringstad. Toll-like receptor signaling promotes development and function of sensory neurons required for a c. elegans pathogen-avoidance behavior. Current Biology, 25:2228-2237, Aug 2015. URL: https://doi.org/10.1016/j.cub.2015.07.037, doi:10.1016/j.cub.2015.07.037. This article has 138 citations and is from a highest quality peer-reviewed journal.

21. (brandt2015tolllikereceptorsignaling pages 8-9): Julia P. Brandt and Niels Ringstad. Toll-like receptor signaling promotes development and function of sensory neurons required for a c. elegans pathogen-avoidance behavior. Current Biology, 25:2228-2237, Aug 2015. URL: https://doi.org/10.1016/j.cub.2015.07.037, doi:10.1016/j.cub.2015.07.037. This article has 138 citations and is from a highest quality peer-reviewed journal.

22. (carmonarosas2025structuralbasisand pages 8-9): Gabriel Carmona-Rosas, Jing-Xian Li, Jayson J. Smith, Wioletta I. Nawrocka, Shou-Qiang Cheng, Elana E. Baltrusaitis, Minglei Zhao, D. Araç, Paschalis Kratsios, and E. Özkan. Structural basis and functional roles for toll-like receptor binding to latrophilin in c. elegans development. Nature structural & molecular biology, 32:1683-1696, Jun 2025. URL: https://doi.org/10.1038/s41594-025-01592-8, doi:10.1038/s41594-025-01592-8. This article has 6 citations and is from a highest quality peer-reviewed journal.

23. (carmonarosas2025structuralbasisand pages 9-10): Gabriel Carmona-Rosas, Jing-Xian Li, Jayson J. Smith, Wioletta I. Nawrocka, Shou-Qiang Cheng, Elana E. Baltrusaitis, Minglei Zhao, D. Araç, Paschalis Kratsios, and E. Özkan. Structural basis and functional roles for toll-like receptor binding to latrophilin in c. elegans development. Nature structural & molecular biology, 32:1683-1696, Jun 2025. URL: https://doi.org/10.1038/s41594-025-01592-8, doi:10.1038/s41594-025-01592-8. This article has 6 citations and is from a highest quality peer-reviewed journal.

24. (kim2005evolutionaryperspectiveson pages 2-3): Dennis H Kim and Frederick M Ausubel. Evolutionary perspectives on innate immunity from the study of caenorhabditis elegans. Current opinion in immunology, 17 1:4-10, Feb 2005. URL: https://doi.org/10.1016/j.coi.2004.11.007, doi:10.1016/j.coi.2004.11.007. This article has 180 citations and is from a peer-reviewed journal.

25. (carmonarosas2025structuralbasisand pages 10-10): Gabriel Carmona-Rosas, Jing-Xian Li, Jayson J. Smith, Wioletta I. Nawrocka, Shou-Qiang Cheng, Elana E. Baltrusaitis, Minglei Zhao, D. Araç, Paschalis Kratsios, and E. Özkan. Structural basis and functional roles for toll-like receptor binding to latrophilin in c. elegans development. Nature structural & molecular biology, 32:1683-1696, Jun 2025. URL: https://doi.org/10.1038/s41594-025-01592-8, doi:10.1038/s41594-025-01592-8. This article has 6 citations and is from a highest quality peer-reviewed journal.

26. (carmonarosas2023structuralbasisand pages 18-23): Gabriel Carmona-Rosas, Jingxian Li, Jayson J. Smith, Shouqiang Cheng, Elana Baltrusaitis, Wioletta I. Nawrocka, Minglei Zhao, Paschalis Kratsios, Demet Araç, and Engin Özkan. Structural basis and functional roles for toll-like receptor binding to latrophilin adhesion-gpcr in embryo development. bioRxiv, May 2023. URL: https://doi.org/10.1101/2023.05.04.539414, doi:10.1101/2023.05.04.539414. This article has 1 citations.

## Artifacts

- [Edison artifact artifact-00](tol-1-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](tol-1-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](tol-1-deep-research-falcon_artifacts/artifact-02.md)

## Citations

1. carmonarosas2023structuralbasisand pages 6-10
2. carmonarosas2025structuralbasisand pages 10-11
3. brandt2015tolllikereceptorsignaling pages 5-6
4. carmonarosas2025structuralbasisand pages 7-8
5. kim2005evolutionaryperspectiveson pages 2-3
6. carmonarosas2025structuralbasisand pages 9-10
7. carmonarosas2025structuralbasisand pages 1-2
8. carmonarosas2025structuralbasisand pages 2-3
9. liberati2004requirementfora pages 4-5
10. liberati2004requirementfora pages 2-2
11. liberati2004requirementfora pages 1-2
12. carmonarosas2023structuralbasisand pages 40-41
13. carmonarosas2025structuralbasisand pages 5-6
14. carmonarosas2023structuralbasisand pages 10-14
15. carmonarosas2025structuralbasisand pages 11-12
16. carmonarosas2023structuralbasisand pages 14-18
17. kim2018signalinginthe pages 12-14
18. kim2018signalinginthe pages 7-9
19. brandt2015tolllikereceptorsignaling pages 8-8
20. brandt2015tolllikereceptorsignaling pages 1-3
21. brandt2015tolllikereceptorsignaling pages 8-9
22. carmonarosas2025structuralbasisand pages 8-9
23. carmonarosas2025structuralbasisand pages 10-10
24. carmonarosas2023structuralbasisand pages 18-23
25. https://doi.org/10.1101/2023.05.04.539414;
26. https://doi.org/10.1038/s41594-025-01592-8
27. https://doi.org/10.1016/j.cub.2015.07.037
28. https://doi.org/10.1038/sj.embor.7401104;
29. https://doi.org/10.1895/wormbook.1.83.2
30. https://doi.org/10.1016/j.cub.2015.07.037;
31. https://doi.org/10.1038/sj.embor.7401104
32. https://doi.org/10.1038/s41594-025-01592-8,
33. https://doi.org/10.1101/2023.05.04.539414,
34. https://doi.org/10.1073/pnas.0308625101,
35. https://doi.org/10.1016/j.cub.2015.07.037,
36. https://doi.org/10.1038/sj.embor.7401104,
37. https://doi.org/10.1895/wormbook.1.83.2,
38. https://doi.org/10.1016/j.coi.2004.11.007,