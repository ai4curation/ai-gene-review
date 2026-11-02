# Brn1/2/4 (Sp-Brn1/2/4, brn1/2/4) — curation notes

UniProt A0A7M7GMA5 (unreviewed, "POU domain protein", 467 aa), GeneID 577601 (NCBI gene
description "brain 1/2/4", alias brn1/2/4, other designation "POU domain, class 3,
transcription factor 4"), PANTHER PTHR11636:SF89. Organism Strongylocentrotus purpuratus
(NCBITaxon:7668).

## Identity of the UniProt entry

- The UniProt entry carries no literature RX lines; it is a genome-project translation
  (RefSeq XP_003729178.1 / LOC577601). Identity with the GRN gene rests on (i) the NCBI
  Gene record for 577601, whose description is "brain 1/2/4" with alias "brn1/2/4" and
  designation "POU domain, class 3, transcription factor 4", retrieved via eutils; (ii) the
  PANTHER subfamily PTHR11636:SF89 (a class III POU / Brn-related subfamily) and PROSITE
  POU-specific + homeobox domains, matching the Yuh et al. description of a POU factor
  "related closely to the mammalian factors Brain-1, -2, and -4"; and (iii) the single
  class III POU gene in the sea urchin genome, for which the human Brn1/Brn2/Brn4/Oct6 are
  equal co-orthologs [PMID:30450080 "The human genes Brn1, Brn2, Brn4, and Oct6 are all
  equal co-orthologs of the sea urchin gene SpBRN1/2/4"].
- Confidence that A0A7M7GMA5 is the brn1/2/4 of the Davidson endoderm GRN: HIGH.

## What the gene is

- Cloned as the predicted midgut regulator of endo16 [PMID:15893979 "The cDNA sequence
  reveals it to be a POU domain factor related closely to the mammalian factors Brain-1, -2,
  and -4. The factor was termed SpBrn1/2/4 (henceforth Brn1/2/4)."].
- Class III POU homeodomain TF (POU-specific domain 219-293, homeodomain 309-369 in the
  UniProt entry); in vertebrates the class III POU genes are neural regulators
  [PMID:26657764 "Brn1/2/4 is related to three Class III POU domain transcription factors
  expressed in vertebrate embryos that have demonstrated roles in neural specification"].

## Expression

- Maternal transcripts decay to undetectable at blastula [PMID:26657764 "Brn1/2/4 is also
  expressed maternally, and transcripts gradually decrease in abundance until they are
  undetectable at the blastula stage"].
- Zygotic activation in the endoderm: first detectable in the 20-h blastula at ~100
  molecules/embryo, then an abrupt 10-fold rise at the onset of gastrulation; late endo16
  rise follows that of brn1/2/4 [PMID:15893979 "the gene is first activated in the 20-h
  blastula, but there remain only about 100 molecules of brn1/2/4 mRNA per embryo (only a
  few per endoderm cell) until an abrupt 10-fold increase occurs as gastrulation begins"].
- Spatial domain in the gut: Yuh et al. described it as confined to the midgut
  [PMID:15893979 "As predicted by the endo16 model, brn1/2/4 expression is confined
  perfectly to the midgut, coincident with the domain of endo16 expression."], whereas a
  later FISH study assigns the endodermal domain to the foregut and adds two ectodermal
  domains [PMID:19250980 "Endodermal expression of this gene is restricted to the foregut.
  SpBrn1/2/4 is also expressed in two distinct ectodermal domains: throughout the stomodeal
  ectoderm, and within cells scattered throughout the ciliated band."]. The discrepancy
  (midgut vs foregut) is unresolved in the cached literature; it may reflect stage or
  probe/method differences. Both studies agree that the gene is a gut-endoderm regulatory
  gene.
- In the Peter & Davidson 2011 endoderm GRN, brn1/2/4 is one of the regulatory genes that
  come on in veg2-derived (anterior endoderm) cells in the last hours before gastrulation
  [PMID:21623371 "A few additional regulatory genes are activated in the final hours before
  gastrulation: brn1/2/4, gatae, dac and tgif are expressed in veg2-derived cells and hnf1
  is expressed in the veg1 endoderm domain by 27 h after fertilization."].

## Place in the endoderm GRN

- Input: Blimp1 (veg2 endoderm) activates brn1/2/4 [PMID:21623371 "Blimp1 then activates
  brn1/2/4 and tgif expression (Fig. 1f)."]. The veg1 regulator Eve affects it only
  indirectly, through a proposed veg1-to-veg2 signal [PMID:21623371 "blimp1b, brn1/2/4,
  gatae and tgif, which continue to be expressed in veg2 endoderm, are indirectly affected
  by the knockdown of eve expression in veg1 descendants (Fig. 1f)"].
- Upstream of it sit the post-gastrular midgut specification genes [PMID:15893979 "The
  brn1/2/4 gene lies downstream of the regulatory genes executing post-gastrular
  specification of the midgut, as shown by further gene expression perturbation
  experiments"].
- Output 1, endo16 (the midgut differentiation gene whose cis-regulatory analysis predicted
  this factor): Brn1/2/4 MASO blocks the late phase of endo16 transcription and abolishes
  expression driven by cis-regulatory Module B, leaving Module A untouched [PMID:15893979
  "Arrest of Brn1/2/4 translation by MASO treatment blocks the late phase of endo16
  expression and specifically abolishes expression of cis-regulatory Module B of endo16,
  while not affecting Module A, also as predicted."]. This is a module-specific, sign-
  positive effect, i.e. Brn1/2/4 is an activator acting through Module B.
- Output 2 (predicted site): the blimp1/krox 1a midgut/hindgut cis-regulatory module
  carries Brn1/2/4 sites [PMID:16798107 "Its sequence contains binding sites for Brn1/2/4,
  Otx, and Blimp1/Krox itself, as predicted in a prior regulatory network analysis."].
- The brief for this review mentioned brn1/2/4 inputs into foxa and gatae; the cached
  Peter & Davidson 2011 text does not state these linkages explicitly (they would be in
  Fig. 4 / the supplementary perturbation tables), so they are not asserted here.
- Not present in Smith & Davidson 2008 (PMID:19104065) or Peter & Davidson 2010
  (PMID:19895806, pre-mid-blastula GRN): consistent with its late (>20 h) activation.

## Second role: neurogenesis

- Wei, Angerer & Angerer 2016 placed Brn1/2/4 downstream of SoxC in the neurogenic pathway
  [PMID:26657764 "Using a combination of molecular screens and tests of gene function by
  morpholino-mediated knockdown, we identified SoxC and Brn1/2/4 , which function
  sequentially in the neurogenic regulatory pathway and are also required for the
  differentiation of all neurons."] and [PMID:26657764 "We conclude that Brn1/2/4 is
  required for the development of serotonergic and all SynB -expressing neurons and can
  directly or indirectly drive the production of excess neurons at low dose"].
- SoxC MASO removes the scattered ectodermal (neural precursor) Brn1/2/4 expression but
  not the foregut expression [PMID:26657764 "in SoxC morphants, labeling of individual
  ectoderm cells for Brn1/2/4 transcripts was dramatically reduced, whereas expression in
  the foregut was not detectably affected"], so the endodermal and neural inputs are
  separate.
- Later larval neurons co-expressing SpLox and Brn1/2/4 are lateral ganglion neurons with a
  "pre-pancreatic" signature [PMID:30450080].

## GOA audit summary

- All 10 GOA rows are electronic (4 IBA from PAINT node PTN000180816, 6 IEA). The TF rows
  (GO:0000981, GO:0000978, GO:0006357, nucleus) are directly supported on the target by the
  endo16 Module B MASO result; the generic parents (GO:0003677, GO:0003700, GO:0006351,
  GO:0006355) are proposed for MODIFY to their Pol II-specific children. GO:0090575
  (transcription regulator complex) has no sea urchin evidence and is kept as non-core.
- NEW: GO:0001228 (activator activity, IMP), GO:0045944 (IMP), GO:0048565 digestive tract
  development (IMP, via endo16 gut differentiation gene), GO:0045666 positive regulation of
  neuron differentiation (IMP, Wei 2016).
