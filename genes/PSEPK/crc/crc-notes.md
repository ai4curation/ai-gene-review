# crc (PP_5292, Q88C91) review notes

## Provenance

- Deep research: `just deep-research PSEPK crc --provider falcon` was attempted on 2026-10-23 and failed
  ("Failed to authenticate"); no other provider is configured. Review built from UniProt and cached literature.
- Identity: UniProt Q88C91 (unreviewed) is named "Exodeoxyribonuclease III" by family rule; locus PP_5292 is
  the KT2440 crc gene [PMID:29188181 "1000 bp targeting regions 5’ and 3’ of the crc gene (PP_5292, GenBank: AE015451.1:6039987..6040766)"].
  The 780-bp span matches the 259-aa Q88C91 sequence.

## Function

- Pseudoenzyme: [PMID:30758287 "the absence of key catalytic residues in the active site cleft indicate that Crc has lost enzymatic function"];
  [PMID:23717639 "Crc protein purified to homogeneity from P. aeruginosa did neither display DNase activity, nor did it bind to previously identified RNA substrates."]
- Co-repressor of Hfq: [PMID:24803210 "Crc was unable to bind RNA in the absence of Hfq. However, pull-down assays showed that Crc and Hfq can form a co-complex with RNA containing a CA motif in vitro."];
  [PMID:34139006 "Here, Crc was shown to enhance Hfq-mediated translational repression of several mRNAs."]
- Catabolite repression: [PMID:24803210 "Inactivation of the hfq or the crc gene impaired catabolite repression to a similar extent."]
- Conserved in Pseudomonadaceae: [PMID:28404995 "Crc and Hfq proteins from either A. vinelandii or P. putida could form a stable complex with an RNA A-rich Hfq-binding motif present in the leader region of gluP mRNA."]
- Older literature (e.g. PMID:22053874) describes Crc itself as the RNA-binding translational repressor sequestered
  by CrcZ/CrcY; this was revised once RNA binding was traced to co-purifying Hfq (PMID:23717639, PMID:23770724).

## Curation decisions

- All nuclease/DNA-binding/DNA-repair/Mg IEAs removed (PSEUDOENZYME_OVERANNOTATION from the exonuclease III rule).
- NEW: contributes_to translation repressor activity (Hfq binds the RNA, so contributes_to rather than enables),
  negative regulation of translation, carbon catabolite repression.
- No molecular_function is asserted for Crc alone in core_functions: its only demonstrated activity is as part of
  the Hfq/Crc assembly; a bare protein-binding term would be uninformative.
