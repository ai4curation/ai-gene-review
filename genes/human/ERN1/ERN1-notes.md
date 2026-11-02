# ERN1 (IRE1alpha, human, O75460) review notes

Deep research: not run (falcon times out in this environment; perplexity-lite unavailable).
Review based on cached GOA-cited publications and the UniProt entry.

## Key findings
- Bifunctional kinase/RNase ER stress sensor; autophosphorylation and HAC1 5' splice-site cleavage
  [PMID:9637683 "hIre1p expressed in mammalian cells displayed intrinsic autophosphorylation activity and an endoribonuclease activity that cleaved the 5' splice site of yeast HAC1 mRNA"]
- RNase activity depends on autophosphorylation; competent kinase on heterologous peptide
  [PMID:21317875 "We show that the Xbp1-specific ribonuclease activity depends on autophosphorylation"]
- XBP1 mRNA is the mammalian substrate [PMID:11779464]; splicing occurs in the cytoplasm [PMID:19622636].
- BiP/ERdj4 keep IRE1 monomeric [PMID:29198525 "ERdj4 associates with IRE1LD and recruits BiP through the stimulation of ATP hydrolysis, forcibly disrupting IRE1 dimers."]
- TRAF2-JNK output [PMID:10650002].

## Curation decisions
- 16 protein binding rows REMOVE; the BiP (HSPA5) row MODIFY to GO:0030544 Hsp70 protein binding.
- `positive regulation of RNA splicing` -> MODIFY to GO:0070054 (IRE1 performs the cleavage).
- identical protein binding -> MODIFY to GO:0042803.
- Indirect physiology (insulin metabolism, H2O2 response, mitochondrion, inner nuclear membrane, positive regulation of ER UPR) marked over-annotated.
- Core MFs: GO:0004521 RNA endonuclease activity; GO:0004674 protein Ser/Thr kinase activity; GO:0042803 homodimerization.

## 2026-10-25 ORGANELLES batch 3 (mitochondrion rows)

Row: GO:0005739 IEA (GO_REF:0000107, Ensembl projection from mouse Q9EQY0). No sub-compartment
rows; no MAM (GO:0044233) row in GOA.

Checks:
- QuickGO (2026-10-25): mouse Q9EQY0's only GO:0005739 row is an MGI IDA from PMID:23028046
  (Ha et al. 2012, anthrax lethal toxin and MLN64 in macrophages). The cached copy is
  abstract-only and does not mention IRE1/Ern1; Europe PMC and BioC full text for PMC3497600
  could not be retrieved, so the assay behind the MGI row is unknown and not called wrong.
- Human ERN1: [file:human/ERN1/ERN1-uniprot.txt "SUBCELLULAR LOCATION: Endoplasmic reticulum
  membrane {ECO:0000269|PubMed:9637683}; Single-pass type I membrane protein"], signal peptide
  1-18, TM 444-464. Not in MitoCarta3.0 (evidence column: "mito protein domain" only).
- An ER-membrane protein enriched at ER-mitochondria contacts will co-purify with crude
  mitochondrial fractions (STOM lesson).

Outcome: row stays MARK_AS_OVER_ANNOTATED (not REMOVE: the projection faithfully transfers a
real MGI row). No sub-compartment row. A MAM row would need a cached source showing IRE1 at
MAM with a MAM marker; none is cached here.
