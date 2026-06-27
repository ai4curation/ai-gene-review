# TOM22 (yeast) — review notes

## Trigger

This review was created to address upstream issue
[geneontology/go-annotation#6466](https://github.com/geneontology/go-annotation/issues/6466),
"PAINT issue: PTN004364609 GO:0008320 | transmembrane protein transporter
activity for Tom40", which states:

> tom40 is the channel, we don't know the MF of tom22

The PANTHER family `PTN004364609` IBA propagation reaches yeast Tom22 via
`SGD:S000005075`. The upstream curator's concern is whether GO:0008320
"transmembrane protein transporter activity" should propagate to Tom22 at all,
since Tom40 is the conducting pore.

## Decision

Retain both GO:0008320 annotations on yeast Tom22 with the `contributes_to`
qualifier:

1. `contributes_to GO:0008320` — IBA from PTN004364609 (GO_REF:0000033) — ACCEPT.
2. `contributes_to GO:0008320` — IMP from PMID:10519552 (SGD assignment) — ACCEPT.

Reasoning:

- The `contributes_to` qualifier in GO semantics encodes exactly the case the
  upstream curator is concerned about: a subunit that does not independently
  perform the MF but is required for the activity of the complex that does.
  Tom22 fits that pattern — it is a receptor/scaffold for the TOM complex, the
  complex as a whole performs transmembrane protein transport, and Tom40 is the
  conducting pore.
- The IBA is not the only source of this annotation. SGD already has an
  experimental **IMP** annotation with `contributes_to` from PMID:10519552
  (van Wilpe et al. 1999, "Tom22 is a multifunctional organizer of the
  mitochondrial preprotein translocase", Nature). Per CLAUDE.md curation
  guidance, an experimental annotation by a real curator should not be removed
  on the basis of an abstract-only read.
- PMID:10519552 establishes that "the translocase dissociates into core
  complexes ... but lacks a tight control of channel gating" in the absence of
  Tom22, i.e. Tom22 is required for the activity of the TOM transmembrane
  protein translocase even though Tom40 is the pore.
- The human ortholog review (`genes/human/TOMM22/TOMM22-ai-review.yaml`) reaches
  the same conclusion: ACCEPT `contributes_to GO:0008320` rather than remove.

The biologically appropriate response to the upstream concern is to keep
`contributes_to` on Tom22 and reserve `enables GO:0008320` for Tom40.

## Other key calls

- All `enables GO:0005515 protein binding` IPIs — MARK_AS_OVER_ANNOTATED. Per
  CLAUDE.md guidance, generic `protein binding` is uninformative; the TOM and
  TOM-SAM complex membership annotations capture the same information with more
  specificity.
- `GO:0006886 intracellular protein transport` IEA — MARK_AS_OVER_ANNOTATED.
  Generic; specific TOM-mediated import BPs are already present.
- `GO:0005739 mitochondrion` HDA × 2 — MARK_AS_OVER_ANNOTATED. Parent of the
  more specific GO:0005741 mitochondrial outer membrane annotations that are
  also present.
- All `GO:0005742 mitochondrial outer membrane translocase complex`,
  `GO:0005741 mitochondrial outer membrane`, and `GO:0045040 protein insertion
  into mitochondrial outer membrane` annotations — ACCEPT.
- `GO:0030150 protein import into mitochondrial matrix` IBA/IEA/IMP — ACCEPT
  with the understanding that matrix import is one of several TOM-mediated
  routes through Tom22; the matrix term is well-supported by the experimental
  IMPs in tom22Δ.

## Data provenance

- Cached publications used (verbatim supporting_text):
  PMID:9774667, PMID:10519552, PMID:11276259, PMID:12628251.
- Cross-reference: `genes/human/TOMM22/TOMM22-ai-review.yaml` (ortholog review)
  and `genes/human/TOMM22/TOMM22-deep-research-falcon.md` (used for orthologue
  context; quoted verbatim).
- Deep research providers (falcon, perplexity-lite) returned no result for
  yeast TOM22 due to missing API keys. Per CLAUDE.md, no
  `*-deep-research-{provider}.md` file was authored.

## Open questions for the upstream curator

- Should the PTN004364609 IBA for GO:0008320 be left in place with
  `contributes_to` on all non-Tom40 subunits (the conservative interpretation
  consistent with the SGD IMP and the human TOMM22 review), or only on
  receptors that have direct experimental support? If the latter, Tom22 should
  still keep the term because PMID:10519552 is a direct IMP.
- For the related `GO:0030943 mitochondrion targeting sequence binding`
  proposed obsoletion (go-annotation#6437 → go-ontology#32108), once the NTR
  replacement term is minted, Tom22 will need a MODIFY pass on the
  `core_functions.molecular_function` slot.
