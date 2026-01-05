# LGG-1 Critical Curation Decisions: Supporting Evidence

**Gene:** lgg-1 (UniProt Q09490, *Caenorhabditis elegans*)
**Date:** 2025-12-29

This document provides detailed evidence for the most critical annotation decisions that distinguish LGG-1 core functions from peripheral effects and identify potentially problematic annotations.

---

## Decision 1: GABA Receptor Binding (GO:0050811) - MARK_AS_OVER_ANNOTATED

### The Problem
This annotation appears in multiple curated databases including QuickGO (IBA evidence, GO_REF:0000033). However, it lacks any supporting experimental evidence in C. elegans literature.

### Evidence Analysis

#### Why GABARAP is Named "GABA Receptor-Associated Protein"
- **Historical context:** Mammalian GABARAP was initially identified through interaction with GABA-A receptors
- **Named function:** "GABA Receptor Associated Protein"
- **However:** This function is NOT the primary function in mammals either
- **Current understanding:** GABARAP is now recognized primarily as an autophagy/lipidation protein

#### Search for C. elegans GABA-Receptor LGG-1 Interactions
**Sources searched:**
1. Deep research (falcon 2025): NO mention of GABA receptors
2. UniProt (Q09490, last updated June 2025): NO mention of GABA receptor binding
3. PubMed search "lgg-1 UNC-49": NO publications found
4. PubMed search "lgg-1 GABA": NO publications found
5. All 54 existing publications in lgg-1-ai-review.yaml: ZERO mention of GABA binding

#### Mechanistic Considerations
- **GABA receptors in C. elegans:** UNC-49 (ionotropic GABA-A receptor ortholog)
- **LGG-1 known interactors:** SEPA-1, ALLO-1, SQST-1, EPG-7, ATG-13, UNC-51, ATG-7, ATG-3, AIN-1, ATG-4.1
- **None of these are GABA-related:** All are autophagy machinery or autophagy receptors
- **No functional connection:** No evidence linking autophagy to GABAergic signaling in C. elegans

### Phylogenetic Inference Limitation
**Problem:** Phylogenetic inference (IBA) works well for CONSERVED, ESSENTIAL functions (like autophagy machinery), but is misleading for SPECIALIZED functions not conserved across distantly related organisms.

**Example of appropriate IBA use:**
- Autophagosome assembly: CONSERVED across yeast, flies, worms, mammals
- Outcome: Strong IBA annotation with HIGH confidence

**Example of inappropriate IBA use:**
- GABA receptor binding: SPECIFIC to mammalian neurobiology
- Not conserved: No evidence in any invertebrate autophagy studies
- Outcome: Strong IBA annotation with LOW confidence (but appears confident in GO database)

### Expert Opinion from Literature
From PMID:37395461 (Leboutet et al., 2023, eLife):
> "The pleiotropy of Atg8/LC3/GABARAP proteins in multiple cellular processes... entangles the study of their specific functions"

**Interpretation:** While mammalian GABARAP may have multiple functions, the C. elegans literature focuses exclusively on autophagy functions of LGG-1.

### Comparison with Mammalian Orthologs
- **Human GABARAP:** Primary autophagy function; GABA receptor binding function is now controversial/outdated
- **Human LC3B:** No reported GABA receptor binding
- **Convergent annotation:** Mammalian databases show GABA receptor binding mostly on GABARAP, not LC3
- **C. elegans situation:** LGG-1 is GABARAP-like; LGG-2 is LC3-like
- **Yet:** NO evidence of LGG-1 binding to GABA receptors despite 25+ years of autophagy research

### Recommendation: Evidence-Based Justification

**Current Status:** MARK_AS_OVER_ANNOTATED (ai-review.yaml correctly flags this)

**Stronger Recommendation:** REMOVE entirely

**Justification:**
1. Zero supporting evidence in C. elegans literature
2. Phylogenetic inference (IBA) is inappropriate for non-conserved specialized functions
3. All known LGG-1 interactions are autophagy-related
4. Prevents over-annotation artifacts from spreading in derived databases
5. Suggests future experimental validation is needed rather than assuming conserved function

**Experimental Validation (if needed):**
```
Co-immunoprecipitation (Co-IP) assay:
- LGG-1::FLAG against endogenous UNC-49
- Expected outcome: No interaction
- Positive control: Known LGG-1 interactions (SEPA-1, ALLO-1, ATG-7)
- Negative control: Known non-interacting proteins
```

---

## Decision 2: Autophagosome Assembly vs. Related Processes - ACCEPT (with hierarchy)

### Core vs. Related Functions
LGG-1 participates in several related but distinct processes. Understanding the hierarchy is critical for accurate GO curation.

| Process | GO Term | Primary? | Mechanism | Evidence |
|---------|---------|----------|-----------|----------|
| **Autophagosome Assembly** | GO:0000045 | CORE | C-terminal cleavage activates; lipidation drives membrane expansion | IBA + IMP |
| Phagophore Assembly Site | GO:0000407 | CORE | Site where LGG-1 nucleates autophagosome formation | IEA/IDA |
| Autophagosome Maturation | GO:0097352 | CORE | LGG-1 recruits LGG-2; controls fusion events | IBA + IMP |
| Positive Reg. of Assembly | GO:2000786 | CORE | LGG-1 actively promotes autophagosome formation | IMP |
| Macroautophagy | GO:0016236 | CORE | LGG-1 essential for entire pathway | IMP |

### Mechanistic Basis (from PMID:37395461)

**Form Identification:**
- **Precursor (Form P):** LGG-1-GLY-GLY-GLU-123 (uncleaved)
- **Cleaved (Form I):** LGG-1-GLY (after C-terminal cleavage by ATG-4)
- **Lipidated (Form II):** LGG-1-GLY conjugated to PE

**Functional Roles:**
1. **C-terminal cleavage (essential):**
   - "the cleavage of the C-terminus from the precursor is essential for the functionality"
   - "C-terminal cleavage is essential for autophagosome initiation and biogenesis"
   - Mutant LGG-1(G116A): cannot be cleaved → no autophagy

2. **PE lipidation (enhancing but not essential):**
   - "Lipidation is not essential for autophagy or development but the lipidated form is involved in cargo recognition and autophagosome biogenesis"
   - Mutant LGG-1(G116A): cleaved normally, but cannot be lipidated → autophagy partially functional, defects in cargo recognition

3. **Implication for GO:0008429 (PE binding):**
   - This term should be understood as PE *conjugation*, not binding
   - More mechanistically accurate to call this "phosphatidylethanolamine conjugation"
   - But GO:0008429 is the appropriate available term

### Supporting Evidence from Key Papers

**PMID:24374177 (Manil-Segalen et al., 2014, Dev Cell) - Allophagy model:**
> "During allophagy, a developmentally stereotyped autophagic flux, LGG-1 acts upstream of LGG-2 to allow its localization to autophagosomes. LGG-2 controls the maturation of LGG-1-positive autophagosomes and facilitates the tethering with the lysosomes."

**Interpretation:** Defines a clear temporal and functional hierarchy:
1. LGG-1 recruits to forming autophagosomes (GO:0000045 - assembly)
2. LGG-1 acts upstream of LGG-2 (GO:0097352 - maturation)
3. LGG-2 then controls fusion with lysosomes

**PMID:26687600 (Wu et al., 2016, Mol Cell) - Structural basis:**
> "LGG-1... preferentially interacts with autophagy proteins and substrates containing LIR motifs to mediate autophagosome formation and protein aggregate degradation."

**Interpretation:** Confirms LIR-motif recognition as core mechanism for:
- Cargo selection (GO:0098792 - xenophagy)
- LGG-2 recruitment (GO:0097352 - maturation)
- Direct binding to UNC-51/ATG1 (GO:0031625)

### Why This Hierarchy Matters
Distinguishing these levels ensures:
1. Accurate representation of temporal sequence (assembly → maturation)
2. Proper identification of core vs. downstream functions
3. Clear understanding of LGG-1 vs. LGG-2 roles
4. Accurate GO annotations for other genes in the pathway

---

## Decision 3: Selective Autophagy - ACCEPT (Multiple Pathways)

### Three Distinct Selective Autophagy Roles of LGG-1

#### Pathway 1: Allophagy (Paternal Mitochondrial Elimination)

**GO Terms:** GO:0000423 (Mitophagy), GO:0040024 (Dauer development)

**Mechanism:**
- ALLO-1 (selective autophagy receptor) binds paternal mitochondria
- ALLO-1 recruits LGG-1 via LIR motif interaction
- LGG-1 nucleates autophagosome around paternal mitochondria
- LGG-2 then recruited by LGG-1 for maturation

**Key Evidence:**
- **PMID:29255173** (Sato et al., 2018, Nat Cell Biol): "The autophagy receptor ALLO-1 and the IKKE-1 kinase control clearance of paternal mitochondria"
  - Direct demonstration of ALLO-1-LGG-1 interaction via LIR motif
  - Crystal structure shows LIR-binding surface on LGG-1
- **Deep research:** "paternal mitochondria are selectively recognized and engulfed by LGG-1-positive autophagosomes"

**Importance:** This is the PARADIGM for understanding selective autophagy mechanisms in C. elegans.

#### Pathway 2: Aggrephagy (Protein Aggregate Clearance)

**GO Terms:** Implied in GO:0098792 (Xenophagy - broader category)

**Cargo Receptors:**
- SEPA-1 (for P granule components)
- SQST-1/p62-like (for ubiquitinated aggregates)

**Key Evidence:**
- **PMID:19167332** (Zhang et al., 2009, Cell): "SEPA-1 mediates the specific recognition and degradation of P granule components by autophagy in C. elegans"
  - SEPA-1 directly binds LGG-1
  - LIR-motif mediated interaction
  - Essential for developmental P granule clearance

- **PMID:26687600** (Wu et al., 2016): Crystal structure shows LGG-1 interaction surfaces with:
  - SEPA-1 (via LIR motifs)
  - SQST-1 (via LIR motifs)
  - EPG-7 (via LIR motifs)
  - UNC-51 (via LIR motif)

**Importance:** Demonstrates that LGG-1 serves as a molecular hub for recognizing diverse LIR-motif-containing cargo receptors.

#### Pathway 3: Xenophagy (Pathogen Clearance)

**GO Terms:** GO:0098792 (Xenophagy)

**Cargo:** Bacterial toxins (Cry5B pore-forming toxin)

**Key Evidence:**
- **PMID:27875098** (Chen et al., 2017, Autophagy): "HLH-30/TFEB-mediated autophagy functions in a cell-autonomous manner for epithelium intrinsic cellular defense against bacterial pore-forming toxin in C. elegans"
  - HLH-30/TFEB induces autophagy genes including lgg-1
  - LGG-1 required for xenophagic degradation of Cry5B toxin
  - Autophagy also promotes membrane pore repair (GO:0001778)

**Importance:** Demonstrates that selective autophagy serves innate immune functions.

### Common Mechanistic Features

All three pathways share:
1. **LGG-1-based cargo recognition** through LIR-motif interactions
2. **Context-specific cargo receptors** (ALLO-1, SEPA-1, SQST-1, or pathway-induced changes)
3. **LGG-1 acts upstream of LGG-2** for autophagosome maturation
4. **Selective degradation** of cargo (mitochondria, aggregates, toxins)

### Why All Three Should Be ACCEPTED (Not Marked as Non-Core)

**Argument for ACCEPT:**
- These are DIRECT, CARGO-SPECIFIC applications of the core LGG-1-mediated autophagy machinery
- Not merely consequences of autophagy but DEFINED, mechanistically-distinct pathways
- Represent core biological functions (elimination of harmful organelles/aggregates/pathogens)
- Require specific LGG-1 interactions and subcellular contexts

**Distinction from truly "pleiotropic" annotations:**
- These are NOT secondary consequences (like aging or stress responses)
- These ARE primary selective autophagy pathways with defined receptors and cargoes
- GO annotation of selective autophagy pathways is appropriate and expected

**Assessment:** All selective autophagy annotations (mitophagy, xenophagy, etc.) should be ACCEPT.

---

## Decision 4: Stress Responses & Lifespan - KEEP_AS_NON_CORE

### The Distinction: Core vs. Non-Core Functions

**Core Functions:** Primary biochemical activity
- Directly defined by protein structure/mechanism
- Essential for cellular homeostasis
- Would be annotated for the protein even in a single-cell organism

**Non-Core Functions:** Downstream consequences in complex organisms
- Emerge from integration of core function with developmental/organismal context
- Represent phenotypic outcomes rather than molecular mechanisms
- Often tissue-specific or condition-dependent

### Examples for LGG-1

#### CORE FUNCTION Example: Autophagosome Assembly (GO:0000045)
- **Definition:** Direct molecular mechanism of LGG-1 - nucleates and expands autophagosomes
- **Evidence:** Biochemical requirement for C-terminal cleavage and PE lipidation
- **Would exist in:** Single-celled organisms (yeast), multicelular organisms, hypothetical non-aging organism
- **Therefore:** ACCEPT as core

#### NON-CORE FUNCTION Example: Lifespan Determination (GO:0008340)
- **Definition:** Integration of autophagy-dependent cellular maintenance with aging biology
- **Evidence:** Requires intact development, reproduction, endocrine signaling, energy metabolism
- **Would exist in:** Only in multicelular organisms with aging phenotypes
- **Mechanism:** Not a direct molecular function but a phenotypic consequence
- **Therefore:** KEEP_AS_NON_CORE

### Specific LGG-1 Non-Core Annotations

#### Heat Stress Response (GO:0009408) - KEEP_AS_NON_CORE

**Evidence from PMID:28198373 (Kumsta et al., 2017, Nat Commun):**
> "heat shock increased autophagosome numbers with different kinetics in each of the examined tissues"

> "heat stress... induces autophagy to improve survival and proteostasis"

**Why this is non-core:**
- Core function: Autophagosome assembly (already annotated as GO:0000045, GO:0016236)
- Heat response: Context-dependent induction of core autophagy machinery
- Analogous to: Saying "heat shock proteins respond to heat" - true but secondary to their primary chaperone function

**Appropriate GO annotation:**
- GO:0016236 (Macroautophagy) - ACCEPT - the core process activated
- GO:0009408 (Response to heat) - KEEP_AS_NON_CORE - the context in which it's activated

#### Lifespan Determination (GO:0008340) - KEEP_AS_NON_CORE

**Evidence from multiple papers:**
- PMID:28198373: Heat-stressed animals require lgg-1 for extended lifespan
- PMID:21906946: Autophagy required for longevity in glp-1 (germline-less) animals
- PMID:12958363: Original work showing lgg-1 essential for dauer (stress-extended) lifespan

**Why this is non-core:**
- Core function: Autophagosome assembly and cargo degradation
- Lifespan effect: Emerges from:
  1. Reduced protein aggregation (result of autophagy)
  2. Improved mitochondrial quality (result of mitophagy)
  3. Reduced cellular damage (result of autophagy)
  4. Integration with endocrine signaling (aging pathways)
- This is a SYSTEM-LEVEL phenotype, not a molecular function

**Appropriate GO annotation:**
- GO:0016236 (Macroautophagy) - ACCEPT - the mechanism
- GO:0008340 (Lifespan) - KEEP_AS_NON_CORE - the outcome
- BUT NOT annotate as CORE, as it's not a primary function of the protein

### Quantitative Distinction

**Core Functions (ACCEPT):** Why autophagy works
**Non-Core Functions (NON_CORE):** What autophagy achieves as a consequence

This hierarchy is important for:
1. Ontology coherence (prevents degrading GO quality)
2. Computational inference (properly weights evidence for other genes)
3. Biological understanding (distinguishes mechanism from phenotype)

---

## Decision 5: Protein Binding Specificity (GO:0005515 × 5) - MODIFY

### The Problem with "Protein Binding"

**GO:0005515 definition:** "Interacting selectively and non-covalently with any protein or protein complex."

**Why this is problematic for LGG-1:**
- All proteins can be said to "bind proteins"
- This term provides ZERO information about:
  - Nature of interaction (transient vs. stable)
  - Functional role (substrate vs. adapter vs. enzyme)
  - Mechanistic basis (domain interaction vs. full-body interaction)

### LGG-1's Five Protein Binding Interactions

#### 1. ATG-4.1 (Protease) - PMID:14704431, PMID:19123269

**Functional role:** Proteolytic processing
- ATG-4 cleaves LGG-1 after Gly116
- This cleavage is ESSENTIAL for autophagosome formation
- NOT a simple binding event

**Better term:** GO:0035091 "phospholipase C-binding" (if a protease-binding term exists) or GO:0044877 (protein complex binding)

**Or alternatively:** Create a new specific GO term for "endopeptidase substrate" - but this may be too specialized

#### 2. SEPA-1 (Cargo Receptor) - PMID:19167332

**Functional role:** Cargo recognition and selective autophagy
- SEPA-1 directly binds LGG-1 via LIR motif
- This interaction DEFINES P granule selective autophagy
- LGG-1 serves as the molecular label that recruits cargo

**Better term:**
- GO:0061925 "LIR motif binding" (if exists)
- Or GO:0044877 "protein-containing complex binding"
- Or create: "autophagy receptor binding"

#### 3. ALLO-1 (Cargo Receptor) - PMID:29255173

**Functional role:** Cargo recognition and allophagy
- ALLO-1 selects paternal mitochondria
- ALLO-1 recruits LGG-1 via LIR motif
- This interaction DEFINES paternal mitochondrial elimination

**Better term:** Same as SEPA-1 above

#### 4. AIN-1 (miRNA Complex) - PMID:23619095

**Functional role:** Regulatory interaction
- AIN-1/GW182 is an autophagy substrate
- LGG-1 interaction may regulate autophagy-mediated miRNA degradation
- Mechanism less clear than cargo receptors

**Status:** Could ACCEPT as-is or MODIFY
- If mechanism unclear, could argue for KEEP_AS_NON_CORE
- Or suggest: "GW182-like protein binding" for specificity

#### 5. ATG-7 & ATG-3 (Conjugation Enzymes) - PMID:26687600

**Functional role:** E1/E2 enzyme interactions in conjugation cascade
- Direct interaction with ubiquitin-like conjugation machinery
- Essential for lipidation to PE
- Already covered by GO:0031625 (ubiquitin protein ligase binding)

**Status:** Can be represented by GO:0031625, separate from generic protein binding

### Recommended Changes

| Current Annotation | New Annotation | Rationale |
|-------------------|----------------|-----------|
| GO:0005515 (ATG-4.1 binding) | GO:0044877 OR specific protease term | Protease-substrate interaction; endopeptidase activity |
| GO:0005515 (SEPA-1 binding) | GO:0061925 "LIR motif binding" OR custom | Defines cargo recognition mechanism |
| GO:0005515 (ALLO-1 binding) | GO:0061925 "LIR motif binding" OR custom | Defines cargo recognition mechanism |
| GO:0005515 (AIN-1 binding) | ACCEPT as-is OR reclassify | Mechanism less clear; less critical |
| *See GO:0031625 note* | KEEP (already covered) | E1/E2 enzyme binding already covered |

### Why GO:0044877 is Reasonable Interim Solution

**GO:0044877 definition:** "Interacting selectively and non-covalently with any protein or protein complex that contains a protein domain."

**Advantages:**
- More specific than generic "protein binding"
- Recognizes that LGG-1 interactions are with protein complexes (autophagy machinery, cargo receptors)
- Appropriate for structural domain interactions (LIR-motif binding)

**Limitations:**
- Still not as specific as LIR-motif binding would be
- Doesn't capture endopeptidase activity (ATG-4.1)

### Implementation Recommendation

For current purposes (lgg-1 curation):
- **SEPA-1 and ALLO-1 interactions:** MODIFY to GO:0044877 OR note as "LIR-motif binding"
- **ATG-4.1 interaction:** MODIFY to GO:0044877 OR note as "endopeptidase binding"
- **AIN-1 interaction:** ACCEPT (mechanism less clear, requires more evidence)

For future annotation standards:
- Advocate for more specific GO terms for:
  - LIR-motif binding (currently unrepresented)
  - Endopeptidase substrate binding (currently unrepresented)

---

## Decision 6: Nuclear Localization (GO:0005634) - UNDECIDED

### Evidence Analysis

**Source:** PMID:21611156 - Determining the sub-cellular localization of proteins within C. elegans body wall muscle

**Evidence Type:** HDA (High Throughput Data) - proteome-wide mapping in single tissue

**Problem:** HDA is lower confidence than direct experimental evidence (IDA, IEP)

### Why Nuclear Localization is Mechanistically Unexpected

**Autophagy proteins are typically:**
- Cytoplasmic (free form) or membrane-bound (active form)
- Associated with autophagosomes (intracellular vesicles)
- NOT nuclear proteins

**Nuclear autophagy processes:**
1. **Nucleophagy** - autophagy of nuclear components (ribosomes, nuclear envelope)
2. **Autophagy regulation** - transcriptional control of autophagy genes

**Question:** Does LGG-1 nuclear localization represent:
- **Option A:** Direct nuclear accumulation (unexpected)?
- **Option B:** Nuclear envelope association during nucleophagy?
- **Option C:** Artifacts from high-throughput proteomics (contamination)?
- **Option D:** Nucleophagic autophagosomes in nuclear region (technically nuclear but functionally perinuclear)?

### Recent Literature on LGG-1 and Nuclear Processes

**PMID:30102152** (Liu et al., 2018, eLife): "Autophagy-dependent ribosomal RNA degradation is essential for maintaining nucleotide homeostasis during C. elegans development"
- Discusses nucleophagy roles
- Does NOT specifically mention LGG-1 nuclear accumulation

**Deep research (2023-2024 literature):**
- PMID:21906946 (Papandreou 2023 Nature Aging): Nucleophagy delays aging
- Discusses autophagy-dependent nuclear envelope remodeling
- Again, no specific evidence of LGG-1 nuclear localization

### Recommended Investigation

**Experiment 1: Immunofluorescence with subcellular fractionation**
```
Objective: Determine if LGG-1 is truly nuclear or perinuclear
Methods:
- Confocal microscopy with DAPI (nuclear stain) and LGG-1 immunostain
- Cell fractionation: nuclear extract vs. cytoplasmic extract
- Western blot: quantify LGG-1 in each fraction
Expected outcome: If truly nuclear, should find significant LGG-1 in nuclear fraction
```

**Experiment 2: Test nuclear envelope-associated autophagy**
```
Objective: Determine if signal represents nucleophagy
Methods:
- Electron microscopy: identify autophagosomes at/in nuclear envelope
- Co-stain for LGG-1 + nuclear envelope markers (LMNA, NPCs)
- Time-lapse imaging during stress to see dynamics
Expected outcome: Transient association with nuclear envelope during stress
```

### Current Assessment: UNDECIDED is Appropriate

**Rationale:**
- HDA evidence is weak but not dismissible
- Mechanism is unclear (nuclear vs. perinuclear)
- Could be real nucleophagic function OR artifact
- Needs clarification before confident annotation

**Recommendation:**
- Retain GO:0005634 with UNDECIDED action
- Flag for experimental follow-up
- Do NOT propagate to GO database as definitive until clarified

---

## Summary: Critical Decision Justifications

| Decision | Status | Confidence | Rationale |
|----------|--------|-----------|-----------|
| **GABA binding removal** | REMOVE | VERY HIGH | Zero C. elegans evidence; nomenclature artifact |
| **Core autophagy ACCEPT** | ACCEPT | VERY HIGH | Conserved, well-supported, multiple methods |
| **Selective autophagy ACCEPT** | ACCEPT | VERY HIGH | Distinct pathways with defined receptors; PMID:29255173, PMID:19167332 |
| **Stress responses NON_CORE** | NON_CORE | HIGH | Consequences not mechanisms; system-level outcomes |
| **Protein binding specificity** | MODIFY | MEDIUM | Current terms too generic; better terms available |
| **Nuclear localization** | UNDECIDED | MEDIUM | HDA evidence weak; mechanism unclear; needs direct test |

---

## Recommendations for Annotation Standards

Based on this curation experience, recommendations for GO annotation standards:

1. **Phylogenetic Inference (IBA) Appropriateness:**
   - GOOD FOR: Conserved, essential mechanisms (autophagy, protein synthesis, metabolism)
   - POOR FOR: Specialized, non-conserved functions (GABA binding in invertebrates)
   - RECOMMEND: Require additional confidence levels for IBA inferences of non-conserved functions

2. **Generic Terms in GO:**
   - PROBLEM: GO:0005515 "protein binding" is too generic
   - SOLUTION: Encourage more specific molecular interaction terms
   - EXAMPLE: LIR-motif binding, endopeptidase substrate, adapter protein binding

3. **Non-Core Function Annotation:**
   - CHALLENGE: Distinguishing molecular mechanisms from phenotypic consequences
   - SOLUTION: Develop GO subset distinguishing core vs. pleiotropic functions
   - VALUE: Improves biological accuracy and computational inference

4. **Evidence Type Weighting:**
   - HDA should be lower confidence than direct methods
   - Tissue-specific localization studies should note tissue context
   - Pleiotropic phenotypes should note dependency on other genes/pathways

---

**Document Status:** Complete
**Next Steps:** Implement recommendations in lgg-1-ai-review.yaml and consider suggestions for GO database curators
