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

## Session 2026-11-12: consolidated with the retired aruF review

This folder duplicated `genes/PSEAE/aruF`, which main had added for the same accession (P80357)
through the AST-module pass. astA survives as the folder name: GOA/PseudoCAP give the symbol as
astA, UniProt has `GN Name=astA` with `aruF` only as a synonym, and main's aruF file itself already
carried `gene_symbol: astA`. The two reviews agreed on all five actions; where they differed, the
aruF pass was right, so its readings were carried across and the notes above are superseded on two
points:

- The SIMILARITY line **is** now recorded as a structured defect. The note above said it was "not
  recorded as a structured defect (not tied to an annotation row)". That rationale was wrong:
  `references[].reference_review.source_defects` is exactly the slot for a defect in the record
  rather than in an annotation row, and it is the slot the aruG review uses for the identical error
  on the beta chain (UniProtKB:P80358). Leaving it out meant UniProt was told that one of the two
  chains of one heterotetramer has a wrong family line while the other, with the same evidence, was
  not reported. The P80357 entry is restored here as WRONG_STATEMENT / CC:SIMILARITY, PROBABLE,
  cross-referencing the beta chain so both are corrected together.
- GO:0008791 IEA now carries a WRONG_QUALIFIER UniProt defect (enables -> contributes_to), and the
  core function uses `contributes_to_molecular_function` rather than `molecular_function`. The
  purified enzyme is a heterotetramer of two different chains and no single chain is shown active
  alone, so the activity belongs to the complex; this is the idiom used for E. coli NuoB/NuoC and
  CysI. The action stays ACCEPT, since the term itself is right.
- Source defect count for this review is therefore 2, not the 1 recorded above: the node-level
  GO_CENTRAL WRONG_TERM (CONFIRMED) and this UniProt WRONG_STATEMENT (PROBABLE). The
  `full_text_unavailable: true` flags the aruF pass carried on PMID:16593724, PMID:7523119 and
  PMID:9393691 are also restored, so the abstract-only status is machine-readable and not only prose.
