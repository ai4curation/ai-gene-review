---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-28T16:13:49.577099'
end_time: '2026-06-28T16:42:40.371838'
duration_seconds: 1730.8
template_file: templates/module_research.md.j2
template_variables:
  module_title: EGFR signaling pathway module
  module_summary: EGF-family ligand binding activates EGFR/ERBB1 receptor tyrosine
    kinase dimers, creating phosphotyrosine docking sites that recruit GRB2/SOS, PI3K,
    PLCG, and STAT branches for proliferation and differentiation outputs.
  module_outline: "- EGFR signaling pathway\n  - 1. egf ligand binds egfr\n  - EGF\
    \ ligand binds EGFR\n    - EGF ligand (molecular player: EGF; activity or role:\
    \ signaling receptor binding)\n    - EGFR receptor (molecular player: EGFR receptor\
    \ family/ortholog group; activity or role: transmembrane receptor protein tyrosine\
    \ kinase activity)\n  - 2. grb2/sos adaptor recruitment\n  - GRB2/SOS adaptor\
    \ recruitment\n    - GRB2 adaptor (molecular player: GRB2 adaptor family/ortholog\
    \ group)\n    - SOS1 Ras GEF (molecular player: SOS1; activity or role: guanyl-nucleotide\
    \ exchange factor activity)\n  - 3. mapk/pi3k transcriptional output\n  - MAPK/PI3K\
    \ transcriptional output\n    - ERBB2 paralogous RTK context (molecular player:\
    \ ERBB2 paralogous RTK context family/ortholog group; activity or role: transmembrane\
    \ receptor protein tyrosine kinase activity)\n    - PI3K p85 adaptor (molecular\
    \ player: PI3K p85 adaptor family/ortholog group)"
  module_connections: '- EGF ligand binds EGFR causes GRB2/SOS adaptor recruitment:
    The initiating event promotes grb2/sos adaptor recruitment.

    - GRB2/SOS adaptor recruitment causes MAPK/PI3K transcriptional output: GRB2/SOS
    adaptor recruitment leads to mapk/pi3k transcriptional output.'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 41
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: egfr_signaling-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: egfr_signaling-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Commissioned Review Brief

## Review Topic

EGFR signaling pathway module

## Working Scope

EGF-family ligand binding activates EGFR/ERBB1 receptor tyrosine kinase dimers, creating phosphotyrosine docking sites that recruit GRB2/SOS, PI3K, PLCG, and STAT branches for proliferation and differentiation outputs.

## Provisional Biological Outline

- EGFR signaling pathway
  - 1. egf ligand binds egfr
  - EGF ligand binds EGFR
    - EGF ligand (molecular player: EGF; activity or role: signaling receptor binding)
    - EGFR receptor (molecular player: EGFR receptor family/ortholog group; activity or role: transmembrane receptor protein tyrosine kinase activity)
  - 2. grb2/sos adaptor recruitment
  - GRB2/SOS adaptor recruitment
    - GRB2 adaptor (molecular player: GRB2 adaptor family/ortholog group)
    - SOS1 Ras GEF (molecular player: SOS1; activity or role: guanyl-nucleotide exchange factor activity)
  - 3. mapk/pi3k transcriptional output
  - MAPK/PI3K transcriptional output
    - ERBB2 paralogous RTK context (molecular player: ERBB2 paralogous RTK context family/ortholog group; activity or role: transmembrane receptor protein tyrosine kinase activity)
    - PI3K p85 adaptor (molecular player: PI3K p85 adaptor family/ortholog group)

## Known Relationships Among Steps

- EGF ligand binds EGFR causes GRB2/SOS adaptor recruitment: The initiating event promotes grb2/sos adaptor recruitment.
- GRB2/SOS adaptor recruitment causes MAPK/PI3K transcriptional output: GRB2/SOS adaptor recruitment leads to mapk/pi3k transcriptional output.

## Assignment

Write a rigorous, review-style synthesis suitable for a molecular biology
audience. Treat the topic as a biological system whose boundaries, core
mechanisms, variants, and unresolved points should be made clear to readers who
know the field but are not specialists in this specific process.

The review should be explanatory rather than encyclopedic. Anchor broad claims
in primary literature or authoritative reviews, but keep the focus on how the
system works and how its parts fit together.

## Questions To Address

1. **Scope and boundaries**
   - What exactly is included in this biological system?
   - Which neighboring pathways, organelle processes, complexes, or regulatory
     events are often confused with it but should be treated separately?
   - Are there competing definitions in the literature?

2. **Core mechanism**
   - What is the best current model for the sequence of events?
   - Which steps are obligatory, which are conditional, and which are accessory?
   - What molecular assemblies, enzymes, receptors, adaptors, transporters, or
     structural units carry out each major step?

3. **Variation**
   - How does the system vary across major evolutionary lineages?
   - Are there well-supported differences between cell types, tissues,
     developmental stages, physiological states, or compartments?
   - Where are there alternative routes that achieve a similar outcome by
     different molecular means?

4. **Conservation and origin**
   - What is the deepest plausible evolutionary origin of the system?
   - Which parts appear ancient and conserved, and which appear to be later
     elaborations, replacements, or lineage-specific losses?
   - When a protein family has expanded, which family members are the best
     representatives for understanding the ancestral role?

5. **Physical and biological constraints**
   - What steps must occur in a particular order?
   - Which events are mutually exclusive, compartment-specific, cell-type
     specific, substrate-specific, or stage-specific?
   - What evidence rules out otherwise plausible paths through the system?

6. **Evidence and controversy**
   - Which mechanistic claims are strongly supported by experiments?
   - Where does the literature disagree, rely on indirect evidence, or mix data
     from organisms that may not be comparable?
   - What are the most important open questions?

## Output Format

Use the style and structure of a concise review article:

1. Executive summary
2. Definition and biological boundaries
3. Mechanistic overview
4. Major molecular players and active assemblies
5. Evolutionary and cell-biological variation
6. Constraints, dependencies, and failure modes
7. Controversies and open questions
8. Key references

Include citations for major claims, preferably PMIDs or DOIs. Be explicit about
uncertainty and avoid overgeneralizing from one organism, cell type, or assay
system to all biology.

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

# Commissioned Review Brief

## Review Topic

EGFR signaling pathway module

## Working Scope

EGF-family ligand binding activates EGFR/ERBB1 receptor tyrosine kinase dimers, creating phosphotyrosine docking sites that recruit GRB2/SOS, PI3K, PLCG, and STAT branches for proliferation and differentiation outputs.

## Provisional Biological Outline

- EGFR signaling pathway
  - 1. egf ligand binds egfr
  - EGF ligand binds EGFR
    - EGF ligand (molecular player: EGF; activity or role: signaling receptor binding)
    - EGFR receptor (molecular player: EGFR receptor family/ortholog group; activity or role: transmembrane receptor protein tyrosine kinase activity)
  - 2. grb2/sos adaptor recruitment
  - GRB2/SOS adaptor recruitment
    - GRB2 adaptor (molecular player: GRB2 adaptor family/ortholog group)
    - SOS1 Ras GEF (molecular player: SOS1; activity or role: guanyl-nucleotide exchange factor activity)
  - 3. mapk/pi3k transcriptional output
  - MAPK/PI3K transcriptional output
    - ERBB2 paralogous RTK context (molecular player: ERBB2 paralogous RTK context family/ortholog group; activity or role: transmembrane receptor protein tyrosine kinase activity)
    - PI3K p85 adaptor (molecular player: PI3K p85 adaptor family/ortholog group)

## Known Relationships Among Steps

- EGF ligand binds EGFR causes GRB2/SOS adaptor recruitment: The initiating event promotes grb2/sos adaptor recruitment.
- GRB2/SOS adaptor recruitment causes MAPK/PI3K transcriptional output: GRB2/SOS adaptor recruitment leads to mapk/pi3k transcriptional output.

## Assignment

Write a rigorous, review-style synthesis suitable for a molecular biology
audience. Treat the topic as a biological system whose boundaries, core
mechanisms, variants, and unresolved points should be made clear to readers who
know the field but are not specialists in this specific process.

The review should be explanatory rather than encyclopedic. Anchor broad claims
in primary literature or authoritative reviews, but keep the focus on how the
system works and how its parts fit together.

## Questions To Address

1. **Scope and boundaries**
   - What exactly is included in this biological system?
   - Which neighboring pathways, organelle processes, complexes, or regulatory
     events are often confused with it but should be treated separately?
   - Are there competing definitions in the literature?

2. **Core mechanism**
   - What is the best current model for the sequence of events?
   - Which steps are obligatory, which are conditional, and which are accessory?
   - What molecular assemblies, enzymes, receptors, adaptors, transporters, or
     structural units carry out each major step?

3. **Variation**
   - How does the system vary across major evolutionary lineages?
   - Are there well-supported differences between cell types, tissues,
     developmental stages, physiological states, or compartments?
   - Where are there alternative routes that achieve a similar outcome by
     different molecular means?

4. **Conservation and origin**
   - What is the deepest plausible evolutionary origin of the system?
   - Which parts appear ancient and conserved, and which appear to be later
     elaborations, replacements, or lineage-specific losses?
   - When a protein family has expanded, which family members are the best
     representatives for understanding the ancestral role?

5. **Physical and biological constraints**
   - What steps must occur in a particular order?
   - Which events are mutually exclusive, compartment-specific, cell-type
     specific, substrate-specific, or stage-specific?
   - What evidence rules out otherwise plausible paths through the system?

6. **Evidence and controversy**
   - Which mechanistic claims are strongly supported by experiments?
   - Where does the literature disagree, rely on indirect evidence, or mix data
     from organisms that may not be comparable?
   - What are the most important open questions?

## Output Format

Use the style and structure of a concise review article:

1. Executive summary
2. Definition and biological boundaries
3. Mechanistic overview
4. Major molecular players and active assemblies
5. Evolutionary and cell-biological variation
6. Constraints, dependencies, and failure modes
7. Controversies and open questions
8. Key references

Include citations for major claims, preferably PMIDs or DOIs. Be explicit about
uncertainty and avoid overgeneralizing from one organism, cell type, or assay
system to all biology.

# The EGFR Signaling Pathway Module: From Ligand Binding to Transcriptional Output

## 1. Executive Summary

The epidermal growth factor receptor (EGFR/ERBB1) signaling pathway constitutes one of the most intensively studied signal transduction cascades in cell biology. At its core, the module operates through a three-step logic: (i) EGF-family ligand binding activates EGFR receptor tyrosine kinase dimers; (ii) autophosphorylation of the receptor C-terminal tail creates phosphotyrosine docking sites; and (iii) recruited adaptors—principally GRB2/SOS1, PI3K, PLCγ, and STAT proteins—relay signals to downstream RAS-MAPK and PI3K-AKT cascades that drive proliferation, differentiation, survival, and migration outputs. This review synthesizes current understanding of the pathway's boundaries, the obligatory sequence of molecular events from ligand engagement through transcriptional output, the variation of this system across tissues and evolutionary lineages, and the most important unresolved questions. Emphasis is placed on recent advances, including the role of GRB2 biomolecular condensates in RAS activation, allosteric mechanisms governing SOS1 catalysis, ligand-bias phenomena that produce distinct signaling outputs from the same receptor, and the emerging significance of EGFR oligomerization beyond canonical dimers.

---

## 2. Definition and Biological Boundaries

### 2.1 What the Module Includes

The EGFR signaling pathway module, as defined here, encompasses the events from extracellular ligand–receptor engagement through the generation of activated RAS-GTP and PI3K-generated PIP3 at the plasma membrane. The core components include: (a) seven EGF-family ligands (EGF, TGF-α, HB-EGF, betacellulin, amphiregulin, epiregulin, and epigen); (b) the four ERBB-family receptors (EGFR/ERBB1, ERBB2/HER2, ERBB3/HER3, ERBB4/HER4), which function as homo- and heterodimeric signaling units; and (c) the immediate cytoplasmic effector layer including GRB2, SOS1, PI3K (p85/p110), PLCγ1, STAT3, and CBL (tito2025egfreceptorin pages 2-4, tito2025egfreceptorin pages 1-2).

### 2.2 What Should Be Treated Separately

Several processes are closely connected to EGFR signaling but are best considered as distinct modules. Endosomal sorting and lysosomal degradation of EGFR represent a trafficking/downregulation module that attenuates signaling rather than constituting the signal itself (schultz2023egfrtraffickingeffect pages 3-5). The downstream RAF-MEK-ERK cascade, while directly engaged by EGFR-activated RAS, is shared with numerous other receptor systems and constitutes its own regulatory module with scaffold proteins such as KSR1. Similarly, the PI3K-AKT-mTOR axis below the level of PIP3 generation serves as a common effector module for many upstream inputs. GPCR-mediated transactivation of EGFR, involving ADAM/MMP-dependent ectodomain shedding of EGFR ligands, represents a cross-pathway regulatory mechanism rather than a core component of the EGFR module itself (tito2025egfreceptorin pages 2-4).

---

## 3. Mechanistic Overview

### 3.1 Step 1: EGF Ligand Binding and Receptor Activation

EGFR is a 170-kDa single-pass transmembrane glycoprotein whose extracellular domain (ECD) comprises four subdomains (I–IV). In the quiescent state, the ECD adopts a closed, autoinhibited conformation in which the ligand-binding pocket (formed between domains I and III) is disrupted and the dimerization arm (domain II) is buried through intramolecular interactions with domain IV (kovacs2022ittakesmore pages 2-4). Ligand binding to domains I and III triggers a large-scale conformational rearrangement that exposes the dimerization arm, enabling intermolecular bridge formation between two receptor monomers (kovacs2022ittakesmore pages 4-5, schultz2023egfrtraffickingeffect pages 1-2).

This dimerization propagates across the membrane through GxxxG-like motifs in the transmembrane domain (TMD), causing the juxtamembrane (JM) segment to dissociate from membrane phospholipids. The intracellular kinase domains then form an asymmetric dimer in which one kinase domain (the "activator") allosterically activates its partner (the "receiver") in a cyclin-like mechanism (kovacs2022ittakesmore pages 4-5, schultz2023egfrtraffickingeffect pages 2-3). A notable feature distinguishing EGFR from most other kinases is that phosphorylation of the kinase domain itself is dispensable for activation—the asymmetric dimer interface alone is sufficient to convert the receiver kinase to an active conformation (kovacs2022ittakesmore pages 4-5).

Autophosphorylation then occurs at five key C-terminal tyrosine residues: Tyr992, Tyr1045, Tyr1068, Tyr1086, and Tyr1173 (martinfernandez2022fluorescenceimagingof pages 4-5). These phosphotyrosines serve as docking sites for SH2- and PTB-domain-containing effectors, with pY1068 and pY1173 being major GRB2 recruitment sites, and pY1045 serving as a direct CBL binding site that initiates receptor downregulation (tito2025egfreceptorin pages 2-4, wang2024theconfigurationof pages 9-11).

### 3.2 Step 2: GRB2/SOS1 Adaptor Recruitment

The adaptor protein GRB2 is a 25-kDa non-enzymatic protein comprising a central SH2 domain flanked by N-terminal and C-terminal SH3 domains. The SH2 domain recognizes pYxNx motifs on activated EGFR (primarily pY1068 and pY1173), tethering GRB2 to the receptor at the plasma membrane (wang2024theconfigurationof pages 1-2, wang2024theconfigurationof pages 9-11).

GRB2 recruitment of SOS1 proceeds through an allosteric, multistep mechanism. SOS1's C-terminal proline-rich domain (PRD) contains multiple proline-rich motifs (PRMs) that bind both nSH3 and cSH3 domains of GRB2. The current model proposes that SOS1 PRM3 initially engages the nSH3 domain; when the GRB2 SH2 domain binds the phosphorylated receptor, a conformational change releases the cSH3 domain from its intramolecular interaction with SH2, enabling a cooperative nSH3-cSH3 back-to-back interaction that allows cSH3 to engage SOS1 PRM4 (jasemi2022allostericregulationof pages 2-4). This dual-site binding renders the overall GRB2-SOS1 interaction approximately twice as strong as individual domain–peptide interactions (wang2024theconfigurationof pages 14-15). The allosteric regulation ensures that SOS1 recruitment is tightly coupled to receptor activation state rather than occurring constitutively (jasemi2022allostericregulationof pages 1-2).

A recently described layer of regulation involves biomolecular condensate formation. Multivalent interactions between phosphorylated EGFR tails, GRB2 dimers (via an SH2/SH3 dimer interface), and SOS1 proline-rich regions drive the assembly of membrane-associated protein condensates. These condensates are essential for efficient SOS1 autoinhibition release and productive RAS activation. Phosphorylation of GRB2 at Tyr160 disrupts the SH2/SH3 dimer interface, dissolving the condensates and establishing a negative feedback mechanism that limits RAS activation at high kinase activity levels (phan2024grb2phosphorylationantagonizes pages 10-14, phan2024grb2phosphorylationantagonizes pages 8-10, phan2024grb2phosphorylationantagonizes pages 1-4, phan2024grb2phosphorylationantagonizes pages 6-8).

### 3.3 SOS1-Catalyzed RAS Activation

SOS1 is a ~170-kDa multidomain protein that functions as the principal guanine nucleotide exchange factor (GEF) for RAS proteins. In its basal cytosolic state, SOS1 is autoinhibited by N-terminal regulatory domains (histone-fold, DH, and PH domains) that block the allosteric RAS-binding pocket (kamel2026disruptingthekras–sos1 pages 7-8). GRB2-mediated membrane recruitment brings SOS1 into proximity with membrane-anchored RAS-GDP.

The catalytic mechanism involves SOS1's CDC25 domain inserting a helical hairpin between RAS switch I and switch II regions, prying open the nucleotide-binding pocket, destabilizing Mg²⁺ coordination, and facilitating GDP release (kamel2026disruptingthekras–sos1 pages 6-7, kamel2026disruptingthekras–sos1 pages 8-10). A critical positive feedback loop then amplifies signaling: RAS-GTP binding to a distinct allosteric site at the REM-CDC25 interface enhances SOS1's exchange activity at the catalytic site, enabling self-amplifying bursts of RAS activation (kamel2026disruptingthekras–sos1 pages 6-7). This two-site mechanism—catalytic plus allosteric—explains the switch-like behavior of RAS activation downstream of growth factor stimulation.

### 3.4 Step 3: MAPK/PI3K Transcriptional Output

**RAS-MAPK branch:** GTP-loaded RAS engages RAF kinases (RAF1, BRAF, ARAF), initiating the three-tiered MAPK cascade: RAF → MEK1/2 → ERK1/2. Activated ERK translocates to the nucleus where it phosphorylates transcription factors governing proliferation and differentiation programs. Importantly, the dynamics of ERK activation—transient versus sustained—contribute to cell-fate decisions and are modulated by ligand identity, as discussed below (tito2025egfreceptorin pages 2-4, zhou2024newdirectionsfor pages 1-2).

**PI3K branch:** Class IA PI3Ks are heterodimers of a p85 regulatory subunit and a p110 catalytic subunit. The p85 SH2 domains bind phosphotyrosine motifs on activated receptors or adaptors, relieving autoinhibition of p110 and enabling PIP2 → PIP3 conversion at the membrane. While EGFR homodimers can directly recruit PI3K, the most potent PI3K activation occurs through ERBB2-ERBB3 heterodimers, as ERBB3 harbors a cluster of six C-terminal tyrosine-containing motifs that represent consensus p85 binding sites (saddawikonefka2022her2andher3 pages 3-4). This makes the ERBB2-ERBB3 dimer the most potent activator of the PI3K/AKT/mTOR pathway, a relationship with major therapeutic implications in HER2-positive cancers (cheng2024acomprehensivereview pages 3-5, saddawikonefka2022her2andher3 pages 3-4).

**PLCγ and STAT branches:** PLCγ1 is recruited to phosphorylated EGFR via its SH2 domains and hydrolyzes PIP2 to generate diacylglycerol (DAG) and inositol trisphosphate (IP3), linking EGFR to PKC and Ca²⁺ signaling. STAT3 can be activated downstream of EGFR directly or through associated kinases, mediating transcriptional programs linked to survival and inflammation, particularly in intestinal epithelial contexts (tito2025egfreceptorin pages 2-4, tito2025egfreceptorin pages 7-9).

---

## 4. Major Molecular Players and Active Assemblies

The following table provides a comprehensive reference for the molecular components discussed in this review:

| Molecular Player | Gene/Protein Name | Family/Classification | Key Domain(s) | Activity/Role in EGFR Pathway |
|---|---|---|---|---|
| EGF | **EGF** | EGF-family ligand; high-affinity EGFR ligand | EGF-like growth factor domain | Canonical soluble ligand that binds EGFR extracellular domains I and III, promotes receptor opening, dimerization, and robust ERK signaling; generally associated with proliferative outputs (tito2025egfreceptorin pages 2-4) |
| TGF-α | **TGFA** | EGF-family ligand; high-affinity EGFR ligand | EGF-like growth factor domain | Activates EGFR similarly to EGF but can stabilize distinct receptor states and trafficking/signaling outputs; often compared with EGF in ligand-bias studies (kovacs2022ittakesmore pages 4-5, tito2025egfreceptorin pages 2-4) |
| HB-EGF | **HBEGF** | EGF-family ligand; high-affinity EGFR ligand | EGF-like growth factor domain; membrane-anchored precursor with heparin-binding region | Potent EGFR ligand that can signal in juxtacrine/paracrine modes after ectodomain shedding; contributes to strong receptor activation and tissue-specific responses (tito2025egfreceptorin pages 2-4, tito2025egfreceptorin pages 17-19) |
| Betacellulin (BTC) | **BTC** | EGF-family ligand; high-affinity EGFR ligand | EGF-like growth factor domain | EGFR/ERBB ligand with context-dependent developmental roles; in pancreas, supports distinct differentiation programs relative to EGF (tito2025egfreceptorin pages 2-4, tito2025egfreceptorin pages 17-19) |
| Amphiregulin (AREG) | **AREG** | EGF-family ligand; low-affinity EGFR ligand | EGF-like growth factor domain | Lower-affinity ligand often linked to weaker but sustained signaling, stromal/epithelial communication, mammary branching programs, and Treg-associated EGFR responses (tito2025egfreceptorin pages 2-4, tito2025egfreceptorin pages 17-19, tito2025egfreceptorin pages 20-22) |
| Epiregulin (EREG) | **EREG** | EGF-family ligand; low-affinity EGFR ligand | EGF-like growth factor domain | Low-affinity ligand that forms less stable receptor dimers yet can drive sustained ERK signaling and differentiation-biased outputs rather than strong proliferation (tito2025egfreceptorin pages 2-4, zhou2024newdirectionsfor pages 1-2) |
| Epigen (EPGN) | **EPGN** | EGF-family ligand; low-affinity EGFR ligand | EGF-like growth factor domain | Weak/low-affinity EGFR ligand associated with less stable dimers and prolonged signaling kinetics that can favor differentiation programs (tito2025egfreceptorin pages 2-4, zhou2024newdirectionsfor pages 1-2) |
| EGFR / ERBB1 | **EGFR** | ERBB-family receptor tyrosine kinase | Extracellular domains I-IV, dimerization arm in domain II, transmembrane helix, juxtamembrane segment, intracellular kinase domain, C-terminal phosphotyrosine tail | Core receptor of the module. Ligand binding exposes the dimerization arm, promotes homo/heterodimerization, asymmetric kinase dimer formation, and tail autophosphorylation at sites including Y992, Y1045, Y1068, Y1086, Y1173 to recruit effectors (tito2025egfreceptorin pages 2-4, martinfernandez2022fluorescenceimagingof pages 4-5, kovacs2022ittakesmore pages 4-5, kovacs2022ittakesmore pages 2-4) |
| ERBB2 / HER2 | **ERBB2** | ERBB-family orphan co-receptor; catalytically potent heterodimer partner | Extracellular domain in constitutively open-like conformation, transmembrane helix, kinase domain, C-terminal tail | No known soluble ligand; preferred heterodimerization partner for other ERBB receptors. Potentiates signaling, especially with EGFR or HER3; EGFR-HER2 heterodimers can alter trafficking and resist endocytosis relative to EGFR homodimers (cheng2024acomprehensivereview pages 3-5, saddawikonefka2022her2andher3 pages 3-4, mudumbi2024distinctinteractionsstabilize pages 28-30) |
| ERBB3 / HER3 | **ERBB3** | ERBB-family pseudokinase scaffold receptor | Extracellular ligand-binding domains, impaired kinase domain, C-terminal tail with multiple p85-binding motifs | Weak/impaired kinase activity but powerful scaffold. When phosphorylated in heterodimers, especially with HER2, its six C-terminal phosphotyrosine motifs recruit PI3K p85 efficiently, making HER2-HER3 a strong PI3K/AKT activator (cheng2024acomprehensivereview pages 3-5, saddawikonefka2022her2andher3 pages 3-4) |
| ERBB4 / HER4 | **ERBB4** | ERBB-family receptor tyrosine kinase | Extracellular ligand-binding domains, transmembrane helix, kinase domain, C-terminal tail | Ligand-responsive ERBB receptor that can heterodimerize with HER2 or other ERBBs; contributes to context-specific developmental signaling and expands ERBB network diversity beyond the EGFR-centered core module (cheng2024acomprehensivereview pages 3-5) |
| GRB2 adaptor protein | **GRB2** | SH2/SH3 adaptor protein | One central SH2 domain; N-terminal and C-terminal SH3 domains | Binds phosphotyrosine motifs on activated EGFR (notably Y1068/Y1173-associated docking in reviewed sources) through SH2 and recruits SOS1 via SH3-proline-rich interactions; essential linker from EGFR to RAS-MAPK signaling (wang2024theconfigurationof pages 1-2, wang2024theconfigurationof pages 9-11, wang2024theconfigurationof pages 14-15) |
| SOS1 | **SOS1** | RAS guanine nucleotide exchange factor (GEF) | Histone-fold region, DH domain, PH domain, REM domain, CDC25 catalytic domain, proline-rich region | Recruited by GRB2 to the plasma membrane, where it catalyzes GDP release from RAS. SOS1 is autoinhibited in the cytosol and activated by membrane recruitment plus allosteric RAS-GTP binding, amplifying EGFR-to-RAS signaling (jasemi2022allostericregulationof pages 2-4, jasemi2022allostericregulationof pages 1-2, kamel2026disruptingthekras–sos1 pages 7-8, kamel2026disruptingthekras–sos1 pages 6-7) |
| PI3K p85 regulatory subunit | **PIK3R1/PIK3R2** (p85α/p85β) | Class IA PI3K regulatory adaptor | SH2 domains, inter-SH2 region | Binds phosphotyrosine motifs on activated receptors/adaptors, especially HER3 tail motifs, and recruits/stabilizes class IA PI3K catalytic subunits at the membrane to generate PIP3 and activate AKT signaling (cheng2024acomprehensivereview pages 3-5, saddawikonefka2022her2andher3 pages 3-4) |
| PLC-γ1 | **PLCG1** | Phospholipase C effector enzyme | SH2 domains, SH3 domain, PH domain, catalytic X/Y core, C2 domain | Recruited to phosphotyrosine-containing receptor complexes via SH2 interactions and hydrolyzes PIP2 to DAG and IP3, linking EGFR to PKC/Ca2+ signaling branches (tito2025egfreceptorin pages 2-4, schultz2023egfrtraffickingeffect pages 3-5) |
| STAT3 | **STAT3** | Signal transducer and activator of transcription | SH2 domain, DNA-binding domain, transactivation domain | Can be activated downstream of EGFR directly or through associated kinases; mediates transcriptional programs linked to survival, inflammation, and oncogenic signaling in specific tissues and disease contexts (tito2025egfreceptorin pages 2-4, tito2025egfreceptorin pages 7-9) |
| CBL | **CBL** | RING-type E3 ubiquitin ligase | TKB/PTB-like phosphotyrosine-binding module, RING finger, proline-rich region | Binds activated EGFR directly or via GRB2-associated complexes (classically around Y1045-linked recruitment), promoting receptor ubiquitination, endocytosis, and lysosomal downregulation (tito2025egfreceptorin pages 2-4, wang2024theconfigurationof pages 14-15) |
| RAS proteins | **KRAS, HRAS, NRAS** | Small GTPases | G-domain with switch I/II regions; C-terminal membrane-targeting motif | Molecular switch immediately downstream of SOS1. GTP-loaded RAS activates RAF and other effectors to propagate EGFR signals into MAPK and related outputs (jasemi2022allostericregulationof pages 1-2, kamel2026disruptingthekras–sos1 pages 7-8, kamel2026disruptingthekras–sos1 pages 8-10) |
| RAF-MEK-ERK cascade | **RAF1/BRAF/ARAF → MAP2K1/2 (MEK1/2) → MAPK1/3 (ERK2/1)** | MAPK kinase cascade | Ser/Thr kinase domains; scaffold-binding regions | Principal transcriptional output arm downstream of EGFR-GRB2-SOS1-RAS. Drives proliferation, differentiation, and context-dependent fate decisions; sustained vs transient ERK dynamics contribute to ligand bias (kemmer2022disentanglingerbbsignaling pages 17-18, tito2025egfreceptorin pages 2-4, zhou2024newdirectionsfor pages 1-2) |
| AKT / PKB | **AKT1/AKT2/AKT3** | AGC-family serine/threonine kinase | N-terminal PH domain, kinase domain, hydrophobic motif tail | Major effector of the PI3K branch. Recruited to PIP3-rich membrane regions and activated downstream of EGFR/ERBB-PI3K signaling to support cell survival, metabolism, growth, and therapy resistance (kemmer2022disentanglingerbbsignaling pages 17-18, cheng2024acomprehensivereview pages 3-5, saddawikonefka2022her2andher3 pages 3-4) |


*Table: This table summarizes the main ligands, receptors, adaptors, and downstream effectors in the EGFR signaling module, with emphasis on how each component contributes to receptor activation and signal propagation. It is useful as a compact reference for the review’s mechanistic sections and for distinguishing core from context-dependent components.*

### 4.1 The ERBB Receptor Combinatorial Code

A distinctive feature of the mammalian EGFR signaling module is its combinatorial receptor logic. ERBB2/HER2 is unique in lacking an endogenous ligand but adopting a constitutively open extracellular conformation, making it the preferred heterodimerization partner for all other ERBB family members (saddawikonefka2022her2andher3 pages 3-4). ERBB3/HER3 possesses impaired kinase activity but serves as the most effective scaffold for PI3K recruitment, containing six p85-binding phosphotyrosine sites on its C-terminal tail (saddawikonefka2022her2andher3 pages 3-4). Consequently, the identity of the dimerization partner profoundly influences downstream pathway preference: EGFR homodimers favor RAS-MAPK activation; ERBB2-ERBB3 heterodimers preferentially drive PI3K-AKT signaling; and EGFR-ERBB2 heterodimers show enhanced signaling potency and altered endocytic trafficking relative to EGFR homodimers (kemmer2022disentanglingerbbsignaling pages 17-18, cheng2024acomprehensivereview pages 3-5).

Mathematical modeling of ERBB signaling across breast cancer subtypes has demonstrated that the intracellular signal transduction network is largely conserved between different cell types, with clinical differences arising primarily from receptor expression levels and specific mutations in downstream components such as PIK3CA (kemmer2022disentanglingerbbsignaling pages 17-18).

---

## 5. Evolutionary and Cell-Biological Variation

### 5.1 Evolutionary Conservation

EGFR signaling is an ancient metazoan innovation. The pathway is conserved across bilaterian animals but appears absent from placozoans and cnidarians, with the planarian *Schmidtea mediterranea* representing the earliest known organism with a functional EGFR signaling system (kniazkina2023doesegfrsignaling pages 2-4). In invertebrate model organisms, a single EGFR ortholog mediates diverse developmental functions: LET-23 in *C. elegans* is essential for vulval induction (induced by the LIN-3 ligand), while DER/Torpedo in *Drosophila melanogaster* responds to multiple ligands (Spitz, Gurken, Vein, Keren) and controls a wide range of developmental and physiological processes (kniazkina2023doesegfrsignaling pages 2-4, kniazkina2023doesegfrsignaling pages 12-14). The downstream RTK-RAS-MAPK axis is described as one of the most highly conserved intracellular signaling cascades (jasemi2022allostericregulationof pages 1-2).

The vertebrate lineage underwent a major expansion, giving rise to four ERBB family receptors and at least seven EGF-family ligands. This expansion enabled increased combinatorial signaling complexity through receptor heterodimerization—a feature largely absent in invertebrate systems with their single EGFR orthologs (kniazkina2023doesegfrsignaling pages 2-4).

| Organism/Taxon | EGFR Ortholog(s) | Number of ERBB-family Receptors | Known Ligands | Key Developmental/Physiological Roles | Key References |
|---|---|---:|---|---|---|
| Placozoa and Cnidaria | No canonical EGFR/ERBB system reported | 0 | Not applicable | Comparative surveys cited in the available review note apparent absence of the EGFR signaling system in these early-branching animal lineages, setting a lower bound on the origin of the pathway after these branches | (kniazkina2023doesegfrsignaling pages 2-4) |
| Planarians (*Schmidtea mediterranea*) | Planarian EGFR-family receptor(s) reported; specific receptor names not given in the available context | At least 1 | EGF-like ligands present in the system, but specific ligand names not provided in the available context | Earliest known animal example in the available review; EGFR signaling implicated in gut progenitor differentiation and regenerative/developmental control | (kniazkina2023doesegfrsignaling pages 2-4, kniazkina2023doesegfrsignaling pages 12-14) |
| *Caenorhabditis elegans* | LET-23 | 1 | LIN-3 | Essential for vulval induction; also participates in neuronal/sleep-regulatory physiology through conserved EGFR signaling logic | (kniazkina2023doesegfrsignaling pages 2-4, kniazkina2023doesegfrsignaling pages 12-14) |
| *Drosophila melanogaster* | DER / Torpedo | 1 | Spitz, Gurken, Vein, Keren | Controls diverse developmental and physiological processes; the available context specifically notes roles in sleep consolidation/maintenance and broad developmental regulation typical of the fly EGFR pathway | (kniazkina2023doesegfrsignaling pages 2-4, kniazkina2023doesegfrsignaling pages 12-14) |
| Vertebrates / Mammals | EGFR/ERBB1, ERBB2/HER2, ERBB3/HER3, ERBB4/HER4 | 4 | Expanded EGF-family ligand set; at least 7 ligands commonly recognized, including EGF, TGF-α, HB-EGF, BTC, AREG, EREG, and EPGN | Expanded receptor-ligand combinatorics enable increased signaling complexity in development, tissue homeostasis, regeneration, immunity, and disease; heterodimer specialization (for example HER2-HER3 and EGFR-HER2) is a major vertebrate elaboration | (kniazkina2023doesegfrsignaling pages 2-4, cheng2024acomprehensivereview pages 3-5, saddawikonefka2022her2andher3 pages 3-4, tito2025egfreceptorin pages 1-2) |


*Table: This table summarizes how EGFR/ERBB signaling is conserved and elaborated across major animal lineages, from single-receptor invertebrate systems to the four-receptor vertebrate ERBB network. It is useful for distinguishing ancient core features from later vertebrate expansions in receptor and ligand complexity.*

### 5.2 Cell-Type and Tissue Variation

EGFR is expressed in epithelial, mesenchymal, bone, immune, cardiac, glial, and neural stem cells, with its activity level and downstream impact varying significantly across tissues (tito2025egfreceptorin pages 1-2). The review by Tito et al. (2025) provides the most comprehensive recent account of organ-specific EGFR functions:

- **Intestine:** EGFR maintains epithelial homeostasis by suppressing pathological cell shedding, promoting mitochondrial biogenesis, and coordinating with Notch and WNT pathways for regeneration (tito2025egfreceptorin pages 7-9, tito2025egfreceptorin pages 5-7).
- **Liver:** EGFR regulates hepatocyte regeneration and fat metabolism; its altered expression is linked to NAFLD and hepatocellular carcinoma (tito2025egfreceptorin pages 11-12).
- **Bone:** EGFR regulates osteoblast maturation through mTOR inhibition and ERK phosphorylation during ossification; in cartilage, it balances anabolic and catabolic processes (tito2025egfreceptorin pages 11-12).
- **Mammary gland:** Different EGFR ligands drive distinct cell fates—low-affinity AREG promotes luminal differentiation, while high-affinity EGF drives myoepithelial differentiation through differential ERK dynamics (tito2025egfreceptorin pages 20-22).
- **Pancreas:** EGF and BTC activate distinct programs controlling β-cell commitment and differentiation (tito2025egfreceptorin pages 17-19).
- **Immune system:** EGFR has distinct roles across T cell subsets: AREG/EGFR enhances Treg suppressive activity; HB-EGF/EGFR promotes IL-2 production in CD4+ cells; and EGFR expression enhances anti-tumor activity in CD8+ cytotoxic T cells (tito2025egfreceptorin pages 17-19).
- **Placenta:** EGFR promotes trophoblast invasion and angiogenesis through MMP9/MMP2 activation; its dysregulation under hypoxia contributes to preeclampsia (tito2025egfreceptorin pages 5-7, tito2025egfreceptorin pages 4-5).
- **Kidney:** EGFR regulates renal electrolyte homeostasis under normal conditions but promotes myofibroblast proliferation and fibrosis following injury (tito2025egfreceptorin pages 20-22).

---

## 6. Constraints, Dependencies, and Failure Modes

### 6.1 Obligatory Ordering of Events

The signaling cascade follows a strict sequential logic: ligand binding → conformational opening of ECD → dimerization → asymmetric kinase dimer formation → C-terminal phosphorylation → adaptor recruitment → downstream activation. Ligand binding is obligatory for wild-type EGFR activation under physiological conditions, although overexpression can promote ligand-independent oligomerization and constitutive phosphorylation (schultz2023egfrtraffickingeffect pages 3-5, schultz2023egfrtraffickingeffect pages 2-3). The asymmetric kinase dimer is required before transphosphorylation can occur, and phosphorylation of the kinase domain itself is dispensable—a constraint that distinguishes EGFR from most kinases (kovacs2022ittakesmore pages 4-5).

### 6.2 Ligand Bias: Different Inputs, Different Outputs

A critical constraint on pathway output is ligand identity. EGF-family ligands are classified as high-affinity (EGF, TGF-α, HB-EGF, BTC) or low-affinity (AREG, EREG, EPGN). Low-affinity ligands form less stable receptor dimers but paradoxically produce more sustained ERK activation, favoring differentiation over proliferation (tito2025egfreceptorin pages 2-4, zhou2024newdirectionsfor pages 1-2). This ligand-bias phenomenon operates through differential receptor dimer conformations and distinct intracellular trafficking routes—stable EGF-EGFR complexes are rapidly internalized and degraded, while AREG-EGFR complexes undergo recycling that prolongs signaling duration. EGFR ligand concentration can functionally switch EGFR from oncogenic to tumor-suppressive roles (zhou2024newdirectionsfor pages 1-2).

### 6.3 Negative Regulation and Pathway Termination

Multiple mechanisms ensure signal termination. CBL-mediated ubiquitination of EGFR (recruited primarily via pY1045) promotes receptor endocytosis and lysosomal degradation (tito2025egfreceptorin pages 2-4). GRB2 can alternately bind CBL through its nSH3 domain, sequestering GRB2 from SOS1 and inhibiting RAS activation (wang2024theconfigurationof pages 14-15). The recently described GRB2 Y160 phosphorylation provides an additional negative feedback: at high kinase activity, phosphorylation of GRB2 disrupts the SH2/SH3 dimer interface, dissolves EGFR-GRB2-SOS1 condensates, and dampens RAS activation in a dose-dependent manner (phan2024grb2phosphorylationantagonizes pages 10-14, phan2024grb2phosphorylationantagonizes pages 8-10).

### 6.4 Failure Modes in Disease

Oncogenic EGFR alterations include activating mutations (e.g., L858R, exon 19 deletions) that promote ligand-independent dimerization and constitutive kinase activation; gene amplification leading to receptor overexpression and oligomerization; and truncation mutants (e.g., EGFRvIII) that lack portions of the ECD but retain signaling capacity through mechanisms that challenge the canonical activation model (schultz2023egfrtraffickingeffect pages 2-3). Resistance to tyrosine kinase inhibitors (TKIs) frequently involves secondary mutations (T790M, C797S), activation of alternative RTKs, or downstream mutations in PIK3CA or RAS family genes (zhou2024newdirectionsfor pages 1-2, kemmer2022disentanglingerbbsignaling pages 17-18).

---

## 7. Controversies and Open Questions

### 7.1 Full-Length EGFR Structure

Despite decades of structural work, the full-length EGFR structure has not been experimentally determined. Current understanding is based primarily on crystal structures of individual domains, and how the extracellular, transmembrane, juxtamembrane, kinase, and C-terminal regions coordinate in an intact receptor remains a major gap (schultz2023egfrtraffickingeffect pages 2-3).

### 7.2 Oligomerization Beyond Dimers

Growing evidence indicates that EGFR forms higher-order oligomers beyond the canonical dimer, and that these oligomeric assemblies are required for efficient signaling. Single-particle tracking studies show that EGF-induced EGFR slow-down requires formation of higher-order oligomers mediated in part by the intracellular kinase domain in its active conformation (mudumbi2024distinctinteractionsstabilize pages 28-30). Transdimer phosphorylation within tetrameric or larger complexes may be required for efficient C-terminal tail phosphorylation (kovacs2022ittakesmore pages 7-8). The relationship between oligomerization state and drug resistance is an active area of investigation, with drug-resistant EGFR mutants exhibiting higher oligomerization (schultz2023egfrtraffickingeffect pages 3-5).

### 7.3 Endosomal Signaling

Whether EGFR continues to signal productively after internalization into endosomes, or whether signaling is primarily a plasma-membrane event, remains debated. The extent to which endosomal versus surface signaling contributes to physiological outputs has important implications for therapeutic strategies targeting receptor trafficking (schultz2023egfrtraffickingeffect pages 3-5).

### 7.4 Kinase-Independent Functions

EGFR has been reported to possess kinase-independent pro-survival functions in cancer cells. Ligand-free EGFR overexpression can activate IRF3 independently of ERK or AKT, and clinical EGFRs lacking extracellular domains challenge the canonical ligand-dependent activation model (schultz2023egfrtraffickingeffect pages 2-3).

### 7.5 Condensate-Dependent RAS Activation

The discovery that GRB2-SOS1-EGFR condensates are required for efficient SOS1 autoinhibition release and RAS activation represents a paradigm shift in understanding signal propagation. However, the in vivo relevance of these condensates, their regulation by cellular context, and their relationship to oncogenic RTK fusions that sequester GRB2 in cytoplasmic condensates require further investigation (phan2024grb2phosphorylationantagonizes pages 1-4, wang2024theconfigurationof pages 5-7).

### 7.6 SOS1 as a Therapeutic Target

SOS1 has emerged as a promising upstream node for KRAS pathway suppression. Multiple SOS1 inhibitors (BI-3406, MRTX0902, BAY-293) are in preclinical and clinical development, acting as KRAS-SOS1 protein-protein interaction disruptors. These agents show particular promise in combination with KRAS(G12C) inhibitors and MEK inhibitors, as SOS1 inhibition attenuates the adaptive feedback reactivation that limits monotherapy efficacy (kamel2026disruptingthekras–sos1 pages 6-7, kamel2026disruptingthekras–sos1 pages 1-2, kamel2026disruptingthekras–sos1 pages 4-6).

---

## 8. Key References

The primary sources supporting this review include:

- Tito C et al. (2025) "EGF receptor in organ development, tissue homeostasis and regeneration." *Journal of Biomedical Science* 32. DOI: 10.1186/s12929-025-01119-9 (tito2025egfreceptorin pages 2-4, tito2025egfreceptorin pages 1-2)
- Kovacs T et al. (2022) "It Takes More than Two to Tango: Complex, Hierarchal, and Membrane-Modulated Interactions in the Regulation of Receptor Tyrosine Kinases." *Cancers* 14:944. DOI: 10.3390/cancers14040944 (kovacs2022ittakesmore pages 4-5, kovacs2022ittakesmore pages 2-4)
- Schultz DF et al. (2023) "EGFR trafficking: effect of dimerization, dynamics, and mutation." *Frontiers in Oncology* 13. DOI: 10.3389/fonc.2023.1258371 (schultz2023egfrtraffickingeffect pages 2-3, schultz2023egfrtraffickingeffect pages 3-5)
- Wang D et al. (2024) "The Configuration of GRB2 in Protein Interaction and Signal Transduction." *Biomolecules* 14:259. DOI: 10.3390/biom14030259 (wang2024theconfigurationof pages 1-2, wang2024theconfigurationof pages 9-11, wang2024theconfigurationof pages 14-15)
- Jasemi NS & Ahmadian MR (2022) "Allosteric regulation of GRB2 modulates RAS activation." *Small GTPases* 13:282-286. DOI: 10.1080/21541248.2022.2089001 (jasemi2022allostericregulationof pages 2-4, jasemi2022allostericregulationof pages 1-2)
- Phan HT et al. (2024) "Grb2 Phosphorylation Antagonizes EGFR-driven Ras Activation by Interfering with Condensate Assembly." *bioRxiv*. DOI: 10.1101/2024.09.05.611544 (phan2024grb2phosphorylationantagonizes pages 10-14, phan2024grb2phosphorylationantagonizes pages 8-10, phan2024grb2phosphorylationantagonizes pages 1-4)
- Saddawi-Konefka R et al. (2022) "HER2 and HER3 as Therapeutic Targets in Head and Neck Cancer." *Cancer Journal* 28:339-345. DOI: 10.1097/ppo.0000000000000622 (saddawikonefka2022her2andher3 pages 3-4)
- Cheng X (2024) "A Comprehensive Review of HER2 in Cancer Biology and Therapeutics." *Genes* 15:903. DOI: 10.3390/genes15070903 (cheng2024acomprehensivereview pages 3-5)
- Kemmer S et al. (2022) "Disentangling ERBB Signaling in Breast Cancer Subtypes—A Model-Based Analysis." *Cancers* 14:2379. DOI: 10.3390/cancers14102379 (kemmer2022disentanglingerbbsignaling pages 17-18)
- Kniazkina M & Dyachuk V (2023) "Does EGFR Signaling Mediate Orexin System Activity in Sleep Initiation?" *Int J Mol Sci* 24:9505. DOI: 10.3390/ijms24119505 (kniazkina2023doesegfrsignaling pages 2-4, kniazkina2023doesegfrsignaling pages 12-14)
- Zhou Y et al. (2024) "New Directions for Advanced Targeting Strategies of EGFR Signaling in Cancer." *Biol Pharm Bull* 47:895-903. DOI: 10.1248/bpb.b23-00924 (zhou2024newdirectionsfor pages 1-2)
- Mudumbi KC et al. (2024) "Distinct interactions stabilize EGFR dimers and higher-order oligomers in cell membranes." *bioRxiv*. DOI: 10.1101/2023.04.10.536273 (mudumbi2024distinctinteractionsstabilize pages 28-30)
- Martin-Fernandez ML (2022) "Fluorescence Imaging of EGFR TKI Resistance in NSCLC." *Cancers* 14:686. DOI: 10.3390/cancers14030686 (martinfernandez2022fluorescenceimagingof pages 4-5)
- Kamel EM et al. (2026) "Disrupting the KRAS–SOS1 protein–protein interaction." *Frontiers in Chemistry* 14. DOI: 10.3389/fchem.2026.1808601 (kamel2026disruptingthekras–sos1 pages 7-8, kamel2026disruptingthekras–sos1 pages 6-7, kamel2026disruptingthekras–sos1 pages 8-10)

References

1. (tito2025egfreceptorin pages 2-4): Claudia Tito, Silvia Masciarelli, Gianni Colotti, and Francesco Fazi. Egf receptor in organ development, tissue homeostasis and regeneration. Journal of Biomedical Science, Feb 2025. URL: https://doi.org/10.1186/s12929-025-01119-9, doi:10.1186/s12929-025-01119-9. This article has 122 citations and is from a domain leading peer-reviewed journal.

2. (tito2025egfreceptorin pages 1-2): Claudia Tito, Silvia Masciarelli, Gianni Colotti, and Francesco Fazi. Egf receptor in organ development, tissue homeostasis and regeneration. Journal of Biomedical Science, Feb 2025. URL: https://doi.org/10.1186/s12929-025-01119-9, doi:10.1186/s12929-025-01119-9. This article has 122 citations and is from a domain leading peer-reviewed journal.

3. (schultz2023egfrtraffickingeffect pages 3-5): Destiny F. Schultz, Daniel D. Billadeau, and Seetharama D. Jois. Egfr trafficking: effect of dimerization, dynamics, and mutation. Frontiers in Oncology, Sep 2023. URL: https://doi.org/10.3389/fonc.2023.1258371, doi:10.3389/fonc.2023.1258371. This article has 46 citations.

4. (kovacs2022ittakesmore pages 2-4): Tamas Kovacs, Florina Zakany, and Peter Nagy. It takes more than two to tango: complex, hierarchal, and membrane-modulated interactions in the regulation of receptor tyrosine kinases. Cancers, 14:944, Feb 2022. URL: https://doi.org/10.3390/cancers14040944, doi:10.3390/cancers14040944. This article has 39 citations.

5. (kovacs2022ittakesmore pages 4-5): Tamas Kovacs, Florina Zakany, and Peter Nagy. It takes more than two to tango: complex, hierarchal, and membrane-modulated interactions in the regulation of receptor tyrosine kinases. Cancers, 14:944, Feb 2022. URL: https://doi.org/10.3390/cancers14040944, doi:10.3390/cancers14040944. This article has 39 citations.

6. (schultz2023egfrtraffickingeffect pages 1-2): Destiny F. Schultz, Daniel D. Billadeau, and Seetharama D. Jois. Egfr trafficking: effect of dimerization, dynamics, and mutation. Frontiers in Oncology, Sep 2023. URL: https://doi.org/10.3389/fonc.2023.1258371, doi:10.3389/fonc.2023.1258371. This article has 46 citations.

7. (schultz2023egfrtraffickingeffect pages 2-3): Destiny F. Schultz, Daniel D. Billadeau, and Seetharama D. Jois. Egfr trafficking: effect of dimerization, dynamics, and mutation. Frontiers in Oncology, Sep 2023. URL: https://doi.org/10.3389/fonc.2023.1258371, doi:10.3389/fonc.2023.1258371. This article has 46 citations.

8. (martinfernandez2022fluorescenceimagingof pages 4-5): Marisa L. Martin-Fernandez. Fluorescence imaging of epidermal growth factor receptor tyrosine kinase inhibitor resistance in non-small cell lung cancer. Cancers, 14:686, Jan 2022. URL: https://doi.org/10.3390/cancers14030686, doi:10.3390/cancers14030686. This article has 8 citations.

9. (wang2024theconfigurationof pages 9-11): Dingyi Wang, Guoxia Liu, Yuxin Meng, Hongjie Chen, Zu Ye, and Ji Jing. The configuration of grb2 in protein interaction and signal transduction. Biomolecules, 14:259, Feb 2024. URL: https://doi.org/10.3390/biom14030259, doi:10.3390/biom14030259. This article has 55 citations.

10. (wang2024theconfigurationof pages 1-2): Dingyi Wang, Guoxia Liu, Yuxin Meng, Hongjie Chen, Zu Ye, and Ji Jing. The configuration of grb2 in protein interaction and signal transduction. Biomolecules, 14:259, Feb 2024. URL: https://doi.org/10.3390/biom14030259, doi:10.3390/biom14030259. This article has 55 citations.

11. (jasemi2022allostericregulationof pages 2-4): Neda S. Kazemein Jasemi and M. Reza Ahmadian. Allosteric regulation of grb2 modulates ras activation. Jun 2022. URL: https://doi.org/10.1080/21541248.2022.2089001, doi:10.1080/21541248.2022.2089001. This article has 15 citations and is from a peer-reviewed journal.

12. (wang2024theconfigurationof pages 14-15): Dingyi Wang, Guoxia Liu, Yuxin Meng, Hongjie Chen, Zu Ye, and Ji Jing. The configuration of grb2 in protein interaction and signal transduction. Biomolecules, 14:259, Feb 2024. URL: https://doi.org/10.3390/biom14030259, doi:10.3390/biom14030259. This article has 55 citations.

13. (jasemi2022allostericregulationof pages 1-2): Neda S. Kazemein Jasemi and M. Reza Ahmadian. Allosteric regulation of grb2 modulates ras activation. Jun 2022. URL: https://doi.org/10.1080/21541248.2022.2089001, doi:10.1080/21541248.2022.2089001. This article has 15 citations and is from a peer-reviewed journal.

14. (phan2024grb2phosphorylationantagonizes pages 10-14): Henry T. Phan, Chun-Wei Lin, Brittany L. Stinger, Joseph B. DeGrandchamp, L.J. Nugent Lew, Serena J. Huang, and Jay T. Groves. Grb2 phosphorylation antagonizes egfr-driven ras activation by interfering with condensate assembly. bioRxiv, Sep 2024. URL: https://doi.org/10.1101/2024.09.05.611544, doi:10.1101/2024.09.05.611544. This article has 5 citations.

15. (phan2024grb2phosphorylationantagonizes pages 8-10): Henry T. Phan, Chun-Wei Lin, Brittany L. Stinger, Joseph B. DeGrandchamp, L.J. Nugent Lew, Serena J. Huang, and Jay T. Groves. Grb2 phosphorylation antagonizes egfr-driven ras activation by interfering with condensate assembly. bioRxiv, Sep 2024. URL: https://doi.org/10.1101/2024.09.05.611544, doi:10.1101/2024.09.05.611544. This article has 5 citations.

16. (phan2024grb2phosphorylationantagonizes pages 1-4): Henry T. Phan, Chun-Wei Lin, Brittany L. Stinger, Joseph B. DeGrandchamp, L.J. Nugent Lew, Serena J. Huang, and Jay T. Groves. Grb2 phosphorylation antagonizes egfr-driven ras activation by interfering with condensate assembly. bioRxiv, Sep 2024. URL: https://doi.org/10.1101/2024.09.05.611544, doi:10.1101/2024.09.05.611544. This article has 5 citations.

17. (phan2024grb2phosphorylationantagonizes pages 6-8): Henry T. Phan, Chun-Wei Lin, Brittany L. Stinger, Joseph B. DeGrandchamp, L.J. Nugent Lew, Serena J. Huang, and Jay T. Groves. Grb2 phosphorylation antagonizes egfr-driven ras activation by interfering with condensate assembly. bioRxiv, Sep 2024. URL: https://doi.org/10.1101/2024.09.05.611544, doi:10.1101/2024.09.05.611544. This article has 5 citations.

18. (kamel2026disruptingthekras–sos1 pages 7-8): Emadeldin M. Kamel, Sally Mostafa Khadrawy, Mohamed A. M. Ali, Mostafa R. Abukhadra, Nour Y. S. Yassin, Saleh Alkhedhairi, Faris F. Aba Alkhayl, and Al Mokhtar Lamsabhi. Disrupting the kras–sos1 protein–protein interaction: mechanistic rationale for pan-kras pathway suppression and combination therapy. Frontiers in Chemistry, Apr 2026. URL: https://doi.org/10.3389/fchem.2026.1808601, doi:10.3389/fchem.2026.1808601. This article has 0 citations.

19. (kamel2026disruptingthekras–sos1 pages 6-7): Emadeldin M. Kamel, Sally Mostafa Khadrawy, Mohamed A. M. Ali, Mostafa R. Abukhadra, Nour Y. S. Yassin, Saleh Alkhedhairi, Faris F. Aba Alkhayl, and Al Mokhtar Lamsabhi. Disrupting the kras–sos1 protein–protein interaction: mechanistic rationale for pan-kras pathway suppression and combination therapy. Frontiers in Chemistry, Apr 2026. URL: https://doi.org/10.3389/fchem.2026.1808601, doi:10.3389/fchem.2026.1808601. This article has 0 citations.

20. (kamel2026disruptingthekras–sos1 pages 8-10): Emadeldin M. Kamel, Sally Mostafa Khadrawy, Mohamed A. M. Ali, Mostafa R. Abukhadra, Nour Y. S. Yassin, Saleh Alkhedhairi, Faris F. Aba Alkhayl, and Al Mokhtar Lamsabhi. Disrupting the kras–sos1 protein–protein interaction: mechanistic rationale for pan-kras pathway suppression and combination therapy. Frontiers in Chemistry, Apr 2026. URL: https://doi.org/10.3389/fchem.2026.1808601, doi:10.3389/fchem.2026.1808601. This article has 0 citations.

21. (zhou2024newdirectionsfor pages 1-2): Yue Zhou, Jun-ichiro Takahashi, and Hiroaki Sakurai. New directions for advanced targeting strategies of egfr signaling in cancer. Biological & pharmaceutical bulletin, 47 5:895-903, May 2024. URL: https://doi.org/10.1248/bpb.b23-00924, doi:10.1248/bpb.b23-00924. This article has 8 citations and is from a peer-reviewed journal.

22. (saddawikonefka2022her2andher3 pages 3-4): Robert Saddawi-Konefka, Shiruyeh Schokrpur, Asona J. Lui, and J. Silvio Gutkind. Her2 and her3 as therapeutic targets in head and neck cancer. The Cancer Journal, 28:339-345, Sep 2022. URL: https://doi.org/10.1097/ppo.0000000000000622, doi:10.1097/ppo.0000000000000622. This article has 29 citations.

23. (cheng2024acomprehensivereview pages 3-5): Xiaoqing Cheng. A comprehensive review of her2 in cancer biology and therapeutics. Genes, Jul 2024. URL: https://doi.org/10.3390/genes15070903, doi:10.3390/genes15070903. This article has 326 citations.

24. (tito2025egfreceptorin pages 7-9): Claudia Tito, Silvia Masciarelli, Gianni Colotti, and Francesco Fazi. Egf receptor in organ development, tissue homeostasis and regeneration. Journal of Biomedical Science, Feb 2025. URL: https://doi.org/10.1186/s12929-025-01119-9, doi:10.1186/s12929-025-01119-9. This article has 122 citations and is from a domain leading peer-reviewed journal.

25. (tito2025egfreceptorin pages 17-19): Claudia Tito, Silvia Masciarelli, Gianni Colotti, and Francesco Fazi. Egf receptor in organ development, tissue homeostasis and regeneration. Journal of Biomedical Science, Feb 2025. URL: https://doi.org/10.1186/s12929-025-01119-9, doi:10.1186/s12929-025-01119-9. This article has 122 citations and is from a domain leading peer-reviewed journal.

26. (tito2025egfreceptorin pages 20-22): Claudia Tito, Silvia Masciarelli, Gianni Colotti, and Francesco Fazi. Egf receptor in organ development, tissue homeostasis and regeneration. Journal of Biomedical Science, Feb 2025. URL: https://doi.org/10.1186/s12929-025-01119-9, doi:10.1186/s12929-025-01119-9. This article has 122 citations and is from a domain leading peer-reviewed journal.

27. (mudumbi2024distinctinteractionsstabilize pages 28-30): Krishna C. Mudumbi, Eric A. Burns, David J. Schodt, Zaritza O. Petrova, Anatoly Kiyatkin, Lucy W. Kim, Emma M. Mangiacapre, Irais Ortiz-Caraveo, Hector Rivera Ortiz, Chun Hu, Kumar D. Ashtekar, Keith A. Lidke, Diane S. Lidke, and Mark A. Lemmon. Distinct interactions stabilize egfr dimers and higher-order oligomers in cell membranes. bioRxiv, Apr 2024. URL: https://doi.org/10.1101/2023.04.10.536273, doi:10.1101/2023.04.10.536273. This article has 43 citations.

28. (kemmer2022disentanglingerbbsignaling pages 17-18): Svenja Kemmer, Mireia Berdiel-Acer, Eileen Reinz, Johanna Sonntag, Nooraldeen Tarade, Stephan Bernhardt, Mirjam Fehling-Kaschek, Max Hasmann, Ulrike Korf, Stefan Wiemann, and Jens Timmer. Disentangling erbb signaling in breast cancer subtypes—a model-based analysis. Cancers, 14:2379, May 2022. URL: https://doi.org/10.3390/cancers14102379, doi:10.3390/cancers14102379. This article has 13 citations.

29. (kniazkina2023doesegfrsignaling pages 2-4): Marina Kniazkina and Vyacheslav Dyachuk. Does egfr signaling mediate orexin system activity in sleep initiation? International Journal of Molecular Sciences, 24:9505, May 2023. URL: https://doi.org/10.3390/ijms24119505, doi:10.3390/ijms24119505. This article has 7 citations.

30. (kniazkina2023doesegfrsignaling pages 12-14): Marina Kniazkina and Vyacheslav Dyachuk. Does egfr signaling mediate orexin system activity in sleep initiation? International Journal of Molecular Sciences, 24:9505, May 2023. URL: https://doi.org/10.3390/ijms24119505, doi:10.3390/ijms24119505. This article has 7 citations.

31. (tito2025egfreceptorin pages 5-7): Claudia Tito, Silvia Masciarelli, Gianni Colotti, and Francesco Fazi. Egf receptor in organ development, tissue homeostasis and regeneration. Journal of Biomedical Science, Feb 2025. URL: https://doi.org/10.1186/s12929-025-01119-9, doi:10.1186/s12929-025-01119-9. This article has 122 citations and is from a domain leading peer-reviewed journal.

32. (tito2025egfreceptorin pages 11-12): Claudia Tito, Silvia Masciarelli, Gianni Colotti, and Francesco Fazi. Egf receptor in organ development, tissue homeostasis and regeneration. Journal of Biomedical Science, Feb 2025. URL: https://doi.org/10.1186/s12929-025-01119-9, doi:10.1186/s12929-025-01119-9. This article has 122 citations and is from a domain leading peer-reviewed journal.

33. (tito2025egfreceptorin pages 4-5): Claudia Tito, Silvia Masciarelli, Gianni Colotti, and Francesco Fazi. Egf receptor in organ development, tissue homeostasis and regeneration. Journal of Biomedical Science, Feb 2025. URL: https://doi.org/10.1186/s12929-025-01119-9, doi:10.1186/s12929-025-01119-9. This article has 122 citations and is from a domain leading peer-reviewed journal.

34. (kovacs2022ittakesmore pages 7-8): Tamas Kovacs, Florina Zakany, and Peter Nagy. It takes more than two to tango: complex, hierarchal, and membrane-modulated interactions in the regulation of receptor tyrosine kinases. Cancers, 14:944, Feb 2022. URL: https://doi.org/10.3390/cancers14040944, doi:10.3390/cancers14040944. This article has 39 citations.

35. (wang2024theconfigurationof pages 5-7): Dingyi Wang, Guoxia Liu, Yuxin Meng, Hongjie Chen, Zu Ye, and Ji Jing. The configuration of grb2 in protein interaction and signal transduction. Biomolecules, 14:259, Feb 2024. URL: https://doi.org/10.3390/biom14030259, doi:10.3390/biom14030259. This article has 55 citations.

36. (kamel2026disruptingthekras–sos1 pages 1-2): Emadeldin M. Kamel, Sally Mostafa Khadrawy, Mohamed A. M. Ali, Mostafa R. Abukhadra, Nour Y. S. Yassin, Saleh Alkhedhairi, Faris F. Aba Alkhayl, and Al Mokhtar Lamsabhi. Disrupting the kras–sos1 protein–protein interaction: mechanistic rationale for pan-kras pathway suppression and combination therapy. Frontiers in Chemistry, Apr 2026. URL: https://doi.org/10.3389/fchem.2026.1808601, doi:10.3389/fchem.2026.1808601. This article has 0 citations.

37. (kamel2026disruptingthekras–sos1 pages 4-6): Emadeldin M. Kamel, Sally Mostafa Khadrawy, Mohamed A. M. Ali, Mostafa R. Abukhadra, Nour Y. S. Yassin, Saleh Alkhedhairi, Faris F. Aba Alkhayl, and Al Mokhtar Lamsabhi. Disrupting the kras–sos1 protein–protein interaction: mechanistic rationale for pan-kras pathway suppression and combination therapy. Frontiers in Chemistry, Apr 2026. URL: https://doi.org/10.3389/fchem.2026.1808601, doi:10.3389/fchem.2026.1808601. This article has 0 citations.

## Artifacts

- [Edison artifact artifact-00](egfr_signaling-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](egfr_signaling-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. schultz2023egfrtraffickingeffect pages 3-5
2. tito2025egfreceptorin pages 2-4
3. kovacs2022ittakesmore pages 2-4
4. kovacs2022ittakesmore pages 4-5
5. martinfernandez2022fluorescenceimagingof pages 4-5
6. jasemi2022allostericregulationof pages 2-4
7. wang2024theconfigurationof pages 14-15
8. jasemi2022allostericregulationof pages 1-2
9. cheng2024acomprehensivereview pages 3-5
10. kemmer2022disentanglingerbbsignaling pages 17-18
11. kniazkina2023doesegfrsignaling pages 2-4
12. tito2025egfreceptorin pages 1-2
13. tito2025egfreceptorin pages 11-12
14. tito2025egfreceptorin pages 20-22
15. tito2025egfreceptorin pages 17-19
16. zhou2024newdirectionsfor pages 1-2
17. schultz2023egfrtraffickingeffect pages 2-3
18. mudumbi2024distinctinteractionsstabilize pages 28-30
19. kovacs2022ittakesmore pages 7-8
20. schultz2023egfrtraffickingeffect pages 1-2
21. wang2024theconfigurationof pages 9-11
22. wang2024theconfigurationof pages 1-2
23. tito2025egfreceptorin pages 7-9
24. kniazkina2023doesegfrsignaling pages 12-14
25. tito2025egfreceptorin pages 5-7
26. tito2025egfreceptorin pages 4-5
27. wang2024theconfigurationof pages 5-7
28. https://doi.org/10.1186/s12929-025-01119-9,
29. https://doi.org/10.3389/fonc.2023.1258371,
30. https://doi.org/10.3390/cancers14040944,
31. https://doi.org/10.3390/cancers14030686,
32. https://doi.org/10.3390/biom14030259,
33. https://doi.org/10.1080/21541248.2022.2089001,
34. https://doi.org/10.1101/2024.09.05.611544,
35. https://doi.org/10.3389/fchem.2026.1808601,
36. https://doi.org/10.1248/bpb.b23-00924,
37. https://doi.org/10.1097/ppo.0000000000000622,
38. https://doi.org/10.3390/genes15070903,
39. https://doi.org/10.1101/2023.04.10.536273,
40. https://doi.org/10.3390/cancers14102379,
41. https://doi.org/10.3390/ijms24119505,