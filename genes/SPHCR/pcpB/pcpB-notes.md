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

So the discriminator between "assay artefact" and "real but slow" cannot be
kcat. It has to be pathway membership plus host genetics.

**The OpenScientist run sharpened this further, and corrected my framing.** A
later paper from the same group argues the slow turnover is not a lack of
optimization at all but a selected optimum: TCBQ is a potent alkylating agent,
and slow release lets the reductase PcpD capture it before it escapes
[PMID:23676275 "The toxicity of TCBQ may have exerted selective pressure to maintain slow turnover of PcpB (0.02 s(-1)) so that a transient interaction between PcpB and PcpD can occur before TCBQ is released from the active site of PcpB."].

That makes pcpB a *stronger* refutation of the kinetic heuristic, not a weaker
one. A low kcat here is evidence of selection, not of its absence. Both
readings fit the same measured number, so the review now records the
unoptimized-versus-selected question as a knowledge gap rather than asserting
either.

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
assembly. Whether it is also caught early in *optimization* is exactly the
open question above. No GO annotation conveys either property, which is raised
as a question in the review.

## Annotation calls

- GO:0018677 (RHEA:18685 exactMatch) ACCEPT; correct specific term.
- GO:0016709 (ARBA) and GO:0016491 (root) are ancestors of it:
  MARK_AS_OVER_ANNOTATED. Unlike the atzA GO:0016810 case, the chemistry is
  right here; only the granularity is wrong.
- GO:0071949 FAD binding ACCEPT, corroborated by the flavin intermediate work.
- As with tfdA and dhlA, no experimental MF annotation exists despite the
  enzymology. The OpenScientist run independently flagged that GO:0018677 and
  GO:0071949 are upgradeable from IEA to EXP/IDA on PMID:22482720.

## Ancestral substrate

Unknown. Structure-activity work shows the enzyme prefers phenols with a low
phenolic pKa, high hydrophobicity and an ortho substituent to the hydroxyl,
which narrows the candidate set, but no natural phenol has been shown to be a
better substrate than PCP.

The para-specificity rule is firmer than I had it: a near-identical
Sphingomonas UG30 ortholog acts on p-nitrophenol, p-nitrocatechol,
2,4-dinitrophenol and 4,6-dinitrocresol, and not on 2,6-DNP or on o- or
m-nitrophenol
[PMID:10907421 "2,6-DNP, o- or m-nitrophenol, picric acid, or the herbicide dinoseb were not metabolized."].
Note this is the UG30 ortholog expressed in E. coli, not this accession.

## Structural analysis: a clean negative

The OpenScientist run attempted the pocket measurement and could not do it,
which is worth recording because it is the kind of negative that otherwise
gets quietly omitted. The AlphaFold model (AF-P42535-F1, **v6** -- the v4 URL
is retired) is good quality, mean pLDDT 91.5 with the FAD motifs above 97, but
it contains **no FAD and no substrate**. The nearest experimental structure,
p-hydroxybenzoate hydroxylase (1PBE), is only 20% identical, so transferring
the flavin and substrate positions by superposition collapsed to a degenerate
three-atom fit. Pocket volume and the substrate-to-C4a-hydroxyflavin distance
were therefore not measured, and the run's candidate ranking is an explicitly
declared SAR heuristic rather than docking.

Consequence for the project: the structural route to an ancestral substrate is
blocked for this enzyme until there is a co-structure with FAD and a bound
phenol, or a much closer experimental homologue. The uncoupling explanation
(bulky 3/4/5 substituents raise uncoupling, an ortho-chlorine lowers it, and
PCP is fully substituted) remains an SAR argument, not a measured geometry.
