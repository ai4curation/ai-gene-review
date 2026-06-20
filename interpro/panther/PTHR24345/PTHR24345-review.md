# PANTHER Family Review: PTHR24345

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR24345 |
| **Family Name** | Serine/threonine-protein kinase PLK |
| **InterPro Entry** | (none integrated) |
| **Total Proteins** | 18,634 |
| **Taxonomic Breadth** | 10,037 taxa |
| **Subfamilies** | 9 |
| **Representative Structure** | 4b6l (oral Polo-like kinase (PLK) inhibitor; residue-targeted drug design) |
| **Anchor gene (S. pombe)** | plo1 (P50528), subfamily PTHR24345:SF0 |

## Executive Summary

PTHR24345 is the **Polo-like kinase (PLK)** family: serine/threonine kinases (EC 2.7.11.21) defined by an N-terminal catalytic domain and a C-terminal **Polo-box domain (PBD)** that binds pre-phosphorylated docking motifs to target the kinase to mitotic structures (spindle pole body/centrosome, kinetochores, the spindle, and the cell-division site). PLKs are master regulators of M phase - mitotic entry, bipolar spindle formation, chromosome biorientation, the metaphase-anaphase transition (via the APC/C), and cytokinesis - and the PLK4 branch additionally governs centriole duplication.

The catalytic and process-level functions of the cell-cycle PLK branch are **deeply conserved**, so (per calibration) cross-subfamily IBA transfer of kinase activity and core mitotic processes to the single fungal PLK is expected to be correct. The main divergence is the **PLK4 (SAK/ZYG-1) subfamily**, which has a distinct centriole-duplication role and a divergent domain architecture (single cryptic Polo box), and the inactive **PLK5** pseudokinase branch.

## Subfamily Analysis

### PTHR24345:SF0 - CELL CYCLE SERINE/THREONINE-PROTEIN KINASE CDC5/MSD2 (ANCHOR SUBFAMILY)
**Members**: ~9 proteins, including S. pombe plo1 (P50528, anchor), S. cerevisiae CDC5 (P32562), Dictyostelium PLK (Q86HN7), Giardia plk (A8BPK8), Zea mays CCRP1 (P0C8M8), and a second S. pombe paralog SPCC70.05c (O74526).

**Function**: The fungal/protist single-PLK clade. **Plo1** is the sole S. pombe Polo-like kinase: it reinforces the Cdc25/Wee1 feedback loop to commit cells to mitosis (gated by SPB recruitment via Cut12), builds the bipolar spindle, promotes chromosome biorientation (Dam1 phosphorylation), engages the APC/C (Cut23/Apc8) for the metaphase-anaphase transition, and couples mitosis to cytokinesis by triggering medial-ring assembly (Mid1) and initiating the SIN. In meiosis it partners with meikin (Moa1).

### PTHR24345:SF93 - SERINE/THREONINE-PROTEIN KINASE PLK1
**Members**: ~9 proteins, e.g. human PLK1 (P53350), mouse Plk1 (Q07832), rat Plk1 (Q62673), Xenopus plk1 (P70032/P62205), Bos taurus PLK1 (Q2TA25), Drosophila polo (P52304), C. elegans plk-1/plk-2/plk-3 (Q20845, Q9N2L7).

**Function**: The canonical metazoan mitotic PLK1 - the functional ortholog of plo1; controls mitotic entry, spindle assembly, APC/C activation and cytokinesis. The closest paralog group to the anchor by function.

### PTHR24345:SF91 - SERINE/THREONINE-PROTEIN KINASE PLK4 (SAK/ZYG-1)
**Members**: ~19 proteins (largest subfamily), e.g. Drosophila SAK (O97143), C. elegans zyg-1 (Q9GT24), S. pombe ksp1 (O14328), Encephalitozoon ECU02_0550 (Q8SSH1), and many insect SAK orthologs.

**Function**: PLK4/SAK is the **master regulator of centriole duplication**, with a divergent architecture (a single, cryptic Polo box) and distinct substrates. **This is the most functionally diverged subfamily** and a clade whose centriole-specific roles should NOT be transferred to the anchor.

### PTHR24345:SF44 - SERINE/THREONINE-PROTEIN KINASE PLK2
**Members**: ~4 proteins, e.g. human PLK2 (Q9NYY3), mouse Plk2 (P53351), rat Plk2 (Q9R012), Pongo PLK2 (Q5R4L1).

**Function**: PLK2 (and PLK3, SF42) are metazoan paralogs with roles in centriole duplication licensing, stress responses, and synaptic plasticity - partly diverged from the core mitotic PLK1/plo1 function.

### Other subfamilies
SF42 (PLK3), SF43 (inactive PLK5 pseudokinase), SF52 (PLK-1 variant), SF87 (TBC1-domain-containing kinase), SF89 (additional PLK4 clade).

## Functional Diversity Assessment

- **Conserved across the cell-cycle PLK branch (SF0/SF93/SF44/SF42):** protein serine/threonine kinase activity, ATP binding, mitotic spindle organization, and SPB/centrosome and kinetochore localization.
- **Diverged:** PLK4/SAK (SF91) centriole-duplication role; PLK5 (SF43) inactive pseudokinase; metazoan PLK2/3 synaptic and stress roles.

## IBA Annotation Assessment

Seven IBA (GO_REF:0000033) annotations were propagated to **plo1 (P50528, SF0)**. Most are flagged `CROSS_SUBFAMILY` and/or `LOCALIZATION`, but per calibration these are expected to be correct for a deeply conserved cell-cycle kinase, and the review accepts the great majority.

| GO ID | Label | Aspect | Node | Seeds (same-SF/other) | Our action |
|-------|-------|--------|------|------------------------|------------|
| GO:0004674 | protein serine/threonine kinase activity | MF | PTN000679870 | 4 (0/4) | **ACCEPT** |
| GO:0005634 | nucleus | CC | PTN007795324 | 4 (2 in family) | **ACCEPT** |
| GO:0000922 | spindle pole | CC | PTN000679870 | 1 | **ACCEPT** |
| GO:0000776 | kinetochore | CC | PTN000679870 | 1 | **ACCEPT** |
| GO:0007052 | mitotic spindle organization | BP | PTN000679870 | 2 | **ACCEPT** |
| GO:0005816 | spindle pole body | CC | PTN001217810 | 1 | **ACCEPT** |
| GO:0005737 | cytoplasm | CC | PTN000679870 | 3 | **KEEP_AS_NON_CORE** |

**GO:0004674 (protein serine/threonine kinase activity) - ACCEPT.** Although flagged CROSS_SUBFAMILY (4 seeds in PLK1/PLK2/PLK3 subfamilies, none in SF0), this is exactly the calibrated case where a conserved catalytic function across fine PLK subfamilies is correct. Plo1 is an experimentally characterized Ser/Thr kinase; accept.

**GO:0005634 (nucleus), GO:0000922 (spindle pole), GO:0005816 (spindle pole body), GO:0000776 (kinetochore) - ACCEPT.** These localization IBAs match the experimentally established Plo1 localizations (SPB, kinetochores, spindle). The S. pombe SPB is the functional equivalent of the metazoan centrosome/spindle pole, so the spindle-pole/SPB transfers are biologically appropriate despite the LOCALIZATION flag. Nuclear localization is consistent with Plo1's mitotic nuclear functions in the closed mitosis of fission yeast.

**GO:0007052 (mitotic spindle organization) - ACCEPT.** Core conserved mitotic process; Plo1 is required for bipolar-spindle formation. Correct.

**GO:0005737 (cytoplasm) - KEEP_AS_NON_CORE.** A generic, low-information localization (3 seeds across PLK2/PLK3/PLK4 subfamilies). Not wrong but uninformative relative to the specific SPB/spindle/kinetochore/division-site locations; retained as non-core.

**Calibration note.** No PLK4/SAK-specific (SF91) centriole-duplication term was propagated to plo1, which is appropriate - that is the one clade whose specialized function should not transfer. The accepted transfers all concern the conserved cell-cycle PLK core, consistent with the guidance that plo1 kinase activity and core mitotic localizations are expected correct.

## Key Considerations for Curators

1. Cell-cycle PLK catalytic activity and core mitotic localizations (SPB/centrosome, spindle, kinetochore) are conserved and safe to propagate across SF0/SF93/SF44/SF42.
2. PLK4/SAK (SF91) centriole-duplication functions are subfamily-specific and must not be transferred to single-PLK fungal members.
3. PLK5 (SF43) is an inactive pseudokinase - do not propagate catalytic activity to it.

## Review Status

- **Date**: 2026-06-07
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER metadata/entries, UniProt, S. pombe plo1 curated review, GOA IBA annotations, PANTHER_IBA_REVIEW propagation table
