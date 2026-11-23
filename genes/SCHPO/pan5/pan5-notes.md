# pan5 (Q9HDU6, SPBPB2B2.09c) notes

Role: ketopantoate reductase PanE (EC 1.1.1.169); module `coenzyme_a_biosynthesis` (pantoate branch, step 2).
Fetch: `just fetch-gene SCHPO pan5` FAILED (no UniProt gene name: "PomBase; SPBPB2B2.09c; -."); refetched with `-u Q9HDU6`.

## Evidence
- [UniProt:Q9HDU6 "FUNCTION: Catalyzes the NADPH-dependent reduction of ketopantoate into"] (by similarity). No S. pombe experimental data on activity.
- S. pombe ORFeome: cytosol and nucleus (HDA, PMID:16823372). No transit peptide.
- S. cerevisiae PAN5 deletion still prototrophic [PMID:19266201 "loss of PAN5 (related to panE from E. coli) still allows prototrophic growth"].

## Decisions
- REMOVE mitochondrion IBA: node PTN001093729 has a single donor SGD:S000002605, which is not PAN5 (S000001105) — the S. cerevisiae PAN5 review identifies it as CBS2. PomBase GO-CAM 67b1629100001098 places pan5 in mitochondrion on the basis of this IBA (evidence ECO:0000318 with PTN001093729), which conflicts with the S. pombe HDA cytosol annotation.
- NADP binding IBA, nucleus HDA non-core.
- Core: GO:0008677 / GO:0015940 / GO:0005829 — matches S. cerevisiae PAN5 review.
