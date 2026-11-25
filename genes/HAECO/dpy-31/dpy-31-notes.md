# dpy-31 notes

## 2026-11-20

- Seeded the review with `just fetch-gene HAECO dpy-31`, pinned to the shared
  retained environment. This fetched the reviewed UniProtKB record for
  `D5FM34` and six GOA IEA rows from UniProt, InterPro, ARBA, and PANTHER.
- No remote deep-research provider was invoked for this pass. The review uses
  the D5FM34 UniProtKB record, the cached abstract for PMID:19883650, and the
  freshly curated worm and BRUMA DPY-31 reviews to check action consistency
  across the `PTHR10127:SF813` DPY-31/NAS-35 subfamily.
- PMID:19883650 explicitly reports H. contortus in the abstract: it
  "identified" DPY-31 orthologs in *Haemonchus contortus* and *Brugia malayi*,
  found that "heterologous expression of the H. contortus dpy-31 orthologue in
  a C. elegans dpy-31 mutant resulted in the full rescue of the mutant body
  form", and showed that recombinant DPY-31 enzymes from both parasites process
  C. elegans SQT-3 "at the correct C-terminal procollagen processing site".
- Local GOA has only IEA rows for D5FM34, while the reviewed UniProtKB record
  cites PMID:19883650 for H. contortus genomic sequence, catalytic activity,
  alternative splicing, and DPY-31/NAS-35 nomenclature.
- Native H. contortus cuticular substrates and an in-species loss-of-function
  phenotype remain inferred from heterologous rescue and SQT-3 cleavage rather
  than assayed directly.
