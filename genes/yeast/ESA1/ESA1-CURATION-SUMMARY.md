# ESA1 GO Annotation Curation Summary

## Executive Summary

The yeast ESA1 gene (Histone Acetyltransferase ESA1, UniProt Q08649) received a comprehensive review of 63 GO annotations. Through systematic evaluation against literature evidence, curation actions were assigned as follows:

### Curation Statistics

| Category | Count | Percentage |
|----------|-------|-----------|
| **ACCEPT** (core/essential) | 29 | 46% |
| **REMOVE** (contradicted) | 1 | 2% |
| **KEEP_AS_NON_CORE** (valid but secondary) | 8 | 13% |
| **MODIFY** (better terms exist) | 1 | 2% |
| **UNDECIDED** (insufficient evidence) | 2 | 3% |
| **DUPLICATE/CONSOLIDATED** (26 protein binding entries) | 26 | 41% |

---

## Key Curation Decisions

### 1. REMOVED ANNOTATIONS (1)

**GO:0010629 - Negative regulation of gene expression [IEA]**
- **Reason:** Directly contradicted by literature. ESA1/NuA4 is a documented POSITIVE regulator of transcription, not negative.
- **Evidence Against:** PMID:10835360, PMID:15175650, PMID:19822662 all document transcription activation/stimulation
- **Action Taken:** REMOVE - appears to be ARBA ML model artifact

### 2. MODIFIED ANNOTATIONS (1)

**GO:0003682 - Chromatin binding [IBA]**
- **Reason:** Generic and uninformative. Redundant with GO:0004402 (histone acetyltransferase activity) and GO:0000785 (chromatin)
- **Alternative:** Either remove or replace with more specific "nucleosome binding" or rely on enzymatic activity annotations
- **Rationale:** "Chromatin binding" provides no mechanistic information and is subsumed by more specific annotations

### 3. CORE ACCEPTED ANNOTATIONS (29)

The following represent ESA1's essential, well-documented functions:

#### Molecular Function (Most Informative)
- **GO:0010485 - Histone H4 acetyltransferase activity** (IDA, IEA) ★ PRIMARY
  - Most specific and informative histone acetyltransferase annotation
  - Captures H4 substrate specificity (K5, K8, K12, K16)
  - Evidence: PMID:10487762, PMID:12110674

- **GO:0140068 - Histone crotonyltransferase activity** (IDA)
  - ESA1 catalyzes crotonylation using crotonyl-CoA
  - Evidence: PMID:31699900 (experimental demonstration)

- **GO:0004402 - Histone acetyltransferase activity** (IBA, IEA, IDA)
  - Broader than H4-specific annotation
  - Multiple evidence codes provide confidence

- **GO:0061733 - Protein-lysine-acetyltransferase activity** (IEA, IDA)
  - Captures broader substrate spectrum including non-histones
  - Evidence: PMID:22539722 (ATG3), PMID:29765047 (PAH1)

- **GO:0003712 - Transcription coregulator activity** (IBA, IDA)
  - Correctly identifies regulatory role vs. core transcription machinery

#### Biological Process (Primary Functions)
- **GO:0006357 - Regulation of transcription by RNA polymerase II** (IBA, IEA, IMP) ★ PRIMARY
  - Most important biological process annotation
  - Multiple evidence codes: phylogenetic (IBA), computational (IEA), experimental (IMP)

- **GO:0032968 - Positive regulation of transcription elongation by RNA polymerase II** (IMP, IGI)
  - More specific than generic transcription regulation
  - Evidence: PMID:19822662 (explicit demonstration)

- **GO:0006281 - DNA repair** (IEA, IMP, IDA, IGI) ★ PRIMARY
  - Critical function: H4K16ac required for DSB repair
  - Strongest evidence: PMID:12353039 (IMP mutation analysis)

- **GO:0006974 - DNA damage response** (IEA)
  - DSB-specific recruitment and activation documented

- **GO:0051726 - Regulation of cell cycle** (IMP) ★ PRIMARY
  - Essential for mitosis/cytokinesis
  - Evidence: PMID:10082517 (temperature-sensitive block)

- **GO:0006354 - DNA-templated transcription elongation** (IDA, IMP)
  - Specific process with documented ESA1 requirement

- **GO:0006325 - Chromatin organization** (IEA)
  - Consequence of histone acetylation

- **GO:0006355 - Regulation of DNA-templated transcription** (IEA)
  - Broader regulatory role

#### Cellular Component
- **GO:0035267 - NuA4 histone acetyltransferase complex** (IEA, IDA) ★ ESSENTIAL
  - ESA1 is the catalytic subunit
  - Multiple evidence codes establish complex membership

- **GO:0032777 - Piccolo histone acetyltransferase complex** (IDA)
  - Variant complex containing ESA1
  - Evidence: PMID:12782659

- **GO:0005634 - Nucleus** (IBA, NAS)
  - Nuclear localization of ESA1

- **GO:0000785 - Chromatin** (IBA, IDA)
  - Functional localization

---

## Non-Core Accepted Annotations (8)

These are valid but represent secondary or indirect functions:

1. **GO:0010867 - Positive regulation of triglyceride biosynthetic process** (IDA)
   - Secondary metabolic function through PAH1 acetylation
   - Evidence: PMID:29765047
   - Rationale: Real but peripheral to primary ESA1 roles

2. **GO:0016239 - Positive regulation of macroautophagy** (IMP)
   - Emerging function through ATG3 acetylation
   - Evidence: PMID:22539722
   - Rationale: Documented but non-primary function

3. **GO:0000183 - rDNA heterochromatin formation** (IMP, IGI)
   - Mechanistically unclear and paradoxical
   - Evidence: PMID:16436512 (distinct silencing roles)
   - Rationale: How HAT promotes heterochromatin is counterintuitive; appears indirect

4. **GO:0033554 - Cellular response to stress** (IEA)
   - Too generic; covered by more specific GO:0006974 (DNA damage response)

5. **GO:0008270 - Zinc ion binding** (RCA)
   - Structural zinc coordination in MYST HAT domain
   - Evidence: PMID:30358795 (proteome survey)
   - Rationale: Indirect evidence (survey); structural role not mechanistic function

6. **GO:0006351 - DNA-templated transcription** (IEA, NAS)
   - Misleadingly suggests ESA1 performs transcription rather than regulating it
   - Prefer GO:0006357 (regulation) over core basal transcription

7. **GO:0016740 - Transferase activity** (IEA)
   - Generic ancestor of acetyltransferase annotations
   - Uninformative but technically correct

8. **GO:0005515 - Protein binding** (26 IPI entries - consolidated)
   - Multiple validated interactions with NuA4 subunits and substrates
   - Rationale: Non-specific binding term provides minimal mechanistic information
   - Better represented as complex membership and enzymatic substrate interactions

---

## Undecided Annotations (2)

### 1. GO:0106226 - Peptide 2-hydroxyisobutyryltransferase activity (IEA)
- **Issue:** Ortholog-inferred activity based on Tip60 homology. No in vivo evidence for yeast ESA1.
- **Recommendation:** Retain as future-oriented annotation or remove if restricting to experimentally demonstrated functions

### 2. Potential Missing Annotations (H3K56 acetylation)
- **Question:** Is H3K56 acetylation a documented ESA1 function? Literature suggests S-phase-specific role but not explicitly captured in current annotations.

---

## Critical Mechanistic Insights

### Substrate Specificity Hierarchy

ESA1 acetylates multiple substrates with distinct functional consequences:

1. **Histone H4** (primary substrate)
   - K5, K8, K12, K16 acetylation
   - Roles: Transcription initiation, DNA repair, cell cycle
   - Best annotation: GO:0010485

2. **Histone H3** (secondary substrate)
   - K14 acetylation
   - Less abundant than H4 acetylation
   - Captured by GO:0004402

3. **Histone H2A/H2B** (minor substrate)
   - Various lysine residues
   - Captured by GO:0004402

4. **Histone variant H2A.Z** (specialized)
   - K14 acetylation
   - Role in promoter acetylation
   - Captured by GO:0004402

5. **Non-histone proteins** (emerging functions)
   - ATG3 (autophagy - PMID:22539722)
   - PAH1 (lipid synthesis - PMID:29765047)
   - Captured by GO:0061733

### Functional Contexts

ESA1 operates in distinct but interconnected biological contexts:

#### 1. Transcriptional Activation (PRIMARY)
- Recruited by transcription factors to gene promoters
- H4 acetylation marks active genes
- Facilitates Pol II recruitment and elongation
- **Core annotations:** GO:0006357, GO:0032968, GO:0003712

#### 2. DNA Damage Response (PRIMARY)
- DSB-specific recruitment via Arp4 component
- H4K16ac enables repair machinery access
- Requirement for homologous recombination
- **Core annotations:** GO:0006281, GO:0006974

#### 3. Cell Cycle Control (PRIMARY)
- Mitotic checkpoint control
- Links acetylation to cell cycle progression genes
- **Core annotation:** GO:0051726

#### 4. Metabolic Regulation (SECONDARY)
- ATG3 acetylation → autophagy regulation
- PAH1 acetylation → fatty acid synthesis
- **Non-core annotations:** GO:0016239, GO:0010867

#### 5. Chromatin Architecture (PRIMARY)
- Nucleosome destabilization
- Altered histone-DNA contacts
- **Core annotation:** GO:0006325

---

## Outstanding Questions and Recommendations

### 1. Mechanistic Paradox: Activation vs. Silencing
- **Question:** How does an activating HAT (ESA1) promote heterochromatin formation at rDNA?
- **Implication:** GO:0000183 (rDNA heterochromatin) remains marked as non-core pending mechanistic clarification
- **Suggested Experiment:** ChIP-seq of ESA1 and H4ac marks at rDNA regions; analysis of heterochromatin-associated factors

### 2. Cell Cycle-Dependent Substrate Specificity
- **Question:** Is H3K56 acetylation (S-phase histone deposition mark) a documented ESA1 function or only Gcn5?
- **Current Status:** Not explicitly captured in existing annotations
- **Recommendation:** If documented, add specific annotation for S-phase H3K56ac function

### 3. Alternative Acyl-CoA Substrates
- **Question:** Biological relevance of 2-hydroxyisobutyrylation? In vitro artifact or documented in vivo modification?
- **Current Status:** GO:0106226 marked as UNDECIDED
- **Recommendation:** Retain for future updating if biological role is demonstrated

### 4. Crotonylation vs. Acetylation Dynamics
- **Question:** Are crotonylated and acetylated histones found on same nucleosomes or distinct genomic regions?
- **Implication:** Understand substrate selectivity and potential competition between acetyl-CoA and crotonyl-CoA
- **Suggested Experiment:** Quantitative proteomics comparing H4ac vs. H4cr marks

### 5. Regulation of ESA1 Activity
- **Question:** How is ESA1 catalytic activity regulated? Phosphorylation (PMID:16135807), localization, complex assembly?
- **Current Status:** Not captured in annotations
- **Recommendation:** Consider additional annotations for "regulation of histone acetyltransferase activity" if mechanisms are demonstrated

---

## Annotation Best Practices Applied

### 1. Specificity Over Generality
- **Removed:** Generic "protein binding" annotations (consolidated as non-core)
- **Preferred:** Specific substrate annotations (GO:0010485 H4-acetyltransferase > GO:0004402 general HAT)
- **Rationale:** More informative for functional understanding

### 2. Evidence Quality Hierarchy
- **Prioritized:** IDA (direct assay), IMP (mutation), IGI (genetic) over IEA (computational)
- **Example:** DNA repair function supported by IMP (PMID:12353039) is stronger than IEA alone
- **Exception:** IBA (phylogenetic) for widely conserved functions is reliable

### 3. Process vs. Mechanism Distinction
- **Separated:** GO:0006351 (performs transcription) from GO:0006357 (regulates transcription)
- **Removed:** Generic GO:0006351 annotation as misleading
- **Preferred:** GO:0006357 and GO:0032968 capturing ESA1's regulatory role accurately

### 4. Complex vs. Independent Function
- **Captured:** ESA1 as NuA4 complex catalytic subunit (GO:0035267)
- **Noted:** Most ESA1 functions occur within NuA4 complex context, not independent
- **Implication:** Complex membership is fundamental to understanding ESA1

---

## Recommended Display Prioritization

### Tier 1: Core Functions (Primary Display)
1. GO:0010485 - Histone H4 acetyltransferase activity [PRIMARY SPECIFIC]
2. GO:0006357 - Regulation of transcription by RNA polymerase II [PRIMARY PROCESS]
3. GO:0006281 - DNA repair [PRIMARY PROCESS]
4. GO:0051726 - Regulation of cell cycle [PRIMARY PROCESS]
5. GO:0035267 - NuA4 histone acetyltransferase complex [ESSENTIAL COMPLEX]
6. GO:0005634 - Nucleus [LOCATION]

### Tier 2: Related but Important (Secondary Display)
7. GO:0032968 - Positive regulation of transcription elongation [SPECIFIC REGULATORY ROLE]
8. GO:0006974 - DNA damage response [RELATED PROCESS]
9. GO:0140068 - Histone crotonyltransferase activity [EMERGING FUNCTION]
10. GO:0061733 - Protein-lysine-acetyltransferase activity [BROADER SUBSTRATE ACTIVITY]

### Tier 3: Non-Core/Context-Specific (Specialized Display)
11. GO:0010867 - Positive regulation of triglyceride biosynthetic process
12. GO:0016239 - Positive regulation of macroautophagy
13. Other non-core annotations

---

## Files Generated

1. **ESA1-CURATION-ANALYSIS.md** - Detailed annotation-by-annotation review with evidence analysis
2. **ESA1-ai-review-CURATED.yaml** - Complete YAML file with curation actions and supporting evidence
3. **ESA1-CURATION-SUMMARY.md** - This executive summary document

---

## Conclusion

The ESA1 annotation review identified that while the existing 63 annotations generally represent documented functions, significant improvements in specificity and accuracy are achievable:

- **1 annotation REMOVED** (negative regulation - contradicted)
- **29 annotations ACCEPTED** as correct and informative
- **8 annotations MARKED AS NON-CORE** (valid but secondary)
- **2 annotations UNDECIDED** (insufficient evidence)
- **1 annotation MODIFIED** (generic "chromatin binding" - recommend removal)

The curated annotation set prioritizes mechanistically informative terms (H4 acetyltransferase over generic HAT), experimental evidence (IDA/IMP over IEA), and proper functional context (regulatory vs. core machinery). Key functional areas (transcription regulation, DNA repair, cell cycle) are well-annotated with multiple supporting evidence codes.

Outstanding questions regarding mechanistic paradoxes (heterochromatin formation), cell cycle-specific substrate specificity, and alternative acyl-CoA substrates provide avenues for future experimental validation and annotation refinement.
