# ABCB19 (MDR1/MDR11/PGP19; At3g28860; UniProt Q9LJX0) notes

Deep research: falcon failed (Edison API 429, 2026-10-05).

## Auxin export
- atmdr1 impaired auxin transport, NPA binding [PMID:11701880 "Auxin transport activity was greatly impaired in atmdr1 and atmdr1 atpgp1 double mutant plants."].
- Root acropetal transport reduced 80% [PMID:17557805 "Mutations in Multidrug Resistance-Like1 (MDR1) reduced acropetal auxin transport in roots by 80% without affecting basipetal transport."]. (MDR1 = ABCB19, MDR4 = ABCB4.)
- phot1 phosphorylation inhibits efflux [PMID:21666806 "phosphorylation of ABCB19 by phot1 inhibits its efflux activity"].
- PIN1 interaction/coordination [PMID:17237354 "Specific PGP-PIN interactions were seen in yeast two-hybrid and coimmunoprecipitation assays."]; stabilizes PIN1 in DRMs [PMID:18774968].

## Brassinosteroid export
- [PMID:38513023 "Bioactive brassinosteroids are potent activators of ABCB19 ATP hydrolysis activity, and transport assays showed that ABCB19 transports brassinosteroids."]
- PMID:39497419 mainly ABCB1; ABCB19 annotations from it kept (ABCB19 likely comparator in full text).
- No GO term for brassinosteroid transport; raised as a suggested question.

## Decisions
- Many developmental/light-response IMP/IEA rows KEEP_AS_NON_CORE (downstream of transport).
- Leaf phyllotactic patterning (PMID:32855213): paper studies petiole angle, not phyllotaxis (full text checked: no "phyllotaxis") -> MARK_AS_OVER_ANNOTATED.
- Cytosol HDA (PMID:28887381) and nucleus ISM REMOVE: 12-TM integral PM protein.
