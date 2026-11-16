# PA2590 (PA2590, Q9I0P7) review notes

## Literature

- Uncharacterised TonB-dependent receptor (UniProt unreviewed, PE 3). Domain content from UniProt: TonB-dependent receptor plug and beta-barrel domains [file:PSEAE/PA2590/PA2590-uniprot.txt "PF00593; TonB_dep_Rec_b-barrel; 1."].
- Has an N-terminal STN domain [file:PSEAE/PA2590/PA2590-uniprot.txt "IPR011662; Secretin/TonB_short_N."], the signalling domain of TonB-dependent transducers of cell-surface signalling (CSS) systems; PA2590 and PA2089 are close paralogues (same PANTHER subfamily PTHR47234:SF3).
- PseudoCAP cites Llamas et al. 2008 for an IDA outer-membrane annotation [PMID:18086184 "the ECF sigmas PA0149, PA1912, PA2050, PA2093 and PA4896 have been overexpressed and their target gene candidates have been identified using DNA microarray, proteomic analysis, and/or lacZ reporter construct"]. Abstract only (not in PMC; WebSearch found no open full text). The abstract does not name PA2590, so it was not possible to check whether it was among the proteins detected in outer membranes or was found only by microarray.

Search: PubMed metadata and cached abstract of PMID:18086184; WebSearch for the paper with the four locus tags (no full text, no other papers on PA2590 found); UniProt record. No other literature on this protein was found.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002933024 | GO:0019867 outer membrane | 4 | 22 (3 taxa) | GO:0019867, IDA, PMID:18086184 | UNVERIFIABLE | Abstract only and does not name PA2590; the location itself is correct on sequence grounds (TonB-dependent receptor plug and barrel), so no PSEUDOCAP defect. | PA2070, PA2089, PA2057 (all the same PseudoCAP IDA, same paper) | Yes as a term; its evidence base is the same paper for all four seeds (see below) |

### Node-level assessment (shared with PA2070, PA2089, PA2057)

All four seeds of the PTN002933024 IBD (Q9I0P7 PA2590, Q9I245 PA2070, Q9I226 PA2089, Q9I258 PA2057) carry the same PseudoCAP IDA citing PMID:18086184, so no seed is independent of that one abstract-only paper. The IBD is nonetheless sound as a term: the 22 leaves (in PAO1, Shewanella oneidensis MR-1 and Xanthomonas campestris) are all TonB-dependent receptors (BtuB, BfeA and relatives), and the outer membrane location follows from the receptor fold whatever the paper showed. No GO_CENTRAL defect. The node term is less precise than GO:0009279 cell outer membrane, which every leaf could carry; this is a granularity note, not a defect. The leaf IBA rows are reviewed TOO_GENERAL in all four genes, because each review accepts GO:0009279 (is_a GO:0019867).
