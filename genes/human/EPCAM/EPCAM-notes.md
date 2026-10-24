# EPCAM review notes

## Biological interpretation

EPCAM is a single-pass epithelial surface glycoprotein with a well-supported lateral/basolateral membrane pool. The clearest molecular relationship in the inspected human experiments is association with claudin-7 and stabilization of a claudin-containing pool. Endogenous co-immunoprecipitation, lysosomal inhibition and a binding-impaired transmembrane mutant support this relationship (PMID:23486470, Figures 5–10). Claudin-1 can associate through claudin-7; a ternary recovery does not establish every possible binary contact.

The traditional model in which EpCAM itself forms adhesive trans oligomers is disputed. Rat EpCAM construct experiments show effects on aggregation and cell-monolayer adhesion (PMID:19276185), while later biochemical and cellular experiments distinguish cis association from trans interactions and fail to detect the proposed homophilic bond under the tested conditions (PMID:30185875, Figures 2–5). The broad contribution to epithelial contacts is retained without assigning a direct homophilic adhesion-mediator activity. [The source guide](EPCAM-source-guide.md) details species, constructs, controls and access.

Proliferation and differentiation effects depend on context. Human embryonic stem-cell knockdown decreases cell counts and changes lineage output (PMID:19785009), whereas human intestinal cell lines respond differently (PMID:23486470). These are supported regulatory phenotypes; they are not evidence that EPCAM is a cell-cycle enzyme or that a single direction applies in every epithelium. The stem-cell differentiation term is refined because the experiment begins with established stem cells and measures subsequent lineage differentiation, whereas GO:0048863 describes acquisition of stem-cell features.

Released EpICD is associated with FHL2 and a nuclear assembly containing LEF1 and beta-catenin, with transcriptional reporter effects (PMID:19136966, actual main figures and supplement). Human promoter ChIP provides further complex-associated evidence (PMID:20064925). Neither a ChIP signal nor an EMSA from a protein assembly proves direct DNA recognition by EPCAM. Other proteins execute the proteolysis; being the cleavage substrate does not give EPCAM protease activity or participation in the cleavage process. No new process annotation is proposed.

## Products and Mendelian mechanisms

The normal UniProt record and independent official FASTA agree on one displayed 314-residue precursor. The signal peptide is 1–23, processed chain 24–314, extracellular topology segment 24–265, membrane helix 266–288 and cytoplasmic segment 289–314. Sequence SHA256 is `e5d527336d82e9309b5ea19a32a85ad410a303db94b245801462e791abd1623c`. No alternative splice product is enumerated in the source record. EpEX/EpICD are proteolytic products, and a recombinant cytoplasmic-tail construct does not establish an exact endogenous cleavage boundary.

Human congenital tufting enteropathy variants and altered EPCAM RNA/protein were inspected in PMID:18572020. Its pathogenic exon-skipped product is not added as a normal isoform. The separate Lynch syndrome mechanism described in PMID:19098912 is transcriptional read-through and silencing of neighboring MSH2 after certain EPCAM genomic deletions. That abstract-supported disease mechanism is not attributed to EpCAM protein as methyltransferase or DNA-repair activity.

## Annotation outcomes and open boundaries

All 40 imported annotations have manual decisions: 17 ACCEPT, 13 KEEP_AS_NON_CORE, 6 MODIFY and 4 UNDECIDED. Imported terms, evidence, citations, partners and source flags are preserved. Supported generic interactions remain non-core when no narrower function is established. The refinements identify claudin-associated cell adhesion molecule binding, cadherin binding, NEK7 kinase binding, plasma membrane, and regulation of cell differentiation. No new annotations or publication quotations were added.

Four uncertainties remain. The ureteric-bud development transfer traces to a mouse expression study whose complete original was unavailable. Three tight-junction annotations retain uncertainty because the older tissue localization experiments were inaccessible and later human intestinal imaging places EPCAM below the tight junction. Valid PAINT ancestry and the correct UniProt location mapping are preserved; one context's negative localization does not establish a universal absence.

The human interaction screen's actual supplementary rows were inspected for all five partners. These are human cDNA-fragment Y2H results, with no established pair-specific mammalian validation. In particular, a CDH1 interaction does not establish that EPCAM binds cadherin across a physiological cell contact, and interaction with CDK5R1 does not make its partner the CDK5 catalytic subunit.

## Research and validation

The normal fetch produced 40 raw/TSV/seed contexts and 28 publication caches. The genuine Falcon command with Perplexity fallback failed; no provider-named substitute was authored. These notes and the source guide are manual research based on the actual originals and database sources described there. Four additional normal publication caches were genuinely acquired for cited supporting/donor studies; an already present PMID:20064925 was reused. Normal source caches and their acquisition flags were preserved.

Genuine normal whole-gene validation passed on 2026-10-24 with three advisories, all for retaining the supported generic CALR, DLST and CDK5R1 interactions as non-core under the campaign policy. Structured provenance records the two inspected IBA uncertainties/refinements. The normal status command reports DRAFT, with no status mismatch. All 32 normal publication caches and the imported source fields remain unchanged. No new environment or dependency installation was used.
