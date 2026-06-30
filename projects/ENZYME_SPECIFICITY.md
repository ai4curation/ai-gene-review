---
title: "Enzyme Specificity Project"
maturity: COMPLETE
tags: [PIPELINE, FLAGSHIP]
---

# Enzyme Specificity Project

## Overview

This project tracks genes where GO annotations fail to capture the correct enzyme specificity - either:
1. **Too narrow**: Annotation to one substrate when enzyme has broader specificity
2. **Too broad**: Generic enzyme class when specific activity is known
3. **Wrong reaction**: Incorrect reaction type based on domain classification

Enzyme specificity is crucial for accurate functional annotation. Misannotated specificity can:
- Mislead metabolic pathway reconstruction
- Cause errors in drug target identification
- Propagate incorrect annotations via IBA

**Source**: Presented at Gene Ontology Consortium Meeting, October 2025, Cambridge UK. See [ai4curation/ai-gene-review](https://github.com/ai4curation/ai-gene-review).

## Categories

### 1. Substrate Specificity Errors

**The Problem**: Enzyme annotated to specific substrate when it has broader or different specificity.

**Example - LPL1 (C. albicans)**:
- Annotated: `GO:0004622` (phosphatidylcholine lysophospholipase activity)
- Actual: Phospholipase B with three distinct activities:
  1. sn-1/sn-2 fatty acid ester hydrolase
  2. Lysophospholipase activity (on ALL glycerophospholipids, not just PC)
  3. Transacylase activity
- **Action**: MODIFY → `GO:0102545` (phospholipase B activity)

### 2. Reaction Mechanism Errors

**The Problem**: Wrong reaction type inferred from domain classification.

**Example - PHYKPL (human)**:
- Domain: Aminotransferase III family
- Annotated: `GO:0008483` (transaminase activity)
- Actual: Phospho-lyase (EC 4.2.3.134), NOT a transaminase
- Evidence: "Unlike AGXT2, AGXT2L1 and AGXT2L2 did not act as transaminases"
- **Action**: REMOVE transaminase; ADD `GO:0016838` (carbon-oxygen lyase activity, acting on phosphates)

### 3. Cofactor Specificity Errors

**The Problem**: Enzyme annotated with wrong cofactor preference.

**Examples**:
- NAD+ vs NADP+ dependent dehydrogenases
- PLP-dependent enzymes with different reaction types

### 4. Non-Enzymatic Homologs

**The Problem**: Enzymatic activity annotated to proteins that have lost catalytic function.

**Example - Epe1 (S. pombe)** (see CONTESTED_FUNCTION.md):
- Annotated: Histone demethylase, oxidoreductase, dioxygenase
- Actual: Pseudo-enzyme with degenerate active site
- **Action**: REMOVE all enzymatic annotations

## Featured Examples

### LPL1 (Candida albicans)

**UniProt**: Q5AMS2
**Species**: CANAL
**Status**: COMPLETE

**Specificity Issue**:
- `GO:0004622` (phosphatidylcholine lysophospholipase) - too narrow
- Enzyme acts on ALL glycerophospholipids, not just PC
- Has three distinct activities (hydrolase, lysophospholipase, transacylase)

**Also**: `GO:0047372` (monoacylglycerol lipase activity) marked KEEP_AS_NON_CORE
- Likely substrate promiscuity, not primary function

### PHYKPL (Homo sapiens)

**UniProt**: Q8IUZ5
**Species**: human
**Status**: COMPLETE

**Specificity Issue**:
- Classified in aminotransferase family → annotated with transaminase activity
- Biochemically demonstrated to be a phospho-lyase
- Different reaction mechanism entirely

**Proposed New Terms**:
- `5-phosphooxy-L-lysine phospho-lyase activity` - specific MF for PHYKPL
- `5-phosphohydroxy-L-lysine catabolic process` - specific BP

### GND1 (Candida albicans)

**UniProt**: A0A1D8PFS4
**Species**: CANAL
**Status**: INITIALIZED (annotations pending review)

**Notes**: 6-phosphogluconate dehydrogenase with interesting dual localization (cytosol and peroxisome via alternative splicing). Review needed for specificity annotations.

### Mitochondrial fatty acid β-oxidation (acyl-chain-length specificity)

**Species**: human · **Status**: COMPLETE · **Module**: `MODULE:fatty_acid_beta_oxidation`

A clean, paralog-rich worked example of **substrate (acyl-chain-length)
specificity**. The four-step β-oxidation spiral (dehydrogenase → hydratase →
3-hydroxyacyl-CoA dehydrogenase → thiolase) is run by families of chain-length-
specific isozymes; the curation principle is **use the chain-length-specific MF
term where one exists, and fall back to the general term where it does not**
("not all MF have them"). Reviewed across all ten human enzymes:

| Step | Gene | UniProt | MF term | Chain-length specificity |
|------|------|---------|---------|--------------------------|
| ① dehydrogenase | ACADVL | P49748 | `GO:0017099` | very-long/long-chain-specific |
| ① dehydrogenase | ACAD9 | Q9H845 | `GO:0017099` | VLC + complex I assembly factor |
| ① dehydrogenase | ACADM | P11310 | `GO:0070991` | medium-chain-specific |
| ① dehydrogenase | ACADS | P16219 | `GO:0016937` | short-chain-specific |
| ② hydratase | HADHA | P40939 | `GO:0004300` | long-chain (no LC-specific MF; in MTP) |
| ② hydratase | ECHS1 | P30084 | `GO:0004300` | short/medium (no SC-specific MF) |
| ③ 3-OH-acyl-CoA DH | HADHA | P40939 | `GO:0016509` | long-chain-specific (in MTP) |
| ③ 3-OH-acyl-CoA DH | HADH | Q16836 | `GO:0003857` | short/medium (no SC-specific MF) |
| ④ thiolase | HADHB | P55084 | `GO:0003988` | long-chain (in MTP; no chain-specific MF) |
| ④ thiolase | ACAA2 | P42765 | `GO:0003988` | medium/long straight-chain (no chain-specific MF) |
| ④ thiolase | ACAT1 | P24752 | `GO:0003985` | acetoacetyl-CoA (C4; ketone-body/Ile, not the spiral) |

**Specificity errors caught:**
- **Too broad → specific (MODIFY)**: HADHA's generic 3-hydroxyacyl-CoA
  dehydrogenase annotations modified to the long-chain-specific `GO:0016509`.
- **Wrong chain-length (over-annotation)**: long-chain `GO:0016509` annotated on
  **HADH**, which is the *short/medium*-chain enzyme — that activity is HADHA's.
- **Wrong subunit / activity (REMOVE)**: thiolase MF (`GO:0003985`) on **HADHA** —
  thiolase is the HADHB subunit's activity; the cited paper itself shows the
  α-cDNA yields only hydratase + dehydrogenase.
- **Cross-gene mis-attribution (REMOVE)**: cholesterol O-acyltransferase +
  ER localization on **ACAT1** — these came from a SOAT1/SOAT2 paper via the
  historical "ACAT1" nickname collision; mitochondrial T2 has no sterol activity.
- **Paralog cross-transfer (REMOVE)**: several IEA/ISS terms on **ACADVL** were
  propagated from mouse LCAD (*Acadl*), including a self-contradictory
  "negative regulation of fatty acid oxidation".

**Reaction-specificity / mapping gap (links to RHEA project):** the GO→RHEA
chaining check on the module flags ① → ② as a break — step ① makes
(2E)-enoyl-CoA, but the hydratase MF `GO:0004300` maps only to RHEA:20724 (the
(3E)-enoyl-CoA variant), not the canonical (2E) crotonase RHEA:16105. The
chemistry is correct; the gap is in the **GO:0004300 → RHEA** mapping. See
`projects/RHEA/RHEA-EC-SPECIFICITY.md` and the module's
`modules/fatty_acid_beta_oxidation/RESULTS.md`.

## Genes for Review

### Priority 1: Completed
| Gene | Species | Issue | Status |
|------|---------|-------|--------|
| LPL1 | CANAL | Substrate specificity too narrow | COMPLETE |
| PHYKPL | human | Wrong reaction mechanism | COMPLETE |
| eryCIII | SACEN | Wrong donor: `GO:0008194` UDP-glycosyltransferase, but uses **TDP**-D-desosamine | COMPLETE |

**eryCIII (cofactor/donor specificity error, BGC project):** the desosaminyl transferase
EryCIII (EC 2.4.1.278) was IEA-annotated `GO:0008194` UDP-glycosyltransferase activity, but it
transfers **TDP-D-desosamine** (a dTDP-sugar), not a UDP-sugar (PMID:15303858). MODIFY to the
accurate, IDA-supported `GO:0016758` hexosyltransferase activity. See `genes/SACEN/eryCIII/`.

### Priority 1: Completed — fatty acid β-oxidation (acyl-chain-length specificity)
| Gene | Species | Issue | Status |
|------|---------|-------|--------|
| ACADVL | human | Chain-length-specific MF; mouse-LCAD paralog cross-transfer removed | COMPLETE |
| ACAD9 | human | VLC dehydrogenase + complex I assembly factor | COMPLETE |
| ACADM | human | Medium-chain-specific MF (`GO:0070991`) | COMPLETE |
| ACADS | human | Short-chain-specific MF (`GO:0016937`) | COMPLETE |
| HADHA | human | Generic→long-chain-specific MODIFY; thiolase MF removed (HADHB's) | COMPLETE |
| HADHB | human | Long-chain thiolase (MTP β subunit) | COMPLETE |
| ECHS1 | human | General hydratase MF (no SC-specific term) | COMPLETE |
| HADH | human | Short/medium MF; long-chain `GO:0016509` over-annotation flagged | COMPLETE |
| ACAT1 | human | SOAT1/cholesterol mis-attribution removed | COMPLETE |
| ACAA2 | human | Straight-chain 3-ketoacyl-CoA thiolase | COMPLETE |

### Priority 2: Pending
| Gene | Species | Issue | Status |
|------|---------|-------|--------|
| GND1 | CANAL | Review pending | INITIALIZED |

## Curation Principles

1. **Verify substrate range**: Don't assume specificity from one characterized reaction
2. **Check reaction mechanism**: Domain family doesn't guarantee mechanism
3. **Distinguish promiscuity from core function**: Secondary activities → KEEP_AS_NON_CORE
4. **Propose specific terms**: When existing terms are too broad or narrow

---

# STATUS

## Completed Reviews
- [x] CANAL/LPL1 - Phospholipase B specificity
- [x] human/PHYKPL - Phospho-lyase vs transaminase
- [x] human β-oxidation acyl-chain-length set (ACADVL, ACAD9, ACADM, ACADS, HADHA, HADHB, ECHS1, HADH, ACAT1, ACAA2)

## Pending Reviews
- [ ] CANAL/GND1 - 6-phosphogluconate dehydrogenase

Last updated: 2026-06-30

# NOTES

## 2026-01-22

**Project Creation**

Created project to track enzyme specificity annotation issues.

**LPL1 Key Points**:
- Phospholipase B enzymes have three activities in one protein
- Current annotation (`GO:0004622`) captures only lysophospholipase on PC
- Better term: `GO:0102545` (phospholipase B activity)
- Also: `GO:0047372` (monoacylglycerol lipase) kept as non-core (likely promiscuous)

**PHYKPL Key Points**:
- Domain classification misleading (aminotransferase family)
- Biochemically: "did not act as transaminases"
- Functions as phospho-lyase (EC 4.2.3.134)
- Needs specific GO term for its reaction

## 2026-06-30

**Added the mitochondrial fatty acid β-oxidation acyl-chain-length specificity set.**

Reviewed all ten human β-oxidation enzymes as a paralog-rich worked example of
substrate-chain-length specificity (a flavour of categories 1 "too broad" and
"wrong substrate"). Curation principle confirmed: use the chain-length-specific
MF where it exists (VLCAD `GO:0017099`, MCAD `GO:0070991`, SCAD `GO:0016937`,
long-chain 3-OH-acyl-CoA DH `GO:0016509`) and fall back to the general term where
none exists (the hydratases ECHS1/HADHA → `GO:0004300`; the straight-chain
thiolases HADHB/ACAA2 → `GO:0003988`; short/medium HADH → `GO:0003857`).

Specificity errors removed/modified: HADHA generic→long-chain MODIFY and the
mis-attributed thiolase MF removed; the long-chain `GO:0016509` over-annotation
on short-chain HADH flagged; ACAT1's SOAT1/cholesterol terms removed
(nickname collision); ACADVL's mouse-LCAD paralog cross-transfers removed.

Cross-link: the cross-species `MODULE:fatty_acid_beta_oxidation` and its
GO→RHEA chaining check (now generalized into the module tooling) surface a
reaction-specificity mapping gap — `GO:0004300` maps to RHEA:20724 (the (3E)
variant) rather than the canonical (2E) crotonase RHEA:16105. Logged for the
RHEA project (`projects/RHEA/RHEA-EC-SPECIFICITY.md`).
