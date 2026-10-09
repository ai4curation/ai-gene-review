# enok (Q9W1A9) review notes

## Identity and activity
- KAT6/MOZ-MORF family MYST HAT; identified from mushroom body neuroblast proliferation defects. [PMID:11231125 "enok encodes a putative histone acetyltransferase (HAT) of the MYST family"]
- Major H3K23 acetyltransferase; all Enok complex subunits needed. [PMID:27198229 "We previously reported that Enok functions as the major HAT for establishing the H3K23ac mark in flies"] [PMID:27198229 "Depletion of any of the four subunits led to reductions in the H3K23ac levels without affecting the H3K14ac levels"]

## Complex and cell cycle
- Enok, Br140, Eaf6, Ing5 copurify. [PMID:27198229 "MudPIT analysis of Flag affinity purifications of Flag-HA-tagged Enok, Br140, Eaf6, and Ing5 showed copurification of these four components."]
- G1/S via Elg1/PCNA. [PMID:27198229 "Depletion of Enok resulted in an Elg1-dependent block at the G1/S transition and reduced chromatin-bound PCNA levels."]

## Transcription / piRNA
- [PMID:33524038 "Enok not only promotes rhino expression by acetylating H3K23"]

## Development
- GSC maintenance [PMID:24120347 "Removal or knockdown of Enok in the germline causes a GSC maintenance defect."]

## Curation decisions (shared across Enok complex genes Br140, Ing5, Eaf6)
- MOZ/MORF complex ACCEPT for all subunits.
- "DNA strand elongation involved in DNA replication" IDA (all four subunits) MODIFY -> GO:0000082 G1/S transition of mitotic cell cycle: the paper measures a G1/S block and chromatin-bound PCNA, not strand elongation.
- Acetyltransferase activator activity ACCEPT for the three non-catalytic subunits.
- enok: generic HAT / H3 HAT / catalytic activity MODIFY -> GO:0043994 H3K23 acetyltransferase; H15-domain-derived nucleosome and nucleosome assembly IEA REMOVE.
