# kynB (PA2081, Q9I234) review notes

Bacterial kynurenine formamidase, step 2 of the aerobic kynurenine (anthranilate)
pathway of tryptophan degradation. Full text of PMID:24942958 read (PMC4243253): the
P. aeruginosa enzyme (PaKynB) was expressed, purified and assayed, and crystallised
with a binuclear Zn2+ centre [PMID:24942958 "we characterize the catalytic properties and present the crystal structures of three bacterial kynurenine formamidases"]. Earlier, PMID:14592712 cloned, expressed and characterised the P. aeruginosa ortholog [PMID:14592712 "This functional prediction was experimentally verified by cloning, expression and enzymatic characterization of recombinant kynurenine formamidase orthologs from Bacillus cereus, Pseudomonas aeruginosa and Ralstonia metallidurans."].

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001258690 | GO:0004061 arylformamidase activity | 2 | 163 (62 taxa) | GO:0004061, IDA PMID:14592712 (PseudoCAP/UniProt), IDA PMID:24942958 (UniProt) | SOUND | PaKynB directly assayed and crystallised. The self-seed (Q9I234) is expected. | B. cereus KynB Q81CK1 (IDA PMID:14592712) | Yes |

Node term is the exact activity and suits the KynB clade. No PSEUDOCAP or GO_CENTRAL
defect on the seed.

Other row: GO:0004328 formamidase activity (InterPro IPR017484 -> GO:0004328) is a
different reaction (formamide amidohydrolase, EC 3.5.1.49). GO:0004061 is not a child
of GO:0004328; they are siblings under GO:0016811. REMOVE as a wrong InterPro2GO
mapping (GO_REF:0000002); no PseudoCAP defect (not a PseudoCAP row).
