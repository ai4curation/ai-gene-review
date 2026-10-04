# Alpi review notes

## Evidence summary
- [UniProtKB:P15693] UniProt describes Alpi as an alkaline phosphatase that hydrolyzes phosphate compounds.
- [PMID:2155025] UniProt cites this publication for GPI anchoring/plasma-membrane context.
- [PMID:24076154] UniProt and GOA cite this publication for alkaline phosphatase activity and metal-ion binding.

## Curation decisions
- Core function: intestinal alkaline phosphatase 1 (alkaline phosphatase activity, GO:0004035).
- Specific catalytic activities and direct metabolic processes were accepted.
- Broad parent, localization, binding, and stimulus-response annotations were modified, kept non-core, or marked over-annotated according to support.

## Re-review 2026-10-04

**GOA changes:** none relevant. The refresh added no new rows and retired none (20 rows, all previously reviewed); qualifiers and WITH/FROM were backfilled.

**Actions changed:**
- GO:0005515 protein binding (IPI, PMID:24076154): MARK_AS_OVER_ANNOTATED -> MODIFY to GO:0042803 protein homodimerization activity, following the protein-binding policy. WITH/FROM is P15693 itself, i.e. the homodimer [UniProtKB:P15693 "SUBUNIT: Homodimer."].
- No other action changes.

**Supporting evidence fixed:**
- Several ACCEPT/KEEP rows cited a sentence that did not support the claim (the prodrug-cleavage intro of PMID:24076154, the modelling sentence of PMID:15885097, the cDNA C-terminus sentence of PMID:7744844), or quoted UniProt DR GO lines, which is circular. One DR-line quote had also drifted after the UniProt refresh (plasma membrane now EXP:UniProtKB). Replaced them with claim-bearing quotes, e.g. [PMID:24076154 "Expression of rat IAP in Escherichia coli (rIAP-Ec) led to ~200-fold loss of activity that was partially recovered by the addition of external Zn(2+) and Mg(2+) ions."], [PMID:7744844 "evidence of surface membrane localization by immunofluorescence using antibody against rat intestinal alkaline phosphatase"], [PMID:2155025 "The cDNA transfected into COS-1 cells produced a membrane-bound IAP that was released by phosphatidylinositol-specific phospholipase (PI-PLC)."].
- GO:0071773 cellular response to BMP stimulus (ISO from mouse MGI:1924018): stays MARK_AS_OVER_ANNOTATED. Traced the donor to mouse IDA PMID:21324897 (now cached). That is an osteoblast miRNA study that used total ALP activity as a differentiation marker [PMID:21324897 "ALP activity and osteocalcin secretion, as markers of osteoblast differentiation, were evaluated after 48 h."]. The source_status is now SOURCE_WEAK_OR_INFERRED and the comment was corrected.
- GO:0002020 protease binding (ISO from human ALPI P09923): stays KEEP_AS_NON_CORE. Traced the donor to IPI PMID:18307834 [PMID:18307834 "Cathepsin C propeptide interacted with proteins with a molecular mass of approximately 70 kDa, including IAP and heat shock cognate protein 70."]. The boilerplate reason was replaced.
- GO:0000287 magnesium ion binding (IDA, PMID:15885097): stays KEEP_AS_NON_CORE, but the reason now notes a discrepancy. The abstract predicts a zinc triad at the rIAP-I active site [PMID:15885097 "These data are consistent with the presence of a triad of zinc atoms at the active site of rIAP-I, but not rIAP-II or hPLAP."], while Mg(2+) is a crystallographically supported cofactor of rat IAP (UniProt COFACTOR, PMID:24076154).

**Description / core_functions:** removed the curation commentary from the description ("The review accepts...", "Falcon deep research corroborates..."). Rewrote it and the core function text as standalone biology.

**Open questions:**
- Does the magnesium ion binding IDA from PMID:15885097 really apply to IAP-I (P15693), given the abstract's zinc-triad model for rIAP-I? Should it be an IAP-II (Alpi2) annotation?
- Is the mouse BMP-response IDA (PMID:21324897) correctly attributed to mouse Alpi rather than tissue-nonspecific Alpl, given that the assay is total ALP activity in ST2 stromal cells?
