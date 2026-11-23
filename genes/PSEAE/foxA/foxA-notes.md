# foxA (PA2466, Q9I116) notes

## Literature (own research, 2026-11-05; no deep-research provider available)

- FoxA is the TonB-dependent receptor for ferrioxamines [PMID:39138320 "FoxA of the ferric forms of nocardamine, bisucaberin, DFOB and DFOG"; "Iron complexed by desferioxamine G is transported by FpvB and FoxA"]. Growth and 55Fe uptake with TBDT deletion mutants.
- Signalling: [PMID:35138377 "The binding of Fe3+ferrioxamine B to the FoxA OM protein triggers the transcription of ferrioxamine transport genes"]; [PMID:25809487 "Upon binding of ferrioxamine by the FoxA receptor, FoxR is processed by a complex proteolytic cascade leading to the release and activation of σ(FoxI)"]. STN domain at residues 78-129 (SMART SM00965).
- Regulation: produced only with ferrioxamine B or ferrichrome [PMID:16484199 "Two of them are only produced in the presence of the hydroxamate siderophores ferrioxamine B and ferrichrome"].
- PMID:16484199 is abstract-only here; the full text could not be retrieved this session (PMC page refused, Europe PMC 500). The earlier foxI review read it and reports FoxI overexpression inducing FoxA and that FoxA is absent in a foxA mutant; whether foxA mutant transport assays are in it is not recorded.
- UniProt Q9I116 carries the wrong ARBA name "Metal-pseudopaline receptor CntO" (UNIPROT source defect recorded on the UniProt reference), as does FiuA.
- Consistent with the foxI review (FoxI transcribes foxA; FoxA is the ferrioxamine receptor).

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000793005 | GO:0015344 siderophore uptake transmembrane transporter activity | 3 | 68 (13 taxa) | GO:0015344, IMP, PMID:16484199 | UNVERIFIABLE | The term is correct for FoxA (mutant growth and 55Fe uptake, PMID:39138320), but the cited abstract shows only proteomic identification and regulation; the full text could not be read to confirm a transport phenotype. | E. coli FhuA P06971 (GO:0015344 IDA PMID:9613584, IMP PMID:1089064); E. coli Fiu P75780 (GO:0015344 IDA PMID:2139424, IMP PMID:31712312) | Yes; two independent E. coli seeds with IDA and IMP |

Other seeds queried live in QuickGO (2026-11-05). The node term suits a TonB-dependent siderophore receptor clade. No PseudoCAP or GO_CENTRAL defect. The GO:0033214 IBD at the same node (seeded by FiuA) is assessed in genes/PSEAE/fiuA/fiuA-notes.md; both are sound.

## Action counts

ACCEPT 8, MODIFY 4, TOO_GENERAL 1.
