# S. pombe tim44 notes

Automated Falcon/Perplexity deep research failed locally, so this review uses a
manual evidence pass over the cached UniProt record, the cached
budding-yeast PAM literature, and the existing PTHR10721 Tim44 PAINT table.

GO-CAM 69729a3800007453 models PomBase:SPBC14C8.02/tim44 with
`GO:0140378 protein complex scaffold activity`, `GO:0030150 protein import
into mitochondrial matrix`, and `GO:0005759 mitochondrial matrix`. This agrees
with the gene review: `GO:0140378` is a missing 2026 PAINT assertion in the
current GOA seed, the matrix-import process is the conserved PAM role, and the
matrix location is acceptable for the activity of a peripheral mitochondrial
inner-membrane scaffold whose functional face is exposed to the matrix.

All seeded rows were inference rows rather than direct S. pombe experimental
rows. The accepted `GO:0001405` and `GO:0030150` IBA rows come from
`PTHR10721 PTN000076497`, which has no loss on the S. pombe `tim44` lineage;
the seeded `GO:0051087` IBA is stale relative to the current PAINT table but
is still correct for the conserved Tim44-mtHsp70 interaction. The accepted ISS
rows transfer budding-yeast Tim44 function and localization from
UniProtKB:Q01852. Hutu et al. 2008 showed directly in budding yeast that
`tim44` mutants selectively impair matrix-targeted precursor import and alter
the association of Pam18/Pam16 and Pam17 at TIM23, supporting the conserved
scaffold/adaptor interpretation.
