---
title: "Ferroptosis: Iron-Dependent Lipid-Peroxidation Cell Death"
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

# Ferroptosis: Iron-Dependent Lipid-Peroxidation Cell Death

An evolved, programmed cell-death process — not a pathological accident

**Chris Mungall | AI-Assisted Gene Review**

2026-06-22

---

## Why Ferroptosis?

- A form of **regulated cell death** driven by **iron-dependent peroxidation of
  PUFA-containing membrane phospholipids** — ending in membrane rupture.
- Mechanistically **distinct** from apoptosis, necroptosis, and pyroptosis:
  **no caspase cascade, no dedicated executioner enzyme.**
- In GO it is a **programmed process** ([GO:0097707](http://purl.obolibrary.org/obo/GO_0097707)),
  so it should be modelled as an **evolved program**, not as damage.
- The underlying chemistry (iron + O₂ + PUFA membranes) is **ancient and
  conserved**; ferroptosis-like death is reported in plants, fungi, and protozoa.
- Major therapeutic interest in **cancer** (induce it) and **neurodegeneration /
  ischemia–reperfusion** (block it).

---

## Key Biology / Mechanism

1. **PUFAs** are esterified into membrane phospholipids (ACSL4 → LPCAT3),
   creating the oxidisable substrate.
2. **Labile iron** (from TFRC import, NCOA4 ferritinophagy) catalyses radical
   chemistry and feeds lipoxygenases.
3. **Lipid peroxidation** generates phospholipid hydroperoxides (PL-OOH).
4. **Defense systems** detoxify PL-OOH or quench radicals.
5. When defenses are **overwhelmed**, propagating radicals **rupture the
   membrane** → cell death.

The defining feature is the **balance** between drivers and several independent
defense arms — not a linear cascade.

---

## A Network, Not a Linear Pathway

- **Drivers** (set the substrate + catalyst):
  - PUFA-phospholipid supply — **ACSL4**, **LPCAT3** (and **FADS1**, **ELOVL5**)
  - Labile-iron supply — **TFRC**, **NCOA4** (vs. protective **FTH1**, **SLC40A1**)
- **One execution node:** iron-catalysed PUFA-PL peroxidation → rupture.
- **Four independent suppressor arms**, each a parallel *negative regulator*:
  - **GPX4–glutathione** (canonical)
  - **FSP1 (AIFM2)–CoQ10**
  - **DHODH–CoQ10** (mitochondrial)
  - **GCH1–BH4** (tetrahydrobiopterin)
- The **redundancy** of the defenses is the scientifically important structure.

---

## Defense Arm 1: GPX4–Glutathione (Canonical)

| Gene | UniProt | Function |
|------|---------|----------|
| SLC7A11 | Q9UPY5 | Cystine/glutamate antiporter (xCT) — cysteine supply |
| SLC3A2 | P08195 | xCT chaperone partner (4F2hc) |
| GCLC | P48506 | Rate-limiting glutathione synthesis |
| GSS | P48637 | Glutathione synthase |
| GPX4 | P36969 | **Reduces phospholipid hydroperoxides** — central suppressor |

GPX4 inhibition (e.g. RSL3) is the canonical way to **trigger** ferroptosis.

---

## Defense Arms 2–4: Parallel & Redundant

| Arm | Gene | UniProt | Mechanism |
|-----|------|---------|-----------|
| FSP1–CoQ10 | AIFM2 | Q9BRQ8 | Regenerates ubiquinol (radical trap), GPX4-independent |
| DHODH–CoQ10 | DHODH | Q02127 | Reduces CoQ in mitochondrial inner membrane |
| GCH1–BH4 | GCH1 | P30793 | Rate-limiting BH4 (radical-trapping antioxidant) |
| GCH1–BH4 | PTS | Q03393 | BH4 synthesis |
| GCH1–BH4 | SPR | P35270 | Final-step BH4 synthesis |

Each arm **independently** suppresses execution — losing one is buffered by the others.

---

## Iron Supply & Regulatory Layer

**Iron (sets the threshold):**

| Gene | UniProt | Role |
|------|---------|------|
| TFRC | P02786 | Iron import — sensitizing |
| NCOA4 | Q13772 | Ferritinophagy — releases iron, sensitizing |
| FTH1 | P02794 | Ferritin storage — protective |
| SLC40A1 | Q9NP59 | Iron export — protective |

**Transcriptional set-point:** **NFE2L2** (Q16236, NRF2) induces defenses;
**KEAP1** (Q14145) represses NRF2; **ATF4** (P18848) induces SLC7A11;
**TP53** (P04637) is context-dependent (canonically represses SLC7A11).

---

## Key Recent Discoveries (2019+)

1. **FSP1–CoQ10 pathway** (Nature 2019, PMID:31634900 / PMID:31634899) —
   GPX4-independent suppression via ubiquinol regeneration.
2. **DHODH in mitochondria** (Nature 2021) — mitochondrial CoQ-based defense.
3. **GCH1/BH4 pathway** (2020) — third parallel radical-trapping antioxidant axis.
4. **Membrane lipid remodelling** — specific PUFA-phospholipids (esp. PE) as the
   critical substrate.

These discoveries reframed ferroptosis from "GPX4 failure" to a
**multi-arm, redundant defense network**.

---

## The Approach: AI Gene Review

- Systematically review existing **GO annotations** for each pathway gene using
  strict GO guidelines.
- Synthesize with **literature** evidence and **bioinformatic** inference.
- Distinguish **core functions** from over-annotation (e.g. generic "cell death"
  terms with only indirect support).
- Capture the integrated mechanism as a validated, decomposable
  **[ferroptosis module](../../../modules/ferroptosis.html)** grounded to UniProt + GO.
- Status: **22 human genes reviewed and validated.**

---

## Conclusions & Future Directions

- Ferroptosis: iron-dependent regulated cell death by **PUFA-phospholipid
  peroxidation** — best modelled as **one execution node with redundant
  suppressor arms**.
- Curation target: **22 genes** across drivers, four defense arms, and regulators.
- An **evolved, conserved program** — appropriate to model as biology, not pathology.
- Next steps:
  - [ ] Fold in 2023–2026 papers (MBOAT1/2, new suppressors)
  - [ ] Ontology-gap assessment for the parallel-defense structure
  - [ ] Cross-link the module to production GO-CAM models
- Parallels the **[Cuproptosis](../../CUPROPTOSIS.html)** project as a
  metal-dependent regulated-cell-death program.
