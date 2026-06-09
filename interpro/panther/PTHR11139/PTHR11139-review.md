# PANTHER Family Review: PTHR11139

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR11139 |
| **Family Name** | DNA Damage Response and Repair Kinase (DDR_Repair_Kinase) |
| **InterPro Entry** | IPR050517 (integrated) |
| **Total Proteins** | 25,560 |
| **Taxonomic Breadth** | 10,867 taxa |
| **Subfamilies** | 17 |
| **Representative Structure** | (none recorded in metadata) |
| **S. pombe anchor gene** | rad3 (Q02099) |

## Executive Summary

PTHR11139 is the **phosphatidylinositol-3-kinase-related kinase (PIKK)** family — large (often >2,000-residue) serine/threonine protein kinases that, despite sequence similarity to lipid kinases, phosphorylate **Ser/Thr residues in S/T-Q motifs** on protein substrates. The family contains the apical DNA-damage and replication-checkpoint sensor kinases **ATR (Rad3/Mec1)** and **ATM (Tel1)**, the double-strand-break repair kinase **DNA-PKcs (PRKDC)**, the nonsense-mediated-decay kinase **SMG1**, the master growth regulator **mTOR (TOR1/TOR2)**, and the (catalytically dead) chromatin scaffold **TRRAP (Tra1)**. All catalytically active members share the C-terminal FAT-kinase-FATC PIKK architecture and the protein-Ser/Thr-kinase activity, but they have diversified into clearly distinct biological pathways.

This is a family with **major neofunctionalization**: DNA-damage signaling (ATR/ATM/DNA-PKcs), nutrient/growth signaling (mTOR), mRNA surveillance (SMG1), and a pseudokinase transcriptional scaffold (TRRAP) all coexist. For the fission-yeast anchor **rad3** (the ATR ortholog) the relevant clade is the **ATR/Mec1 checkpoint** branch. The conserved protein-Ser/Thr-kinase activity propagates appropriately across the whole family, but pathway-specific process and localization terms (e.g. mTOR growth signaling, TRRAP transcription) must not be transferred onto rad3.

## Subfamily Analysis

### PTHR11139:SF125 — SERINE/THREONINE-PROTEIN KINASE MEC1 (the anchor's subfamily)
**Members:** ~6 proteins

**Representative members (real, from the CSV):**
- *S. pombe* rad3 (Q02099) — the anchor
- *S. cerevisiae* MEC1 (P38111)
- *Candida albicans* MEC1 (Q59LR2)
- *Kluyveromyces lactis* MEC1 (Q6CT34)
- *Candida glabrata* MEC1 (Q6FX42)
- *Eremothecium gossypii* MEC1 (Q75DB8)

**Function:** Fungal ATR ortholog (Mec1/Rad3) — the apical sensor kinase of the DNA-structure checkpoints, activated at RPA-coated ssDNA and signaling to Chk1/Cds1.

**Anchor placement:** The rad3 UniProt record assigns it to **PTHR11139:SF125** (`SERINE/THREONINE-PROTEIN KINASE MEC1`), grouping it with budding-yeast Mec1 and other fungal Mec1 orthologs — the correct fungal ATR group. (Metazoan ATR is the sibling subfamily SF69.)

### PTHR11139:SF69 — SERINE/THREONINE-PROTEIN KINASE ATR
**Members:** ~10 proteins (one of the largest subfamilies)

**Representative members:** Human ATR (Q13535), mouse Atr (Q9JKK8), *Drosophila* mei-41 (Q9VXG8).

**Function:** Metazoan ATR — the direct functional ortholog of rad3/Mec1; replication-stress and DNA-damage checkpoint kinase. SF69 and SF125 together constitute the ATR clade.

### PTHR11139:SF9 — SERINE/THREONINE-PROTEIN KINASE MTOR
**Members:** ~11 proteins (largest subfamily)

**Representative members:** Human MTOR (P42345), *S. cerevisiae* TOR1 (P35169), TOR2 (P32600).

**Function:** mTOR, the nutrient/growth-signaling PIKK at the core of TORC1/TORC2 — a distinct pathway from DNA-damage signaling.

### PTHR11139:SF68 — DNA-DEPENDENT PROTEIN KINASE CATALYTIC SUBUNIT (DNA-PKcs)
**Members:** ~6 proteins

**Representative members:** Human PRKDC (P78527), mouse Prkdc (P97313).

**Function:** DNA-PKcs, the NHEJ double-strand-break repair kinase.

### PTHR11139:SF1 — TRANSFORMATION/TRANSCRIPTION DOMAIN-ASSOCIATED PROTEIN (TRRAP)
**Members:** ~10 proteins

**Representative members:** Human TRRAP (Q9Y4A5), *S. cerevisiae* TRA1 (P38811).

**Function:** TRRAP/Tra1 — a catalytically dead PIKK serving as a scaffold in HAT (SAGA/NuA4) transcriptional coactivator complexes; pseudokinase neofunctionalization.

### PTHR11139:SF71 / SF119 — SERINE/THREONINE-PROTEIN KINASE SMG1
**Representative members:** Human SMG1 (Q96Q15).

**Function:** SMG1, the PIKK that phosphorylates UPF1 in nonsense-mediated mRNA decay.

## Functional Diversity Assessment

- **Conserved core:** protein serine/threonine kinase activity (S/T-Q motif), PIKK FAT-kinase-FATC architecture, ATP binding.
- **Neofunctionalization:** MAJOR — DNA-damage/replication checkpoint (ATR, ATM, DNA-PKcs), growth signaling (mTOR), mRNA surveillance (SMG1), pseudokinase transcription scaffold (TRRAP). Pathway-specific process terms are not interchangeable.
- **Subfunctionalization (within DDR branch):** ATR (replication stress) vs. ATM (DSB) vs. DNA-PKcs (NHEJ).

## IBA Annotation Assessment

The following IBA (GO_REF:0000033) annotations are propagated to **rad3** (Q02099). Node and seed data from `rad3-goa.tsv` and `iba_propagation.tsv`.

| GO ID | Label | Aspect | PANTHER node | Our action | Flags | Verdict |
|-------|-------|--------|--------------|-----------|-------|---------|
| GO:0004674 | protein serine/threonine kinase activity | MF | PTN000124197 | ACCEPT | CROSS_SUBFAMILY | **Appropriate** |
| GO:0000077 | DNA damage checkpoint signaling | BP | PTN001673376 | ACCEPT | CROSS_SUBFAMILY | **Appropriate** |
| GO:0005694 | chromosome | CC | PTN001673376 | ACCEPT | CROSS_SUBFAMILY;LOCALIZATION | **Appropriate** |

**GO:0004674 (protein serine/threonine kinase activity).** Flagged CROSS_SUBFAMILY (node PTN000124197, seeds include human ATR Q13535, ATM Q13315, DNA-PKcs P78527, SMG1 Q96Q15 across SF68/SF69/SF71). This is the defining catalytic activity of the entire active PIKK family; transfer across the DNA-damage-kinase subfamilies is exactly the broadly conserved function the calibrated rules say is correct. rad3 is experimentally a protein Ser/Thr (S/T-Q) kinase. **Appropriate — core.**

**GO:0000077 (DNA damage checkpoint signaling).** Flagged CROSS_SUBFAMILY (seeds include human ATR Q13535 and ATM Q13315 from SF69). This is the core biological process of the ATR/ATM checkpoint clade to which rad3/Mec1 belongs; cross-subfamily transfer from metazoan ATR (the direct ortholog group) to fungal Mec1/rad3 is biologically correct and matches rad3's curated role as the apical checkpoint sensor kinase. **Appropriate — core.**

**GO:0005694 (chromosome).** Flagged CROSS_SUBFAMILY;LOCALIZATION (seeds include ATR Q13535 / ATM Q13315). rad3 is a nuclear, chromatin-associated kinase that localizes to sites of DNA damage, stalled forks and telomeres, so chromosome localization is consistent with its known biology, not contradicted by it. Per the rules, localization transfer that matches the gene's documented localization is appropriate. **Appropriate.**

**Verdict:** All three rad3 IBAs are well-supported by the family tree. Every flag is CROSS_SUBFAMILY arising from propagation between the metazoan ATR (SF69)/ATM and fungal Mec1 (SF125) checkpoint subfamilies — the correct ortholog clade — plus the conserved PIKK kinase activity. None of rad3's IBAs derive from the mTOR (SF9), TRRAP (SF1) or SMG1 pathways, so the major neofunctionalization boundaries within this family were respected. No over-propagations detected.

## Review Status

- **Date**: 2026-06-07
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER metadata/member table, UniProt (Q02099), rad3 GOA IBA rows, iba_propagation.tsv, rad3-ai-review.yaml
