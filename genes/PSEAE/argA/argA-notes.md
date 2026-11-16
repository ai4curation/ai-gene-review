# argA (PA5204, P22567) review notes

## Literature summary

- ArgA is the classical NAGS, the first enzyme of arginine biosynthesis [PMID:22447897 "N -acetyl- l -glutamate synthase (NAGS), the enzyme encoded by argA , catalyzes the first step of arginine biosynthesis"], using acetyl-CoA as the acetyl donor [PMID:22447897 "producing N -acetyl- l -glutamate (NAG) from glutamate and acetyl coenzyme A (acetyl-CoA) and being feedback inhibited by arginine"].
- The activity assays in this paper use glutamate plus acetyl-CoA [PMID:22447897 "30 mM l -glutamate (sodium salt), 4 mM acetyl-CoA, and, when used, the indicated concentrations of arginine hydrochloride"].
- Domain dissection: [PMID:22447897 "The AAK domain was hexameric and inactive, whereas the GNAT domain was monomeric/dimeric and catalytically active"]; [PMID:22447897 "the hexameric architecture appears to be essential for arginine inhibition"].
- The UniProt record gives the acetyl-CoA reaction (RHEA:24292) and the HAMAP rule MF_01105 (N_acetyl_glu_synth).

Literature search (2026-11-05): PubMed MCP and NCBI E-utilities failed all session; Europe PMC search was
intermittent. The review rests on PMID:22447897 (full text cached, read), the UniProt record, and live QuickGO
queries for the E. coli seed P0A6C5 and for the GO:0004042/GO:0004358 definitions and synonyms.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN004744913 | GO:0006526 L-arginine biosynthetic process | 2 | 95 (48 taxa) | GO:0006526, IMP, PMID:22447897 | SOUND | ArgA catalyses the first step of the pathway. The evidence is biochemical (IDA would be the better code), but the claim is right. | E. coli ArgA P0A6C5 (EcoCyc IMP PMID:1102931, IDA PMID:17651682) | Yes; E. coli ArgA IMP/IDA |
| PTN004744913 | GO:0004358 L-glutamate N-acetyltransferase activity, acting on acetyl-L-ornithine as donor | 2 | 95 (48 taxa) | GO:0004358, IMP, PMID:22447897 | WRONG | Full text read: all assays use acetyl-CoA plus glutamate (GO:0004042). GO:0004358 is the ArgJ ornithine-acetyltransferase reaction. The two terms share the synonyms "N-acetylglutamate synthase activity" and "L-glutamate N-acetyltransferase activity" (checked in QuickGO), the likely cause. | E. coli ArgA P0A6C5 (EcoCyc IDA PMID:16890, PMID:17651682), same error: E. coli ArgA is also the acetyl-CoA NAGS (UniProt P0A6C5 reaction; PMID:16890 is titled "N-acetylglutamate synthase of Escherichia coli") | No. The only other seed has the same error, so the node term is wrong for the ArgA clade. GO_CENTRAL defect filed (CONFIRMED), repoint to GO:0004042 |

Defects filed on this gene:

- PSEUDOCAP WRONG_TERM on the GO:0004358 IMP row, CONFIRMED (full text read), repoint to GO:0004042.
- GO_CENTRAL WRONG_TERM on the GO:0004358 IBA row (node PTN004744913), CONFIRMED, repoint to GO:0004042.
- UNIPROT WRONG_TERM on the ARBA00086662 GO:0004358 IEA row, PROBABLE.
- Not filed here (another resource's record on another gene): the EcoCyc GO:0004358 IDA rows on E. coli ArgA P0A6C5
  have the same error and should be repointed to GO:0004042.

## Action summary

10 rows. MODIFY 4 (GO:0004358 IBA, IEA and IMP to GO:0004042; GO:0016747 IEA to GO:0004042); ACCEPT 5
(GO:0006526 x3, GO:0004042 IEA, GO:0005737 IEA); KEEP_AS_NON_CORE 1 (GO:0042802 IPI).
