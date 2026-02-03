# SPKW Apoptosis Subproject

**Parent project:** [SPKW.md](SPKW.md)

## Overview

This subproject identifies human proteins annotated to "apoptotic process" (GO:0006915) or descendants where the **only** evidence comes from UniProt Keywords mapping (GO_REF:0000043). These annotations lack corroboration from any other source (experimental, computational, or curator statements).

The goal is to review these annotations to determine if they are well-supported by literature or if they represent cases where the UniProt "Apoptosis" keyword was applied but the connection to apoptosis is weak or indirect.

## Query Methodology

Using DuckDB on `~/repos/go-db/db/goa_human.ddb`:

```sql
-- Find proteins with apoptotic process annotations ONLY from UniProt Keywords
WITH all_apoptotic AS (
    SELECT a.db_object_id, a.db_object_symbol, a.supporting_references
    FROM gaf_association a
    INNER JOIN isa_partof_closure ipc ON a.ontology_class_ref = ipc.subject
    WHERE ipc.object = 'GO:0006915'  -- apoptotic process
      AND a.is_negation = false
),
genes_with_other_evidence AS (
    SELECT DISTINCT db_object_id
    FROM all_apoptotic
    WHERE supporting_references != 'GO_REF:0000043'
),
spkw_only_genes AS (
    SELECT DISTINCT db_object_id, db_object_symbol
    FROM all_apoptotic
    WHERE supporting_references = 'GO_REF:0000043'
      AND db_object_id NOT IN (SELECT db_object_id FROM genes_with_other_evidence)
)
SELECT * FROM spkw_only_genes ORDER BY db_object_symbol;
```

## Summary Statistics (Human - goa_human.ddb)

- **Total SPKW-only genes with apoptotic process annotations**: 280
- **Source**: GO_REF:0000043 (UniProtKB-KW → GO mapping)

## Status

- Total reviewed: 23/280 genes (8.2%)
- Issue rate: 87% (20/23) - includes OVER-ANNOTATION and MODIFY
- Legitimate for GO:0006915: 3 (API5, AVEN, BCL2L12)
- MODIFY to regulatory term: 1 (AIMP2 → GO:0043065)

## Genes for Review (Sample - Alphabetical)

| Gene | UniProt | Description | Status | Notes |
|------|---------|-------------|--------|-------|
| ADAMTSL4 | Q6UY14 | ADAMTS-like protein 4 | **REVIEWED - OVER-ANNOTATION** | |
| AIMP1 | Q12904 | tRNA synthase complex protein 1 | **REVIEWED - OVER-ANNOTATION** | Caspase substrate |
| AIMP2 | Q13155 | tRNA synthase complex protein 2 | **REVIEWED - MODIFY** | Moonlighting; core=MSC scaffold |
| AKTIP | Q9H8T0 | AKT-interacting protein | **REVIEWED - OVER-ANNOTATION** | |
| APBB1 | O00213 | Amyloid beta A4 precursor protein-binding protein | **REVIEWED - OVER-ANNOTATION** | |
| API5 | Q9BZZ5 | Apoptosis inhibitor 5 | **REVIEWED - LEGITIMATE** | Evolved anti-apoptotic |
| APIP | Q96GX9 | Methylthioribulose-1-phosphate dehydratase | **REVIEWED - OVER-ANNOTATION** | Core=methionine salvage |
| APLP1 | P51693 | Amyloid-like protein 1 | **REVIEWED - OVER-ANNOTATION** | |
| AREL1 | O15033 | Apoptosis-resistant E3 ubiquitin ligase 1 | **REVIEWED - OVER-ANNOTATION** | |
| ARL6IP1 | Q15041 | ADP-ribosylation factor-like protein 6-interacting protein 1 | **REVIEWED - OVER-ANNOTATION** | Core=ER shaping |
| ASAH2 | Q9NR71 | Neutral ceramidase | **REVIEWED - OVER-ANNOTATION** | Core=ceramide metabolism |
| ATG4D | Q86TL0 | Cysteine protease ATG4D | **REVIEWED - OVER-ANNOTATION** | Core=autophagy |
| ATG5 | Q9H1Y0 | Autophagy protein 5 | **REVIEWED - OVER-ANNOTATION** | Core=autophagy |
| AVEN | Q9NQS1 | Cell death regulator Aven | **REVIEWED - LEGITIMATE** | Evolved anti-apoptotic |
| AXIN1 | O15169 | Axin-1 | **REVIEWED - OVER-ANNOTATION** | Core=Wnt signaling |
| BABAM2 | Q9NXR7 | BRISC and BRCA1-A complex member 2 | pending | |
| BAG1 | Q99933 | BAG family molecular chaperone regulator 1 | **REVIEWED - OVER-ANNOTATION** | Core=Hsp70 co-chaperone |
| BCAP29 | Q9UHQ4 | B-cell receptor-associated protein 29 | pending | |
| BCAP31 | P51572 | B-cell receptor-associated protein 31 | **REVIEWED - OVER-ANNOTATION** | Caspase substrate |
| BCL2L12 | Q9HB09 | Bcl-2-like protein 12 | **REVIEWED - LEGITIMATE** | Bcl-2 family |
| BECN1 | Q14457 | Beclin-1 | **REVIEWED - OVER-ANNOTATION** | Core=autophagy |
| BIRC5 | O15392 | Baculoviral IAP repeat-containing protein 5 (survivin) | **REVIEWED - OVER-ANNOTATION** | Core=mitosis (CPC) |
| C1QBP | Q07021 | Complement C1q-binding protein | **REVIEWED - OVER-ANNOTATION** | Core=mt-translation |
| CD47 | Q08722 | Leukocyte surface antigen CD47 | **REVIEWED - OVER-ANNOTATION** | Core=phagocytosis checkpoint |
| CDK1 | P06493 | Cyclin-dependent kinase 1 | **REVIEWED - OVER-ANNOTATION** | Core=cell cycle |

*Full list: 280 genes total - see query above to regenerate*

---

## Pilot Batch Review Results

Selected 5 genes that appeared suspicious for over-annotation based on names (e.g., "tRNA synthase complex protein").

**Key Principle Applied:** Over-annotation occurs when a protein is annotated to "apoptotic process" based on:
- Being a **substrate/target** of apoptosis machinery (not participating IN apoptosis)
- Having **causal downstream effects** on apoptosis through pleiotropic mechanisms
- Having effects at **pharmacological concentrations** rather than physiological
- Performing a **different core function** where apoptotic effects are secondary

An **evolved regulatory mechanism** is different - this requires evidence that the gene product specifically evolved to regulate apoptosis as part of its function.

| Gene | Core Function | Apoptosis Relationship | Assessment |
|------|---------------|------------------------|------------|
| **AIMP1** | MSC scaffold, tRNA binding | Cleaved BY caspase-7 → releases EMAP-II; EMAP-II "induces apoptosis at high concentrations" | **OVER-ANNOTATION** - being a caspase substrate ≠ participating in apoptosis; EMAP-II effect is pharmacological |
| **AIMP2** | MSC scaffold | Proapoptotic via p53 stabilization (blocks MDM2); stress-responsive nuclear translocation | **MODIFY** → GO:0043065 (positive regulation of apoptotic process). Genuine evolved moonlighting function, but AIMP2 REGULATES apoptosis via p53, doesn't participate IN apoptotic process |
| **APIP** | Methionine salvage enzyme (MtnB) | Moonlighting: binds Apaf-1, inhibits apoptosis; enzymatic activity dispensable for anti-apoptotic effect | **OVER-ANNOTATION** - core function is metabolic; apoptosis effect is moonlighting; INHIBITS not participates |
| **ARL6IP1** | ER membrane shaping (reticulon-like) | Named "ARMER"; inhibits CASP9-dependent apoptosis | **OVER-ANNOTATION** - anti-apoptotic effect likely secondary to ER homeostasis; deep research is all about ER morphology |
| **ASAH2** | Neutral ceramidase (sphingolipid metabolism) | Reduces ceramide → shifts ceramide/S1P balance toward survival | **OVER-ANNOTATION** - metabolic enzyme; apoptotic effect is downstream of ceramide catabolism, not an evolved regulatory function |

**Results: 5 of 5 genes have issues with GO:0006915. AIMP2 has a genuine apoptosis-related function but requires MODIFY to regulatory term.**

---

## Detailed Gene Analysis

### AIMP1 (Q12904) - tRNA synthase complex protein 1

**Core evolved function:** Scaffold/organizing subunit of the multi-aminoacyl tRNA synthetase complex (MSC); has OB-fold for tRNA binding.

**Apoptosis connection:**
- Cleaved BY caspase-7 during apoptosis → releases EMAP-II cytokine
- EMAP-II has proinflammatory effects and "induces apoptosis at high concentrations"

**Why OVER-ANNOTATION:**
- Being **cleaved BY caspases** makes you a **target/substrate** of apoptosis, not a participant IN the apoptotic process
- EMAP-II inducing apoptosis "at high concentrations" is a **pharmacological effect**, not a physiological evolved function
- 2024 literature focuses on EMAP-II as a stress/inflammation signal, not as having an evolved proapoptotic role
- Core function is clearly the MSC scaffold role

---

### AIMP2 (Q13155) - tRNA synthase complex protein 2

**Core evolved function:** MSC scaffold (multi-aminoacyl-tRNA synthetase complex).

**Apoptosis connection:**
- Moonlighting function: upon DNA damage, AIMP2 is phosphorylated, dissociates from MSC, translocates to nucleus
- Mechanism: blocks MDM2-mediated ubiquitination of p53, thereby stabilizing p53
- p53 then activates apoptotic genes
- Evidence (PMID:18695251): AIMP2 depletion → resistance to apoptosis; reintroduction → susceptibility restored

**Why MODIFY (not LEGITIMATE for GO:0006915):**
- The evidence is **phenotypic**: cells ± AIMP2 differ in apoptosis susceptibility
- The mechanism is **regulatory**: AIMP2 → blocks MDM2 → stabilizes p53 → p53 activates apoptosis
- AIMP2 does NOT directly participate in apoptotic process execution (caspase cascades, MOMP, DNA fragmentation)
- This is a genuine evolved moonlighting function, but the correct term is **GO:0043065 (positive regulation of apoptotic process)**
- Analogous to APBB1 - both regulate apoptosis but don't participate IN apoptosis

---

### APIP (Q96GX9) - Methylthioribulose-1-phosphate dehydratase

**Core evolved function:** Enzyme in the **methionine salvage pathway** (MtnB step). Catalyzes dehydration of MTRu-1-P.

**Apoptosis connection:**
- Named "APAF1-interacting protein" because it binds Apaf-1
- Competes with procaspase-9 for Apaf-1 binding, thereby inhibiting apoptosome
- Key finding: "APIP's enzymatic activity is **dispensable** for anti-apoptotic effects" - this is a moonlighting function

**Why OVER-ANNOTATION:**
- Primary evolved function is **methionine salvage** (metabolic)
- The Apaf-1 binding is a real moonlighting function, but:
  - It **INHIBITS** apoptosis, doesn't participate in it
  - "Apoptotic process" (GO:0006915) implies direct participation
  - The regulatory annotation (GO:0043066) is more accurate

---

### ARL6IP1 (Q15041) - ADP-ribosylation factor-like protein 6-interacting protein 1

**Core evolved function:** **ER membrane-shaping protein** with reticulon-like hairpins that generate positive membrane curvature and promote tubular ER formation.

**Apoptosis connection:**
- Named "ARMER" (Apoptotic regulator in the membrane of the ER)
- Has IDA evidence for GO:0043066 (negative regulation of apoptotic process)
- Inhibits CASP9-dependent apoptosis

**Why OVER-ANNOTATION:**
- Deep research is **entirely about ER morphology**, not apoptosis
- Loss of protein → disrupted ER structure → ER stress → cell death
- This is a **downstream consequence** of ER dysfunction, not an evolved apoptosis regulatory function
- Anti-apoptotic effect likely reflects the importance of proper ER structure for cell viability
- Linked to hereditary spastic paraplegia (HSP) via ER dysfunction, not apoptosis dysregulation

---

### ASAH2 (Q9NR71) - Neutral ceramidase

**Core evolved function:** **Neutral ceramidase enzyme** (EC 3.5.1.23). Hydrolyzes ceramide → sphingosine + fatty acid. Primary role in intestinal digestion of dietary sphingolipids.

**Apoptosis connection:**
- Ceramide is generally proapoptotic; sphingosine-1-phosphate (S1P) is pro-survival
- By breaking down ceramide, ASAH2 shifts the balance toward survival signaling
- Has IMP evidence for GO:2001234 (negative regulation of apoptotic signaling pathway)

**Why OVER-ANNOTATION:**
- This is exactly the "**causal downstream effect**" pattern
- Core function is **ceramide metabolism** (especially dietary sphingolipids in intestine)
- The anti-apoptotic effect is a **metabolic consequence** of reducing ceramide levels
- The enzyme didn't evolve TO regulate apoptosis - it evolved to metabolize ceramides, and ceramides happen to be involved in apoptotic signaling
- Deep research emphasizes intestinal brush border function and dietary sphingolipid catabolism

---

## Batch 2 Review Results

Expanded review to 15 additional genes using the strict over-annotation criteria established in the pilot batch.

| Gene | UniProt | Core Function | Assessment | Rationale |
|------|---------|---------------|------------|-----------|
| **ADAMTSL4** | Q6UY14 | ECM/microfibril organization for lens zonules | **OVER-ANNOTATION** | No apoptosis function in literature; core function is extracellular matrix assembly |
| **AKTIP** | Q9H8T0 | Telomere replication support, ESCRT function | **OVER-ANNOTATION** | No apoptosis function; UEV-domain protein for telomere/cytokinesis |
| **API5** | Q9BZZ5 | Anti-apoptotic scaffold | **LEGITIMATE** | Evolved anti-apoptotic mechanisms: binds caspase-2 CARD, protects Acinus from cleavage |
| **ATG4D** | Q86TL0 | Autophagy protease (LC3/GABARAP processing) | **OVER-ANNOTATION** | Core function is autophagy; no evolved apoptosis function |
| **ATG5** | Q9H1Y0 | Autophagy E3-like (ATG12-ATG5-ATG16L1) | **OVER-ANNOTATION** | Core function is autophagosome biogenesis; apoptosis effects are secondary |
| **AVEN** | Q9NQS1 | Anti-apoptotic (BCL-XL/Apaf-1 binding) | **LEGITIMATE** | Evolved anti-apoptotic function: binds BCL-XL, inhibits Apaf-1/apoptosome, has BH3-like motif |
| **AXIN1** | O15169 | Wnt signaling scaffold (β-catenin destruction) | **OVER-ANNOTATION** | Core function is Wnt/β-catenin pathway; no apoptosis mentioned in research |
| **BAG1** | Q99933 | Hsp70 co-chaperone/nucleotide exchange factor | **OVER-ANNOTATION** | Core function is proteostasis/chaperoning; BCL2 binding is secondary |
| **BCAP31** | P51572 | ER cargo receptor/quality control | **OVER-ANNOTATION** | Core function is ER QC; is a caspase-8 substrate (like AIMP1) |
| **BCL2L12** | Q9HB09 | Anti-apoptotic (caspase/p53 inhibition) | **LEGITIMATE** | Evolved function: directly inhibits caspase-7, antagonizes p53, Bcl-2 family member |
| **BECN1** | Q14457 | Autophagy (PI3KC3 scaffold) | **OVER-ANNOTATION** | Core function is autophagy; BCL2 interaction regulates autophagy, not apoptosis |
| **BIRC5** | O15392 | Mitosis (CPC component) | **OVER-ANNOTATION** | "survivin's best-established function is mitotic CPC"; anti-apoptotic effects are indirect |
| **C1QBP** | Q07021 | Mitochondrial RNA binding, complement receptor | **OVER-ANNOTATION** | Core functions are mt-translation and C1q binding; no apoptosis core function |
| **CD47** | Q08722 | Phagocytosis checkpoint ("don't eat me") | **OVER-ANNOTATION** | Core function is innate immune checkpoint (SIRPα); not apoptosis |
| **CDK1** | P06493 | Cell cycle kinase (G2/M transition) | **OVER-ANNOTATION** | Core function is cell cycle; phosphorylates apoptosis substrates but that's not its evolved function |

**Results Summary: 12 OVER-ANNOTATION, 3 LEGITIMATE**

---

## Detailed Analysis - Batch 2 Legitimate Genes

### API5 (Q9BZZ5) - Apoptosis inhibitor 5

**Core evolved function:** Anti-apoptotic scaffold protein with HEAT/ARM-like helical repeat architecture.

**Why LEGITIMATE:**
- **Direct caspase-2 inhibition:** Binds the CARD domain of caspase-2, preventing dimerization/activation
- **Acinus protection:** Binds Acinus and protects it from caspase-3 cleavage, blocking DNA fragmentation
- **E2F1 axis modulation:** Suppresses E2F1-dependent apoptosis
- All mechanisms are specific, evolved anti-apoptotic functions, not pleiotropic effects

---

### AVEN (Q9NQS1) - Cell death regulator Aven

**Core evolved function:** Anti-apoptotic regulator.

**Why LEGITIMATE:**
- **BCL-XL binding:** Direct interaction with BCL-XL, stabilizing it and potentiating its anti-apoptotic function
- **Apaf-1 inhibition:** Binds Apaf-1, preventing apoptosome assembly and caspase-9 activation
- **BH3-like motif:** Predicted BH3-like sequence (aa 141-153) for BCL-XL interaction
- **Proteolytic regulation:** Cathepsin D cleaves N-terminus to release potent anti-apoptotic C-terminal fragment
- Specific evolved mechanisms, not downstream/metabolic effects

---

### BCL2L12 (Q9HB09) - Bcl-2-like protein 12

**Core evolved function:** Anti-apoptotic Bcl-2 family member.

**Why LEGITIMATE:**
- **Direct caspase inhibition:** Inhibits effector caspase-7 (and possibly caspase-3)
- **p53 antagonism:** Binds and neutralizes p53 transcriptional activity
- **Bcl-2 family member:** Has BH3-like motif, part of the evolved apoptosis regulatory network
- Named appropriately - this is a bona fide anti-apoptotic protein with evolved mechanisms

---

## Detailed Analysis - Batch 2 Over-Annotations (Selected)

### BIRC5/Survivin (O15392)

**Why OVER-ANNOTATION despite "Apoptosis inhibitor" name:**
- Deep research states: "survivin's best-established function is as an essential CPC component regulating mitotic progression"
- "Anti-apoptotic effects are context-dependent and likely mediated by networks (XIAP, SMAC) rather than direct caspase inhibition"
- Core evolved function is **mitosis** (Chromosomal Passenger Complex), not apoptosis
- This is a case where the gene NAME is misleading - the protein evolved for cell division, with indirect anti-apoptotic effects

### ATG5 (Q9H1Y0)

**Why OVER-ANNOTATION despite "Apoptosis-specific protein" alias:**
- Core function is autophagy: E3-like activity in ATG12-ATG5-ATG16L1 complex for LC3 lipidation
- While autophagy and apoptosis have crosstalk, ATG5's evolved function is autophagosome biogenesis
- The UniProt alias "Apoptosis-specific protein" reflects early naming, not current functional understanding

### CDK1 (P06493)

**Why OVER-ANNOTATION:**
- Core function is cell cycle control (essential G2/M transition kinase)
- 2023 review notes CDK1 phosphorylates "caspase-9, Bcl-2 family, survivin" among its 1000+ substrates
- Phosphorylating apoptosis-related proteins as part of cell cycle doesn't make apoptosis its evolved function
- This is like annotating a transcription factor to all processes its target genes are involved in

---

## Cumulative Results

| Batch | Total Genes | Over-Annotation/Modify | Legitimate | Issue Rate |
|-------|-------------|------------------------|------------|------------|
| Pilot (5) | 5 | 5 | 0 | 100% |
| Batch 2 (15) | 15 | 12 | 3 | 80% |
| Additional (3) | 3 | 3 | 0 | 100% |
| **Combined** | **23** | **20** | **3** | **87%** |

**Legitimate genes for GO:0006915 (3/23):**
1. API5 - evolved anti-apoptotic (caspase-2, Acinus)
2. AVEN - evolved anti-apoptotic (BCL-XL, Apaf-1)
3. BCL2L12 - Bcl-2 family member (caspase-7, p53)

**MODIFY to regulatory term (1/23):**
1. AIMP2 - genuine proapoptotic moonlighting function via p53/MDM2, but should be GO:0043065 (positive regulation of apoptotic process)

**Common issue patterns:**
1. **Regulatory vs participatory conflation** (AIMP2, APBB1) - gene regulates apoptosis but doesn't participate IN the process → MODIFY to regulatory term
2. **Autophagy proteins** (ATG4D, ATG5, BECN1) - autophagy/apoptosis crosstalk ≠ apoptosis function
3. **Cell cycle proteins** (CDK1, BIRC5) - core function is cell cycle, not apoptosis
4. **Caspase substrates** (AIMP1, BCAP31) - being cleaved BY apoptosis ≠ participating IN apoptosis
5. **Metabolic enzymes** (ASAH2, APIP) - metabolic effects on apoptosis ≠ evolved function
6. **Core functions elsewhere** (ADAMTSL4=ECM, C1QBP=mt-translation, CD47=phagocytosis, AXIN1=Wnt, ARL6IP1=ER shaping, AKTIP=telomeres, BAG1=chaperoning)

---

## Key Findings

1. **Stricter criteria for legitimate GO:0006915 (apoptotic process) annotation:**
   - Must **directly participate** in apoptotic process execution (caspase cascades, MOMP, DNA fragmentation)
   - Being a **caspase substrate** ≠ participating in apoptosis
   - **Regulating** apoptosis (even via genuine evolved mechanisms) ≠ participating IN apoptosis
   - Effects at **pharmacological concentrations** ≠ physiological function
   - **Downstream metabolic effects** ≠ evolved function

2. **Regulatory vs participatory distinction is critical:**
   - AIMP2 has a genuine evolved proapoptotic function (p53 stabilization) but REGULATES apoptosis
   - The phenotypic evidence (cells ± gene = differential apoptosis susceptibility) supports regulatory annotation
   - Correct term is GO:0043065 (positive regulation of apoptotic process), not GO:0006915

3. **UniProt "Apoptosis" keyword is too broad:**
   - Applied to anything that affects apoptosis (participates, regulates, is a substrate, has downstream effects)
   - GO term "apoptotic process" implies direct participation, which is inappropriate for most of these

**Recommendations:**
- Genes with genuine regulatory functions: MODIFY to regulatory term (GO:0043065/GO:0043066)
- Genes with different core functions: Mark as OVER-ANNOTATED or REMOVE
- Only genes that directly execute apoptosis should retain GO:0006915

---

## Notes

### 2026-01-31

**APLP1 Review Completed**

APLP1 is classified as an **OVER-ANNOTATION** for GO:0006915 (apoptotic process):

- **Core function:** APP-family synaptic adhesion protein; homodimer/heterodimer-mediated cell-cell adhesion
- **Apoptosis relationship:** C30 fragment is reported to enhance neuronal apoptosis, suggesting regulation rather than direct apoptotic process participation
- **Assessment:** Modify GO:0006915 to GO:0043065 (positive regulation of apoptotic process); keep as non-core due to indirect/by-similarity evidence

**Follow-up adjustment**
- Changed GO:0006915 review action to MARK_AS_OVER_ANNOTATED (fragment-specific, by-similarity evidence); removed the proposed replacement to GO:0043065.

**AREL1 Review Completed**

AREL1 is classified as an **OVER-ANNOTATION** for GO:0006915 (apoptotic process):

- **Core function:** HECT-type E3 ubiquitin ligase that ubiquitinates IAP antagonists (SMAC, HtrA2, ARTS)
- **Apoptosis relationship:** Anti-apoptotic via degradation of IAP antagonists; supports negative regulation, not direct apoptotic process
- **Assessment:** Mark GO:0006915 as over-annotated; keep GO:0043066 (negative regulation of apoptotic process) as core

### 2026-01-19

**APBB1 Review Completed**

APBB1 (Fe65) is classified as an **OVER-ANNOTATION** for GO:0006915 (apoptotic process):

- **Core function:** Adaptor protein that binds APP intracellular domain via PTB domains; transcription coregulator
- **Apoptosis relationship:** APBB1 REGULATES apoptosis by binding phosphorylated H2AX Y142 and recruiting pro-apoptotic JNK1 to DNA damage sites (PMID:19234442 Nature)
- **Assessment:** The correct term is GO:0043065 (positive regulation of apoptotic process), which already has IDA evidence from PMID:18468999. The generic GO:0006915 is over-annotated because APBB1 doesn't execute apoptosis - it recruits pro-apoptotic factors as an adaptor

This continues the pattern: APBB1 has a genuine role in apoptosis regulation but is incorrectly annotated to "apoptotic process" instead of the more specific regulatory term.

### 2026-01-18

**Apoptosis Subproject Initialization**

Created subproject to review apoptotic process annotations on human proteins that have ONLY UniProt Keyword (SPKW) evidence via GO_REF:0000043, with no corroborating evidence from any other method.

**Key findings from DuckDB analysis:**
- 280 human genes have apoptotic process (GO:0006915 or descendants) annotations derived SOLELY from UniProt Keywords
- These annotations have no corroboration from:
  - Experimental evidence (IDA, IMP, IGI, etc.)
  - Curator statements (TAS, NAS, IC)
  - Computational methods (ISS, ISO, IBA)
  - Other IEA pipelines (InterPro, Reactome, etc.)

**Source breakdown of ALL IEA apoptotic annotations (for context):**
- GO_REF:0000043 (UniProtKB-KW): 539 annotations
- GO_REF:0000107 (Reactome): 458 annotations
- GO_REF:0000117 (UniProt): 71 annotations
- GO_REF:0000002 (InterPro2GO): 44 annotations
