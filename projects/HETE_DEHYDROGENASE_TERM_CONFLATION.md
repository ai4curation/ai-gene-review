---
title: "5(S)-HETE Dehydrogenase Activity (GO:0097265) — Two Reactions Conflated in One Term"
maturity: SCOPING
tags: [OBSOLETION]
species: [human]
genes: [CYP4F3]
---

# 5(S)-HETE Dehydrogenase Activity (GO:0097265) — Two Reactions Conflated in One Term

**Bottom line:** `GO:0097265 "5(S)-hydroxyeicosatetraenoic acid dehydrogenase
activity"` currently describes two different enzymes at once. Its **name,
synonyms, `is_a` placement and defining paper** all specify a microsomal
NADP⁺-dependent dehydrogenase that oxidises 5(S)-HETE to 5-oxo-ETE. Its
**definition formula and RHEA cross-reference** specify something else entirely:
an O₂-consuming, P450-reductase-dependent ω-hydroxylation of 5-HETE to
5,20-dihydroxy-ETE. The term's own GO history dates the split precisely — on
**2026-04-12** the original dehydrogenase definition was deleted, the
ω-hydroxylation formula was added, and `RHEA:48656` was attached, while the name,
the three dehydrogenase synonyms and the parent class were left untouched. The
recommended fix is therefore **repair, not obsoletion**: revert the definition,
drop the RHEA xref, and re-point `RHEA:48656` in `rhea2go` to `GO:0102033`. Only
two annotations exist and both are IEA from that mapping, so nothing
experimental is at risk.

We found this while reviewing CYP4F3, which carries the term.

## The two readings

| | Name / synonyms / parent / PMID:1326548 | Definition formula / RHEA:48656 |
|---|---|---|
| Enzyme | 5(S)-hydroxyeicosanoid dehydrogenase (5-HEDH) | a CYP4F ω-hydroxylase |
| Reaction | 5-HETE + NADP⁺ = 5-oxo-ETE + NADPH + H⁺ | 5-HETE + O₂ + reduced CPR = 5,20-dihydroxy-ETE + oxidised CPR + H₂O + H⁺ |
| Chemistry | oxidation of an existing 5-hydroxyl | insertion of a new hydroxyl at C20 |
| Cofactor | NADP⁺ as acceptor | O₂ + NADPH via cytochrome P450 reductase |
| Product | 5-oxo-ETE | 5,20-diHETE |

The definition even contains the contradiction in a single sentence: it writes
the product as "5,20-dihydroxy-(6E,8Z,11Z,14Z)-eicosatetraenoate **(5-oxo-ETE)**",
gluing the old product name onto the new formula. 5,20-diHETE and 5-oxo-ETE are
different compounds made by different enzymes.

The placement follows the dehydrogenase reading. The term's `is_a` path is
`GO:0016616` (oxidoreductase activity, acting on the CH-OH group of donors, **NAD
or NADP as acceptor**) → `GO:0016614` → `GO:0016491`. An O₂-consuming
monooxygenation does not belong under a CH-OH/NAD(P)-acceptor parent; the CYP4F3
activity terms all sit under `GO:0004497` / `GO:0016712` instead.

## The 2026-04-12 edit

QuickGO's term history (GO release `releases/2026-09-27`) records the change that
created the conflation, all on one date:

| Date | Action | Field | Content |
|---|---|---|---|
| 2026-04-12 | Deleted | DEFINITION | `Catalysis of the reaction: 5-HETE + NADP+ = 5-oxo-ETE + NADPH + H+.` |
| 2026-04-12 | Added | DEFINITION | `…5-HETE + reduced [NADPH-hemoprotein reductase] + O2 = 5,20-dihydroxy-…-eicosatetraenoate (5-oxo-ETE)…` |
| 2026-04-12 | Added | XREF | `RHEA:48656` |

Nothing else changed: the label, the synonyms `5-HETE dehydrogenase activity`,
`5-hydroxy-eicosatetraenoic acid dehydrogenase activity` and
`5(S)-HETE dehydrogenase activity`, and the parentage all still describe the
dehydrogenase. Earlier history shows the term is long-standing — a Reactome xref
was removed from it in 2019 — and the 2022-09-01 entry shows the pre-existing
definition being reformatted while keeping the same NADP⁺ chemistry.

So this is not a term that was always wrong. It was a sound term that a
definition swap repurposed without renaming or re-parenting it.

## The original term was well grounded

`PMID:1326548` — one of the term's own definitional xrefs — is the
characterisation of exactly this dehydrogenase. According to PubMed (Powell,
Gravelle & Gravel, *J Biol Chem* 1992;267:19233-41):

> The 5-hydroxyeicosanoid dehydrogenase activity is localized in the microsomal
> fraction and requires NADP+ as a cofactor.

> The preferred substrate for this enzyme is
> 5(S)-hydroxy-6,8,11,14-eicosatetraenoic acid (5(S)-HETE) (Km, 0.2 microM),
> which is converted to 5-oxo-6,8,11,14-eicosatetraenoic acid.

The paper also establishes the enzyme's positional and stereochemical
specificity — little or no oxidation at the 8-, 9-, 11-, 12- or 15-positions,
5(R)-HETE a poor substrate, and no activity on the 5-hydroxyl of LTB4 itself
because of its 6-*cis* geometry. 5-oxo-ETE is a potent neutrophil
chemoattractant, so the activity is biologically substantive and worth a term.

## What the term is annotated to, and why

Exactly **two** annotations exist, across all taxa, and both arrive through the
xref added in that 2026-04-12 edit:

| Gene | Taxon | Evidence | Reference |
|---|---|---|---|
| CYP4F3 | 9606 | IEA | `GO_REF:0000116` (rhea2go) |
| Cyp4f1 | 10116 | IEA | `GO_REF:0000116` (rhea2go) |

Both are CYP4F ω-hydroxylases, so both match the *definition* and neither
matches the *name*. The RHEA xref is what made `rhea2go` map `RHEA:48656` onto
this term, which is the whole source of the annotation set. **No experimental
annotation would be affected by fixing the term.**

CYP4F3 genuinely performs the reaction in the definition: the purified
neutrophil enzyme ω-hydroxylates 5-HETE
([PMID:9675028](https://pubmed.ncbi.nlm.nih.gov/9675028/) — "5-HETE and
12-HETE … were efficiently omega-hydroxylated"). That paper is also one of the
term's xrefs, which is presumably how the two readings came to share a term.

## Recommendation

**Repair the term rather than obsolete it.** Obsoletion was our first instinct,
on the GO:0052869 / GO:0018777 precedent that GO does not keep a term per
ω-hydroxylase substrate. That precedent is sound but applies to the *definition*
reading only — and the name, parentage and PMID:1326548 all point at a real,
distinct enzyme that deserves to keep its term.

1. **Revert the definition** to the NADP⁺ dehydrogenase reaction
   (`5-HETE + NADP+ = 5-oxo-ETE + NADPH + H+`), restoring agreement with the
   label, the three synonyms, the `GO:0016616` parent and PMID:1326548.
2. **Remove the `RHEA:48656` xref** and the `PMID:9675028` xref, which belong to
   the ω-hydroxylation reading.
3. **Re-point `RHEA:48656` in `rhea2go` to `GO:0102033`**
   (long-chain fatty acid omega-hydroxylase activity), consistent with how GO
   handles per-substrate ω-hydroxylations after obsoleting `GO:0052869`
   (arachidonate) and `GO:0018777`. The two IEA annotations then land on a term
   that matches both their chemistry and their enzymes.
4. **Consider re-parenting** under a 5-HEDH-appropriate NADP⁺ oxidoreductase
   class if `GO:0016616` proves too general once the definition is restored.

If GO prefers the opposite resolution — keep the ω-hydroxylation reading and
obsolete the dehydrogenase sense — then `5-oxo-ETE` biology loses its only
activity term, since GO has **no** other term for 5-hydroxyeicosanoid
dehydrogenase (searches for "5-oxo-ETE", "hydroxyeicosanoid dehydrogenase" and
"oxoeicosanoid" return nothing relevant; only `GO:0050646 5-oxo-…-icosatetraenoic
acid binding` exists). A new term would then be needed. We are **not** proposing
one here: no gene in this repository has been reviewed for that activity, and the
enzyme's gene identity is not something we have established.

## Status

- **Started**: 2026-10-29
- **Maturity**: SCOPING — defect characterised and evidenced; not yet submitted
  to GO.
- **Checked live**: term name, definition, synonyms, `is_a` ancestry, xrefs and
  full edit history from QuickGO (GO release `releases/2026-09-27`);
  `RHEA:48656` equation from the RHEA REST API; the two annotations and their
  evidence codes from the QuickGO annotation API.
- **Found via**: the CYP4F3 gene review, which handles its own row as a MODIFY
  to `GO:0102033` and raises the term defect as a `suggested_questions` entry.
- **Related**: [CYTOCHROME_P450](CYTOCHROME_P450.md) ·
  [RHEA](RHEA.md) — the `rhea2go` mapping that produced both annotations is the
  pipeline that project audits.
