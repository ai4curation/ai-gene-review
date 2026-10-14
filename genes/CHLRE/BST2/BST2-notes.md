# BST2 (Chlamydomonas reinhardtii) review notes

UniProt A0A2K3CTQ2 (TrEMBL, "Uncharacterized protein", 450 aa); locus Cre16.g663400 /
CHLRE_16g663400v5. Paralogs: BST1 = Cre16.g662600 -> A0A2K3CTN0 (reviewed in
genes/CHLRE/BST1); BST3 (LCI11) = Cre16.g663450 -> A0A2K3CTP3.

## Deep research

Not run. Deep research is unavailable in this session: falcon returns HTTP 402 Payment
Required and the perplexity provider is missing (same result as the BST1 run on 2026-10-03).
No deep-research file exists; this review is built from the primary literature cached in
publications/ and stays consistent with the sibling BST1 review.

## Identity and family

- Three paralogs clustered on chr 16 [PMID:31391312 "BST1 (Cre16.g662600), BST2
  (Cre16.g663400), and BST3 (Cre16.g663450) (collectively BST1–3) are paralogous
  bestrophin-like genes"].
- >80% identical; name LCI11 historically used for BST2 and BST3 [PMID:31391312 "BST2 and
  BST3 were previously reported as LCI11 by Fang et al. (16). An alignment between the 3
  Chlamydomonas bestrophin-like proteins showed that the proteins are >80% identical to one
  another"]. Note that the 2017 interactome uses LCI11 for Cre16.g663450 (BST3).
- Closest land-plant homolog Arabidopsis VCCN1, ~30% identity [PMID:31391312].
- Predicted chloroplast transit peptide [PMID:31391312 "predicted that each BST protein had a
  chloroplast transit peptide and was likely to be a chloroplast membrane protein"].
- Homology model (done for BST1, applies to the >80%-identical group) [PMID:31391312 "the
  selective pore is positively charged, supporting the hypothesis that BST1–3 transport
  negatively charged ions"].

## BST2-specific data

- Expression: induced in ambient CO2; CIA5 dependence partial [PMID:31391312 "BST2 transcript
  levels in cia5 cells showed reduced induction in ambient CO2 when compared with D66 cells,
  where BST2 transcript levels increase in ambient CO2 conditions."], whereas BST1 and BST3
  were severely reduced in cia5. Expressed above BST1 [PMID:31391312 "BST1 had a lower level of
  expression than BST2 or BST3"].
- Localization: Venus fusion (PSAD promoter) in thylakoid membranes, into pyrenoid tubules,
  enriched at pyrenoid periphery [PMID:31391312 "The localization studies visually showed that
  BST1, BST2, and BST3 were preferentially concentrated near the pyrenoid"]. Native-promoter
  control was done only for BST3.
- Interactome: BST2 is a prey of BST1 and BST3 baits [PMID:28938113 "LCI11 and Cre16.g662600
  directly interact, and both also interact with another bestrophin-like protein,
  Cre16.g663400."]. LCIB/LCIC interactions were reported for BST3 and BST1 only
  [PMID:28938113 "Both LCIB and LCIC interact with LCI11 (Cre16.g663450), and LCIC also
  interacts with Cre16.g662600"].
- Phenotype: only via triple RNAi [PMID:31391312 "RT-qPCR showed that bsti-1 had significantly
  reduced expression of BST1, BST2, and BST3 compared with D66"]; no BST2 single mutant.

## Family-level physiology (shared with BST1)

- Triple knockdown: poor low-CO2 growth, lower Ci affinity, reduced 14Ci accumulation
  [PMID:31391312 "These results indicate that BST1–3 play an important role in Ci uptake and
  fixation in low CO2 conditions in Chlamydomonas."].
- pmf effect opposite to Arabidopsis vccn1 [PMID:31391312 "The presence of AtVCCN1 decreases
  pmf in Arabidopsis, but the presence of the 3 BST proteins increases pmf in Chlamydomonas."].
- HCO3- delivery to CAH3 is a proposal [PMID:31391312 "We propose that BST1–3 are the
  transporters that bring HCO3− to CAH3 inside the thylakoid."]; no transport data for any of
  BST1-3 [PMID:39240724 "BST4 may function as an HCO3− channel, like that proposed for BST1-3
  (Mukherjee et al. 2019), but there are currently no data to support this hypothesis"].

## Annotation decisions (mirroring BST1)

- GO:0005247 IBA -> MODIFY to GO:0005253 monoatomic anion channel activity.
- GO:0005886 IEA (ARBA "Cell membrane") -> REMOVE; contradicted by thylakoid localization.
- GO:0019684 IBA -> MARK_AS_OVER_ANNOTATED (VCCN1-specific pmf role; divergent in BST1-3).
- GO:0042651 IBA -> ACCEPT.
- GO:1902476 IEA -> MODIFY to GO:0098656 monoatomic anion transmembrane transport.
- NEW GO:0009535 chloroplast thylakoid membrane, IDA PMID:31391312.
- Module family `bst_thylakoid_channel` (GO:0005253 on GO:0009535) is supported for BST2 at the
  same (family-inference) strength as for BST1.
