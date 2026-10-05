# GHSR: ProtNLM function-text review

**PLI (score 0) for oxytocin-receptor identity; the G-protein/PLC-calcium signaling clause is compatible with GHSR.**

## Original prediction

[ProtNLM F6QF00](https://www.uniprot.org/uniprotkb/F6QF00/entry#prot-nlm), frozen API snapshot 2026-09-08.

> Receptor for oxytocin. The activity of this receptor is mediated by G proteins which activate a phosphatidylinositol-calcium second messenger system

## Atomic assessment

| Claim | Assessment | Evidence |
|---|---|---|
| Receptor for oxytocin | PLI | The complete conserved receptor is GHSR, with the ghrelin-receptor architecture and ligand-pocket conservation. |
| Activity mediated by G proteins | Supported | Cloning/pharmacology and ghrelin-bound G-protein complex structures directly establish coupling. |
| Phosphatidylinositol-calcium second messengers | Supported mammalian inference | GHSR couples through Gq/PLC; this shared downstream pathway does not determine oxytocin specificity. |

[PMID:35027551](https://pubmed.ncbi.nlm.nih.gov/35027551/) reports the “active ghrelin receptor-Go complex bound to the endogenous agonist ghrelin.” The [full-length horse alignment](GHSR-bioinformatics/RESULTS.md) gives 348/366 identities (95.1%) with no missing receptor segment. Conserved subfamily identity and molecular structure justify transferring ghrelin specificity rather than an unrelated peptide-GPCR specificity. This is a family inference, not an unreported horse binding assay.

The horse-specific [PMID:42426797](https://pubmed.ncbi.nlm.nih.gov/42426797/), DOI [10.1186/s12917-026-05700-8](https://doi.org/10.1186/s12917-026-05700-8), confirms GHSR1a amplicon identity in equine pituitary/adrenal medulla. It supports the relevant horse locus/expression context but does not test oxytocin pharmacology. **PARALOG_OVERANNOTATION** describes the wrong peptide-receptor subfamily assignment; the exact model donor is unknown.

A separate annotation error occurs in ordinary GOA: horse GHRH-receptor activity (GO:0016520) is transferred from human GHSR despite the cited discovery paper explicitly distinguishing GHRH from ghrelin. This is corrected in both main reviews and does not serve as evidence that ProtNLM is correct.
