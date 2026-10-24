# CSN1S2 (Bos taurus, P02663) - curation notes

## Identity
- Alpha-S2-casein, 222 aa precursor; signal 1-15; mature 16-222; most phosphorylated bovine casein (10-13 phosphoserines in three phosphate clusters); two Cys (disulfide dimers); internal repeat 76-140/158-222 [file:BOVIN/CSN1S2/CSN1S2-uniprot.txt "Important role in the capacity of milk to transport calcium phosphate."]
- Up to 10% of bovine casein [PMID:19307615 "alpha(S2)-Casein (alpha(S2)-CN) comprises up to 10% of the casein fraction in bovine milk."]; positively charged C-terminus [PMID:19307615 "This region may be the site for interactions with kappa-carrageenan, phosphate, and other anions."]
- Calcium-sensitive casein [PMID:21245413 "Ca-sensitive caseins (α(s)- and β-caseins) bind Ca but precipitate at high Ca concentrations"]. Human milk lacks alpha-s2 [PMID:7556666 "Since human milk does not contain any casein-alpha s2"].

## Core biology
- Ca-phosphate sequestration by casein phosphate centres [PMID:23958008; PMID:14735250] (shared family mechanism, see CSN1S1 notes).
- Amyloid propensity: alpha-s2 readily forms fibrils in vitro at neutral pH/37C; inhibited by alpha-s1 [PMID:18302322 "Thus, alpha s2-casein is particularly susceptible to fibril formation under physiological conditions."]; corpora amylacea in bovine mammary tissue [PMID:18302322 "The calcified proteinaceous deposits, or corpora amylacea, of bovine mammary tissue often comprise a network of amyloid fibrils"].
- tPA binding: dimeric alpha-s2 binds tPA on ligand blot; casein micelle as matrix for plasminogen activation in milk [PMID:8186264 "multimeric forms of kappa-casein and dimeric alpha s2-casein were identified as t-PA binding components."].
- Casocidin-I (f165-203) antibacterial peptide isolated from milk [PMID:7556666 "The primary structure of the peptide was revealed as a 39-amino-acid-containing fragment of bovine alpha s2-casein (position 165-203)"] -- peptide product, not activity of intact protein; not in GOA.

## GOA-cited references assessed
- PMID:3585228, PMID:16174355 hormone-response readouts (see CSN1S1 notes). PMID:16174355 abstract measures alpha-s1 mRNA and "alpha-casein" release - alpha-s2 not explicitly mentioned in abstract (full text not available).
- PMID:3549815 casein infusion study, weak for localisation.
- PMID:5168866 Golgi micelle formation, abstract-only.

## Deep research
- OpenScientist run had not been delivered at the time of writing.

## Deep research integration (OpenScientist, 2026-10-24)

All PMIDs cited by the report were fetched into publications/ (one, PMID:26735893, could
not be fetched) and the points used were checked against the abstracts.

- No contradictions with the review. The report's primary function (calcium phosphate
  sequestration by phosphoserine clusters, micelle building, extracellular site) matches
  the core function.
- Added to GO:0140314 (NEW): PMID:31928725 (caseins sequester calcium phosphate
  nanoclusters through multiply phosphorylated short sequences), PMID:32921475 (micellar
  calcium is either in CCP held by phosphoserine clusters or bound directly to
  phosphoserine), and a quote from the report.
- Added to GO:0042803 homodimerization (KEEP_AS_NON_CORE): PMID:16546124 (disulphide
  dimers in casein micelles of all milks studied). The report's statement that bovine
  alpha-s2 forms homo- and heterodimers overstates this abstract, which shows homo- and
  heterodimers only for rodent caseins; recorded in the reference review.
- Not used for GO: FAM20C (kinase property), casocidin-1 and caseinophosphopeptide
  activities (peptide-derived, PMID:7556666, 9216247, 10532380), iron chelation by goat
  phosphopeptides (PMID:28215884), breed polymorphisms (PMID:40184159, 33546434, 37685069).
  The report's "four phosphate centers" (its own sequence scan) versus the review's "three
  phosphoserine clusters" was not changed: it is a counting convention, not a primary
  finding.

## Reviewer feedback (PR #5352, 2026-10-24)

- Dropped the NEW GO:0007595 lactation row and removed lactation from core_functions.
  The comparator check had left out the same-role mouse paralogs Csn1s2a and Csn1s2b,
  neither of which carries lactation, and alpha-s2-casein has no knockout or other direct
  evidence that it does part of the work of lactation, so the absence is treated as a
  convention to respect. The "Added for consistency" clause went with the row.
- Status set to COMPLETE.
