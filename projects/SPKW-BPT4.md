# SPKW Bacteriophage T4 (BPT4) Subproject

**Parent project:** [SPKW.md](SPKW.md)

## Overview

Bacteriophages present a unique test case for SPKW annotation quality. Many GO terms relating to host-pathogen interactions were designed for eukaryotic pathogens (viruses, bacteria, fungi) infecting eukaryotic hosts. When these terms are applied to bacteriophages (which infect bacteria), semantic mismatches can occur.

**Key question**: Do GO terms for "immune suppression" and "defense response" apply when the host is a bacterium that lacks an immune system in the GO sense?

## Statistics (2026-01-31)

| Metric | Count |
|--------|-------|
| T4 genes in UniProt | ~300 |
| SPKW annotations (GO_REF:0000043) | ~150 |
| Genes with potentially problematic immune/defense terms | 3+ |

## Problematic Term Categories

1. **Eukaryotic immune terms applied to phage-bacteria interactions**:
   - GO:0052170 (symbiont-mediated suppression of host innate immune response)
   - GO:0052031 (symbiont-mediated perturbation of host defense response)
   - GO:0042742 (defense response to bacterium)

2. **Antibiotic response terms applied to phage enzymes**:
   - GO:0046677 (response to antibiotic)
   - GO:0031427 (response to methotrexate)

## Status

- [x] Initial exploration complete (2026-01-31)
- [x] Deep research for all 3 genes (2026-01-31)
- [x] Annotation review complete for all 3 genes (2026-01-31)
- [x] Write-up complete (2026-01-31)

---

## Case Studies (3 genes reviewed)

### Case 1: DAM - DNA Adenine Methyltransferase

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

### Case 2: E - T4 Lysozyme

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

### Case 3: frd - Dihydrofolate Reductase

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

## T4 Bacteriophage Over-Annotation Patterns

| Pattern | Example | Frequency | Severity |
|---------|---------|-----------|----------|
| **Eukaryotic immune terms for phage** | DAM (innate immune suppression) | High | **Critical** |
| **Defense/offense inversion** | E lysozyme (defense response) | Medium | High |
| **Drug target as drug response** | frd (antibiotic response) | Medium | Medium |

## Summary: Result 3/3 (100%) problematic annotations

All three T4 phage genes with SPKW-unique "immune" or "defense" annotations were over-annotated:

| Gene | UniProt | Problematic Annotation | Action | Correct Term |
|------|---------|------------------------|--------|--------------|
| DAM | P04392 | symbiont-mediated suppression of host innate immune response | **REMOVE** | GO:0099018 (R-M system evasion) |
| DAM | P04392 | symbiont-mediated perturbation of host defense response | **REMOVE** | GO:0099018 (R-M system evasion) |
| E | P00720 | defense response to bacterium | **REMOVE** | GO:0044659 (viral release by cytolysis) |
| frd | P04382 | response to antibiotic | **REMOVE** | (MF terms sufficient) |
| frd | P04382 | response to methotrexate | **REMOVE** | (MF terms sufficient) |

## Key Lessons from Bacteriophage Analysis

1. **GO terms encode eukaryote-centric biology**: Terms like "innate immune response" and "defense response" assume eukaryotic biology. Bacterial anti-phage systems (R-M, CRISPR) require different terminology.

2. **Host-pathogen terms need taxonomic context**: A term describing how a virus evades mammalian immunity should not be applied to a phage evading bacterial restriction.

3. **UniProt keywords are eukaryote-biased**: Keywords like "Inhibition of host innate immune response by virus" were created for eukaryotic viruses and don't translate to bacteriophages.

4. **"Defense" depends on perspective**: From the phage's perspective, lysozyme enables reproduction. From the bacterium's perspective, it's attack. Neither is "defense response to bacterium."

5. **Drug target ≠ drug response**: An enzyme being inhibited by an antibiotic doesn't mean the organism "responds" to that antibiotic in a biological process sense.

## Recommendations for Phage/Virus SPKW Curation

1. **Create phage-specific term mappings**: Keywords about host-pathogen interactions should map to different GO terms for phages vs. eukaryotic viruses

2. **Review all "innate immune" annotations on phage proteins**: These are likely systematically incorrect

3. **Distinguish R-M evasion from immune suppression**: GO:0099018 exists specifically for phage-bacteria interactions

4. **Validate "antibiotic resistance" claims**: Being a drug target does not equal conferring resistance, especially for phage enzymes

## Comparison: All Organisms Analyzed

| Organism | Domain | Over-Annotation Rate | Main Patterns |
|----------|--------|---------------------|---------------|
| Human | Eukarya | 80-100% | Process conflation |
| S. pombe | Eukarya | 100% (ATG-meiosis) | Support process conflation |
| D. melanogaster | Eukarya | 50% | Mixed |
| P. putida | Bacteria | 25% | RT defense keyword |
| Arabidopsis | Eukarya | 75% | Subclade divergence |
| **T4 Phage** | **Virus** | **100%** | **Eukaryote-centric terms** |

## Review Files Location

```
genes/BPT4/
├── DAM/DAM-ai-review.yaml   (REMOVE: immune suppression - bacteria lack innate immunity)
├── E/E-ai-review.yaml       (REMOVE: defense response - phage is attacker not defender)
└── frd/frd-ai-review.yaml   (REMOVE: antibiotic response - drug target ≠ response)
```
