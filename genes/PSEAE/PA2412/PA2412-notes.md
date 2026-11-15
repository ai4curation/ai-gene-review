# PA2412 (Q9I169) notes

PubMed search returned API errors on 2026-11-05, so later MbtH-NRPS papers on
PA2412 could not be retrieved; all three PseudoCAP papers are abstract only.

## Literature

- Deletion phenotype [PMID:17502378 "Our results demonstrate that PA2412 is necessary for the production or secretion of pyoverdine at normal levels. The PA2412 deletion strain is able to use exogenously produced pyoverdine"].
- Co-expression [PMID:17502378 "Coexpressed with the pyoverdine synthetic enzymes is a 72-amino acid MbtH-like family member designated PA2412."].
- Ochsner 2002 is a GeneChip study [PMID:12207696 "Under low-iron conditions, expression of 26 genes or operons was reduced in a DeltapvdS mutant"]; the abstract does not state a PA2412 mutant was assayed.
- Lamont and Martin 2003 mutated candidates [PMID:12686626 "The candidate genes were mutated and the effects of the mutations on pyoverdine production were determined."]; PA2412 not named in the abstract.

## PseudoCAP IBA-seed assessment

Other seeds' experimental support queried live in QuickGO on 2026-11-05.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002212932 | GO:0019290 siderophore biosynthetic process | 2 | 8 (7 taxa) | GO:0002049, IMP, PMID:17502378 | SOUND | Deletion lowers pyoverdine output; uptake normal. | E. coli YbdZ P18393 (IMP PMID:20845982, IDA PMID:28880538 enterobactin biosynthesis) | Yes |
| PTN002212932 | same | 2 | 8 | GO:0002049, IMP, PMID:12686626 | UNVERIFIABLE | Abstract does not name PA2412; term correct anyway. | as above | Yes |
| PTN002212932 | same | 2 | 8 | GO:0002049, IMP, PMID:12207696 | UNVERIFIABLE | Expression study; mutant not stated in abstract; term correct anyway. | as above | Yes |

No PSEUDOCAP or GO_CENTRAL defect (term true for PA2412; node term suits
NRPS-associated MbtH-like proteins).
