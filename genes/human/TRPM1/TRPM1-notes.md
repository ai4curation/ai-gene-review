# TRPM1 (melastatin, Q7Z4N2) review notes

Session 2026-11-16, DISMECH vision-alignment campaign (complete CSNB).

## Biology (with provenance)

- TRP channel, TRPM subfamily; first described as melastatin, a melanocyte/melanoma gene whose
  expression falls with melanoma aggressiveness [PMID:9806836] (mouse genomics; TAS-level only).
- Bona fide plasma-membrane cation channel, Ca2+/divalent permeable, zinc-inhibited; forms
  heteromultimers with TRPM3 [PMID:21278253 "TRPM1 proteins are bona fide ion-conducting plasma membrane channels"]
  (heterologous expression). Mediates Ca2+ entry in HEK293 [PMID:11535825].
- Retina: the ON-bipolar transduction channel downstream of mGluR6 and Go
  [PMID:19966281 "TRPM1-L functions as a constitutively active nonselective cation channel and its activity is negatively regulated by Go in the mGluR6 cascade"] (mouse);
  [PMID:19861548 "TRPM1 is necessary for the depolarizing light response of ON-bipolar cells"] (mouse, macaque localisation);
  human cCSNB with ON-bipolar dysfunction [PMID:19878917, PMID:19896109];
  localised to ON bipolar dendrites in human retina [PMID:19896109].
- Most TRPM1 in ON-bipolar cells is in the ER of soma/axon/dendrites, not Golgi; dendritic tips hold the
  functional pool [PMID:30027108] (mouse, endogenous).
- Melanocytes (human): mGluR6 agonist enhances TRPM1 Ca2+ uptake, positive coupling because Galpha-o
  is absent [PMID:23452348]. Non-core for retina.

## Decisions summary

- Core MF: monoatomic cation channel activity (nonselective; Ca2+ permeable rows on calcium channel
  activity accepted).
- Retina-core processes: visual perception; mGluR6 pathway (as effector channel). Melanocyte Ca2+ import
  kept (also true of a Ca2+-permeable PM channel).
- PDZ fragmentomics protein-binding IPIs removed as uninformative (screen of PDZ-PBM affinities).
- ER/ER membrane: endogenous native ER pool in mouse ON-bipolar cells -> KEEP_AS_NON_CORE.
- "cellular response to light stimulus" -> visual perception: the bipolar cell responds to glutamate.
