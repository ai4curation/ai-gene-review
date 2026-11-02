# FRI (FRIGIDA) curation notes

## Session 2026-10-05 (vernalization_flc_silencing module)

- Accession choice: the functional protein is P0DH90 (FRIGI_ARATH; H51/Sf-2 allele, 609 aa). The Col-0 entry Q67Z93 (At4g00650, "Inactive protein FRIGIDA", 314 aa) encodes a truncated loss-of-function allele. Folder `FRI` = P0DH90. GOA rows on P0DH90 are sparse (2 IPI protein binding, 1 IEA nuclear speck).
- Falcon deep research failed (agentapi not found / timeout), so no deep-research file was written.
- Natural variation: [PMID:11030654 "Most of the early-flowering ecotypes analyzed carry FRI alleles containing one of two different deletions that disrupt the open reading frame."]
- FRI up-regulates FLC: [PMID:14973192 "In winter-annual accessions of Arabidopsis, FRI activity blocks flowering through the up-regulation of the floral inhibitor FLOWERING LOCUS C (FLC)."]
- FRI-C scaffold: [PMID:21282526 "Here, we report that FRI acts as a scaffold protein interacting with FRL1, FES1, SUF4, and FLX to form a transcription activator complex (FRI-C)."]; SUF4 provides DNA binding: [PMID:21282526 "SUF4 binds to a cis-element of the FLC promoter"].
- Chromatin: [PMID:19567704 "FRI mediates WDR5a enrichment at the FLC locus, leading to increased H3K4me3 and FLC upregulation."]
- Cap-binding complex: [PMID:19429606 "CBP20 interacted directly with FRI in yeast and in planta"]. The FIP1/FIP2 Y2H interactors are uninformative: [PMID:19429606 "The additional FRI interactors identified in the yeast two-hybrid screens encode novel proteins with no clearly identifiable functional domains"].
- Localization: [PMID:17138694 "YFP:FRI was dispersed throughout the nucleus, and fluorescence was observed as evenly distributed speckles"]. Cold condensates: [PMID:34732891 "cold rapidly promotes the formation of FRI nuclear condensates that do not colocalize with an active FLC locus"]. This paper was the subject of a Matters Arising exchange (reply PMID:37438593), so it is used cautiously.

## Decisions
- Protein binding (FIP1, FIP2): REMOVE as uninformative.
- Nuclear speck IEA: ACCEPT.
- NEW: transcription coactivator activity (GO:0003713), positive regulation of DNA-templated transcription (GO:0045893), nucleus (IDA). The coactivator term was chosen over protein-macromolecule adaptor activity because FRI-C is explicitly a transcription activator complex and FRI has no DNA-binding domain.
