# PANTHER Family Review: PTHR23063

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR23063 |
| **Family Name** | Glycerophospholipid acyltransferase (GPAT / GPL_acyltransferase) |
| **InterPro Entry** | none (no integrated InterPro entry) |
| **Total Proteins** | 16,888 |
| **Taxonomic Breadth** | 11,476 taxa; 4,623 proteomes (spans bacteria, fungi, plants, metazoa) |
| **Subfamilies** | 22 |
| **Module role** | Kennedy pathway **step 1** — ER glycerol-3-phosphate (sn-1) acylation producing lysophosphatidic acid (LPA). Exemplar: `UniProtKB:Q8GWG0 (GPAT9_ARATH)` at **PTHR23063:SF2**; module function `GO:0004366 glycerol-3-phosphate O-acyltransferase activity` |

## Executive Summary

PTHR23063 is a broad **membrane-bound (HXXXXD-motif) glycerolipid/glycerophospholipid acyltransferase** family. Its members transfer acyl groups onto glycerol-3-phosphate or onto lysophospholipid acceptors, and the family collects several distinct activities: sn-1 glycerol-3-phosphate acyltransferases (GPAT3/GPAT4/GPAT9), lysophosphatidylcholine acyltransferases (LPCAT1/2/4), lyso-PE acyltransferases (LPEAT), and bacterial lyso-ornithine lipid acyltransferases (OlsA). The HXXXXD catalytic motif is shared across the family and is required for acyl transfer.

Within seed triacylglycerol assembly, the relevant member is **GPAT9** (Arabidopsis GPAT9, Q8GWG0), which catalyzes the committed first step of glycerolipid/Kennedy-pathway assembly: acylation of the sn-1 position of glycerol-3-phosphate to give lysophosphatidic acid (`GO:0004366`). GPAT9 is the ER-resident, membrane-integral GPAT that feeds the downstream LPAAT → PAP → DGAT sequence; it is distinct from the soluble plastidial GPAT and from the land-plant-specific soluble/cutin GPAT (GPAT1–8) families, which are not in this PANTHER family. The plant GPAT9 sits within a much larger family whose other subfamilies perform phospholipid remodeling (Lands cycle) rather than de novo sn-1 acylation, so the specific GPAT9 activity is a subfamily-level property, not a family-wide one.

## Subfamily Analysis

- **Exemplar subfamily**: GPAT9 is **PTHR23063:SF2** ("GLYCEROL-3-PHOSPHATE ACYLTRANSFERASE 4, ISOFORM D-RELATED"). Human/mouse GPAT4 map to SF37 and GPAT3 to SF10, i.e. the animal ER GPAT3/4 (AGPAT-like) orthologs are close relatives of plant GPAT9.
- **Broad parent**: 22 subfamilies spanning **11,476 taxa across bacteria (e.g. Brucella/Rhizobium OlsA, SF52), fungi (S. pombe vps66, SF60), plants and metazoa**. The family is clearly **cross-kingdom** and functionally heterogeneous: SF7/SF13/SF21/SF57 are lysophospholipid (LPCAT/LPEAT) remodeling enzymes, not de novo GPATs. The specific sn-1 glycerol-3-phosphate acyltransferase activity is confined to the GPAT3/4/9 subfamilies (SF2/SF10/SF37).

## IBA / PAINT Assessment

Local PAINT (IBD) data (`PTHR23063-paint.tsv`):

| Node | GO ID | Aspect | Negated | Notes |
|------|-------|--------|---------|-------|
| PTN000551966 | GO:0005783 endoplasmic reticulum | C | false | ER localization propagated to a pan-eukaryotic node (seeds incl. AT5G60620, human Q53EU6/GPAT3, Q86UL3/GPAT4). Consistent with ER-membrane GPAT/LPCAT enzymes. |
| PTN001128751 | GO:0005783 endoplasmic reticulum | C | false | ER localization at the LPCAT-containing node (human LPCAT2 Q7L5N7, LPCAT1 Q8NF37, LPCAT4 Q643R3). |
| PTN001128751 | GO:0042171 lysophosphatidic acid acyltransferase activity | F | false | Acyltransferase MF propagated to the LPCAT sub-node (seeds Q7L5N7, RGD:1311599). |
| PTN002746859 | GO:0005783 endoplasmic reticulum | C | false | ER localization for an Arabidopsis node (AT1G80950). |

Notable: the **GPAT9-specific `GO:0004366 glycerol-3-phosphate O-acyltransferase activity` is NOT among the propagated PAINT nodes here** — the only propagated MF is a lysophosphatidic-acid acyltransferase term on the LPCAT node. PAINT propagation in this family is dominated by the shared ER localization (`GO:0005783`) plus a remodeling-type acyltransferase MF, not by the de novo sn-1 GPAT activity that defines GPAT9's module role.

## InterPro2GO / parent-family mapping verdict

**Do NOT map `GO:0004366 glycerol-3-phosphate O-acyltransferase activity` at the parent-family level.** PTHR23063 is a cross-kingdom, functionally mixed acyltransferase family (GPAT + LPCAT + LPEAT + bacterial OlsA) with 22 subfamilies; whole-protein assignment of the sn-1 GPAT activity would over-annotate the numerous LPCAT/LPEAT remodeling members and the bacterial lyso-ornithine acyltransferases. The GPAT9 module function is safe only at the **SF2 (and sibling GPAT3/4 SF10/SF37) subfamily / PAINT-node level**. A generic membrane-acyltransferase term (e.g. the HXXXXD-motif acyltransferase activity) plus ER-membrane localization is the most that is defensible family-wide.

## Review Status

- **Date**: 2026-07-11
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER metadata/entries, local PAINT (PTHR23063-paint.tsv), UniProt, plant bioenergy module curation
