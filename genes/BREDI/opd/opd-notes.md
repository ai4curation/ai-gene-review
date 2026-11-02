# Notes: opd (phosphotriesterase / OPH, Brevundimonas diminuta)

Part of the category-4 counter-example set in
`projects/NONPHYSIOLOGICAL_REACTIONS.md`. This is the extreme case at the
opposite end of the spectrum from benzil reductase.

## Why it anchors the set

Every known substrate is synthetic. UniProt states it plainly: "All of the
phosphate triesters found to be substrates are synthetic compounds. The
identity of any naturally occurring substrate for the enzyme is unknown." And
yet the enzyme hydrolyses paraoxon "at a rate approaching the diffusion limit
and thus appears to be optimally evolved for utilizing this synthetic
substrate".

Near-diffusion-limited catalysis on a compound that has existed for under a
century is the strongest possible evidence that an activity is selected rather
than incidental. If substrate provenance were the test for a non-physiological
annotation, this enzyme would be the first casualty and the test would be
obviously wrong.

Specificity is also narrow in the informative direction: no activity on
phosphate mono- or diesters, and none as an esterase or protease. A promiscuous
hydrolase would be a weaker case.

## Progenitor identified

Homologues annotated as "putative PTEs" are actually proficient lactonases
(PTE-like lactonases, PLLs) acting on quorum-sensing N-acyl homoserine
lactones, with weak phosphotriesterase side activity
[PMID:17105187 "phosphotriesterase (PTE), an enzyme thought to have evolved for the purpose of"].
PTE is argued to have evolved from a PLL member by exploiting latent
promiscuous paraoxonase activity. This makes opd one of the few members of the
set with a named ancestral function, which is why it is worth keeping in the
project as a reference point.

## Annotation calls

- GO:0004063 ACCEPT (both the IDA and the EC-mapped IEA). Correct specific term.
- GO:0016788 (ester-bond hydrolase, from InterPro) MARK_AS_OVER_ANNOTATED.
  Formally an ancestor, but flagged rather than silently accepted because the
  broad term invites reading opd as a general esterase, which it is not.
- GO:0008270 zinc ion binding ACCEPT; binuclear Zn centre, well established.
- Two caveats recorded in the review that no action in the vocabulary
  expresses: the CACAO annotation uses `part_of GO:0005886` where `located_in`
  fits a peripheral membrane protein (the parallel IEA row uses `located_in`),
  and the localization experiment was done with opd expressed in *Pseudomonas*
  sp. Ind01, not in *B. diminuta*
  [PMID:23574004 "The heterologously expressed OPH, which is a substrate of twin arginine transport (Tat) pathway, successfully targeted to the membrane of Pseudomonas sp. Ind01."].

## Reference quality note

PMID:23574004 is the source of both IDA rows but its purpose is constructing a
biocatalyst. Marked MEDIUM relevance / VERIFIED. For this gene the biocatalysis
literature and the physiological literature are largely the same literature,
which is a reminder that journal provenance alone is a weak project signal.
