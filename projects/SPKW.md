# SwissProt Keywords (SP KW) Unique Terms Project

## Overview

This project focuses on reviewing genes that have unique or unusual SwissProt Keyword (SP KW) terms. These keywords often highlight specialized functions that may require careful curation to ensure GO annotations properly capture the biology.

## Goals

1. Review genes with unique SP KW terms to ensure GO annotations are complete and accurate
2. Identify cases where GO terms may be missing or over-annotated relative to UniProt keywords
3. Propose new GO terms where gaps exist

## Tasks

### Phase 1: Initial Gene Set

- [x] Review human MAP3K5 - COMPLETE (Dec 23)
- [x] Review human PHF23 - COMPLETE (Dec 23)
- [~] Review human SIRT2 - IN PROGRESS (Dec 23)

## Status

Started: 2025-12-23
- MAP3K5: Complete
- PHF23: Complete (DRAFT status) - negative regulator of autophagy via LRSAM1 degradation
- SIRT2: In progress - passes validation with warnings, needs supporting_text additions

## Notes

**Selection criteria:**
- Genes with SP KW terms that are rare or unique across the proteome
- Focus on keywords that suggest specialized molecular functions or biological processes

**Gene-specific notes:**

- **MAP3K5**: Review completed Dec 23
- **PHF23**: Review completed Dec 23 - core function is negative regulation of autophagy through promoting ubiquitination and degradation of LRSAM1. PHD zinc finger domain mediates protein interactions.
- **SIRT2**: Review in progress Dec 23 - NAD-dependent protein deacetylase and demyristoylase. Core functions include histone deacetylation (H4K16), tubulin deacetylation, and cell cycle regulation. Also has efficient demyristoylase activity. Review has 170+ existing annotations covering multiple evidence types. Remaining work: add supporting_text to reference findings.

---

## Subproject: Apoptotic Process SPKW-Only Annotations

### Overview

This subproject identifies human proteins annotated to "apoptotic process" (GO:0006915) or descendants where the **only** evidence comes from UniProt Keywords mapping (GO_REF:0000043). These annotations lack corroboration from any other source (experimental, computational, or curator statements).

The goal is to review these annotations to determine if they are well-supported by literature or if they represent cases where the UniProt "Apoptosis" keyword was applied but the connection to apoptosis is weak or indirect.

### Query Methodology

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

### Summary Statistics (Human - goa_human.ddb)

- **Total SPKW-only genes with apoptotic process annotations**: 280
- **Source**: GO_REF:0000043 (UniProtKB-KW → GO mapping)

### Genes for Review (Sample - Alphabetical)

| Gene | UniProt | Description | Status |
|------|---------|-------------|--------|
| ADAMTSL4 | Q6UY14 | ADAMTS-like protein 4 | **REVIEWED - OVER-ANNOTATION** |
| AIMP1 | Q12904 | tRNA synthase complex protein 1 | **REVIEWED - OVER-ANNOTATION** |
| AIMP2 | Q13155 | tRNA synthase complex protein 2 | **REVIEWED - LEGITIMATE** |
| AKTIP | Q9H8T0 | AKT-interacting protein | **REVIEWED - OVER-ANNOTATION** |
| APBB1 | O00213 | Amyloid beta A4 precursor protein-binding protein | **REVIEWED - OVER-ANNOTATION** |
| API5 | Q9BZZ5 | Apoptosis inhibitor 5 | **REVIEWED - LEGITIMATE** |
| APIP | Q96GX9 | Methylthioribulose-1-phosphate dehydratase | **REVIEWED - OVER-ANNOTATION** |
| APLP1 | P51693 | Amyloid-like protein 1 | **REVIEWED - OVER-ANNOTATION** |
| AREL1 | O15033 | Apoptosis-resistant E3 ubiquitin ligase 1 | **REVIEWED - OVER-ANNOTATION** |
| ARL6IP1 | Q15041 | ADP-ribosylation factor-like protein 6-interacting protein 1 | **REVIEWED - OVER-ANNOTATION** |
| ASAH2 | Q9NR71 | Neutral ceramidase | **REVIEWED - OVER-ANNOTATION** |
| ATG4D | Q86TL0 | Cysteine protease ATG4D | **REVIEWED - OVER-ANNOTATION** |
| ATG5 | Q9H1Y0 | Autophagy protein 5 | **REVIEWED - OVER-ANNOTATION** |
| AVEN | Q9NQS1 | Cell death regulator Aven | **REVIEWED - LEGITIMATE** |
| AXIN1 | O15169 | Axin-1 | **REVIEWED - OVER-ANNOTATION** |
| BABAM2 | Q9NXR7 | BRISC and BRCA1-A complex member 2 | pending |
| BAG1 | Q99933 | BAG family molecular chaperone regulator 1 | **REVIEWED - OVER-ANNOTATION** |
| BCAP29 | Q9UHQ4 | B-cell receptor-associated protein 29 | pending |
| BCAP31 | P51572 | B-cell receptor-associated protein 31 | **REVIEWED - OVER-ANNOTATION** |
| BCL2L12 | Q9HB09 | Bcl-2-like protein 12 | **REVIEWED - LEGITIMATE** |
| BECN1 | Q14457 | Beclin-1 | **REVIEWED - OVER-ANNOTATION** |
| BIRC5 | O15392 | Baculoviral IAP repeat-containing protein 5 (survivin) | **REVIEWED - OVER-ANNOTATION** |
| C1QBP | Q07021 | Complement C1q-binding protein | **REVIEWED - OVER-ANNOTATION** |
| CD47 | Q08722 | Leukocyte surface antigen CD47 | **REVIEWED - OVER-ANNOTATION** |
| CDK1 | P06493 | Cyclin-dependent kinase 1 | **REVIEWED - OVER-ANNOTATION** |

*Full list: 280 genes total - see query above to regenerate*

---

# STATUS

## Phase 1 (Original)
- [x] Review human MAP3K5 - COMPLETE (Dec 23)
- [x] Review human PHF23 - COMPLETE (Dec 23)
- [x] Review human SIRT2 - COMPLETE (Jan 19, 2026)

## Apoptosis Subproject
- [x] Initial review batch (5/5 complete - pilot batch)
- [x] Batch 2 review (15/15 complete)
- [x] APBB1 review (1/1 complete)
- [x] APLP1 review (1/1 complete)
- [x] AREL1 review (1/1 complete)
- Total reviewed: 23/280 genes (8.2%)
- Over-annotation rate: 82.6% (19/23)
- Legitimate annotations: 4 (AIMP2, API5, AVEN, BCL2L12)

## Rhythmic Process Subproject
- [x] Pilot review (5/5 complete)
- Total reviewed: 5/146 genes (3.4%)
- Over-annotation rate: **100%** (5/5)
- Legitimate annotations: 0 (none in pilot)

## Autophagy Subproject
- [x] Batch 1 (4/4 complete): ABL1, BCL2, FOXO1, LRRK2
- [x] Batch 2 (5/5 complete): DRAM1, DRAM2, DAP, CLTC, HMGB1
- [x] Batch 3 (5/5 complete): IFI16, IRF8, LRPPRC, HAP1/APEX1, GRAMD1A
- Total reviewed: 14/123 genes (11.4%)
- Over-annotation rate: 79% (11/14)
- Legitimate annotations: 3 (DRAM1, DRAM2, DAP)
- Note: HDAC6 was removed from analysis (has corroborating IGI evidence)

## Cumulative Results (All Subprojects)

| Subproject | Total Genes | Reviewed | Over-Annotation | Legitimate | Rate |
|------------|-------------|----------|-----------------|------------|------|
| Apoptosis | 280 | 23 | 19 | 4 | 82.6% |
| Rhythmic Process | 146 | 5 | 5 | 0 | 100% |
| Autophagy | 123 | 14 | 11 | 3 | 79% |
| **Combined** | **549** | **42** | **35** | **7** | **83.3%** |

**Legitimate genes identified (7/40):**
1. AIMP2 - proapoptotic (p53/MDM2)
2. API5 - anti-apoptotic (caspase-2, Acinus)
3. AVEN - anti-apoptotic (BCL-XL, Apaf-1)
4. BCL2L12 - anti-apoptotic (Bcl-2 family)
5. DRAM1 - autophagy (lysosomal membrane, VAMP8 stabilization)
6. DRAM2 - autophagy (lysosomal membrane, autophagic flux)
7. DAP - autophagy regulation (mTORC1 substrate, negative regulator)

**Last updated**: 2026-01-31

# NOTES

## 2026-01-19

**APBB1 Review Completed**

APBB1 (Fe65) is classified as an **OVER-ANNOTATION** for GO:0006915 (apoptotic process):

- **Core function:** Adaptor protein that binds APP intracellular domain via PTB domains; transcription coregulator
- **Apoptosis relationship:** APBB1 REGULATES apoptosis by binding phosphorylated H2AX Y142 and recruiting pro-apoptotic JNK1 to DNA damage sites (PMID:19234442 Nature)
- **Assessment:** The correct term is GO:0043065 (positive regulation of apoptotic process), which already has IDA evidence from PMID:18468999. The generic GO:0006915 is over-annotated because APBB1 doesn't execute apoptosis - it recruits pro-apoptotic factors as an adaptor

This continues the pattern: APBB1 has a genuine role in apoptosis regulation but is incorrectly annotated to "apoptotic process" instead of the more specific regulatory term.

---

**SIRT2 Review Finalized**

Completed finalization of the SIRT2 review:
- Added supporting_text to key reference findings (PMID:24769394, PMID:24825348, PMID:15213244, PMID:27512957, PMID:30154464)
- Fixed inconsistent review actions (mitochondrion GO:0005739 now consistently REMOVE)
- Added 3 NEW annotations for core functions:
  - GO:0031115 (negative regulation of microtubule polymerization)
  - GO:0016192 (vesicle-mediated transport)
  - GO:0030261 (chromosome condensation)
- Validation now passes with only 6 warnings (acceptable edge cases)

**SIRT2 Key Classification:**
- NOT an apoptosis gene (core function is NAD-dependent deacetylase)
- Primary targets: alpha-tubulin (K40), histones (H4K16, H3K18), transcription factors (FOXO, p65, HIF1A)
- Additional activities: demyristoylase, debenzoylase, de-methacrylase
- The "rhythmic process" annotation was from SPKW evidence and is an over-annotation

## 2026-01-31

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

---

## 2026-01-18

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

**Query used:**
```sql
duckdb -readonly ~/repos/go-db/db/goa_human.ddb "
WITH all_apoptotic AS (
    SELECT a.db_object_id, a.db_object_symbol, a.supporting_references
    FROM gaf_association a
    INNER JOIN isa_partof_closure ipc ON a.ontology_class_ref = ipc.subject
    WHERE ipc.object = 'GO:0006915'
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
"
```

---

### Pilot Batch Review Results (2026-01-18) - REVISED

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
| **AIMP2** | MSC scaffold | Specific proapoptotic function via p53 stabilization (blocks MDM2); stress-responsive nuclear translocation; mutagenesis confirms | **LEGITIMATE** - genuine evolved proapoptotic mechanism |
| **APIP** | Methionine salvage enzyme (MtnB) | Moonlighting: binds Apaf-1, inhibits apoptosis; enzymatic activity dispensable for anti-apoptotic effect | **OVER-ANNOTATION** - core function is metabolic; apoptosis effect is moonlighting; INHIBITS not participates |
| **ARL6IP1** | ER membrane shaping (reticulon-like) | Named "ARMER"; inhibits CASP9-dependent apoptosis | **OVER-ANNOTATION** - anti-apoptotic effect likely secondary to ER homeostasis; deep research is all about ER morphology |
| **ASAH2** | Neutral ceramidase (sphingolipid metabolism) | Reduces ceramide → shifts ceramide/S1P balance toward survival | **OVER-ANNOTATION** - metabolic enzyme; apoptotic effect is downstream of ceramide catabolism, not an evolved regulatory function |

**Results: 4 of 5 genes have over-annotations; only AIMP2 is legitimate.**

---

### Detailed Gene Analysis

#### AIMP1 (Q12904) - tRNA synthase complex protein 1

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

#### AIMP2 (Q13155) - tRNA synthase complex protein 2

**Core evolved function:** Also MSC scaffold.

**Apoptosis connection:**
- UniProt states: "Functions as a proapoptotic factor"
- Specific mechanism: blocks MDM2-mediated ubiquitination and degradation of p53
- Stress-responsive nuclear translocation
- Mutagenesis data shows specific variants with "loss of proapoptotic activity"

**Why LEGITIMATE:**
- This is a genuine **evolved proapoptotic function**:
  - Specific molecular mechanism (p53 stabilization via MDM2 inhibition)
  - Mutagenesis evidence identifies specific residues required
  - Stress-responsive nuclear translocation = specific cellular program
- NOT a pleiotropic downstream effect

---

#### APIP (Q96GX9) - Methylthioribulose-1-phosphate dehydratase

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

#### ARL6IP1 (Q15041) - ADP-ribosylation factor-like protein 6-interacting protein 1

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

#### ASAH2 (Q9NR71) - Neutral ceramidase

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

### Key Findings (Revised)

1. **Stricter criteria for legitimate apoptosis annotation:**
   - Must have an **evolved function** in apoptosis, not just causal/pleiotropic effects
   - Being a **caspase substrate** ≠ participating in apoptosis
   - Effects at **pharmacological concentrations** ≠ physiological function
   - **Downstream metabolic effects** ≠ evolved regulatory function

2. **Result: 4 of 5 genes are over-annotated:**
   - Only AIMP2 has genuine evolved proapoptotic function (p53 stabilization via MDM2 inhibition)
   - AIMP1, APIP, ARL6IP1, ASAH2 all have different core functions with apoptotic effects being secondary

3. **UniProt "Apoptosis" keyword is too broad:**
   - Applied to anything that affects apoptosis (participates, regulates, is a substrate, has downstream effects)
   - GO term "apoptotic process" implies direct participation, which is inappropriate for most of these

**Recommendations:**

- **AIMP2**: Keep annotation - legitimate
- **AIMP1, APIP, ARL6IP1, ASAH2**: Mark as OVER-ANNOTATED or REMOVE
  - These proteins have different core functions
  - Their relationship to apoptosis is either as substrates, regulators, or through downstream metabolic effects
  - More specific regulatory terms (GO:0043066) are appropriate where experimental evidence exists

**Next steps:** Review more genes to confirm this pattern and develop systematic criteria for identifying over-annotations based on core function analysis.

---

### Batch 2 Review Results (2026-01-18)

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

### Detailed Analysis - Batch 2 Legitimate Genes

#### API5 (Q9BZZ5) - Apoptosis inhibitor 5

**Core evolved function:** Anti-apoptotic scaffold protein with HEAT/ARM-like helical repeat architecture.

**Why LEGITIMATE:**
- **Direct caspase-2 inhibition:** Binds the CARD domain of caspase-2, preventing dimerization/activation
- **Acinus protection:** Binds Acinus and protects it from caspase-3 cleavage, blocking DNA fragmentation
- **E2F1 axis modulation:** Suppresses E2F1-dependent apoptosis
- All mechanisms are specific, evolved anti-apoptotic functions, not pleiotropic effects

---

#### AVEN (Q9NQS1) - Cell death regulator Aven

**Core evolved function:** Anti-apoptotic regulator.

**Why LEGITIMATE:**
- **BCL-XL binding:** Direct interaction with BCL-XL, stabilizing it and potentiating its anti-apoptotic function
- **Apaf-1 inhibition:** Binds Apaf-1, preventing apoptosome assembly and caspase-9 activation
- **BH3-like motif:** Predicted BH3-like sequence (aa 141-153) for BCL-XL interaction
- **Proteolytic regulation:** Cathepsin D cleaves N-terminus to release potent anti-apoptotic C-terminal fragment
- Specific evolved mechanisms, not downstream/metabolic effects

---

#### BCL2L12 (Q9HB09) - Bcl-2-like protein 12

**Core evolved function:** Anti-apoptotic Bcl-2 family member.

**Why LEGITIMATE:**
- **Direct caspase inhibition:** Inhibits effector caspase-7 (and possibly caspase-3)
- **p53 antagonism:** Binds and neutralizes p53 transcriptional activity
- **Bcl-2 family member:** Has BH3-like motif, part of the evolved apoptosis regulatory network
- Named appropriately - this is a bona fide anti-apoptotic protein with evolved mechanisms

---

### Detailed Analysis - Batch 2 Over-Annotations (Selected)

#### BIRC5/Survivin (O15392)

**Why OVER-ANNOTATION despite "Apoptosis inhibitor" name:**
- Deep research states: "survivin's best-established function is as an essential CPC component regulating mitotic progression"
- "Anti-apoptotic effects are context-dependent and likely mediated by networks (XIAP, SMAC) rather than direct caspase inhibition"
- Core evolved function is **mitosis** (Chromosomal Passenger Complex), not apoptosis
- This is a case where the gene NAME is misleading - the protein evolved for cell division, with indirect anti-apoptotic effects

#### ATG5 (Q9H1Y0)

**Why OVER-ANNOTATION despite "Apoptosis-specific protein" alias:**
- Core function is autophagy: E3-like activity in ATG12-ATG5-ATG16L1 complex for LC3 lipidation
- While autophagy and apoptosis have crosstalk, ATG5's evolved function is autophagosome biogenesis
- The UniProt alias "Apoptosis-specific protein" reflects early naming, not current functional understanding

#### CDK1 (P06493)

**Why OVER-ANNOTATION:**
- Core function is cell cycle control (essential G2/M transition kinase)
- 2023 review notes CDK1 phosphorylates "caspase-9, Bcl-2 family, survivin" among its 1000+ substrates
- Phosphorylating apoptosis-related proteins as part of cell cycle doesn't make apoptosis its evolved function
- This is like annotating a transcription factor to all processes its target genes are involved in

---

### Cumulative Results (Pilot + Batch 2)

| Batch | Total Genes | Over-Annotation | Legitimate | Over-Annotation Rate |
|-------|-------------|-----------------|------------|---------------------|
| Pilot (5) | 5 | 4 | 1 | 80% |
| Batch 2 (15) | 15 | 12 | 3 | 80% |
| **Combined** | **20** | **16** | **4** | **80%** |

**Legitimate genes identified (4/20):**
1. AIMP2 - genuine proapoptotic function via p53/MDM2
2. API5 - evolved anti-apoptotic (caspase-2, Acinus)
3. AVEN - evolved anti-apoptotic (BCL-XL, Apaf-1)
4. BCL2L12 - Bcl-2 family member (caspase-7, p53)

**Common over-annotation patterns:**
1. **Autophagy proteins** (ATG4D, ATG5, BECN1) - autophagy/apoptosis crosstalk ≠ apoptosis function
2. **Cell cycle proteins** (CDK1, BIRC5) - core function is cell cycle, not apoptosis
3. **Caspase substrates** (AIMP1, BCAP31) - being cleaved BY apoptosis ≠ participating IN apoptosis
4. **Metabolic enzymes** (ASAH2, APIP) - metabolic effects on apoptosis ≠ evolved function
5. **Core functions elsewhere** (ADAMTSL4=ECM, C1QBP=mt-translation, CD47=phagocytosis, AXIN1=Wnt, ARL6IP1=ER shaping, AKTIP=telomeres, BAG1=chaperoning)

---

## Subproject: Rhythmic Process SPKW-Only Annotations

### Overview

This subproject identifies human proteins annotated to "rhythmic process" (GO:0048511) where the **only** evidence comes from UniProt Keywords mapping (GO_REF:0000043). Notably, 100% of SPKW annotations to this term lack corroborating evidence from any other source.

### Summary Statistics

- **Total SPKW-only genes**: 146
- **Total SPKW annotations**: 146
- **% with no corroboration**: 100%
- **Source keyword**: UniProtKB-KW:KW-0151 (Biological rhythms)

### Key Concern

The UniProt "Biological rhythms" keyword appears to be applied broadly to any protein whose expression or activity oscillates with circadian rhythm, OR to proteins that affect rhythmic processes. This is different from proteins whose **evolved core function** is to generate or maintain biological rhythms.

**Core circadian clock genes** (likely LEGITIMATE):
- CLOCK, BMAL1, BMAL2, PER1, PER2, PER3, CRY1, CRY2, TIMELESS, CIART, NR1D1, NR1D2

**Genes with other core functions** (likely OVER-ANNOTATION):
- ATG7 (autophagy), CDK1 (cell cycle), CREB1 (transcription factor), TP53 (tumor suppressor)

### Pilot Batch for Review

| Gene | UniProt | Description | Core Function (confirmed) | Status |
|------|---------|-------------|---------------------------|--------|
| ATG7 | O95352 | Autophagy-related protein 7 | Autophagy (E1-like enzyme) | **OVER-ANNOTATION** |
| CREB1 | P16220 | cAMP-responsive element-binding protein 1 | Transcription factor | **OVER-ANNOTATION** |
| SIRT1 | Q96EB6 | NAD-dependent protein deacetylase sirtuin-1 | Deacetylase (many substrates) | **OVER-ANNOTATION** |
| TARDBP | Q13148 | TAR DNA-binding protein 43 | RNA binding/splicing | **OVER-ANNOTATION** |
| TP53 | P04637 | Cellular tumor antigen p53 | Tumor suppressor | **OVER-ANNOTATION** |

**Result: 5/5 genes (100%) are OVER-ANNOTATED**

### Criteria for Legitimate Rhythmic Process Annotation

A legitimate annotation requires evidence that the gene:
1. Has an **evolved function** in generating/maintaining biological rhythms
2. Is part of the core molecular clock machinery (TTFL components)
3. Regulates clock gene expression as its **primary function**

NOT legitimate if:
- Expression oscillates but core function is elsewhere
- Affects rhythms through downstream/pleiotropic effects
- Is a target/substrate of clock-controlled processes

---

### Detailed Analysis - Rhythmic Process Pilot

#### ATG7 (O95352) - Autophagy-related protein 7

**Core function:** E1-like ubiquitin-activating enzyme that activates ATG8 (LC3/GABARAP) and ATG12 in the ubiquitin-like conjugation cascades for autophagosome formation.

**Why OVER-ANNOTATION:**
- Deep research is entirely about **autophagy** (canonical autophagy, LC3 lipidation, CASM)
- No mention of rhythmic process or circadian rhythm
- Core function is autophagy E1-like enzyme activity
- If autophagy flux oscillates with circadian rhythm, that doesn't make ATG7 a "rhythmic process" gene

---

#### CREB1 (P16220) - cAMP-responsive element-binding protein 1

**Core function:** bZIP transcription factor that binds CRE elements (TGACGTCA) to regulate gene expression in response to cAMP/PKA, Ca2+/CaMK, and MAPK signaling.

**Why OVER-ANNOTATION:**
- Deep research covers neuronal activity-dependent transcription, metabolic regulation, cancer, immune function
- **No mention of circadian rhythm or rhythmic process** in the deep research
- Core function is cAMP-responsive transcription
- CREB may regulate clock gene expression, but that doesn't make rhythm its core function

---

#### SIRT1 (Q96EB6) - NAD-dependent protein deacetylase sirtuin-1

**Core function:** NAD-dependent lysine deacetylase with broad substrate specificity.

**Why OVER-ANNOTATION:**
- Deep research mentions circadian briefly: "deacetylates core clock components (BMAL1/PER2)"
- But this is **ONE of MANY substrates**: p53 (apoptosis), NF-κB (inflammation), FOXO (stress), HIF (hypoxia), PGC-1α (metabolism), histones (chromatin)
- Core function is NAD-dependent deacetylation, not rhythm generation
- The clock deacetylation is a downstream effect of the enzymatic activity, not an evolved rhythmic function

---

#### TARDBP (Q13148) - TAR DNA-binding protein 43 (TDP-43)

**Core function:** RNA-binding protein essential for splicing repression (cryptic exon suppression), mRNA stability/transport, and autoregulation.

**Why OVER-ANNOTATION:**
- Deep research is entirely about **RNA metabolism** and **ALS/FTD neurodegeneration**
- No mention of rhythmic process or circadian rhythm
- Core function is RNA binding/splicing regulation
- TDP-43 proteinopathy in 95-97% of ALS cases - this is about neurodegeneration, not rhythm

---

#### TP53 (P04637) - Cellular tumor antigen p53

**Core function:** Tumor suppressor transcription factor that coordinates cell-cycle arrest, apoptosis, senescence, DNA repair, and metabolic reprogramming.

**Why OVER-ANNOTATION:**
- Deep research is entirely about **tumor suppression**: DNA damage response, MDM2 regulation, apoptosis, ferroptosis, cancer therapy
- No mention of rhythmic process or circadian rhythm
- Core function is stress-responsive transcription for cell fate decisions
- Most frequently mutated tumor suppressor - this is about cancer, not rhythm

---

### Key Finding: Rhythmic Process has 100% Over-Annotation Rate in Pilot

This is **worse than apoptosis** (which had 80% over-annotation rate).

The UniProt "Biological rhythms" keyword (KW-0151) appears to be applied to:
1. Proteins whose expression oscillates with circadian rhythm (not the same as function IN rhythm)
2. Proteins that affect rhythm through pleiotropic effects (transcription factors, enzymes)
3. Proteins that are substrates/targets of clock machinery

**Recommendation:** The GO term GO:0048511 "rhythmic process" should be reviewed systematically. With 146 SPKW-only genes and 100% over-annotation in pilot, this mapping may be fundamentally problematic.

---

## Subproject: Autophagy SPKW-Only Annotations

### Overview

This subproject identifies human proteins annotated to "autophagy" (GO:0006914) where the **only** evidence comes from UniProt Keywords mapping (GO_REF:0000043).

### Summary Statistics

- **Total SPKW-only genes**: 123
- **Total SPKW annotations**: 172
- **% with no corroboration**: 71.5%
- **Source keyword**: UniProtKB-KW:KW-0073 (Autophagy)

### Key Concern

The UniProt "Autophagy" keyword may be applied to:
1. Core autophagy machinery (ATG proteins, VPS proteins) - LEGITIMATE
2. Proteins that **regulate** autophagy (kinases, transcription factors) - may be over-annotation
3. Proteins that are **substrates** of autophagy (cargo receptors, aggregates) - may be over-annotation
4. Proteins whose loss **affects** autophagy flux through pleiotropic effects

### Pilot Batch for Review

| Gene | UniProt | Description | Core Function (confirmed) | Status |
|------|---------|-------------|---------------------------|--------|
| ABL1 | P00519 | Tyrosine-protein kinase ABL1 | Non-receptor tyrosine kinase (cytoskeleton, DNA damage) | **OVER-ANNOTATION** |
| BCL2 | P10415 | Apoptosis regulator Bcl-2 | Anti-apoptotic (MOMP inhibition) | **OVER-ANNOTATION** |
| FOXO1 | Q12778 | Forkhead box protein O1 | Transcription factor (metabolism) | **OVER-ANNOTATION** |
| LRRK2 | Q5S007 | Leucine-rich repeat kinase 2 | Ser/Thr kinase + GTPase (Rab phosphorylation) | **OVER-ANNOTATION** |

**Result: 4/4 genes (100%) are OVER-ANNOTATED**

*Note: HDAC6 was initially included but removed from this analysis - it has corroborating evidence (IGI for GO:0061734 type 2 mitophagy from PMID:20457763), so it does not meet the SPKW-only criteria. The HDAC6 gene review was retained separately.*

### Criteria for Legitimate Autophagy Annotation

A legitimate annotation requires evidence that the gene:
1. Has an **evolved function** in autophagosome formation/maturation
2. Is part of the core autophagy machinery (ATG proteins, PI3K complex, LC3 system)
3. Functions as a selective autophagy receptor as its **primary function**
4. Has direct physical role in autophagy pathway (e.g., cargo trafficking to autophagosome)

NOT legitimate if:
- Regulates autophagy via upstream signaling (kinases, TFs)
- Is degraded by autophagy (substrate)
- Loss causes autophagy defects through pleiotropic effects

---

### Detailed Analysis - Autophagy Pilot

#### ABL1 (P00519) - Tyrosine-protein kinase ABL1

**Core function:** Non-receptor tyrosine kinase (EC 2.7.10.2) with SH2-SH3-kinase architecture. Functions in DNA damage response (DDR), cytoskeletal dynamics (F-actin binding), and cell signaling. Famously drives CML when fused to BCR.

**Why OVER-ANNOTATION:**
- Deep research is entirely about **tyrosine kinase activity**: DDR, cytoskeleton, BCR-ABL in leukemia, allosteric regulation
- No mention of autophagy in deep research
- Core function is tyrosine phosphorylation of diverse substrates (YAP1, HK2, RAD51)
- Any autophagy effects would be through signaling cascades, not direct participation

---

#### BCL2 (P10415) - Apoptosis regulator Bcl-2

**Core function:** Anti-apoptotic regulator that prevents mitochondrial outer membrane permeabilization (MOMP). BH1-4 domains form hydrophobic groove that sequesters BH3-only proteins (BIM, PUMA) and restrains BAX/BAK.

**Why OVER-ANNOTATION:**
- Core evolved function is clearly **apoptosis regulation**
- BCL2 does interact with BECN1 (Beclin-1) and can regulate autophagy
- However, this is a **regulatory interaction** - BCL2's evolved function is to inhibit apoptosis, and its autophagy regulation is through the same BH3-groove mechanism
- BCL2 didn't evolve TO regulate autophagy - it evolved to regulate apoptosis, and BECN1 happens to have a BH3 domain
- The annotation "autophagy" implies direct participation, not regulatory crosstalk

---

#### FOXO1 (Q12778) - Forkhead box protein O1

**Core function:** Forkhead transcription factor that binds 5′-TTGTTTAC-3′ consensus. Regulated by insulin/PI3K/AKT signaling. Primary functions in gluconeogenesis (activates PCK1, G6PC), oxidative stress, and metabolic homeostasis.

**Why OVER-ANNOTATION:**
- Deep research is about **metabolic control** and **transcription factor function**
- FOXO1 can transcriptionally activate autophagy genes as one of its many target gene programs
- But FOXO1's evolved function is as a **metabolic transcription factor**, not as autophagy machinery
- This is similar to annotating p53 to "apoptosis" - it regulates apoptosis genes but its core function is broader
- Transcriptional regulation of autophagy ≠ direct function in autophagy

---

#### LRRK2 (Q5S007) - Leucine-rich repeat serine/threonine-protein kinase 2

**Core function:** Dual enzyme with Ser/Thr kinase (EC 2.7.11.1) and GTPase (EC 3.6.5.-) activities. Primary substrates are Rab GTPases (Rab10 Thr73, Rab8, Rab12). Regulates endolysosomal trafficking and ciliogenesis. Linked to Parkinson's disease.

**Why OVER-ANNOTATION:**
- Deep research is about **Rab phosphorylation** and **endolysosomal trafficking**
- LRRK2 affects the lysosomal system (LYTL - lysosomal tubulation/sorting)
- While autophagy ultimately requires lysosomes, LRRK2's evolved function is Rab-mediated membrane trafficking
- Autophagy defects from LRRK2 mutations are **downstream effects** of impaired endolysosomal trafficking
- Core function is Rab phosphorylation for trafficking, not autophagosome biogenesis

---

## Subproject: ANOGA (Anopheles gambiae) SPKW-Only Annotations

### Overview

This subproject explores UniProt Keyword (SPKW) unique contributions to *Anopheles gambiae* (African malaria mosquito) GO annotations. ANOGA is of high interest because:

1. **Vector biology relevance**: Mosquito immune system and salivary proteins are critical for understanding malaria transmission
2. **Less curated organism**: Fewer experimental annotations means higher reliance on automated pipelines
3. **Unique biology**: Insect immunity, blood-feeding adaptations, and vector-pathogen interactions

### Summary Statistics (from ANOGA.ddb)

| Metric | Value |
|--------|-------|
| Total ANOGA annotations | 86,061 |
| SPKW (GO_REF:0000043) annotations | 17,787 |
| SPKW-unique annotations | 12,076 |
| Unique genes with SPKW-only annotations | 5,812 |
| Unique GO terms from SPKW-only | 246 |

### Distribution by Aspect

| Aspect | Annotations | Genes | Terms |
|--------|-------------|-------|-------|
| F (Molecular Function) | 7,883 | 4,125 | 83 |
| P (Biological Process) | 3,616 | 2,693 | 143 |
| C (Cellular Component) | 577 | 508 | 20 |

### High-Interest Categories for ANOGA

These terms are uniquely relevant to mosquito biology:

| Term | Label | SPKW-unique Genes | Interest Level |
|------|-------|-------------------|----------------|
| GO:0002376 | immune system process | 147 | **HIGH** - vector immunity |
| GO:0045087 | innate immune response | 76 | **HIGH** - pathogen response |
| GO:0090729 | toxin activity | 15 | **HIGH** - salivary proteins |
| GO:0042742 | defense response to bacterium | 11 | **HIGH** - antimicrobials |

### Known Problematic Terms (from Human Analysis)

| Term | Label | SPKW-unique Genes | Expected Over-annotation Rate |
|------|-------|-------------------|------------------------------|
| GO:0006915 | apoptotic process | 28 | ~80% (based on human) |
| GO:0048511 | rhythmic process | 20 | ~100% (based on human) |
| GO:0006914 | autophagy | 16 | ~80% (based on human) |

### High-Count Broad Terms

These are likely legitimate but too generic to be informative:

| Term | Label | Genes |
|------|-------|-------|
| GO:0046872 | metal ion binding | 1,697 |
| GO:0016787 | hydrolase activity | 1,011 |
| GO:0016740 | transferase activity | 903 |
| GO:0000166 | nucleotide binding | 688 |
| GO:0006351 | DNA-templated transcription | 567 |

### Interesting Example: D7 Salivary Proteins

The D7 protein family (D7r1, D7L1, D7L2, 7DL3) are salivary gland proteins involved in blood-feeding. They have SPKW-unique annotations to:

- **GO:0090729** (toxin activity) - via SPKW
- **GO:0042311** (vasodilation) - via SPKW
- **GO:0097746** (blood vessel diameter maintenance) - via SPKW

These appear to be **legitimate** annotations since D7 proteins:
- Bind biogenic amines (histamine, serotonin) to counteract host hemostasis
- Have evolved specifically for blood-feeding function
- Are well-characterized in mosquito salivary biology

However, the "toxin activity" term may be debatable - D7 proteins are more accurately described as having anti-hemostatic activity rather than being true toxins.

### Sweet-Spot Terms for Review (10-30 genes)

Biological Process terms that may warrant review:

| Term | Label | Genes |
|------|-------|-------|
| GO:0006508 | proteolysis | 49 |
| GO:0030154 | cell differentiation | 44 |
| GO:0022904 | respiratory electron transport chain | 44 |
| GO:0007399 | nervous system development | 26 |
| GO:0007608 | sensory perception of smell | 19 |
| GO:0007601 | visual perception | 13 |
| GO:0016055 | Wnt signaling pathway | 13 |

### Query Used

```sql
-- Database: ~/repos/go-db/db/ANOGA.ddb
-- Find SPKW-unique contributions (gene-term pairs with no other evidence)

WITH spkw_annotations AS (
    SELECT a.db_object_id, a.db_object_symbol, a.ontology_class_ref, a.aspect
    FROM gaf_association a
    WHERE a.supporting_references = 'GO_REF:0000043'
),
gene_term_with_other_evidence AS (
    SELECT DISTINCT db_object_id, ontology_class_ref
    FROM gaf_association
    WHERE supporting_references != 'GO_REF:0000043'
),
spkw_unique AS (
    SELECT s.*
    FROM spkw_annotations s
    WHERE NOT EXISTS (
        SELECT 1 FROM gene_term_with_other_evidence o
        WHERE o.db_object_id = s.db_object_id
          AND o.ontology_class_ref = s.ontology_class_ref
    )
)
SELECT
    su.ontology_class_ref,
    tl.label,
    su.aspect,
    COUNT(DISTINCT su.db_object_id) as gene_count
FROM spkw_unique su
JOIN term_label tl ON su.ontology_class_ref = tl.id
GROUP BY su.ontology_class_ref, tl.label, su.aspect
ORDER BY gene_count DESC;
```

### Recommendations

1. **Prioritize immune terms for review**: GO:0002376 and GO:0045087 have the most SPKW-unique genes and are highly relevant to vector biology research

2. **Validate toxin activity annotations**: The D7 proteins suggest some toxin annotations may be legitimate, but "toxin" may not be the best term

3. **Check apoptosis/autophagy/rhythm**: Based on human experience, expect 80-100% over-annotation rate

4. **Consider ANOGA-specific biology**: Blood-feeding, olfaction (host-seeking), and innate immunity are core mosquito biology that may have legitimate unique annotations

### Status

- [x] Initial exploration complete (2026-01-30)
- [x] D7 protein family review complete (2026-01-30) - **ALL 8 PROTEINS REVIEWED**
- [x] Immune gene pilot batch complete (2026-01-30) - **6 GENES REVIEWED**
- [x] PGRP/TEP extended batch (2026-01-31) - **ALL 8 GENES REVIEWED**
- [ ] Review remaining immune genes (~133 more)

### D7 Family Review Summary (8 proteins)

| Gene | UniProt | Binding Specificity | Toxin Activity Annotation | Key Finding |
|------|---------|---------------------|---------------------------|-------------|
| D7r1 | Q9UB30 | Serotonin, histamine | **OVER-ANNOTATED** | Kratagonist for biogenic amines |
| D7r2 | Q9UB31 | Serotonin, histamine, norepinephrine | N/A (not annotated) | Kratagonist for biogenic amines |
| D7r3 | A0A1S4GYH9 | Serotonin, histamine | N/A (not annotated) | Has IDA evidence for localization |
| D7r4 | Q7PNF2 | Serotonin, histamine, norepinephrine, tryptamine | N/A (not annotated) | Crystal structure solved |
| **D7r5** | Q7PN86 | **NONE** | N/A (not annotated) | Possible pseudogene, no binding |
| D7L1 | Q7PJ76 | Leukotriene C4, thromboxane A2 | **OVER-ANNOTATED** | Binds eicosanoids, not amines |
| D7L2 | A0A1S4GYJ6 | Weak leukotriene binding | **OVER-ANNOTATED** | Less characterized |
| **D7L3** | A0A1S4HE90 | **Serotonin only** | **OVER-ANNOTATED** | Only long-form that binds amine |

**Result: 4/4 (100%) "toxin activity" annotations are OVER-ANNOTATED; the other 4 D7 proteins do not carry GO:0090729 in GOA**

#### Why "Toxin Activity" is Wrong for D7 Proteins

The GO definition of toxin activity (GO:0090729) requires:
> "initiating pathogenesis (leading to an abnormal, generally detrimental state)"

D7 proteins fail this criterion because:
1. They do NOT initiate pathogenesis - they facilitate normal feeding behavior
2. They do NOT cause tissue damage - effects are reversible
3. The host returns to normal after the mosquito finishes feeding
4. Their mechanism is sequestration (removing mediators), not introducing harmful substances

#### The Kratagonism Mechanism

D7 proteins are "kratagonists" (from Greek *kratos* = power/strength + antagonist) - high-affinity scavengers that neutralize host defense molecules:

```
Host response to bite:
  Tissue damage → Serotonin/Histamine release → Vasoconstriction + Inflammation
                                    ↓
                           D7 protein binds mediator
                                    ↓
                           Mediator sequestered (inactive)
                                    ↓
                           Blood vessel stays dilated → Successful feeding
```

This is fundamentally different from toxin activity:
- **Toxin**: Introduces harmful substance → causes pathology
- **Kratagonist**: Removes host substance → prevents host defense

#### Short-Form vs Long-Form D7 Proteins

| Property | Short Forms (D7r1-5) | Long Forms (D7L1-3) |
|----------|---------------------|---------------------|
| Size | ~15-17 kDa | ~30 kDa (two OBP domains) |
| Primary ligands | Biogenic amines | Eicosanoids (lipid mediators) |
| Targets | Serotonin, histamine | Leukotrienes, thromboxane A2 |
| Host pathway blocked | Vasoconstriction | Inflammation, platelet aggregation |

**Exception**: D7L3 (7DL3) binds serotonin, making it unique among long-forms.

#### Key Biological Findings

1. **D7 proteins are "kratagonists"** - they sequester host signaling molecules to prevent vasoconstriction and inflammation
2. **This is NOT "toxin activity"** which requires "initiating pathogenesis" per GO definition
3. **D7r5 is particularly notable** - it doesn't bind ANY ligands and may be a pseudogene (PMID:16301315: "appears to be on the path to becoming a pseudogene")
4. **Long-form D7s (D7L1-2)** bind eicosanoids (leukotrienes, thromboxane), not biogenic amines
5. **D7L3 is unusual** - the only long-form that binds a biogenic amine (serotonin only)

#### Recommended GO Annotations for D7 Proteins

**Instead of "toxin activity":**
- GO:0051378 (serotonin binding) - for D7r1-4, D7L3
- GO:0051381 (histamine binding) - for D7r1-4
- GO:1900047 (negative regulation of hemostasis) - for all
- GO:0005615 (extracellular space) - appropriate, keep

#### Full Documentation

See comprehensive write-up: `interpro/panther/PTHR11857/PTHR11857-summary.md`

---

## Subproject: S. pombe (Schizosaccharomyces pombe) SPKW-Only Annotations

### Overview

S. pombe is a well-curated model organism with extensive experimental annotations from PomBase. This makes it an ideal test case for identifying TRUE SPKW-unique annotations that are not subsumed by more specific experimental evidence.

### Query Methodology

Used closure-based query to find TRUE SPKW-unique annotations:
- An SPKW annotation to term X is NOT unique if there exists a non-SPKW annotation to term Y where Y is_a X
- This excludes cases where SPKW provides a broad term but experimental evidence exists for a specific child term

### Key Statistics (2026-01-31)

| Metric | Count |
|--------|-------|
| Naive SPKW-unique (gene-term pairs) | 7,221 |
| TRUE SPKW-unique (after closure filtering) | 1,963 |
| Reduction from closure filtering | 73% |

The 73% reduction demonstrates the importance of using closure-based queries. Most SPKW annotations to broad terms are subsumed by more specific experimental annotations to child terms.

### Identified Over-Annotation Pattern: Meiotic Cell Cycle

207 genes have TRUE SPKW-unique "meiotic cell cycle" (GO:0051321) annotations.

**Notable case: ATG autophagy genes**

7 genes have BOTH "meiotic cell cycle" AND "autophagy" SPKW annotations:
- atg101, atg13, atg16, atg2, atg38, atg5, snx41

These genes have extensive experimental evidence for autophagy functions (IMP for macroautophagy, mitophagy, reticulophagy) but **zero** experimental evidence for meiotic cell cycle.

**Root cause**: UniProt assigns "Meiosis" keyword because autophagy is upregulated during sporulation (meiosis in yeast). This is the same logic error as human apoptosis annotations - a support process gets conflated with the main process.

**GO subset status**: GO:0051321 is in goslim_yeast and goslim_drosophila (NOT in gocheck_do_not_annotate). The specific meiotic phases (prophase I, metaphase II, etc.) ARE in do-not-annotate.

### Full Gene Reviews Completed (2026-01-31)

All 7 ATG genes underwent complete annotation review with deep research. Results:

| Gene | UniProt | Annotations Reviewed | Meiotic Cell Cycle Action | Core Function |
|------|---------|---------------------|---------------------------|---------------|
| atg101 | O13978 | 21 | **REMOVE** | Atg1/ULK1 kinase complex component |
| atg13 | O36019 | 31 | **REMOVE** | Atg1 kinase regulator, autophagy initiation |
| atg16 | O94656 | 11 | **REMOVE** | E3-like ligase for Atg8 lipidation |
| atg2 | O94649 | 26 | **REMOVE** | Lipid transfer protein, ER-phagophore bridge |
| atg38 | O94427 | 10 | **REMOVE** | PtdIns3K complex I subunit |
| atg5 | O74971 | 25 | **REMOVE** | Atg12-Atg5-Atg16 complex component |
| snx41 | O60107 | 19 | **REMOVE** | Sorting nexin for retrograde transport/autophagy |

**Key evidence supporting REMOVE decisions:**

1. **Gene naming misleading**: All genes have "mug" synonyms (meiotically up-regulated gene) based on expression studies (PMID:16303567), but transcriptional upregulation ≠ functional involvement

2. **Experimental evidence is for autophagy, not meiosis**:
   - PMID:19778961: "autophagy-defective cells with amino acid auxotrophy were able to recover sporulation when an excess of required amino acids was supplied"
   - This proves autophagy provides nutrients during sporulation, not meiotic regulation

3. **Consistent pattern**: All 7 genes had the same over-annotation logic - upregulation during meiosis was conflated with functional involvement in meiotic cell cycle

### Lessons Learned from S. pombe Analysis

1. **Expression ≠ Function**: Genes upregulated during a biological process are not necessarily functional regulators of that process

2. **Support processes get conflated**: Autophagy supports meiosis/sporulation by providing nutrients, but ATG genes are not meiotic regulators

3. **Gene naming can mislead**: The "mug" (meiotically up-regulated gene) nomenclature led to inappropriate keyword assignments

4. **Closure filtering is essential**: 73% of naive SPKW-unique annotations were redundant with more specific experimental evidence

5. **Well-curated organisms still have systematic over-annotation**: Even with extensive PomBase curation, SPKW-derived annotations introduced errors

### Review Files Location

```
genes/SCHPO/
├── atg101/atg101-ai-review.yaml
├── atg13/atg13-ai-review.yaml
├── atg16/atg16-ai-review.yaml
├── atg2/atg2-ai-review.yaml
├── atg38/atg38-ai-review.yaml
├── atg5/atg5-ai-review.yaml
└── snx41/snx41-ai-review.yaml
```

---

## Subproject: D. melanogaster (Drosophila) SPKW-Only Annotations

### Overview

Analysis of TRUE SPKW-unique annotations in D. melanogaster using closure-based query.

### Key Statistics (2026-01-31)

| Metric | Count |
|--------|-------|
| TRUE SPKW-unique annotations | 4,101 |
| Unique genes | 2,753 |
| Unique terms | 198 |

### Distribution by Aspect

| Aspect | Annotations | Genes | Terms |
|--------|-------------|-------|-------|
| F (Molecular Function) | 2,501 (61%) | 1,695 | 71 |
| P (Biological Process) | 1,404 (34%) | 1,143 | 112 |
| C (Cellular Component) | 196 (5%) | 189 | 15 |

### Top TRUE SPKW-Unique Terms

| Term | Label | Genes | Notes |
|------|-------|-------|-------|
| GO:0046872 | metal ion binding | 1,088 | Very broad MF term |
| GO:0008270 | zinc ion binding | 436 | Broad MF term |
| GO:0051301 | cell division | 119 | Mix of legitimate and over-annotation |
| GO:0007165 | signal transduction | 115 | Broad term |
| GO:0045087 | innate immune response | 63 | Likely legitimate for AMPs |
| GO:0006915 | apoptotic process | 28 | Needs case-by-case review |
| GO:0031640 | killing of cells of another organism | 24 | **Legitimate** - lysozymes, AMPs |
| GO:0051321 | meiotic cell cycle | 20 | Different pattern than S. pombe |

### Pattern Analysis

**1. "Killing of cells of another organism" (GO:0031640) - LEGITIMATE**

24 genes with this annotation are primarily:
- **Lysozymes** (LysB, LysD, LysE, LysP, LysS, LysX) - with "hydrolase activity, acting on glycosyl bonds"
- **Antimicrobial peptides** (Drosomycin, Metchnikowin, Baramicin)
- **Spätzle** (spz) - cytokine that activates Toll pathway

These are legitimate annotations for antimicrobial effectors.

**2. Meiotic Cell Cycle (GO:0051321) - MIXED**

Unlike S. pombe where ATG genes were wrongly annotated, D. mel meiotic annotations include:
- **GATOR1 complex** (Nprl2, Nprl3, Iml1) - These have EXPERIMENTAL evidence for germline/meiotic functions (PMID:25512509) alongside their TOR-regulation role
- **Cell division genes** (Bub3, Cdc37, cnn) - Potentially legitimate
- Some may still be over-annotations requiring case-by-case review

**3. Apoptotic Process (GO:0006915) - NEEDS REVIEW**

28 genes include:
- **Legitimate**: Buffy (Bcl-2 family), HtrA2, Opa1, ASPP, Daxx
- **Questionable**: Akt, Pdk1, Lkb1 (growth signaling kinases)
- **Cross-talk**: BI-1 (has both apoptosis AND autophagy annotations)

### Key Differences from S. pombe

| Pattern | S. pombe | D. melanogaster |
|---------|----------|-----------------|
| Meiotic cell cycle | ATG genes over-annotated (NO experimental meiotic evidence) | GATOR1 complex has experimental meiotic evidence |
| Organism context | Unicellular - meiosis = sporulation | Multicellular - germline development |
| Main issue | Autophagy conflated with meiosis | Less clear-cut; some legitimate meiotic functions |

### Lessons Learned from D. melanogaster Analysis

1. **Organism biology matters**: The same GO term can have different validity in different organisms. Meiotic annotations in unicellular yeasts (sporulation) differ fundamentally from multicellular organisms (germline development).

2. **SPKW can capture legitimate unique biology**: The "killing of cells of another organism" annotations for lysozymes and AMPs are appropriate and represent genuine SPKW contributions.

3. **MF terms dominate TRUE SPKW-unique**: 61% of unique contributions are Molecular Function, often very broad terms (metal ion binding, zinc ion binding). These may be accurate but uninformative.

4. **GATOR1 is a special case**: These genes regulate both TOR signaling (autophagy) AND have bona fide germline functions. The meiotic annotation may be appropriate here, unlike S. pombe ATG genes.

5. **Apoptosis annotations need case-by-case review**: Unlike the systematic ATG over-annotation in S. pombe, D. mel apoptosis includes a mix of legitimate (Bcl-2 family) and questionable (growth kinases) annotations.

### Comparative Summary: S. pombe vs D. melanogaster

```
┌─────────────────────────────────────────────────────────────────────┐
│                    SPKW Over-Annotation Patterns                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  S. pombe (Unicellular Yeast)                                       │
│  ────────────────────────────                                       │
│  Pattern: Expression during meiosis → "Meiosis" keyword             │
│  Problem: ATG genes upregulated for autophagy during sporulation    │
│  Result:  SYSTEMATIC over-annotation (7/7 genes = 100%)             │
│  Action:  REMOVE meiotic cell cycle from all ATG genes              │
│                                                                      │
│  D. melanogaster (Multicellular)                                    │
│  ──────────────────────────────                                     │
│  Pattern: More nuanced - some legitimate, some questionable         │
│  Difference: Dedicated germline cells with distinct regulation      │
│  Result:  MIXED - requires case-by-case review                      │
│  Action:  Cannot apply blanket removal; need individual assessment  │
│                                                                      │
│  Key Insight: Same GO term, different validity by organism context  │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

### Detailed Case Studies (Full Reviews Completed 2026-01-31)

#### Case 1: Buffy - Regulation vs Participation Conflation ✓

**Gene:** Buffy (Q8T8Y5) - Bcl-2 family anti-apoptotic protein

**Review file:** `genes/DROME/Buffy/Buffy-ai-review.yaml`

**SPKW annotation:** GO:0006915 (apoptotic process)

**Experimental evidence:** GO:0043066 (negative regulation of apoptotic process) via IMP/IGI

**Review decision:** **MODIFY** → GO:0043066 (negative regulation of apoptotic process)

**Analysis:** Buffy REGULATES apoptosis (as a Bcl-2 family member), it doesn't participate in or execute apoptosis. The SPKW annotation conflates regulatory role with process membership. Key evidence:
- "Buffy, the second Drosophila Bcl-2-like protein, is a pro-survival protein" (PMID:12853472)
- Overexpression inhibits developmental and irradiation-induced apoptosis
- Localizes to ER (not mitochondria like Debcl)

**Category:** SPKW captures correct biology but at wrong specificity

---

#### Case 2: Ced-12 - Legitimate SPKW Contribution ✓

**Gene:** Ced-12 (Q9VKB2) - ELMO homolog, engulfment machinery

**Review file:** `genes/DROME/Ced-12/Ced-12-ai-review.yaml`

**SPKW annotations:** GO:0006915 (apoptotic process), GO:0006909 (phagocytosis)

**Experimental evidence (IMP/IGI):** cell migration, myoblast fusion, border follicle cell migration, actin organization

**Review decisions:**
- GO:0006909 (phagocytosis) → **ACCEPT** - legitimate conserved function
- GO:0006915 (apoptotic process) → **MODIFY** to GO:0043652 (engulfment of apoptotic cell)

**Analysis:** This is a **truly valuable SPKW contribution**. Ced-12/ELMO is named after C. elegans CED-12, a core component of apoptotic corpse engulfment machinery. D. melanogaster experimental work focused on cell migration and myoblast fusion, but the conserved efferocytosis function is captured ONLY by SPKW. The modification from "apoptotic process" to "engulfment of apoptotic cell" clarifies that ELMO functions in the engulfing cell, not the dying cell.

**Category:** SPKW provides unique functional insight missing from experimental annotations

---

#### Case 3: Sin1 - Over-annotation via Signaling Pathway ✓

**Gene:** Sin1 (Q9V719) - TORC2 complex subunit

**Review file:** `genes/DROME/Sin1/Sin1-ai-review.yaml`

**SPKW annotation:** GO:0006915 (apoptotic process)

**Experimental evidence:** TORC2 signaling (IGI), insulin receptor signaling (IMP), Akt activation

**Review decision:** **REMOVE**

**Analysis:** Sin1 is a TORC2 subunit. The pathway to apoptosis is too indirect:
```
Sin1 → TORC2 → Akt → Bad → apoptosis
       (4-5 enzymatic steps)
```
This is classic **signaling over-extension**. Sin1's core function is TORC2 complex assembly and substrate recruitment via its CRIM and PH domains. The apoptosis connection is too many steps removed to justify direct annotation.

**Category:** SPKW over-extends from indirect signaling connection

---

#### Case 4: LysB - Correct Function, Wrong Context ✓

**Gene:** LysB (Q08694) - Lysozyme B, glycosyl hydrolase family 22

**Review file:** `genes/DROME/LysB/LysB-ai-review.yaml`

**SPKW annotations:**
- GO:0031640 (killing of cells of another organism)
- GO:0042742 (defense response to bacterium)

**Review decisions:**
- GO:0031640 → **ACCEPT** - lysozyme activity DOES kill bacteria
- GO:0042742 → **MODIFY** to GO:0007586 (digestion)

**Analysis:** LysB is a **digestive enzyme**, not an immune effector:
- Expressed in midgut (larvae and adults), NOT in fat body or hemocytes
- REPRESSED (not induced) after bacterial infection
- UniProt: "Unlikely to play an active role in the humoral immune defense. May have a function in the digestion of bacteria in the food."

The "killing of cells of another organism" annotation is **correct** - lysozyme enzymatic activity does result in bacterial death. But the "defense response to bacterium" annotation implies immune function, which is **wrong** for LysB. The biological context is digestion, not immunity.

**Category:** SPKW captures correct molecular outcome but wrong biological context

---

### Categories of SPKW-Unique Annotations

| Category | Description | Example | Action |
|----------|-------------|---------|--------|
| **Regulation conflation** | Annotated to process when evidence is for regulation | Buffy | Consider MODIFY to regulation term |
| **Legitimate unique** | SPKW captures biology missing from experimental data | Ced-12 | KEEP - valuable contribution |
| **Signaling over-extension** | Indirect pathway connection | Sin1 | Consider REMOVE or very broad term |
| **Support process conflation** | Process X active during process Y | S. pombe ATG | REMOVE |
| **Correct but uninformative** | Very broad terms (metal ion binding) | CG genes | Keep but low priority |

### Recommendations for SPKW Curation

1. **Use closure-based queries**: Reduces false positives by 70%+ in well-curated organisms

2. **Check experimental evidence before removing**: D. mel GATOR1 genes have experimental meiotic evidence that S. pombe ATG genes lack

3. **Consider organism biology**: Unicellular vs multicellular organisms have fundamentally different meiotic biology

4. **Prioritize patterns over individual genes**: Finding systematic over-annotation patterns (like ATG-meiosis in yeast) is more impactful than reviewing individual genes

5. **Some SPKW annotations are legitimate**: Don't assume all SPKW-unique = over-annotation. Lysozymes and AMPs in D. mel are correctly annotated.

6. **Check for regulation vs participation**: SPKW often conflates regulatory roles with process membership - consider if a "regulation of X" term would be more appropriate

7. **Value novel functional insights**: Cases like Ced-12 where SPKW captures known biology that experimental annotations miss are valuable contributions to GO

---

# NOTES

## 2026-01-31

**S. pombe Meiotic Cell Cycle Over-Annotation Pattern Identified**

Analyzed TRUE SPKW-unique annotations in S. pombe using proper closure-based query (checking if non-SPKW evidence exists for child terms). Found 207 genes with TRUE SPKW-unique "meiotic cell cycle" (GO:0051321) annotations.

**Key finding**: ATG (autophagy) genes are annotated to "meiotic cell cycle" via SPKW, but this is an **over-annotation**:

| Gene | SPKW Terms | Experimental Evidence |
|------|-----------|----------------------|
| atg101 | meiotic cell cycle, autophagy, sporulation | autophagosome assembly (IMP), macroautophagy (IMP) |
| atg13 | meiotic cell cycle, autophagy, sporulation | macroautophagy (IMP), mitophagy (IMP) |
| atg16 | meiotic cell cycle, autophagy | macroautophagy (IMP) |
| atg2 | meiotic cell cycle, autophagy, sporulation | macroautophagy (IMP), lipid droplet autophagy (IMP) |
| atg38 | meiotic cell cycle, autophagy | macroautophagy (IMP) |
| atg5 | meiotic cell cycle, autophagy | macroautophagy (IMP), mitophagy (IMP), reticulophagy (IMP) |
| snx41 | meiotic cell cycle, autophagy | (sorting nexin for autophagy) |

**The pattern**: UniProt assigns the "Meiosis" keyword to ATG genes because autophagy is upregulated during meiosis/sporulation. This leads to GO:0051321 annotation via GO_REF:0000043. However, ATG genes are **autophagy machinery**, not meiotic regulators. They support meiosis by providing autophagy, but they don't regulate the meiotic cell cycle per se.

**Note on GO:0051321**: The term is NOT in `gocheck_do_not_annotate` - it's actually a GO slim term (goslim_yeast, goslim_drosophila). The specific meiotic phases (prophase I, metaphase I, etc.) ARE in do-not-annotate. So the term itself is appropriate for annotations, but the UniProt keyword mapping creates over-annotations.

**Same logic as human apoptosis**: Process X (autophagy) is active during process Y (meiosis), so genes for X get annotated to Y. This is a systematic SPKW over-annotation pattern.

---

## 2026-01-30

**D7 Family Review Completed (8 proteins)**

Completed comprehensive review of all 8 D7 salivary proteins in Anopheles gambiae.

**Summary**: All D7 proteins with GO:0090729 (4/4) are OVER-ANNOTATED; the other 4 D7 proteins do not carry the toxin activity annotation.

| Short forms (D7r1-5) | Long forms (D7L1-3) |
|---------------------|---------------------|
| D7r1-4: Bind biogenic amines | D7L1: Binds LTC4, TXA2 |
| D7r5: **NO binding** (pseudogene?) | D7L2: Weak LTB4/D4 binding |
| | D7L3: Binds serotonin only |

**D7r5 is particularly interesting** - it's the only D7 protein that does NOT bind any ligands. From PMID:16301315: "The nonbinding D7 protein is poorly expressed in the salivary glands and appears to be on the path to becoming a pseudogene."

---

**D7r1 Review Completed**

Completed detailed review of D7r1 (Q9UB30), the first D7 salivary protein in ANOGA.

**Key finding**: The "toxin activity" (GO:0090729) annotation is an **OVER-ANNOTATION**.

The GO definition of toxin activity requires "initiating pathogenesis (leading to an abnormal, generally detrimental state)" but D7r1:
1. Does NOT initiate pathogenesis - it facilitates feeding
2. Does NOT cause tissue damage - it transiently sequesters host mediators
3. The effect is reversible and temporary
4. The host returns to normal state after feeding

**Mechanism**: D7r1 functions as a "kratagonist" - a high-affinity scavenger that binds serotonin and histamine to prevent vasoconstriction, platelet aggregation, and inflammation at the feeding site.

**More accurate terms**:
- GO:0051378 (serotonin binding) - MF
- GO:0051381 (histamine binding) - MF
- GO:1900047 (negative regulation of hemostasis) - BP

**Also notable**: The "odorant binding" (GO:0005549) annotation from InterPro is based on structural family membership (PBP/GOBP) but D7r1 doesn't function in olfaction - it binds biogenic amines in saliva.

Review file: `genes/ANOGA/D7r1/D7r1-ai-review.yaml`

---

**ANOGA Subproject Initialized**

Performed initial DuckDB analysis of SPKW unique contributions to Anopheles gambiae:

- ANOGA has 86k total annotations, with 18k from SPKW
- 12,076 annotations (on 5,812 genes) are SPKW-unique (no corroborating evidence)
- Most SPKW-unique terms are in Molecular Function (83 terms, 7.9k annotations)
- High interest for vector biology: immune system process (147 genes), innate immune response (76 genes)
- D7 salivary proteins (D7r1, D7L1, D7L2, 7DL3) are interesting case study - their "toxin activity" annotation may be legitimate but term choice is questionable

**Key difference from human**: ANOGA has much less experimental annotation coverage, so SPKW contributions may be relatively more valuable as provisional annotations, even if over-annotation rates are similar to human.

**Next steps**: Select pilot batch focusing on immune/defense terms that are relevant to vector biology.

---

### PANTHER Family Analysis: PTHR11857 (OBP/PBP-related)

**Family context for D7 proteins**: The D7L1 and D7L2 proteins belong to PANTHER family PTHR11857 (Odorant-binding/pheromone-binding protein-related), specifically subfamily SF43 (GEO07291P1-RELATED).

**Deep research completed**: `interpro/panther/PTHR11857/PTHR11857-deep-research-falcon.md`

**Key findings about the family**:

| Subfamily | Structure | Function | Members in PTHR11857 |
|-----------|-----------|----------|---------------------|
| Classic OBPs | 6 Cys, 6 α-helices | Odorant transport | Drosophila Obp genes |
| Plus-C OBPs | ≥8 Cys, extra disulfides | Specialized/non-olfactory | Extended variants |
| Minus-C OBPs | 4-5 Cys, flexible | Broader ligand spectra | Reduced variants |
| PBPs | Classic scaffold | Sex pheromone binding | Lepidopteran PBPs |
| GOBPs | Similar to PBPs | Host volatile recognition | GOBP1/2 clades |
| **SF43** | Mixed D7s + OBPs | **Neo-functionalized** | D7L1, D7L2, Obp56d |

**Critical insight - Neo-functionalization**: The D7 salivary proteins in subfamily SF43 represent a clear case of **neo-functionalization**:

- **Ancestral function (OBPs)**: Transport odorants/pheromones to olfactory receptors in sensory lymph
- **Derived function (D7s)**: Sequester host signaling molecules (serotonin, histamine, leukotrienes) in saliva to facilitate blood feeding

Both share:
- Similar structural fold (OBP-like helical architecture)
- Bind similar ligands (biogenic amines)
- Extracellular secretion

But differ in:
- **Biological context**: Olfactory tissue vs. salivary gland
- **Biological role**: Sensory perception vs. anti-hemostatic adaptation
- **Evolutionary purpose**: Chemical communication vs. blood-feeding facilitation

**GO annotation implications**:

1. **"odorant binding" (GO:0005549)** - Based on family membership via InterPro, but D7 proteins don't function in olfaction → **MODIFY** to specific binding terms (serotonin/histamine/leukotriene binding)

2. **"toxin activity" (GO:0090729)** - Applied via SPKW "Toxin" keyword, but D7 proteins are kratagonists not toxins → **OVER-ANNOTATED**

3. **"extracellular space" (GO:0005615)** - Appropriate for both OBPs and D7s (both are secreted)

**This case study demonstrates how PANTHER family membership can propagate inappropriate GO annotations when neo-functionalization has occurred.**

---

### Immune Gene Pilot Batch Review (6 genes)

Reviewed 6 well-characterized ANOGA immune genes with SPKW-unique annotations to "immune system process" (GO:0002376).

| Gene | UniProt | Description | Immune Status | Key Issue Found |
|------|---------|-------------|---------------|-----------------|
| **TEP1** | C9XI63 | Thioester-containing protein 1 | ✅ LEGITIMATE | Remove "endopeptidase inhibitor" (opsonin, not inhibitor) |
| **SRPN2** | Q7QIJ8 | Serpin 2 | ✅ LEGITIMATE | Core melanization regulator, well-supported |
| **PGRPS1** | Q7QFK2 | Peptidoglycan recognition protein S1 | ✅ LEGITIMATE | Remove "amidase activity" (lacks catalytic residues) |
| **CLIPB4** | Q7PEV7 | CLIP-domain serine protease B4 | ✅ LEGITIMATE | Add GO:0035006 (melanization defense response) |
| **TOLL9** | Q5TWL7 | Toll receptor 9 | ✅ LEGITIMATE | Remove "inflammatory response" (vertebrate-specific term) |
| **psidin** | Q7PYI4 | Phagocyte signaling-impaired protein | ❌ OVER-ANNOTATED | Core function is NatB acetyltransferase subunit |

**Result: 5/6 (83%) immune annotations are LEGITIMATE**

#### Comparison: D7 vs Immune Genes

| Batch | Genes | Over-Annotation Rate | Pattern |
|-------|-------|---------------------|---------|
| D7 proteins | 8 | 100% | "Toxin activity" wrong for kratagonists |
| Immune genes | 6 | 17% | Most are bona fide immune genes |

#### Key Pattern: Secondary Over-annotations from Domain Homology

Even when the primary immune annotation is correct, we found **secondary over-annotations** from automated pipelines:

| Gene | Over-annotated Term | Source | Reason |
|------|---------------------|--------|--------|
| TEP1 | GO:0004866 (endopeptidase inhibitor) | InterPro | A2M domain ≠ inhibitor function |
| PGRPS1 | GO:0008745 (amidase activity) | IBA/IEA | Lacks catalytic zinc-binding residues |
| TOLL9 | GO:0006954 (inflammatory response) | IBA | Vertebrate-specific term for insects |
| psidin | GO:0002376 (immune system process) | IEA | Phenotype from Drosophila, not core function |

#### Biological Insights

1. **TEP1**: Complement-like opsonin that binds Plasmodium ookinetes via thioester bond
2. **SRPN2**: Key negative regulator of melanization cascade (inhibits CLIPB9/CLIPB10)
3. **PGRPS1**: Non-catalytic PGRP that senses bacterial peptidoglycan (Toll pathway)
4. **CLIPB4**: Upstream protease in prophenoloxidase activation cascade
5. **TOLL9**: Pattern recognition receptor activating Rel1/NF-κB pathway
6. **psidin**: NAA25/MDM20 ortholog - NatB complex subunit, NOT an immune protein

#### Files

All review files at `genes/ANOGA/`:
- TEP1, SRPN2, PGRPS1, CLIPB4, TOLL9, psidin

---

### PGRP/TEP Extended Batch Review (8 genes)

Extended review of PGRP (peptidoglycan recognition protein) and TEP (thioester-containing protein) families - key innate immune genes in Anopheles.

| Gene | UniProt | Description | Immune Status | Key Finding |
|------|---------|-------------|---------------|-------------|
| **PGRPLB** | F5HMW5 | PGRP-LB (catalytic, transmembrane) | ✅ LEGITIMATE | Catalytic amidase, negative regulator of IMD pathway |
| **PGRPLC** | A7UTA1 | PGRP-LC (non-catalytic, transmembrane) | ✅ LEGITIMATE | Principal IMD receptor; REMOVE "amidase activity" (non-catalytic) |
| **PGRPLD** | A0A1S4GYQ6 | PGRP-LD | ✅ LEGITIMATE | IMD pathway receptor |
| **PGRPS2** | D2SU82 | PGRP-S2 (secreted, catalytic) | ✅ LEGITIMATE | Catalytic amidase (retains His-His-Tyr-Cys zinc-binding) |
| **PGRPS3** | D2STP8 | PGRP-S3 (secreted, catalytic) | ✅ LEGITIMATE | Retains zinc-binding catalytic residues (unlike S1) |
| **TEP2** | Q5TQC0 | Thioester-containing protein 2 | ✅ LEGITIMATE | REMOVE "endopeptidase inhibitor" (opsonin, not inhibitor) |
| **TEP6** | Q7Q251 | Thioester-containing protein 6 | ✅ LEGITIMATE | REMOVE "endopeptidase inhibitor" (opsonin, not inhibitor) |
| **TEP10** | Q7PSK0 | Thioester-containing protein 10 | ✅ LEGITIMATE | REMOVE "endopeptidase inhibitor" (opsonin, not inhibitor) |

**Result: 8/8 (100%) immune annotations are LEGITIMATE**

#### Key Pattern: PGRP Catalytic vs Non-Catalytic

| PGRP Type | Examples | Zinc-binding Residues | Function |
|-----------|----------|----------------------|----------|
| **Catalytic** | PGRPLB, PGRPS2, PGRPS3 | Present (His-His-Tyr-Cys) | N-acetylmuramoyl-L-alanine amidase - degrades PGN |
| **Non-catalytic receptor** | PGRPLC, PGRPS1 | Absent/mutated | Pattern recognition receptor - binds PGN to signal |
| **Non-catalytic regulator** | PGRPLD | Absent | Negative regulator of immunity (no PGN binding/cleavage) |

#### Key Pattern: TEP "Endopeptidase Inhibitor" Over-annotation

All TEPs (TEP1, TEP2, TEP6, TEP10) are incorrectly annotated with **GO:0004866 (endopeptidase inhibitor activity)** based on InterPro A2M domain mapping. This is a systematic over-annotation:

- **Source**: InterPro2GO from IPR001599 (Alpha-2-macroglobulin)
- **Problem**: Vertebrate A2M proteins ARE protease inhibitors, but insect TEPs have **functionally diverged**
- **Reality**: Insect TEPs are **complement-like opsonins** that covalently tag pathogens via thioester bond
- **Action**: REMOVE the endopeptidase inhibitor annotation from all ANOGA TEPs

```
A2M Family Functional Divergence:
┌─────────────────────┐
│   Common Ancestor   │ (A2M domain + thioester)
└──────────┬──────────┘
           │
     ┌─────┴─────┐
     ▼           ▼
┌─────────┐ ┌──────────────┐
│Vertebrate│ │Insect TEPs   │
│A2M       │ │              │
└────┬────┘ └──────┬───────┘
     │             │
  Protease      Complement-like
  Trapping      Opsonization
     │             │
  Inhibitor     Pathogen
  Activity      Tagging
```

#### Files

All review files at `genes/ANOGA/`:
- PGRPLB, PGRPLC, PGRPLD, PGRPS2, PGRPS3, TEP2, TEP6, TEP10

---

## Subproject: P. putida (Pseudomonas putida) SPKW-Only Annotations

### Overview

P. putida KT2440 is a well-characterized environmental soil bacterium known for its metabolic versatility, solvent tolerance, and plant growth-promoting properties. Unlike the eukaryotic organisms analyzed previously, P. putida shows a distinctly different SPKW annotation pattern - one with much lower apparent over-annotation rates.

### Key Statistics (2026-01-31)

| Metric | Count |
|--------|-------|
| Total annotations | 30,961 |
| SPKW annotations | 7,290 (24%) |
| TRUE SPKW-unique (after closure) | 1,648 |
| Unique genes with TRUE SPKW-unique | 1,098 |
| Unique terms in TRUE SPKW-unique | 149 |
| **Closure filtering reduction** | **77%** |

### Distribution by Aspect

| Aspect | Annotations | Genes | Terms |
|--------|-------------|-------|-------|
| F (Molecular Function) | 1,171 (71%) | 842 | 54 |
| P (Biological Process) | 444 (27%) | 333 | 87 |
| C (Cellular Component) | 33 (2%) | 32 | 8 |

### Evidence Source Distribution

P. putida is primarily annotated via automated pipelines:

| Source | Annotations | Description |
|--------|-------------|-------------|
| GO_REF:0000002 | 9,048 | InterPro2GO |
| GO_REF:0000043 | 7,290 | UniProtKB-KW (SPKW) |
| GO_REF:0000118 | 5,244 | TreeGrafter phylogenetic |
| GO_REF:0000104 | 3,086 | UniRule |
| GO_REF:0000117 | 1,651 | UniProt automatic |

Very few experimental annotations exist (~50 from PMIDs), making automated pipelines the primary annotation source.

### Top TRUE SPKW-Unique Terms

| Term | Label | Genes | Assessment |
|------|-------|-------|------------|
| GO:0046872 | metal ion binding | 295 | Broad MF - likely accurate but uninformative |
| GO:0016787 | hydrolase activity | 130 | Broad MF - likely accurate |
| GO:0000166 | nucleotide binding | 130 | Broad MF - likely accurate |
| GO:0003677 | DNA binding | 115 | Broad MF - likely accurate |
| GO:0032259 | methylation | 41 | **LEGITIMATE** - methyltransferases |
| GO:0006508 | proteolysis | 33 | **LEGITIMATE** - proteases |
| GO:0071555 | cell wall organization | 32 | **LEGITIMATE** - PG biosynthesis |
| GO:0008360 | regulation of cell shape | 27 | **LEGITIMATE** - PG biosynthesis |
| GO:0046677 | response to antibiotic | 7 | **LEGITIMATE** - antibiotic resistance genes |
| GO:0046685 | response to arsenic | 6 | **LEGITIMATE** - arsenic resistance operons |
| GO:0051607 | defense response to virus | 3 | **QUESTIONABLE** - RT genes |

### Pattern Analysis

#### 1. Methylation (41 genes) - LEGITIMATE

Genes include:
- **ada** - O6-methylguanine-DNA methyltransferase (alkylation damage repair)
- **bioC** - Malonyl-CoA O-methyltransferase (biotin synthesis)
- **cheR2, cheR3** - Chemotaxis protein methyltransferases
- **cfa** - Cyclopropane-fatty-acyl-phospholipid synthase
- Various PP_XXXX locus tags

These are actual methyltransferases where "methylation" is their core function. **LEGITIMATE annotation.**

#### 2. Cell Wall / Cell Shape (32 + 27 genes) - LEGITIMATE

Genes include:
- **ftsI** - Peptidoglycan D,D-transpeptidase (PBP3)
- **mraY** - Phospho-N-acetylmuramoyl-pentapeptide-transferase
- **mrdA-I, mrdA-II** - Peptidoglycan D,D-transpeptidases (PBP2)
- **ddl, ddlA, ddlB** - D-alanine--D-alanine ligases
- **mrcA, mrcB** - Penicillin-binding proteins 1A/1B

These are peptidoglycan biosynthesis enzymes that DIRECTLY determine bacterial cell shape. In bacteria, cell wall biosynthesis = cell shape regulation. **LEGITIMATE annotation.**

#### 3. Response to Antibiotic (7 genes) - LEGITIMATE

| Gene | Function | Why Legitimate |
|------|----------|----------------|
| mrcA, mrcB | PBPs | Target of beta-lactams |
| amgK, anmK, murU, mupP | PG recycling | Cell wall integrity |
| ampC | Beta-lactamase | Direct antibiotic inactivation |
| pvdT | Pyoverdine transporter | Siderophore/efflux |

These genes confer antibiotic resistance as part of their core functions. Unlike eukaryotic over-annotations, these are not "downstream effects" - these genes ARE the antibiotic resistance mechanisms.

#### 4. Response to Arsenic (6 genes) - LEGITIMATE

P. putida has two arsenic resistance operons (ars1, ars2):
- **arsB-I, arsB-II** - Arsenite efflux pumps (also transport antimony)
- **arsR1, arsR2** - Arsenic-responsive transcription regulators
- **PP_1928, PP_2716** - Putative arsenic reductases

These are canonical arsenic resistance genes. **LEGITIMATE annotation.**

#### 5. Defense Response to Virus (3 genes) - QUESTIONABLE

| Gene | UniProt | Function |
|------|---------|----------|
| PP_0635 | Q877L4 | Reverse transcriptase |
| PP_1250 | Q877Q1 | Reverse transcriptase |
| PP_1846 | Q877L1 | Reverse transcriptase |

All three are reverse transcriptases, likely from mobile genetic elements (retrons or group II introns).

**Why this may be over-annotation:**
- Some bacterial RTs ARE involved in phage defense (DGRs, retrons in anti-phage systems, CRISPR-RTs)
- But most bacterial RTs are just mobile element machinery
- Without evidence these specific RTs function in defense, the annotation is speculative
- The UniProt "Host-virus interaction" keyword may be too broadly applied to any RT

**This is the only potential systematic over-annotation pattern identified in P. putida.**

### Key Differences from Eukaryotic Organisms

| Feature | Eukaryotes (Human, D. mel, S. pombe) | P. putida |
|---------|--------------------------------------|-----------|
| Over-annotation rate | 80-100% for BP terms | Very low (<5% estimated) |
| Main problematic terms | Apoptosis, meiosis, autophagy, rhythm | RT-based "defense response to virus" only |
| Pattern type | Process conflation (support ≠ participation) | Minimal - most annotations are accurate |
| MF vs BP | BP over-annotations common | MF dominates TRUE unique (71%) |
| Annotation density | Many annotations per gene | Sparse - few experimental |

### Why P. putida SPKW Annotations Are More Accurate

1. **Simpler biology**: Bacteria lack the complex regulatory networks (apoptosis, autophagy, circadian rhythms) that get over-annotated in eukaryotes

2. **Direct function mapping**: Bacterial gene functions map more directly to processes:
   - Methyltransferase → methylation (direct)
   - PBP → cell wall organization (direct)
   - Arsenic pump → arsenic response (direct)

3. **No process conflation**: Bacteria don't have meiosis, apoptosis, or circadian rhythms, so those problematic keyword mappings don't apply

4. **Less signaling complexity**: Fewer multi-step signaling pathways that lead to "4 steps removed" over-annotations (like Sin1 → TORC2 → Akt → apoptosis)

5. **UniProt keywords more appropriate**: Keywords like "Antibiotic resistance" map well to bacterial gene functions

### Comparison: SPKW Over-Annotation Patterns Across Organisms

```
Over-Annotation Severity by Organism Type
─────────────────────────────────────────────────────────────

Human (apoptosis/autophagy/rhythm):     ████████████████████  ~80-100%
S. pombe (meiotic cell cycle/ATG):      ████████████████████  ~100% (systematic)
D. melanogaster (apoptotic process):    ████████████          ~50% (mixed)
ANOGA - immune genes:                   ███                   ~17%
ANOGA - D7 "toxin activity":            ████████████████████  ~100%
P. putida (most BP terms):              █                     ~5% (mostly accurate)

Legend: Each █ = ~5% over-annotation rate
```

### Recommendations for P. putida Curation

1. **Low priority for manual review**: Unlike eukaryotic organisms, P. putida SPKW annotations appear largely accurate

2. **Focus on RT genes**: The 3 "defense response to virus" genes are the main candidates for review

3. **Validate MF terms are appropriate specificity**: Many are very broad (metal ion binding, hydrolase activity)

4. **Use as positive control**: P. putida demonstrates that SPKW can produce accurate annotations when:
   - Organism biology is simple (no complex regulatory networks)
   - Keywords map directly to gene functions
   - Evolutionary distances are small (bacterial keywords for bacteria)

### Conclusion

P. putida presents a stark contrast to the eukaryotic organisms analyzed in this project. While human, D. melanogaster, and S. pombe showed 80-100% over-annotation rates for BP terms like apoptosis, autophagy, and meiotic cell cycle, P. putida's TRUE SPKW-unique annotations are largely accurate.

This difference stems from:
1. Simpler bacterial biology without the complex processes that get conflated in eukaryotes
2. More direct mapping between UniProt keywords and bacterial gene functions
3. Absence of the "support process conflation" pattern (e.g., autophagy during meiosis)

The main lesson: **SPKW over-annotation is not universal** - it's driven by specific patterns in keyword-to-GO mappings for complex eukaryotic processes. For bacteria like P. putida, SPKW provides valuable provisional annotations that are largely accurate.

### Full Gene Reviews Completed (2026-01-31)

Four representative genes underwent complete annotation review with deep research:

| Gene | UniProt | Annotations | Key Finding |
|------|---------|-------------|-------------|
| PP_0635 | Q877L4 | 7 | **OVER-ANNOTATION** - "defense response to virus" incorrect for group II intron RT |
| ada | Q88PZ2 | 13 | **MODIFY** - "methylation" misleading; Ada removes methyl groups (dealkylation) |
| ampC | Q88IX3 | 5 | **LEGITIMATE** - "response to antibiotic" correct for beta-lactamase |
| mrcA | Q88CU6 | 16 | **LEGITIMATE** - cell shape/antibiotic response correct for PBP1A |

**Over-annotation rate: 1/4 (25%)** - confirming P. putida has much lower over-annotation than eukaryotes.

---

#### Case 1: PP_0635 - The One Over-Annotation ✓

**Gene:** PP_0635 (Q877L4) - Reverse transcriptase

**Review file:** `genes/PSEPK/PP_0635/PP_0635-ai-review.yaml`

**SPKW annotation:** GO:0051607 (defense response to virus)

**Review decision:** **REMOVE**

**Analysis:** PP_0635 is a **group II intron maturase** (based on Group_II_RT_mat and Mat_intron_G2 domains), NOT a defense-associated RT. This is a critical distinction:

| RT Type | Function | Defense? |
|---------|----------|----------|
| **Group II intron maturases** | Mobile element splicing/homing | NO |
| Retrons | Anti-phage abortive infection | YES |
| CRISPR-associated RTs | Adaptive immunity | YES |
| Diversity-generating retroelements (DGRs) | Receptor diversification | Indirect |

**Evidence:**
- Domain architecture is characteristic of group II introns, not retrons
- No retron operon (ncRNA + effector) found near PP_0635
- 2024 literature (Gapinska et al., NAR) explicitly distinguishes defense RTs from group II maturases

**This confirms the "defense response to virus" annotation was too broadly applied to all bacterial RTs.**

**Proposed replacement annotations:**
- GO:0006315 (homing of group II introns)
- GO:0000373 (Group II intron splicing)

---

#### Case 2: ada - Correct Biology, Wrong Term ✓

**Gene:** ada (Q88PZ2) - Bifunctional alkylation repair protein/transcription factor

**Review file:** `genes/PSEPK/ada/ada-ai-review.yaml`

**SPKW annotation:** GO:0032259 (methylation)

**Review decision:** **MODIFY** → GO:0035510 (DNA dealkylation)

**Analysis:** The "methylation" annotation is **misleading**. Ada does not add methyl groups to substrates - it REMOVES them from damaged DNA:

```
O6-methylguanine-DNA + Ada-Cys → guanine-DNA + Ada-S-methyl-Cys
                                         (suicidal reaction)
```

Ada is a methylated-DNA-[protein]-cysteine S-methyltransferase (EC 2.1.1.63), meaning the methyl group is transferred TO the protein, not FROM it. The correct GO term is GO:0035510 (DNA dealkylation).

**This is an example where SPKW captures the correct biology but the GO term mapping is imprecise.**

**Core functions confirmed:**
- GO:0003908 (methylated-DNA-[protein]-cysteine S-methyltransferase activity)
- GO:0006307 (DNA alkylation repair)
- GO:0003700 (DNA-binding transcription factor activity) - adaptive response regulator

---

#### Case 3: ampC - Legitimate Annotation ✓

**Gene:** ampC (Q88IX3) - Class C beta-lactamase

**Review file:** `genes/PSEPK/ampC/ampC-ai-review.yaml`

**SPKW annotation:** GO:0046677 (response to antibiotic)

**Review decision:** **ACCEPT**

**Analysis:** The "response to antibiotic" annotation is **fully legitimate** because:

1. **Inducible expression**: ampC expression is induced by beta-lactam antibiotics via AmpR-muropeptide signaling
2. **Direct function**: AmpC directly hydrolyzes beta-lactam antibiotics (cephalosporins, penicillins)
3. **Environmental response**: Also induced by indole and other environmental signals

This is NOT the "downstream effect" pattern seen in eukaryotes. AmpC IS the antibiotic response mechanism.

**Minor modification suggested:**
- GO:0017001 (antibiotic catabolic process) → GO:0030655 (beta-lactam antibiotic catabolic process) - more specific

---

#### Case 4: mrcA - Legitimate Multiple Annotations ✓

**Gene:** mrcA (Q88CU6) - Penicillin-binding protein 1A

**Review file:** `genes/PSEPK/mrcA/mrcA-ai-review.yaml`

**SPKW annotations:**
- GO:0008360 (regulation of cell shape) - **ACCEPT**
- GO:0046677 (response to antibiotic) - **ACCEPT**
- GO:0071555 (cell wall organization) - **MODIFY** to GO:0031504 (peptidoglycan-based cell wall organization)
- GO:0006508 (proteolysis) - **KEEP_AS_NON_CORE**

**Review decisions:** All **LEGITIMATE**

**Analysis:** PBP1A is a bifunctional enzyme:
- **Glycosyltransferase domain**: Polymerizes glycan chains (EC 2.4.99.28)
- **Transpeptidase domain**: Cross-links peptide stems (EC 3.4.16.4)

Both activities directly synthesize peptidoglycan, which:
1. Determines bacterial cell shape (rod vs coccus)
2. Is the target of beta-lactam antibiotics

Unlike Sin1 in D. melanogaster (4 steps to apoptosis), mrcA is **directly** involved in cell shape and is **directly** targeted by antibiotics.

---

### Summary: P. putida Curation Results

| Gene | Main SPKW Term | Action | Pattern |
|------|----------------|--------|---------|
| PP_0635 | defense response to virus | **REMOVE** | Keyword too broadly applied to RT family |
| ada | methylation | **MODIFY** | Correct biology, imprecise term |
| ampC | response to antibiotic | **ACCEPT** | Directly legitimate |
| mrcA | cell shape/antibiotic | **ACCEPT** | Directly legitimate |

**Key insight:** The ONE over-annotation (PP_0635) follows a specific pattern - the UniProt "Antiviral defense" keyword was applied to ALL bacterial reverse transcriptases, when only a subset (retrons, Abi systems) have defense functions. This is a targetable systematic error.

### Review Files Location

```
genes/PSEPK/
├── PP_0635/PP_0635-ai-review.yaml  (OVER-ANNOTATION: defense response)
├── ada/ada-ai-review.yaml          (MODIFY: methylation → dealkylation)
├── ampC/ampC-ai-review.yaml        (LEGITIMATE)
└── mrcA/mrcA-ai-review.yaml        (LEGITIMATE)
```

---

## Subproject: Arabidopsis thaliana (ARATH) SPKW-Only Annotations

### Overview

Arabidopsis thaliana is the premier plant model organism. Unlike TAIR (which has no SPKW annotations due to its own curation pipeline), the GOA database contains substantial SPKW-derived annotations. This analysis examines whether the over-annotation patterns seen in animals apply to plants.

### Key Statistics (2026-01-31)

| Metric | Count |
|--------|-------|
| Total annotations (GOA) | 299,228 |
| SPKW annotations | 46,710 (16%) |
| TRUE SPKW-unique (after closure) | 13,108 |
| Unique genes with TRUE SPKW-unique | 8,433 |
| Unique terms in TRUE SPKW-unique | 266 |
| **Closure filtering reduction** | **72%** |

### Distribution by Aspect

| Aspect | Annotations | Genes | Terms |
|--------|-------------|-------|-------|
| F (Molecular Function) | 7,225 (55%) | 4,980 | 80 |
| P (Biological Process) | 5,170 (39%) | 3,778 | 163 |
| C (Cellular Component) | 713 (6%) | 651 | 23 |

### Top TRUE SPKW-Unique Terms

| Term | Label | Genes | Expected Pattern |
|------|-------|-------|------------------|
| GO:0046872 | metal ion binding | 2,258 | Broad MF - legitimate |
| GO:0008270 | zinc ion binding | 1,035 | Broad MF - legitimate |
| GO:0006952 | defense response | 535 | **Mixed** - need case review |
| GO:0005524 | ATP binding | 517 | Broad MF - legitimate |
| GO:0071555 | cell wall organization | 305 | Likely legitimate |
| GO:0031640 | killing of cells of another organism | 291 | **Needs review** - defensins |
| GO:0050832 | defense response to fungus | 277 | Mixed |
| GO:0009734 | auxin-activated signaling pathway | 169 | **Needs review** |
| GO:0051301 | cell division | 204 | Likely legitimate |
| GO:0048511 | rhythmic process | 21 | **100% over-annotated in human** |
| GO:0051321 | meiotic cell cycle | 24 | **Problematic in S. pombe** |
| GO:0006914 | autophagy | 5 | 80% over-annotated in human |

### Plant-Specific Considerations

Unlike animals, plants have:
1. **Hormone signaling pathways** (auxin, ABA, ethylene, etc.) with specific GO terms
2. **Photosynthesis and light responses** - unique to photosynthetic organisms
3. **Cell wall biology** - fundamentally different from animal ECM
4. **Defense without immune cells** - rely on innate immunity in every cell
5. **Specialized reproductive biology** - pollen, self-incompatibility

### Full Gene Reviews Completed (2026-01-31)

| Gene | UniProt | Category | Key SPKW Term | Action | Finding |
|------|---------|----------|---------------|--------|---------|
| LCR1 | P82716 | Defensin | killing of cells | **REMOVE** | PCP-like DEFL, not antimicrobial |
| ELF4 | O04211 | Circadian | rhythmic process | **MARK_OVER_ANNOTATED** | Redundant with specific terms |
| ARF19 | Q8RYC8 | Hormone | auxin signaling | **MODIFY** | ARF responds TO auxin, not signal transduction |
| BUB3.1 | Q9LJN8 | Cell cycle | meiotic cell cycle | **MODIFY** | General SAC gene, not meiosis-specific |

**Over-annotation patterns: 3/4 genes had issues (75%)**

---

#### Case 1: LCR1 - Subclade-Specific Function vs Family Annotation ✓

**Gene:** LCR1 (P82716) - Defensin-like protein 147

**Review file:** `genes/ARATH/LCR1/LCR1-ai-review.yaml`

**SPKW annotation:** GO:0031640 (killing of cells of another organism)

**Review decision:** **REMOVE**

**Analysis:** This is a **surprising finding**. Unlike the D. melanogaster lysozymes which were correctly annotated to "killing", LCR1 should NOT have this annotation because:

1. **LCR1 is a PCP-like (pollen coat protein-like) defensin-like protein (DEFL)**
   - Within the ~300-member Arabidopsis DEFL family, LCR1 clusters with reproductive signaling proteins
   - This is distinct from PDF1.1/PDF1.2 defensins with proven antimicrobial activity

2. **Expression pattern contradicts defense function**
   - Expressed exclusively in flower buds
   - NOT in stems, roots, or leaves where defense would be needed

3. **No experimental antimicrobial evidence**
   - Deep research states: "LCR1's direct antimicrobial activity is not reported"
   - UniProt keywords based on family, not gene-specific data

**This demonstrates that family-level keyword assignments can miss subclade-specific functional divergence.**

---

#### Case 2: ELF4 - Legitimate but Redundant ✓

**Gene:** ELF4 (O04211) - EARLY FLOWERING 4

**Review file:** `genes/ARATH/ELF4/ELF4-ai-review.yaml`

**SPKW annotation:** GO:0048511 (rhythmic process)

**Review decision:** **MARK_AS_OVER_ANNOTATED**

**Analysis:** Unlike human "rhythmic process" genes (100% over-annotated), ELF4 IS a bona fide clock gene:
- Core component of the Evening Complex (EC) with ELF3 and LUX
- Experimental evidence for circadian rhythm regulation (IMP, IDA)

However, the "rhythmic process" annotation is **redundant** because ELF4 already has:
- GO:0042752 (regulation of circadian rhythm) - IDA
- GO:0042753 (positive regulation of circadian rhythm) - IMP
- GO:0009649 (entrainment of circadian clock) - IMP

**The SPKW annotation is accurate but adds no information beyond existing specific terms.**

Also identified: GO:0009908 (flower development) → MODIFY to GO:0009909 (regulation of flower development) - ELF4 controls flowering TIME, not flower organogenesis.

---

#### Case 3: ARF19 - Signaling Endpoint vs Transduction ✓

**Gene:** ARF19 (Q8RYC8) - Auxin Response Factor 19

**Review file:** `genes/ARATH/ARF19/ARF19-ai-review.yaml`

**SPKW annotation:** GO:0009734 (auxin-activated signaling pathway)

**Review decision:** **MODIFY** → GO:0009733 (response to auxin)

**Analysis:** This reveals a subtle but important distinction:

```
Auxin Signaling Pathway:
┌─────────────────────────────────────────────────────────┐
│ Auxin → TIR1/AFB receptor → AUX/IAA degradation → ARF  │
│   ↑                                                    │
│   Signal molecule                     Downstream effector
└─────────────────────────────────────────────────────────┘
```

ARF19:
- Does NOT bind auxin directly
- Is RELEASED from repression when AUX/IAA proteins are degraded
- Acts as the ENDPOINT transcription factor, not a signal transducer

The GO definition of "auxin-activated signaling pathway" refers to "binding of auxin to a receptor" - ARF19 is downstream of this. The correct term is GO:0009733 (response to auxin).

**This pattern is analogous to Sin1 in D. mel - both are downstream effectors incorrectly annotated to the signaling pathway.**

---

#### Case 4: BUB3.1 - General vs Specific Cell Cycle Function ✓

**Gene:** BUB3.1 (Q9LJN8) - BUB3 spindle checkpoint protein

**Review file:** `genes/ARATH/BUB3.1/BUB3.1-ai-review.yaml`

**SPKW annotation:** GO:0051321 (meiotic cell cycle)

**Review decision:** **MODIFY** → GO:0000278 (mitotic cell cycle)

**Analysis:** This parallels the S. pombe ATG gene pattern but with a key difference:

| Organism | Gene | Keyword | Actual Function | Over-annotation Type |
|----------|------|---------|-----------------|---------------------|
| S. pombe | atg5 | Meiosis | Autophagy | Completely wrong process |
| Arabidopsis | BUB3.1 | Meiosis | Cell cycle checkpoint | Wrong specificity within correct process |

BUB3.1 is a **general spindle assembly checkpoint protein**:
- Functions in BOTH mitosis and meiosis
- Experimental evidence is primarily for mitotic function
- Recent studies (2024) show BUB3.1/BUB3.2 specialize in cytokinesis, not meiosis

The "meiotic cell cycle" annotation implies a meiosis-specific function that is not supported. BUB3.3 appears to be the paralog with kinetochore-specific functions.

---

### Arabidopsis Over-Annotation Patterns

| Pattern | Example | Frequency | Severity |
|---------|---------|-----------|----------|
| **Subclade function divergence** | LCR1 (PCP-like, not antimicrobial) | Novel | High |
| **Redundant broad term** | ELF4 (rhythmic process) | Common | Low |
| **Downstream effector as pathway** | ARF19 (auxin signaling) | Common | Medium |
| **General as specific** | BUB3.1 (meiotic vs cell cycle) | Common | Medium |

### Comparison: Arabidopsis vs Other Organisms

| Organism | Over-Annotation Rate | Main Patterns |
|----------|---------------------|---------------|
| Human (apoptosis) | 80-100% | Process conflation |
| S. pombe (ATG-meiosis) | 100% | Support process conflation |
| D. melanogaster | 50% | Mixed |
| P. putida | 25% | RT defense keyword |
| **Arabidopsis** | **75%** | Subclade divergence, specificity |

### Key Lessons from Arabidopsis

1. **Subclade functional divergence matters**: The DEFL family shows that family-level keywords can mask subfunctionalization. LCR1 is in a reproductive signaling subclade, not an antimicrobial subclade.

2. **Redundancy is common in well-curated organisms**: When experimental annotations exist (ELF4), SPKW adds redundant broad terms rather than new information.

3. **Signaling endpoint ≠ signaling pathway**: ARF19 reveals the same pattern as Sin1 - downstream effectors get annotated to the pathway they respond to.

4. **Plants have similar meiosis over-annotation issues**: BUB3.1 shows that keywords like "Meiosis" get applied to general cell cycle genes, though less severely than the ATG-meiosis conflation in yeast.

### Recommendations for Plant SPKW Curation

1. **Review defensin family annotations**: Check if genes are in antimicrobial or PCP-like subclades before accepting "killing" annotations

2. **Validate hormone signaling terms**: Distinguish between signal transduction components and downstream response factors

3. **Check experimental redundancy**: For well-characterized genes, SPKW may add no new information

4. **Apply same meiosis criteria as yeast**: General cell cycle genes should not get meiosis-specific annotations without direct evidence

### Review Files Location

```
genes/ARATH/
├── LCR1/LCR1-ai-review.yaml      (REMOVE: killing - PCP-like subclade)
├── ELF4/ELF4-ai-review.yaml      (REDUNDANT: rhythmic process)
├── ARF19/ARF19-ai-review.yaml    (MODIFY: auxin signaling → response)
└── BUB3.1/BUB3.1-ai-review.yaml  (MODIFY: meiotic → mitotic cell cycle)
```

---

## Subproject: Bacteriophage T4 (BPT4) SPKW-Only Annotations

### Overview

Bacteriophages present a unique test case for SPKW annotation quality. Many GO terms relating to host-pathogen interactions were designed for eukaryotic pathogens (viruses, bacteria, fungi) infecting eukaryotic hosts. When these terms are applied to bacteriophages (which infect bacteria), semantic mismatches can occur.

**Key question**: Do GO terms for "immune suppression" and "defense response" apply when the host is a bacterium that lacks an immune system in the GO sense?

### Statistics (2026-01-31)

| Metric | Count |
|--------|-------|
| T4 genes in UniProt | ~300 |
| SPKW annotations (GO_REF:0000043) | ~150 |
| Genes with potentially problematic immune/defense terms | 3+ |

### Problematic Term Categories

1. **Eukaryotic immune terms applied to phage-bacteria interactions**:
   - GO:0052170 (symbiont-mediated suppression of host innate immune response)
   - GO:0052031 (symbiont-mediated perturbation of host defense response)
   - GO:0042742 (defense response to bacterium)

2. **Antibiotic response terms applied to phage enzymes**:
   - GO:0046677 (response to antibiotic)
   - GO:0031427 (response to methotrexate)

### Case Studies (3 genes reviewed)

---

#### Case 1: DAM - DNA Adenine Methyltransferase

**Gene:** DAM (P04392) - DNA adenine methylase

**Review file:** `genes/BPT4/DAM/DAM-ai-review.yaml`

**SPKW annotations to review:**
- GO:0052170 (symbiont-mediated suppression of host innate immune response)
- GO:0052031 (symbiont-mediated perturbation of host defense response)

**Review decision:** **REMOVE** both annotations

**Analysis:** This is a clear case of eukaryote-centric terms being incorrectly applied to a bacteriophage:

```
GO:0052170 Definition:
"Suppression by the symbiont of the innate immune response of the host organism"

The problem:
┌─────────────────────────────────────────────────────────────────────────────┐
│ Bacteria do NOT have an "innate immune response" in the GO sense           │
│                                                                             │
│ Eukaryotic innate immunity: Pattern recognition receptors (TLRs), cytokines│
│ Bacterial anti-phage defense: Restriction-modification, CRISPR-Cas, Abi    │
│                                                                             │
│ These are DIFFERENT biological systems requiring DIFFERENT GO terms        │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Correct term (already present):** GO:0099018 (symbiont-mediated evasion of host restriction-modification system)
- Definition explicitly mentions phages and bacterial R-M systems
- Accurately describes T4 Dam's biological role

**T4 Dam's actual function:**
1. Methylates GATC sites on phage DNA (Dam methylation)
2. Protects phage DNA from host restriction enzymes (DpnI, EcoRV, etc.)
3. May also regulate phage gene expression timing

**Why the SPKW keyword is wrong:** UniProt keyword "Inhibition of host innate immune response by virus" was designed for eukaryotic viruses (HIV, Influenza, etc.) suppressing human immune systems. Applying it to bacteriophages is semantically incorrect.

---

#### Case 2: E - T4 Lysozyme

**Gene:** E (P00720) - T4 phage lysozyme

**Review file:** `genes/BPT4/E/E-ai-review.yaml`

**SPKW annotation to review:**
- GO:0042742 (defense response to bacterium)

**Review decision:** **REMOVE**

**Analysis:** This annotation inverts the biological relationship:

```
GO:0042742 Definition:
"Reactions triggered in response to the presence of a bacterium that act
to protect the cell or organism"

How this term is properly used:
  Eukaryote (human) → produces lysozyme → kills invading bacteria
  This is DEFENSE

How it's misapplied to T4 lysozyme:
  T4 phage → produces lysozyme → lyses host bacterium for viral release
  This is PARASITISM, not defense!
```

**T4 lysozyme's actual function:**
1. Hydrolyzes peptidoglycan (beta-1,4 glycosidic bonds between NAM and NAG)
2. Part of the holin-endolysin-spanin lysis system
3. Enables progeny phage release through host cell lysis

**Correct annotation:** GO:0044659 (viral release from host cell by cytolysis) - already present and correctly describes the biological process.

**Additional issue found:**
- GO:0031640 (killing of cells of another organism) marked as OVER-ANNOTATED
- The host bacterium IS the organism in which the phage replicates; "another organism" framing is questionable

**Reference error noted:** PMID:4582731 is about T7 lysozyme (an amidase), not T4 lysozyme (a muramidase). The citation was incorrectly associated in the source database.

---

#### Case 3: frd - Dihydrofolate Reductase

**Gene:** frd (P04382) - Dihydrofolate reductase (T4 DHFR)

**Review file:** `genes/BPT4/frd/frd-ai-review.yaml`

**SPKW annotations to review:**
- GO:0046677 (response to antibiotic)
- GO:0031427 (response to methotrexate)

**Review decision:** **REMOVE** both annotations

**Analysis:** This conflates "being a drug target" with "responding to a drug":

```
The logic error:
┌─────────────────────────────────────────────────────────────────────────────┐
│ UniProt keywords: "Antibiotic resistance", "Trimethoprim resistance"        │
│                              ↓ (mapped to)                                  │
│ GO term: "response to antibiotic"                                           │
│                                                                             │
│ Problem: Being INHIBITED by an antibiotic ≠ RESPONDING to an antibiotic    │
│                                                                             │
│ - DHFR is the TARGET of trimethoprim (inhibits the enzyme)                  │
│ - Phages don't have "antibiotic response pathways"                          │
│ - T4 DHFR does NOT confer trimethoprim resistance                          │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Literature evidence (PMID:32253217, Sanchez-Osuna 2020):**
> "Phage-encoded DHFRs do NOT confer trimethoprim resistance despite homology"
> "Phage folA genes primarily serve phage nucleotide metabolism rather than resistance"

**T4 DHFR's actual function:**
1. Reduces dihydrofolate to tetrahydrofolate
2. Essential for thymidylate synthesis during phage DNA replication
3. Contributes to the phage's unique nucleotide pool (hydroxymethylcytosine production)

**Correct annotations (retained):**
- GO:0004146 (dihydrofolate reductase activity)
- GO:0046654 (tetrahydrofolate biosynthetic process)

---

### T4 Bacteriophage Over-Annotation Patterns

| Pattern | Example | Frequency | Severity |
|---------|---------|-----------|----------|
| **Eukaryotic immune terms for phage** | DAM (innate immune suppression) | High | **Critical** |
| **Defense/offense inversion** | E lysozyme (defense response) | Medium | High |
| **Drug target as drug response** | frd (antibiotic response) | Medium | Medium |

### Summary: Result 3/3 (100%) problematic annotations

All three T4 phage genes with SPKW-unique "immune" or "defense" annotations were over-annotated:

| Gene | UniProt | Problematic Annotation | Action | Correct Term |
|------|---------|------------------------|--------|--------------|
| DAM | P04392 | symbiont-mediated suppression of host innate immune response | **REMOVE** | GO:0099018 (R-M system evasion) |
| DAM | P04392 | symbiont-mediated perturbation of host defense response | **REMOVE** | GO:0099018 (R-M system evasion) |
| E | P00720 | defense response to bacterium | **REMOVE** | GO:0044659 (viral release by cytolysis) |
| frd | P04382 | response to antibiotic | **REMOVE** | (MF terms sufficient) |
| frd | P04382 | response to methotrexate | **REMOVE** | (MF terms sufficient) |

### Key Lessons from Bacteriophage Analysis

1. **GO terms encode eukaryote-centric biology**: Terms like "innate immune response" and "defense response" assume eukaryotic biology. Bacterial anti-phage systems (R-M, CRISPR) require different terminology.

2. **Host-pathogen terms need taxonomic context**: A term describing how a virus evades mammalian immunity should not be applied to a phage evading bacterial restriction.

3. **UniProt keywords are eukaryote-biased**: Keywords like "Inhibition of host innate immune response by virus" were created for eukaryotic viruses and don't translate to bacteriophages.

4. **"Defense" depends on perspective**: From the phage's perspective, lysozyme enables reproduction. From the bacterium's perspective, it's attack. Neither is "defense response to bacterium."

5. **Drug target ≠ drug response**: An enzyme being inhibited by an antibiotic doesn't mean the organism "responds" to that antibiotic in a biological process sense.

### Recommendations for Phage/Virus SPKW Curation

1. **Create phage-specific term mappings**: Keywords about host-pathogen interactions should map to different GO terms for phages vs. eukaryotic viruses

2. **Review all "innate immune" annotations on phage proteins**: These are likely systematically incorrect

3. **Distinguish R-M evasion from immune suppression**: GO:0099018 exists specifically for phage-bacteria interactions

4. **Validate "antibiotic resistance" claims**: Being a drug target does not equal conferring resistance, especially for phage enzymes

### Comparison: All Organisms Analyzed

| Organism | Domain | Over-Annotation Rate | Main Patterns |
|----------|--------|---------------------|---------------|
| Human | Eukarya | 80-100% | Process conflation |
| S. pombe | Eukarya | 100% (ATG-meiosis) | Support process conflation |
| D. melanogaster | Eukarya | 50% | Mixed |
| P. putida | Bacteria | 25% | RT defense keyword |
| Arabidopsis | Eukarya | 75% | Subclade divergence |
| **T4 Phage** | **Virus** | **100%** | **Eukaryote-centric terms** |
| **E. coli O157:H7** | **Bacteria** | **50%** | **Toxin vs effector confusion** |

### Review Files Location

```
genes/BPT4/
├── DAM/DAM-ai-review.yaml   (REMOVE: immune suppression - bacteria lack innate immunity)
├── E/E-ai-review.yaml       (REMOVE: defense response - phage is attacker not defender)
└── frd/frd-ai-review.yaml   (REMOVE: antibiotic response - drug target ≠ response)
```

### Status

- [x] Initial exploration complete (2026-01-31)
- [x] Deep research for all 3 genes (2026-01-31)
- [x] Annotation review complete for all 3 genes (2026-01-31)
- [x] Write-up complete (2026-01-31)

---

## Subproject: E. coli O157:H7 (ECO57) SPKW-Only Annotations

### Overview

E. coli O157:H7 is a pathogenic bacterium with well-characterized virulence factors including:
- **Shiga toxins (Stx1, Stx2)** - True toxins that kill host cells
- **Type III secretion system (T3SS) effectors** - Signaling modulators that manipulate host cells

This provides an ideal test case for distinguishing between:
1. **True toxins** - Proteins that directly damage/kill host cells (LEGITIMATE toxin annotations)
2. **Effectors** - Proteins that modulate signaling without direct cytotoxicity (potential OVER-ANNOTATIONS)

### Statistics (2026-01-31)

| Metric | Count |
|--------|-------|
| Total SPKW annotations (taxon:83334) | ~74,000 |
| SPKW-unique "toxin activity" annotations | 37 genes |
| SPKW-unique "killing of cells" annotations | 24 genes |

### Case Studies (2 genes reviewed)

---

#### Case 1: nleB1 - Type III Effector (OVER-ANNOTATED)

**Gene:** nleB1 (Q8XBX8) - Protein-arginine N-acetylglucosaminyltransferase

**Review file:** `genes/ECO57/nleB1/nleB1-ai-review.yaml`

**SPKW annotation:** GO:0090729 (toxin activity)

**Review decision:** **REMOVE**

**Analysis:** NleB1 is a T3SS effector that modulates host signaling, NOT a toxin:

```
True Toxin (e.g., Stx2A):
┌─────────────────────────────────────────────────────────────────────────────┐
│ Enters cell → Inactivates ribosomes → Halts translation → CELL DEATH       │
│                                                                             │
│ Direct cytotoxicity = TRUE TOXIN                                            │
└─────────────────────────────────────────────────────────────────────────────┘

NleB1 (Type III Effector):
┌─────────────────────────────────────────────────────────────────────────────┐
│ Injected via T3SS → GlcNAcylates death domain proteins → Blocks apoptosis  │
│                                                                             │
│ Modulates signaling = EFFECTOR, NOT TOXIN                                   │
│                                                                             │
│ Key difference: NleB1 PREVENTS cell death, not causes it!                   │
└─────────────────────────────────────────────────────────────────────────────┘
```

**NleB1's actual function:**
1. Glycosyltransferase that adds GlcNAc to arginine residues
2. Targets death domain proteins (FADD, TRADD, RIPK1)
3. Blocks death receptor signaling complex assembly
4. SUPPRESSES apoptosis and necroptosis - opposite of toxin!

**Literature evidence (PMID:30619781):**
> "NleB1 inhibitors were not significantly toxic to mammalian cells"
> "Did not cause significant macrophage death"

**Core function:** GO:0106362 (protein-arginine N-acetylglucosaminyltransferase activity)

---

#### Case 2: stx2A - Shiga Toxin A Subunit (LEGITIMATE)

**Gene:** stx2A (A0A9Q6Z964) - rRNA N-glycosylase

**Review file:** `genes/ECO57/stx2A/stx2A-ai-review.yaml`

**SPKW annotation:** GO:0090729 (toxin activity)

**Review decision:** **ACCEPT** (Legitimate annotation)

**Analysis:** Stx2A is a TRUE TOXIN with direct cytotoxic activity:

```
Shiga Toxin Mechanism:
┌─────────────────────────────────────────────────────────────────────────────┐
│ 1. B pentamer binds Gb3 receptor → Endocytosis                              │
│ 2. A chain cleaved by furin → A1 (catalytic) released to cytosol            │
│ 3. A1 depurinates A4324 in 28S rRNA sarcin-ricin loop                       │
│ 4. Ribosomes inactivated → Translation halted → CELL DEATH                  │
│                                                                             │
│ Direct ribosome inactivation = TRUE TOXIN ACTIVITY                          │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Stx2A's actual function:**
1. rRNA N-glycosylase (EC 3.2.2.22)
2. Depurinates specific adenine in 28S rRNA sarcin-ricin loop
3. Inactivates ribosomes (ribosome-inactivating protein, RIP)
4. Causes hemolytic uremic syndrome (HUS) in humans

**This is EXACTLY what "toxin activity" (GO:0090729) describes:**
> "initiating pathogenesis (leading to an abnormal, generally detrimental state)"

---

### Key Finding: Distinguishing Toxins from Effectors

| Property | True Toxin (Stx2A) | Effector (NleB1) |
|----------|-------------------|------------------|
| **Mechanism** | Direct cytotoxicity | Signaling modulation |
| **Effect on cell** | Kills cell | Manipulates cell |
| **Target** | Essential machinery (ribosomes) | Signaling proteins (death domains) |
| **Outcome** | Cell death | Cell survival (blocks apoptosis) |
| **GO:0090729 appropriate?** | **YES** | **NO** |

### Over-Annotation Pattern: "Toxin" Applied to Effectors

The UniProt "Toxin" keyword is being applied too broadly to T3SS effectors:

**Genes correctly annotated as toxins:**
- stx1A, stx1B, stx2A, stx2B (Shiga toxins) - TRUE TOXINS
- hlyA, hlyE (hemolysins) - TRUE TOXINS (pore-forming)

**Genes incorrectly annotated as toxins:**
- nleB1, nleB2 (glycosyltransferases) - EFFECTORS
- nleE (cysteine methyltransferase) - EFFECTOR

### Comparison: O157:H7 vs Other Organisms

| Organism | Domain | Toxin Annotation Accuracy | Notes |
|----------|--------|--------------------------|-------|
| E. coli O157:H7 | Bacteria | ~50% (split) | True toxins correct, effectors wrong |
| T4 Phage | Virus | 0% | No true toxins, all over-annotated |
| A. gambiae D7 | Eukarya | 0% | Kratagonists, not toxins |

### Recommendations for Bacterial Pathogen SPKW Curation

1. **Distinguish toxins from effectors**: Toxins directly kill; effectors modulate signaling

2. **Check mechanism of action**: Does the protein directly damage cells or manipulate them?

3. **Consider the biological outcome**: If a protein PREVENTS cell death (like NleB1), it's not a toxin

4. **Validate Shiga toxin family**: These are legitimate toxin annotations

5. **Review T3SS effector annotations**: Many may have incorrect "toxin" annotations

### Review Files Location

```
genes/ECO57/
├── nleB1/nleB1-ai-review.yaml   (REMOVE: toxin - is effector that blocks apoptosis)
└── stx2A/stx2A-ai-review.yaml   (ACCEPT: toxin - true ribosome-inactivating protein)
```

### Status

- [x] Initial exploration complete (2026-01-31)
- [x] Deep research for 2 genes (2026-01-31)
- [x] Annotation review complete (2026-01-31)
- [x] Write-up complete (2026-01-31)
- [ ] Additional T3SS effectors (nleB2, nleE, etc.) - future work
