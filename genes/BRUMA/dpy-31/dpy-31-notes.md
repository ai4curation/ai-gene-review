# BRUMA dpy-31 notes

## 2026-11-20

- Ran `just fetch-gene BRUMA dpy-31` before this cross-check. The command
  backfilled `supporting_entities` for the six existing GOA rows in
  `dpy-31-ai-review.yaml`; remote UniProt and GOA records differed from the
  checked-in cache, but this pass did not force-refresh those source files.
- `genes/BRUMA/dpy-31/dpy-31-uniprot.txt` is the UniProtKB/Swiss-Prot record
  for A8Q2D1 and places the protein in PANTHER `PTHR10127:SF813`, the same
  DPY-31/NAS-35 subfamily used in the nematode cuticle collagen maturation
  module for worm P98060 and HAECO D5FM34.
- PMID:19883650 is cached as an abstract only, but it directly names the
  Brugia ortholog and states that "the recombinant DPY-31 enzymes from both
  H. contortus and B. malayi" cleaved the C. elegans cuticle collagen SQT-3 at
  the expected C-terminal procollagen processing site.
- PMID:26546217 is cached as full text and supports retaining DPY-31 as a
  biochemically active parasite enzyme and nematode drug-target anchor: the
  study screened 104 compounds against recombinant DPY-31 from the human
  parasite B. malayi and sheep parasite T. circumcincta.
- This cross-check did not invoke a remote deep-research provider. It used the
  existing initialized BRUMA review, the cached UniProt/GOA records, the cached
  primary DPY-31 publications, the nematode cuticle collagen maturation module,
  and the freshly reviewed worm DPY-31 ortholog.
- UniProt records direct experimental support on A8Q2D1 for the partial EC
  assignment and FUNCTION line through PMID:19883650 and PMID:26546217, but the
  local GOA file contains only IEA rows. The recombinant B. malayi cleavage
  result supports the existing `GO:0004222` claim experimentally, so it is a
  curation gap rather than a candidate `NEW` row.
- The previous review treated `GO:0008237` metallopeptidase activity as
  `MARK_AS_OVER_ANNOTATED`; under the 2026-11-14 action ruling this is better
  modeled as `TOO_GENERAL` because it is a true parent of the accepted
  `GO:0004222` metalloendopeptidase activity row.
- The B. malayi evidence demonstrates recombinant cleavage and inhibition.
  Native B. malayi cuticular substrates and an in-species loss-of-function
  phenotype remain inferred from conservation with C. elegans rather than
  assayed directly.
