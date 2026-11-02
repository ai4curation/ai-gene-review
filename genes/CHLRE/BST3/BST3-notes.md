# BST3 (Chlamydomonas reinhardtii) review notes

UniProt A0A2K3CTP3 (TrEMBL, "Uncharacterized protein", 466 aa); locus Cre16.g663450 /
CHLRE_16g663450v5. Called LCI11 in the 2017 interactome. Paralogs: BST1 = Cre16.g662600 ->
A0A2K3CTN0 (genes/CHLRE/BST1); BST2 = Cre16.g663400 -> A0A2K3CTQ2 (genes/CHLRE/BST2).

## Deep research

Not run. Deep research is unavailable in this session: falcon returns HTTP 402 Payment
Required and the perplexity provider is missing (same as for the BST1 and BST2 runs on
2026-10-03). No deep-research file exists; this review is built from the primary literature
cached in publications/ and stays consistent with the sibling BST1/BST2 reviews.

## Identity and family

- Three paralogs clustered on chr 16 [PMID:31391312 "BST1 (Cre16.g662600), BST2
  (Cre16.g663400), and BST3 (Cre16.g663450) (collectively BST1–3) are paralogous
  bestrophin-like genes"].
- LCI11 name and >80% identity [PMID:31391312 "BST2 and BST3 were previously reported as LCI11
  by Fang et al. (16). An alignment between the 3 Chlamydomonas bestrophin-like proteins showed
  that the proteins are >80% identical to one another"]. Fang et al. = PMID:22634760 (verified
  via PubMed esearch/esummary); the cached text of that paper does not mention LCI11 or
  Cre16.g663450 (gene data are in uncached supplementary tables). The 2017 interactome uses
  LCI11 specifically for Cre16.g663450 [PMID:28938113 "Both LCIB and LCIC interact with LCI11
  (Cre16.g663450)"]. A PubMed search for "LCI11 Chlamydomonas" returns no hits.
- Predicted chloroplast transit peptide [PMID:31391312 "predicted that each BST protein had a
  chloroplast transit peptide and was likely to be a chloroplast membrane protein"].
- Homology model of the group: [PMID:31391312 "the selective pore is positively charged,
  supporting the hypothesis that BST1–3 transport negatively charged ions"].
- UniProt subcellular location "Cell membrane" is an ARBA default for bestrophins
  (ARBA00004651); contradicted by experiment.

## BST3-specific data

- Expression: low-CO2 induced within 2 h [PMID:31391312 "All 3 genes had increased transcript
  levels within 2 h after the switch to low CO2"]; strongly CIA5-dependent [PMID:31391312 "the
  cia5 mutant exhibited severely reduced expression of BST1 and BST3 under both CO2 conditions,
  a transcriptional pattern observed with other CCM genes"].
- Localization: the only paralog imaged from its native promoter [PMID:31391312 "This line
  showed the same localization pattern as BST3 under the constitutive PSAD promoter (Fig. 3C),
  and quantification of enrichment showed a 1.46-fold enrichment"]; thylakoid membranes
  extending into pyrenoid tubules [PMID:31391312 "All 3 BST-like proteins localized to the
  thylakoid membranes of the chloroplast"].
- Interactome (LCI11 bait): LCIB, LCIC, BST1, BST2 [PMID:28938113 "Both LCIB and LCIC interact
  with LCI11 (Cre16.g663450), and LCIC also interacts with Cre16.g662600"; "LCI11 and
  Cre16.g662600 directly interact, and both also interact with another bestrophin-like
  protein, Cre16.g663400."].
- Single mutant: CLiP bst3 (LMJ.RY0402.089365), protein-null [PMID:31391312 "The BST3
  transcript was not detected in bst3 (SI Appendix, Fig. S4B), and the BST3 protein was
  absent"], weak phenotype, implying redundancy [PMID:31391312 "This led us to think that BST1
  or BST2 function might be redundant with BST3"].

## Family-level physiology (shared with BST1/BST2)

- Triple knockdown: poor low-CO2 growth, lower Ci affinity [PMID:31391312 "These results
  indicate that BST1–3 play an important role in Ci uptake and fixation in low CO2 conditions in
  Chlamydomonas."].
- pmf effect opposite to Arabidopsis vccn1 [PMID:31391312 "The presence of AtVCCN1 decreases
  pmf in Arabidopsis, but the presence of the 3 BST proteins increases pmf in Chlamydomonas."].
- HCO3- delivery to CAH3 is a proposal [PMID:31391312 "We propose that BST1–3 are the
  transporters that bring HCO3− to CAH3 inside the thylakoid."]; no transport data
  [PMID:39240724 "BST4 may function as an HCO3− channel, like that proposed for BST1-3
  (Mukherjee et al. 2019), but there are currently no data to support this hypothesis"].

## Annotation decisions (mirroring BST1/BST2)

- GO:0005247 IBA -> MODIFY to GO:0005253 monoatomic anion channel activity.
- GO:0005886 IEA (ARBA "Cell membrane") -> REMOVE; contradicted by native-promoter thylakoid
  localization.
- GO:0019684 IBA -> MARK_AS_OVER_ANNOTATED (VCCN1-specific pmf role; divergent in BST1-3).
- GO:0042651 IBA -> ACCEPT.
- GO:1902476 IEA -> MODIFY to GO:0098656 monoatomic anion transmembrane transport.
- NEW GO:0009535 chloroplast thylakoid membrane, IDA PMID:31391312.
- No NEW BP term: bst3 single mutant phenotype is weak and the triple-RNAi Ci-uptake defect is
  necessity evidence shared by three paralogs; the CCM process role stays in core_functions
  prose.
- Module family `bst_thylakoid_channel` (GO:0005253 on GO:0009535) is supported for BST3 at
  the same family-inference strength as for BST1/BST2; BST3 has the strongest location
  evidence of the three.
