# TRY (TRIPTYCHON; At5g53200; UniProt Q8GV05) curation notes

## Identity
- Q8GV05 TRY_ARATH, 106 aa single-repeat R3 MYB, locus AT5G53200. Paralogs: CPC, ETC1, ETC2, ETC3, TCL1 (six R3 MYBs; [PMID:18644155]).

## Key findings (with provenance)
- TRY lacks an activation domain and functions in lateral inhibition [PMID:12356720 "We show that the TRIPTYCHON gene that functions in lateral inhibition encodes a single-repeat MYB-related transcription factor that lacks a recognizable activation domain."]
- TRY and CPC act together in trichome lateral inhibition and redundantly in root epidermis [PMID:12356720 "Both genes are expressed in trichomes and act together during lateral inhibition."]; try cpc: all cells contacting a trichome become trichomes [PMID:12356720].
- TRY blocks GL1-GL3 interaction; GFP-TRY nuclear in trichomes [PMID:14561633 "TRY has the ability to prevent the GL1 GL3 interaction"].
- TRY is transcriptionally activated by GL1/GL3 and moves between cells [PMID:18766177 "TRIPTYCHON and CAPRICE but not GLABRA1 and GLABRA3 can move between cells"].
- Negative autoregulation: TRY/CPC suppress TRY promoter; TRY protein-specific properties needed for cluster suppression [PMID:21951724].
- Quantitative pull-downs: R3 MYB inhibitors bind GL3 more weakly than GL1 [PMID:38504903].
- All R3 MYBs interact with GL3; GL1/WER + GL3/EGL3 activate TRY transcription in protoplasts [PMID:18644155].

## Curation decisions
- GO:0003700 ISS -> MODIFY to GO:0140416 transcription regulator inhibitor activity (competitive sequestration of bHLH partner).
- GO:0000976 IBA and Y1H IPI kept as non-core: TRY DNA binding in planta is not established, but HT Y1H [PMID:25533953] recorded a promoter interaction.
- CrY2H-seq protein binding rows -> REMOVE (uninformative, HT, no follow-up).
- GO:0010154 fruit development cites PMID:3793867, a Campylobacter paper (same erroneous PMID used on a GL1 row) -> MARK_AS_OVER_ANNOTATED (reference_review WRONG_IDENTIFIER); only fruit-related biology is R3 MYB suppression of silique trichomes [PMID:18644155]; no replacement guessed.
- Core: GO:0140416 + GO:1900032 regulation of trichome patterning (matching the GOA IMP convention).
- Falcon deep research generated (TRY-deep-research-falcon.md).
