# PA3678 (mexL, Q9HXW2) review notes

PA3678 is the mexL locus, divergent from mexJK (PA3677-PA3676). UniProt carries no gene name.

## Literature

- MexL is a TetR-family repressor of mexJK [PMID:12193619 "Expression of this operon is negatively regulated by the product of mexL, a gene located upstream of and transcribed divergently from mexJK"]; a triclosan-resistant mutant carries a substitution in the MexL HTH.
- Purified MexL is a tetramer and binds the 94-bp mexL-mexJ intergenic region [PMID:15855505 "Gel mobility shift and footprinting assays demonstrated that MexL, but not MexL(A47D), binds specifically to the 94-bp mexL-mexJ intergenic region"], regulating both mexL and mexJK [PMID:15855505 "consistent with MexL regulating the expression of both mexL and mexJK, which was ascertained by gene fusion analyses"].

Search: PubMed metadata/abstracts for GOA-cited PMIDs (abstract-only caches).

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN004738546 | GO:0006355 regulation of DNA-templated transcription | 19 | 411 (33 taxa) | GO:0045892, IMP, PMID:12193619 | SOUND | Abstract states mexL negatively regulates mexJK and the resistant mutant has a mexL HTH substitution; footprinting and fusions (PMID:15855505) confirm direct repression. | 18 other seeds incl. AcrR, RutR, KstR, EthR | Yes |
| PTN004738546 | GO:0000976 / GO:0003700 (not in worklist for this gene) | 7 / 7 | 411 | CollecTF IPI GO:0000976 / GO:0001217, PMID:15855505 | SOUND | Not PseudoCAP; EMSA + footprinting. | AcrR, VC_1746, NfxB, others | Yes |

Node-level verdict for PTN004738546 (all three IBDs stand on many experimentally characterised TetR regulators, no GO_CENTRAL defect) is recorded once in `genes/PSEAE/nfxB/nfxB-notes.md`.

No PseudoCAP defect for this gene.
