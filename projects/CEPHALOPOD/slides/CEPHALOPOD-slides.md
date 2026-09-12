---
title: "Cephalopod Neuro Gene Reviews"
marp: true
theme: default
paginate: true
backgroundColor: #fff
style: |
  section { font-size: 24px; }
  h1 { color: #2c3e50; }
  h2 { color: #34495e; }
  table { font-size: 18px; }
  section.lead h1 { font-size: 48px; }
---

<!-- _class: lead -->

# Cephalopod Neuro Gene Reviews

### Curating the largest invertebrate brains out of an annotation desert

Chris Mungall | AI-Assisted Gene Review
2026-06-22

---

## The problem: an annotation desert

- Cephalopods have the **largest invertebrate nervous systems**, adaptive camouflage, and remarkable cognition
- Yet only **27 experimental GO annotations** exist across all cephalopod species
- That is **0.008%** of 333,921 total Cephalopoda annotations
- Only **11 gene products across 7 species** have *any* experimental GO evidence

> Almost everything we "know" about cephalopod genes comes from electronic inference, not curation.

---

## How thin is the evidence?

GO annotation status for Cephalopoda (taxon:6605), QuickGO May 2026:

| Evidence Type | Count | % |
|---------------|-------|---|
| IEA (InterPro/HAMAP) | 149,500 | 44.8% |
| IBA (TreeGrafter) | 101,488 | 30.4% |
| IEA (UniProt/UniRule) | 53,446 | 16.0% |
| ISS | 50 | 0.01% |
| **IDA** | **19** | **0.006%** |
| **EXP** | **4** | **0.001%** |
| **IEP** | **2** | **0.001%** |

~99% is electronic transfer; the experimental core is vanishingly small.

---

## Key biology: why cephalopods are special

- **Protocadherin expansion**: >160 genes in octopus (vs ~70 in mammals); neural-enriched
- **C2H2 zinc finger expansion**: vertebrate-convergent gene family amplification
- **Extensive A-to-I RNA editing**: >57,000 recoding sites; temperature-responsive
- **Taxonomically restricted genes**: hundreds of cephalopod-specific genes in skin, suckers, nervous system
- **Horizontal gene transfer**: 12 bacterial HGT genes in *O. bimaculoides*, including immune defense

These features make naive homology-based annotation systematically unreliable.

---

## The approach

- Apply the **ai-gene-review framework** to experimentally characterized cephalopod genes
- Synthesize **literature deep research + computational predictions + bioinformatics**
- Review each existing annotation against GO guidelines: ACCEPT / MODIFY / REMOVE / over-annotated
- Propose **new annotations** where strong evidence exists but GO is silent
- Integrate **scRNA-seq cell-type context** (MF + cell type + cell role → inferred BP)
- Organism dirs follow UniProt mnemonics: OCTVU, OCTBM, DORPE, SEPOF, ...

---

## Status: 16 genes reviewed across 7 species

| Gene | Species | UniProt | Highlight |
|------|---------|---------|-----------|
| DDO | OCTVU | A0A7E6FSU6 | D-Asp in retina at 2.30 umol/g |
| AP180 | DORPE | Q9U6M6 | Spurious "locomotion" removed |
| cpx | DORPE | Q95PA1 | Dual clamp/activator (IPI) |
| CTR1 | OCTVU | Q7YW31 | "Vasopressin receptor" corrected |
| RHO | SEPOF | O16005 | PLC-activating opsin; dermal photoreception |
| CRT1 | OCTBM | A0A0L8FVQ9 | Contact chemosensation, feeding |
| sympp | STHOU | C6KYS2 | Novel bioluminescence luciferase |
| OCTS1 | OCTVU | P27013 | GST over-annotated (1/700 kcat) |

*(8 more: OPR, FMRFa, khc, CTR2, TDO, SERT, reflectin, ADAR2)*

---

## Finding 1: systematic IEA errors exposed

- **Vasopressin-receptor mis-annotation is pervasive**: CTR1, CTR2, OPR all carried GO:0005000 (vasopressin receptor activity) from IEA — **none bind vasopressin**. Correct term: GO:0008188 (neuropeptide receptor activity)
- **ARBA false positives for non-model organisms**: kinesin tagged "locomotion", "nuclear migration", "isomerase activity"; AP180 tagged "locomotion", "Golgi apparatus"
- **tRNA vs RNA deaminase confusion**: ADAR2 mis-annotated with tRNA-specific adenosine deaminase activity (ADAT function), via TreeGrafter

---

## Finding 2: ancestral-function over-annotation

**S-crystallin (OCTS1, P27013)** — a textbook case:

- Retains GO:0004364 (glutathione transferase activity) from sequence homology
- But has **1/700 the catalytic efficiency** of real GST
- Binds GSH **43-fold tighter** than GST-sigma — for **structural stabilization** (raises Tm by ~7 C), not catalysis
- PDB 5B7C; assembles into a colloidal gel for the lens

Sequence homology preserved; the *function* diverged. The annotation should not.

---

## Finding 3: novel biology captured for the first time

- **Dermal photoreception**: rhodopsin in skin chromatophores mediates LACE (light-activated chromatophore expansion). Best term: **GO:0030265** (PLC-activating opsin-mediated signaling) — child of *both* GPCR signaling and phototransduction
- **Contact chemosensation**: CRT1, a cephalopod-specific channel (no homologs outside Cephalopoda), evolved from nAChRs via retrotransposition (26 intronless genes on one chromosome). Bacterial metabolites on eggs activate CRT1 to drive **brooding behavior** — a microbiome-receptor-behavior circuit (Sepela 2025, *Cell*)

---

## Finding 4: RNA editing tunes protein function

- **Kinesin (khc, DORPE)** velocities are tissue-specific via RNA editing:
  - optic lobe variants ~520 nm/s; unedited ~587 nm/s; stellate ganglion ~620-674 nm/s
  - **37 editing sites in the motor domain alone**
  - the most direct demonstration of RNA editing tuning protein properties in any organism
- **Complexin (cpx)** has a dual role: N-terminal domain (residues 1-26) promotes fusion while the central helix clamps spontaneous release — first shown at the squid giant synapse

---

## Finding 5: filling the desert

- Well-characterized genes with near-zero GO coverage:
  - **FMRFa** (2 annotations), **SLC6A4/SERT** (0), **reflectin** (0)
- The project proposed **19 annotations across these 3 genes alone**
- Deep research surfaced biology missing from initial reviews:
  - **DDO** has a visual-system role: D-aspartate at 2.30 umol/g in retina (PMID:15491279)
  - **Symplectin** may be bifunctional: conserved pantetheinase triad (E60-K163-C196); unique cation specificity K+ > Rb+ > Na+ (not Ca2+)
  - **OPR** is an antidiuretic-hormone receptor (octopressin lowers hemolymph osmolarity)

---

## scRNA-seq x function: inferring biological process

Logic: gene G has MF **F** + is a marker for cell type **C** + C has role **R** → G involved in **BP = F in R context**

| Gene | New BP | Evidence | Species |
|------|--------|---------|---------|
| RHO | Dermal light sensing / body patterning | IEP+IDA | *O. bimaculoides* |
| CRT1 | Contact chemosensation / prey capture | IEP+IDA | *O. bimaculoides* |
| Hemocyanin | Innate immune defense | IDA (AMP) | *N. pompilius* |
| FMRFa | Visual circuit neuromodulation | IEP | *O. bimaculoides* |

Yield is small: a **Swiss-Prot bottleneck** (~35 useful entries) and cross-species mapping limit reach.

---

## Why curation here is hard

1. **Near-zero experimental GO** — only 27 annotations; most curation is necessarily *novel*
2. **Fragmented UniProt** — *E. scolopes* has **0** Swiss-Prot entries despite being a major model
3. **No nomenclature committee** — gene names inconsistent across species
4. **Multi-species biology** — same gene studied in different species; per-species vs consolidated reviews
5. **Large genomes** — 2.7-5.7 Gb, 42-71% repeats; gene counts vary 2-fold between methods
6. **Limited reverse genetics** — only **2 CRISPR papers** exist (*D. pealeii* TDO; *E. berryi* TDO+IDO)

---

## Conclusions & future directions

- AI gene review converts an annotation desert into curated, evidence-backed function statements
- It both **fixes systematic IEA/ARBA errors** and **captures genuinely novel cephalopod biology** (dermal photoreception, contact chemosensation, RNA-edited motors)
- **Status**: 16 genes / 7 species reviewed; project IN_PROGRESS (FLAGSHIP)
- **Next**:
  - Request Swiss-Prot review of *O. bimaculoides* TrEMBL markers (dat, vacht, nos, tyrbh)
  - Build **GO-CAM models** for the visual and chromatophore systems with cell-type context
  - Leverage expanding *E. berryi* CRISPR knockouts for functional inference

---

<!-- _class: lead -->

# Thank you

Project CEPHALOPOD — AI Gene Review for Cephalopod Genes
Chris Mungall | 2026-06-22
