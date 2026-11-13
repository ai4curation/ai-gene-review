# tsi6 (PA0092, Q9I740) review notes

## Review session 2026-11-13 (PseudoCAP tier 3, shared-claim group tse6/tsi6)

Fetched with `just fetch-gene PSEAE tsi6`. No deep-research provider file was generated.

Two rows, and they pull in opposite directions once the full text is read.

**GO:0097351 toxin sequestering activity: correct, and this is the core function.** Tsi6 is the
cognate immunity protein that neutralises Tse6, with the non-cognate control that makes it
specific: [PMID:24589350 "the observed toxicity was specific to Tse6-CT as co-expression of Tsi6,
but not the non-cognate cytoplasmic immunity protein Tsi2, provided full rescue of E. coli
viability"]. The same term on the effector tse6 inverts the relationship and is recommended for
deletion in that review.

**GO:0033103 protein secretion by the type VI secretion system: over-annotated.** The paper
describes tsi6 as [PMID:24589350 "all located upstream of a small ORF that encodes a protein with
predicted cytoplasmic localization"] and tests it as a PA0093-specific immunity determinant; the
row appears to come from the pair-level competition experiment,
[PMID:24589350 "Taken together, these data indicate that PA0093–PA0092 are H1-T6SS E–I pair that
participate in interbacterial interactions."] That shows tsi6 is required for the outcome of those
competitions, not that it does any of the work of protein secretion -- the project's rule on
`involved_in` draws exactly this line. Marked over-annotated rather than removed, since tsi6 is
genuinely part of the H1-T6SS locus and a secretion-related role is not excluded by what is
reported.
