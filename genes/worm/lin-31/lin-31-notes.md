# lin-31 (C. elegans) research notes

UniProt: P34683 (LIN31_CAEEL, Swiss-Prot, PE 4 "Predicted"), 237 aa. ORF K10G6.1,
WormBase WBGene00003017, chromosome II. Forkhead (FOX) family; CDD FH_FOXB, PANTHER
PTHR11829:SF377. Human ortholog listed by the Alliance: FOXB2.

## Provenance of this research

- Automated deep research was **not available** for this review (no FutureHouse,
  Perplexity or OpenAI keys in this environment), so no `-deep-research-<provider>.md`
  file exists. The literature work below is manual.
- The WormBase hand-written description was fetched with
  `just mod-description-deep-research worm lin-31`
  (`lin-31-deep-research-wormbase.md`) and used as a recall checklist.
- Queries run (2026-11-16):
  - PubMed esearch `lin-31[tiab] AND elegans[tiab]` (18 hits) and
    `(LIN-31[tiab] OR "lin-31"[tw]) AND (elegans OR nematode)` (22 hits).
  - Europe PMC `"LIN-31" AND elegans` (205 hits, full-text mentions; scanned titles).
  - Web search for Clayton et al. 2008 (VPC quiescence) follow-up.
  - QuickGO by reference for PMID:18082681, 8504934, 10419688, 20042118, 23995389,
    9604932 (only the 9604932 nucleus IDA row exists for lin-31).
- Papers cached with `just fetch-pmid`: 8504934, 11102360, 8807292, 18082681, 16412617,
  12710960, 20042118 (full text), 10419688, 24885717 (full text), 30544993 (full text,
  review), 23995389 (full text). Full text was not retrievable (PMC 403, Europe PMC 500)
  for 11102360, 8807292, 18082681 and 11861555.

## Identity

- lin-31 encodes an HNF-3/fork head (FOX) transcription factor
  [PMID:8504934 "lin-31 encodes a member of the HNF-3/fork head family of DNA-binding
  transcription factors"]. Modern nomenclature places it in FoxB
  [PMID:18082681 "the LIN-1/Ets and LIN-31/FoxB transcription factors promote expression
  of CKI-1"; PMID:23995389 "lin-31, which encodes a FOXB transcription factor required for
  vulval development"].
- UniProt FUNCTION (curated, derived from the 1993 paper): "Lin-31 regulates how vulval
  precursor cells choose their fate. It helps specify three alternative cell fates in
  vulval development." Fork-head DNA-binding domain residues 12-103 (PROSITE PRU00089).
  The C-terminal half is predicted disordered (MobiDB-lite).

## Vulval cell fate specification (core biology)

- Genetics: lin-31 acts downstream of let-60/Ras
  [PMID:8504934 "We show that lin-31 acts downstream of the ras homolog let-60"]. Loss of
  lin-31 randomises VPC fates rather than simply removing or adding vulval fates
  [PMID:8504934 "in lin-31 mutants, these cells do not properly choose which fate to
  express and therefore adopt any one of the three possible vulval cell fates in a
  deregulated fashion"].
- Null alleles: most alleles are null and the forkhead DNA-binding domain is essential
  [PMID:11102360 "the DNA-binding domain plays a critical role in LIN-31 function"].
- Cell autonomy: mosaic analysis puts the requirement in the Pn.p cells
  [PMID:8807292 "lin-31, which specifies cell fates during vulval induction and encodes a
  putative transcription factor similar to HNF-3/fork head, acts in the Pn.p cells"].
- MAP kinase link (Tan, Lackner & Kim 1998): [PMID:9604932 "lin-31 and lin-1 act
  genetically downstream of mpk-1, and both proteins can be directly phosphorylated by MAP
  kinase"]; [PMID:9604932 "LIN-31 binds to LIN-1, and the LIN-1/LIN-31 complex inhibits
  vulval induction"]; [PMID:9604932 "Phosphorylation of LIN-31 by MPK-1 disrupts the
  LIN-1/LIN-31 complex, relieving vulval inhibition"]; the activator role is stated as a
  hypothesis: [PMID:9604932 "Phosphorylated LIN-31 may also act as a transcriptional
  activator, promoting vulval cell fates"]. The paper framed LIN-31 as
  [PMID:9604932 "a vulval-specific effector of MPK-1, while LIN-1 acts as a general
  effector"].
- **Endogenous phosphosite test (Dickinson et al. 2013).** Cas9 knock-ins changed the four
  C-terminal MAPK threonines to Ala or Glu. Both gave the same mild morphology phenotype,
  not a fate phenotype: [PMID:23995389 "Mutation of the four MAPK phosphorylation sites to
  alanine caused a distorted vulval morphology at the L4 stage and a partially penetrant
  protruding vulva phenotype in the adult"], [PMID:23995389 "A similar phenotype was
  observed when these residues were mutated to glutamic acid, mimicking constitutive
  phosphorylation"]. The 2018 review reads this as: [PMID:30544993 "However, subsequent
  CRISPR knock-ins of phosphodefective and phosphomimetic mutations in the same putative
  MPK-1 sites failed to alter VPC patterning, so regulation of LIN-31 may be more complex"].
  So the 1998 phosphorylation-dissociation model is not established for the endogenous
  protein; the phosphosites matter for vulval morphogenesis.
- LIN-1 does not always need LIN-31: lag-2 repression by LIN-1 is LIN-31-independent
  [PMID:21596897 "This role for LIN-1 in lag-2 regulation does not require LIN-31
  /Forkhead"].

## Targets and DNA binding

- lin-39 (Hox): LIN-31 binds and positively regulates a 1.3 kb lin-39 enhancer that drives
  Ras-dependent P6.p expression [PMID:16782085 "The Forkhead domain protein LIN-31 also
  acts positively on lin-39 in P6.p via this module"]; the follow-up paper states the
  binding directly [PMID:24885717 "we showed that LIN-1, LIN-31 and LIN-39 directly bind
  this cis-regulatory module"]. This is the basis of the IDA sequence-specific DNA binding
  row. Note a discordant earlier result with full-length reporters: P6.p upregulation
  [PMID:16412617 "appears to be independent of LIN-31, SEM-4, EOR-1 and EOR-2"].
- egl-17/FGF: late repression of the distal enhancer needs lin-1 and lin-31
  [PMID:12710960 "Since expression of egl-17::GFP driven by the distal enhancer can no
  longer be turned off at late stages in lin-1 and lin-31 mutants"]. Genetic, not shown to
  be direct.
- cki-1 (CIP/KIP CDK inhibitor): see below.

## VPC cell-cycle quiescence (not in the WormBase text)

- [PMID:18082681 "Mutation of lin-1 or lin-31, two downstream targets of the Receptor
  Tyrosine kinase (RTK)/Ras/MAP kinase cascade that controls VPC cell fate, disrupts the
  temporary VPC quiescence"]; [PMID:18082681 "LIN-1 and LIN-31 promote cki-1/Kip-1
  transcription prior to their inhibition through RTK/Ras/MAPK activation"].
- Reporter evidence only (abstract); whether cki-1 is a direct LIN-31 target is untested.
  Not added as a NEW GO row (TF -> CKI transcription -> G1 arrest is an indirect chain
  with abstract-only evidence; recorded in description, core function text and
  suggested experiments instead).

## Male roles (not in the WormBase text)

- Spicule development: [PMID:10419688 "Mutations in lin-31 result in identical cell
  migration and spicule morphology defects"] (same as TGF-beta pathway mutants).
- B lineage: LIN-31 acts downstream of EGF in Bgamma
  [PMID:20042118 "However, we found that LIN-31 is required to positively regulate ceh-13
  transcription"], contradicting the "vulval-specific effector" framing of 1998.

## GO annotation thoughts

- MF: forkhead DNA-binding TF, RNA Pol II-specific (IBA) is the core activity; the IDA
  sequence-specific DNA binding row (PMID:16782085) is evidence for binding a Pol II
  cis-regulatory module (lin-39 enhancer), so MODIFY to GO:0000978.
- BP: vulval development (IMP/IGI, PMID:11861555, lin-45 raf paper; full text not
  readable here, allele WBVar00089926 = lin-31(n1053)). Accept; the term is correct.
  vulval cell fate specification (GO:0072327) would be more specific, but it is a
  descendant of a term the gene already carries and the row's own paper is unread, so no
  MODIFY or NEW.
- CC: nucleus (IDA from PMID:9604932, IBA, IEA) - accept.
- No PAINT losses on the lineage (`just paint-losses worm lin-31`).
