# ALPK2 (Q86TB3) review notes

## 2026-10-04: PAINT/affinage review

**Affinage trust gate:** a blocking "symbol collision" gate fired because the narrative opens with zebrafish. I quarantined the output with --out and read it. It describes ALPK2 (hESC, zebrafish and mouse studies of the same gene), so I wrote it with --force and recorded this in reference_review.

The cardiogenesis role is contested across species:
- **hESCs and zebrafish:** [PMID:29888752 "Using antisense knockdown and CRISPR/Cas9 mutagenesis in hESCs and zebrafish, we demonstrate that ALPK2 promotes cardiac function and cardiomyocyte differentiation."]
- **Mouse knockouts:** [PMID:32383995 "We found that Alpk2-gKO mice exhibited normal cardiac function and morphology up to one year of age."]
- **UniProt** carries a CAUTION on the same point.

Decisions:
- **Kinase, Ser kinase and ATP binding (IEA): ACCEPT.**
- **All cardiac IMP and IEA rows: KEEP_AS_NON_CORE.** The curator's hESC evidence is not overruled, but the role is not established for the mammalian organism.
- **Colon 3D-culture rows** (apoptosis, gene expression; PMID:22641666) and **variant-study rows** (polarity, basolateral membrane; PMID:28668886): KEEP_AS_NON_CORE.
- **No NEW.** Tropomyosin 1 phosphorylation is indirect (overexpression; PMID:39556326).
