# PANTHER Family Review: PTHR10177

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR10177 |
| **Family Name** | CYCLINS |
| **InterPro Entry** | IPR039361 (integrated) |
| **Total Proteins** | 51,432 |
| **Taxonomic Breadth** | 9,950 taxa |
| **Subfamilies** | 159 |
| **Representative Structure** | 4eoj (Thr160-phosphorylated CDK2 H84S/Q85M/K89D - human cyclin A3 complex with ATP) |
| **S. pombe anchor gene** | cdc13 (P10815) |

## Executive Summary

PTHR10177 is the **cyclin** superfamily: the regulatory subunits that bind and activate cyclin-dependent kinases (CDKs) to drive ordered progression through the eukaryotic cell cycle. The unifying molecular feature of the family is the **cyclin box fold**, a conserved ~100-residue helical domain that docks onto the CDK and reorganizes its activation loop and PSTAIRE helix to create an active kinase. Most members confer a **cyclin-dependent protein serine/threonine kinase regulator activity** (GO:0016538) and assemble with their CDK partner into a **cyclin-dependent protein kinase holoenzyme complex** (GO:0000307).

The family is large and substantially **subfunctionalized** (159 subfamilies): although the cyclin-box/CDK-activation function is broadly conserved, individual cyclin classes have specialized in *when* in the cell cycle they act and *which* CDK and substrates they engage. The principal eukaryotic classes are the G1/S cyclins (cyclin D, cyclin E), S-phase cyclins (cyclin A), and mitotic B-type cyclins (cyclin B), plus more divergent transcriptional cyclins (cyclin C/H/K/T families) and meiotic cyclins. Conservation of the central MPF (cyclin B-CDK1) role from yeast to human is very high, so the core cell-cycle annotations propagate cleanly across orthologs; the risk in such a large family is over-specific propagation between functionally distinct cyclin classes.

## Subfamily Analysis

> Note: the cached `PTHR10177-entries.csv` export does not populate per-protein subfamily (SF) assignments (all 225 representative rows have empty `subfamily`/`subfamily_name` fields), so the subfamily breakdown below is described at the level of the well-established cyclin classes represented among the real members in the file rather than by numbered SF IDs.

### Mitotic B-type cyclins (cyclin B / cyclin AB class) — the anchor's class
**Representative members (real, from the CSV):**
- *S. pombe* cdc13 (P10815) — the anchor
- Human CCNB1 (P14635), CCNB2 (O95067)
- Mouse Ccnb1 (P24860), Ccnb2 (P30276)
- *Drosophila* CycB (P20439)
- *S. cerevisiae* CLB1 (P24868), CLB2 (P24869), CLB3 (P24870), CLB4 (P24871)

**Function:** Bind CDK1 (Cdc2) to form **M-phase-promoting factor (MPF)**, the principal driver of mitotic entry and progression; APC/C-mediated destruction-box-dependent degradation at anaphase resets the cycle.

**Anchor placement:** The fission-yeast UniProt record assigns cdc13 to **PTHR10177** at the family level only (`DR PANTHER; PTHR10177; CYCLINS; 1.`) with no specific SF, consistent with the empty SF fields in the member table. Biologically, cdc13 is the single mitotic B-type cyclin of *S. pombe* and groups with the cyclin B / cyclin AB class (CCNB1/CCNB2, CLB1-4, CycB).

### S-phase / G1-S cyclins (cyclin A and cyclin E class)
**Representative members:** Human CCNA2 (P20248), CCNE1 (P24864), CCNE2 (O96020); *Drosophila* CycA (P14785).

**Function:** Activate CDK2/CDK1 to drive S-phase entry and DNA replication; cyclin E controls the G1/S transition and origin licensing.

### G1 (cyclin D / Cln) class
**Representative members:** Human CCND1 (P24385), CCND2 (P30279); mouse Ccnd1 (P25322), Ccnd2 (P30280); *S. cerevisiae* CLN3 (P13365); *S. pombe* puc1 (P25009), cig1 (P24865).

**Function:** Govern G1 progression and the G1/S commitment (START); D-type cyclins partner CDK4/6 in metazoa.

### Divergent / specialized cyclins
**Representative members:** Human CCNO (P22674), mouse Ccno (P0C242), Ccng2 (O08918); *S. pombe* rem1 (O14332, a meiotic cyclin).

**Function:** These members illustrate the family's diversification into meiosis-specific, transcriptional and atypical cyclin roles distinct from the canonical cell-cycle CDK activators.

## Functional Diversity Assessment

- **Conserved core:** cyclin-box-mediated CDK binding and activation (GO:0016538), assembly into a CDK holoenzyme (GO:0000307).
- **Subfunctionalization:** HIGH — distinct cyclin classes act at G1, G1/S, S, and M, partner different CDKs, and (for transcriptional cyclins) regulate RNA Pol II rather than the cell-division cycle. Propagation of *phase-specific* process terms between classes is the main over-annotation risk.

## IBA Annotation Assessment

The following IBA (GO_REF:0000033) annotations are propagated to **cdc13** (P10815). PANTHER node and seed information taken from `cdc13-goa.tsv` and `iba_propagation.tsv`.

| GO ID | Label | Aspect | PANTHER node | Our action | Verdict |
|-------|-------|--------|--------------|-----------|---------|
| GO:0016538 | cyclin-dependent protein serine/threonine kinase regulator activity | MF | PTN000019791 | ACCEPT | **Appropriate** |
| GO:0000307 | cyclin-dependent protein kinase holoenzyme complex | CC | PTN000019791 | ACCEPT | **Appropriate** |
| GO:0005815 | microtubule organizing center | CC | PTN007424001 | KEEP_AS_NON_CORE | **Appropriate but non-core** |
| GO:0007089 | traversing start control point of mitotic cell cycle | BP | PTN000808767 | MARK_AS_OVER_ANNOTATED | **Over-propagation** |

**GO:0016538 / GO:0000307 (CORE).** These are the defining family-level functions of a cyclin: regulating a CDK and being part of the CDK holoenzyme. The seeds (PTN000019791) include human CCNB1 (P14635), CCNA2 (P20248), CCNE1 (P24864) and other bona fide cyclins, exactly the class cdc13 belongs to. The propagation is strongly supported by the family tree and matches cdc13's experimentally established role as the cyclin partner of Cdc2/MPF. **Appropriate — core.**

**GO:0005815 (microtubule organizing center).** Flagged LOCALIZATION. This is supported here rather than spurious: cdc13-Cdc2 is independently documented to concentrate at the spindle pole body (the fungal MTOC) in G2 and on the mitotic spindle. The IBA seeds include cyclin orthologs that localize to centrosomes/SPB. It is correctly retained but as a **non-core** localization rather than a defining function.

**GO:0007089 (traversing start control point of mitotic cell cycle).** Flagged NO_UNIPROT_SEEDS — the supporting node (PTN000808767) carries no UniProt-backed experimental seeds, and "traversing START" is a G1/commitment process more characteristic of G1 cyclins (Cln/Cig/Puc) than of the mitotic B-type cyclin cdc13, whose core role is G2/M (mitotic entry). Propagating a START-phase process to a mitotic cyclin is a class-mismatch typical of a large, phase-subfunctionalized family. Marked **MARK_AS_OVER_ANNOTATED**.

**Verdict:** cdc13's MF and CDK-complex IBAs are well-supported by the family tree and represent genuine core cyclin functions. The localization IBA is appropriate but non-core. The single over-propagation is the START-traversal process term (GO:0007089), which reflects transfer of a G1-cyclin-class process onto a mitotic cyclin and is correctly down-weighted.

## Review Status

- **Date**: 2026-06-07
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER metadata/member table, UniProt (P10815), cdc13 GOA IBA rows, iba_propagation.tsv, cdc13-ai-review.yaml
