# Notes: dhlA (haloalkane dehalogenase, Xanthobacter autotrophicus GJ10)

Part of the category-4 counter-example set in
`projects/NONPHYSIOLOGICAL_REACTIONS.md`.

## Why this gene is in the set

1,2-dichloroethane is a high-volume industrial commodity chemical (vinyl
chloride manufacture). X. autotrophicus GJ10 grows on it as sole carbon
source, with dhlA as step 1 of 4. Cofactor-independent, alpha/beta-hydrolase
fold, Asp-His-Asp triad with a covalent alkyl-enzyme intermediate established
crystallographically. Substrate range: terminal mono- and di-chlorinated and
brominated alkanes up to C4, best on 1,2-dichloroethane, 1,3-dichloropropane
and 1,2-dibromoethane.

## Annotation finding: the correct Rhea arrangement

GO:0018786 haloalkane dehalogenase activity holds RHEA:19081 (the generic
1-haloalkane reaction) as an **exactMatch** and the specific RHEA:25185
(1,2-dichloroethane) as a **narrowMatch**. That is exactly right: the specific
reaction attaches as a narrowMatch to a term defined over the substrate class,
not to an EC-level grouping term.

This is the template for fixing RHEA:25968, which currently sits as a
narrowMatch on the EC 1.1.1.- grouping class GO:0016616 and should move to
GO:0004090 carbonyl reductase (NADPH) activity.

## Annotation finding: epoxide hydrolase by fold transfer

GO:0004301 epoxide hydrolase activity arrives via TreeGrafter from
PANTHER:PTN000107240. Epoxide hydrolases and haloalkane dehalogenases share the
alpha/beta-hydrolase fold and an analogous nucleophile-His-acid triad, so they
cluster in sequence-based trees, but the reactions differ: ring-opening of a
strained C-O-C to a diol versus displacement of halide from a saturated carbon.
No epoxide is reported as a dhlA substrate. REMOVE, with a propagation_review
recording PROPAGATION_BAD / FUNCTIONAL_DIVERGENCE.

Same failure mode as GO:0016810 on PSESD/atzA: a structural signature
predicting the superfamily's prevalent chemistry rather than the member's own
reaction. Two occurrences in a six-gene set suggests this is worth counting
systematically; the fix belongs at the PANTHER node, not per gene.

GO:0003824 (root catalytic activity, from the epoxide hydrolase-like IPR000639)
is the least informative possible MF statement: MARK_AS_OVER_ANNOTATED.

## Curation gap

As with tfdA and pcpB, no experimental GO annotation exists despite a solved
structure, trapped reaction intermediates and decades of mechanistic work.

## Ancestral substrate

Unknown and untested. Biogenic halomethanes and haloethanes are produced in
marine and soil environments, so an ancient origin is plausible, but the
hypothesis has not been tested for this enzyme.
