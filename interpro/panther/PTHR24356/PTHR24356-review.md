# PANTHER Family Review: PTHR24356

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR24356 |
| **Family Name** | SERINE/THREONINE-PROTEIN KINASE |
| **InterPro Entry** | IPR050236 |
| **Total Proteins** | 32,144 |
| **Taxonomic Breadth** | 10,298 taxa |
| **Subfamilies** | 101 |
| **Representative Structure** | 1uu9 (human PDK1 kinase domain in complex with BIM-3) |
| **Anchor gene (S. pombe)** | sid2 (Q09898), subfamily PTHR24356:SF417 |

## Executive Summary

PTHR24356 is a large family of **AGC-group serine/threonine protein kinases** (EC 2.7.11.1). It contains several distinct functional branches: the **NDR/LATS** kinases (DBF2/DBF20, LATS1/2, the Hippo-pathway effectors and the fission-yeast SIN/MEN kinases), the master AGC-activating kinase **PDK1/PDPK1**, the mitotic **Greatwall/MASTL/RIM15** kinases, and the **MAST** (microtubule-associated) kinases. The unifying feature is the AGC catalytic core with a hydrophobic-motif/activation-loop regulatory architecture; most members require activation by an upstream kinase (e.g. PDK1) and/or an associated regulatory (Mob) subunit.

The catalytic molecular function is conserved family-wide, but the family is **highly subfunctionalized** by branch: NDR/LATS act in mitotic-exit/cytokinesis and Hippo growth control, PDK1 is an upstream master regulator, Greatwall controls PP2A inhibition at mitosis, and MAST kinases act on microtubule-associated substrates. IBA transfer of catalytic activity is safe; process and complex terms must be gated to the correct (NDR) branch.

## Subfamily Analysis

### PTHR24356:SF417 - CELL CYCLE PROTEIN KINASE DBF2-RELATED (ANCHOR SUBFAMILY)
**Members**: ~6 proteins, including S. pombe sid2 (Q09898, anchor), S. cerevisiae DBF2 (P22204) and DBF20 (P32328), Candida DBF2 (Q59KM8), Dictyostelium ndrC (Q54P47) and DDB_G0278845 (Q1ZXI5).

**Function**: The **NDR-kinase / mitotic-exit-network (MEN) / septation-initiation-network (SIN)** branch. **Sid2** is the most downstream SIN effector in fission yeast: it works as an obligate complex with its Mob1 regulatory subunit, resides at the SPB, and at the end of anaphase translocates to the division site/contractile ring where it phosphorylates Clp1/Flp1, Cdc12, Mid1, Cdc11 and Nak1 to drive ring constriction and septum formation. The S. cerevisiae orthologs DBF2/DBF20 are the MEN effector kinases. This subfamily is functionally coherent (NDR kinases acting in mitotic exit/cytokinesis with a Mob co-factor).

### PTHR24356:SF1 - SERINE/THREONINE-PROTEIN KINASE GREATWALL (MASTL/RIM15)
**Members**: ~16 proteins (largest subfamily), e.g. human MASTL (E1BFR5 ortholog set), Xenopus mastl (B1WAR9, Q6NTJ3), zebrafish mastl (Q6DBX4), S. cerevisiae RIM15 (P43565), Arabidopsis IREH1 (F4J6F6), Toxoplasma ROP35.

**Function**: Greatwall/MASTL phosphorylates ENSA/ARPP19 to inhibit PP2A-B55 during mitotic entry; RIM15 is the budding-yeast nutrient-responsive paralog. Distinct mechanism and substrates from the NDR branch.

### PTHR24356:SF163 - 3-PHOSPHOINOSITIDE-DEPENDENT PROTEIN KINASE 1 (PDK1)-RELATED
**Members**: ~13 proteins, e.g. human PDPK1 (O15530), rat Pdpk1 (O55173), S. cerevisiae PKH1/PKH2 (Q03407, Q12236), S. pombe ksg1 (Q12701), Candida PKH2 (Q5A3P6), Dictyostelium pdkA (Q54TW2), Arabidopsis PDPK2 (Q4V3C8).

**Function**: PDK1 is the **master upstream activator** that phosphorylates the activation loop of many AGC kinases. A regulatory hub rather than a mitotic-exit effector.

### PTHR24356:SF138 / SF149 - SERINE/THREONINE-PROTEIN KINASE LATS1 / LATS2
**Members**: human LATS1 (O95835, SF138), mouse Lats2 (Q7TSJ6, SF149), and orthologs.

**Function**: NDR-family Hippo-pathway effector kinases that phosphorylate YAP/TAZ to control organ size and tumor suppression. The metazoan NDR branch sister to the SIN/MEN kinases.

### Other subfamilies
SF140/SF150/SF136/SF224 (MAST1-4, microtubule-associated Ser/Thr kinases), SF413 (CEK1-related), SF405 (PKH3), SF418/SF420/SF422 (WARTS/PPK35 and other AGC kinases).

## Functional Diversity Assessment

- **Conserved family-wide (safe to propagate):** protein serine/threonine kinase activity and ATP binding.
- **Branch-specific (gate carefully):** NDR/SIN/MEN cytokinesis and mitotic-exit processes and Mob-containing complexes (DBF2/Sid2/LATS); PDK1 upstream-activation role; Greatwall PP2A-inhibition; MAST microtubule-associated functions.

## IBA Annotation Assessment

Five IBA annotations in the Sid2 review correspond to cached PAINT ancestral assertions: kinase activity and intracellular signal transduction at PTN000683254, Sid2-Mob1 complex and regulation of exit from mitosis at PTN008614896, and spindle pole body localization at PTN001220075. These assertions carry evidence from several database namespaces; absence of UniProt-prefixed sources does not indicate absence of experimental grounding. Assertion/source identities were verified from cached PAINT data; ancestral placement was not independently re-evaluated from a tree and alignment.

| GO ID | Label | Aspect | Node | Our action |
|-------|-------|--------|------|------------|
| GO:0004674 | protein serine/threonine kinase activity | MF | PTN000683254 | **ACCEPT** |
| GO:0035556 | intracellular signal transduction | BP | PTN000683254 | **KEEP_AS_NON_CORE** |
| GO:0034973 | Sid2-Mob1 complex | CC | PTN008614896 | **ACCEPT** |
| GO:0005816 | spindle pole body | CC | PTN001220075 | **ACCEPT** |
| GO:0007096 | regulation of exit from mitosis | BP | PTN008614896 | **MARK_AS_OVER_ANNOTATED** |

**GO:0004674 (protein serine/threonine kinase activity) — ACCEPT.** Sid2 is experimentally established as a Ser/Thr kinase. The cached IBD sources include Sid2 itself (PomBase:SPAC24B11.11c), which is legitimate experimental grounding for a phylogenetic assertion, not circularity. Source counts do not measure the quality of the ancestral placement.

**GO:0034973 (Sid2-Mob1 complex) — ACCEPT.** Direct interaction and complex membership are supported by PMID:10769201 and PMID:10837231. The cached IBD sources are PomBase:SPAC24B11.11c and SGD:S000003324; neither being UniProt-prefixed makes the assertion unsupported.

**GO:0005816 (spindle pole body) — ACCEPT.** Retain experimentally supported SPB localization. PMID:10459013 reports Sid2-GFP localization throughout the cell cycle; PMID:22684255 distinguishes this reporter from untagged Sid2 detected in the cytoplasm during G2. Do not generalize the reporter result to constitutive interphase SPB residence of untagged Sid2. The cached IBD has fungal taxon restriction taxon:4751 and includes Sid2 among its sources.

**GO:0035556 (intracellular signal transduction) — KEEP_AS_NON_CORE.** This broad process is correct for the SIN effector kinase, although its septation-initiation and cytokinesis roles are more informative. The cached IBD also includes Sid2 among its sources.

**GO:0007096 (regulation of exit from mitosis) — MARK_AS_OVER_ANNOTATED.** The cached IBD at PTN008614896 cites CGD:CAL0000197161. The recommendation concerns the fit of this inherited process to S. pombe Sid2: experimental studies distinguish Sid2-dependent cytokinesis initiation from MEN-like control of mitotic exit (PMID:10837231; PMID:22684255). Source count and source database are not evidence against the ancestral assertion. Do not describe this record as a verified pairwise transfer from S. cerevisiae Dbf2 or claim that the source experiment is wrong.

**Calibration note.** Retain the catalytic, complex and localization assertions; flag the mitotic-exit process on target-specific functional grounds and retain generic signal transduction as non-core. This assessment does not infer evidence quality from donor counts or identifier namespaces.

## Key Considerations for Curators

1. AGC/NDR catalytic activity is conserved family-wide and safe to propagate.
2. SIN/MEN cytokinesis functions and Mob-containing complexes are specific to the NDR branch (SF417 / LATS subfamilies) - do not transfer to PDK1, Greatwall or MAST branches.
3. "Regulation of exit from mitosis" (a MEN concept) should not be applied to the fission-yeast SIN effector Sid2, whose role is cytokinesis/septation; prefer SIN/cytokinesis-specific terms.

## Review Status

- **Date**: 2026-06-07
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER metadata/entries, UniProt, S. pombe sid2 curated review, GOA IBA annotations, PANTHER_IBA_REVIEW propagation table
