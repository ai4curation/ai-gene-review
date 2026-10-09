# Notes: pcpB (pentachlorophenol 4-monooxygenase, Sphingobium chlorophenolicum)

Part of the category-4 counter-example set in
`projects/NONPHYSIOLOGICAL_REACTIONS.md`. This is the most important member of
that set, because it breaks the kinetic heuristic.

## Why this gene matters for the project

A tempting signal for detecting non-physiological activities is low catalytic
efficiency: benzil reductase turns over at 9-64 min-1, far below a
well-matched enzyme. pcpB refutes it as a standalone criterion. Its kcat is
0.024 s-1
[PMID:22482720 "The k(cat) for PCP (0.024 s(-1)) is very low, suggesting that the enzyme is not well evolved for turnover of this substrate."],
and it is nonetheless the committed, flux-limiting step of its host's genuine
catabolic pathway
[PMID:22482720 "Flux through the pathway is limited by PCP hydroxylase."].

So the discriminator between "assay artefact" and "real but unoptimized" cannot
be kcat. It has to be pathway membership plus host genetics.

## How bad the enzyme actually is

- Extensive uncoupling: the C4a-hydroxyflavin intermediate decomposes to H2O2
  in a futile cycle consuming NADPH
  [PMID:22482720 "the C4a-hydroxyflavin intermediate, instead of hydroxylating the substrate, can decompose to produce H(2)O(2) in a futile cycle that consumes NADPH"].
- Promiscuous activity on the downstream metabolite tetrachlorohydroquinone,
  which reverses pathway flux. An activity of this enzyme that is actively
  detrimental to the host.
- The pathway itself was assembled by patching horizontally acquired enzymes
  into existing metabolism
  [PMID:22482720 "S. chlorophenolicum appears to have assembled a poorly functioning pathway for degradation of PCP by patching enzymes recruited via two independent horizontal gene transfer events into an existing metabolic pathway."].

PCP was introduced in the 1930s, so this is a pathway caught early in
optimization: real function, incomplete adaptation. No GO annotation conveys
that, which is raised as a question in the review.

## Annotation calls

- GO:0018677 (RHEA:18685 exactMatch) ACCEPT; correct specific term.
- GO:0016709 (ARBA) and GO:0016491 (root) are ancestors of it:
  MARK_AS_OVER_ANNOTATED. Unlike the atzA GO:0016810 case, the chemistry is
  right here; only the granularity is wrong.
- GO:0071949 FAD binding ACCEPT, corroborated by the flavin intermediate work.
- As with tfdA and dhlA, no experimental MF annotation exists despite the
  enzymology.

## Ancestral substrate

Unknown. Structure-activity work shows the enzyme prefers phenols with a low
phenolic pKa, high hydrophobicity and an ortho substituent to the hydroxyl,
which narrows the candidate set, but no natural phenol has been shown to be a
better substrate than PCP.
