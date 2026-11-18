# A0A0H2ZF55 (PA14_15840 / LdtPae3) curation notes

## 2026-11-17 — PA14 tether-hydrolase candidate (PTHR36699:SF1)

A0A0H2ZF55 is *Pseudomonas aeruginosa* strain UCBPP-PA14 locus PA14_15840, a
small Sec-exported YafK/LdtF-family protein (PANTHER PTHR36699:SF1). In the PA14
L,D-transpeptidase survey it is "LdtPae3", the candidate hydrolase that releases
OprI from peptidoglycan. The assignment is explicitly tentative, based on the
absence of amide-bond-forming activity plus similarity to E. coli YafK
[PMID:37255442, "The function of LdtPae3 was tentatively assigned to the release
of OprI based on both the absence of detectable amide bond-forming activity
(formation of 3→3 and tripeptide→ OprI bonds) and the close similarity between
LdtPae3 and E. coli hydrolase YafK."]. It shares PTHR36699:SF1 with the
experimentally characterised E. coli DpaA (P0AA99) and the *P. putida* KT2440
ortholog PP_1451 (Q88MW7).

## Locus identity

PA14_15840 (A0A0H2ZF55) = PA14 LdtPae3 (the hydrolase, PTHR36699:SF1), distinct
from PA14_27180 (A0A0H2ZCT9) = PA14 LdtPae2 (the anchoring enzyme, PTHR30582:SF24).
The two are paralogs in different PANTHER families and play the opposite roles
(write vs erase) of the tether-remodeling module.

## Carboxypeptidase activity is an over-annotation here

The carboxypeptidase activity of this subfamily is a narrow, glycine-specific
(meso-Dpm-Gly) activity demonstrated **only** in the E. coli DpaA exemplar;
PMID:33947763 states that classical ld-carboxypeptidase activity in DpaA
homologues is speculative ("more experiments will be necessary to determine
whether some DpaA-like proteins show ld-carboxypeptidase activity"). LdtPae3 is
biochemically uncharacterised, so the GO:0004180 carboxypeptidase row is marked
over-annotated rather than kept as a non-core function, consistent with the
SUBFAMILY_ONLY scope in the PTHR36699 family review and the PP_1451 ortholog.

The core molecular function is grounded as the specific GO:0061785 peptidoglycan
endopeptidase activity (the broader parent GO:0004175 is not asserted separately,
to avoid an ancestor/descendant redundancy).
