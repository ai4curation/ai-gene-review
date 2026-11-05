# PA3345 / HptB (Q9HYQ0) review notes

## Literature

Search (Europe PMC REST, 2026-11-05: `TITLE:HptB AND aeruginosa`,
`TITLE:"histidine-containing phosphotransfer" AND aeruginosa`) returned PMIDs 16182517,
18256026, 20398205, 22128156, 27792789 (and its correction 27902688). PMID:31019225 was
added for the HsbR-RpoS link.

1. Lin et al. 2006 [PMID:16182517], abstract only. PA1611 signals through HptB (PA3345)
   to PA3346 [PMID:16182517 "We herein demonstrate that the hybrid sensor PA1611 carries
   out specific signal transduction, through HptB (PA3345), to the response regulator
   PA3346"]. Phenotypes of an hptB deletion implicate it in flagellar activity, chemotaxis,
   twitching and biofilm formation; the abstract does not give the signs.
2. Hsu et al. 2008 [PMID:18256026], abstract only. In vitro phosphorelay profiling: four
   sensors (PA1611, PA1976, PA2824, RetS) transfer phosphoryl groups to HptB, and from HptB
   to PA3346 (HsbR) [PMID:18256026 "Among the 12 recombinant orphan sensor kinases tested,
   4 of these sensors (PA1611, PA1976, PA2824, and RetS) transferred the phosphoryl group
   to HptB (PA3345)."]. Bacterial two-hybrid interactions with each sensor.
3. Bordi et al. 2010 [PMID:20398205], full text cached. hptB deletion is hyperbiofilm
   (pel-dependent, via GacA and rsmY), complemented by hptB in trans [PMID:20398205 "The
   hptB mutant has a hyperbiofilm phenotype compared with PAK (Fig."].
4. Bhuwan et al. 2012 [PMID:22128156], abstract only. hptB mutant is non-swarming; HsbR
   (PA3346) kinase domain phosphorylates HsbA (PA3347), which partner-switches with FlgM.
5. Valentini et al. 2016 [PMID:27792789], full text cached. hptB mutant: more EPS,
   more attachment and twitching, less swimming and swarming.
6. Bouillet et al. 2019 [PMID:31019225], full text cached. HsbR is an anti-sigma factor
   for RpoS; RpoS acts downstream of HptB in biofilm control.

Sign summary: HptB negatively regulates biofilm formation and twitching, positively
regulates swimming and swarming. GO:2000145 regulation of cell motility (unsigned)
therefore fits the mixed-sign motility evidence.

UniProt Q9HYQ0: 116 aa, HPt domain 18-116 (PROSITE PS50894), phosphohistidine His57
(ProRule), PANTHER PTHR28242 (YPD1), crystal structure PDB 7C1I.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002000688 | GO:0009927 histidine phosphotransfer kinase activity | 9 | 462 (57 taxa) | GO:0009927, IDA, PMID:16182517 (PseudoCAP) | SOUND | Abstract states that phosphoryl transfer from PA1611 to PA3346 goes through HptB; the follow-up (PMID:18256026, same group) shows in vitro transfer from four sensors to HptB and on to PA3346. HPt domain with conserved His57. Abstract-only reading, no defect claimed. | Arabidopsis AHP1/2/3/5/AHP4 (AT3G21510, AT3G29350, AT1G03430, AT5G39340, AT3G16360), S. pombe Mpr1 (SPBC725.02), A. nidulans YpdA (Q5BBS5), Dictyostelium RdeA (DDB_G0282923) | Yes; the eukaryotic HPt seeds (yeast and plant Ypd1/AHP proteins) have strong experimental support. The term defines HPt proteins and suits the clade. No GO_CENTRAL defect. |

Consistency: PA3343 (HsbD) review describes HsbD as linking c-di-GMP signalling to the
HptB pathway; this review agrees (HptB → HsbR → HsbA → HsbD/FlgM, and HsbR → RpoS).
The rpoS review in this batch uses the same PMID:31019225 evidence for the RpoS-HsbR
sigma-factor antagonist complex.

## Annotation decisions

- GO:0009927 (IBA, IDA): ACCEPT; core.
- GO:0004672 IEA (ARBA): TOO_GENERAL (GO:0009927 is_a GO:0004672).
- GO:0000160 (IBA, IEA): ACCEPT.
- GO:0005737 IBA: ACCEPT (no signal peptide/TM; soluble 116-aa protein).
- GO:0043424 IBA: KEEP_AS_NON_CORE (two-hybrid interaction with sensors).
- GO:1900191 IMP: ACCEPT (hyperbiofilm of ΔhptB, complemented; PMID:20398205).
- GO:2000145 IMP: ACCEPT (mixed-sign motility effects).
- GO:0050921 IMP: KEEP_AS_NON_CORE (sign of the chemotaxis effect not verified).
