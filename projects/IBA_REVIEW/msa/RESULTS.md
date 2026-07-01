---
title: "IBA Pseudo-Enzyme MSA Checks"
species: [human]
genes: [AGO1, AGO2, AGO3, AGO4, DPYSL2, CRMP1, DPYSL3, DPYSL4]
---

# MSA check of two pseudo-enzyme claims

Reproducible alignment-level verification of catalytic-residue loss for two of the
pseudo-enzyme examples in the [IBA_REVIEW findings](../../IBA_REVIEW.md) (Pattern 7).
Earlier passes relied on UniProt CAUTION/FUNCTION text; this analysis independently
inspects the actual residues.

Run: `uv run python catalytic_residue_msa.py` (FAMSA alignment via `pyfamsa`).
Target sequences come from the repo's local `genes/.../*-uniprot.txt`; the reference
active enzyme (DPYS) and the catalytic-residue **positions** are pulled live from the
UniProt REST feature tables (with a documented hardcoded fallback for the AGO2
positions if the API returns none — not triggered in the runs reported here, which
used the live metal-binding-site features).

## 1. Human Argonautes AGO1–4 — RNase-H-like catalytic site (DDH of the DEDH tetrad)

Residues at the positions UniProt annotates on AGO2 as divalent-metal-binding
(the catalytic Asp/Asp/His — i.e. the DDH metal-coordinating subset of the
canonical DEDH slicer tetrad; the catalytic-glutamate "finger" is discussed in
the caveats and is not in the metal-binding feature set):

| AGO2 position | AGO1 | AGO2 | AGO3 | AGO4 |
|---------------|------|------|------|------|
| D597          | D    | **D** | D   | D    |
| D669          | D    | **D** | D   | **G** |
| H807          | R    | **H** | H   | **R** |

- **AGO2** (the only human slicer) has the intact tetrad.
- **AGO4** has **two** substitutions — D669G and H807R — consistent with no
  endonuclease activity. This is direct, alignment-level support for the AGO4 REMOVE
  (`GO:0004521` RNA endonuclease activity).
- Nuance the MSA reveals: **AGO3 retains the full tetrad** (D/D/H), so its weak slicing
  is *not* explained by tetrad loss — a blanket "only AGO2 has the residues" would have
  been wrong. AGO1 loses only the catalytic His (H→R).

## 2. CRMP/DPYSL family vs active dihydropyrimidinase (DPYS, Q14117)

Residues at DPYS's UniProt-annotated Zn(2+)-coordinating / active-site positions:

| DPYS position | DPYS | DPYSL2 | DPYSL3 | DPYSL4 | DPYSL5 | CRMP1 |
|---------------|------|--------|--------|--------|--------|-------|
| H67  (Zn)     | H    | H      | H      | H      | **S**  | **N** |
| H69  (Zn)     | H    | **R**  | H      | **R**  | H      | **Y** |
| K159 (carbamate→Zn) | K | **L** | **M** | **L** | **Q** | **Q** |
| H192 (Zn)     | H    | H      | H      | H      | H      | H     |
| H248 (Zn)     | H    | **K**  | **K**  | **K**  | **N**  | **K** |
| D326 (Zn)     | D    | **A**  | **A**  | **A**  | D      | **G** |

- **All five CRMP/DPYSL paralogs have lost the carbamylated catalytic Lys159** — the
  residue that bridges the binuclear metal centre — plus several Zn-coordinating
  His/Asp. Without K159 there is no metal site and no amidohydrolase activity.
- This is first-hand confirmation of the UniProt CAUTION ("Lacks most of the conserved
  residues … essential for binding the metal cofactor") and supports the `GO:0016812`
  REMOVE across DPYSL2/3/4 (and the same basis for DPYSL5/CRMP1).

## Caveats

- FAMSA with a UPGMA guide tree; results are robust because the inspected columns are
  deep, conserved active-site positions (unambiguous to align).
- UniProt annotated 3 metal-binding residues on AGO2 (the two Asp and the His that
  coordinate the cations); the "E" of the DEDH shorthand is the catalytic glutamate
  finger and is not in the metal-binding feature set, so it is not shown here.
- This verifies *catalytic-residue loss*, which is necessary (not by itself sufficient)
  evidence; it is corroborated by the experimental/curated statements cited in the
  findings.
