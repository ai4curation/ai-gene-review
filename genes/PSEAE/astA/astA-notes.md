# astA (aruF, PA0896, P80357) review notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE P80357 --alias astA`; accession matches the worklist. No
deep-research provider used. PMID:16593724, PMID:7523119 and PMID:9393691 are abstract-only
(PubMed MCP returned no body for PMC323859 or PMC179677).

### Literature

- Arginine/ornithine succinyltransferase purified to homogeneity; two subunits, heterotetramer
  [PMID:7523119 "After SDS/PAGE two subunits of 35 kDa and 37 kDa were evident, indicating that the enzyme is a heterotetramer."]
  The N-terminal sequences of these subunits define P80357 (alpha, AruF) and P80358 (beta, AruG).
- [PMID:9393691 "the aruF and aruG genes encode the subunits (AruAI and AruAII) of arginine and ornithine N2-succinyltransferases."]
- Pathway: [PMID:16593724 "Enzyme assays with crude P. aeruginosa extracts established the following pathway"].
- Family: Pfam AstA (PF04958) and AstA_C, InterPro IPR016181 acyl-CoA N-acyltransferase (GNAT-like),
  NCBIfam TIGR03245. Not homologous to the AstB dihydrolase (Pfam AstB, PF04996), but PANTHER
  places both in PTHR30420 (AstA/AruG as SF1, 53 members; AstB as SF2, 138 members).
- UniProt's SIMILARITY line ("Belongs to the succinylarginine dihydrolase family", ECO:0000305)
  appears to follow the PANTHER family name; on domain content AstA is an arginine
  N-succinyltransferase. Not recorded as a structured defect (not tied to an annotation row);
  flagged here for UniProt.

### Annotation decisions

- ACCEPT: GO:0006527 (IDA, IBA, IEA), GO:0008791 (IEA).
- REMOVE: GO:0009015 N-succinylarginine dihydrolase activity (IBA). Node-level GO_CENTRAL defect
  recorded here (CONFIRMED: leaf GAF checked, PTN000764516 delivers GO:0009015 to 7 AstA-type
  leaves: P0AE37, P80357, P80358, Q8EJ55, Q8ZPV1, Q9KNW3, Q9ZC67).
- Not proposed as NEW: ornithine catabolism. The purified enzyme succinylates L-ornithine as well
  (PMID:7523119), so GO:0006593 L-ornithine catabolic process is plausible; left for a later pass.
- Action counts: ACCEPT 4, REMOVE 1. Source defects: GO_CENTRAL 1 (CONFIRMED).

## PseudoCAP IBA-seed assessment

PTN000764516 is shared with astB (PA0899) and aruG (PA0897); verdicts consistent across the three.
The GO:0009015 node defect is recorded here once and cross-referenced from astB and aruG.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000764516 | GO:0006527 L-arginine catabolic process | 4 | 12 (6 taxa) | GO:0006527, IDA, PMID:16593724 (PseudoCAP) | SOUND | AstA is the alpha subunit of arginine N-succinyltransferase, step 1 of the AST pathway. The 1986 paper establishes the pathway (extract assays, aru mutants); gene identity came later (PMID:7523119, PMID:9393691). Abstract only. | E. coli AstB P76216 (IMP PMID:9696779), astB O50175, aruG P80358 | Yes |
| PTN000764516 | GO:0009015 N-succinylarginine dihydrolase activity | 1 | 12 | not seeded by astA (sole seed E. coli AstB P76216, IDA PMID:15703173) | n/a (not a PseudoCAP seed) | Node term does not suit the clade: the node spans the AstA/AruG succinyltransferase subfamily, which has no dihydrolase activity. GO_CENTRAL defect recorded here. | — | Stands for AstB (SF2) only; must move to the SF2 node |
