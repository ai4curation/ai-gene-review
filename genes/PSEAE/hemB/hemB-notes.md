# hemB (PA5243, Q59643) review notes

No deep-research provider was available; notes compiled from the UniProt entry and cached abstracts.

- ALAD / porphobilinogen synthase, EC 4.2.1.24, homooctamer (UniProt, PMID:10356331, PMID:12079382, PMID:19822707).
- [PMID:16819823 "Porphobilinogen synthase catalyzes the first committed step of the tetrapyrrole biosynthesis pathway"]; [PMID:16819823 "one of the determined protein structures provides for the first time structural evidence of a magnesium ion in the active site"].
- [PMID:9529530 "The hemB gene was cloned from Pseudomonas aeruginosa by functional complementation of an E. coli hemB mutant"]; [PMID:9529530 "P. aeruginosa hemB was overexpressed in an E. coli hemB mutant using the phage T7 RNA polymerase system and its Mg(2+)-dependent activity was directly demonstrated"].
- Both papers abstract-only (no PMCID).

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | other seeds | IBD stands without this seed? | verdict | rationale |
|---|---|---|---|---|---|---|---|---|
| PTN000156046 | GO:0004655 porphobilinogen synthase activity | 9 | 149 (126 taxa) | GO:0004655, IMP, PMID:9529530 (PseudoCAP; also UniProt EXP PMID:16819823) | E. coli HemB P0ACB2, human ALAD P13716, bovine Q58DK5, mouse, rat, yeast HEM2, fly, Plasmodium Q8IL68 | Yes | SOUND | Activity directly measured after overexpression; complementation agrees. IDA would fit as well as IMP. Node term suits the ALAD family. |

No source defects. Metal ion binding MODIFY to magnesium ion binding. Actions: 9 ACCEPT, 1 MODIFY.
