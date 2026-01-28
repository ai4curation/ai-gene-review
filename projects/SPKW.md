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
| APLP1 | P51693 | Amyloid-like protein 1 | pending |
| AREL1 | O15033 | Apoptosis-resistant E3 ubiquitin ligase 1 | pending |
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
- Total reviewed: 21/280 genes (7.5%)
- Over-annotation rate: 81% (17/21)
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
| Apoptosis | 280 | 21 | 17 | 4 | 81% |
| Rhythmic Process | 146 | 5 | 5 | 0 | 100% |
| Autophagy | 123 | 14 | 11 | 3 | 79% |
| **Combined** | **549** | **40** | **33** | **7** | **82.5%** |

**Legitimate genes identified (7/40):**
1. AIMP2 - proapoptotic (p53/MDM2)
2. API5 - anti-apoptotic (caspase-2, Acinus)
3. AVEN - anti-apoptotic (BCL-XL, Apaf-1)
4. BCL2L12 - anti-apoptotic (Bcl-2 family)
5. DRAM1 - autophagy (lysosomal membrane, VAMP8 stabilization)
6. DRAM2 - autophagy (lysosomal membrane, autophagic flux)
7. DAP - autophagy regulation (mTORC1 substrate, negative regulator)

**Last updated**: 2026-01-19

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
