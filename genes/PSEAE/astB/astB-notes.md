# astB (aruB, PA0899, O50175) review notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE O50175 --alias astB`; accession matches the worklist. No
deep-research provider used. PMID:16593724 and PMID:9393691 are abstract-only (PubMed MCP returned
no body for PMC323859 or PMC179677).

### Literature

- AST pathway defined in P. aeruginosa from aru mutants and crude-extract enzyme assays
  [PMID:16593724 "Enzyme assays with crude P. aeruginosa extracts established the following pathway: L-arginine + succinyl-CoA --> N(2)-succinylarginine --> N(2)-succinylornithine --> N_succinylglutamate 5-semialdehyde --> N-succinylglutamate --> succinate + glutamate."]
  Some aru mutants accumulated N2-succinylarginine, the expected phenotype of a dihydrolase block.
- Genes assigned later [PMID:9393691 "The aruR, aruC, aruD, aruB, and aruE genes specify the ArgR regulatory protein, N2-succinylornithine 5-aminotransferase, N-succinylglutamate 5-semialdehyde dehydrogenase, N2-succinylarginine dihydrolase, and N-succinylglutamate desuccinylase, respectively"].
- Family: Pfam AstB (PF04996), HAMAP MF_01172, NCBIfam TIGR03241. PANTHER puts AstB in
  PTHR30420:SF2, but the same PANTHER family also holds the unrelated AstA/AruG
  succinyltransferases (SF1, Pfam AstA, GNAT-like acyl-CoA N-acyltransferase fold).

### Annotation decisions

- ACCEPT: GO:0009015 (IBA, IEA), GO:0006527 (IDA, IBA, IEA).
- TOO_GENERAL: GO:0006525 arginine metabolic process (IEA); GO:0006527 is_a GO:0006525.
- Pathway-specific children of GO:0006527 (GO:0019544, GO:0019545) are obsolete, so GO:0006527 is
  as precise as GO allows.
- Action counts: ACCEPT 5, TOO_GENERAL 1. No source defects on this gene.

## PseudoCAP IBA-seed assessment

PTN000764516 is shared with astA (PA0896) and aruG (PA0897); verdicts are kept consistent. The
node-level GO_CENTRAL defect for the GO:0009015 IBD (dihydrolase placed at a node that also covers
the AstA succinyltransferase subfamily) is recorded once, on astA. On astB itself the GO:0009015
IBA is correct.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000764516 | GO:0006527 L-arginine catabolic process | 4 | 12 (6 taxa) | GO:0006527, IDA, PMID:16593724 (PseudoCAP) | SOUND | The term is right for AstB (step 2 of the AST pathway). The 1986 paper defines the pathway by extract assays and aru mutants; gene identity came in PMID:9393691, so the paper supports the pathway rather than naming this locus. Abstract only. | E. coli AstB P76216 (IMP PMID:9696779), astA P80357, aruG P80358 (same PseudoCAP paper) | Yes (E. coli AstB) |
| PTN000764516 | GO:0009015 N-succinylarginine dihydrolase activity | 1 | 12 | not seeded by astB (sole seed E. coli AstB P76216, IDA PMID:15703173) | n/a | Correct for the AstB subfamily; wrongly inherited by AstA/AruG leaves. | — | Stands for SF2; defect recorded on astA |
