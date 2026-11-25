# mgr2 manual deep research

`just deep-research-falcon SCHPO mgr2 --fallback perplexity-lite` failed
because the Falcon and Perplexity providers were unavailable in this runtime.
`just mod-description-deep-research SCHPO mgr2` skipped because no MOD
description provider is configured for `SCHPO`. `just paint-losses SCHPO mgr2`
reported no IRD or IKR loss on the P79082 lineage.

## Summary

S. pombe mgr2 (SPBC27.06c; UniProt P79082) encodes a small conserved
Mgr2/Romo1-family membrane protein. The S. pombe UniProt record predicts two
transmembrane helices, and PANTHER places S. pombe mgr2, budding-yeast MGR2,
and human ROMO1 together in `PTHR28525:SF1`.

The PAINT extract for `PTHR28525` contains three positive IBD rows at
`PTN002003652`: `GO:0005744` TIM23 mitochondrial import inner membrane
translocase complex, `GO:0030150` protein import into mitochondrial matrix, and
`GO:0045039` protein insertion into mitochondrial inner membrane. Searches for
`mgr2`, `SPBC27.06c`, `P79082`, and fission-yeast Mgr2/Romo1/TIM23 literature
found no direct S. pombe paper that characterizes an elemental molecular
function for Mgr2.

Budding-yeast Mgr2 is a TIM23 complex subunit. Gebert et al. identified Mgr2 by
affinity purification of the Tim21-containing presequence translocase, showed
that it copurifies with Tim23 and Tim21, and showed that mgr2 deletion disrupts
assembly of the Tim21-containing TIM23SORT state and efficient TOM-TIM23
coupling (PMID:22613836).

The insertion row is supported by the lateral sorting mechanism. Ieva et al.
showed that Mgr2 contacts preproteins in transit, that Mgr2 abundance affects
the timing of preprotein release into the mitochondrial inner membrane, and that
Mgr2-deficient mitochondria mis-sort precursors with defective stop-transfer
signals into the inner membrane (PMID:25454944). Matta et al. then found that
the first transmembrane region of Mgr2 is needed for Tim23 and Tim21
association, the second transmembrane region helps bridge respiratory complexes
to the TIM23 complex through Tim21, and both transmembrane regions are required
for lateral sorting into the inner membrane (PMID:32186971).

Human ROMO1 supports conservation of the Mgr2/Romo1 TIM23 role outside fungi.
Richter et al. identified ROMO1 as a human TIM23 constituent and showed that it
participates in TIM21 dynamics and the selective import of YME1L
(PMID:30598479). The human specialization does not justify adding a
S. pombe-specific YME1L or OPA1/Mgm1 processing annotation, but it supports the
PANTHER placement of TIM23-complex membership and inner-membrane insertion at
the Mgr2/Romo1 family node.

The PomBase HDA row from Matsuyama et al. reports cytoplasm for an S. pombe
C-terminal YFP fusion (PMID:16823372). That conflicts with the two predicted
transmembrane helices and the conserved TIM23-complex role, but the cached
paper is abstract-only and does not show the individual mgr2 image. The row is
therefore undecided pending image and tag-compatibility review.

## Annotation consequences

- Accept all three PAINT IBA rows. `GO:0005744`, `GO:0030150`, and
  `GO:0045039` are all placed at `PTN002003652` in PTHR28525 and agree with the
  budding-yeast Mgr2 mechanism.
- Accept the PomBase IC row to `GO:7770060` because TIM23-complex membership
  and the Mgr2 lateral gatekeeper mechanism both support the specific
  TOM-TIM23-SORT insertion process.
- Treat `GO:0016020` membrane as correct but too generic; S. pombe Mgr2 should
  be placed at the mitochondrial inner membrane.
- Accept the MF ND root row. Current GO annotations describe where Mgr2 acts and
  which import processes it contributes to, but no elemental MF term captures
  its substrate-gate or assembly role.
- Mark the Matsuyama et al. cytoplasm HDA row undecided until the original
  image can be checked.

## GO-CAM 69729a3800007453 consistency

The model represents mgr2 as enabling the root `GO:0003674` molecular function
in the mitochondrial inner membrane during `GO:0030150` protein import into the
mitochondrial matrix. The gene review is consistent with that representation:
Mgr2 is a TIM23 inner-membrane subunit with no more specific GO molecular
function currently available, and its conserved gatekeeper activity contributes
to both matrix-destined TIM23 import and TOM-TIM23-SORT-mediated inner-membrane
insertion.
