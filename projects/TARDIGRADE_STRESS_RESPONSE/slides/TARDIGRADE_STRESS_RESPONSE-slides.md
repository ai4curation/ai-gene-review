---
title: "Tardigrade Stress Response Protein Curation"
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

# Tardigrade Stress Response Protein Curation

### How a "water bear" survives near-total desiccation — and what its proteome teaches us about annotation pitfalls

Chris Mungall | AI-Assisted Gene Review

2026-06-22

---

## The Problem: Surviving the Impossible

- *Ramazzottius varieornatus* (RAMVA) is an extremotolerant tardigrade
- It survives **near-complete desiccation** by entering a dormant **tun state**
- The same machinery confers resistance to **ionizing radiation, extreme temperatures, vacuum, and high pressure**
- During desiccation, **massive ROS accumulation** damages biomolecules in every cellular compartment
- Radiation tolerance is likely a *byproduct* of desiccation tolerance — both stresses generate hydroxyl radicals

**Goal:** curate the complete reviewed (Swiss-Prot) stress-response proteome of RAMVA

---

## Key Biology: A Compartment-Partitioned Defense

Tardigrade-unique intrinsically disordered proteins (TDPs) each protect a different compartment:

| Family | Compartment | Role |
|--------|-------------|------|
| **Dsup** | Nucleus/chromatin | Shields DNA from hydroxyl radicals via nucleosome binding |
| **CAHS** | Cytosol | Form protective hydrogels/filaments upon desiccation |
| **SAHS** | Extracellular | Protect secreted components; FABP-like fold |
| **MAHS** | Mitochondria | Protect mitochondrial function |
| **RvLEAM** | Mitochondria | LEA protein; shared with plants/nematodes |

Plus conventional ROS-scavenging enzymes (Cu/Zn-SODs, Mn-SOD).

---

## Two Unifying Themes

**Intrinsic disorder**
- Most TDPs are intrinsically disordered proteins (IDPs)
- Disorder enables flexible, multivalent interactions (chromatin for Dsup, cytoskeleton for CAHS)
- Enables reversible phase transitions (CAHS hydrogel formation) that physically stabilize structures during water loss

**Evolutionary uniqueness**
- CAHS, SAHS, MAHS, Dsup are **tardigrade-specific** — no homologs outside the phylum
- RvLEAM is the exception: LEA proteins occur in plants/nematodes — convergent evolution of desiccation tolerance

---

## The Approach: AI-Assisted Gene Review

- Curate each Swiss-Prot protein against existing GOA annotations using GO guidelines
- For each annotation: **ACCEPT / MODIFY / REMOVE / NEW** with literature + bioinformatic support
- Deep research (falcon) synthesized per gene; reviewer adjudication on top
- Where annotations were missing or wrong, propose **NEW** terms or corrections
- Custom **bioinformatics pipeline** (sequence conservation + PROSITE motifs + Pfam) to test catalytic claims

---

## Finding 1: A Systematic Annotation Gap

- The most consistent gap across **all TDPs**: absence of **GO:0009269 (response to desiccation)**
- This is *the* core biological process for the entire family
- Proposed as **NEW for every gene** in the project
- **Response to osmotic stress** proposed for several genes with gain-of-function data (MAHS, RvLEAM expressed in human cells)

> The defining function of the whole protein family was simply not in the database.

---

## Finding 2: The Nuclear Shield — Dsup

- **Dsup** (P0DOW4): nucleosome-binding chromatin shield
- Protects against both **X-ray and H2O2-induced** DNA damage via the *same* nucleosome-shielding mechanism
- Curation nuance: GO:0003677 (DNA binding) first proposed for MODIFY → nucleosome binding
- Corrected to **ACCEPT**: GO:0031491 (nucleosome binding) is NOT a child of DNA binding (it sits under chromatin binding) — both are valid independent MF annotations
- Key refs: Hashimoto et al. 2016 (PMID:27649274); Chavez et al. 2019 (PMID:31571581)

---

## Finding 3: The SOD Paralog Family Is Half Broken

RAMVA has ~10 Cu/Zn-SOD paralogs. Bioinformatic analysis (sequence + PROSITE PS00087 + Pfam):

| Verdict | Count | Examples |
|---------|-------|----------|
| Confirmed pseudoenzyme | 1 | RvSOD15 / RvY_13070 |
| Probably impaired | 3 | RvY_00650, RvY_03757, RvY_17310 |
| Copper chaperone (not a SOD) | 1 | RvY_15948 (CCS homolog) |
| Likely functional canonical SOD | 4 | RvY_00651, RvY_03754, RvY_09480, RvY_10893 |

At least **4 of 9** Cu/Zn-SOD-family paralogs appear to have lost/impaired canonical SOD activity.

---

## Finding 3 (cont.): RvSOD15 the Pseudoenzyme

- Crystal structure (PMID:37358501) shows **Val87 replaces the catalytic His** copper ligand
- Confirmed structurally → its **4 SOD-activity annotations are OVER-ANNOTATED**
- Three more paralogs keep all four catalytic Cu histidines at the residue level, **yet fail PROSITE PS00087** (N-terminal Cu coordination signature)
- By analogy with the failed V87H rescue in RvSOD15 (loop dynamics), these are likely impaired too
- Validates Sim & Inoue (2023): "some other RvSODs are also unusual SODs" — now with a precise count

---

## Finding 4: Annotation Propagation Errors Are Systematic

- Automated pipelines (**InterPro2GO, EC2GO, UniRule, ARBA**) assigned GO:0004784 (SOD activity) to **ALL** Cu/Zn-SOD-family proteins by Pfam membership alone
- No check of catalytic-residue conservation or motif integrity
- Canonical **"annotation propagation by family membership"** failure — documented for ≥4 of 9 paralogs
- **RvY_01767 (Mn-SOD)** also got a spurious "respiratory chain complex" annotation from an ARBA rule (it is a soluble matrix protein) → 1 REMOVE

---

## Finding 5: SAHS Proteins Have FABP-Like Folds

- **SAHS1** and **SAHS2** adopt beta-barrel folds homologous to fatty acid-binding proteins
- Crystal structures available (SAHS1: Fukuda et al. 2017, PMID:28703282)
- Lipid binding was annotated for SAHS1 but **not** SAHS2 → proposed to add for SAHS2
- Illustrates how structural homology informs missing molecular-function annotations

---

## What Makes Curation Hard Here

- **Tardigrade-unique proteins** have no homologs → little transferable annotation; the core process (desiccation response) was simply absent
- **Pseudoenzymes hide in plain sight**: full catalytic residues present at sequence level can still be non-functional (loop/motif context matters)
- **Family-membership propagation** systematically over-annotates enzymatic activity
- **GO graph subtleties**: nucleosome binding vs DNA binding placement changes the right action
- Disorder + phase behavior are biologically central but awkward to capture in current GO terms

---

## Conclusions & Status

- Full reviewed RAMVA stress proteome curated: **Dsup, 3 CAHS, 2 SAHS, MAHS, RvLEAM, 10 Cu/Zn-SODs, 1 Mn-SOD**
- **GO:0009269 (response to desiccation)** proposed as the unifying NEW term across all TDPs
- A reusable SOD bioinformatics pipeline (`analyze_sods.py`, `check_prosite.py`) revealed ~half the SOD expansion may be non-catalytic
- "Gene duplication = more antioxidant capacity" is only **partially** correct

**Future:** capture intrinsic-disorder/phase-transition function in GO; extend pseudoenzyme screening to the broader paralog set; experimental validation of impaired-SOD predictions.
