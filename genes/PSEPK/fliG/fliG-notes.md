# fliG (PP_4368, Q88ET5) notes

## 2026-11-03 re-review
- Deep research: `just deep-research PSEPK fliG --provider perplexity` failed (provider 'perplexity' not available); `just mod-description-deep-research` skipped (no MOD provider configured for PSEPK). Existing falcon report used; every falcon quote was checked as a verbatim substring.
- UniProt quotes now cite the local flat file (file:PSEPK/fliG/fliG-uniprot.txt). ARBA-only, imported (ECO:0000313), DE-name and DR GO lines are not used as support.
- Most rows lacked supported_by; added quotes from PMID:31452860 (full text) [PMID:31452860 "FliG is directly involved in torque generation [8]."] [PMID:31452860 "the FliM1/FliN3 complex binds to the FliG ring structure through a one-to-one interaction between FliG and FliM to form the continuous C ring wall"], the UniProt PIRNR-backed FUNCTION line, NCBIfam TIGR00207 and the falcon fliEFG operon statement.
- Location rows: GO:0009425 basal body and GO:0009288 flagellum MODIFY -> GO:0009433 C ring (correct but general); GO:0005886 MODIFY -> GO:0009898 cytoplasmic side of plasma membrane (peripheral, PIRNR-backed location). GO:0003774 MODIFY -> GO:0140605 (contributes_to). Chemotaxis KEEP_AS_NON_CORE (FliG performs the switching step but its core role is rotation). GO:0071973 ACCEPT.
- Added NEW GO:0005198 structural molecule activity (IC) as a second core function: the C-ring module asserts this complex-level activity and FliG forms the ring scaffold. Status remains COMPLETE.
