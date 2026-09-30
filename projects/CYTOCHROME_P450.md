---
title: "Cytochrome P450 Project: GO molecular function across the human superfamily"
maturity: IN_PROGRESS
tags: [PIPELINE]
species: [human]
genes: [CYP4F3, CYP4F2, CYP4A11, CYP4F22, CYP3A4, CYP1B1, CYP2J2, CYP2E1, CYP11B2, CYP19A1, CYP24A1, CYP26C1, CYP51A1, CYP27A1]
---

# Cytochrome P450 Project

**Bottom line:** the 60 reviewed human cytochrome P450 entries carry **556
catalytic-activity lines, 528 of them experimental**, covering **297 distinct
reactions** — and GO represents that with **84 substrate-naming molecular-function
terms**, of which **201 of the 297 reactions (68%) reach no GO term at all**. The
annotation that *does* exist is sound: 48 of the 56 CYPs with a substrate-naming
term have experimental evidence for it, only 4 rest on IBA, and the
closure-filtered propagation gap is **zero**. So this family's problem is neither
bad annotation nor failed propagation — it is **resolution**. The sharpest
evidence is an asymmetry inside one protein: CYP4F3 has all three steps of
leukotriene-B4 ω-oxidation as GO terms, each mapped to its own RHEA reaction,
while the chemically identical C22/C26 fatty-acid ω-oxidation cascade on the same
protein has a term for step 1 and none for steps 2 and 3. GO is willing to
represent these reactions; nobody has requested the terms.

We did this because the P450s are where every general claim about enzyme
annotation quality gets tested: they are the most substrate-promiscuous family in
the human proteome, 21 of the 60 are disease genes, and the repository's own
coverage of them is badly skewed — **all 13 CYP reviews here are
endogenous-substrate enzymes, and none of the drug-metabolising CYP1/2/3/4
enzymes has been reviewed at all.**

## Overview

This project audits the GO molecular-function representation of the human
cytochrome P450 superfamily as a whole, rather than one enzyme at a time. It
grew out of the family scan in the [RHEA](RHEA.md) project
([RHEA-PROMISCUOUS-FAMILIES.md](RHEA/RHEA-PROMISCUOUS-FAMILIES.md)), which found
CYP450s to be the extreme case of reaction-to-term drop-out; this project asks
what that means for the annotations themselves and turns it into a curation
worklist.

Everything is computed live by [`cyp_go_audit.py`](CYTOCHROME_P450/cyp_go_audit.py)
against UniProtKB, QuickGO, `rhea2go` and `ec2go`. Per-gene, per-reaction and
per-chemistry tables are in [`data/`](CYTOCHROME_P450/data/). No result is
hardcoded.

## How "informative" is decided

Calling a term "generic" by eye is where an audit like this usually goes wrong,
so the cut is derived from the data. For every catalytic MF term annotated
anywhere in the family, count how many *other* annotated terms are its `is_a`
descendants. The counts break sharply:

| Descendants within the family | Term |
|---:|---|
| 81 | `GO:0016491` oxidoreductase activity |
| 70 | `GO:0004497` monooxygenase activity |
| 61 | `GO:0016705` oxidoreductase activity, acting on paired donors… |
| 29 | `GO:0016712` …reduced flavin or flavoprotein as one donor… |
| 24 | `GO:0008395` steroid hydroxylase activity |
| **6** | `GO:0016713` …reduced iron-sulfur protein as one donor… |
| 5 | `GO:0008391` arachidonate monooxygenase activity |
| ≤4 | *(everything else — 14 terms, each with one or two children)* |

The gap between 24 and 6 separates five family-wide **hub** terms from the tail
of real activities that merely have a child or two. Terms at or above 20
descendants are treated as hubs (`--hub-threshold`, and the whole distribution is
emitted so the choice can be checked). Each CYP then falls in one of three tiers:

- **substrate-resolved** — carries a non-hub activity term that is also maximally
  specific within the family;
- **partially-resolved** — carries a non-hub term, but the family resolves it
  further on other members;
- **unresolved** — every catalytic term it carries is a hub, so GO does not say
  which reaction it catalyses.

## Results

| | Count |
|---|---:|
| Reviewed human CYP entries | 60 |
| …with at least one curated reaction | 57 |
| Catalytic-activity lines (RHEA) | 556 |
| …experimental (`ECO:0000269`) | **528 (95%)** |
| Distinct reactions | 297 |
| …reaching a GO term via `rhea2go` | 96 |
| …**with no GO target** | **201 (68%)** |
| …unmapped *and* carrying no EC number | 192 |
| Distinct MF terms annotated to the family | 107 |
| …catalytic | 89 |
| …substrate-naming (non-hub) | 84 |
| Tier: substrate-resolved / partially / unresolved | **52 / 4 / 4** |
| Substrate-naming term backed by experiment / IBA / other | **48 / 4 / 4** |
| Closure-filtered propagation gaps | **0** |
| Genes with ≥1 unmapped reaction | 45 of 60 |
| Disease genes in the family | 21 |

### The annotation is curated, not inherited

The result that constrains everything else: of the 56 CYPs carrying a
substrate-naming activity term, **48 have experimental evidence for it** and only
4 depend on IBA. Nor is anything failing to propagate — applying `is_a` closure,
**no entry lacks a term that one of its mapped reactions would supply**. This
family is not a propagation-failure or over-propagation story, and the review
actions one reaches for in those cases (`REMOVE`, `MARK_AS_OVER_ANNOTATED`) are
mostly not what its annotations need.

What it lacks is resolution. 297 experimentally curated reactions are represented
by 84 substrate-naming terms, a median of **3 per enzyme**, and 184 of the
unmapped reactions carry experimental evidence. The information exists in
UniProt and stops at GO's door.

### The cascade asymmetry: CYP4F3 against itself

The single clearest gap in the family, and the one that rules out "GO does not
model these reactions" as an explanation.

Fatty-acid ω-oxidation is three sequential oxidations by the same P450:
ω-methyl → ω-hydroxy → ω-oxo → dicarboxylate. **For leukotriene B4, GO has all
three steps, and `rhea2go` maps all three:**

| Step | Reaction | GO term | Mapped? |
|---|---|---|---|
| 1 | RHEA:22176 LTB4 → 20-OH-LTB4 | `GO:0050051` leukotriene-B4 20-monooxygenase activity | ✅ |
| 2 | RHEA:48668 20-OH-LTB4 → 20-oxo-LTB4 | `GO:0097258` 20-hydroxy-leukotriene B4 omega oxidase activity | ✅ |
| 3 | RHEA:48672 20-oxo-LTB4 → 20-COOH-LTB4 | `GO:0097259` 20-aldehyde-leukotriene B4 20-monooxygenase activity | ✅ |

**For the C22 and C26 fatty-acid route — on the same enzymes, all experimental —
only step 1 has a term:**

| Step | Reaction | Enzymes | GO term |
|---|---|---|---|
| 1 | RHEA:48664 etc. ω-hydroxylation | CYP4F2, CYP4F3, CYP4F11 | `GO:0102033` / `GO:0140692` ✅ |
| 2 | RHEA:39055 (C22), RHEA:39059 (C26) → ω-oxo | CYP4A11, CYP4F2, CYP4F3 | **none** |
| 3 | RHEA:39043 (C22), RHEA:39047 (C26) → dicarboxylate | CYP4A11, CYP4F2, CYP4F3 | **none** |

CYP4F3 carries both cascades. The LTB4 one is fully represented in GO; the
dicarboxylic-acid one, which is the route to the substrates of peroxisomal
β-oxidation and is implicated in ω-oxidation induction in fatty-acid oxidation
disorders, stops after the first step. `GO:0010430 fatty acid omega-oxidation`
exists as a *biological process*, so the pathway is known to GO — but a BP term
cannot receive a `rhea2go` mapping, which needs a molecular function.

The `GO:0097258` / `GO:0097259` pair is therefore an in-family **template**: two
new terms, built on a precedent from the same proteins, would close steps 2 and 3
for the whole very-long-chain route. Added as batch 8 of the RHEA mapping set
(below).

Zoomed out, the same shape recurs: **all 17 oxo-forming reactions in the family
are unmapped (100%)**, across CYP24A1's vitamin-D C24 oxidation chain, CYP19A1's
19-oxo aromatase intermediate, CYP51A1's 32-oxolanosterol step, CYP26C1's
4-oxoretinoate steps and CYP11B2's 18-oxocortisol step. Where GO represents a
cascade at all it tends to use one *net-reaction* term — `GO:0070330 aromatase
activity` and `GO:0008398 sterol 14-demethylase activity` are both defined with
3 O₂ and 3 reductase equivalents, releasing formate — so RHEA's partial reactions
have nothing to land on. The LTB4 trio proves the alternative is acceptable to GO.

### Unmapped chemistry, by class

| Chemistry | Substrate class | Reactions | Unmapped | % |
|---|---|---:|---:|---:|
| hydroxylation | steroid / sterol | 79 | 54 | 68% |
| hydroxylation | eicosanoid / PUFA | 36 | 28 | 78% |
| epoxidation | eicosanoid / PUFA | 32 | 18 | 56% |
| hydroxylation | other fatty acid | 28 | 18 | 64% |
| oxo-formation | steroid / sterol | 10 | 10 | **100%** |
| oxo-formation | other | 7 | 7 | **100%** |
| epoxidation | other fatty acid | 5 | 5 | **100%** |
| aromatization (formate-releasing) | steroid / sterol | 10 | 5 | 50% |

Chemistry and substrate classes are assigned by pattern-matching the reaction
equation — a summary aid, with the per-reaction assignment emitted in
[`data/cyp-reactions.tsv`](CYTOCHROME_P450/data/cyp-reactions.tsv) so it can be
checked. The three 100% rows are the cascade-step classes above.

### CYP4F22: the one enzyme GO does not describe

Four CYPs are **unresolved**, and three are explained: `CYP4Z2P` and `CYP2G1P`
are pseudogenes, and `CYP20A1` is a genuine orphan with no curated reaction, so
GO's silence is correct. That leaves one:

**CYP4F22 (Q6NT55)** carries two experimental ultra-long-chain fatty acid
ω-hydroxylation reactions, EC 1.14.14.177 (which has no `ec2go` line), and its
entire GO molecular function is `monooxygenase activity`, the
`oxidoreductase activity, acting on paired donors…` parents, `iron ion binding`,
`heme binding` and `protein binding`. Nothing in GO states what it does. It is
the gene mutated in **autosomal recessive congenital ichthyosis 5**, where the
ω-hydroxylation of ultra-long-chain fatty acids for acylceramide synthesis *is*
the disease mechanism. `GO:0140692 very long-chain fatty acid omega-hydroxylase
activity` is defined for chains longer than 22 carbons and covers both reactions
without a new term being needed — so this is a mapping gap, closed by batch 7 of
the RHEA set.

The four **partially-resolved** CYPs are a milder version: CYP26C1 and CYP2W1
have `retinoic acid 4-hydroxylase activity` by IDA, CYP2A7 and CYP2F1 have
`arachidonate epoxygenase activity`, in each case a term that other family
members resolve further.

### Repository coverage is skewed to endogenous metabolism

| | Reviewed here | Not reviewed |
|---|---:|---:|
| CYPs | 13 | 47 |
| Median curated reactions | 9 | 5 |
| Largest unmapped-reaction count | 14 (CYP27A1) | **35 (CYP4F3)** |

The 13 reviewed CYPs — CYP11A1, CYP11B1, CYP11B2, CYP17A1, CYP19A1, CYP21A2,
CYP27A1, CYP39A1, CYP46A1, CYP51A1, CYP7A1, CYP7B1, CYP8B1 — are, without
exception, **endogenous-substrate enzymes**: steroidogenesis, bile-acid
synthesis, sterol and vitamin-D metabolism. Not one of the
xenobiotic-metabolising CYP1, CYP2, CYP3 or CYP4 enzymes has a review, and those
are precisely the promiscuous ones carrying the largest unmapped reaction sets
(CYP4F3 35, CYP3A4 29, CYP4F2 21, CYP1A1 18).

This is a defensible historical accident — the endogenous CYPs arrive through
pathway projects — but it means the family's hardest annotation questions are all
in the unreviewed half.

## New GO term proposals

Consolidated from this audit and the RHEA family scan. All rows live in
[`rhea2go.sssom.yaml`](RHEA/rhea2go.sssom.yaml) and validate with
`just validate-rhea-mappings`.

| Proposed term | Reactions | Enzymes | Precedent / sibling |
|---|---|---|---|
| ω-hydroxy-very-long-chain fatty acid ω-oxidase activity | RHEA:39055, RHEA:39059 | CYP4A11, CYP4F2, CYP4F3 | `GO:0097258` (same step, LTB4) |
| ω-oxo-very-long-chain fatty acid ω-oxidase activity | RHEA:39043, RHEA:39047 | CYP4A11, CYP4F2, CYP4F3 | `GO:0097259` (same step, LTB4) |
| estrogen 4-hydroxylase activity | RHEA:47280, RHEA:47292 | CYP1B1 (+5 more) | `GO:0101021` (2-), `GO:0101020` (16α-) |
| eicosapentaenoate epoxygenase activity | RHEA:39779 (+3) | CYP2J2 (+6 more) | `GO:0008392` (arachidonate) |
| docosahexaenoate epoxygenase activity | RHEA:52120 (+5) | CYP2J2 (+6 more) | `GO:0071614` (linoleate) |
| 18-hydroxycorticosterone 18-oxidase activity | RHEA:50792 | CYP11B2 | `GO:0047783` (preceding step) |

And two **mapping**-only fixes, needing no new term: CYP4F22's two ULCFA
reactions onto `GO:0140692`, and the CYP2E1/CYP4F ω and ω-1 hydroxylation
instance reactions onto `GO:0102033` / `GO:0120319` (34 reviewed annotations).

## Curation Recommendations

1. **Do not read low reaction-to-term ratios as over-annotation.** Every review
   action that removes or downgrades an annotation is the wrong tool here: the
   existing terms are experimentally grounded and nothing is over-propagated. The
   actions this family needs are `NEW` (rarely, per the term proposals above) and
   mapping additions.
2. **Check for an in-family template before proposing a term.** The LTB4 trio
   settles the ω-oxidation proposals in a way that no argument from first
   principles could. Ask whether GO already represents this exact chemistry for a
   *different substrate on the same protein*.
3. **Distinguish the cascade-step gap from the per-substrate gap.** A missing
   term for an intermediate step of a multi-step transformation is a real gap
   with a precedent. A missing term for one more substrate of an activity GO
   already names is not — per
   [RHEA-PROMISCUOUS-FAMILIES.md](RHEA/RHEA-PROMISCUOUS-FAMILIES.md), GO
   obsoleted `GO:0018777` for exactly that reason.
4. **Review the xenobiotic CYPs.** The unreviewed half holds the promiscuity, the
   pharmacogenomics and the unmapped reactions.
5. **`unresolved` is a worklist, not a verdict.** Three of the four unresolved
   CYPs should stay that way (two pseudogenes and an orphan); the tier is useful
   precisely because it is small enough to adjudicate by hand.

## Follow-Up Targets

| Target | Rationale |
|---|---|
| Gene review: **CYP4F22** | The one CYP with curated reactions and no informative GO MF; disease mechanism is the reaction itself. |
| Gene review: **CYP4F3** and **CYP4F2** | Largest unmapped reaction sets; carry both sides of the cascade asymmetry, so the review can propose the two ω-oxidation terms in context. |
| Gene review: **CYP1B1** | Anchors the estrogen 4-hydroxylase proposal; glaucoma/ASGD6 disease gene. |
| Gene review: **CYP2J2** | Anchors the EPA/DHA epoxygenase proposals. |
| Submit the six new-term requests to GO | Each has a named sibling or precedent and a reviewed enzyme with experimental evidence. |
| Extend the tier audit to mouse and rat CYPs | Tests whether the resolution deficit is GO-wide or human-annotation-specific. |
| Cross-check against GO-CAM | Whether any CYP cascade is already modelled step-by-step in `gocams/`, which would supply further precedent. |

## Methods

`cyp_go_audit.py` fetches reviewed human CYP entries (UniProt family query),
their `CC CATALYTIC ACTIVITY` RHEA cross-references and evidence codes, their
GOA molecular-function rows from QuickGO with evidence and reference, and `is_a`
ancestor closures for every term involved. Hub/tier classification, provenance,
reaction coverage and the chemistry classification are computed from those
inputs. Review coverage is read from `genes/human/<GENE>/<GENE>-ai-review.yaml`.

```bash
cd projects/CYTOCHROME_P450
uv run python cyp_go_audit.py --out data
uv run python cyp_go_audit.py --out data --hub-threshold 25   # move the hub cut
```

Outputs: `data/cyp-summary.json`, `data/cyp-entries.tsv` (per gene, with tier,
provenance and review status), `data/cyp-reactions.tsv` (per reaction, with the
`rhea2go`/`ec2go` comparison and chemistry class), `data/cyp-chemistry.tsv`,
`data/cyp-propagation-gaps.tsv` (empty).

## Project Status

- **Started**: 2026-09-30
- **Maturity**: IN_PROGRESS — family-wide audit complete and reproducible; term
  proposals recorded in the RHEA SSSOM set; the exemplar gene reviews and the GO
  new-term requests are the open work.
- **Computed live**: 60 reviewed entries, 556 reaction annotations (528
  experimental), 297 distinct reactions, 96 mapped / 201 unmapped (192 without an
  EC), 107 MF terms (89 catalytic, 84 substrate-naming), tiers 52/4/4, provenance
  48 experimental / 4 IBA / 4 other, 0 closure-filtered propagation gaps, 13 of
  60 reviewed in this repository.
- **Related**: [RHEA](RHEA.md) ·
  [RHEA-PROMISCUOUS-FAMILIES.md](RHEA/RHEA-PROMISCUOUS-FAMILIES.md) ·
  [ENZYME_SPECIFICITY](ENZYME_SPECIFICITY.md)
