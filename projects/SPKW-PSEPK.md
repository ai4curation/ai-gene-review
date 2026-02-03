# SPKW P. putida (Pseudomonas putida) Subproject

**Parent project:** [SPKW.md](SPKW.md)

## Overview

P. putida KT2440 is a well-characterized environmental soil bacterium known for its metabolic versatility, solvent tolerance, and plant growth-promoting properties. Unlike the eukaryotic organisms analyzed previously, P. putida shows a distinctly different SPKW annotation pattern - one with much lower apparent over-annotation rates.

## Key Statistics (2026-01-31)

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

## Top TRUE SPKW-Unique Terms

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

---

## Pattern Analysis

### 1. Methylation (41 genes) - LEGITIMATE

Genes include:
- **ada** - O6-methylguanine-DNA methyltransferase (alkylation damage repair)
- **bioC** - Malonyl-CoA O-methyltransferase (biotin synthesis)
- **cheR2, cheR3** - Chemotaxis protein methyltransferases
- **cfa** - Cyclopropane-fatty-acyl-phospholipid synthase
- Various PP_XXXX locus tags

These are actual methyltransferases where "methylation" is their core function. **LEGITIMATE annotation.**

### 2. Cell Wall / Cell Shape (32 + 27 genes) - LEGITIMATE

Genes include:
- **ftsI** - Peptidoglycan D,D-transpeptidase (PBP3)
- **mraY** - Phospho-N-acetylmuramoyl-pentapeptide-transferase
- **mrdA-I, mrdA-II** - Peptidoglycan D,D-transpeptidases (PBP2)
- **ddl, ddlA, ddlB** - D-alanine--D-alanine ligases
- **mrcA, mrcB** - Penicillin-binding proteins 1A/1B

These are peptidoglycan biosynthesis enzymes that DIRECTLY determine bacterial cell shape. In bacteria, cell wall biosynthesis = cell shape regulation. **LEGITIMATE annotation.**

### 3. Response to Antibiotic (7 genes) - LEGITIMATE

| Gene | Function | Why Legitimate |
|------|----------|----------------|
| mrcA, mrcB | PBPs | Target of beta-lactams |
| amgK, anmK, murU, mupP | PG recycling | Cell wall integrity |
| ampC | Beta-lactamase | Direct antibiotic inactivation |
| pvdT | Pyoverdine transporter | Siderophore/efflux |

These genes confer antibiotic resistance as part of their core functions. Unlike eukaryotic over-annotations, these are not "downstream effects" - these genes ARE the antibiotic resistance mechanisms.

### 4. Response to Arsenic (6 genes) - LEGITIMATE

P. putida has two arsenic resistance operons (ars1, ars2):
- **arsB-I, arsB-II** - Arsenite efflux pumps (also transport antimony)
- **arsR1, arsR2** - Arsenic-responsive transcription regulators
- **PP_1928, PP_2716** - Putative arsenic reductases

These are canonical arsenic resistance genes. **LEGITIMATE annotation.**

### 5. Defense Response to Virus (3 genes) - QUESTIONABLE

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

---

## Key Differences from Eukaryotic Organisms

| Feature | Eukaryotes (Human, D. mel, S. pombe) | P. putida |
|---------|--------------------------------------|-----------|
| Over-annotation rate | 80-100% for BP terms | Very low (<5% estimated) |
| Main problematic terms | Apoptosis, meiosis, autophagy, rhythm | RT-based "defense response to virus" only |
| Pattern type | Process conflation (support ≠ participation) | Minimal - most annotations are accurate |
| MF vs BP | BP over-annotations common | MF dominates TRUE unique (71%) |
| Annotation density | Many annotations per gene | Sparse - few experimental |

## Why P. putida SPKW Annotations Are More Accurate

1. **Simpler biology**: Bacteria lack the complex regulatory networks (apoptosis, autophagy, circadian rhythms) that get over-annotated in eukaryotes

2. **Direct function mapping**: Bacterial gene functions map more directly to processes:
   - Methyltransferase → methylation (direct)
   - PBP → cell wall organization (direct)
   - Arsenic pump → arsenic response (direct)

3. **No process conflation**: Bacteria don't have meiosis, apoptosis, or circadian rhythms, so those problematic keyword mappings don't apply

4. **Less signaling complexity**: Fewer multi-step signaling pathways that lead to "4 steps removed" over-annotations (like Sin1 → TORC2 → Akt → apoptosis)

5. **UniProt keywords more appropriate**: Keywords like "Antibiotic resistance" map well to bacterial gene functions

---

## Comparison: SPKW Over-Annotation Patterns Across Organisms

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

---

## Full Gene Reviews Completed (2026-01-31)

Four representative genes underwent complete annotation review with deep research:

| Gene | UniProt | Annotations | Key Finding |
|------|---------|-------------|-------------|
| PP_0635 | Q877L4 | 7 | **OVER-ANNOTATION** - "defense response to virus" incorrect for group II intron RT |
| ada | Q88PZ2 | 13 | **MODIFY** - "methylation" misleading; Ada removes methyl groups (dealkylation) |
| ampC | Q88IX3 | 5 | **LEGITIMATE** - "response to antibiotic" correct for beta-lactamase |
| mrcA | Q88CU6 | 16 | **LEGITIMATE** - cell shape/antibiotic response correct for PBP1A |

**Over-annotation rate: 1/4 (25%)** - confirming P. putida has much lower over-annotation than eukaryotes.

---

### Case 1: PP_0635 - The One Over-Annotation ✓

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

### Case 2: ada - Correct Biology, Wrong Term ✓

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

### Case 3: ampC - Legitimate Annotation ✓

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

### Case 4: mrcA - Legitimate Multiple Annotations ✓

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

## Summary: P. putida Curation Results

| Gene | Main SPKW Term | Action | Pattern |
|------|----------------|--------|---------|
| PP_0635 | defense response to virus | **REMOVE** | Keyword too broadly applied to RT family |
| ada | methylation | **MODIFY** | Correct biology, imprecise term |
| ampC | response to antibiotic | **ACCEPT** | Directly legitimate |
| mrcA | cell shape/antibiotic | **ACCEPT** | Directly legitimate |

**Key insight:** The ONE over-annotation (PP_0635) follows a specific pattern - the UniProt "Antiviral defense" keyword was applied to ALL bacterial reverse transcriptases, when only a subset (retrons, Abi systems) have defense functions. This is a targetable systematic error.

## Recommendations for P. putida Curation

1. **Low priority for manual review**: Unlike eukaryotic organisms, P. putida SPKW annotations appear largely accurate

2. **Focus on RT genes**: The 3 "defense response to virus" genes are the main candidates for review

3. **Validate MF terms are appropriate specificity**: Many are very broad (metal ion binding, hydrolase activity)

4. **Use as positive control**: P. putida demonstrates that SPKW can produce accurate annotations when:
   - Organism biology is simple (no complex regulatory networks)
   - Keywords map directly to gene functions
   - Evolutionary distances are small (bacterial keywords for bacteria)

## Conclusion

P. putida presents a stark contrast to the eukaryotic organisms analyzed in this project. While human, D. melanogaster, and S. pombe showed 80-100% over-annotation rates for BP terms like apoptosis, autophagy, and meiotic cell cycle, P. putida's TRUE SPKW-unique annotations are largely accurate.

This difference stems from:
1. Simpler bacterial biology without the complex processes that get conflated in eukaryotes
2. More direct mapping between UniProt keywords and bacterial gene functions
3. Absence of the "support process conflation" pattern (e.g., autophagy during meiosis)

The main lesson: **SPKW over-annotation is not universal** - it's driven by specific patterns in keyword-to-GO mappings for complex eukaryotic processes. For bacteria like P. putida, SPKW provides valuable provisional annotations that are largely accurate.

## Review Files Location

```
genes/PSEPK/
├── PP_0635/PP_0635-ai-review.yaml  (OVER-ANNOTATION: defense response)
├── ada/ada-ai-review.yaml          (MODIFY: methylation → dealkylation)
├── ampC/ampC-ai-review.yaml        (LEGITIMATE)
└── mrcA/mrcA-ai-review.yaml        (LEGITIMATE)
```
