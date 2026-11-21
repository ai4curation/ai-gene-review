# PA2070 (PA2070, Q9I245) review notes

## Literature

- Uncharacterised TonB-dependent receptor (UniProt unreviewed, PE 3). Domain content from UniProt: TonB-dependent receptor plug and beta-barrel domains [file:PSEAE/PA2070/PA2070-uniprot.txt "PF00593; TonB_dep_Rec_b-barrel; 1."].
- No STN domain; signal peptide 1-28 (SignalP). PANTHER subfamily PTHR47234:SF2.
- PseudoCAP cites Llamas et al. 2008 for an IDA outer-membrane annotation [PMID:18086184 "the ECF sigmas PA0149, PA1912, PA2050, PA2093 and PA4896 have been overexpressed and their target gene candidates have been identified using DNA microarray, proteomic analysis, and/or lacZ reporter construct"]. Abstract only (not in PMC; WebSearch found no open full text). The abstract does not name PA2070, so it was not possible to check whether it was among the proteins detected in outer membranes or was found only by microarray.

Search: PubMed metadata and cached abstract of PMID:18086184; WebSearch for the paper with the four locus tags (no full text, no other papers on PA2070 found); UniProt record. No other literature on this protein was found.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002933024 | GO:0019867 outer membrane | 4 | 22 (3 taxa) | GO:0019867, IDA, PMID:18086184 | UNVERIFIABLE | Abstract only and does not name PA2070; the location itself is correct on sequence grounds (TonB-dependent receptor plug and barrel), so no PSEUDOCAP defect. | PA2590, PA2089, PA2057 (all the same PseudoCAP IDA, same paper) | Yes as a term; its evidence base is the same paper for all four seeds (see below) |

Node-level assessment for PTN002933024 is recorded once, in `genes/PSEAE/PA2590/PA2590-notes.md`: the IBD stands as a term (all leaves are TonB-dependent receptors), no GO_CENTRAL defect; all four seeds rest on the same paper.
