# SPKW D. melanogaster (Drosophila) Subproject

**Parent project:** [SPKW.md](SPKW.md)

## Overview

Analysis of TRUE SPKW-unique annotations in D. melanogaster using closure-based query.

## Key Statistics (2026-01-31)

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

## Top TRUE SPKW-Unique Terms

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

## Pattern Analysis

### 1. "Killing of cells of another organism" (GO:0031640) - LEGITIMATE

24 genes with this annotation are primarily:
- **Lysozymes** (LysB, LysD, LysE, LysP, LysS, LysX) - with "hydrolase activity, acting on glycosyl bonds"
- **Antimicrobial peptides** (Drosomycin, Metchnikowin, Baramicin)
- **Spätzle** (spz) - cytokine that activates Toll pathway

These are legitimate annotations for antimicrobial effectors.

### 2. Meiotic Cell Cycle (GO:0051321) - MIXED

Unlike S. pombe where ATG genes were wrongly annotated, D. mel meiotic annotations include:
- **GATOR1 complex** (Nprl2, Nprl3, Iml1) - These have EXPERIMENTAL evidence for germline/meiotic functions (PMID:25512509) alongside their TOR-regulation role
- **Cell division genes** (Bub3, Cdc37, cnn) - Potentially legitimate
- Some may still be over-annotations requiring case-by-case review

### 3. Apoptotic Process (GO:0006915) - NEEDS REVIEW

28 genes include:
- **Legitimate**: Buffy (Bcl-2 family), HtrA2, Opa1, ASPP, Daxx
- **Questionable**: Akt, Pdk1, Lkb1 (growth signaling kinases)
- **Cross-talk**: BI-1 (has both apoptosis AND autophagy annotations)

## Key Differences from S. pombe

| Pattern | S. pombe | D. melanogaster |
|---------|----------|-----------------|
| Meiotic cell cycle | ATG genes over-annotated (NO experimental meiotic evidence) | GATOR1 complex has experimental meiotic evidence |
| Organism context | Unicellular - meiosis = sporulation | Multicellular - germline development |
| Main issue | Autophagy conflated with meiosis | Less clear-cut; some legitimate meiotic functions |

---

## Detailed Case Studies (Full Reviews Completed 2026-01-31)

### Case 1: Buffy - Regulation vs Participation Conflation ✓

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

### Case 2: Ced-12 - Legitimate SPKW Contribution ✓

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

### Case 3: Sin1 - Over-annotation via Signaling Pathway ✓

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

### Case 4: LysB - Correct Function, Wrong Context ✓

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

## Categories of SPKW-Unique Annotations

| Category | Description | Example | Action |
|----------|-------------|---------|--------|
| **Regulation conflation** | Annotated to process when evidence is for regulation | Buffy | Consider MODIFY to regulation term |
| **Legitimate unique** | SPKW captures biology missing from experimental data | Ced-12 | KEEP - valuable contribution |
| **Signaling over-extension** | Indirect pathway connection | Sin1 | Consider REMOVE or very broad term |
| **Support process conflation** | Process X active during process Y | S. pombe ATG | REMOVE |
| **Correct but uninformative** | Very broad terms (metal ion binding) | CG genes | Keep but low priority |

---

## Lessons Learned from D. melanogaster Analysis

1. **Organism biology matters**: The same GO term can have different validity in different organisms. Meiotic annotations in unicellular yeasts (sporulation) differ fundamentally from multicellular organisms (germline development).

2. **SPKW can capture legitimate unique biology**: The "killing of cells of another organism" annotations for lysozymes and AMPs are appropriate and represent genuine SPKW contributions.

3. **MF terms dominate TRUE SPKW-unique**: 61% of unique contributions are Molecular Function, often very broad terms (metal ion binding, zinc ion binding). These may be accurate but uninformative.

4. **GATOR1 is a special case**: These genes regulate both TOR signaling (autophagy) AND have bona fide germline functions. The meiotic annotation may be appropriate here, unlike S. pombe ATG genes.

5. **Apoptosis annotations need case-by-case review**: Unlike the systematic ATG over-annotation in S. pombe, D. mel apoptosis includes a mix of legitimate (Bcl-2 family) and questionable (growth kinases) annotations.

---

## Comparative Summary: S. pombe vs D. melanogaster

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

## Recommendations for SPKW Curation

1. **Use closure-based queries**: Reduces false positives by 70%+ in well-curated organisms

2. **Check experimental evidence before removing**: D. mel GATOR1 genes have experimental meiotic evidence that S. pombe ATG genes lack

3. **Consider organism biology**: Unicellular vs multicellular organisms have fundamentally different meiotic biology

4. **Prioritize patterns over individual genes**: Finding systematic over-annotation patterns (like ATG-meiosis in yeast) is more impactful than reviewing individual genes

5. **Some SPKW annotations are legitimate**: Don't assume all SPKW-unique = over-annotation. Lysozymes and AMPs in D. mel are correctly annotated.

6. **Check for regulation vs participation**: SPKW often conflates regulatory roles with process membership - consider if a "regulation of X" term would be more appropriate

7. **Value novel functional insights**: Cases like Ced-12 where SPKW captures known biology that experimental annotations miss are valuable contributions to GO

## Review Files Location

```
genes/DROME/
├── Buffy/Buffy-ai-review.yaml
├── Ced-12/Ced-12-ai-review.yaml
├── Sin1/Sin1-ai-review.yaml
└── LysB/LysB-ai-review.yaml
```
