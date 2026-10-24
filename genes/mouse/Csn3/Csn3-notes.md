# Csn3 (mouse kappa-casein, P06796) - review notes

- Calcium-insensitive casein, derived from an FDCSP-like SCPP precursor [PMID:21245413 "the five exons of the Ca-insensitive casein gene are all reminiscent of FDCSP"]. UniProt: "Kappa-casein stabilizes micelle formation, preventing casein precipitation in milk." Chymosin cleavage site 118-119 (para-kappa-casein / caseinomacropeptide), O-glycosylation sites by similarity.
- Knockout (Shekar et al. 2006): [PMID:16698927 "these females did not suckle their pups and failed to lactate because of destabilization of the micelles in the lumina of the mammary gland"]; [PMID:16698927 "The mutant kappa-casein allele did not affect the expression of other milk proteins in Csnk-/- females."]
- Human micelle fractionation: [PMID:7979373 "Since kappa-casein also stabilizes the micelles against precipitation by Ca2+ ions, a surface position for most of the kappa-casein is implied."]
- Transgenic bovine kappa-casein in mouse milk reduces micelle size [PMID:8792278 "Milk from transgenic lines expressing high bovine kappa-CN had a significantly smaller micelle size than did control milk."]
- No GO MF term for casein micelle stabilization; per family-wide convention the core MF is GO:0140777 protein-containing complex stabilizing activity (imperfect: micelle is not a defined complex); raised as a suggested question.
- nutrient reservoir activity (IDA PMID:21789179): true but peripheral -- kappa-casein is the least abundant casein [PMID:21789179 "κ-casein (the casein protein which is present in milk in least abundance)"].

## Deep research
- OpenScientist deep research not available at time of review.

## Deep research integration (OpenScientist, 2026-10-24)

The report arrived after the review; its PMIDs were fetched into publications/ and the
points used were checked against the abstracts.

- No contradiction with the review. The report's primary function (micelle colloidal
  stabilization; Csnk-/- females fail to lactate) matches core GO:0140777, protein
  stabilization and lactation (IMP, PMID:16698927).
- Added to GO:0140777 (NEW): PMID:12778565 ("stabilizing hairy brush of kappa-casein") and a
  quote from the report.
- Report error, not adopted: it calls para-kappa-casein "membrane-anchored"; it remains on
  the micelle, not on a membrane.
- Not used: chymosin cleavage (an activity of chymosin; kappa-casein is the substrate),
  glycomacropeptide bioactivities (PMID:30870995 and others; peptide-derived), Elf5
  co-expression (PMID:18180458), micelle scattering models (PMID:21112300, 22381008,
  25388767).
- GO:0045735 nutrient reservoir activity stays KEEP_AS_NON_CORE (least abundant casein; its
  distinctive essential role is stabilization); see mouse Csn1s2a for the contrasting core
  call on a major casein.
- No action changes.
- Also added PMID:41200845 (kappa-casein inhibits calcium-induced amorphous aggregation of beta-casein in vitro, found via the rat Csn3 report) to GO:0140777 and the IBA protein stabilization row, as direct biochemical support for the stabilizing activity.
