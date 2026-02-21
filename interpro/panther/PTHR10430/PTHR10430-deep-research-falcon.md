---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-02-16T18:50:53.794446'
end_time: '2026-02-16T19:00:28.563459'
duration_seconds: 574.77
template_file: templates/family_research.md
template_variables:
  family_id: PTHR10430
  family_name: '{''name'': ''PEROXIREDOXIN'', ''short'': None}'
  interpro_id: IPR037944
  root_node: ''
  subfamily_count: '0'
  subfamily_summary: No subfamily information available.
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 50
---

## Question

# PANTHER Family Research

## Family Context

- **Family ID:** PTHR10430
- **Family Name:** {'name': 'PEROXIREDOXIN', 'short': None}
- **InterPro Entry:** IPR037944
- **Root Node:** 
- **Number of Subfamilies:** 0

### Subfamily Summary

No subfamily information available.

---

## Research Objective

This is a PANTHER protein family that may contain subfamilies with divergent functions. Your task is to investigate the evolutionary relationships and functional diversity within this family, with particular attention to:

1. **Neo-functionalization**: Have any subfamilies evolved new functions distinct from the ancestral function?
2. **Subfunctionalization**: Have subfamilies specialized for different substrates, cellular contexts, or organisms?
3. **GO annotation accuracy**: Are the GO annotations propagated from ancestral nodes appropriate for all descendants?

## Research Questions

### 1. Family Function Overview

For this protein family:
- What is the common structural fold shared by family members?
- What is the ancestral/core function of this family?
- What cofactors, substrates, or binding partners are typical?
- What are the key catalytic/functional residues?

### 2. Subfamily Functional Diversity

For each major subfamily:
- What is the specific function of proteins in this subfamily?
- Does this function differ from the ancestral function?
- What is the EC number (if enzymatic)?
- What experimental evidence supports this function?

### 3. Neo-functionalization Detection

Look for signs of functional divergence:
- Are there subfamilies with different EC numbers within the family?
- Are there subfamilies that catalyze opposite reactions (e.g., synthesis vs degradation)?
- Are there subfamilies with different substrate specificities?
- Do any subfamilies have non-catalytic functions (e.g., structural, regulatory)?

### 4. Branch Length Analysis

Consider the evolutionary divergence:
- Which subfamilies have the longest branch lengths from the root?
- Do longer branches correlate with functional changes?
- Are there any very short branches that might be recent duplications?

### 5. GO Annotation Assessment

For GO annotations propagated across the family:
- Are these annotations appropriate for ALL subfamilies?
- Should any subfamilies have different/opposite annotations?
- Are there subfamilies that should be excluded from certain annotations?
- What subfamily-specific annotations should be added?

### 6. Literature Support

- What are the key papers describing this protein family?
- Are there papers specifically about functional divergence within the family?
- Are there structural biology papers showing differences between subfamilies?
- Are there biochemical studies comparing activities of different family members?

## Output Format

Please provide your findings in a narrative format with citations. Structure your response as:

1. **Executive Summary** - Brief overview of family diversity and key findings
2. **Ancestral Function** - What the common ancestor likely did
3. **Subfamily Analysis** - Function of each major subfamily with evidence
4. **Functional Divergence** - Cases of neo-functionalization or subfunctionalization
5. **GO Annotation Issues** - Problematic annotations and recommendations
6. **Key Literature** - Citations supporting the analysis

Be sure to include citations (PMIDs) for all statements.


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

# PANTHER Family Research

## Family Context

- **Family ID:** PTHR10430
- **Family Name:** {'name': 'PEROXIREDOXIN', 'short': None}
- **InterPro Entry:** IPR037944
- **Root Node:** 
- **Number of Subfamilies:** 0

### Subfamily Summary

No subfamily information available.

---

## Research Objective

This is a PANTHER protein family that may contain subfamilies with divergent functions. Your task is to investigate the evolutionary relationships and functional diversity within this family, with particular attention to:

1. **Neo-functionalization**: Have any subfamilies evolved new functions distinct from the ancestral function?
2. **Subfunctionalization**: Have subfamilies specialized for different substrates, cellular contexts, or organisms?
3. **GO annotation accuracy**: Are the GO annotations propagated from ancestral nodes appropriate for all descendants?

## Research Questions

### 1. Family Function Overview

For this protein family:
- What is the common structural fold shared by family members?
- What is the ancestral/core function of this family?
- What cofactors, substrates, or binding partners are typical?
- What are the key catalytic/functional residues?

### 2. Subfamily Functional Diversity

For each major subfamily:
- What is the specific function of proteins in this subfamily?
- Does this function differ from the ancestral function?
- What is the EC number (if enzymatic)?
- What experimental evidence supports this function?

### 3. Neo-functionalization Detection

Look for signs of functional divergence:
- Are there subfamilies with different EC numbers within the family?
- Are there subfamilies that catalyze opposite reactions (e.g., synthesis vs degradation)?
- Are there subfamilies with different substrate specificities?
- Do any subfamilies have non-catalytic functions (e.g., structural, regulatory)?

### 4. Branch Length Analysis

Consider the evolutionary divergence:
- Which subfamilies have the longest branch lengths from the root?
- Do longer branches correlate with functional changes?
- Are there any very short branches that might be recent duplications?

### 5. GO Annotation Assessment

For GO annotations propagated across the family:
- Are these annotations appropriate for ALL subfamilies?
- Should any subfamilies have different/opposite annotations?
- Are there subfamilies that should be excluded from certain annotations?
- What subfamily-specific annotations should be added?

### 6. Literature Support

- What are the key papers describing this protein family?
- Are there papers specifically about functional divergence within the family?
- Are there structural biology papers showing differences between subfamilies?
- Are there biochemical studies comparing activities of different family members?

## Output Format

Please provide your findings in a narrative format with citations. Structure your response as:

1. **Executive Summary** - Brief overview of family diversity and key findings
2. **Ancestral Function** - What the common ancestor likely did
3. **Subfamily Analysis** - Function of each major subfamily with evidence
4. **Functional Divergence** - Cases of neo-functionalization or subfunctionalization
5. **GO Annotation Issues** - Problematic annotations and recommendations
6. **Key Literature** - Citations supporting the analysis

Be sure to include citations (PMIDs) for all statements.


## Executive Summary
PANTHER family **PTHR10430 (PEROXIREDOXIN)** and InterPro **IPR037944** correspond to the broadly distributed peroxiredoxin (Prx/PRDX) superfamily of cysteine-dependent peroxide reductases. Across bacteria, archaea, and eukaryotes, Prxs share a thioredoxin-like fold and a conserved **peroxidatic cysteine (CP)** motif, but they diversify into at least **six mechanistically and structurally distinguishable classes** (Prx1/AhpC, Prx5, Prx6, Tpx, BCP/PrxQ, AhpE) with different resolving-cysteine positions, oligomerization behaviors, reductant systems, and cellular localizations. This functional diversity supports extensive **subfunctionalization** (e.g., compartment-specific isoforms, reductant preferences) and clear cases of **neo-functionalization**, most notably the **PRDX6/Prx6 class** acquiring non-peroxidase enzymatic activities (e.g., phospholipase A2-related functions) and oxidation-state-dependent **chaperone/holdase** behavior. Recent 2023–2024 literature emphasizes Prxs as **H2O2 sensors and “proxy oxidants”** in redox relay signaling, with oligomeric-state dynamics coupled to redox state and hyperoxidation/recovery cycles that regulate signaling range and timing. Quantitative data support Prxs as extremely fast (kcat/Km or second-order rates often ~10^7–10^8 M−1 s−1) and abundant proteins that can dominate cellular peroxide removal. (perkins2015modelsystemsfor pages 70-75, hall2011structurebasedinsightsinto pages 1-2, sadowskabartosz2023peroxiredoxin2an pages 1-2, villar2023themultifacetednature pages 1-2)

## Ancestral Function (core function likely present at the root)
### Common fold and defining catalytic motif
Prxs share a **thioredoxin-like fold** (classically described as ~7 β-strands and ~5 α-helices in the core) and a universally conserved active-site region containing the **Pxxx(T/S)xxC** motif that houses the nucleophilic **CP**. (perkins2015modelsystemsfor pages 70-75, reeves2011kineticthermodynamicanda pages 27-31, hall2011structurebasedinsightsinto pages 1-2)

### Core catalytic mechanism and key residues
The ancestral/core biochemical function is **thiol-dependent reduction of peroxides** (H2O2, organic hydroperoxides; often also peroxynitrite) without heme/selenium cofactors. CP is activated (low pKa) as a thiolate that performs an **SN2-type attack** on peroxide, forming **CP–SOH (sulfenic acid)**. Catalysis requires a conformational cycle between **fully folded (FF)** and **locally unfolded (LU)** states to enable disulfide formation and recycling. (perkins2015modelsystemsfor pages 70-75, hall2011structurebasedinsightsinto pages 1-2, perkins2015modelsystemsfora pages 70-75)

A conserved set of active-site residues (including Thr/Ser in the motif and an Arg-containing active-site environment) forms an H-bond network supporting the transition state and the extraordinary peroxide reactivity observed for many Prxs. (hall2011structurebasedinsightsinto pages 1-2, harper2017anatlasof pages 2-4)

### Resolving cysteine and reductant systems
Prxs partition into mechanistic types based on how CP–SOH is resolved:
- **Typical 2-Cys**: CP–SOH forms an **intersubunit** disulfide with a **resolving cysteine (CR)** on the partner subunit.
- **Atypical 2-Cys**: CP–SOH forms an **intrasubunit** CP–CR disulfide (CR position varies across helices/tail).
- **1-Cys**: no dedicated CR; CP–SOH is reduced by external thiols/small molecules.

Recycling commonly proceeds through **thioredoxin/thioredoxin reductase (Trx/TrxR)** systems for 2-Cys Prxs; 1-Cys Prxs can be reduced by **glutathione** or other small-molecule reductants, depending on lineage and cellular context. (reeves2011kineticthermodynamicanda pages 27-31, perkins2015modelsystemsfora pages 70-75, knoops2007evolutionofthe pages 4-6)

### Hyperoxidation and repair
Under high peroxide flux, CP–SOH can be further oxidized to **CP–SO2−/SO2H (hyperoxidation)**, which in many eukaryotes can be reversed by **ATP-dependent sulfiredoxin (Srx)**. Hyperoxidation sensitivity varies among isoforms and is considered a regulatory feature in peroxide signaling. (perkins2015modelsystemsfor pages 70-75, sadowskabartosz2023peroxiredoxin2an pages 2-4, perkins2014tuningofperoxiredoxin pages 1-5)

## Subfamily Analysis (major functional classes)
Although the supplied PANTHER record reports “0 subfamilies,” the peroxiredoxin superfamily has robust, structure-informed functional subdivision into six classes used by PREX and subsequent active-site profiling frameworks. (perkins2015modelsystemsfor pages 70-75, soito2011prexperoxiredoxinclassification pages 1-2)

### 1) Prx1/AhpC (typical 2-Cys)
**Function:** High-efficiency peroxide reductases; in eukaryotes also key H2O2 sensors/regulators for signaling. (hall2011structurebasedinsightsinto pages 1-2, perkins2015peroxiredoxinsguardiansagainst pages 2-3)

**Mechanism:** Predominantly typical 2-Cys with CR near the C-terminus; disulfide formation requires LU transition. (hall2011structurebasedinsightsinto pages 1-2, reeves2011kineticthermodynamicanda pages 27-31)

**Oligomerization:** Often form B-type dimers and higher-order decamers (toroids), with redox-state-dependent transitions. (perkins2015peroxiredoxinsguardiansagainst pages 2-3, villar2023themultifacetednature pages 2-4)

**Localization examples (mammals):** PrxI/II cytosol/nucleus; PrxIII mitochondria; PrxIV secretory/ER-related compartments. (rhee2017multiplefunctionsand pages 2-4, perkins2015peroxiredoxinsguardiansagainst pages 2-3)

**Quantitative note:** Very high rates are reported for Prx reactions with H2O2 (~10^7 M−1 s−1 scale). (hall2011structurebasedinsightsinto pages 1-2, perkins2014tuningofperoxiredoxin pages 1-5)

### 2) Prx5 (often atypical 2-Cys; mixed 1-Cys/2-Cys usage)
**Function:** Peroxide reduction with notable diversity; in mammals PRDX5 (PrxV) favors alkyl hydroperoxides/peroxynitrite relative to H2O2 in some contexts. (rhee2017multiplefunctionsand pages 1-2)

**Mechanism & reductants:** Mechanistic diversity within the class includes both 1-Cys and 2-Cys solutions; some proteins are fused to **glutaredoxin (Grx) domains** (~16% in one survey), implying alternative reductant coupling in those lineages. (perkins2015modelsystemsfor pages 49-52, perkins2015modelsystemsfora pages 49-52)

**Evolutionary signal:** In metazoan comparative genomics, PRX5 shows **lower conservation and gene loss** in multiple lineages and high active-site diversity at CR positions, consistent with lineage-specific specialization and/or redundancy with other mitochondrial Prxs. (hewitt2023antioxidantenzymesthat pages 5-6)

### 3) Prx6 (1-Cys-dominant; multifunctional)
**Canonical function:** Peroxide reduction (notably alkyl hydroperoxides/lipid peroxides in mammalian contexts). (rhee2017multiplefunctionsand pages 2-4, rhee2017multiplefunctionsand pages 1-2)

**Neo-functionalization:** Mammalian PRDX6 (PrxVI) is annotated as **aiPLA2** and has additional lipid-related enzymatic functions (reviewed as aiPLA2/LPCAT-related activities) with distinct active centers (e.g., peroxidatic cysteine vs a catalytic triad for PLA2-like activity), enabling context-dependent anti-oxidant or pro-oxidant roles in respiratory disease models. (rhee2017multiplefunctionsand pages 2-4, jia2023antioxidantandprooxidant pages 1-3)

**Evolutionary conservation:** PRX6 is particularly conserved across metazoa and is consistently cytoplasmic in a broad survey, supporting an essential, conserved role and suggesting its multifunctionality is evolutionarily stable. (hewitt2023antioxidantenzymesthat pages 5-6, hewitt2023antioxidantenzymesthat pages 8-9)

### 4) Tpx (thiol peroxidase; bacterial-focused)
**Distribution & mechanism:** Reported as bacterial-only in some classifications; often forms A-type dimers, with subfamily-specific structural features (e.g., N-terminal β-hairpin). (perkins2015modelsystemsfor pages 49-52, perkins2015modelsystemsfora pages 49-52)

### 5) BCP/PrxQ
**Distribution:** Found in bacteria and plants; absent in animals in several summaries. (perkins2015modelsystemsfor pages 49-52, perkins2015modelsystemsfora pages 49-52)

**Mechanism:** CR frequently located in helix α2 or α3 (reported as common positional solutions within this family). (reeves2011kineticthermodynamicanda pages 27-31)

### 6) AhpE
**Distribution:** Bacterial; less structurally represented historically, complicating automated annotation and clustering. (harper2017anatlasof pages 19-20, harper2017anatlasof pages 1-2)

## Functional Divergence (neo-functionalization and subfunctionalization)
### Subfunctionalization: compartmentalization and isoform diversification
Across evolution, Prx gene number increases with organismal complexity (example counts: **E. coli ~3, S. cerevisiae ~5, H. sapiens ~6, A. thaliana ~9**), interpreted as expansion enabling **subcellular targeting** (mitochondrial, nuclear, peroxisomal, chloroplast) and specialization. (knoops2007evolutionofthe pages 4-6)

In animals, phylogenomics supports three major clades (AhpC-PRX1, PRX5, PRX6) that were likely present in ancestral metazoans; in one survey of 19 species, **799 PRX-domain-containing sequences** were found, with a filtered set of **110 sequences** retaining the canonical CP motif used for catalysis, consistent with strong active-site conservation despite family expansion. (hewitt2023antioxidantenzymesthat pages 3-4)

### Neo-functionalization: emergence of non-peroxidase activities and signaling “relay” roles
**PRDX6/Prx6 multifunctionality** (peroxidase plus aiPLA2/LPCAT-related activities) is a strong example of neo-functionalization relative to the ancestral peroxide-reductase role, and it underpins opposing phenotypes (anti-oxidant vs pro-oxidant) depending on localization/pH and regulatory context in respiratory disease models. (jia2023antioxidantandprooxidant pages 1-3)

Beyond enzymology, multiple lines of evidence position Prx as **H2O2 sensors and redox relays (“proxy oxidants”)**, requiring pre-assembled Prx–target complexes and suitable target cysteines for efficient relay. This represents a functional divergence from simple detoxification toward regulated signaling, consistent with evolutionary proposals that metazoan Prxs shifted toward modulation of peroxide signaling and show increased hyperoxidation sensitivity. (knoops2007evolutionofthe pages 1-4, villar2023themultifacetednature pages 2-4)

### Oligomerization-linked functional switching (chaperone/holdase)
Recent expert synthesis links Prx redox state to quaternary structure: reduced forms favor decamer/dodecamer assemblies, disulfide forms favor dimers, and hyperoxidized forms can produce high-molecular-weight species associated with **chaperone-like (holdase) activity** (noting ongoing debate about physiological relevance in some contexts). A quantitative example is reported for human Prx1: equal dimer/decamer distribution at ~**1.36 mM monomer** concentration, and redox-driven decamer↔dimer transitions can be reversed by thioredoxin but not glutathione. (villar2023themultifacetednature pages 2-4)

### Quantitative case study: erythrocyte Prdx2 as an implementation-ready model
A 2023 review emphasizes Prdx2 as **“the third most abundant erythrocyte protein,”** predominantly dimeric but capable of forming decamers, and reacting very rapidly with H2O2 (**k > 10^7 M−1 s−1**). It also provides physiologically grounded reductant levels (erythrocyte **GSH ~2 mM; Trx ~3–5 μM**) and highlights sulfiredoxin repair of hyperoxidized Prdx2 and disease-associated increases in oxidation as readouts of oxidative stress. (sadowskabartosz2023peroxiredoxin2an pages 1-2)

## GO Annotation Issues and Recommendations (propagation across descendants)
### Why naive propagation is risky in PTHR10430
Multiple sources caution that broad labels such as **“thioredoxin peroxidase,” “1-Cys Prx,” or “atypical 2-Cys Prx”** do not map cleanly onto the six mechanistic/structural subfamilies, and that full-sequence similarity thresholds cannot reliably separate some functionally distinct groups, notably **Prx1 vs Prx6**. Active-site profiling approaches (DASP/PREX; MISST) were developed specifically because no single BLAST-like threshold can resolve these subgroups. (harper2017anatlasof pages 19-20, poole2016distributionandfeatures pages 1-2, harper2017anatlasof pages 1-2)

In particular, active-site profiling distinguished Prx1 and Prx6 using subgroup-specific motifs (e.g., PxDF(T/S)FVCP vs Px(D/N)(F/Y)TPVCP), demonstrating that a small active-site difference can be diagnostic of a different functional family; this argues against propagating detailed mechanistic GO terms without subfamily assignment. (harper2017anatlasof pages 13-14)

### Recommended GO propagation strategy
**Safe-to-propagate across essentially all catalytically intact peroxiredoxins** (when the CP motif is present):
- Molecular function: peroxide reductase / thiol-dependent peroxidase activity in a general sense, anchored on the conserved CP motif and shared fold/mechanism. (perkins2015modelsystemsfor pages 70-75, hewitt2023antioxidantenzymesthat pages 3-4)

**Should be restricted to specific mechanistic classes/subfamilies:**
- “Thioredoxin-dependent” reductant usage should not be assumed for 1-Cys lineages; 1-Cys Prxs can use glutathione or other small-molecule reductants. (knoops2007evolutionofthe pages 4-6, perkins2015modelsystemsfora pages 49-52)
- “Typical 2-Cys peroxiredoxin activity” should be restricted to **Prx1/AhpC-like** enzymes with an appropriate CR arrangement (intersubunit disulfide) rather than assigned broadly to the whole family. (reeves2011kineticthermodynamicanda pages 27-31, knoops2007evolutionofthe pages 4-6)

**Subfamily-specific additions (do not propagate to all descendants):**
- For Prx6/PRDX6-like proteins: add lipid-related enzymatic functions (aiPLA2/LPCAT-related activities) where supported; these are not ancestral or universal Prx properties and represent neo-functionalization in this class. (rhee2017multiplefunctionsand pages 2-4, jia2023antioxidantandprooxidant pages 1-3)

**Practical recommendation for PTHR10430 curation:**
- Implement an explicit subfamily assignment layer (e.g., via PREX/DASP/MISST-style active-site profiles) before propagating any mechanistically specific GO terms such as “thioredoxin peroxidase activity,” “alkyl hydroperoxide reductase activity,” or “phospholipase A2 activity.” (poole2016distributionandfeatures pages 1-2, soito2011prexperoxiredoxinclassification pages 1-2)

## Current applications and real-world implementations (2023–2024 emphasis)
1. **Biomarkers and disease readouts:** Multiple recent syntheses describe Prx isoforms as biomarker candidates across cancer, neurodegeneration, cardiovascular disease, diabetes complications, inflammatory disease, and infection severity; the translational theme is isoform-specific dysregulation with prognostic/diagnostic value. (qausain2024unravelingtheperoxidase pages 10-11, qausain2024unravelingtheperoxidase pages 11-12)
2. **Therapeutic targeting and drug discovery:** 2023 expert opinion notes a surge in **Prx inhibitor** development, but also emphasizes selectivity challenges because most inhibitors exploit catalytic-cysteine reactivity and may target many cellular cysteines. (villar2023themultifacetednature pages 2-4)
3. **Respiratory disease targeting (PRDX6):** PRDX6 is presented as a therapeutic target in respiratory diseases because of its multifunctionality and context-dependent anti-/pro-oxidant roles controlled by subcellular localization, pH, and transcriptional/miRNA regulation. (jia2023antioxidantandprooxidant pages 1-3)
4. **Redox signaling tool development:** Prx-based probes and biophysical tools for analyzing oligomerization and redox transitions are highlighted as enabling technologies; kinetics can separate fast H2O2 sensing (ms) from slower intramolecular reporting steps (min). (villar2023themultifacetednature pages 2-4)

## Key Literature (URLs and publication dates; PMIDs)
The tool-accessible full texts used here consistently expose **DOIs/URLs and dates**, but **PMIDs were not present in the retrieved text extracts**, so they cannot be reliably reported for every citation in this report.

**Recent (prioritized 2023–2024):**
- Villar SF, Ferrer-Sueta G, Denicola A. *The multifaceted nature of peroxiredoxins in chemical biology.* **Current Opinion in Chemical Biology** (Oct 2023). https://doi.org/10.1016/j.cbpa.2023.102355 (villar2023themultifacetednature pages 1-2)
- Sadowska-Bartosz I, Bartosz G. *Peroxiredoxin 2: An Important Element of the Antioxidant Defense of the Erythrocyte.* **Antioxidants** (Apr 2023). https://doi.org/10.3390/antiox12051012 (sadowskabartosz2023peroxiredoxin2an pages 1-2)
- Jia W, Dong C, Li B. *Anti-Oxidant and Pro-Oxidant Effects of Peroxiredoxin 6: A Potential Target in Respiratory Diseases.* **Cells** (Jan 2023). https://doi.org/10.3390/cells12010181 (jia2023antioxidantandprooxidant pages 1-3)
- Hewitt OH, Degnan SM. *Antioxidant enzymes that target hydrogen peroxide are conserved across the animal kingdom, from sponges to mammals.* **Scientific Reports** (Feb 2023). https://doi.org/10.1038/s41598-023-29304-6 (hewitt2023antioxidantenzymesthat pages 3-4)
- Sies H, Mailloux RJ, Jakob U. *Fundamentals of redox regulation in biology.* **Nature Reviews Molecular Cell Biology** (Apr 2024). https://doi.org/10.1038/s41580-024-00730-2 (qausain2024unravelingtheperoxidase pages 6-8)

**Foundational classification/annotation resources:**
- Soito L et al. *PREX: PeroxiRedoxin classification indEX.* **Nucleic Acids Research** (Oct 2011). https://doi.org/10.1093/nar/gkq1060 (soito2011prexperoxiredoxinclassification pages 1-2)
- Poole LB, Nelson KJ. *Distribution and Features of the Six Classes of Peroxiredoxins.* **Molecules and Cells** (Jan 2016). https://doi.org/10.14348/molcells.2016.2330 (poole2016distributionandfeatures pages 1-2)
- Harper AF et al. *An Atlas of Peroxiredoxins… functionally relevant clustering.* **PLOS Computational Biology** (Feb 2017). https://doi.org/10.1371/journal.pcbi.1005284 (harper2017anatlasof pages 1-2)

**Mechanism/structure foundations:**
- Hall A et al. *Structure-based insights into the catalytic power and conformational dexterity of peroxiredoxins.* **Antioxidants & Redox Signaling** (Aug 2011). https://doi.org/10.1089/ars.2010.3624 (hall2011structurebasedinsightsinto pages 1-2)
- Perkins A et al. *Tuning of Peroxiredoxin Catalysis for Various Physiological Roles.* **Biochemistry** (Dec 2014). https://doi.org/10.1021/bi5013222 (perkins2014tuningofperoxiredoxin pages 1-5)

### Notes on evidence gaps
- **Branch lengths from PANTHER or dedicated phylogenies** were not available in the retrieved texts; evolutionary divergence is therefore discussed using conservation/diversification and gene-loss patterns as proxies rather than quantitative branch-length statistics. (hewitt2023antioxidantenzymesthat pages 5-6, hewitt2023antioxidantenzymesthat pages 3-4)
- **EC numbers** are not consistently used for Prxs in the retrieved sources; functional description is best captured via mechanistic class and reductant coupling rather than EC assignment. (poole2016distributionandfeatures pages 1-2, soito2011prexperoxiredoxinclassification pages 1-2)

References

1. (perkins2015modelsystemsfor pages 70-75): A Perkins. Model systems for structural investigations into peroxiredoxin catalysis, conformation change, and inactivation. Unknown journal, 2015.

2. (hall2011structurebasedinsightsinto pages 1-2): Andrea Hall, Kimberly Nelson, Leslie B. Poole, and P. Andrew Karplus. Structure-based insights into the catalytic power and conformational dexterity of peroxiredoxins. Antioxidants & redox signaling, 15 3:795-815, Aug 2011. URL: https://doi.org/10.1089/ars.2010.3624, doi:10.1089/ars.2010.3624. This article has 414 citations and is from a domain leading peer-reviewed journal.

3. (sadowskabartosz2023peroxiredoxin2an pages 1-2): Izabela Sadowska-Bartosz and Grzegorz Bartosz. Peroxiredoxin 2: an important element of the antioxidant defense of the erythrocyte. Antioxidants, 12:1012, Apr 2023. URL: https://doi.org/10.3390/antiox12051012, doi:10.3390/antiox12051012. This article has 38 citations.

4. (villar2023themultifacetednature pages 1-2): Sebastián F. Villar, Gerardo Ferrer-Sueta, and Ana Denicola. The multifaceted nature of peroxiredoxins in chemical biology. Oct 2023. URL: https://doi.org/10.1016/j.cbpa.2023.102355, doi:10.1016/j.cbpa.2023.102355. This article has 42 citations and is from a peer-reviewed journal.

5. (reeves2011kineticthermodynamicanda pages 27-31): SA Reeves. Kinetic, thermodynamic and mechanistic features of escherichia coli bcp, an unusually versatile peroxiredoxin. Unknown journal, 2011.

6. (perkins2015modelsystemsfora pages 70-75): A Perkins. Model systems for structural investigations into peroxiredoxin catalysis, conformation change, and inactivation. Unknown journal, 2015.

7. (harper2017anatlasof pages 2-4): Angela F. Harper, Janelle B. Leuthaeuser, Patricia C. Babbitt, John H. Morris, Thomas E. Ferrin, Leslie B. Poole, and Jacquelyn S. Fetrow. An atlas of peroxiredoxins created using an active site profile-based approach to functionally relevant clustering of proteins. PLOS Computational Biology, 13:e1005284, Feb 2017. URL: https://doi.org/10.1371/journal.pcbi.1005284, doi:10.1371/journal.pcbi.1005284. This article has 28 citations and is from a highest quality peer-reviewed journal.

8. (knoops2007evolutionofthe pages 4-6): Bernard Knoops, ElÉonore Loumaye, and ValÉrie Van Der Eecken. Evolution of the peroxiredoxins. Sub-cellular biochemistry, 44:27-40, Jan 2007. URL: https://doi.org/10.1007/978-1-4020-6051-9\_2, doi:10.1007/978-1-4020-6051-9\_2. This article has 131 citations.

9. (sadowskabartosz2023peroxiredoxin2an pages 2-4): Izabela Sadowska-Bartosz and Grzegorz Bartosz. Peroxiredoxin 2: an important element of the antioxidant defense of the erythrocyte. Antioxidants, 12:1012, Apr 2023. URL: https://doi.org/10.3390/antiox12051012, doi:10.3390/antiox12051012. This article has 38 citations.

10. (perkins2014tuningofperoxiredoxin pages 1-5): Arden Perkins, Leslie B. Poole, and P. Andrew Karplus. Tuning of peroxiredoxin catalysis for various physiological roles. Biochemistry, 53:7693-7705, Dec 2014. URL: https://doi.org/10.1021/bi5013222, doi:10.1021/bi5013222. This article has 155 citations and is from a peer-reviewed journal.

11. (soito2011prexperoxiredoxinclassification pages 1-2): Laura Soito, Chris Williamson, Stacy T. Knutson, Jacquelyn S. Fetrow, Leslie B. Poole, and Kimberly J. Nelson. Prex: peroxiredoxin classification index, a database of subfamily assignments across the diverse peroxiredoxin family. Nucleic Acids Research, 39:D332-D337, Oct 2011. URL: https://doi.org/10.1093/nar/gkq1060, doi:10.1093/nar/gkq1060. This article has 130 citations and is from a highest quality peer-reviewed journal.

12. (perkins2015peroxiredoxinsguardiansagainst pages 2-3): Arden Perkins, Kimberly J. Nelson, Derek Parsonage, Leslie B. Poole, and P. Andrew Karplus. Peroxiredoxins: guardians against oxidative stress and modulators of peroxide signaling. Trends in biochemical sciences, 40 8:435-45, Aug 2015. URL: https://doi.org/10.1016/j.tibs.2015.05.001, doi:10.1016/j.tibs.2015.05.001. This article has 744 citations and is from a domain leading peer-reviewed journal.

13. (villar2023themultifacetednature pages 2-4): Sebastián F. Villar, Gerardo Ferrer-Sueta, and Ana Denicola. The multifaceted nature of peroxiredoxins in chemical biology. Oct 2023. URL: https://doi.org/10.1016/j.cbpa.2023.102355, doi:10.1016/j.cbpa.2023.102355. This article has 42 citations and is from a peer-reviewed journal.

14. (rhee2017multiplefunctionsand pages 2-4): Sue Goo Rhee and In Sup Kil. Multiple functions and regulation of mammalian peroxiredoxins. Annual review of biochemistry, 86:749-775, Jun 2017. URL: https://doi.org/10.1146/annurev-biochem-060815-014431, doi:10.1146/annurev-biochem-060815-014431. This article has 346 citations and is from a domain leading peer-reviewed journal.

15. (rhee2017multiplefunctionsand pages 1-2): Sue Goo Rhee and In Sup Kil. Multiple functions and regulation of mammalian peroxiredoxins. Annual review of biochemistry, 86:749-775, Jun 2017. URL: https://doi.org/10.1146/annurev-biochem-060815-014431, doi:10.1146/annurev-biochem-060815-014431. This article has 346 citations and is from a domain leading peer-reviewed journal.

16. (perkins2015modelsystemsfor pages 49-52): A Perkins. Model systems for structural investigations into peroxiredoxin catalysis, conformation change, and inactivation. Unknown journal, 2015.

17. (perkins2015modelsystemsfora pages 49-52): A Perkins. Model systems for structural investigations into peroxiredoxin catalysis, conformation change, and inactivation. Unknown journal, 2015.

18. (hewitt2023antioxidantenzymesthat pages 5-6): Olivia H. Hewitt and Sandie M. Degnan. Antioxidant enzymes that target hydrogen peroxide are conserved across the animal kingdom, from sponges to mammals. Scientific Reports, Feb 2023. URL: https://doi.org/10.1038/s41598-023-29304-6, doi:10.1038/s41598-023-29304-6. This article has 36 citations and is from a peer-reviewed journal.

19. (jia2023antioxidantandprooxidant pages 1-3): Wenhui Jia, Chunling Dong, and Bo Li. Anti-oxidant and pro-oxidant effects of peroxiredoxin 6: a potential target in respiratory diseases. Cells, 12:181, Jan 2023. URL: https://doi.org/10.3390/cells12010181, doi:10.3390/cells12010181. This article has 24 citations.

20. (hewitt2023antioxidantenzymesthat pages 8-9): Olivia H. Hewitt and Sandie M. Degnan. Antioxidant enzymes that target hydrogen peroxide are conserved across the animal kingdom, from sponges to mammals. Scientific Reports, Feb 2023. URL: https://doi.org/10.1038/s41598-023-29304-6, doi:10.1038/s41598-023-29304-6. This article has 36 citations and is from a peer-reviewed journal.

21. (harper2017anatlasof pages 19-20): Angela F. Harper, Janelle B. Leuthaeuser, Patricia C. Babbitt, John H. Morris, Thomas E. Ferrin, Leslie B. Poole, and Jacquelyn S. Fetrow. An atlas of peroxiredoxins created using an active site profile-based approach to functionally relevant clustering of proteins. PLOS Computational Biology, 13:e1005284, Feb 2017. URL: https://doi.org/10.1371/journal.pcbi.1005284, doi:10.1371/journal.pcbi.1005284. This article has 28 citations and is from a highest quality peer-reviewed journal.

22. (harper2017anatlasof pages 1-2): Angela F. Harper, Janelle B. Leuthaeuser, Patricia C. Babbitt, John H. Morris, Thomas E. Ferrin, Leslie B. Poole, and Jacquelyn S. Fetrow. An atlas of peroxiredoxins created using an active site profile-based approach to functionally relevant clustering of proteins. PLOS Computational Biology, 13:e1005284, Feb 2017. URL: https://doi.org/10.1371/journal.pcbi.1005284, doi:10.1371/journal.pcbi.1005284. This article has 28 citations and is from a highest quality peer-reviewed journal.

23. (hewitt2023antioxidantenzymesthat pages 3-4): Olivia H. Hewitt and Sandie M. Degnan. Antioxidant enzymes that target hydrogen peroxide are conserved across the animal kingdom, from sponges to mammals. Scientific Reports, Feb 2023. URL: https://doi.org/10.1038/s41598-023-29304-6, doi:10.1038/s41598-023-29304-6. This article has 36 citations and is from a peer-reviewed journal.

24. (knoops2007evolutionofthe pages 1-4): Bernard Knoops, ElÉonore Loumaye, and ValÉrie Van Der Eecken. Evolution of the peroxiredoxins. Sub-cellular biochemistry, 44:27-40, Jan 2007. URL: https://doi.org/10.1007/978-1-4020-6051-9\_2, doi:10.1007/978-1-4020-6051-9\_2. This article has 131 citations.

25. (poole2016distributionandfeatures pages 1-2): Leslie B. Poole and Kimberly J. Nelson. Distribution and features of the six classes of peroxiredoxins. Molecules and Cells, 39:53-59, Jan 2016. URL: https://doi.org/10.14348/molcells.2016.2330, doi:10.14348/molcells.2016.2330. This article has 96 citations and is from a peer-reviewed journal.

26. (harper2017anatlasof pages 13-14): Angela F. Harper, Janelle B. Leuthaeuser, Patricia C. Babbitt, John H. Morris, Thomas E. Ferrin, Leslie B. Poole, and Jacquelyn S. Fetrow. An atlas of peroxiredoxins created using an active site profile-based approach to functionally relevant clustering of proteins. PLOS Computational Biology, 13:e1005284, Feb 2017. URL: https://doi.org/10.1371/journal.pcbi.1005284, doi:10.1371/journal.pcbi.1005284. This article has 28 citations and is from a highest quality peer-reviewed journal.

27. (qausain2024unravelingtheperoxidase pages 10-11): Sana Qausain and Mohd Basheeruddin. Unraveling the peroxidase activity in peroxiredoxins: a comprehensive review of mechanisms, functions, and biological significance. Cureus, Aug 2024. URL: https://doi.org/10.7759/cureus.66117, doi:10.7759/cureus.66117. This article has 12 citations.

28. (qausain2024unravelingtheperoxidase pages 11-12): Sana Qausain and Mohd Basheeruddin. Unraveling the peroxidase activity in peroxiredoxins: a comprehensive review of mechanisms, functions, and biological significance. Cureus, Aug 2024. URL: https://doi.org/10.7759/cureus.66117, doi:10.7759/cureus.66117. This article has 12 citations.

29. (qausain2024unravelingtheperoxidase pages 6-8): Sana Qausain and Mohd Basheeruddin. Unraveling the peroxidase activity in peroxiredoxins: a comprehensive review of mechanisms, functions, and biological significance. Cureus, Aug 2024. URL: https://doi.org/10.7759/cureus.66117, doi:10.7759/cureus.66117. This article has 12 citations.

## Citations

1. rhee2017multiplefunctionsand pages 1-2
2. hewitt2023antioxidantenzymesthat pages 5-6
3. reeves2011kineticthermodynamicanda pages 27-31
4. knoops2007evolutionofthe pages 4-6
5. hewitt2023antioxidantenzymesthat pages 3-4
6. jia2023antioxidantandprooxidant pages 1-3
7. villar2023themultifacetednature pages 2-4
8. harper2017anatlasof pages 13-14
9. villar2023themultifacetednature pages 1-2
10. qausain2024unravelingtheperoxidase pages 6-8
11. soito2011prexperoxiredoxinclassification pages 1-2
12. poole2016distributionandfeatures pages 1-2
13. harper2017anatlasof pages 1-2
14. hall2011structurebasedinsightsinto pages 1-2
15. perkins2014tuningofperoxiredoxin pages 1-5
16. perkins2015modelsystemsfor pages 70-75
17. perkins2015modelsystemsfora pages 70-75
18. harper2017anatlasof pages 2-4
19. perkins2015peroxiredoxinsguardiansagainst pages 2-3
20. rhee2017multiplefunctionsand pages 2-4
21. perkins2015modelsystemsfor pages 49-52
22. perkins2015modelsystemsfora pages 49-52
23. hewitt2023antioxidantenzymesthat pages 8-9
24. harper2017anatlasof pages 19-20
25. knoops2007evolutionofthe pages 1-4
26. qausain2024unravelingtheperoxidase pages 10-11
27. qausain2024unravelingtheperoxidase pages 11-12
28. https://doi.org/10.1016/j.cbpa.2023.102355
29. https://doi.org/10.3390/antiox12051012
30. https://doi.org/10.3390/cells12010181
31. https://doi.org/10.1038/s41598-023-29304-6
32. https://doi.org/10.1038/s41580-024-00730-2
33. https://doi.org/10.1093/nar/gkq1060
34. https://doi.org/10.14348/molcells.2016.2330
35. https://doi.org/10.1371/journal.pcbi.1005284
36. https://doi.org/10.1089/ars.2010.3624
37. https://doi.org/10.1021/bi5013222
38. https://doi.org/10.1089/ars.2010.3624,
39. https://doi.org/10.3390/antiox12051012,
40. https://doi.org/10.1016/j.cbpa.2023.102355,
41. https://doi.org/10.1371/journal.pcbi.1005284,
42. https://doi.org/10.1007/978-1-4020-6051-9\_2,
43. https://doi.org/10.1021/bi5013222,
44. https://doi.org/10.1093/nar/gkq1060,
45. https://doi.org/10.1016/j.tibs.2015.05.001,
46. https://doi.org/10.1146/annurev-biochem-060815-014431,
47. https://doi.org/10.1038/s41598-023-29304-6,
48. https://doi.org/10.3390/cells12010181,
49. https://doi.org/10.14348/molcells.2016.2330,
50. https://doi.org/10.7759/cureus.66117,