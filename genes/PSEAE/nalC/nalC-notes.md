# nalC (PA3721, Q9HXS0) review notes

## Literature

- PA3721 was identified as nalC by transposon mutagenesis of nalC-type MexAB-OprM hyperexpressers; it represses the divergent PA3720-PA3719 operon [PMID:15387820 "PA3720-PA3719, whose expression was negatively regulated by PA3721"], and its effect on MexAB-OprM runs through PA3719 [PMID:15387820 "Thus, the nalC (PA3721) mutation serves only to enhance PA3720-PA3719 expression"]. PA3719 is the ArmR anti-repressor of MexR.
- Purified NalC binds an inverted repeat at the PA3720-armR promoter; PCP releases it [PMID:22393435 "The NalC binding site was localized to an inverted repeat (IR) sequence upstream of PA3720-armR"]. Full text read: the nalC mutant K1454 shows increased PA3720-armR expression [PMID:22393435 "although the mutant showed the expected increase in PA3720-armR expression compared with its wild type parent K767"].

Search: PubMed metadata for GOA-cited PMIDs; PMID:22393435 full text cached and read.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN004738546 | GO:0000976 transcription cis-regulatory region binding | 7 | 411 (33 taxa) | GO:0000976, IDA, PMID:22393435 | SOUND | EMSA with purified NalC, binding site mapped to an IR (full text). This is the only support for nalC as a seed (pseudocap_only_support). | AcrR P0ACS9 (IDA), VC_1746 Q9KR96, NfxB, MexZ, MexL, NalD | Yes |
| PTN004738546 | GO:0006355 regulation of DNA-templated transcription | 19 | 411 (33 taxa) | GO:0045892, IMP, PMID:22393435 | SOUND | Increased PA3720-armR expression in the nalC mutant (full text). | 18 other seeds incl. AcrR, RutR, KstR, EthR | Yes |

Node-level verdict for PTN004738546 (all three IBDs stand on many experimentally characterised TetR regulators, no GO_CENTRAL defect) is recorded once in `genes/PSEAE/nfxB/nfxB-notes.md`.

Non-seed PseudoCAP rows: GO:0032410 (PMID:15387820) WRONG, DELETE_ROW defect PROBABLE (same pattern as nfxB/nalD/mexZ). GO:0034763 MARK_AS_OVER_ANNOTATED: NalC affects efflux only through the ArmR-MexR cascade; no defect filed.
