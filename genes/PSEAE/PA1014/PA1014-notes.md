# PA1014 (Q9I4V9, WapB) review notes

No deep-research provider was available. Sources: UniProt record (TrEMBL), cached
PMID:21441506 (abstract only; the PubMed MCP returned no full-text body for
PMC3133124). PubMed and Europe PMC searches failed on 2026-11-05 (server errors),
so no further literature could be retrieved.

## Function

- PA1014 is required for LPS outer-core biosynthesis and was renamed wapB
  [PMID:21441506 "Here, we show that a previously uncharacterized gene, pa1014, is involved in outer core biosynthesis"].
- The mutant core lacks the terminal beta-1,2-linked glucose; complementation restores it
  [PMID:21441506 "revealed that the core OS of the wapB mutant lacked the terminal β-1,2-linked-d-glucose residue"].
- Gain of function in 11 IATS serotypes lacking Glc(IV); the authors conclude a 1,2-glucosyltransferase
  [PMID:21441506 "Our results strongly suggested that wapB encodes a 1,2-glucosyltransferase."].
- Domain: GT2-like (InterPro IPR001173), nucleotide-diphospho-sugar transferase fold (IPR029044); PANTHER PTHR43685:SF2.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000531320 | GO:0016757 glycosyltransferase activity | 7 | 44 (17 taxa) | GO:0008919 LPS glucosyltransferase I activity, IDA, PMID:21441506 (PseudoCAP) | SOUND | Mutant LPS structure, complementation and gain of function in other serotypes show WapB adds the terminal outer-core glucose; the generic node term is certainly true. Evidence code probably IMP rather than IDA (SUSPECTED PSEUDOCAP WRONG_EVIDENCE_CODE; does not affect the term). | WapR Q9HUG5, MigA Q9I5M1 (P. aeruginosa outer-core GTs), B. subtilis SunS O31986, Salmonella RfbV P26401, E. coli WcaA P77414, M. tuberculosis Rv2957 P9WMX7 | Yes; generic GT activity for a GT2 clade rests on several characterised members. No GO_CENTRAL defect. |

PA1014 also receives GO:0009244 (LPS core region biosynthetic process) from the child node
PTN000531351, which it does not seed (seeds WapR and MigA, reviewed in parallel). The term is
directly supported for PA1014 by its own mutant data; no node defect from this gene.

Defects recorded: PSEUDOCAP 1 (WRONG_EVIDENCE_CODE, SUSPECTED, CHECK); GO_CENTRAL 0.
