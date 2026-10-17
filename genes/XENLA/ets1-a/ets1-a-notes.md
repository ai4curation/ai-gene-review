# ets1-a (P18755, Xenopus laevis) — review notes

Project context: `projects/NEURAL_CREST_ORIGINS.md`, Tier 1 (neural crest specifiers,
candidate vertebrate innovations). Task: place Ets1 in the correct NC GRN layer and
check whether its GO annotations reflect that.

## Identity

- UniProt P18755 "Protein c-ets-1-A", 438 aa; PNT (SAM/pointed) domain 49-134, ETS
  DNA-binding domain 332-412, autoinhibitory helices HI-1/HI-2/H4/H5 flanking the ETS
  domain (by similarity to mouse P27577). Xenbase cross-reference: ets1.S
  (XB-GENE-6254436). The second homeolog (ets1b / ets1.L) exists; most frog
  loss-of-function reagents knock down both.
- All 21 existing GOA rows are electronic or ISS/IBA; there is no Xenopus experimental
  annotation on P18755.

## Molecular activity

- Classic ETS-family sequence-specific transcription factor; activator in most contexts.
  In chick cranial NC, Ets1 directly binds and activates the Sox10E2 enhancer
  [PMID:20139305 "ChIP, DNA-pull down, and gel-shift assays demonstrate their direct binding to the Sox10E2 enhancer in vivo, whereas mutation of their corresponding binding sites, or inactivation of the three upstream regulators, abolishes both reporter and endogenous Sox10 expression."]
- In Xenopus, overexpressed Ets1a binds the id3 promoter and recruits HDAC1 to repress
  it (context-dependent repression)
  [PMID:26198637 "Mechanistically, we found that Ets1 binds to id3 promoter as well as histone deacetylase 1, suggesting that Ets1 recruits histone deacetylase 1 to the promoter of id3, thereby inducing histone deacetylation of the id3 promoter."]
  The construct was explicitly the ets1a ORF [file:XENLA/ets1-a/ets1-a-deep-research-falcon.md "FLAG-tagged frog Ets1a occupied its predicted binding region in embryo chromatin-immunoprecipitation assays."]
  Note: this is a gain-of-function result; excess Ets1 represses NC markers, so it is
  a dosage effect rather than evidence that Ets1 normally inhibits NC formation.
- Cofactor: Vgll3 [PMID:28870996 "These results demonstrate that vgll3 can interact with ets1 and stimulate a MCAT element-dependent gene promoter."]

## Expression

- Xenopus: maternal, then NC and derivatives, plus hemangioblast/endothelial lineages
  [PMID:9303349 "In neurula and tailbud stages, ets-1 and ets-2 transcripts are detected in neural crest cells and their derivatives."]
  [PMID:9303349 "Specific transcription can also be observed for ets-1 in the hemangioblastic precursors, in endothelial cells of the forming heart and blood vessels."]
- Pre-migratory and migratory crest [PMID:32713114 "The proto-oncogene ets1 is highly expressed in the pre-migratory and migratory neural crest (NC), and has been implicated in the delamination and migration of the NC cells."]
- Chick: onset at HH7-8 in cranial neural folds, AFTER the border genes, maintained in
  migrating crest [PMID:27339986 "Onset of Tfap2b, Sox8 and Ets1 expression was observed later at HH7 and HH8, in neural crest progenitors residing within the cranial neural folds"]

## Network position (layer)

- Chick cranial NC circuit: Brn3c/Lhx5/Dmbx1 (anterior border) -> Tfap2b/Sox8 -> Ets1
  [PMID:27339986 "Finally, Tfap2b activates expression of Ets1 as the neural crest becomes specified"]
- Ets1 (with Sox9, cMyb) is a direct input to the cranial Sox10 enhancer
  [PMID:20139305 "Three transcription factors, Sox9, Ets1, and cMyb, acting via one of the identified enhancers, Sox10E2, are required for direct initial activation of endogenous Sox10 expression and the specification of delaminating/migrating cranial NC."]
- Gain of function/sufficiency: Sox8 + Tfap2b + Ets1 reprogram trunk NC to cranial
  identity and chondrogenic potential; Ets1 alone insufficient
  [PMID:27339986 "Thus, introducing components of the cranial-specific transcriptional circuit is sufficient to reprogram trunk neural crest and to drive them to adopt an additional cartilaginous fate."]
  [PMID:27339986 "Early cranial-specific factors (Brn3c, Lhx5 and Dmbx1), or individual late factors, were unable to activate the cranial enhancer in the trunk."]
- Ets1 required for Alx1 in facial mesenchyme [PMID:27339986 "We found that Ets1 was required for the expression of ALX Homeobox 1 (Alx1, also known as Cartilage Paired-Class Homeoprotein 1) in the facial mesenchyme"]
- Chick delamination: Ets1 required and sufficient for cranial-type cell recruitment
  [PMID:17987123 "We show that ets-1 promotes massive cell recruitment and induces local degradations of the basal lamina, two separable events which are sufficient to initiate ectopic delaminations."]
  [PMID:17987123 "Altogether, these data show a specific requirement of ets-1 in cranial NCCs delamination."]

**Conclusion on layer:** Ets1 is NOT a neural plate border specifier (onset is after
border genes, downstream of Tfap2b) and not a competence/pluripotency factor. It is a
late neural crest specifier / cranial-identity factor whose principal Xenopus
loss-of-function output is delamination and migration rather than initial induction.

## Xenopus loss of function

- Ets1 MO (both homeologs) — initial foxd3/snai2 not prevented, migration/streams
  disrupted [file:XENLA/ets1-a/ets1-a-deep-research-falcon.md "Thus, impaired migration and delamination are better-established physiological outcomes than an absolute requirement for initial whole-embryo crest induction."]
- NC-targeted vs heart-mesoderm-targeted MO
  [PMID:25691536 "Using a translation-blocking antisense morpholino to knockdown Ets1 protein selectively in the NC, we observed defects in NC delamination from the neural tube, collective cell migration, as well as segregation of NC streams in the cranial and cardiac regions."]
  [PMID:25691536 "The formation of the primitive heart tube was dramatically delayed and the endocardial tissue appeared depleted."]
- Downstream msmb3 (X. tropicalis mutant RNA-seq; X. laevis follow-up)
  [PMID:32713114 "Among them, the expression of microseminoprotein beta gene 3 (msmb3) was positively regulated by Ets1 in both X. laevis and X. tropicalis."]

## Evolution (outgroup)

- Lamprey: Ets1 absent from premigratory/migratory NC; deployed later than in amniotes
  [PMID:31645763 "In contrast to amniotes, our results show that Brn3, Lhx5, Dmbx1, and Ets1 appear to be absent from lamprey premigratory or migratory NC (Fig 1B)."]
- Little skate has it: gnathostome acquisition
  [PMID:31645763 "Since Ets1 appears in the little skate migratory NC as in other gnathostomes, we conclude that this early node was a novelty acquired by the cranial NC GRN prior to divergence of cartilaginous and bony fishes (Fig 2A,B, SupFig2)."]
- So Ets1's NC role is a gnathostome-level recruitment (not even pan-vertebrate),
  consistent with the project's Tier 1 framing, and verifies the PMID:27339986 claim
  (it is the chick cranial circuit Sox8/Tfap2b/Ets1).

## Annotation decisions (summary)

- MF: ACCEPT RNAPII-specific DNA-binding TF activity; MODIFY generic DNA binding to
  RNAPII cis-regulatory region sequence-specific DNA binding; NEW activator activity
  (GO:0001228), based on direct Sox10E2 activation by the ortholog.
- BP: NEW neural crest cell migration (GO:0001755) and neural crest cell delamination
  (GO:0036032); NEW endocardium development (GO:0003157). Comparator check: Xenopus
  TFs hic1.L, kmt2d.L, sox10.S, snai2.S carry GO:0001755; chick SOX9 carries
  GO:0036032. Not proposing neural crest cell fate specification: in Xenopus initial
  specifier expression is not Ets1-dependent; the chick Sox10E2 data are a question
  for experts.
- Vascular/erythroid ISS terms (from human ETS1 cell-culture work) kept as non-core
  or flagged; endothelial expression in frog supports the vascular ones.
- Cytoplasm: non-core.
