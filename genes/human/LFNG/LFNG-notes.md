# LFNG (human, Q8NES3) review notes

## Identity
- Beta-1,3-N-acetylglucosaminyltransferase lunatic fringe (EC 2.4.1.222). PANTHER PTHR10811 (FRINGE-RELATED); no subfamily line in UniProt.
- IBA: O-fucosylpeptide 3-beta-GlcNAc-transferase activity and regulation of Notch signaling pathway, PTN000087518.

## Key findings
- Fringe proteins are O-fucose-specific beta1,3-GlcNAc-transferases on Notch EGF repeats [PMID:10935626].
- LFNG reduces JAG1 binding and JAG1-triggered NOTCH2 signaling, not DLL1 [PMID:11346656].
- SCDO3 DxD-motif variant abolishes activity [PMID:30531807]; LFNG mutation causes SCD3 [PMID:19061953].
- Requires Mn2+; Golgi type II membrane protein (UniProt).

## Decisions
- Core: GO:0033829 in GO:0008593 and GO:0014807; Golgi membrane.
- Negative regulation of Notch kept non-core (direction depends on ligand); extracellular region/animal organ morphogenesis over-annotated.

## Variant-relevant biology
- Fringe is a ligand-selectivity modifier: enhances Delta-like, reduces Jagged/Serrate responses; oscillates in the vertebrate segmentation clock.

## Deep research
- Falcon deep research completed: file:human/LFNG/LFNG-deep-research-falcon.md (first attempt timed out at the 600 s wrapper default; rerun with --timeout 2700). Key statements quoted in the review are verbatim from that file.
