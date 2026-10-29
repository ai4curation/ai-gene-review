# GHSR: ProtNLM function-text review

**PLI (score 0) for oxytocin-receptor identity; G-protein coupling is correct but already annotated (CNN), and phosphatidylinositol-calcium signaling is correct and more specific than existing annotation (COR).**

## Original prediction

[ProtNLM F6QF00](https://www.uniprot.org/uniprotkb/F6QF00/entry#prot-nlm), frozen API snapshot 2026-09-08.

> Receptor for oxytocin. The activity of this receptor is mediated by G proteins which activate a phosphatidylinositol-calcium second messenger system

## Atomic assessment

| Claim | Assessment | Evidence |
|---|---|---|
| Receptor for oxytocin | PLI | The complete conserved receptor is GHSR, with the ghrelin-receptor architecture and ligand-pocket conservation. |
| Activity mediated by G proteins | CNN | Cloning/pharmacology and ghrelin-bound G-protein complex structures directly establish coupling; horse GHSR already carries G protein-coupled receptor signaling pathway (GO:0007186) in GOA. |
| Phosphatidylinositol-calcium second messengers | COR | GHSR agonists stimulate inositol phosphate turnover through Gq/PLC; horse GOA carries only the parent GPCR-signaling term. This shared downstream pathway does not determine oxytocin specificity. |

[PMID:35027551](https://pubmed.ncbi.nlm.nih.gov/35027551/) reports the “active ghrelin receptor-Go complex bound to the endogenous agonist ghrelin.” The [full-length horse alignment](GHSR-bioinformatics/RESULTS.md) gives 348/366 identities (95.1%) with no missing receptor segment. Conserved subfamily identity and molecular structure justify transferring ghrelin specificity rather than an unrelated peptide-GPCR specificity. This is a family inference, not an unreported horse binding assay. For the second-messenger clause, [PMID:12907757](https://pubmed.ncbi.nlm.nih.gov/12907757/) reports that “Ghrelin and a number of the known nonpeptide GH secretagogues acted as agonists stimulating inositol phosphate turnover further” in cells expressing the ghrelin receptor. Horse GHSR GOA and the gene review carry G protein-coupled receptor signaling pathway but no phospholipase C-activating or phosphatidylinositol-mediated signaling term, so this more specific clause is novel for the gene.

The horse-specific [PMID:42426797](https://pubmed.ncbi.nlm.nih.gov/42426797/), DOI [10.1186/s12917-026-05700-8](https://doi.org/10.1186/s12917-026-05700-8), confirms GHSR1a amplicon identity in equine pituitary/adrenal medulla. It supports the relevant horse locus/expression context but does not test oxytocin pharmacology. **PARALOG_OVERANNOTATION** describes the wrong peptide-receptor subfamily assignment; the exact model donor is unknown.

A separate annotation error occurs in ordinary GOA: horse GHRH-receptor activity (GO:0016520) is transferred from human GHSR despite the cited discovery paper explicitly distinguishing GHRH from ghrelin. This is corrected in both main reviews and does not serve as evidence that ProtNLM is correct.
