# hsp-70 (C12C8.1) curation notes

UniProt O45246 (TrEMBL, 643 aa), WormBase C12C8.1. Inducible cytosolic HSP70
(counterpart of human HSPA1A/B). Deep research: not run (falcon times out in
this environment; perplexity-lite unavailable). Review built from cached
publications and PubMed searches.

## Identity
- C. elegans has a multigene hsp70 family [PMID:2225768 "There are at least nine genes in the hsp70 multigene family of C. elegans."].
- Four cytosolic HSP70s: HSP-1, C12C8.1, F44E5.4, F44E5.5 [PMID:41387410 "Of the seven canonical HSP70 family chaperones found in C. elegans, four are cytosolic (HSP-1, C12C8.1, F44E5.4, F44E5.5)"].
- Sequence: begins MSTCKAIGIDLG (no signal peptide), ends EEVD (cytosolic HSP70 co-chaperone motif). ARBA "ER lumen" is therefore wrong -> REMOVE.

## Expression
- Silent at ambient temperature, strongly induced by heat; C12C8.1 promoter is the standard phsp70::gfp reporter [PMID:23637632 "Expression of this reporter is not detected under ambient growth conditions of development and adulthood (Figure 1A) and is induced strongly by HS (Figure 1B)."].
- >1000-fold mRNA induction after heat shock [PMID:28198373 "As expected, this treatment markedly increased (>1000-fold) expression of the HSP genes hsp-70 (C12C8.1) and hsp-16.1."].
- HSF-1 dependent [PMID:27688402 "The expression of classical heat-shock genes hsp-16.41 and hsp-70 (C12C8.1) was severely compromised (>99% reduced) in hsf-1(ok600) animals exposed to heat shock compared with N2 animals"].
- Tunicamycin induction, attenuated in xbp-1 (Table I of PMID:12186849) -> ER UPR/IRE1 HEP rows kept as non-core (output gene, cytosolic).

## Decisions
- GO:0044183 (IBA, ISS) MODIFY -> GO:0140662 ATP-dependent protein folding chaperone, matching hsp-1.
- GO:0005832 CCT (IDA, PMID:9434769, abstract-only): MARK_AS_OVER_ANNOTATED. Abstract names 52-65 kDa CCT subunits and co-purifying HSP60; an HSP70 is not a CCT subunit. Not removed since full text unread.
- Lifespan IGI (PMID:14668486) KEEP_AS_NON_CORE [PMID:14668486 "Down-regulation of individual molecular chaperones, transcriptional targets of HSF-1, also decreased longevity of long-lived mutant but not wild-type animals."].
- No gene-specific biochemistry exists for C12C8.1; MF rests on the PAINT HSP70 node and ISS from HSPA1A.
