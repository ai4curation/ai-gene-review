# tse6 (PA0093, Q9I739) review notes

## Review session 2026-11-13 (PseudoCAP tier 3, shared-claim group tse6/tsi6)

Fetched with `just fetch-gene PSEAE tse6`. No deep-research provider file was generated. Both cited
papers are cached **with full text**.

### The finding: the effector is annotated as if it were its own immunity protein

`GO:0097351 toxin sequestering activity` is annotated by IMP from PMID:24589350 to **both** halves
of the tse6-tsi6 bicistron. The term is defined as "Binding to a toxin to prevent it from
interacting with other partners or to inhibit its localization to the area of the cell or complex
where it is active" -- an immunity protein's job. Tse6 is the toxin.

The full text states the direction outright:
[PMID:24589350 "These results demonstrate that the Toxin_61 domain of Tse6 is a potent cytoplasmic
toxin whose activity can be specifically neutralized by Tsi6."] with the specificity control
[PMID:24589350 "the observed toxicity was specific to Tse6-CT as co-expression of Tsi6, but not the
non-cognate cytoplasmic immunity protein Tsi2, provided full rescue of E. coli viability"].

So the row is REMOVEd here and kept on tsi6, with a WRONG_GENE_PRODUCT PseudoCAP defect at
CONFIRMED asking for the deletion on Q9I739 and retention on Q9I740. Nothing is lost: Tse6's own
activity is carried by its NAD+ and NADP+ nucleosidase rows. This is the shared-claim pattern the
tier-3 worklist was built to surface -- one pair-level experiment entered on both genes.

### Annotation decisions

- ACCEPT: GO:0050135 (IDA, the assayed activity and the mechanism of toxicity), GO:0003953 (IEA;
  a separate substrate rather than a general/specific pair), GO:0033103 (IDA and IMP).
- KEEP_AS_NON_CORE: GO:0016020 membrane -- plausible for a PAAR-motif effector carried on a VgrG
  spike, but no compartment is established and the toxin acts in the recipient cytoplasm.
- REMOVE: GO:0097351, as above.

A first draft attributed the quote "Tse5 and Tse6 delivery strictly required a cognate VgrG" to
PMID:24794869; it is in PMID:24589350. The reference validator caught it, and the row citing
PMID:24794869 now quotes that paper's own statement about VgrG1a-dependent toxicity and PA0093.

## Corrections, 2026-11-13 (PR #6341 review)

**The catalytic rows cited a quote about neutralisation.** `GO:0050135` and `GO:0003953` were
anchored to the PMID:24589350 sentence about Tsi6 neutralising the toxin, which says nothing about
catalysis, and so was the core function. PMID:26456113 was cached with full text in this very PR
and states it outright: [PMID:26456113 "Tse6, acts on target cells by degrading the universally
essential dinucleotides NAD(+) and NADP(+)"]. Both rows and the core function now rest on that.

**The GO:0033103 argument was the wrong one.** The reason given was that delivery required a
cognate VgrG -- but being carried by a secretion system is being its *cargo*, and a substrate is
not a participant; that is the same rule used two files away to downgrade tsi6's identical row, so
the two calls read as one argument applied two ways. The verdict stands, on a different basis:
Tse6 is an evolved PAAR protein, and [PMID:26456113 "PAAR repeat sequences, which fold into a
pyramidal structure that interacts with the tip of the VgrG spike"], so it supplies a structural
component the apparatus depends on -- the scaffold case CLAUDE.md works through for thyroglobulin.
That is also exactly what distinguishes it from Tsi6, which contributes nothing to the apparatus.
