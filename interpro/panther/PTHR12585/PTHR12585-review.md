# PANTHER Family Review: PTHR12585

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR12585 |
| **Family Name** | SCC1 / RAD21 FAMILY MEMBER |
| **InterPro Entry** | IPR039781 |
| **Total Proteins** | 11,089 |
| **Taxonomic Breadth** | 9,207 taxa |
| **Subfamilies** | 14 |
| **Representative Structure** | 8roe (Human cohesin SMC1A-HD(shortCC-EQ)/RAD21-C complex, ADP-bound) |
| **S. pombe anchor gene** | rad21 (P30776) |

## Executive Summary

PTHR12585 encodes the **alpha-kleisin subunit of the cohesin complex** (the SCC1/RAD21/REC8 family). Family members are intrinsically disordered, elongated proteins whose conserved N- and C-terminal domains clamp onto the ATPase head domains of the two SMC subunits (Smc1/Smc3 in mitotic cohesin), thereby closing the tripartite cohesin ring that topologically entraps DNA and holds sister chromatids together from S phase until anaphase. The ring is opened at the metaphase-to-anaphase transition by separase-mediated proteolytic cleavage of the kleisin.

The conserved core function across the family is **kleisin-mediated bridging of SMC heads to form a DNA-entrapping ring that mediates sister chromatid cohesion**. The family shows clear **subfunctionalization rather than neofunctionalization**: the mitotic kleisin (RAD21/Scc1) and the meiosis-specific kleisin (REC8, cleaved by separase to drive the two meiotic divisions) perform the same fundamental ring-closing/cleavage chemistry but are deployed in different cell-cycle programs, and vertebrates carry an additional meiotic paralog RAD21L. All retain the defining separase-cleavage and SMC-binding architecture.

## Subfamily Analysis

### PTHR12585:SF69 - FI11703P (the anchor subfamily)
**Members**: ~4 of the curated reference set

**Key Members**:
- *S. pombe* rad21 (P30776) — **the S. pombe anchor gene**
- *Xenopus laevis* rad21 (O93310)
- *S. cerevisiae* MCD1/Scc1 (Q12158)
- *Arabidopsis thaliana* SYN4 (Q8W1Y0)

**Function**: Mitotic alpha-kleisin; bridges Smc1/Smc3 heads, mediates mitotic sister chromatid cohesion, and is cleaved by separase at anaphase. **The S. pombe anchor gene rad21 (P30776) belongs to this subfamily (PTHR12585:SF69), consistent with its UniProt cross-reference `DR PANTHER; PTHR12585:SF69`.** Note this subfamily groups the canonical fungal/plant mitotic kleisins (Scc1-type) together with the *Xenopus* rad21.

### PTHR12585:SF20 - DOUBLE-STRAND-BREAK REPAIR PROTEIN RAD21 HOMOLOG
**Members**: ~4

**Key Members**:
- Human RAD21 (O60216)
- Mouse Rad21 (Q61550)
- Bovine RAD21 (Q3SWX9)

**Function**: Vertebrate mitotic RAD21 kleisin — functionally equivalent to the fungal Scc1/rad21 of SF69, separated by phylogenetic divergence rather than functional change.

### PTHR12585:SF27 - MEIOTIC RECOMBINATION PROTEIN REC8 HOMOLOG
**Members**: ~4

**Key Members**:
- Human REC8 (O95072)
- Mouse Rec8 (Q8C5S7), Rat Rec8 (Q6AYJ4)
- *C. elegans* rec-8 (Q9XUB3)

**Function**: Meiosis-specific kleisin. REC8 replaces RAD21 in the meiotic cohesin complex and its stepwise (arm then centromeric) separase cleavage underlies the reductional and equational meiotic divisions. The fission yeast meiotic ortholog rec8 (P36626) sits in the related SF72.

### PTHR12585:SF19 - DOUBLE-STRAND-BREAK REPAIR PROTEIN RAD21-LIKE PROTEIN 1
**Members**: ~3

**Key Members**:
- Human RAD21L1 (Q9H4I0)
- Mouse Rad21l1 (A2AU37)
- Giant panda RAD21L1 (D2HSB3)

**Function**: Vertebrate meiosis-specific kleisin paralog RAD21L, which cooperates with REC8 in establishing meiotic chromosome axes.

### Other subfamilies
Additional fungal/plant kleisins occupy singleton or small subfamilies, e.g. *S. pombe* rec8 (P36626, SF72), *S. cerevisiae* REC8 (Q12188, SF51), and the *Arabidopsis* SYN1/2/3 paralogs (SF64/SF73/SF55) reflecting plant expansion of the kleisin family.

## IBA Annotation Assessment

The following IBA (GO_REF:0000033, ECO:0000318) annotations were propagated to the anchor gene **rad21 (P30776)**. None of these are CROSS_SUBFAMILY-flagged in `iba_propagation.tsv`; all propagate within or consistently with the kleisin core function.

| GO ID | Label | Aspect | Node | Our action | Assessment |
|-------|-------|--------|------|------------|------------|
| GO:0030892 | mitotic cohesin complex | CC | PTN000971622 | ACCEPT | **Appropriate.** Rad21 is the defining kleisin of the mitotic cohesin complex; this is the core localization. Flagged LOCALIZATION/NO_UNIPROT_SEEDS only as triage, not a verdict. |
| GO:0007064 | mitotic sister chromatid cohesion | BP | PTN000971622 | ACCEPT | **Appropriate.** Core conserved biological process of the mitotic kleisin; experimentally established for S. pombe rad21. |
| GO:1990414 | replication-born double-strand break repair via sister chromatid exchange | BP | PTN000286904 | KEEP_AS_NON_CORE | **Appropriate but non-core.** Cohesin contributes to DSB repair via the sister template; this is a genuine but secondary role relative to cohesion. Correctly retained as non-core. |
| GO:0003682 | chromatin binding | MF | PTN000286904 | ACCEPT | **Appropriate.** Cohesin is loaded onto and bound across chromatin; broadly conserved across the family. |

**Verdict**: All IBA propagations to rad21 are appropriate. They reflect the conserved kleisin core function (cohesin ring component, sister chromatid cohesion, chromatin association) and a correctly down-weighted DSB-repair role. No over-propagation (no contradicting localization terms from sibling subfamilies; no paralog-specific functions misapplied).

## Review Status

- **Date**: 2026-06-07
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER/InterPro metadata and member tables, S. pombe rad21 UniProt and GOA (IBA) records, the curated rad21 ai-review, and `projects/PANTHER_IBA_REVIEW/iba_propagation.tsv`
