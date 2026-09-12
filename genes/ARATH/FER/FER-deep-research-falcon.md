Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Gene Research for GO Annotation Review

## Target

- Gene symbol: FER
- Organism: Arabidopsis thaliana

## UniProt Context

=== UNIPROT METADATA ===
UniProt ID: Q9SCZ4
Entry Name: FERON_ARATH
Gene Name: FER
Locus Tag: At3g51550 {ECO:0000312|Araport:AT3G51550}
Gene Synonyms: AAK1, SIR {ECO:0000303|PubMed:12620194}, SRN
Protein Name: Receptor-like protein kinase FERONIA
EC Number: 2.7.11.1
Organism: Arabidopsis thaliana (Mouse-ear cress)
NCBI Taxonomy ID: 3702
Function: Receptor-like protein kinase that mediates the female control of male gamete delivery during fertilization, including growth cessation of compatible pollen tubes ensuring a reproductive isolation barriers, by regulating MLO7 subcellular polarization upon pollen tube perception in the female gametophyte synergids. Required for cell elongation during vegetative growth, mostly in a brassinosteroids- (BR-) independent manner. Acts as an upstream regulator for the Rac/Rop-signaling pathway that controls ROS-mediated root hair development. Seems to regulate a cross-talk between brassinosteroids and ethylene signaling pathways during hypocotyl elongation. Negative regulator of brassinosteroid response in light- grown hypocotyls, but required for brassinosteroid response in etiolated seedlings. Mediates sensitivity to powdery mildew (e.g. Golovinomyces orontii). Positive regulator of auxin-promoted growth that represses the abscisic acid (ABA) signaling via the activation of ABI2 phosphatase. Required for RALF1-mediated extracellular alkalinization in a signaling pathway preventing cell expansion.
Subcellular Location: Cell membrane
Subunit: Interacts with ROPGEF1 (PubMed:20876100). Interacts with RALF1; triggering phosphorylation status and subsequent activation (PubMed:24458638). Interacts with LRE and LLG1 (PubMed:26052747). Interacts, via its extracellular domain, with FERONIA at the synergid cell surface (PubMed:27524487).
======================

## Research Objective

Prepare a comprehensive literature-backed research report for GO annotation review of the target gene.

Focus on:

1. The core biochemical activity of the gene product and any substrate specificity.
2. The activation or maturation mechanism of the protein, including proteolytic processing if relevant.
3. The best-supported subcellular localization and complexes where the active protein functions.
4. The strongest experimentally supported biological processes in the target organism, or in very close orthologs when transfer is justified.
5. Which annotations appear to reflect core function versus context-specific, pleiotropic, or over-extended roles.
6. Any evidence bearing on apoptosis, developmental cell death, neuronal roles, inflammatory signaling, pyroptosis, synaptic remodeling, protein processing, and localization to cytoplasm, cytosol, nucleus, or signaling complexes.

## Output Requirements

Structure the report as:

1. Executive summary
2. Molecular function
3. Biological process roles
4. Cellular localization and complexes
5. Annotation-risk assessment
6. Key literature

Use citations for all substantive claims.


## Gene Research Report for GO Annotation Review

### Target
- **Gene symbol:** FER (FERONIA)  
- **Organism:** *Arabidopsis thaliana*  
- **UniProt:** Q9SCZ4 (FERONIA_ARATH)  

---

## 1. Executive summary

FERONIA (FER) is a **plasma-membrane (cell-surface) malectin-like receptor kinase** of the CrRLK1L family that functions in **extracellular peptide perception and cell-wall–coupled signaling**. The best-supported core role in *Arabidopsis* is in **female-controlled pollen tube reception**, where FER in synergid cells is required for **pollen tube bursting/rupture and sperm release**, and mutants show strong, quantifiable fertility defects (e.g., ~80% of fer female gametophytes fail to trigger pollen-tube bursting; fer/fer plants produce ~20% of wild-type seed set) (cheung2024feroniaareceptor pages 3-4). 

Mechanistically, FER forms a **cell-surface coreceptor complex with LORELEI/LLG-family GPI-anchored proteins** and binds **RALF peptides**; structural work (summarized in a 2024 Annual Review) includes a solved **RALF23–LLG2–FER extracellular heterocomplex** (cheung2024feroniaareceptor pages 8-9, cheung2024feroniaareceptor pages 31-36). Downstream, FER couples to **ROPGEFs → RAC/ROP GTPases → NADPH oxidase–dependent ROS** that are required for **tip growth and cell integrity**, supporting roles in **root hair development/integrity** and ROS-associated growth control (li2016feroniaandher pages 4-5, cheung2024feroniaareceptor pages 31-36). 

Recent (2024) mechanistic work adds regulation of FER kinase activity by a phosphatase: the clade-H PP2C **PP2C12 binds FER and dephosphorylates its activation-loop Thr696**, tuning RALF1 sensitivity and root hair phenotypes (preprint evidence; quantitative assays n>100 per genotype, ANOVA P<0.01) (hou2024thephosphatasepp2c12 pages 9-14). 

FER is also repeatedly described as **pleiotropic**, with context-dependent roles in ABA and salt-stress responses and in immunity; these are supported by phenotypes and pathway associations but are higher risk for over-broad GO biological-process annotations compared with the core reproductive and RALF/ROS tip-growth modules (cheung2024feroniaareceptor pages 3-4, cheung2024feroniaareceptor pages 31-36). 

---

## 2. Molecular function

### 2.1 Key concepts and definitions (current understanding)

**Receptor-like protein kinase / Ser/Thr kinase:** FER is a single-pass transmembrane receptor kinase with a cytosolic Ser/Thr kinase domain (minkoff2017acellfreemethod pages 1-2). The 2024 review explicitly notes FER’s **self-phosphorylation** and places it as a signaling hub in cell-surface perception modules (cheung2024feroniaareceptor pages 1-3). 

**Malectin-like extracellular domains:** FER contains tandem malectin-like domains (MALA/MALB). Canonical carbohydrate-binding residues are not conserved, but the domain architecture is consistent with a role in binding peptide ligands and possibly cell-wall–associated cues (cheung2024feroniaareceptor pages 3-4, cheung2024feroniaareceptor pages 8-9). 

**RALF peptides:** RAPID ALKALINIZATION FACTOR peptides are secreted peptides that can induce extracellular alkalinization and growth changes. FER is one of the best-characterized RALF receptors, especially for RALF1 and RALF23 in reviewed literature (cheung2024feroniaareceptor pages 3-4). 

**LLG/LRE co-receptors (GPI-anchored proteins):** LORELEI (LRE) and LLG1 are GPI-anchored proteins that act as **chaperones and co-receptors**, promoting FER plasma-membrane delivery and functioning in FER signaling complexes (li2015glycosylphosphatidylinositolanchoredproteinsas pages 1-2, li2015glycosylphosphatidylinositolanchoredproteinsas pages 8-11). 

### 2.2 Core biochemical activity and substrate specificity

**Kinase activity:** FER has demonstrable protein kinase activity. In vitro reconstitution in lipid nanodiscs increased FER kinase activity versus soluble protein, and active-site residues (K565, K663) coordinating ATP were identified by ATP-analog labeling and mutagenesis (Minkoff et al., Apr 2017, JBC; https://doi.org/10.1074/jbc.m116.761981) (minkoff2017acellfreemethod pages 1-2). 

**In vivo targets/substrates:** The retrieved primary excerpts provide strong pathway placement (e.g., ROPGEF/ROP signaling; RALF-induced receptor phosphorylation), but limited direct in vivo substrate mapping. The 2024 review summarizes that FER phosphorylates multiple targets including **PhyB**, and transcription factors **MYC2** and **ABI5**, affecting nuclear accumulation/stability of these targets; however, these are summarized statements rather than assay details in the excerpts provided here (cheung2024feroniaareceptor pages 18-19). 

**Regulatory phosphosites:** A 2024 preprint demonstrates biochemical regulation of FER phosphorylation state: PP2C12 dephosphorylates FER’s cytoplasmic domain in vitro and phosphoproteomics implicates **Thr696** in the FER activation loop as a PP2C12-sensitive site (Hou et al., Nov 2024, bioRxiv; https://doi.org/10.1101/2024.11.05.622083) (hou2024thephosphatasepp2c12 pages 9-14). This provides unusually direct, site-level evidence relevant to kinase regulation.

### 2.3 Ligand binding and activation mechanism

**RALF binding:** Multiple lines of evidence support FER as a RALF receptor. RALF1 binds directly to the FER extracellular domain and RALF1 treatment enhances FER phosphorylation at C-terminal Ser residues (li2016feroniaandher pages 4-5). RALF1 association with a FER–LLG1 complex is supported by MBP-RALF1 pull-down capturing coexpressed FER and LLG1 (li2015glycosylphosphatidylinositolanchoredproteinsas pages 11-13). Structural evidence summarized in 2024 includes a solved **RALF23–LLG2–FER extracellular heterocomplex**, supporting a tripartite ligand–co-receptor–receptor activation architecture (cheung2024feroniaareceptor pages 8-9).

**Co-receptor dependence and trafficking as part of activation competence:** LLG1/LRE are pivotal for FER to reach the plasma membrane and signal. Loss of LLG1 causes FER-GFP retention in ER-like reticulate/perinuclear structures; co-expression of GPI-anchored LLG1 restores membrane localization, while a GPI-anchor–defective LLG1ΔC is much less effective (li2015glycosylphosphatidylinositolanchoredproteinsas pages 8-11). These data support that complex formation and trafficking are integral to functional receptor availability at the cell surface.

**Proteolytic processing/maturation:** No evidence in the retrieved excerpts supports proteolytic processing or maturation of FER itself (no receptor cleavage/ectodomain shedding/propeptide removal reported) (cheung2024feroniaareceptor pages 3-4, cheung2024feroniaareceptor pages 31-36).

---

## 3. Biological process roles

### 3.1 Strongest experimentally supported core processes

#### Pollen tube reception and sperm release (female fertility)
FER is a founding factor required for male–female communication at fertilization. In a large fraction of fer mutant female gametophytes, the penetrated pollen tube **fails to burst**, preventing sperm release and fertilization (cheung2024feroniaareceptor pages 3-4). Quantitative phenotypes summarized in the 2024 Annual Review include:
- ~**80%** of fer mutant female gametophytes: pollen tube fails to burst (cheung2024feroniaareceptor pages 3-4).
- Self-fertilized fer/fer plants produce ~**20%** of wild-type seed set (cheung2024feroniaareceptor pages 3-4).
- ~**80%** of ovules from fer/fer plants are sterile (cheung2024feroniaareceptor pages 3-4).

This is the single best-supported biological process annotation candidate for FER.

#### Root hair development / tip growth integrity and ROS signaling
FER is a key regulator of polarized growth processes, particularly root hairs. Loss of FER (and of LLG1) causes emerging root hairs to extrude cytoplasm and collapse, consistent with weakened cell wall/integrity (li2015glycosylphosphatidylinositolanchoredproteinsas pages 8-11). FER functions upstream of RAC/ROP activation and is required for **NADPH oxidase–dependent ROS production**, linking it to ROS-mediated growth and integrity (li2016feroniaandher pages 4-5, cheung2024feroniaareceptor pages 31-36).

#### RALF1-mediated growth inhibition and extracellular alkalinization
FER is required for cellular responses to RALF1, a peptide that triggers extracellular alkalinization and growth inhibition. fer mutants are described as RALF-insensitive in this context, and RALF1 induces FER phosphorylation changes (wolf2014growthcontrola pages 1-2, li2016feroniaandher pages 4-5). A 2024 preprint further ties RALF1 sensitivity to FER phosphorylation-state regulation by PP2C12 (hou2024thephosphatasepp2c12 pages 9-14).

### 3.2 Context-specific / pleiotropic processes (supported but higher GO-annotation risk)

#### ABA-related phenotypes
FER intersects with ABA-associated pathways: fer seedlings are **hypersensitive to ABA-suppressed seedling growth** and are defective in stomatal aperture closure regulation (cheung2024feroniaareceptor pages 3-4). This supports an ABA-response role, but its mechanistic proximity to core receptor function is less direct than in reproduction and RALF response.

#### Salt stress response
FER buffers high-salinity stress; under high salt conditions fer seedlings show **root cell bursting and arrested root growth** (cheung2024feroniaareceptor pages 31-36). This phenotype is robust but likely emerges from the broader cell-wall integrity and ROS signaling network, so GO terms should be chosen carefully to avoid implying FER is a dedicated salt sensor.

#### Immunity modulation
FER is implicated in immune outputs, including altered flg22-triggered ROS/MAPK responses and pathogen susceptibility patterns, as summarized in older reviews/perspectives and in pleiotropy discussions (wolf2014growthcontrola pages 1-2, li2016feroniaandher pages 2-4). However, immune-related annotations are particularly prone to over-extension because FER may modulate immunity indirectly through cell-wall integrity, ROS, and receptor-complex cross-talk.

---

## 4. Cellular localization and complexes

### 4.1 Best-supported localization

**Plasma membrane (cell membrane):** FER is described and experimentally supported as a plasma-membrane receptor. In wild-type vegetative tissues, pFER::FER-GFP localizes predominantly at the cell membrane, with negligible intracellular signal (li2015glycosylphosphatidylinositolanchoredproteinsas pages 8-11). The 2024 Annual Review also explicitly states FER is located in the cell membrane (cheung2024feroniaareceptor pages 3-4).

**Filiform apparatus (synergid cell region):** In ovules, FER-GFP localizes prominently at the filiform apparatus—a membrane-enriched cell-wall region where pollen tube reception occurs (li2015glycosylphosphatidylinositolanchoredproteinsas pages 8-11).

**Endoplasmic reticulum (trafficking/retention):** FER can accumulate in ER-like reticulate structures when LLG1/LRE are missing. ER-Tracker staining and RFP-ER co-localization support ER retention, consistent with a chaperone/co-receptor role for GPI-anchored LLG/LRE in FER secretory trafficking (li2015glycosylphosphatidylinositolanchoredproteinsas pages 8-11).

### 4.2 Complexes and interaction partners (experimentally supported)

**FER–LLG1 / FER–LRE complex (coreceptor/chaperone):** LLG1/LRE bind FER’s extracellular juxtamembrane region and are required for efficient FER plasma-membrane localization; interactions are supported by localization rescue, pull-downs, co-immunoprecipitation, and BiFC (li2015glycosylphosphatidylinositolanchoredproteinsas pages 1-2, li2015glycosylphosphatidylinositolanchoredproteinsas pages 11-13).

**FER–RALF complexes:** RALF1 association with a FER–LLG1 complex is supported by MBP-RALF1 pull-down capturing FER and LLG1 (li2015glycosylphosphatidylinositolanchoredproteinsas pages 11-13). Structural evidence summarized in 2024 supports a RALF23–LLG2–FER extracellular heterocomplex (cheung2024feroniaareceptor pages 8-9).

**FER–ROPGEF interaction:** FER interacts directly with ROPGEFs (cheung2024feroniaareceptor pages 3-4), providing a direct mechanistic link to RAC/ROP activation.

**FER–PP2C12 complex:** PP2C12 associates with FER (co-IP in *N. benthamiana* and Arabidopsis; BiFC peripheral signal) and dephosphorylates FER’s cytoplasmic domain (hou2024thephosphatasepp2c12 pages 9-14). This is recent (2024) and potentially important for GO annotation as “regulation of kinase activity” evidence.

---

## 5. Annotation-risk assessment (core vs over-extended)

### 5.1 High-confidence “core function” annotation set

1. **Receptor kinase activity / protein Ser/Thr kinase activity**: Strong biochemical evidence from nanodisc reconstitution and active-site mapping (minkoff2017acellfreemethod pages 1-2).  
2. **Plasma membrane receptor complex mediating peptide (RALF) signaling**: Physical complex and ligand association evidence (FER–LLG1/LRE; FER–RALF; structural RALF23–LLG–FER complex) (li2015glycosylphosphatidylinositolanchoredproteinsas pages 11-13, cheung2024feroniaareceptor pages 8-9).  
3. **Pollen tube reception and pollen tube bursting control**: Quantified fertility defects and mechanistic ROS-linked pollen tube rupture context (cheung2024feroniaareceptor pages 3-4, wolf2014growthcontrola pages 1-2).  
4. **Root hair development / tip growth integrity via RAC/ROP→ROS**: Strong phenotype and mechanistic linkage (li2015glycosylphosphatidylinositolanchoredproteinsas pages 8-11, li2016feroniaandher pages 4-5).  

These are most appropriate as “core” GO annotations.

### 5.2 Medium-confidence, context-dependent annotations

- **ABA response / seedling growth suppression / stomatal regulation**: Clear phenotypic evidence, but may be indirect through broader signaling network (cheung2024feroniaareceptor pages 3-4). 
- **Salt stress response**: Strong stress phenotype (root cell bursting and growth arrest) but likely via cell wall integrity/ROS and should be scoped narrowly (cheung2024feroniaareceptor pages 31-36). 
- **Immunity modulation**: Evidence exists for altered immune responses/pathogen outcomes, but causal molecular mechanisms may be indirect; avoid assigning overly specific immune signaling terms unless primary data support direct receptor complex roles (wolf2014growthcontrola pages 1-2, li2016feroniaandher pages 2-4).

### 5.3 High-risk annotations to avoid without additional evidence

- **Apoptosis / pyroptosis / inflammatory signaling / neuronal or synaptic roles:** Not biologically applicable and not supported by any evidence in plants (wolf2014growthcontrola pages 1-2, cheung2024feroniaareceptor pages 3-4). 
- **Programmed cell death (PCD) as a direct FER function:** Some sources use “cell death” language in mutant phenotype summaries or reproductive contexts, but the excerpts primarily describe **mechanical rupture/bursting** (pollen tube bursting; root hair/cell bursting) and do not provide canonical PCD markers. Therefore, annotating FER directly to PCD/apoptosis is not justified from the available evidence (li2016feroniaandher pages 2-4, cheung2024feroniaareceptor pages 31-36, hofte2015theyinand pages 9-10). 
- **Nuclear localization of FER:** Although FER’s kinase activity affects nuclear targets (MYC2, ABI5) per review summaries, none of the retrieved excerpts provide direct evidence that FER localizes to the nucleus; avoid GO cellular component annotations to nucleus for FER based solely on downstream nuclear signaling (cheung2024feroniaareceptor pages 18-19).
- **Proteolytic processing/maturation of FER:** No support in retrieved evidence (cheung2024feroniaareceptor pages 31-36).

---

## 6. Recent developments and applications (2023–2024 prioritized)

### 6.1 2024: Structural consolidation and network framing
The 2024 Annual Review of Plant Biology article frames FER as a **global signaling hub** and highlights structural advances including the **RALF23–LLG2–FER extracellular heterocomplex**, supporting a ligand–co-receptor–receptor model for signal perception and emphasizing FER’s pleiotropic integration with cell wall, membrane, cytoplasmic, and nuclear signaling networks (Cheung, Jul 2024; https://doi.org/10.1146/annurev-arplant-102820-103424) (cheung2024feroniaareceptor pages 8-9, cheung2024feroniaareceptor pages 31-36).

### 6.2 2024: Kinase regulation by PP2C12 (fine-tuning RALF/LRX/FER module)
Hou et al. (Nov 2024 preprint) provides a direct mechanistic connection between a PP2C phosphatase and FER kinase activation-loop phosphorylation. Key GO-relevant findings include:
- PP2C12 interacts with FER (co-IP; BiFC) (hou2024thephosphatasepp2c12 pages 9-14).
- PP2C12 dephosphorylates FERCD in vitro, with phosphoproteomics suggesting dephosphorylation at **Thr696** (hou2024thephosphatasepp2c12 pages 9-14).
- PP2C12-GFP overexpression reduces RALF1 sensitivity; quantitative phenotyping was performed with **n>100 per genotype** and significant differences (P<0.01) (hou2024thephosphatasepp2c12 pages 9-14).

These data support curated annotations around **regulation of receptor kinase activity** and **cell wall integrity signaling**, while noting preprint status.

### 6.3 Real-world implementations and translational framing
FER is widely discussed as a leverage point for **growth and resilience engineering** because it integrates RALF signaling, cell wall integrity, and stress responses; the 2024 Annual Review explicitly highlights the potential applications of FER-family modules for improving plant growth and resilience (cheung2024feroniaareceptor pages 3-4). While specific deployed agronomic products are not in the provided evidence, the described mechanisms (stress buffering; growth–defense balance) represent a plausible translational axis.

---

## 7. Evidence-to-annotation table

| GO aspect | Proposed GO annotation | Evidence summary | Experimental system/assay | Notes on scope | Key quantitative/statistical data if present | Primary citation with year and URL |
|---|---|---|---|---|---|---|
| MF | protein serine/threonine kinase activity | FER is a single-pass receptor-like Ser/Thr kinase with self-phosphorylation activity; reconstituted FER kinase activity was measured in lipid nanodiscs, and active-site Lys565/Lys663 were identified (cheung2024feroniaareceptor pages 1-3, minkoff2017acellfreemethod pages 1-2) | Cell-free expression in nanodiscs; kinase assay; ATP-analog labeling; mutagenesis; phosphoproteomics | Core function; strong support for kinase activity, but direct in vivo substrates remain limited in foundational papers | No effect size reported in excerpt; active-site residues K565 and K663 identified (minkoff2017acellfreemethod pages 1-2) | Minkoff et al. 2017, Journal of Biological Chemistry, https://doi.org/10.1074/jbc.m116.761981 |
| MF | peptide hormone binding | RALF1 binds the FER extracellular domain and RALF peptides bind the FER-LLG complex; RALF23-LLG2-FER extracellular heterocomplex has structural support (li2016feroniaandher pages 4-5, cheung2024feroniaareceptor pages 8-9) | Direct ligand-binding studies; radiolabeled ligand binding to membranes; pull-down with MBP-RALF1; structural complex determination | Core function; strongest ligand annotation is peptide binding rather than broad carbohydrate binding | Reduced radiolabeled RALF1 binding to fer membranes reported qualitatively (li2016feroniaandher pages 4-5) | Li et al. 2016, Plant Physiology, https://doi.org/10.1104/pp.16.00667; Cheung 2024, Annual Review of Plant Biology, https://doi.org/10.1146/annurev-arplant-102820-103424 |
| MF | signaling receptor activity | FER forms a cell-surface coreceptor pair with LLG proteins and perceives RALF peptides to initiate downstream signaling through ROPGEFs/RAC-ROPs (cheung2024feroniaareceptor pages 3-4, cheung2024feroniaareceptor pages 1-3) | Genetics; interaction studies; structural and review synthesis from primary literature | Core function; highly supported at pathway level | None in excerpt | Cheung 2024, Annual Review of Plant Biology, https://doi.org/10.1146/annurev-arplant-102820-103424 |
| MF | ROP guanyl-nucleotide exchange factor binding | FER directly interacts with ROPGEFs via its cytoplasmic region, linking receptor activation to RAC/ROP signaling (li2016feroniaandher pages 4-5, cheung2024feroniaareceptor pages 31-36, cheung2024feroniaareceptor pages 3-4) | Protein interaction studies; domain mapping | Core signaling mechanism; suitable for binding annotation if direct interaction is curated | No quantitative binding constants in excerpt | Li et al. 2016, Plant Physiology, https://doi.org/10.1104/pp.16.00667; Cheung 2024, Annual Review of Plant Biology, https://doi.org/10.1146/annurev-arplant-102820-103424 |
| MF | protein phosphatase binding | PP2C12 physically associates with FER and dephosphorylates the FER cytoplasmic domain at Thr696 in vitro (hou2024thephosphatasepp2c12 pages 9-14) | Co-IP in Nicotiana and Arabidopsis; BiFC; in vitro phosphatase assay; phosphoproteomics | Useful interaction annotation, but regulatory partner is from 2024 preprint and should be flagged as provisional | n>100 per genotype in associated phenotype assays; one-way ANOVA with Tukey unequal N-HSD, P<0.01 for root hair/RALF assays (hou2024thephosphatasepp2c12 pages 9-14) | Hou et al. 2024, bioRxiv, https://doi.org/10.1101/2024.11.05.622083 |
| BP | pollen tube reception | fer female gametophytes fail to induce pollen tube bursting after entry into the ovule, causing fertilization failure and pollen tube pileup (cheung2024feroniaareceptor pages 3-4, wolf2014growthcontrola pages 1-2) | Mutant phenotype analysis; reproductive microscopy; FER-GFP/ROS localization in synergids | Core, best-supported biological process in Arabidopsis | ~80% of fer mutant female gametophytes show failed pollen tube burst; ~80% of ovules from fer/fer are sterile; fer/fer plants produce ~20% of WT seed set (cheung2024feroniaareceptor pages 3-4) | Escobar-Restrepo et al. 2007 Science as summarized in Cheung 2024, https://doi.org/10.1146/annurev-arplant-102820-103424 |
| BP | regulation of pollen tube rupture | FER is required for ROS/hydroxyl radical production at the filiform apparatus, promoting pollen tube rupture and sperm release (wolf2014growthcontrola pages 1-2) | FER-GFP localization; ROS localization; mutant phenotype analysis | Core reproductive role; avoid overextending to generic programmed cell death | No quantitative value in excerpt | Duan et al. 2014 as summarized in Wolf & Höfte 2014, https://doi.org/10.1105/tpc.114.125518 |
| BP | root hair cell development | FER is a major regulator of root hair growth; fer root hairs burst/collapse with cytoplasmic leakage and reduced integrity (li2015glycosylphosphatidylinositolanchoredproteinsas pages 8-11, cheung2024feroniaareceptor pages 31-36) | Mutant phenotype analysis; imaging of emerging root hairs; genetic interaction | Core vegetative function; evidence supports tip-growth integrity more strongly than general root development | In Hou 2024 root hair scoring used n>100 per genotype with P<0.01 (hou2024thephosphatasepp2c12 pages 9-14) | Duan et al. 2010 and Li et al. 2015 as summarized in Li et al. 2015 eLife, https://doi.org/10.7554/elife.06587 |
| BP | reactive oxygen species biosynthetic process | Loss of FER reduces activated RAC/ROPs and suppresses NADPH oxidase-dependent ROS production in roots and root hairs (li2016feroniaandher pages 4-5, cheung2024feroniaareceptor pages 31-36) | Genetic analysis; RAC/ROP activation and ROS phenotypes | Core downstream process in polarized growth; annotate carefully as regulation/signaling-linked rather than direct catalytic ROS production by FER | No numeric effect size in excerpt | Li et al. 2016, Plant Physiology, https://doi.org/10.1104/pp.16.00667 |
| BP | cellular response to rapid alkalinization factor | fer mutants are RALF1-insensitive for root growth inhibition and alkalinization-linked responses; FER phosphorylation changes after RALF1 treatment (li2016feroniaandher pages 4-5, wolf2014growthcontrola pages 1-2) | Ligand treatment; mutant root growth assays; phospho-response assays | Core signaling response; strong GO-relevant process annotation | Hou 2024 used 2 µM RALF1 and found significant genotype effects, P<0.01 (hou2024thephosphatasepp2c12 pages 9-14) | Haruta et al. 2014 and Li et al. 2016 as summarized in Li et al. 2016, https://doi.org/10.1104/pp.16.00667 |
| BP | negative regulation of cell expansion | RALF1-FER signaling triggers extracellular alkalinization and growth arrest, likely via H+-ATPase regulation (li2016feroniaandher pages 4-5, wolf2014growthcontrola pages 1-2) | Peptide treatment; growth assays; phosphoproteomic inference on AHA2 | Strong but context-linked; best as process tied to RALF response rather than universal FER role | No numeric effect size in excerpt | Wolf & Höfte 2014, Plant Cell, https://doi.org/10.1105/tpc.114.125518 |
| BP | response to abscisic acid | fer seedlings are hypersensitive to ABA-suppressed growth and germination/greening defects are reported (cheung2024feroniaareceptor pages 3-4, cheung2024feroniaareceptor pages 31-36, cheung2024feroniaareceptor pages 18-19) | Mutant seedling phenotypes; hormone sensitivity assays | Context-specific/pleiotropic; not as core as reproduction or RALF signaling | No statistical values in excerpt | Cheung 2024, Annual Review of Plant Biology, https://doi.org/10.1146/annurev-arplant-102820-103424 |
| BP | response to salt stress | FER buffers high-salinity stress; fer seedlings show root cell bursting and root-growth arrest under salt stress (cheung2024feroniaareceptor pages 31-36, cheung2024feroniaareceptor pages 18-19) | Stress phenotype analysis | Context-specific; strong phenotype but not FER's primary GO core | No statistics in excerpt | Cheung 2024, Annual Review of Plant Biology, https://doi.org/10.1146/annurev-arplant-102820-103424 |
| BP | regulation of plant-type hypersensitive response / immune signaling | fer mutants show altered immunity, including enhanced flg22-triggered ROS/MAPK outputs and altered pathogen susceptibility (wolf2014growthcontrola pages 1-2, li2016feroniaandher pages 2-4) | Mutant pathogen phenotypes; immune elicitor responses | Annotation risk: immune roles are pleiotropic and context-dependent; avoid broad inflammatory analogies | No statistics in excerpt | Wolf & Höfte 2014, Plant Cell, https://doi.org/10.1105/tpc.114.125518 |
| CC | plasma membrane | FER-GFP localizes predominantly to the cell membrane in wild type tissues; FER is described as a cell-surface receptor kinase (li2015glycosylphosphatidylinositolanchoredproteinsas pages 8-11, cheung2024feroniaareceptor pages 3-4) | Stable/transient FER-GFP localization; microscopy | Best-supported cellular component | None | Li et al. 2015, eLife, https://doi.org/10.7554/elife.06587 |
| CC | filiform apparatus | In ovules, FER-GFP is enriched at the filiform apparatus of synergid cells, where pollen tube reception occurs (li2015glycosylphosphatidylinositolanchoredproteinsas pages 8-11) | Ovule imaging with FER-GFP | Strong localization in reproductive context; suitable as specialized PM-associated location if ontology permits | Localization compromised in lre mutants qualitatively (li2015glycosylphosphatidylinositolanchoredproteinsas pages 8-11) | Li et al. 2015, eLife, https://doi.org/10.7554/elife.06587 |
| CC | endoplasmic reticulum | In llg1/lre backgrounds FER-GFP accumulates in reticulate/perinuclear ER-like structures and colocalizes with ER markers, indicating trafficking through and retention in ER when chaperoning fails (li2015glycosylphosphatidylinositolanchoredproteinsas pages 8-11) | ER-Tracker; RFP-ER colocalization; protoplast cotransfection rescue | Annotation risk: ER localization reflects trafficking/retention, not the principal active site of FER function | llg1 rescue of PM localization significant at p<10^-2 in protoplast assay (li2015glycosylphosphatidylinositolanchoredproteinsas pages 8-11) | Li et al. 2015, eLife, https://doi.org/10.7554/elife.06587 |
| CC | receptor complex | FER forms complexes with LLG1/LRE at the cell surface and with RALF peptides; structural evidence supports RALF23-LLG2-FER extracellular heterocomplex (li2015glycosylphosphatidylinositolanchoredproteinsas pages 11-13, li2015glycosylphosphatidylinositolanchoredproteinsas pages 16-17, cheung2024feroniaareceptor pages 31-36) | Co-IP; pull-down; BiFC; structural complex determination | Core complex annotation strongly supported | None in excerpt | Li et al. 2015, eLife, https://doi.org/10.7554/elife.06587; Cheung 2024, Annual Review of Plant Biology, https://doi.org/10.1146/annurev-arplant-102820-103424 |
| CC | membrane microdomain | FER trafficking/recruitment to membrane microdomains is discussed and supported by detergent-resistant membrane partitioning and LLG-dependent targeting (li2016feroniaandher pages 4-5, cheung2024feroniaareceptor pages 31-36, li2016feroniaandher pages 2-4) | Membrane fractionation; trafficking studies; review synthesis | Moderate annotation risk: evidence supports regulated partitioning, but term choice should match direct assay resolution | Qualitative only in excerpt | Li et al. 2016, Plant Physiology, https://doi.org/10.1104/pp.16.00667 |
| BP | programmed cell death | Evidence does not support direct FER annotation to apoptosis/PCD; reported phenotypes are pollen tube bursting failure, root hair/cell bursting, and occasional generic 'cell death' descriptions without canonical PCD markers (hofte2015theyinand pages 9-10, wolf2014growthcontrola pages 1-2, cheung2024feroniaareceptor pages 31-36) | Phenotype descriptions; review synthesis | High annotation risk; avoid unless primary molecular PCD markers are available | None | Wolf & Höfte 2014, Plant Cell, https://doi.org/10.1105/tpc.114.125518; Cheung 2024, Annual Review of Plant Biology, https://doi.org/10.1146/annurev-arplant-102820-103424 |
| CC | nucleus | No direct evidence in retrieved excerpts that FER itself localizes to the nucleus; FER can phosphorylate nuclear-acting targets such as MYC2 and ABI5, but this does not justify nuclear localization of FER (cheung2024feroniaareceptor pages 18-19, cheung2024feroniaareceptor pages 1-3) | Review synthesis of kinase-target studies | High annotation risk; do not annotate FER to nucleus based on downstream nuclear signaling alone | None | Cheung 2024, Annual Review of Plant Biology, https://doi.org/10.1146/annurev-arplant-102820-103424 |


*Table: This table maps the strongest GO-relevant evidence for Arabidopsis FERONIA to molecular function, biological process, and cellular component claims. It is designed to help distinguish core annotations from context-specific or high-risk overextensions during GO review.*

---

## 8. Key literature (GO-relevant; with publication dates and URLs)

1. **Cheung, A.Y. (Jul 2024).** *FERONIA: A Receptor Kinase at the Core of a Global Signaling Network.* **Annual Review of Plant Biology** 75:345–375. https://doi.org/10.1146/annurev-arplant-102820-103424 (cheung2024feroniaareceptor pages 3-4, cheung2024feroniaareceptor pages 8-9)
2. **Hou, X. et al. (Nov 2024).** *The phosphatase PP2C12 is a negative player in LRX-RALF-FER-mediated cell wall integrity sensing.* **bioRxiv**. https://doi.org/10.1101/2024.11.05.622083 (hou2024thephosphatasepp2c12 pages 9-14)
3. **Li, C. et al. (Jun 2015).** *GPI-anchored proteins as chaperones and co-receptors for FERONIA receptor kinase signaling in Arabidopsis.* **eLife** 4:e06587. https://doi.org/10.7554/eLife.06587 (li2015glycosylphosphatidylinositolanchoredproteinsas pages 8-11, li2015glycosylphosphatidylinositolanchoredproteinsas pages 11-13)
4. **Li, C. et al. (Jun 2016).** *FERONIA and Her Pals: Functions and Mechanisms.* **Plant Physiology** 171:2379–2392. https://doi.org/10.1104/pp.16.00667 (li2016feroniaandher pages 4-5, li2016feroniaandher pages 2-4)
5. **Minkoff, B.B. et al. (Apr 2017).** *Cell-free expression and reconstitution enables functional characterization of FERONIA.* **Journal of Biological Chemistry** 292:5932–5942. https://doi.org/10.1074/jbc.m116.761981 (minkoff2017acellfreemethod pages 1-2)
6. **Wolf, S. & Höfte, H. (May 2014).** *Growth Control: A Saga of Cell Walls, ROS, and Peptide Receptors.* **The Plant Cell** 26:1848–1856. https://doi.org/10.1105/tpc.114.125518 (wolf2014growthcontrola pages 1-2)
7. **Höfte, H. (Feb 2015).** *The yin and yang of cell wall integrity control: brassinosteroid and FERONIA signaling.* **Plant & Cell Physiology** 56:224–231. https://doi.org/10.1093/pcp/pcu182 (hofte2015theyinand pages 9-10)



References

1. (cheung2024feroniaareceptor pages 3-4): Alice Y. Cheung. Feronia: a receptor kinase at the core of a global signaling network. Jul 2024. URL: https://doi.org/10.1146/annurev-arplant-102820-103424, doi:10.1146/annurev-arplant-102820-103424. This article has 78 citations and is from a domain leading peer-reviewed journal.

2. (cheung2024feroniaareceptor pages 8-9): Alice Y. Cheung. Feronia: a receptor kinase at the core of a global signaling network. Jul 2024. URL: https://doi.org/10.1146/annurev-arplant-102820-103424, doi:10.1146/annurev-arplant-102820-103424. This article has 78 citations and is from a domain leading peer-reviewed journal.

3. (cheung2024feroniaareceptor pages 31-36): Alice Y. Cheung. Feronia: a receptor kinase at the core of a global signaling network. Jul 2024. URL: https://doi.org/10.1146/annurev-arplant-102820-103424, doi:10.1146/annurev-arplant-102820-103424. This article has 78 citations and is from a domain leading peer-reviewed journal.

4. (li2016feroniaandher pages 4-5): Chao Li, H.-M. Wu, and Alice Y. Cheung. Feronia and her pals: functions and mechanisms1[open]. Plant Physiology, 171:2379-2392, Jun 2016. URL: https://doi.org/10.1104/pp.16.00667, doi:10.1104/pp.16.00667. This article has 216 citations and is from a highest quality peer-reviewed journal.

5. (hou2024thephosphatasepp2c12 pages 9-14): Xiaoyu Hou, Kyle W. Bender, Gabor Kadler, Shibu Gupta, Mona Häfliger, Amandine Guérin, Anouck Diet, Stefan Roffler, Daniela Campanini, Thomas Wicker, Cyril Zipfel, and Christoph Ringli. The phosphatase pp2c12 is a negative player in lrx-ralf-fer-mediated cell wall integrity sensing. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.05.622083, doi:10.1101/2024.11.05.622083. This article has 1 citations.

6. (minkoff2017acellfreemethod pages 1-2): Benjamin B. Minkoff, Shin-ichi Makino, Miyoshi Haruta, Emily T. Beebe, Russell L. Wrobel, Brian G. Fox, and Michael R. Sussman. A cell-free method for expressing and reconstituting membrane proteins enables functional characterization of the plant receptor-like protein kinase feronia. Journal of Biological Chemistry, 292:5932-5942, Apr 2017. URL: https://doi.org/10.1074/jbc.m116.761981, doi:10.1074/jbc.m116.761981. This article has 27 citations and is from a domain leading peer-reviewed journal.

7. (cheung2024feroniaareceptor pages 1-3): Alice Y. Cheung. Feronia: a receptor kinase at the core of a global signaling network. Jul 2024. URL: https://doi.org/10.1146/annurev-arplant-102820-103424, doi:10.1146/annurev-arplant-102820-103424. This article has 78 citations and is from a domain leading peer-reviewed journal.

8. (li2015glycosylphosphatidylinositolanchoredproteinsas pages 1-2): Chao Li, Fang-Ling Yeh, Alice Y Cheung, Qiaohong Duan, Daniel Kita, Ming-Che Liu, Jacob Maman, Emily J Luu, Brendan W Wu, Laura Gates, Methun Jalal, Amy Kwong, Hunter Carpenter, and Hen-Ming Wu. Glycosylphosphatidylinositol-anchored proteins as chaperones and co-receptors for feronia receptor kinase signaling in arabidopsis. eLife, Jun 2015. URL: https://doi.org/10.7554/elife.06587, doi:10.7554/elife.06587. This article has 370 citations and is from a domain leading peer-reviewed journal.

9. (li2015glycosylphosphatidylinositolanchoredproteinsas pages 8-11): Chao Li, Fang-Ling Yeh, Alice Y Cheung, Qiaohong Duan, Daniel Kita, Ming-Che Liu, Jacob Maman, Emily J Luu, Brendan W Wu, Laura Gates, Methun Jalal, Amy Kwong, Hunter Carpenter, and Hen-Ming Wu. Glycosylphosphatidylinositol-anchored proteins as chaperones and co-receptors for feronia receptor kinase signaling in arabidopsis. eLife, Jun 2015. URL: https://doi.org/10.7554/elife.06587, doi:10.7554/elife.06587. This article has 370 citations and is from a domain leading peer-reviewed journal.

10. (cheung2024feroniaareceptor pages 18-19): Alice Y. Cheung. Feronia: a receptor kinase at the core of a global signaling network. Jul 2024. URL: https://doi.org/10.1146/annurev-arplant-102820-103424, doi:10.1146/annurev-arplant-102820-103424. This article has 78 citations and is from a domain leading peer-reviewed journal.

11. (li2015glycosylphosphatidylinositolanchoredproteinsas pages 11-13): Chao Li, Fang-Ling Yeh, Alice Y Cheung, Qiaohong Duan, Daniel Kita, Ming-Che Liu, Jacob Maman, Emily J Luu, Brendan W Wu, Laura Gates, Methun Jalal, Amy Kwong, Hunter Carpenter, and Hen-Ming Wu. Glycosylphosphatidylinositol-anchored proteins as chaperones and co-receptors for feronia receptor kinase signaling in arabidopsis. eLife, Jun 2015. URL: https://doi.org/10.7554/elife.06587, doi:10.7554/elife.06587. This article has 370 citations and is from a domain leading peer-reviewed journal.

12. (wolf2014growthcontrola pages 1-2): Sebastian Wolf and Herman Höfte. Growth control: a saga of cell walls, ros, and peptide receptors. Plant Cell, 26:1848-1856, May 2014. URL: https://doi.org/10.1105/tpc.114.125518, doi:10.1105/tpc.114.125518. This article has 127 citations and is from a highest quality peer-reviewed journal.

13. (li2016feroniaandher pages 2-4): Chao Li, H.-M. Wu, and Alice Y. Cheung. Feronia and her pals: functions and mechanisms1[open]. Plant Physiology, 171:2379-2392, Jun 2016. URL: https://doi.org/10.1104/pp.16.00667, doi:10.1104/pp.16.00667. This article has 216 citations and is from a highest quality peer-reviewed journal.

14. (hofte2015theyinand pages 9-10): Herman Höfte. The yin and yang of cell wall integrity control: brassinosteroid and feronia signaling. Plant & cell physiology, 56 2:224-31, Feb 2015. URL: https://doi.org/10.1093/pcp/pcu182, doi:10.1093/pcp/pcu182. This article has 80 citations and is from a domain leading peer-reviewed journal.

15. (li2015glycosylphosphatidylinositolanchoredproteinsas pages 16-17): Chao Li, Fang-Ling Yeh, Alice Y Cheung, Qiaohong Duan, Daniel Kita, Ming-Che Liu, Jacob Maman, Emily J Luu, Brendan W Wu, Laura Gates, Methun Jalal, Amy Kwong, Hunter Carpenter, and Hen-Ming Wu. Glycosylphosphatidylinositol-anchored proteins as chaperones and co-receptors for feronia receptor kinase signaling in arabidopsis. eLife, Jun 2015. URL: https://doi.org/10.7554/elife.06587, doi:10.7554/elife.06587. This article has 370 citations and is from a domain leading peer-reviewed journal.