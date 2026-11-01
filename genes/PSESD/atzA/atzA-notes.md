# Notes: atzA (atrazine chlorohydrolase, Pseudomonas sp. ADP)

Reviewed as part of `projects/NONPHYSIOLOGICAL_REACTIONS.md`, specifically the
category-4 counter-example set: enzymes whose substrates are man-made but whose
functions are real and selected.

## Why this gene is in the set

Atrazine is a synthetic herbicide introduced in the 1950s. A naive "synthetic
substrate implies non-physiological activity" filter would flag atzA. It should
not: Pseudomonas sp. ADP uses atrazine as a nitrogen source and atzA is the
committed first step [PMID:8759853 "Pseudomonas sp. strain ADP metabolizes atrazine to carbon dioxide and ammonia via the intermediate hydroxyatrazine."].

## Evidence

- Purified enzyme, hydrolytic mechanism established by (18)O labelling
  [PMID:8759853 "The purified enzyme in H2(18)O yielded [18O]hydroxyatrazine, indicating that AtzA is a chlorohydrolase and not an oxygenase."].
- Narrow specificity: atrazine, simazine, desethylatrazine; not terbutylazine,
  desethyldesisopropylatrazine or melamine
  [PMID:8759853 "AtzA catalyzes the dechlorination of atrazine, simazine, and desethylatrazine but is not active with melamine, terbutylazine, or desethyldesisopropylatrazine."].
- kcat/Km for atrazine 14,600 s-1.M-1, no measurable deaminase activity
  [PMID:22768133 "AtzA is an efficient atrazine dechlorinase with no measurable deaminase activity"].

## Annotation finding: fold-level IEA to the wrong bond class

GO:0016810 (hydrolase acting on C-N but not peptide bonds) comes from
IPR011059, a metal-dependent hydrolase composite domain shared across the
amidohydrolase superfamily, whose best-known members are deaminases. AtzA
cleaves a C-halide bond and sits under GO:0019120, a sibling branch. REMOVE.

The instructive part: the 98%-identical paralog TriA (melamine deaminase),
differing at nine residues, *does* belong in GO:0016810
[PMID:11274097 "AtzA was shown to exclusively catalyze dehalogenation of halo-substituted triazine ring compounds and had no activity with melamine and ammeline."].
So the term is right for the family and wrong for this member, which is exactly
what a fold-based inference cannot distinguish. Same failure mode as the
GO:0004301 epoxide hydrolase annotation on XANAU/dhlA.

GO:0016787 (root hydrolase) is redundant with the specific activity:
MARK_AS_OVER_ANNOTATED.

## Contrast with the benzil reductase case

The Rhea-derived IEA here (GO_REF:0000120, RHEA:11312 + EC:3.8.1.8) lands on
the correct specific term GO:0018788 because RHEA:11312 is an exactMatch. That
is the arrangement RHEA:25968 should have on GO:0004090 rather than a
narrowMatch on the grouping class GO:0016616.

## Open question

Which of AtzA and TriA is ancestral is unresolved, and no natural triazine
substrate has been tested for either.
