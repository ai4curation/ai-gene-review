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

## 2026-09-29 IBA refresh

PTHR12504 current PAINT still places these IBDs at `PTN004364609`:

- `GO:0005742 mitochondrial outer membrane translocase complex`, seeded by
  `FB:FBgn0035473|RGD:1303260|SGD:S000005075|UniProtKB:Q9NS69`.
- `GO:0030150 protein import into mitochondrial matrix`, seeded by
  `RGD:1303260|SGD:S000005075|UniProtKB:Q9NS69`.

The GOA `contributes_to GO:0008320` row still points to `PTN004364609` with
`SGD:S000005075`, but the current `PTHR12504-paint.tsv` snapshot has no
GO:0008320 row at that node. Human TOMM22 carries the same IBA source and should
be rechecked in a follow-up pass. I recorded `SOURCE_STALE_OR_MISSING` for the PTN
and set the stale PAINT row to REMOVE while preserving the biological call:
yeast TOM22 has a direct SGD IMP to `contributes_to GO:0008320`, and the
`contributes_to` qualifier remains the right semantics for a receptor/scaffold
subunit that helps the TOM complex transport proteins without itself being the
Tom40 pore.

A 2024-2026 PubMed check found recent mitochondrial-import papers that mention
Tom22, including Mishra et al.'s yeast import-clogging work in its preprint and
published forms [PMID:41279142 "Proximity-dependent biotin identification (BioID)
suggested that Mfb1 interacts with several mitochondrial surface proteins including
Tom22, a component of the TOM complex."; PMID:41457021 "Proximity-dependent biotin
identification (BioID) suggested that Mfb1 interacts with several mitochondrial
surface proteins including Tom22, a component of the TOM complex."] and a
reconstituted-human-TOM PINK1 study [PMID:38848361 "co-expression of human PINK1
and all seven TOM subunits in Saccharomyces cerevisiae is sufficient for PINK1
activation"]. None changed the core yeast TOM22 signal-receptor, TOM-scaffold, or
`contributes_to` transporter-activity calls.

## Decision

Remove the stale GO:0008320 PAINT propagation, but retain GO:0008320 on yeast
Tom22 with the `contributes_to` qualifier through direct SGD support:

1. `contributes_to GO:0008320` - IBA from PTN004364609 (GO_REF:0000033) - REMOVE as stale in current PAINT.
2. `contributes_to GO:0008320` — IMP from PMID:10519552 (SGD assignment) — ACCEPT.

Reasoning:

- The `contributes_to` qualifier in GO semantics encodes exactly the case the
  upstream curator is concerned about: a subunit that does not independently
  perform the MF but is required for the activity of the complex that does.
  Tom22 fits that pattern — it is a receptor/scaffold for the TOM complex, the
  complex as a whole performs transmembrane protein transport, and Tom40 is the
  conducting pore.
- The stale IBA is not the only source of this annotation. SGD already has an
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
  the same biological conclusion: Tom22 orthologs contribute to GO:0008320 as
  TOM receptor/scaffold subunits even though Tom40 is the pore.

The biologically appropriate response to the upstream concern is to keep direct
`contributes_to` support on Tom22 and reserve `enables GO:0008320` for Tom40.

## Other key calls

- All `enables GO:0005515 protein binding` IPIs — REMOVE. Per project guidance,
  generic `protein binding` is uninformative; the TOM and TOM-SAM complex
  membership annotations capture the same information with more specificity.
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
- Recent literature checked:
  PMID:41457021, PMID:41279142, PMID:38848361.
- Cross-reference: `genes/human/TOMM22/TOMM22-ai-review.yaml` (ortholog review)
  and `genes/human/TOMM22/TOMM22-deep-research-falcon.md` (used for orthologue
  context; quoted verbatim).
- Deep research providers (falcon, perplexity-lite) returned no result for
  yeast TOM22 due to missing API keys. Per CLAUDE.md, no
  `*-deep-research-{provider}.md` file was authored.

## Open questions for the upstream curator

- If PAINT restores GO:0008320 at a Tom22 ancestral node, should the propagation
  use `contributes_to` on all non-Tom40 subunits or only on receptors that have
  direct experimental support? If the latter, yeast Tom22 should still keep the
  term because PMID:10519552 is a direct IMP.
- For the related `GO:0030943 mitochondrion targeting sequence binding`
  proposed obsoletion (go-annotation#6437 → go-ontology#32108), once the NTR
  replacement term is minted, Tom22 will need a MODIFY pass on the
  `core_functions.molecular_function` slot.
