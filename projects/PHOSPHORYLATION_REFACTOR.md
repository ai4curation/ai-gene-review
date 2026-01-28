# Phosphorylation Annotation Refactor Project

## Overview

This project reviews GO annotations to phosphorylation-related terms (GO:0016310 or is-a/part-of descendants) for genes that are NOT annotated to protein kinase activity (GO:0004672 or descendants). The goal is to identify and correct potential over-annotations or mis-annotations where genes are annotated to phosphorylation processes without having kinase activity themselves.

Many genes may legitimately participate in phosphorylation without being kinases themselves - for example:
- **Cyclins**: Activate cyclin-dependent kinases but do not have kinase activity
- **Signaling ligands/receptors**: Trigger phosphorylation cascades but the phosphorylation is catalyzed by downstream kinases
- **Adapter proteins**: Scaffold kinase-substrate interactions
- **Regulatory subunits**: Regulate kinase activity without catalyzing phosphorylation

However, annotating these genes directly to "protein phosphorylation" (GO:0006468) may be an over-annotation. The correct annotation should be to the regulatory process (e.g., "positive regulation of protein phosphorylation") rather than the process itself.

---

## Executive Summary: Cross-Species Analysis

This project systematically analyzed phosphorylation annotations across **9 Model Organism Databases (MODs)**: human (GOA), mouse (MGI), rat (RGD), fly (FlyBase), zebrafish (ZFIN), worm (WormBase), Arabidopsis (TAIR), budding yeast (SGD), and fission yeast (PomBase).

### Annotation Quality by Database

| MOD | Organism | Problematic Annotations | Quality Grade |
|-----|----------|------------------------|---------------|
| **SGD** | S. cerevisiae | 0 | EXCELLENT |
| **PomBase** | S. pombe | 0 | EXCELLENT |
| **WormBase** | C. elegans | 0 | EXCELLENT |
| **ZFIN** | D. rerio | 1 | VERY GOOD |
| **FlyBase** | D. melanogaster | ~3 | GOOD |
| **TAIR** | A. thaliana | ~7-10 | GOOD |
| **RGD** | R. norvegicus | 11 | MODERATE |
| **MGI** | M. musculus | ~20 | NEEDS REVIEW |
| **GOA** | H. sapiens | ~45 | NEEDS REVIEW |

### Key Findings

1. **Yeast and worm MODs are gold standard.** SGD, PomBase, and WormBase all have zero phosphorylation over-annotations. Cyclins are correctly annotated to regulatory activity (GO:0016538 "cyclin-dependent protein serine/threonine kinase regulator activity"), not to phosphorylation processes. This is the correct pattern that other MODs should follow.

2. **Mammalian MODs have systematic annotation issues.** MGI and GOA show recurring patterns of over-annotation:
   - **Cyclins** annotated to "protein phosphorylation" when they should be annotated to regulatory activity
   - **Signaling ligands** (EGF, EPO, PDGF, GAS6, endothelin) annotated as if they catalyze phosphorylation, when they trigger receptor-mediated signaling cascades
   - **Phosphatases** annotated to phosphorylation - the opposite reaction! (CDC25B, PPP3CB, PTPN6 in human; TOPP4, CDC25 in Arabidopsis)
   - **Transcription factors** treated as kinases when they are substrates (CREB1, ATF2, ERG, RUNX3, RARA)
   - **Adapter proteins** credited with kinase activity belonging to associated kinases

3. **Errors propagate via ISS transfer.** The rat database (RGD) demonstrates this clearly: 7 of 11 problematic annotations are ISS transfers from mouse/human, replicating the same errors (Ppp3cb phosphatase, Glyctk sugar kinase, Gas6/Pdgfb ligands). The glycerate kinase error specifically appears in human (GLYCTK), fly (CG9886), zebrafish (glyctk), and rat (Glyctk). This highlights how computational inference methods can spread annotation errors across species.

4. **Opposite-reaction errors are particularly problematic.** Annotating phosphatases (enzymes that REMOVE phosphate) to phosphorylation (the process of ADDING phosphate) represents a fundamental biological error. Found in:
   - Human: CDC25B, PPP3CB, PTPN6, PPP4R1
   - Rat: Ppp3cb (calcineurin, ISS from human)
   - Arabidopsis: TOPP4, CDC25

5. **Lipid and sugar kinases require substrate-specific terms.** Genes like PI3K (lipid kinase), IP6K3 (inositol kinase), and GLYCTK (sugar kinase) should not be annotated to "protein phosphorylation" - they should use substrate-appropriate terms like GO:0046834 (lipid phosphorylation) or GO:0046835 (carbohydrate phosphorylation).

6. **Smaller, more focused MODs show higher quality.** The pattern suggests that databases with smaller genomes and longer curation histories (yeast, worm) have achieved more rigorous annotation standards for distinguishing between:
   - Genes that **catalyze** phosphorylation (kinases → GO:0006468)
   - Genes that **regulate** phosphorylation (cyclins, ligands → GO:0045859)
   - Genes that **are substrates** of phosphorylation (should not be annotated to BP)

### Recommended Actions

1. **Immediate corrections** for clear misannotations (phosphatases, sugar kinases)
2. **Systematic review** of cyclin annotations in mammalian MODs
3. **ISS transfer guidelines** should be tightened to prevent error propagation
4. **Training materials** on distinguishing process vs. regulatory annotations

---

## Taxonomy of Phosphorylation Over-Annotation Errors

This taxonomy categorizes the types of errors found when reviewing phosphorylation annotations. Each category has a short code for reference. Note that individual cases may exhibit features of multiple categories, and the detailed free-text summaries in gene reviews capture important nuances.

### S: Substrate-as-Enzyme Misannotation
The gene product is the **substrate** being phosphorylated, not the enzyme performing phosphorylation. This is the most common error type.

**Pattern**: Paper describes "phosphorylation OF [gene]" rather than "phosphorylation BY [gene]"

| Code | Subtype | Description | Examples |
|------|---------|-------------|----------|
| S | General | Gene is phosphorylated by a kinase | CTBP1, GMFB, GMFG, ILF3, Bcl2 |
| S-adapter | Adapter/signal | Adapter protein phosphorylated as part of signaling | HCST (DAP10), LIMD1 |
| S-tf | Transcription factor | TF phosphorylated to regulate activity | CREB1, ATF2, ERG, RUNX3, RARA |

**Diagnostic clue**: UniProt shows phosphorylation sites on the protein; paper title says "phosphorylation OF [gene]"

---

### W: Wrong Substrate Type
The gene is indeed a kinase, but phosphorylates **non-protein substrates**. GO:0006468 "protein phosphorylation" is incorrect.

| Code | Subtype | Correct Substrate | Correct GO Term | Examples |
|------|---------|-------------------|-----------------|----------|
| W-sugar | Sugar kinase | Carbohydrates | GO:0046835 | GLYCTK |
| W-lipid | Lipid kinase | Phospholipids | GO:0046834 | PIK3CD |
| W-inositol | Inositol kinase | Inositol polyphosphates | GO:0052746 | IP6K3 |
| W-nucleoside | Nucleoside kinase | Nucleosides | GO:0046939 | - |

**Diagnostic clue**: EC number indicates non-protein substrate (e.g., EC 2.7.1.137 for PI3K)

---

### O: Opposite Reaction (Phosphatase)
The gene encodes a **phosphatase** that catalyzes **dephosphorylation** (removes phosphate groups), the opposite of phosphorylation.

| Code | Subtype | EC Class | Examples |
|------|---------|----------|----------|
| O-tyr | Tyrosine phosphatase | EC 3.1.3.48 | PTPN6, CDC25B |
| O-ser | Ser/Thr phosphatase | EC 3.1.3.16 | PPP3CB, PPP4R1 |
| O-dual | Dual-specificity | EC 3.1.3.48 | CDC25B |

**Diagnostic clue**: Gene name contains "phosphatase", "PTP", "PP", "CDC25"; EC 3.1.3.x

---

### R: Regulatory Role
The gene **regulates** phosphorylation indirectly but does not catalyze it. Should be annotated to "regulation of..." terms.

| Code | Subtype | Mechanism | Preferred GO | Examples |
|------|---------|-----------|--------------|----------|
| R-cyclin | Cyclin/CDK activator | Activates CDK kinase | GO:0061575 | Ccnb1, Ccne1, CCNE1, Ccnt1, Cdk5r1 |
| R-ligand | Signaling ligand | Binds receptor, triggers cascade | GO:0045859 | Egf, Epo, Gas6, PDGFA, PDGFB |
| R-receptor | Receptor | Activates kinases on ligand binding | GO:0045859 | Drd1, Ednra |
| R-cytokine | Cytokine | Activates JAK-STAT pathway | GO:0042531 | IL15, IL21, IFNL4 |
| R-adapter | Adapter/scaffold | Recruits kinases to substrates | GO:0045859 | ABI2, YWHAZ, MAML1, PRRT1 |
| R-gtpase | GTPase | Regulates kinases via GTP cycling | GO:0045859 | Cdc42 |
| R-redox | Redox regulator | Controls phosphorylation via redox | GO:1903719 | PRDX4 |

**Diagnostic clue**: Gene activates/recruits kinases but has no kinase domain itself

---

### C: Complex-Level Attribution
The kinase activity belongs to **associated kinases in a complex**, not the annotated gene product itself.

| Code | Description | Examples |
|------|-------------|----------|
| C | Scaffold subunit of kinase complex | COPS2, COPS8 (COP9 signalosome - kinase activity from CK2/PKD) |

**Diagnostic clue**: Paper says "complex has kinase activity" but annotated gene is structural/scaffold subunit

---

### U: Ubiquitin Ligase Misclassification
The gene encodes an **E3 ubiquitin ligase** (EC 2.3.2.x), not a kinase.

| Code | Description | Examples |
|------|-------------|----------|
| U | E3 ubiquitin ligase | Cbl, BIRC6, MEX3B |

**Diagnostic clue**: RING finger domain; EC 2.3.2.x; UniProt shows ubiquitin ligase activity

---

### A: ATPase Misclassification
The gene has **ATPase activity** (ATP hydrolysis), which was confused with kinase activity (ATP-dependent phosphate transfer).

| Code | Description | Examples |
|------|-------------|----------|
| A | ATPase domain protein | MORC3 (GHL-ATPase) |

**Diagnostic clue**: ATPase domain (GHL, AAA+); EC 3.6.x.x

---

### X: Wrong Reference
The cited **PMID does not support** the annotation, either due to data entry error or the paper being about something else entirely.

| Code | Description | Examples |
|------|-------------|----------|
| X | PMID doesn't support annotation | TOLLIP (PMID:1085432 is about lymphoma from 1976) |

**Diagnostic clue**: Paper topic unrelated to gene or phosphorylation

---

### Combined Patterns

Some genes exhibit multiple error types:

| Gene | Primary | Secondary | Notes |
|------|---------|-----------|-------|
| PICK1 | R-adapter | S | Binds PKC (adapter) AND is phosphorylated at Thr-82 (substrate) |
| MAML1 | R-adapter | S | Recruits CDK8 AND is phosphorylated at Ser-314/360 |
| BIRC6 | U | S | E3 ligase AND shown as substrate in UniProt |
| TNKS | U (PARP) | S | Poly-ADP-ribosyltransferase AND phosphorylated by GSK3 |

---

### Summary Statistics by Error Type

Based on review of ~45 human and mouse genes:

| Category | Count | % | Action |
|----------|-------|---|--------|
| S (Substrate) | ~18 | 40% | REMOVE |
| R (Regulatory) | ~15 | 33% | MODIFY → regulatory term |
| W (Wrong substrate) | ~4 | 9% | MODIFY → correct substrate type |
| O (Opposite reaction) | ~4 | 9% | REMOVE |
| U (Ubiquitin ligase) | ~3 | 7% | REMOVE |
| A (ATPase) | ~1 | 2% | REMOVE |
| X (Wrong reference) | ~1 | 2% | REMOVE |

**Preferred replacement terms:**
- GO:0045859 "regulation of protein kinase activity" (most common)
- GO:0046834 "lipid phosphorylation" (for lipid kinases)
- GO:0046835 "carbohydrate phosphorylation" (for sugar kinases)
- GO:1903719 "regulation of I-kappaB phosphorylation" (for NF-κB pathway)
- GO:0042531 "positive regulation of tyrosine phosphorylation of STAT protein" (for cytokines)

---

## Query Methodology

### Rationale

The query strategy is based on a simple observation about GO annotation consistency:

1. **Kinase activity annotations (GO:0004672) are generally reliable.** When a curator annotates a gene to "protein kinase activity" or a child term, they are making a direct molecular function assignment: this gene product IS a kinase. These annotations typically require strong evidence (catalytic domain, enzymatic assay, etc.) and are rarely over-annotated.

2. **Phosphorylation process annotations (GO:0006468) are more heterogeneous.** Annotations to "protein phosphorylation" or child terms indicate the gene is involved in the biological process. This can mean the gene:
   - **Catalyzes** the reaction (kinase) - CORRECT if also has kinase activity annotation
   - **Regulates** the reaction (cyclin, ligand) - should use regulatory term instead
   - **Is phosphorylated** (substrate) - should not be annotated to BP at all
   - **Scaffolds** the reaction (adapter) - ambiguous, may warrant regulatory term

3. **The set difference is a priori suspect.** Genes annotated to phosphorylation (BP) that are NOT annotated to kinase activity (MF) form a candidate set for review. If a gene truly catalyzes protein phosphorylation, it should have both annotations. The absence of kinase activity suggests the phosphorylation annotation may be:
   - An over-annotation (gene regulates but doesn't catalyze)
   - A substrate-as-enzyme error (gene is phosphorylated, not phosphorylating)
   - A wrong-substrate error (gene phosphorylates lipids/sugars, not proteins)
   - An opposite-reaction error (gene is a phosphatase)

This approach assumes kinase activity annotations are correct and uses their absence as a flag for potential phosphorylation over-annotation. A separate project could review kinase activity annotations directly, but that is out of scope here.

### SQL Query

Using DuckDB databases from `~/repos/go-db/db/`:

```sql
-- Find genes annotated to phosphorylation PROCESS terms (GO:0016310) or descendants
-- that are NOT annotated to protein kinase activity (GO:0004672) or descendants
-- IMPORTANT: Exclude regulatory terms (activation/regulation) which GO places under
-- the phosphorylation hierarchy but are not problematic annotations
WITH phospho_genes AS (
    SELECT DISTINCT a.db_object_id, a.db_object_symbol, a.ontology_class_ref
    FROM gaf_association a
    INNER JOIN isa_partof_closure ipc ON a.ontology_class_ref = ipc.subject
    INNER JOIN term_label t ON a.ontology_class_ref = t.id
    WHERE ipc.object = 'GO:0016310'  -- phosphorylation
      AND t.label NOT LIKE '%activation%'
      AND t.label NOT LIKE '%regulation%'
),
kinase_genes AS (
    SELECT DISTINCT a.db_object_id
    FROM gaf_association a
    INNER JOIN isa_partof_closure ipc ON a.ontology_class_ref = ipc.subject
    WHERE ipc.object = 'GO:0004672'  -- protein kinase activity
)
SELECT p.*
FROM phospho_genes p
WHERE p.db_object_id NOT IN (SELECT db_object_id FROM kinase_genes);
```

**Note**: GO models some regulatory terms (e.g., GO:0042976 "activation of Janus kinase activity")
as subclasses of phosphorylation terms. These are excluded because they are appropriate annotations
for receptors/ligands that activate kinases - not over-annotations.

## Summary Statistics (Mouse - MGI database)

- **Total non-kinase genes with phosphorylation annotations**: 166 (after excluding regulatory terms)
- **Breakdown by term**:
  - protein phosphorylation (GO:0006468): 87 genes
  - carbohydrate phosphorylation (GO:0046835): 25 genes
  - peptidyl-tyrosine phosphorylation (GO:0018108): 11 genes
  - lipid phosphorylation (GO:0046834): 9 genes
  - activation of Janus kinase activity (GO:0042976): 8 genes
  - peptidyl-serine phosphorylation (GO:0018105): 8 genes
  - generic phosphorylation (GO:0016310): 7 genes
  - various other specific phosphorylation terms

- **Evidence type breakdown**:
  - ISO: 90 annotations (75 genes)
  - IDA: 70 annotations (65 genes)
  - IMP: 53 annotations (49 genes)
  - IEA: 53 annotations (28 genes)
  - ISS: 32 annotations (26 genes)
  - IBA: 25 annotations (19 genes)
  - TAS/NAS/IGI: Minor contributions

## Categories of Non-Kinase Phosphorylation Annotations

### Likely Correct (Not Kinases, But Legitimately Involved)
1. **Sugar kinases** (hexokinase, glucokinase, fructokinase): These are kinases but not PROTEIN kinases
2. **Lipid kinases** (diacylglycerol kinases): Phosphorylate lipids, not proteins
3. **Nucleoside kinases**: Phosphorylate nucleosides

### Potentially Problematic
1. **Cyclins** (Ccnb1, Ccne1): Activate CDKs but shouldn't be annotated to "protein phosphorylation" directly
2. **Signaling molecules** (Egf, Epo, Gas6): Ligands that trigger phosphorylation cascades
3. **Receptors** (Agtr1a, Drd1, Ednra): Receptors that activate kinase signaling
4. **Adapter proteins**: Scaffold proteins

## Model Species

**Primary: Mus musculus (mouse)**
- Database: `/Users/cjm/repos/go-db/db/mgi.ddb`
- Taxon ID: 10090

## Genes for Review (Priority Order)

### Priority 1: Cyclins and CDK Regulators
These are clear cases where "protein phosphorylation" is an over-annotation for genes that activate CDKs but do not catalyze phosphorylation themselves.

| Gene | UniProt | MGI ID | Annotation | Evidence | Status | Action |
|------|---------|--------|------------|----------|--------|--------|
| Ccnb1 | P24860 | MGI:88302 | protein phosphorylation (GO:0006468) | IDA | reviewed | MODIFY → GO:0045859 |
| Ccne1 | Q61457 | MGI:88316 | protein phosphorylation (GO:0006468) | IDA/ISS | reviewed | MODIFY → GO:0045859 |
| Ccnt1 | Q9QWV9 | MGI:1328363 | protein phosphorylation (GO:0006468) | ISO | reviewed | MODIFY → GO:0045859 |
| Cdk5r1 | P61809 | MGI:101764 | peptidyl-serine phosphorylation (GO:0018105) | ISO | reviewed | MODIFY → GO:0045859 |

**Rationale**: All cyclins and CDK activators form complexes with their CDK partners (e.g., Cyclin B1-CDK1, Cyclin E1-CDK2, Cyclin T1-CDK9, p35-CDK5). The kinase activity is performed by the CDK subunit, not by the cyclin/activator. UniProt states for each: "The cyclin subunit imparts substrate specificity to the complex" but "only the heterodimer shows kinase activity." These genes already have correct annotations to GO:0061575 "cyclin-dependent protein serine/threonine kinase activator activity".

### Priority 2: Signaling Ligands/Growth Factors
Ligands that trigger phosphorylation but shouldn't be annotated to the process directly.

| Gene | MGI ID | Annotation | Evidence | Priority |
|------|--------|------------|----------|----------|
| Egf | MGI:95290 | peptidyl-tyrosine phosphorylation | IDA | HIGH |
| Epo | MGI:95407 | peptidyl-serine phosphorylation | IDA | HIGH |
| Edn1 | MGI:95283 | protein phosphorylation | IDA | MEDIUM |
| Gas6 | MGI:95660 | protein phosphorylation | ISS/ISO | MEDIUM |
| Ang2 | MGI:104984 | protein phosphorylation | IDA/IMP | MEDIUM |

### Priority 3: Receptors
Receptors with "protein phosphorylation" annotations (after excluding regulatory terms).

| Gene | UniProt | MGI ID | Annotation | Evidence | Status | Action |
|------|---------|--------|------------|----------|--------|--------|
| Drd1 | Q61616 | MGI:99578 | protein phosphorylation (GO:0006468) | IDA | reviewed | MODIFY → GO:0045859 |
| Ednra | Q61614 | MGI:105923 | protein phosphorylation (GO:0006468) | IMP | reviewed | MODIFY → GO:0045859 |

**Note**: Agtr1a and Ghr were initially included but removed after refining the query methodology.
They only have GO:0042976 "activation of Janus kinase activity" which is a regulatory term -
appropriate for receptors that activate JAKs, not an over-annotation.

### Priority 4: Other Interesting Cases
| Gene | UniProt | MGI ID | Annotation | Evidence | Status | Action |
|------|---------|--------|------------|----------|--------|--------|
| App | P12023 | MGI:88059 | GO:0006468 protein phosphorylation | IMP | reviewed | REMOVE (describes dephosphorylation!) |
| Bcl2 | P10417 | MGI:88138 | GO:0018105/GO:0018107 peptidyl-Ser/Thr phosphorylation | IDA | reviewed | REMOVE (Bcl2 is SUBSTRATE, not enzyme) |
| Cbl | P22682 | MGI:88279 | GO:0006468 protein phosphorylation | ISS | reviewed | REMOVE (ubiquitin ligase, not kinase) |
| Cdc42 | P60766 | MGI:106211 | GO:0006468 protein phosphorylation | IMP | reviewed | MODIFY → GO:0045859 (GTPase, not kinase) |

## Expected Outcomes

For most of these genes, the appropriate curation action will be:
1. **MODIFY** to **GO:0045859 "regulation of protein kinase activity"** (or positive/negative children) - this is the preferred replacement term since the phosphorylation branch annotations will be removed
2. **ACCEPT** if there's legitimate evidence the gene product directly catalyzes phosphorylation (e.g., sugar kinases)
3. **REMOVE** if the annotation is clearly incorrect

## Key GO Terms

| GO ID | Term | Usage |
|-------|------|-------|
| GO:0016310 | phosphorylation | Parent BP term (problematic) |
| GO:0004672 | protein kinase activity | MF for actual kinases |
| GO:0006468 | protein phosphorylation | BP (problematic for non-kinases) |
| GO:0045859 | regulation of protein kinase activity | **PREFERRED REPLACEMENT** |
| GO:0071902 | positive regulation of protein serine/threonine kinase activity | More specific positive reg |
| GO:0043405 | regulation of MAP kinase activity | For MAPK pathway regulators |
| GO:0042976 | activation of Janus kinase activity | For JAK pathway (already used) |

---

# STATUS

- [x] Priority 1: Cyclins and CDK regulators (4/4)
  - [x] Ccnb1 - MODIFY GO:0006468 → GO:0045859
  - [x] Ccne1 - MODIFY GO:0006468 → GO:0045859 (2 annotations)
  - [x] Ccnt1 - MODIFY GO:0006468 → GO:0045859
  - [x] Cdk5r1 - MODIFY GO:0018105 → GO:0045859
- [x] Priority 2: Signaling ligands (5/5)
  - [x] Egf - MODIFY GO:0018108 → GO:0045859 (secreted ligand binds EGFR kinase)
  - [x] Epo - MODIFY GO:0018105 → GO:0045859 (hormone activates JAK2 via EPOR)
  - [x] Edn1 - MODIFY GO:0006468 → GO:0045859 (secreted peptide binds Ednra/Ednrb)
  - [x] Gas6 - MODIFY GO:0006468 → GO:0045859 (ligand for AXL/TYRO3/MER RTKs)
  - [x] Ang2 - **REMOVE** (MISANNOTATION: papers about Angiotensin II, not Angiogenin-2)
- [x] Priority 3: Receptors (2/2 reviewed)
  - [x] Drd1 - MODIFY GO:0006468 → GO:0045859
  - [x] Ednra - MODIFY GO:0006468 → GO:0045859
  - ~~Agtr1a~~ - removed (only has regulatory term, not a target)
  - ~~Ghr~~ - removed (only has regulatory term, not a target)
- [x] Priority 4: Other cases (4/4)
  - [x] App - **REMOVE** (paper PMID:16025111 describes DEphosphorylation, not phosphorylation!)
  - [x] Bcl2 - **REMOVE** (2 annotations: Bcl2 is SUBSTRATE of phosphorylation, not enzyme)
  - [x] Cbl - **REMOVE** (E3 ubiquitin ligase EC 2.3.2.27, not a kinase)
  - [x] Cdc42 - MODIFY → GO:0045859 (small GTPase EC 3.6.5.2, regulates kinases)

**Last updated**: 2026-01-18

---

# HUMAN PHOSPHORYLATION ANALYSIS

## Overview

Extending the mouse analysis to human (goa_human.ddb) using the same query methodology.

## Summary Statistics (Human - GOA database)

- **Total non-kinase genes with phosphorylation annotations**: 131 (after excluding regulatory terms)
- **Protein phosphorylation candidates (need review)**: 54 genes

### Breakdown by term type:
| Term | GO ID | Gene Count |
|------|-------|------------|
| protein phosphorylation | GO:0006468 | 32 |
| carbohydrate phosphorylation | GO:0046835 | 28 |
| lipid phosphorylation | GO:0046834 | 9 |
| phosphorylation (generic) | GO:0016310 | 6 |
| peptidyl-tyrosine phosphorylation | GO:0018108 | 4 |
| tyrosine phosphorylation of STAT protein | GO:0007260 | 3 |
| peptidyl-threonine phosphorylation | GO:0018107 | 2 |
| peptidyl-serine phosphorylation | GO:0018105 | 2 |
| I-kappaB phosphorylation | GO:0007252 | 2 |

**Notes**:
- Carbohydrate and lipid kinases are legitimate (non-protein kinases)
- Focus on protein/peptidyl phosphorylation terms (54 genes)

## Human Genes for Review (Priority Order)

### Priority H1: Phosphatases (CRITICAL - Opposite Function!)
These are PHOSPHATASES annotated to phosphorylation - the opposite reaction!

| Gene | UniProt | Annotation | Evidence | Expected Action |
|------|---------|------------|----------|-----------------|
| CDC25B | P30305 | protein phosphorylation (GO:0006468) | IDA | REMOVE (phosphatase!) |
| PPP3CB | P16298 | protein phosphorylation (GO:0006468) | ISS | REMOVE (calcineurin phosphatase) |
| PTPN6 | P29350 | peptidyl-tyrosine phosphorylation (GO:0018108) | IDA | REMOVE (SHP-1 phosphatase) |

**Rationale**: These are protein phosphatases (remove phosphate groups), not kinases (add phosphate groups). Annotating them to "phosphorylation" is fundamentally incorrect.

### Priority H2: Cyclins (Same as Mouse Pattern)

| Gene | UniProt | Annotation | Evidence | Expected Action |
|------|---------|------------|----------|-----------------|
| CCNE1 | P24864 | protein phosphorylation (GO:0006468) | IMP | MODIFY → GO:0045859 |

**Rationale**: Same as mouse Ccne1 - Cyclin E1 activates CDK2, which performs phosphorylation.

### Priority H3: Signaling Ligands/Growth Factors

| Gene | UniProt | Annotation | Evidence | Expected Action |
|------|---------|------------|----------|-----------------|
| GAS6 | Q14393 | protein phosphorylation (GO:0006468) | IDA | MODIFY → GO:0045859 |
| PDGFA | P04085 | peptidyl-tyrosine autophosphorylation (GO:0038083) | NAS | MODIFY |
| PDGFB | P01127 | peptidyl-tyrosine phosphorylation + protein phosphorylation | IDA | MODIFY → GO:0045859 |
| CALCA | P06881 | protein phosphorylation (GO:0006468) | IDA | MODIFY → GO:0045859 |
| ADM2 | Q7Z4H4 | protein phosphorylation (GO:0006468) | IDA | MODIFY → GO:0045859 |
| IGFBP3 | P17936 | protein phosphorylation (GO:0006468) | IDA | MODIFY → GO:0045859 |
| CCL11 | P51671 | protein phosphorylation (GO:0006468) | TAS | MODIFY → GO:0045859 |

**Rationale**: Ligands that bind receptors and trigger phosphorylation cascades but don't catalyze phosphorylation themselves.

### Priority H4: Cytokines (STAT Phosphorylation Pattern)

| Gene | UniProt | Annotation | Evidence | Expected Action |
|------|---------|------------|----------|-----------------|
| IL15 | P40933 | tyrosine phosphorylation of STAT protein (GO:0007260) | IDA | MODIFY → regulatory term |
| IL21 | Q9HBE4 | tyrosine phosphorylation of STAT protein (GO:0007260) | IDA | MODIFY → regulatory term |
| IFNL4 | K9M1U5 | tyrosine phosphorylation of STAT protein (GO:0007260) | IDA | MODIFY → regulatory term |

**Rationale**: Cytokines activate JAK-STAT signaling but don't directly phosphorylate STAT proteins. JAKs perform the phosphorylation.

### Priority H5: Transcription Factors (Likely Substrates)

| Gene | UniProt | Annotation | Evidence | Expected Action |
|------|---------|------------|----------|-----------------|
| CREB1 | P16220 | protein phosphorylation (GO:0006468) | IDA | INVESTIGATE |
| ATF2 | P15336 | peptidyl-threonine phosphorylation (GO:0018107) | IDA | INVESTIGATE |
| ERG | P11308 | protein phosphorylation (GO:0006468) | TAS | INVESTIGATE |
| RUNX3 | Q13761 | protein phosphorylation (GO:0006468) | IDA | INVESTIGATE |
| RARA | P10276 | protein phosphorylation (GO:0006468) | IMP | INVESTIGATE |

**Rationale**: Transcription factors are typically SUBSTRATES of phosphorylation, not enzymes. Need to verify if papers describe TF as enzyme or substrate.

### Priority H6: Adapter/Scaffold Proteins

| Gene | UniProt | Annotation | Evidence | Expected Action |
|------|---------|------------|----------|-----------------|
| ABI2 | Q9NYB9 | peptidyl-tyrosine phosphorylation (GO:0018108) | IDA | MODIFY → GO:0045859 |
| ABI3 | Q9P2A4 | peptidyl-tyrosine phosphorylation (GO:0018108) | IDA | MODIFY → GO:0045859 |
| YWHAZ | P63104 | protein phosphorylation (GO:0006468) | IMP | MODIFY → GO:0045859 |

**Rationale**: Adapter proteins scaffold kinase-substrate interactions but don't catalyze phosphorylation.

### Priority H7: Other Non-Kinase Enzymes

| Gene | UniProt | Annotation | Evidence | Expected Action |
|------|---------|------------|----------|-----------------|
| TNKS | O95271 | peptidyl-Ser/Thr phosphorylation | IDA | REMOVE (PARP, not kinase) |
| BIRC6 | Q9NR09 | protein phosphorylation (GO:0006468) | TAS | REMOVE (ubiquitin ligase) |
| LIPE | Q05469 | protein phosphorylation (GO:0006468) | TAS | REMOVE (lipase) |

### Other Genes for Review

| Gene | UniProt | Annotation | Evidence | Notes |
|------|---------|------------|----------|-------|
| ERC1 | Q8IUD2 | I-kappaB phosphorylation | IDA | Scaffold protein |
| PRDX4 | Q13162 | I-kappaB phosphorylation | TAS | Peroxiredoxin |
| MORC3 | Q14149 | peptidyl-serine + protein phosphorylation | IDA | ATPase |
| LIMD1 | Q9UGP4 | phosphorylation | IDA | LIM domain protein |
| TOLLIP | Q9H0E2 | phosphorylation | IDA | Signaling adapter |
| MEX3B | Q6ZN04 | protein autophosphorylation + protein phosphorylation | ISS | RNA binding |
| COPS2 | P61201 | protein phosphorylation | IDA | COP9 signalosome |
| COPS8 | Q99627 | protein phosphorylation | IDA | COP9 signalosome |
| CTBP1 | Q13363 | protein phosphorylation | TAS | Transcriptional corepressor |
| GLYCTK | Q8IVS8 | protein phosphorylation | IDA | Glycerate kinase |
| GMFB | P60983 | protein phosphorylation | TAS | Glia maturation factor |
| GMFG | O60234 | protein phosphorylation | TAS | Glia maturation factor |
| HCST | Q9UBK5 | protein phosphorylation | IGI | Immune receptor adapter |
| ILF3 | Q12906 | protein phosphorylation | IDA | Nuclear factor |
| IP6K3 | Q96PC2 | protein phosphorylation | IDA | Inositol kinase |
| MAML1 | Q92585 | protein phosphorylation | IDA | Notch coactivator |
| PICK1 | Q9NRD5 | protein phosphorylation | ISS | PDZ scaffold |
| PIK3CD | O00329 | protein phosphorylation | NAS | Lipid kinase |
| PPP4R1 | Q8TF05 | protein phosphorylation | ISS | PP4 regulatory subunit |
| PRRT1 | Q99946 | protein phosphorylation | ISS | Proline-rich transmembrane |

## Cross-Species Comparison

| Pattern | Mouse | Human | Notes |
|---------|-------|-------|-------|
| Cyclins | Ccnb1, Ccne1, Ccnt1 | CCNE1 | Same over-annotation pattern |
| GAS6 ligand | Gas6 | GAS6 | Same over-annotation |
| Phosphatases | - | CDC25B, PPP3CB, PTPN6 | Human-specific problem |
| Cytokines | - | IL15, IL21, IFNL4 | Human-specific |
| Ubiquitin ligases | Cbl | BIRC6 | Same pattern |

## STATUS (Human)

- [x] Priority H1: Phosphatases (3/3) **CRITICAL MISANNOTATIONS**
  - [x] CDC25B - **REMOVE** (phosphatase EC 3.1.3.48, dephosphorylates CDK1)
  - [x] PPP3CB - **REMOVE** (calcineurin phosphatase EC 3.1.3.16)
  - [x] PTPN6 - **REMOVE** (2 annotations - SHP-1 tyrosine phosphatase EC 3.1.3.48)
- [x] Priority H2: Cyclins (1/1)
  - [x] CCNE1 - **MODIFY** → GO:0045859 (cyclin activates CDK2, no kinase activity itself)
- [x] Priority H3: Signaling Ligands (6/6) *CALCA had no phosphorylation annotation*
  - [x] GAS6 - **MODIFY** → GO:0045859 (TAM receptor ligand)
  - [x] PDGFA - **REMOVE** (ligand annotated to autophosphorylation!)
  - [x] PDGFB - **MODIFY** (2 annotations) → GO:0045859 (PDGFR ligand)
  - [x] ADM2 - **MODIFY** → GO:0045859 (CALCRL/RAMP ligand)
  - [x] IGFBP3 - **MODIFY** → GO:0045859 (IGF binding protein)
  - [x] CCL11 - **MODIFY** → GO:0045859 (CCR3 chemokine ligand)
- [x] Priority H4: Cytokines (3/3)
  - [x] IL15 - **MODIFY** → GO:0042531 (cytokine INDUCES JAK-STAT, doesn't phosphorylate)
  - [x] IL21 - **MODIFY** → GO:0042531 (cytokine INDUCES JAK-STAT, doesn't phosphorylate)
  - [x] IFNL4 - **MODIFY** → GO:0042531 (type III interferon INDUCES JAK-STAT)
- [x] Priority H5: Transcription Factors (5/5)
  - [x] CREB1 - **REMOVE** (bZIP TF is SUBSTRATE, phosphorylated by CaMK/AKT/PKA)
  - [x] ATF2 - **REMOVE** (bZIP TF is SUBSTRATE, phosphorylated at Thr-69/71 by p38/ERK)
  - [x] ERG - **REMOVE** (ETS family TF is SUBSTRATE, phosphorylated by PKC)
  - [x] RUNX3 - **REMOVE** (Runt-domain TF is SUBSTRATE, phosphorylated by Src)
  - [x] RARA - **REMOVE** (nuclear receptor is SUBSTRATE, phosphorylated by AKT1/PKA)
- [x] Priority H6: Adapter Proteins (3/3)
  - [x] ABI2 - **MODIFY** → GO:0045859 (Abl interactor promotes c-Abl kinase activity, not enzyme)
  - [x] ABI3 - **ACCEPT** (correct NEGATIVE annotation - "does not promote" phosphorylation)
  - [x] YWHAZ - **MODIFY** → GO:0045859 (14-3-3 scaffold regulates RAF-ERK pathway)
- [x] Priority H7: Other Non-Kinase Enzymes (3/3)
  - [x] TNKS - **REMOVE** (PARP EC 2.4.2.30, paper describes GSK3 phosphorylating TNKS - substrate!)
  - [x] BIRC6 - **REMOVE** (ubiquitin ligase EC 2.3.2.24, no kinase activity - UniProt shows substrate)
  - [x] LIPE - **REMOVE** (lipase EC 3.1.1.79, paper explicitly describes LIPE as substrate of PKA/AMPK)

---

# NOTES

## 2026-01-19 (Session 9 continued - Batch 2)

**Other Genes for Review - Second Batch (5 genes)**

Reviewed 5 more genes from the "Other Genes" list:

1. **LIMD1** (Q9UGP4) - LIM domain scaffold protein
   - Annotation: GO:0016310 "phosphorylation" (IDA, PMID:18439753)
   - Paper title: "Cell cycle regulated phosphorylation OF LIMD1" - LIMD1 is the SUBSTRATE
   - UniProt shows LIMD1 phosphorylated at Ser-272, Ser-277, Ser-304, Ser-421, Ser-424
   - Action: **REMOVE** [S-adapter] (substrate-as-enzyme misannotation)

2. **TOLLIP** (Q9H0E2) - Signaling adapter (Toll-interacting protein)
   - Annotation: GO:0016310 "phosphorylation" (IDA, PMID:1085432)
   - **WRONG PMID**: PMID:1085432 is about "Malignant lymphoma" from 1976!
   - TOLLIP "Inhibits IRAK1 phosphorylation" - it REGULATES kinases, doesn't phosphorylate
   - Action: **REMOVE** [X + R-adapter] (wrong PMID + not a kinase)

3. **MEX3B** (Q6ZN04) - RNA-binding E3 ubiquitin ligase
   - Annotations: GO:0006468 + GO:0046777 "autophosphorylation" (ISS from MEX3C)
   - MEX3B has KH domains (RNA-binding) and RING finger (E3 ligase), NOT a kinase
   - UniProt shows MEX3B is PHOSPHORYLATED at Ser-4, Ser-288, Ser-462 - it's a substrate
   - Action: **REMOVE** [U + S] (2 annotations - E3 ligase and substrate, no kinase activity)

4. **COPS2** (P61201) - COP9 signalosome subunit 2
   - Annotation: GO:0006468 "protein phosphorylation" (IDA, PMID:9535219)
   - Paper shows CSN complex has kinase activity, but "via association with CK2 and PKD kinases"
   - COPS2 is a PCI-domain scaffold, not a kinase subunit
   - Action: **MODIFY** [C] → GO:0045859 "regulation of protein kinase activity"

5. **COPS8** (Q99627) - COP9 signalosome subunit 8
   - Annotation: GO:0006468 "protein phosphorylation" (IDA, PMID:9535219) - same paper as COPS2
   - Same issue: PCI-domain scaffold, kinase activity from associated kinases
   - Action: **MODIFY** [C] → GO:0045859 "regulation of protein kinase activity"

**New patterns identified:**
1. **Wrong PMID** (TOLLIP) - annotation references completely unrelated paper
2. **Complex-level kinase activity** (COPS2/8) - multiprotein complex has kinase activity via associated kinases, but scaffold subunits incorrectly annotated

---

## 2026-01-19 (Session 9 continued - Batch 3)

**Other Genes for Review - Third Batch (10 genes)**

Reviewed final 10 genes from the "Other Genes" list:

1. **CTBP1** (Q13363) - Transcriptional corepressor
   - Annotation: GO:0006468 "protein phosphorylation" (TAS, PMID:8440238)
   - Paper: "CtBP is a phosphoprotein" - CTBP1 is the SUBSTRATE, phosphorylated by HIPK2
   - Action: **REMOVE** [S] (substrate-as-enzyme misannotation)

2. **GMFB** (P60983) - Glia maturation factor beta
   - Annotation: GO:0006468 "protein phosphorylation" (TAS, PMID:7598724)
   - Paper: "GMF can be phosphorylated in vitro... by PKC, PKA, and CKII"
   - Action: **REMOVE** [S] (substrate-as-enzyme misannotation)

3. **GMFG** (O60234) - Glia maturation factor gamma
   - Annotation: GO:0006468 "protein phosphorylation" (TAS, PMID:7598724)
   - Same paper as GMFB - GMF family proteins are substrates of kinases
   - Action: **REMOVE** [S] (substrate-as-enzyme misannotation)

4. **HCST** (Q9UBK5) - Hematopoietic cell signal transducer (DAP10)
   - Annotation: GO:0006468 "protein phosphorylation" (IGI, PMID:10528161)
   - Paper: "binds PI3-kinase following phosphorylation of a cytoplasmic YINM motif"
   - HCST is phosphorylated and then recruits PI3K - adapter, not kinase
   - Action: **REMOVE** [S-adapter] (adapter protein, substrate)

5. **ILF3** (Q12906) - Interleukin enhancer-binding factor 3 (NFAR)
   - Annotation: GO:0006468 "protein phosphorylation" (IDA, PMID:21123651)
   - Paper title: "Phosphorylation of the NFAR proteins BY... PKR"
   - ILF3/NFAR is the SUBSTRATE, phosphorylated by PKR at Thr-188 and Thr-315
   - Action: **REMOVE** [S] (substrate-as-enzyme misannotation)

6. **MAML1** (Q92585) - Mastermind-like protein 1
   - Annotation: GO:0006468 "protein phosphorylation" (IDA, PMID:16510869)
   - MAML1 is transcriptional coactivator that "recruits CycC:CDK8 to phosphorylate Notch ICD"
   - Also phosphorylated at Ser-314, Ser-360 (substrate)
   - Action: **MODIFY** [R-adapter + S] → GO:0045859 (recruits kinases, regulatory role)

7. **PICK1** (Q9NRD5) - PRKCA-binding protein
   - Annotation: GO:0006468 "protein phosphorylation" (ISS, GO_REF:0000024)
   - PICK1 = "Protein interacting with C kinase 1" - binds PKC, doesn't have kinase activity
   - Phosphorylated at Thr-82 (substrate), PDZ scaffold protein
   - Action: **REMOVE** [R-adapter + S] (scaffold, not kinase)

8. **PIK3CD** (O00329) - PI3K catalytic subunit delta
   - Annotation: GO:0006468 "protein phosphorylation" (NAS, PMID:9113989)
   - PIK3CD is a LIPID kinase (EC 2.7.1.137) - phosphorylates phosphatidylinositol, NOT proteins
   - Paper: "does not phosphorylate p85" (unlike p110alpha), only has autophosphorylation
   - Action: **MODIFY** [W-lipid] → GO:0046834 "lipid phosphorylation"

9. **PPP4R1** (Q8TF05) - Protein phosphatase 4 regulatory subunit 1
   - Annotation: GO:0006468 "protein phosphorylation" (ISS, GO_REF:0000024)
   - PPP4R1 is regulatory subunit of a PHOSPHATASE (PP4) - catalyzes DEPHOSPHORYLATION!
   - Paper: "PP4-phosphatase complex dephosphorylates gamma-H2AX"
   - Action: **REMOVE** [O-ser] (OPPOSITE REACTION - phosphatase, not kinase!)

10. **PRRT1** (Q99946) - Proline-rich transmembrane protein 1 (SynDIG4)
    - Annotation: GO:0006468 "protein phosphorylation" (ISS, GO_REF:0000024)
    - PRRT1 is transmembrane protein, AMPAR auxiliary subunit
    - Function: "regulating basal phosphorylation levels of GRIA1" - REGULATES, not catalyzes
    - Action: **MODIFY** [R-adapter] → GO:0045859 (regulatory role)

**Summary of Third Batch:**
- **REMOVE**: 7 genes (CTBP1[S], GMFB[S], GMFG[S], HCST[S-adapter], ILF3[S], PICK1[R-adapter+S], PPP4R1[O-ser])
- **MODIFY**: 3 genes (MAML1[R-adapter+S], PIK3CD[W-lipid], PRRT1[R-adapter])

**New pattern identified:**
- **Lipid kinase** [W-lipid] (PIK3CD) - EC number for lipid substrate phosphorylation, not protein

---

## 2026-01-19 (Session 9 continued)

**Other Genes for Review - First Batch (5 genes)**

Reviewed 5 genes from the "Other Genes" list:

1. **ERC1** (Q8IUD2) - Scaffold protein
   - Annotation: GO:0007252 "I-kappaB phosphorylation" (IDA)
   - Status: **ALREADY CORRECTED** in GOA (now has GO:0043123 "positive regulation of canonical NF-kappaB signal transduction")
   - ERC1 is a regulatory subunit of IKK complex, not a kinase

2. **PRDX4** (Q13162) - Peroxiredoxin (EC 1.11.1.24)
   - Annotation: GO:0007252 "I-kappaB phosphorylation" (TAS, PMID:9388242)
   - Paper: "Regulatory role... regulates NF-kappaB activity via a modulation of IkappaB-alpha phosphorylation"
   - PRDX4 is an antioxidant that REGULATES IkappaB phosphorylation through redox control
   - Action: **MODIFY** → GO:1903719 "regulation of I-kappaB phosphorylation"

3. **MORC3** (Q14149) - GHL-ATPase domain protein
   - Annotations: GO:0006468 + GO:0018105 (IDA, PMID:17332504)
   - Paper: "genotoxic stress-induced phosphorylation... in Morc3-/- fibroblasts" - p53 IS phosphorylated even without MORC3
   - MORC3 affects p53 activity through PML-NB recruitment, not by performing phosphorylation
   - Action: **REMOVE** (2 annotations)

4. **GLYCTK** (Q8IVS8) - Glycerate kinase (EC 2.7.1.31)
   - Annotation: GO:0006468 "protein phosphorylation" (IDA, PMID:16753811)
   - GLYCTK is a SUGAR kinase - it phosphorylates D-glycerate, NOT proteins
   - Already has correct annotation GO:0008887 "glycerate kinase activity"
   - Action: **REMOVE** (wrong substrate type)

5. **IP6K3** (Q96PC2) - Inositol hexakisphosphate kinase 3 (EC 2.7.4.21)
   - Annotation: GO:0006468 "protein phosphorylation" (IDA, PMID:11502751)
   - IP6K3 is an INOSITOL POLYPHOSPHATE kinase - it phosphorylates InsP6, NOT proteins
   - Paper title: "Identification and characterization of a novel inositol hexakisphosphate kinase"
   - Action: **REMOVE** (wrong substrate type)

**Key insight**: Found two new categories of misannotation:
1. **Small molecule kinases** (GLYCTK, IP6K3) - phosphorylate sugars or inositol polyphosphates, not proteins
2. **ATPases** (MORC3) - have ATPase activity but confused with kinase activity

---

## 2026-01-19 (Session 9)

**Human Priority H7: Other Non-Kinase Enzymes - Complete**

All 3 genes reviewed. ALL are misannotations where non-kinase enzymes are incorrectly
annotated to phosphorylation. These genes are SUBSTRATES of kinases, not enzymes:

1. **TNKS** (O95271) - Tankyrase-1
   - Annotations: GO:0018105 "peptidyl-serine phosphorylation" + GO:0018107 "peptidyl-threonine
     phosphorylation" (IDA, PMID:17026964)
   - TNKS is a Poly ADP-ribose polymerase (PARP, EC 2.4.2.30) - NOT a kinase
   - Paper title: "Mitotic phosphorylation of tankyrase... by GSK3"
   - GSK3 is the kinase that phosphorylates TNKS at S978, T982, S987, S991
   - TNKS is the SUBSTRATE, GSK3 is the kinase
   - Action: **REMOVE** (2 annotations)

2. **BIRC6** (Q9NR09) - Baculoviral IAP repeat-containing protein 6 (BRUCE/Apollon)
   - Annotation: GO:0006468 "protein phosphorylation" (TAS, PMID:18329369)
   - BIRC6 is a ubiquitin-conjugating E2/E3 enzyme (EC 2.3.2.24) - NOT a kinase
   - Paper describes BRUCE's "ubiquitin-conjugating activity" in cytokinesis abscission
   - No mention of phosphorylation activity
   - UniProt shows BIRC6 is PHOSPHORYLATED at Ser-480, Ser-581, etc. - it's a substrate
   - Action: **REMOVE**

3. **LIPE** (Q05469) - Hormone-sensitive lipase
   - Annotation: GO:0006468 "protein phosphorylation" (TAS, PMID:3420405)
   - LIPE is a lipase (EC 3.1.1.79) - NOT a kinase
   - Paper title: "Hormone-sensitive lipase: sequence, expression, and chromosomal localization"
   - PMID:3420405: "Hormone-sensitive lipase...is acutely controlled through reversible
     phosphorylation by catecholamines and insulin"
   - "The activity-controlling phosphorylation site was localized to Ser563"
   - LIPE is the SUBSTRATE of PKA/AMPK phosphorylation that regulates its lipase activity
   - Action: **REMOVE**

**Key insight**: These are all enzymes with well-characterized non-kinase activities
(PARP, ubiquitin ligase, lipase) that are REGULATED by phosphorylation - they are
substrates of kinases, not enzymes that perform phosphorylation.

---

## ALL HUMAN PRIORITIES COMPLETE (H1-H7)

Total genes reviewed: 24
- H1 Phosphatases: 3 → REMOVE (opposite function!)
- H2 Cyclins: 1 → MODIFY
- H3 Signaling Ligands: 6 → 5 MODIFY, 1 REMOVE (PDGFA)
- H4 Cytokines: 3 → MODIFY
- H5 Transcription Factors: 5 → REMOVE (substrates, not enzymes)
- H6 Adapter Proteins: 3 → 2 MODIFY, 1 ACCEPT (negative annotation)
- H7 Other Non-Kinase Enzymes: 3 → REMOVE (substrates of kinases)

## 2026-01-19 (Session 8 continued)

**Human Priority H6: Adapter Proteins - Complete**

All 3 adapter/scaffold proteins reviewed:

1. **ABI2** (Q9NYB9) - Abl interactor 2
   - Annotation: GO:0018108 "peptidyl-tyrosine phosphorylation" (IDA, PMID:17101133)
   - ABI2 is an Abl interactor that PROMOTES c-Abl kinase-mediated phosphorylation
   - PMID:17101133: "Abi-2... promoted the c-Abl-mediated phosphorylation of Mena"
   - c-Abl is the kinase, ABI2 is the regulator/adapter
   - Action: **MODIFY** → GO:0045859

2. **ABI3** (Q9P2A4) - ABI gene family member 3 (NESH)
   - Annotation: GO:0018108 "peptidyl-tyrosine phosphorylation" (IDA, PMID:17101133, **NEGATED**)
   - This is a CORRECT NEGATIVE annotation
   - PMID:17101133: "NESH (Abi-3) had no such effect" on promoting phosphorylation
   - Unlike Abi-1/2, NESH does NOT promote c-Abl-mediated phosphorylation
   - Action: **ACCEPT** (correct negative annotation)

3. **YWHAZ** (P63104) - 14-3-3 protein zeta/delta
   - Annotation: GO:0006468 "protein phosphorylation" (IMP, PMID:31024343)
   - YWHAZ is a 14-3-3 scaffold protein that REGULATES RAF-ERK signaling
   - PMID:31024343: "enhances Raf-stimulated Erk phosphorylation" - RAF is kinase
   - 14-3-3 proteins bind phosphoproteins and modulate kinase pathways, no kinase activity
   - Action: **MODIFY** → GO:0045859

**Key insight**: Adapter proteins scaffold kinase-substrate interactions and regulate
kinase activity, but the actual phosphorylation is performed by the kinases they interact
with (c-Abl, RAF, etc.), not by the adapters themselves.

## 2026-01-19 (Session 8)

**Human Priority H5: Transcription Factors - Complete**

All 5 transcription factors reviewed. ALL are misannotations where the TF is the
SUBSTRATE of phosphorylation (is phosphorylated BY kinases), not the enzyme:

1. **CREB1** (P16220) - cAMP response element-binding protein
   - Annotation: GO:0006468 "protein phosphorylation" (IDA, PMID:8798441)
   - CREB1 is a bZIP family transcription factor extensively PHOSPHORYLATED by kinases
   - UniProt: "Phosphorylated... by CaMK1/2/4, AKT, RPS6KA3/4/5, SGK1, TSSK4, HIPK2"
   - PMID:8798441: "phosphorylated CREB was present" - CREB1 is substrate
   - Action: **REMOVE**

2. **ATF2** (P15336) - Activating transcription factor 2
   - Annotation: GO:0018107 "peptidyl-threonine phosphorylation" (IDA, PMID:17267404)
   - ATF2 is a bZIP TF that is PHOSPHORYLATED at Thr-69/71 by p38 MAPK, ERK, JNK
   - ATF2 has HAT activity (EC 2.3.1.48), NOT kinase activity
   - PMID:17267404: "phosphorylation of ATF2 on Thr71" - ATF2 is substrate
   - Action: **REMOVE**

3. **ERG** (P11308) - Transcriptional regulator ERG
   - Annotation: GO:0006468 "protein phosphorylation" (TAS, PMID:8502479)
   - ERG is an ETS family transcription factor that is PHOSPHORYLATED by PKC
   - PMID:8502479: "ERG-2 is a nuclear phosphoprotein" and "phosphorylated by
     activation of protein kinase C" - ERG is substrate
   - Action: **REMOVE**

4. **RUNX3** (Q13761) - Runt-related transcription factor 3
   - Annotation: GO:0006468 "protein phosphorylation" (IDA, PMID:20100835)
   - RUNX3 is a Runt-domain TF that is PHOSPHORYLATED by Src kinase
   - Paper title: "Src kinase phosphorylates RUNX3 at tyrosine residues"
   - Action: **REMOVE**

5. **RARA** (P10276) - Retinoic acid receptor alpha
   - Annotation: GO:0006468 "protein phosphorylation" (IMP, PMID:16456540)
   - RARA is a nuclear hormone receptor (NR1 subfamily) with no kinase activity
   - PMID:16456540 describes p38MAPK phosphorylating SRC-3 coactivator, not RARA
   - UniProt: "Phosphorylated by AKT1... Phosphorylated by PKA" - RARA is substrate
   - Action: **REMOVE**

**Key insight**: Transcription factors are classic targets/substrates of
kinase-mediated phosphorylation that regulates their transcriptional activity.
None of them have kinase activity themselves. These are substrate-as-enzyme errors.

## 2026-01-18 (Session 7)

**Human Priority H4: Cytokines - Complete**

All 3 genes reviewed. All have GO:0007260 "tyrosine phosphorylation of STAT protein" which
should be MODIFY → GO:0042531 "positive regulation of tyrosine phosphorylation of STAT protein".

1. **IL15** (P40933) - Interleukin-15
   - Annotation: GO:0007260 "tyrosine phosphorylation of STAT protein" (IDA, PMID:12244150)
   - IL15 is a cytokine that binds IL15R and activates the JAK-STAT pathway
   - The JAK kinases (JAK1/JAK3) phosphorylate STAT proteins, not IL15 itself
   - IL15 already has GO:0050731 "positive regulation of peptidyl-tyrosine phosphorylation"
   - Action: **MODIFY** → GO:0042531

2. **IL21** (Q9HBE4) - Interleukin-21
   - Annotation: GO:0007260 "tyrosine phosphorylation of STAT protein" (IDA, PMID:12244150)
   - PMID:12244150: "IL-21 induced STAT3 activation" - cytokine triggers, doesn't catalyze
   - IL21 already has GO:0042531 (IDA, PMID:17673207) - correct annotation exists
   - Action: **MODIFY** → GO:0042531

3. **IFNL4** (K9M1U5) - Interferon lambda-4
   - Annotation: GO:0007260 "tyrosine phosphorylation of STAT protein" (IDA, PMID:23291588)
   - PMID:23291588: "Transient overexpression of IFNL4 in a hepatoma cell line induced STAT1
     and STAT2 phosphorylation" - interferon triggers downstream kinases
   - IFNL4 is a secreted type III interferon (cytokine) with no kinase activity
   - Action: **MODIFY** → GO:0042531

**Key insight**: GO:0007260 "tyrosine phosphorylation of STAT protein" is a BP term describing
the actual phosphorylation event. For cytokines that INDUCE this process (but don't catalyze it),
the correct term is GO:0042531 "positive regulation of tyrosine phosphorylation of STAT protein".

## 2026-01-18 (Session 6)

**Human Priority H1: Phosphatases - Complete**

Discovered and reviewed the most egregious annotation errors: PHOSPHATASES annotated to
PHOSPHORYLATION (the opposite reaction they catalyze).

1. **CDC25B** (P30305) - M-phase inducer phosphatase 2
   - Annotation: GO:0006468 "protein phosphorylation" (IDA, PMID:17332740)
   - **CRITICAL ERROR**: CDC25B is EC 3.1.3.48 (protein tyrosine phosphatase)
   - UniProt: "Directly dephosphorylates CDK1 and stimulates its kinase activity"
   - PMID:17332740: describes CDC25B as "the phosphatase required for activation of
     mitotic cyclin/Cdk1 complexes"
   - Action: **REMOVE** (phosphatase, not kinase)

2. **PPP3CB** (P16298) - Calcineurin A subunit beta
   - Annotation: GO:0006468 "protein phosphorylation" (ISS, GO_REF:0000024)
   - **CRITICAL ERROR**: PPP3CB is EC 3.1.3.16 (phosphoprotein phosphatase)
   - UniProt: "Dephosphorylates TFEB", "Dephosphorylates and activates NFATC1",
     "Dephosphorylates and inactivates ELK1", "Dephosphorylates DARPP32"
   - Already correctly annotated to GO:0006470 "protein dephosphorylation"
   - ISS transfer from mouse P48453 is erroneous
   - Action: **REMOVE** (phosphatase, not kinase)

3. **PTPN6** (P29350) - SHP-1 tyrosine phosphatase
   - Annotations: GO:0018108 "peptidyl-tyrosine phosphorylation" (IDA x2)
   - **CRITICAL ERROR**: PTPN6 is EC 3.1.3.48 (protein tyrosine phosphatase)
   - The name literally contains "phosphatase": "Tyrosine-protein phosphatase
     non-receptor type 6"
   - Already correctly annotated to GO:0035335 "peptidyl-tyrosine dephosphorylation"
   - PMID:18802077: explicitly identifies SHP-1 as a phosphatase that dephosphorylates
   - Action: **REMOVE** (2 annotations - phosphatase, not kinase)

**Key insight**: These are not subtle over-annotations - they are **opposite-polarity
annotations**. Phosphatases remove phosphate; kinases add phosphate. Annotating a
phosphatase to a phosphorylation term is like annotating a helicase to DNA synthesis.

## 2026-01-18 (Session 5)

**Priority 4: Other Interesting Cases - Complete**

All 4 genes reviewed. All are misannotations or over-annotations:

1. **App** (P12023) - Amyloid-beta precursor protein ⚠️ MISANNOTATION
   - Annotation: GO:0006468 "protein phosphorylation" (IMP, PMID:16025111)
   - **CRITICAL ERROR**: PMID:16025111 describes DEPHOSPHORYLATION, not phosphorylation!
   - The paper shows amyloid-beta promotes "Dephosphorylation of the NMDA receptor subunit
     NR2B at Tyr1472" via phosphatases PP2B and STEP
   - App is a transmembrane glycoprotein cleaved to produce amyloid-beta - no kinase activity
   - Action: **REMOVE** (wrong process - paper describes opposite)

2. **Bcl2** (P10417) - Apoptosis regulator Bcl-2 ⚠️ MISANNOTATION
   - Annotations: GO:0018105 "peptidyl-serine phosphorylation" (IDA, PMID:14660795)
                  GO:0018107 "peptidyl-threonine phosphorylation" (IDA, PMID:14660795)
   - **CRITICAL ERROR**: Paper describes Bcl2 being PHOSPHORYLATED (as substrate)
   - PMID:14660795: "phosphorylation enhances Bcl2's antiapoptotic function"
   - UniProt: "Phosphorylated by PKC, ERKs, MAPK8/JNK1 at Thr-69, Ser-70, Ser-84"
   - Bcl2 is the TARGET of phosphorylation, not the enzyme
   - Action: **REMOVE** (Bcl2 is substrate, not enzyme)

3. **Cbl** (P22682) - E3 ubiquitin-protein ligase CBL ⚠️ MISANNOTATION
   - Annotation: GO:0006468 "protein phosphorylation" (ISS, GO_REF:0000024)
   - Cbl's enzymatic activity is EC 2.3.2.27 (ubiquitin transferase)
   - UniProt: "Phosphorylated on tyrosine residues by ALK, EGFR, FGR, INSR, SYK, FYN, ZAP70"
   - Cbl is the SUBSTRATE of phosphorylation, not the enzyme
   - ISS transfer is inappropriate - Cbl has no kinase activity in any species
   - Action: **REMOVE** (ubiquitin ligase, not kinase)

4. **Cdc42** (P60766) - Cell division control protein 42 homolog
   - Annotation: GO:0006468 "protein phosphorylation" (IMP, PMID:31219639)
   - Cdc42 is a small GTPase (EC 3.6.5.2) - not a kinase
   - PMID:31219639: "Cdc42 activation by endothelin" - describes Cdc42 being activated
   - Cdc42 regulates actin cytoskeleton via GTP/GDP cycling, not phosphorylation
   - Already correctly annotated to GO:0003924 "GTPase activity"
   - Action: **MODIFY** → GO:0045859 "regulation of protein kinase activity"

**Note**: The ai-review.yaml files for these 4 genes are newly created stubs with many
pre-existing reference title mismatches that block validation. The phosphorylation
annotation edits need to be applied after fixing the reference titles.

## 2026-01-18 (Session 4)

**Priority 2: Signaling Ligands - Complete**

All 5 genes reviewed. 4 are over-annotations (MODIFY), 1 is a misannotation (REMOVE):

1. **Egf** (P01132) - Epidermal growth factor
   - Annotation: GO:0018108 "peptidyl-tyrosine phosphorylation" (IDA, PMID:9687508)
   - EGF is a secreted ligand that binds EGFR (the kinase). EGFR performs tyrosine phosphorylation
   - UniProt: "EGF stimulates the growth of various epidermal and epithelial tissues"
   - Action: **MODIFY** → GO:0045859

2. **Epo** (P07321) - Erythropoietin
   - Annotation: GO:0018105 "peptidyl-serine phosphorylation" (IDA, PMID:9171102)
   - EPO is a secreted hormone that binds EPOR, activating JAK2, which then activates JNK1
   - JNK1 (MAPK8) performs the serine phosphorylation - not EPO
   - Action: **MODIFY** → GO:0045859

3. **Edn1** (P22387) - Endothelin-1
   - Annotation: GO:0006468 "protein phosphorylation" (IDA, PMID:18940799)
   - Edn1 is a secreted peptide that binds Ednra/Ednrb receptors
   - The receptors activate downstream kinases - Edn1 doesn't phosphorylate
   - Action: **MODIFY** → GO:0045859

4. **Gas6** (Q61592) - Growth arrest-specific 6
   - Annotations: GO:0006468 "protein phosphorylation" (ISS, ISO)
   - Gas6 is a "Ligand for tyrosine-protein kinase receptors AXL, TYRO3 and MER" (UniProt)
   - The receptor kinases perform phosphorylation upon Gas6 binding
   - Already correctly annotated to GO:0045860 "positive regulation of protein kinase activity"
   - Action: **MODIFY** → GO:0045859

5. **Ang2** (Q64438) - Angiogenin-2 ⚠️ MISANNOTATION
   - Annotations: GO:0006468 "protein phosphorylation" (IDA PMID:28096417, IMP PMID:25313067)
   - **CRITICAL ERROR**: Both PMIDs are about **Angiotensin II** (AngII), NOT Angiogenin-2!
     - PMID:25313067: "Angiotensin II signaling via protein kinase C phosphorylates Kelch-like 3"
     - PMID:28096417: "Phosphorylation by PKC and PKA regulate...WNK4"
   - These papers describe how the hormone Angiotensin II activates PKC/PKA
   - Ang2 (Angiogenin-2) is a RIBONUCLEASE (EC 3.1.27.-) with no involvement in angiotensin signaling
   - Gene symbol confusion: Ang2 vs AngII
   - Action: **REMOVE** (wrong gene entirely)

## 2026-01-18 (Session 3)

**Priority 1: Cyclins and CDK Regulators - Complete**

All 4 genes reviewed. All are over-annotations:

1. **Ccnb1** (P24860) - G2/mitotic-specific cyclin-B1
   - Annotation: GO:0006468 "protein phosphorylation" (IDA, PMID:12124778)
   - Forms Cyclin B1-CDK1 complex (MPF). CDK1 is the kinase, cyclin provides specificity
   - Already correctly annotated to GO:0061575 "cyclin-dependent protein serine/threonine kinase activator activity"
   - Action: **MODIFY** → GO:0045859

2. **Ccne1** (Q61457) - G1/S-specific cyclin-E1
   - Annotations: GO:0006468 "protein phosphorylation" (ISS, IDA)
   - Forms Cyclin E1-CDK2 complex. CDK2 is the kinase
   - Already correctly annotated to GO:0016538 "cyclin-dependent protein serine/threonine kinase regulator activity"
   - Action: **MODIFY** → GO:0045859

3. **Ccnt1** (Q9QWV9) - Cyclin-T1
   - Annotation: GO:0006468 "protein phosphorylation" (ISO, PMID:16109376)
   - Forms P-TEFb complex (Cyclin T1-CDK9). CDK9 is the kinase
   - UniProt: "Required to activate the protein kinase activity of CDK9"
   - Already correctly annotated to GO:0061575 (ISS)
   - Action: **MODIFY** → GO:0045859

4. **Cdk5r1** (P61809) - CDK5 activator 1 (p35)
   - Annotation: GO:0018105 "peptidyl-serine phosphorylation" (ISO)
   - Forms p35-CDK5 complex. CDK5 is the kinase
   - UniProt: "Only the heterodimer shows kinase activity"
   - Already correctly annotated to GO:0061575 (IMP)
   - Action: **MODIFY** → GO:0045859

## 2026-01-18 (Session 2)

**Query Methodology Correction**

Initial query was flawed - it included regulatory terms like GO:0042976 "activation of Janus kinase activity"
that GO has placed under the phosphorylation hierarchy. These are NOT problematic annotations for receptors.

**The fix**: Exclude terms with "activation" or "regulation" in the label:
```sql
AND t.label NOT LIKE '%activation%'
AND t.label NOT LIKE '%regulation%'
```

This reduced the target set from 174 to **166 genes**.

**Priority 3: Receptors Review (Corrected)**

After refining the query, only 2 receptors remain as targets:

1. **Drd1** (Q61616) - Dopamine D1 receptor
   - Annotation: GO:0006468 "protein phosphorylation" (IDA, PMID:18496528)
   - PMID:18496528 shows D1R triggers a cascade (D1R → cAMP → PP2A → DARPP-32 → PP1 inhibition → H3 phosphorylation)
   - The receptor does NOT perform phosphorylation - it regulates kinase/phosphatase activity
   - Action: **MODIFY** → GO:0045859 "regulation of protein kinase activity"

2. **Ednra** (Q61614) - Endothelin receptor type A
   - Annotation: GO:0006468 "protein phosphorylation" (IMP, PMID:31219639)
   - PMID:31219639 shows Ednra activates Cdc42 in a signaling cascade
   - The receptor does NOT perform phosphorylation directly
   - Action: **MODIFY** → GO:0045859 "regulation of protein kinase activity"

**Removed from target list (false positives)**:
- Agtr1a, Ghr - Only annotated to GO:0042976 "activation of Janus kinase activity" which is
  a regulatory term, appropriate for receptors that activate JAKs

## 2026-01-18 (Session 1)

**Project Initialization**

Created project to review phosphorylation annotations on non-kinase genes. Used DuckDB query on MGI database to identify 174 mouse genes annotated to phosphorylation (or descendants) that are NOT annotated to protein kinase activity.

Key findings from initial analysis:
- 87 genes annotated to "protein phosphorylation" (GO:0006468) - most likely to need review
- Many are cyclins, signaling ligands, and receptors - these likely need modification to regulatory terms
- Some are legitimate non-protein kinases (sugar kinases, lipid kinases) - these are likely correct
- Evidence types include IDA (70), IMP (53), and ISO (90) - mix of experimental and orthology

Query used:
```sql
duckdb -readonly ~/repos/go-db/db/mgi.ddb "
WITH phospho_genes AS (
    SELECT DISTINCT a.db_object_id, a.db_object_symbol, a.ontology_class_ref
    FROM gaf_association a
    INNER JOIN isa_partof_closure ipc ON a.ontology_class_ref = ipc.subject
    WHERE ipc.object = 'GO:0016310'
),
kinase_genes AS (
    SELECT DISTINCT a.db_object_id
    FROM gaf_association a
    INNER JOIN isa_partof_closure ipc ON a.ontology_class_ref = ipc.subject
    WHERE ipc.object = 'GO:0004672'
)
SELECT p.* FROM phospho_genes p
WHERE p.db_object_id NOT IN (SELECT db_object_id FROM kinase_genes);
"
```

---

# FLY (DROSOPHILA) PHOSPHORYLATION ANALYSIS

## Overview

Extended the phosphorylation annotation analysis to Drosophila melanogaster using FlyBase database
(`fb.ddb`). The fly genome shows **significantly fewer problematic annotations** compared to mouse
and human - most non-kinase phosphorylation annotations are for legitimate non-protein kinases
(sugar kinases, lipid kinases).

## Summary Statistics (Fly - FlyBase database)

- **Total annotations in database**: 186,975
- **Non-kinase genes with phosphorylation annotations**: ~50 (after excluding regulatory terms)
- **Breakdown by term type**:
  - carbohydrate phosphorylation (GO:0046835): ~25 genes (legitimate sugar kinases)
  - lipid phosphorylation (GO:0046834): ~5 genes (legitimate lipid kinases)
  - protein phosphorylation (GO:0006468): **6 genes** (potential issues)

**Key finding**: Fly has far fewer problematic annotations. Most non-protein kinase annotations
are for legitimate metabolic kinases (ribokinase, hexokinase, etc.).

## Fly Candidates for Review

### Legitimate Annotations (No Action Needed)

| Gene | GO Term | EC Number | Substrate | Status |
|------|---------|-----------|-----------|--------|
| Mulk | lipid phosphorylation | EC 2.7.1.- | Ceramide, DAG | ✓ CORRECT |
| rdgA | lipid phosphorylation | EC 2.7.1.107 | Diacylglycerol | ✓ CORRECT |

**Mulk** (Multi-substrate lipid kinase / CG31873)
- Ceramide kinase that phosphorylates ceramide to form ceramide-1-phosphate
- Also has diacylglycerol kinase activity
- Involved in primordial germ cell migration and WntD signaling
- Reference: Waggoner et al. (2004) J Biol Chem 279:38228-38235
- Status: **CORRECT** - legitimate lipid kinase

**rdgA** (retinal degeneration A)
- Diacylglycerol kinase (EC 2.7.1.107)
- Phosphorylates diacylglycerol to form phosphatidic acid
- Critical for photoreceptor function and phototransduction
- Status: **CORRECT** - legitimate lipid kinase

### Potential Issues

| Gene | GO Term | Issue | Code | Recommended Action |
|------|---------|-------|------|-------------------|
| Argk1 | phosphorylation | Phosphagen kinase (non-protein) | W | INVESTIGATE |
| Dref | protein phosphorylation + autophosphorylation | Transcription factor | R/S | REVIEW |
| CG9886 | protein phosphorylation | Glycerate kinase (sugar) | W-sugar | **REMOVE** |

**Argk1** (Arginine kinase 1)
- Phosphagen kinase (EC 2.7.3.3) that phosphorylates arginine
- Phosphagen kinases are involved in energy buffering (like creatine kinase in vertebrates)
- Catalyzes: L-arginine + ATP ⇌ Nω-phospho-L-arginine + ADP
- **NOT** a protein kinase - phosphorylates free arginine for energy storage
- Status: **BORDERLINE** - technically phosphorylates an amino acid, but the free amino acid,
  not peptidyl-arginine residues. May warrant review but distinct from "protein phosphorylation".

**Dref** (DNA replication-related element factor)
- Annotated to both GO:0006468 and GO:0046777 (autophosphorylation)
- Dref is a **transcription factor** that regulates cell proliferation genes
- Literature shows Dref REGULATES kinase pathways (JNK, Hippo/Warts, EGFR/MAPK)
- No evidence of intrinsic kinase activity - likely an [R] or [S] type error
- Status: **NEEDS REVIEW** - transcription factors are typically substrates, not kinases

**CG9886** (Glycerate kinase)
- Annotated to GO:0006468 "protein phosphorylation"
- CG9886 is glycerate kinase (EC 2.7.1.31) - phosphorylates D-glycerate
- Reaction: (R)-glycerate + ATP = (2R)-3-phosphoglycerate + ADP
- **CLEAR MISANNOTATION**: This is a sugar/metabolic kinase, NOT a protein kinase
- Already has correct annotation GO:0008887 "glycerate kinase activity"
- Status: **REMOVE** [W-sugar] - wrong substrate type

## Cross-Species Comparison: Fly vs Mouse/Human

| Pattern | Mouse | Human | Fly | Notes |
|---------|-------|-------|-----|-------|
| Cyclins misannotated | Ccnb1, Ccne1, Ccnt1, Cdk5r1 | CCNE1 | None found | Fly annotation more conservative |
| Phosphatases misannotated | - | CDC25B, PPP3CB, PTPN6 | None found | No opposite-reaction errors in fly |
| Sugar kinases misannotated | - | GLYCTK | CG9886 | Same pattern across species |
| Transcription factors | - | CREB1, ATF2, ERG, RUNX3, RARA | Dref? | Needs verification |
| Signaling ligands | Egf, Epo, Edn1, Gas6, Ang2 | GAS6, PDGFA/B, IL15/21 | None found | Fly ligands not over-annotated |

**Key observation**: FlyBase annotations are more conservative than MGI/GOA. The problematic
patterns seen in mouse/human (cyclins, signaling ligands, phosphatases) are largely absent
in fly. Only 1 clear error found (CG9886), with 2 cases needing further investigation
(Argk1, Dref).

## STATUS (Fly)

- [x] Query analysis completed
- [x] Mulk - **CORRECT** (lipid kinase)
- [x] rdgA - **CORRECT** (lipid kinase)
- [ ] Argk1 - **INVESTIGATE** (phosphagen kinase - borderline case)
- [ ] Dref - **INVESTIGATE** (transcription factor with suspicious annotations)
- [x] CG9886 - **REMOVE** [W-sugar] (glycerate kinase, not protein kinase)

**Last updated**: 2026-01-19

---

## 2026-01-19 (Session 9 continued - Fly Analysis)

Extended analysis to Drosophila melanogaster using FlyBase database (fb.ddb).

**Key finding**: Fly has **far fewer problematic annotations** than mouse or human. The SQL query
that found ~130-160 targets in mammalian databases found only ~50 in fly, with most being
legitimate non-protein kinases (sugar kinases, lipid kinases).

**Candidates analyzed**:

1. **Mulk** (Multi-substrate lipid kinase) - **CORRECT**
   - Ceramide kinase (EC 2.7.1.x) that also has diacylglycerol kinase activity
   - Legitimately phosphorylates lipids (ceramide, DAG), not proteins
   - Involved in PGC migration and WntD signaling

2. **rdgA** (retinal degeneration A) - **CORRECT**
   - Diacylglycerol kinase (EC 2.7.1.107)
   - Legitimately phosphorylates DAG to form phosphatidic acid
   - Essential for phototransduction

3. **Argk1** (Arginine kinase 1) - **INVESTIGATE**
   - Phosphagen kinase (EC 2.7.3.3)
   - Phosphorylates L-arginine (free amino acid) for energy storage
   - NOT a protein kinase - doesn't phosphorylate peptidyl residues
   - Borderline case - phosphorylates amino acid, but not in protein context

4. **Dref** (DNA replication-related element factor) - **INVESTIGATE**
   - Transcription factor annotated to GO:0006468 + GO:0046777 (autophosphorylation)
   - Literature shows Dref REGULATES kinase pathways (JNK, Hippo, EGFR/MAPK)
   - Transcription factors are typically SUBSTRATES, not kinases
   - Likely [R] or [S] type error - needs detailed review

5. **CG9886** - **REMOVE** [W-sugar]
   - Annotated to GO:0006468 "protein phosphorylation"
   - Actually a glycerate kinase (EC 2.7.1.31) - phosphorylates D-glycerate (sugar)
   - Clear wrong substrate type error
   - FlyBase correctly shows "enables glycerate kinase activity"

**Conclusion**: Fly annotation quality for phosphorylation terms is notably higher than
mammalian MODs. Only 1 clear error (CG9886) and 2 borderline cases requiring expert review.

---

# YEAST (SGD) PHOSPHORYLATION ANALYSIS

## Overview

Extended the phosphorylation annotation analysis to Saccharomyces cerevisiae using the SGD database
(`sgd.ddb`). The yeast genome shows **exemplary annotation quality** - ZERO problematic annotations
were found. All genes annotated to protein phosphorylation terms have appropriate protein kinase
activity annotations.

## Summary Statistics (Yeast - SGD database)

- **Total annotations in database**: 153,185
- **Non-kinase genes with phosphorylation annotations**: **0** (none!)
- **Breakdown by term type**:
  - carbohydrate phosphorylation: 15 genes (legitimate sugar kinases)
  - protein phosphorylation: 3 genes (**all are kinases**)
  - peptidyl-serine/threonine phosphorylation: 1 gene (IPL1, **is a kinase**)
  - protein autophosphorylation: 1 gene (GCN2, **is a kinase**)

## Yeast Protein Kinase Annotations (All Correct)

All genes with protein phosphorylation BP annotations have appropriate kinase MF annotations:

| Gene | Phosphorylation Annotation | Kinase Activity Annotations | Status |
|------|---------------------------|----------------------------|--------|
| IPL1 | peptidyl-Ser/Thr phosphorylation | protein kinase activity, Ser/Thr kinase | ✓ CORRECT |
| GCN2 | protein phosphorylation, autophosphorylation | eIF2α kinase, Ser/Thr kinase | ✓ CORRECT |
| COQ8 | protein phosphorylation | protein kinase activity | ✓ CORRECT |
| PBS2 | protein phosphorylation | MAP kinase kinase activity | ✓ CORRECT |

**IPL1** - Aurora kinase B homolog (EC 2.7.11.1)
- Chromosomal passenger complex kinase
- Correctly annotated to both process (peptidyl-serine/threonine phosphorylation) and function (kinase activity)

**GCN2** - General control nonderepressible 2 (EC 2.7.11.1)
- eIF2α kinase activated by amino acid starvation
- Correctly annotated to protein phosphorylation AND has kinase activity

**COQ8** - Coenzyme Q biosynthesis kinase (atypical kinase)
- UbiB family kinase involved in CoQ biosynthesis
- Correctly annotated with kinase activity

**PBS2** - MAP kinase kinase (EC 2.7.12.2)
- Dual-specificity MAPKK in HOG pathway
- Correctly has MAP kinase kinase activity annotation

## Yeast Cyclin Annotations (Correct Pattern)

Unlike mammals, yeast cyclins are correctly annotated:

| Cyclin | Annotation | Status |
|--------|-----------|--------|
| CLB1-6 | cyclin-dependent protein serine/threonine kinase regulator activity | ✓ CORRECT |
| CLN1-3 | cyclin-dependent protein serine/threonine kinase regulator activity | ✓ CORRECT |
| PCL1-9 | cyclin-dependent protein serine/threonine kinase regulator activity | ✓ CORRECT |

Yeast cyclins are annotated to the **regulatory function** (GO:0016538), NOT to the phosphorylation
process. This is the correct annotation pattern that was missing in mammals.

## Cross-Species Comparison: All MODs

| Pattern | Mouse | Human | Fly | Yeast |
|---------|-------|-------|-----|-------|
| Total problematic annotations | ~20 | ~45 | ~3 | **0** |
| Cyclins misannotated | 4 genes | 1 gene | 0 | **0** |
| Phosphatases misannotated | 0 | 3 genes | 0 | **0** |
| Signaling ligands misannotated | 5 genes | 7+ genes | 0 | **0** |
| Sugar kinases misannotated | 0 | 1 gene | 1 gene | **0** |
| Transcription factors | 0 | 5 genes | 1? | **0** |
| Adapter proteins | 0 | 3 genes | 0 | **0** |

**Key observation**: SGD has the highest annotation quality among the MODs surveyed. This may reflect:
1. Smaller genome with more intensive curation per gene
2. Longer history of GO annotation refinement
3. Stricter curator guidelines for distinguishing process vs function annotations

## STATUS (Yeast)

- [x] Query analysis completed - **ZERO problematic annotations found**
- [x] All 4 genes with protein phosphorylation terms verified as kinases
- [x] Yeast cyclins confirmed to have correct regulatory annotations
- [x] No further curation actions needed

**Last updated**: 2026-01-19

---

## 2026-01-19 (Session 9 continued - Yeast Analysis)

Extended analysis to Saccharomyces cerevisiae using SGD database (sgd.ddb).

**Key finding**: Yeast has **ZERO problematic phosphorylation annotations**. Every gene annotated
to protein phosphorylation or peptidyl phosphorylation terms (IPL1, GCN2, COQ8, PBS2) is a
legitimate kinase with appropriate kinase activity annotations.

**Annotation quality highlights**:

1. **Cyclins annotated correctly**: Unlike mammals, yeast cyclins (CLB1-6, CLN1-3, PCL1-9) are
   annotated to "cyclin-dependent protein serine/threonine kinase regulator activity" (GO:0016538),
   NOT to "protein phosphorylation". This is the correct pattern.

2. **No substrate-as-enzyme errors**: None of the mammalian error patterns (signaling ligands,
   transcription factors, adapter proteins annotated to phosphorylation) were found in yeast.

3. **No opposite-reaction errors**: No phosphatases annotated to phosphorylation.

**Conclusion**: SGD serves as a gold standard for phosphorylation annotation quality. The patterns
of over-annotation seen in MGI and GOA are absent in SGD, suggesting different curation standards
or more thorough quality control.

---

# S. POMBE (POMBASE) PHOSPHORYLATION ANALYSIS

## Overview

Extended the phosphorylation annotation analysis to Schizosaccharomyces pombe using the PomBase
database (`pombase.ddb`). Like S. cerevisiae, S. pombe shows **exemplary annotation quality** -
ZERO problematic annotations were found.

## Summary Statistics (S. pombe - PomBase database)

- **Total annotations in database**: 90,710
- **Non-kinase genes with phosphorylation annotations**: **0** (none!)
- **Breakdown by term type**:
  - carbohydrate phosphorylation: 9 genes (legitimate sugar kinases)
  - protein phosphorylation: 1 gene (gsk3, **is a kinase**)
  - peptidyl-serine phosphorylation: 1 gene (dsk1, **is a kinase**)

## S. pombe Protein Kinase Annotations (All Correct)

All genes with protein phosphorylation BP annotations have appropriate kinase MF annotations:

| Gene | Phosphorylation Annotation | Kinase Activity Annotations | Status |
|------|---------------------------|----------------------------|--------|
| dsk1 | peptidyl-serine phosphorylation | protein Ser/Thr kinase activity | ✓ CORRECT |
| gsk3 | protein phosphorylation | protein Ser/Thr/Tyr kinase activity | ✓ CORRECT |

**dsk1** - Dual-specificity kinase related
- DYRK family kinase
- Correctly annotated to both process and function

**gsk3** - Glycogen synthase kinase 3 homolog
- GSK-3 family kinase, central metabolic regulator
- Correctly has protein kinase activity (including tyrosine kinase)

## S. pombe Cyclin Annotations (Correct Pattern)

Like S. cerevisiae, S. pombe cyclins are correctly annotated:

| Cyclin/Regulator | Annotation | Status |
|------------------|-----------|--------|
| cdc13 (B-cyclin) | cyclin-dependent protein serine/threonine kinase activator activity | ✓ CORRECT |
| cig1, cig2 | cyclin-dependent protein serine/threonine kinase activator activity | ✓ CORRECT |
| puc1 | cyclin-dependent protein serine/threonine kinase regulator activity | ✓ CORRECT |
| mcs2 | cyclin-dependent protein serine/threonine kinase activator activity | ✓ CORRECT |
| suc1 | cyclin-dependent protein serine/threonine kinase activator activity | ✓ CORRECT |

**cdc2** (the CDK) is correctly annotated to "cyclin-dependent protein serine/threonine kinase activity".

S. pombe cyclins are annotated to **regulatory/activator functions**, NOT to the phosphorylation
process itself. This is the correct annotation pattern.

## Cross-Species Comparison: Final Summary

| Pattern | Mouse | Human | Fly | S. cerevisiae | S. pombe |
|---------|-------|-------|-----|---------------|----------|
| **Total problematic** | ~20 | ~45 | ~3 | **0** | **0** |
| Cyclins misannotated | 4 | 1 | 0 | **0** | **0** |
| Phosphatases | 0 | 3 | 0 | **0** | **0** |
| Signaling ligands | 5 | 7+ | 0 | **0** | **0** |
| Sugar kinases | 0 | 1 | 1 | **0** | **0** |
| TFs as substrates | 0 | 5 | 1? | **0** | **0** |
| Adapter proteins | 0 | 3 | 0 | **0** | **0** |

**Key observation**: Both yeast MODs (SGD, PomBase) have perfect phosphorylation annotation quality.
This suggests:
1. Fungal MODs may have more rigorous curation standards
2. Smaller genomes allow more thorough annotation review
3. Longer-established annotation practices with strict guidelines

## STATUS (S. pombe)

- [x] Query analysis completed - **ZERO problematic annotations found**
- [x] All genes with protein phosphorylation terms verified as kinases (dsk1, gsk3)
- [x] S. pombe cyclins confirmed to have correct regulatory annotations
- [x] No further curation actions needed

**Last updated**: 2026-01-19

---

## 2026-01-19 (Session 9 continued - S. pombe Analysis)

Extended analysis to Schizosaccharomyces pombe using PomBase database.

**Key finding**: S. pombe has **ZERO problematic phosphorylation annotations**, matching S. cerevisiae.
Both yeast species have exemplary annotation quality.

**Verified genes**:
- **dsk1** - DYRK family kinase, correctly has kinase activity
- **gsk3** - GSK-3 homolog, correctly has Ser/Thr/Tyr kinase activity

**Cyclin annotations verified**: All S. pombe cyclins (cdc13, cig1, cig2, puc1, mcs2, suc1) are
annotated to regulator/activator functions, NOT to phosphorylation processes.

**Annotation quality gradient (final)**:
- **EXCELLENT**: SGD, PomBase (0 errors)
- **GOOD**: FlyBase (1 clear error, 2 borderline)
- **NEEDS REVIEW**: MGI (~20 errors), GOA (~45 errors)

---

# ZEBRAFISH (ZFIN) PHOSPHORYLATION ANALYSIS

## Overview

Extended the phosphorylation annotation analysis to Danio rerio using the ZFIN database
(`zfin.ddb`). Zebrafish shows **very good annotation quality** - only 1 problematic annotation
was found (glyctk - a sugar kinase), which is the same pattern seen in human and fly.

## Summary Statistics (Zebrafish - ZFIN database)

- **Total annotations in database**: 250,491
- **Non-kinase genes with protein phosphorylation annotations**: **1** (glyctk only)
- **Protein phosphorylation annotations**: 14 genes total
  - 13 are verified kinases ✓
  - 1 is misannotated (glyctk)

## Verified Kinases with Protein Phosphorylation Annotations

All 13 genes with protein phosphorylation annotations (excluding glyctk) have kinase activity:

| Gene | Kinase Type | Status |
|------|-------------|--------|
| acvr1l | Receptor kinase | ✓ CORRECT |
| camk2a | CaM kinase II | ✓ CORRECT |
| cdkl1 | CDK-like kinase | ✓ CORRECT |
| chek1 | Checkpoint kinase | ✓ CORRECT |
| coq8aa | Atypical kinase | ✓ CORRECT |
| coq8b | Atypical kinase | ✓ CORRECT |
| csnk1a1 | Casein kinase I | ✓ CORRECT |
| dclk2a | DCK-like kinase | ✓ CORRECT |
| ilk | Integrin-linked kinase | ✓ CORRECT |
| jak1 | Janus kinase | ✓ CORRECT |
| pim2 | PIM kinase | ✓ CORRECT |
| sik3 | Salt-inducible kinase | ✓ CORRECT |
| snrkb | SNF-related kinase | ✓ CORRECT |

## Single Misannotation

| Gene | GO Term | Issue | Code | Action |
|------|---------|-------|------|--------|
| **glyctk** | protein phosphorylation | Glycerate kinase (EC 2.7.1.31) | W-sugar | **REMOVE** |

**glyctk** - Glycerate kinase
- Same error as human GLYCTK and fly CG9886
- Glycerate kinase phosphorylates D-glycerate (a sugar), NOT proteins
- This is a cross-species systematic error from ISS transfer (GO_REF:0000024)

## Zebrafish Cyclin Annotations (Correct Pattern)

All zebrafish cyclins are correctly annotated:

| Cyclin | Annotation | Status |
|--------|-----------|--------|
| ccna1, ccna2 | cyclin-dependent protein serine/threonine kinase regulator activity | ✓ CORRECT |
| ccnb1, ccnb2, ccnb3 | cyclin-dependent protein serine/threonine kinase regulator activity | ✓ CORRECT |
| ccnc | cyclin-dependent protein serine/threonine kinase regulator activity | ✓ CORRECT |
| ccnd1, ccnd2a/b, ccnd3 | cyclin-dependent protein serine/threonine kinase regulator activity | ✓ CORRECT |
| ccne1, ccne2 | cyclin-dependent protein serine/threonine kinase regulator activity | ✓ CORRECT |

**No zebrafish cyclins are annotated to "protein phosphorylation"** - they all have the correct
regulatory activity annotation.

## Signaling Ligands (Correct - No Over-annotations)

Zebrafish signaling ligands (egfa, egfb, epo, gas6, pdgfa/b) are NOT annotated to phosphorylation
process terms - avoiding the over-annotation pattern seen in mouse and human.

## Cross-Species Comparison: Updated Final Summary

| Pattern | Mouse | Human | Fly | Zebrafish | S. cerevisiae | S. pombe |
|---------|-------|-------|-----|-----------|---------------|----------|
| **Total problematic** | ~20 | ~45 | ~3 | **1** | **0** | **0** |
| Cyclins misannotated | 4 | 1 | 0 | **0** | **0** | **0** |
| Phosphatases | 0 | 3 | 0 | **0** | **0** | **0** |
| Signaling ligands | 5 | 7+ | 0 | **0** | **0** | **0** |
| Sugar kinases | 0 | 1 | 1 | **1** | **0** | **0** |
| TFs as substrates | 0 | 5 | 1? | **0** | **0** | **0** |
| Adapter proteins | 0 | 3 | 0 | **0** | **0** | **0** |

**Key observation**: ZFIN annotation quality is very good, comparable to FlyBase. Only the
glyctk sugar kinase error (propagated by ISS transfer) was found.

## STATUS (Zebrafish)

- [x] Query analysis completed - **1 problematic annotation found**
- [x] glyctk verified as sugar kinase (EC 2.7.1.31) - **REMOVE** [W-sugar]
- [x] 13 other protein phosphorylation genes verified as kinases
- [x] Zebrafish cyclins confirmed to have correct regulatory annotations
- [x] No signaling ligand over-annotations found

**Last updated**: 2026-01-19

---

## 2026-01-19 (Session 9 continued - Zebrafish Analysis)

Extended analysis to Danio rerio using ZFIN database.

**Key finding**: ZFIN has **1 problematic phosphorylation annotation** - glyctk (glycerate kinase).
This is the same pattern seen in human (GLYCTK) and fly (CG9886), likely propagated by ISS transfer.

**Annotation quality highlights**:

1. **Cyclins annotated correctly**: All zebrafish cyclins (ccna, ccnb, ccnc, ccnd, ccne series)
   are annotated to "kinase regulator activity", NOT to "protein phosphorylation"

2. **Signaling ligands NOT over-annotated**: Unlike mammals, zebrafish EGF, EPO, GAS6, PDGF
   homologs are not annotated to phosphorylation process terms

3. **Most protein kinases verified**: Of 14 genes with protein phosphorylation annotations,
   13 are verified kinases with appropriate kinase activity annotations

**Annotation quality gradient (updated)**:
- **EXCELLENT**: SGD, PomBase (0 errors)
- **VERY GOOD**: ZFIN (1 error - glyctk only)
- **GOOD**: FlyBase (1 clear error, 2 borderline)
- **NEEDS REVIEW**: MGI (~20 errors), GOA (~45 errors)

---

# C. ELEGANS (WORMBASE) PHOSPHORYLATION ANALYSIS

## Overview

Extended the phosphorylation annotation analysis to Caenorhabditis elegans using the WormBase
database (`wb.ddb`). C. elegans shows **exemplary annotation quality** - ZERO problematic
annotations were found. All genes annotated to protein/peptidyl phosphorylation terms are
verified protein kinases.

## Summary Statistics (C. elegans - WormBase database)

- **Total annotations in database**: 138,500
- **Non-kinase genes with protein phosphorylation annotations**: **0** (none!)
- **Protein phosphorylation annotations**: 7 genes - all verified kinases ✓
- **Peptidyl-serine/tyrosine phosphorylation**: 8 annotations - all verified kinases ✓

## Verified Kinases with Protein Phosphorylation Annotations

All genes with protein phosphorylation BP annotations have appropriate kinase MF annotations:

| Gene | Kinase Type | Status |
|------|-------------|--------|
| cdk-8 | Cyclin-dependent kinase | ✓ CORRECT |
| famk-1 | FAM20C-like kinase | ✓ CORRECT |
| grk-2 | G protein-coupled receptor kinase | ✓ CORRECT |
| ikke-1 | IKK epsilon kinase | ✓ CORRECT |
| pkc-1 | Protein kinase C | ✓ CORRECT |
| spk-1 | Sphingosine kinase | ✓ CORRECT |
| svh-2 | Receptor tyrosine kinase | ✓ CORRECT |

## Peptidyl Phosphorylation Annotations (All Correct)

| Gene | GO Term | Kinase Type | Status |
|------|---------|-------------|--------|
| cst-1 | peptidyl-serine phosphorylation | Hippo kinase MST1/2 homolog | ✓ CORRECT |
| kin-3 | peptidyl-serine phosphorylation | Casein kinase I | ✓ CORRECT |
| pmk-1 | peptidyl-serine phosphorylation | p38 MAPK | ✓ CORRECT |
| tpa-1 | peptidyl-serine phosphorylation | Protein kinase C theta | ✓ CORRECT |
| ddr-2 | peptidyl-tyrosine phosphorylation | Discoidin domain receptor | ✓ CORRECT |
| mbk-2 | peptidyl-tyrosine phosphorylation | DYRK family kinase | ✓ CORRECT |
| svh-2 | peptidyl-tyrosine phosphorylation | Receptor tyrosine kinase | ✓ CORRECT |

## C. elegans Cyclin Annotations (Correct Pattern)

All C. elegans cyclins are correctly annotated:

| Cyclin | Annotation | Status |
|--------|-----------|--------|
| cya-1, cya-2 (Cyclin A) | cyclin-dependent protein serine/threonine kinase regulator activity | ✓ CORRECT |
| cyb-1, cyb-2.1, cyb-2.2, cyb-3 (Cyclin B) | cyclin-dependent protein serine/threonine kinase regulator activity | ✓ CORRECT |
| cyd-1 (Cyclin D) | cyclin-dependent protein serine/threonine kinase regulator activity | ✓ CORRECT |
| cye-1 (Cyclin E) | cyclin-dependent protein serine/threonine kinase regulator activity | ✓ CORRECT |

CDKs (cdk-1, cdk-8, cdk-9, cdk-11.1, cdk-11.2, cdk-12) are correctly annotated to
"cyclin-dependent protein serine/threonine kinase activity".

**No C. elegans cyclins are annotated to "protein phosphorylation"** - they all have the correct
regulatory activity annotation.

## Cross-Species Comparison: Final Summary (All 7 MODs)

| Pattern | Mouse | Human | Fly | Zebrafish | Worm | S. cerevisiae | S. pombe |
|---------|-------|-------|-----|-----------|------|---------------|----------|
| **Total problematic** | ~20 | ~45 | ~3 | 1 | **0** | **0** | **0** |
| Cyclins misannotated | 4 | 1 | 0 | 0 | **0** | **0** | **0** |
| Phosphatases | 0 | 3 | 0 | 0 | **0** | **0** | **0** |
| Signaling ligands | 5 | 7+ | 0 | 0 | **0** | **0** | **0** |
| Sugar kinases | 0 | 1 | 1 | 1 | **0** | **0** | **0** |
| TFs as substrates | 0 | 5 | 1? | 0 | **0** | **0** | **0** |
| Adapter proteins | 0 | 3 | 0 | 0 | **0** | **0** | **0** |

**Key observation**: WormBase joins SGD and PomBase with perfect phosphorylation annotation
quality. Three model organism databases now demonstrate zero errors: S. cerevisiae, S. pombe,
and C. elegans.

## STATUS (C. elegans)

- [x] Query analysis completed - **ZERO problematic annotations found**
- [x] All 7 genes with protein phosphorylation verified as kinases
- [x] All 8 peptidyl phosphorylation annotations verified as kinases
- [x] C. elegans cyclins confirmed to have correct regulatory annotations
- [x] No further curation actions needed

**Last updated**: 2026-01-19

---

## 2026-01-19 (Session 9 continued - C. elegans Analysis)

Extended analysis to Caenorhabditis elegans using WormBase database.

**Key finding**: WormBase has **ZERO problematic phosphorylation annotations**, joining SGD
and PomBase as MODs with perfect annotation quality for this term set.

**Verified kinases**:
- Protein phosphorylation: cdk-8, famk-1, grk-2, ikke-1, pkc-1, spk-1, svh-2 (all kinases)
- Peptidyl-serine: cst-1, kin-3, pmk-1, tpa-1 (all kinases)
- Peptidyl-tyrosine: ddr-2, mbk-2, svh-2 (all kinases)

**Cyclin annotations verified**: All C. elegans cyclins (cya, cyb, cyd, cye series) are
annotated to regulator/activator functions, NOT to phosphorylation processes.

**Annotation quality gradient (final - 7 MODs)**:
- **EXCELLENT**: SGD, PomBase, WormBase (0 errors)
- **VERY GOOD**: ZFIN (1 error)
- **GOOD**: FlyBase (~3 errors)
- **NEEDS REVIEW**: MGI (~20 errors), GOA (~45 errors)

---

# ARABIDOPSIS (TAIR) PHOSPHORYLATION ANALYSIS

## Overview

Extended the phosphorylation annotation analysis to Arabidopsis thaliana using the TAIR database
(`tair.ddb`). Arabidopsis shows **moderate annotation issues** - approximately 42 genes without
protein kinase activity annotations have protein/peptidyl phosphorylation annotations. Several
clear misannotation patterns were identified, including phosphatases annotated to phosphorylation.

## Summary Statistics (Arabidopsis - TAIR database)

- **Total annotations in database**: 227,211
- **Non-kinase genes with protein phosphorylation annotations**: 42 (using symbol matching)
- **Breakdown by evidence type**:
  - IEA (computational): 29 genes
  - IDA (direct assay): 14 genes
  - IMP: 2 genes
  - ISS/IPI: 2 genes

## Confirmed Misannotations (Experimentally Supported)

### Phosphatases Annotated to Phosphorylation [O]

| Gene | GO Term | Issue | Code | Action |
|------|---------|-------|------|--------|
| **TOPP4** | protein phosphorylation | Type 1 Protein Phosphatase (EC 3.1.3.16) | O-ser | **REMOVE** |
| **CDC25** | protein phosphorylation | Tyrosine phosphatase (EC 3.1.3.48) | O-tyr | **REMOVE** |

**TOPP4** (AT2G39840) - Type One Protein Phosphatase 4
- Has "protein serine/threonine phosphatase activity" annotation
- Member of PP1 phosphatase complex
- Phosphatases catalyze dephosphorylation, NOT phosphorylation

**CDC25** (AT5G03455) - Cell division cycle 25 phosphatase
- Has "protein tyrosine phosphatase activity" annotation
- Unlike animal CDC25 phosphatases, plant CDC25 has unclear function
- Still annotated as phosphatase - opposite reaction

### Lipid Kinases Annotated to Protein Phosphorylation [W-lipid]

| Gene | GO Term | Issue | Code | Action |
|------|---------|-------|------|--------|
| **ATPI4K ALPHA** | protein phosphorylation | PI4-kinase (EC 2.7.1.67) | W-lipid | **MODIFY** → GO:0046834 |
| **PI4K GAMMA 7** | protein autophosphorylation | PI4-kinase | W-lipid | **MODIFY** → GO:0046834 |

These are phosphatidylinositol 4-kinases that phosphorylate lipids, not proteins.

### Sugar/Carbohydrate Kinases [W-sugar]

| Gene | GO Term | Issue | Code | Action |
|------|---------|-------|------|--------|
| **PWD** | protein autophosphorylation | Phosphoglucan water dikinase | W-sugar | **MODIFY** → GO:0046835 |

**PWD** (AT5G26570) - Phosphoglucan water dikinase
- Has "alpha-glucan, water dikinase activity" and "carbohydrate kinase activity"
- Phosphorylates starch glucans for degradation, NOT proteins

### Regulatory Subunits [R-regulatory]

| Gene | GO Term | Issue | Code | Action |
|------|---------|-------|------|--------|
| **CKB2** | protein phosphorylation | CK2 regulatory beta subunit | R-regulatory | **MODIFY** → GO:0045859 |

**CKB2** (AT4G17640) - Casein Kinase 2 Beta 2
- Has "protein kinase regulator activity" and "protein kinase CK2 complex"
- Regulatory subunit - kinase activity is from CK2 alpha subunits

### Substrate/Immune Regulator [S]

| Gene | GO Term | Issue | Code | Action |
|------|---------|-------|------|--------|
| **RIN4** | protein phosphorylation | RPM1-Interacting Protein 4 | S | **REMOVE** |

**RIN4** (AT3G25070) - Key plant immunity regulator
- Phosphorylated BY pathogen effectors and kinases (e.g., RPS2, RPM1 pathway)
- RIN4 is the SUBSTRATE, not the enzyme
- Known to be phosphorylated at multiple sites during immune signaling

### Special Cases - Needs Investigation

| Gene | GO Term | Status | Notes |
|------|---------|--------|-------|
| **CRY2** | protein autophosphorylation | INVESTIGATE | Cryptochrome - may have genuine kinase activity |
| **LecRK-I.5/I.8** | protein phosphorylation/autophosphorylation | INVESTIGATE | Receptor-like kinases - may have kinase domain |
| **AAK1** | protein autophosphorylation | INVESTIGATE | May be genuine kinase |

**CRY2** (AT1G04400) - Cryptochrome 2
- Blue light photoreceptor with "kinase activity" annotation
- Some cryptochromes have genuine autophosphorylation activity
- Needs literature review to determine if this is substrate or enzyme activity

## IEA Annotations (29 genes)

Many unnamed genes (AT* format) with IEA evidence from TAIR computational analysis. These may be:
- Predicted kinases without experimental validation
- Proteins with kinase-like domains but unclear function
- Computational false positives

These require case-by-case review with lower priority than IDA-supported annotations.

## Arabidopsis Cyclin Annotations

Not specifically checked, but plant cyclins (CYCA, CYCB, CYCD series) should be verified for
correct annotation to regulatory activity rather than phosphorylation.

## Cross-Species Comparison: Final Summary (All 8 MODs)

| Pattern | Mouse | Human | Fly | Zebrafish | Worm | Arabidopsis | S. cerevisiae | S. pombe |
|---------|-------|-------|-----|-----------|------|-------------|---------------|----------|
| **Total problematic** | ~20 | ~45 | ~3 | 1 | 0 | **~7-10** | 0 | 0 |
| Phosphatases | 0 | 3 | 0 | 0 | 0 | **2** | 0 | 0 |
| Lipid kinases | 0 | 1 | 0 | 0 | 0 | **2** | 0 | 0 |
| Sugar kinases | 0 | 1 | 1 | 1 | 0 | **1** | 0 | 0 |
| Regulatory subunits | 0 | 0 | 0 | 0 | 0 | **1** | 0 | 0 |
| Substrates | 0 | 5 | 1? | 0 | 0 | **1** | 0 | 0 |

**Key observation**: TAIR has moderate annotation quality, similar to or better than mammalian
databases for the confirmed issues. The presence of phosphatases (TOPP4, CDC25) annotated to
phosphorylation is concerning - same pattern as human GOA.

## STATUS (Arabidopsis)

- [x] Query analysis completed - **~7-10 clear problematic annotations found**
- [x] 2 phosphatases (TOPP4, CDC25) identified - **REMOVE** [O]
- [x] 2 lipid kinases (ATPI4K ALPHA, PI4K GAMMA 7) - **MODIFY** [W-lipid]
- [x] 1 sugar dikinase (PWD) - **MODIFY** [W-sugar]
- [x] 1 regulatory subunit (CKB2) - **MODIFY** [R-regulatory]
- [x] 1 substrate (RIN4) - **REMOVE** [S]
- [ ] CRY2, LecRK genes need further investigation
- [ ] IEA annotations (29 genes) need systematic review

**Last updated**: 2026-01-19

---

## 2026-01-19 (Session 9 continued - Arabidopsis Analysis)

Extended analysis to Arabidopsis thaliana using TAIR database.

**Key finding**: TAIR has **~7-10 clear problematic phosphorylation annotations**, plus ~29 IEA
annotations requiring systematic review.

**Confirmed misannotations (IDA/IMP supported)**:
1. **TOPP4** - Protein phosphatase annotated to phosphorylation [O-ser]
2. **CDC25** - Tyrosine phosphatase annotated to phosphorylation [O-tyr]
3. **ATPI4K ALPHA** - PI4-kinase (lipid kinase) [W-lipid]
4. **PI4K GAMMA 7** - PI4-kinase (lipid kinase) [W-lipid]
5. **PWD** - Starch dikinase [W-sugar]
6. **CKB2** - CK2 regulatory subunit [R-regulatory]
7. **RIN4** - Immune regulator (substrate) [S]

**Note**: Initial query found 49 genes, but 7 were false positives due to different ID formats
in TAIR (locus:XXXXXX vs ATXGXXXXX). Symbol-based matching reduced this to 42 genes.

**Annotation quality gradient (final - 8 MODs)**:
- **EXCELLENT**: SGD, PomBase, WormBase (0 errors)
- **VERY GOOD**: ZFIN (1 error)
- **GOOD**: FlyBase (~3 errors), TAIR (~7-10 confirmed)
- **NEEDS REVIEW**: MGI (~20 errors), GOA (~45 errors)

---

# RAT (RGD) PHOSPHORYLATION ANALYSIS

## Overview

Extended the phosphorylation annotation analysis to Rattus norvegicus using the RGD database
(`rgd.ddb`). Rat shows **moderate annotation issues** - 11 genes were identified, but most are
ISS transfers from mouse/human showing identical error patterns. A few IDA annotations warrant
closer examination.

## Summary Statistics (Rat - RGD database)

- **Total annotations in database**: 635,614
- **Non-kinase genes with protein phosphorylation annotations**: 11
- **Breakdown by evidence type**:
  - ISS: 7 annotations (transferred from orthologs)
  - IDA: 4 annotations (direct experimental evidence)

## Candidates Analysis

### ISS Transfers (Same Errors as Mouse/Human)

| Gene | GO Term | Error Type | Code | Origin |
|------|---------|------------|------|--------|
| **Gas6** | protein phosphorylation | Signaling ligand | R-ligand | Mouse/Human |
| **Glyctk** | protein phosphorylation | Sugar kinase (EC 2.7.1.31) | W-sugar | Human |
| **Ilf3** | protein phosphorylation | Substrate | S | Human |
| **Pdgfb** | protein phosphorylation, peptidyl-Tyr phosphorylation | Signaling ligand | R-ligand | Human |
| **Prrt1** | protein phosphorylation | Adapter protein | R-adapter | Human |
| **Ywhaz** | protein phosphorylation | 14-3-3 adapter | R-adapter | Human |
| **Ppp3cb** | protein phosphorylation | **PHOSPHATASE** (calcineurin) | O-ser | Human |

**Ppp3cb** is particularly egregious - it's calcineurin, a calcium-dependent protein serine/threonine
PHOSPHATASE (EC 3.1.3.16), annotated to phosphorylation. Has "phosphatase activity" (IDA/TAS) annotations.

### IDA Annotations (Require Review)

| Gene | GO Term | Analysis | Code | Action |
|------|---------|----------|------|--------|
| **Grm5** | protein phosphorylation | GPCR with "protein tyrosine kinase activator activity" | R-receptor | **MODIFY** |
| **Pick1** | protein phosphorylation | PDZ scaffold with "protein kinase C binding" | R-adapter | **MODIFY** |
| **Thy1** | protein autophosphorylation | GPI-anchored protein, no kinase domain | S? | **INVESTIGATE** |

**Grm5** (Metabotropic glutamate receptor 5)
- GPCR that activates Src family kinases via Homer scaffolding
- Has "protein tyrosine kinase activator activity" (IGI/ISO)
- The receptor ACTIVATES kinases but doesn't phosphorylate - should be regulatory term
- Action: **MODIFY** → GO:0045859 [R-receptor]

**Pick1** (Protein interacting with C kinase 1)
- PDZ domain protein that binds and scaffolds PKC
- Has "protein kinase C binding" (IDA) - it's an ADAPTER, not a kinase
- Action: **MODIFY** → GO:0045859 [R-adapter]

**Thy1** (Thy-1 membrane glycoprotein)
- GPI-anchored membrane protein
- Annotated to "protein autophosphorylation" (IDA) but has NO kinase domain
- Also has "negative regulation of protein kinase activity" (IDA)
- May be a substrate that affects kinases, not a kinase itself
- Action: **INVESTIGATE** - likely [S] substrate error

## Cross-Species Comparison: Final Summary (All 9 MODs)

| Pattern | Mouse | Human | Rat | Fly | Zebrafish | Worm | Arabidopsis | S. cerevisiae | S. pombe |
|---------|-------|-------|-----|-----|-----------|------|-------------|---------------|----------|
| **Total problematic** | ~20 | ~45 | **11** | ~3 | 1 | 0 | ~7-10 | 0 | 0 |
| Phosphatases | 0 | 3 | **1** | 0 | 0 | 0 | 2 | 0 | 0 |
| Signaling ligands | 5 | 7+ | **2** | 0 | 0 | 0 | 0 | 0 | 0 |
| Sugar kinases | 0 | 1 | **1** | 1 | 1 | 0 | 1 | 0 | 0 |
| Receptors | 2 | 0 | **1** | 0 | 0 | 0 | 0 | 0 | 0 |
| Adapter proteins | 0 | 3 | **3** | 0 | 0 | 0 | 0 | 0 | 0 |
| Substrates | 0 | 5 | **2** | 1? | 0 | 0 | 1 | 0 | 0 |

**Key observation**: RGD errors are almost entirely ISS transfers from MGI/GOA. The 4 IDA annotations
(Grm5, Pick1, Thy1) represent independent rat-specific curation that also shows over-annotation patterns.

## STATUS (Rat)

- [x] Query analysis completed - **11 problematic annotations found**
- [x] 7 ISS transfers identified (same errors as mouse/human)
- [x] 1 phosphatase (Ppp3cb) - **REMOVE** [O-ser]
- [x] 2 signaling ligands (Gas6, Pdgfb) - **MODIFY** [R-ligand]
- [x] 1 sugar kinase (Glyctk) - **REMOVE** [W-sugar]
- [x] 2 adapters (Prrt1, Ywhaz, Pick1) - **MODIFY** [R-adapter]
- [x] 1 receptor (Grm5) - **MODIFY** [R-receptor]
- [ ] Thy1 autophosphorylation needs literature review

**Last updated**: 2026-01-19

---

## 2026-01-19 (Session 10 - Rat Analysis)

Extended analysis to Rattus norvegicus using RGD database.

**Key finding**: RGD has **11 problematic phosphorylation annotations**, mostly ISS transfers from
mouse/human. The errors mirror those found in the source databases (MGI, GOA).

**ISS transfer errors (7 genes)**:
- Gas6, Pdgfb - signaling ligands [R-ligand]
- Glyctk - sugar kinase [W-sugar]
- Ilf3 - substrate [S]
- Prrt1, Ywhaz - adapter proteins [R-adapter]
- Ppp3cb - phosphatase (calcineurin) [O-ser]

**IDA annotations requiring review (4 genes)**:
- Grm5 - GPCR that activates kinases [R-receptor]
- Pick1 - PKC scaffold/adapter [R-adapter]
- Thy1 - GPI protein with suspicious autophosphorylation claim [S?]

**Annotation quality gradient (updated - 9 MODs)**:
- **EXCELLENT**: SGD, PomBase, WormBase (0 errors)
- **VERY GOOD**: ZFIN (1 error)
- **GOOD**: FlyBase (~3 errors), TAIR (~7-10 confirmed)
- **MODERATE**: RGD (11 errors, mostly ISS transfers)
- **NEEDS REVIEW**: MGI (~20 errors), GOA (~45 errors)
