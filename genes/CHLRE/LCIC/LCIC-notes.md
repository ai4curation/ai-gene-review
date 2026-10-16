# LCIC (Q75NZ1, Cre06.g307500) review notes

## Provenance / process

- 2026-10-03: GOA has 0 rows for Q75NZ1, so the review consists only of NEW proposals and core functions.
- Deep research: `scripts/deep_research_wrapper.py CHLRE LCIC falcon --fallback perplexity-lite` failed.
  Falcon (Edison API) returned `402 Payment Required`; the perplexity-lite fallback reported
  "Provider 'perplexity' not available". It was not retried, and no deep-research file was written.
  The literature was gathered instead through PubMed esearch (`LCIC/LciC AND Chlamydomonas`,
  `LCIB AND (pyrenoid OR Chlamydomonas)`), and four new PMIDs were cached
  (28938113, 34791500, 36856938, 15235119).
- The cached PMID:27911826 is abstract-only. I read the PMC full text (PMC5187666) from
  pmc.ncbi.nlm.nih.gov during the review. Quotes from it below are marked (full text, not cached).

## Identity and family

- 443 aa, chloroplast transit peptide, Pfam PF18599 LCIB_C_CA domain (88-322), disordered C-terminus
  (424-443). PANTHER PTHR38016:SF1. LCIB paralog (Q75NZ2).
- PDB 5B5X: LCIC residues 40-344 at 2.51 A, with Zn2+ bound by Cys119, His179 and Cys203 (UniProt BINDING
  features; I checked the residues against the sequence: C119, H179, C203).

## Complex and localization

- LCIB-LCIC interaction by Y2H/IP-MS; the two co-localize near the pyrenoid as a ~350 kDa hexamer
  [PMID:20660228 "LCIB interacts with the LCIB homologous protein LCIC in yeast and in vivo"]
  [PMID:20660228 "LCIB and LCIC are co-localized in the vicinity of the pyrenoid under LC conditions in the light, forming a hexamer complex of approximately 350 kDa"].
- LCIC-mCherry forms puncta at the pyrenoid periphery, outside the starch-sheath plates
  [PMID:28938113 "1) LCIB and LCIC localize to puncta around the periphery"]
  [PMID:28938113 "STA2 was localized within the perimeter described by LCIC"]
  [PMID:28938113 "Our data confirm that LCIB and LCIC, known stromal soluble proteins, are in a tight complex"].
  Location is therefore chloroplast stroma at the pyrenoid periphery, not the pyrenoid matrix (I did not
  propose GO:1990732).
- LCIC interacts with the bestrophin-like proteins LCI11 and Cre16.g662600
  [PMID:28938113 "Both LCIB and LCIC interact with LCI11 (Cre16.g663450), and LCIC also interacts with Cre16.g662600"].
- LCIC is needed for LCIB to move to the pyrenoid, and LCIC is absent in lcib mutants
  [PMID:34791500 "LCIB migration to around the pyrenoid required the accumulation of LCIC in the Chlamydomonas chloroplast"]
  [PMID:34791500 "This is consistent with the results that the accumulation of LCIC was also missing in the lcib mutant"].
- Recombinant co-expression gives a ~440 kDa 1:1 complex. Isolated LCIC is a dimer, and mixing
  separately purified LCIB and LCIC does not reconstitute the complex (full text, not cached, PMC5187666).

## Carbonic anhydrase activity: this is the key point for the module

- Jin et al. 2016 full text (not cached): "CsLCIB, CrLCIB, CrLCIC, recombinant CrLCIB-LCIC complex, and
  native CrLCIB-LCIC complex were inactive under all conditions tested". Only PtLCIB3, PtLCIB4 and FjLCIB
  were active. The inactivity is attributed to disordering of His161 and Arg193 in LCIC. A Ser160
  phosphosite lies next to His161.
- The cached full-text secondary sources restate this:
  [PMID:28938113 "However, recombinant LCIB/C had no carbonic anhydrase function"]
  [PMID:34791500 "Recombinant LCIB, LCIC, LCIB-LCIC complex, and native LCIB-LCIC complex do not have CA activity (Jin et al., 2016)"].
- Kasili et al. 2023 shows LCIB alone complements CA-deficient yeast (nce103) and Arabidopsis (beta-ca5)
  [PMID:36856938 "We provide evidence that LCIB is an active CA using a Saccharomyces cerevisiae CA knockout mutant"].
  The abstract does not test LCIC.
- Conclusion: there is no direct evidence that LCIC has carbonate dehydratase activity (GO:0004089), and
  in vitro assays of LCIC and the native complex were negative. I therefore did not assert GO:0004089 for
  LCIC, either as enables or as contributes_to. The module annoton `lcib_lcic_ca` assigns GO:0004089 to the
  complex. For LCIB that is now supportable from complementation data. For LCIC it is not supported. The
  module's own description already says CA activity "has not been robustly measured in vitro".
- I also considered a NOT carbonate dehydratase activity (IDA) annotation, but did not add one. The
  authors suggest the activity may be regulated (conformational, by phosphorylation, or by complex
  dissociation), and the negative assays are in vitro only.

## BP

- GO has no "CO2-concentrating mechanism" process term. There is no lcic mutant phenotype, and necessity is
  confounded by LCIC loss in lcib mutants. No BP was proposed.
