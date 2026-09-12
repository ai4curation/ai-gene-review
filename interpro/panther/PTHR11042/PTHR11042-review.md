# PANTHER Family Review: PTHR11042

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR11042 |
| **Family Name** | Cell Cycle and Stress Response Kinase (CC_SR_Kinase) |
| **InterPro Entry** | IPR050339 (integrated) |
| **Total Proteins** | 27,717 |
| **Taxonomic Breadth** | 11,117 taxa |
| **Subfamilies** | 31 |
| **Representative Structure** | 8bju (Human WEE1 kinase in complex with a pyrazolopyrimidinone inhibitor) |
| **S. pombe anchor gene** | wee1 (P07527) |

## Executive Summary

PTHR11042 is a family of **protein kinases** that splits into two functionally distinct but evolutionarily related branches: (1) the **Wee1/Myt1** cell-cycle-inhibitory kinases that phosphorylate the inhibitory Tyr15/Thr14 of CDK1 (Cdc2) to **negatively regulate the G2/M transition**, and (2) the **eIF2alpha kinases** (GCN2, PERK/EIF2AK3, HRI/EIF2AK1, PKR/EIF2AK2) that phosphorylate eIF2-alpha to trigger the **integrated stress response** and shut down global translation. Both branches are serine/threonine (Wee1 additionally tyrosine) kinases sharing the conserved bilobal protein-kinase fold, which is why PANTHER groups them, but their substrates and biology are very different.

This makes PTHR11042 a family with **substantial neofunctionalization**: a single PANTHER family spans cell-cycle Tyr15 kinases and translational stress-response kinases. For the fission-yeast anchor **wee1**, the relevant branch is unambiguously the **Wee1 kinase** branch. The risk profile is therefore propagation of eIF2alpha-kinase / stress-response terms onto Wee1 members (and vice versa); the shared kinase-activity and nuclear-localization terms, by contrast, propagate appropriately across the family.

## Subfamily Analysis

### PTHR11042:SF196 — MITOSIS INHIBITOR PROTEIN KINASE SWE1 (the anchor's subfamily)
**Members:** small fungal Wee1 clade

**Representative members (real, from the CSV):**
- *S. pombe* wee1 (P07527) — the anchor
- *S. cerevisiae* SWE1 (P32944)
- *Candida albicans* SWE1 (Q5AP97)

**Function:** Fungal Wee1/Swe1 — the dose-dependent inhibitory kinase that phosphorylates Cdc2/Cdk1 on Tyr15 to delay mitotic entry until cells reach a threshold size.

**Anchor placement:** The wee1 UniProt record assigns it to **PTHR11042:SF196** (`MITOSIS INHIBITOR PROTEIN KINASE SWE1`), grouping it with budding-yeast Swe1 and Candida Swe1 — the correct fungal Wee1 ortholog group.

### PTHR11042:SF72 / SF185 — WEE1-LIKE PROTEIN KINASE (metazoan WEE1)
**Representative members:** Human WEE1 (P30291), mouse Wee1 (P47810).

**Function:** Metazoan somatic WEE1, the canonical CDK1-Tyr15 inhibitory kinase and G2/M checkpoint effector.

### PTHR11042:SF75 — WEE1-LIKE PROTEIN KINASE 2 (WEE2/WEE1B)
**Members:** ~11 proteins (one of the largest subfamilies)

**Representative members:** Human WEE2 (P0C1S8), mouse Wee2 (Q66JT0).

**Function:** Oocyte-specific Wee1B/WEE2, maintaining meiotic (oocyte) arrest via CDK1-Tyr15 phosphorylation.

### PTHR11042:SF183 — MEMBRANE-ASSOCIATED TYROSINE/THREONINE CDC2-INHIBITORY KINASE (MYT1/PKMYT1)
**Members:** ~7 proteins

**Representative members:** Human PKMYT1 (Q99640), mouse Pkmyt1 (Q9ESG9).

**Function:** Myt1, the membrane-associated Thr14/Tyr15 CDK1-inhibitory kinase — the second arm of CDK1 inhibition alongside Wee1.

### eIF2alpha kinase branch — PTHR11042:SF160 (HRI/EIF2AK1), SF136 (GCN2/EIF2AK4), SF166 (PERK/EIF2AK3)
**Members:** SF160 ~10, SF136 ~7 (large subfamilies)

**Representative members:** Human EIF2AK1/HRI (Q9BQI3), *S. cerevisiae* GCN2 (P15442), human EIF2AK4/GCN2 (Q9P2K8).

**Function:** Stress-sensing kinases that phosphorylate eIF2-alpha (EIF2S1) to activate the integrated stress response — a function distinct from cell-cycle CDK1 inhibition.

## Functional Diversity Assessment

- **Conserved core:** protein kinase (serine/threonine; tyrosine for Wee1/Myt1) catalytic activity, ATP binding.
- **Neofunctionalization:** MAJOR — Wee1/Myt1 (CDK1-Tyr15 cell-cycle inhibition) vs. eIF2alpha kinases (translational stress response). Substrate and process terms are NOT interchangeable between these branches.
- **Subfunctionalization (within Wee1 branch):** somatic WEE1 vs. oocyte WEE2 vs. membrane Myt1; fungal Swe1.

## IBA Annotation Assessment

The following IBA (GO_REF:0000033) annotations are propagated to **wee1** (P07527). Node and seed data from `wee1-goa.tsv` and `iba_propagation.tsv`.

| GO ID | Label | Aspect | PANTHER node | Our action | Flags | Verdict |
|-------|-------|--------|--------------|-----------|-------|---------|
| GO:0004713 | protein tyrosine kinase activity | MF | PTN000867899 | ACCEPT | NO_UNIPROT_SEEDS | **Appropriate** |
| GO:0010972 | negative regulation of G2/M transition of mitotic cell cycle | BP | PTN008315181 | ACCEPT | CROSS_SUBFAMILY | **Appropriate** |
| GO:0110031 | negative regulation of G2/MI transition of meiotic cell cycle | BP | PTN008315181 | ACCEPT | NO_UNIPROT_SEEDS | **Appropriate** |
| GO:0005634 | nucleus | CC | PTN000113601 | ACCEPT | CROSS_SUBFAMILY;LOCALIZATION | **Appropriate** |
| GO:0005737 | cytoplasm | CC | PTN000113601 | KEEP_AS_NON_CORE | CROSS_SUBFAMILY;LOCALIZATION | **Appropriate (non-core)** |

**GO:0004713 (protein tyrosine kinase activity).** NO_UNIPROT_SEEDS but with/from includes PomBase Swe1/Wee1 nodes (SPBC660.14 = mik1, SPCC18B5.03 = wee1) and SGD SWE1. Wee1 is a dual-specificity kinase whose physiological output is Tyr15 phosphorylation of Cdc2; the tyrosine-kinase MF is exactly its core catalytic function. **Appropriate — core.**

**GO:0010972 (negative regulation of G2/M transition).** Flagged CROSS_SUBFAMILY (node PTN008315181, seeds include SF183/Myt1-related and human Wee/Myt members). This is the defining biological role of the entire Wee1/Myt1 inhibitory branch, and wee1 is the founding member of that role; cross-subfamily transfer among Wee1/Wee2/Myt1 is biologically correct, not an error. **Appropriate — core.**

**GO:0110031 (negative regulation of G2/MI transition of meiotic cell cycle).** NO_UNIPROT_SEEDS (PomBase-supported). Consistent with wee1's documented role (with Mik1) in restraining premature meiotic divisions. **Appropriate** (context-specific but biologically sound).

**GO:0005634 (nucleus).** Flagged CROSS_SUBFAMILY;LOCALIZATION but matches wee1's known predominantly nuclear / spindle-pole-body localization where it acts on Cdc2. The cross-subfamily flag reflects that nuclear localization is shared across Wee1-branch members; this is a broadly conserved localization for a nuclear cell-cycle kinase and is correct per the calibrated rules. **Appropriate.**

**GO:0005737 (cytoplasm).** Flagged CROSS_SUBFAMILY;LOCALIZATION. The seeds for the cytoplasm term (node PTN000113601) include eIF2alpha-kinase-branch and Myt1/membrane members that are predominantly cytoplasmic; cytoplasmic localization is more characteristic of those branches than of nuclear/SPB-localized fission-yeast Wee1. Rather than calling it wrong (wee1 does have some cytoplasmic/cortical-node presence at Cdr2 nodes), it is correctly down-weighted to **KEEP_AS_NON_CORE** — the only term here where cross-branch localization transfer warranted caution.

**Verdict:** wee1's catalytic and G2/M-inhibitory IBAs are strongly supported by the Wee1/Myt1 branch of the tree and represent genuine core functions. The CROSS_SUBFAMILY flags on the kinase/regulation terms are correct propagations within the inhibitory-kinase branch. The single localization term flagged for caution (cytoplasm) is retained as non-core. No stress-response (eIF2alpha-branch) terms leaked onto wee1, so the major neofunctionalization boundary was respected.

## Review Status

- **Date**: 2026-06-07
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER metadata/member table, UniProt (P07527), wee1 GOA IBA rows, iba_propagation.tsv, wee1-ai-review.yaml
