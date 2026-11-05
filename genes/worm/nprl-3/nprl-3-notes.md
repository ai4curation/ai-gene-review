# nprl-3 notes

## 2026-10-28 initial review

- fetch-gene resolved Q20069 (Swiss-Prot NPRL3_CAEEL, WormBase WBGene00018072, GeneID 185331). 7 GOA rows, all IEA/ISS/IBA.
- Key paper PMID:23705068 (full text cached) read: nprl-3(ku540) loss of function suppresses L1 arrest of elo-5 / cgt-1;cgt-3; suppression requires TORC1 components [PMID:23705068 "Taken together, these results indicate that TORC1 acts downstream of d17iso-GlcCer and is negatively regulated by NPRL-3."].
- PMID:26109047 (full text): NPRL-3 also affects intestinal apical polarity, TORC1-independently [PMID:26109047 "This nprl-3(lf)-caused polarity restoration is independent of TORC1 activation"]. Did not propose a NEW polarity term: evidence is mutant suppression only, and the authors frame it as upstream of TORC1; mechanism unknown.
- Decisions: GATOR1 complex and negative regulation of TORC1 signaling ACCEPT (core); IEA "negative regulation of TOR signaling" MODIFY to TORC1 child; amino acid starvation and autophagy KEEP_AS_NON_CORE (downstream/context, not tested in worm); lysosomal membrane ACCEPT (by orthology; no worm localization).
- Added NEW contributes_to GTPase activator activity (ISS from human NPRL3; NPRL2-NPRL3 heterodimer executes GAP on RAGA). Comparator: worm nprl-2 already carries contributes_to GO:0005096 IBA.
- Curation gap (not a knowledge gap): no worm IMP annotations from PMID:23705068 in GOA.
