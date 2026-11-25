# nalD (PA3574, Q9HY46) review notes

## Literature

- nalD (PA3574) mutations cause MexAB-OprM overexpression in a transposon mutant and clinical isolates, reversed by the cloned gene [PMID:15855496 "the cloned nalD gene reduced the multidrug resistance and MexAB-OprM expression of the transposon mutant and clinical isolates"].
- NalD binds an operator overlapping a second mexAB-oprM promoter, whose activity rises in a nalD mutant [PMID:17028276 "increased expression from this promoter was seen in a nalD mutant, consistent with NalD directly controlling mexAB-oprM expression from a second promoter"].
- Pyocyanin binds NalD and MexR and releases them from the mexA promoter [PMID:40794867 "Electrophoretic mobility shift assays show that PYO binding to MexR and NalD induces their dissociation from the mexA promoter"].

Search: PubMed metadata for GOA-cited PMIDs; PMID:15855496 and PMID:40794867 full text cached.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN004738546 | GO:0006355 regulation of DNA-templated transcription | 19 | 411 (33 taxa) | GO:0045892, IMP, PMID:17028276 | SOUND | Abstract states NalD binding and increased promoter expression in the nalD mutant. | 18 other seeds incl. AcrR, RutR, KstR, EthR | Yes |
| PTN004738546 | GO:0000976 (not in worklist for this gene) | 7 | 411 | UniProt IDA, PMID:40794867 | SOUND | EMSA on the mexA promoter (not PseudoCAP). | AcrR, VC_1746, NfxB, nalC, MexL, MexZ | Yes |

Node-level verdict for PTN004738546 (all three IBDs stand on many experimentally characterised TetR regulators, no GO_CENTRAL defect) is recorded once in `genes/PSEAE/nfxB/nfxB-notes.md`.

Non-seed PseudoCAP rows: GO:0032410 (PMID:17028276) DELETE_ROW defect PROBABLE. GO:0034763 and GO:0051051 MODIFY to GO:1905700 (direct repressor of a xenobiotic efflux pump; same choice as mexZ).
