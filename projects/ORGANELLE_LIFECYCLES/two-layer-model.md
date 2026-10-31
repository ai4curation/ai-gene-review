---
title: "Two-layer model: steps need activities, activities need realizers"
---

# Two-layer model: steps need activities, activities need realizers

[Back to Organelle Lifecycle Modules](../ORGANELLE_LIFECYCLES.md)

**Bottom line:** a module used as a rule should make two different kinds of
claim, and the engine should keep them apart. A process step requires a
molecular function (MF); that requirement is close to binary. An MF is
carried out by one of several families, domains or complexes; that mapping is
open-world and gappy. Both are written as `variant_sets` and compile to an OR;
the engine now labels each gap by layer, so a genome that fails a rule says
which kind of gap it hit.

## The two layers

**Layer 1: process step → required activity.** "Presequence import across the
inner membrane" requires a presequence translocase channel activity. This is
close to definitional. Where lineages genuinely differ, the difference is a
deliberate biological claim: Saccharomyces oxidises NADH with single-subunit
dehydrogenases instead of complex I (a different MF, not a different family
for the same MF), and mitosomes have no respiration at all. These alternatives
are few, curated, and modelled as optional parts or route variants. Failing
this layer says "this organism does not do X".

**Layer 2: activity → realizer.** An MF is carried out by a family, a domain
or a complex, and the mapping is uncertain in four ways:

| Problem | Example in this project |
|---|---|
| Disjunctive: unrelated families carry the same MF | non-orthologous displacement |
| Under-matched: a divergent ortholog falls outside the selector | ATOM40 vs the Tom40 family is disputed |
| Over-matched: the selector also catches paralogs | every Hsp70 matches the mtHsp70 step; PTHR12763 also catches DNAJC15 |
| Incomplete: some realizers are unknown | any step with no characterised member in a lineage |

A realizer can itself be a conjunction (a complex of subunits), so in general
an MF step is satisfied by an OR of ANDs. Failing this layer usually says
"no known realizer was detected", which is a statement about our knowledge and
our detection as much as about the organism.

## Consequence for gap reports

| Layer that fails | What the gap means | Natural follow-up |
|---|---|---|
| 1 (step → MF) | the organism lacks the activity, or uses a route the module does not model | biological claim; check the route list |
| 2 (MF → realizer) | the activity is expected but no realizer was found | search for divergent homologs, unknown families, assembly gaps |

The engine's `GAP_HYPOTHESES` list already contains both kinds ("an
alternative route not represented in the module" is layer 1; "non-orthologous
/ unannotated enzyme fills this step" is layer 2), but it attaches the whole
list to every gap.

## Worked example: kinetoplastid import

Kinetoplastids (Trypanosoma, Leishmania) lack the separate TIM23 and TIM22
channels; their inner membrane uses a single translocase built around one
Tim17-family protein (TbTim17) plus lineage-specific subunits. (These
statements are from the general literature and have not yet been checked
against data in this repository.)

- **Modelled as a route variant (the original plan item):** "TIM23 + TIM22"
  OR "kinetoplastid single translocase". This puts the difference in layer 1,
  as though trypanosomes used a different import route.
- **Modelled in two layers:** the two activities (presequence translocase
  channel, carrier insertase) stay required; each gains a kinetoplastid
  realizer. The difference sits in layer 2, where it belongs: same activities,
  one protein carrying both.

The selector caution applies in either form. The added realizer must be the
kinetoplastid lineage of the Tim17 family, not the whole family; otherwise
every eukaryote, all of which have Tim17, satisfies the step and the rule
stops detecting loss of TIM23. Local PANTHER membership files cover only model
organisms, so the kinetoplastid placement must come from PANTHER's own
classification of the T. brucei and Leishmania proteins before any id is
written into the module.

## What the engine did, and what changed

Before this change, running the mitochondrion umbrella in
`ai_gene_review.module_logic` with TIM23 and TIM22 absent showed four
problems. Each is now addressed:

| Problem | Change |
|---|---|
| The gap was reported only at the umbrella stage (`protein_import`); the failing steps showed only when the import module was run on its own. | `gap_report` descends through failed steps, `module_ref` nodes and referenced modules, and returns each gap at its innermost failing element with its full path, e.g. `protein_import → mitochondrial_protein_import → tim23_translocation → mitochondrial_protein_import#tim23_channel`. |
| `gap_candidates` listed every atom under the failed step: 16 import symbols, 14 of them present. | `gap_candidates` lists only atoms that do not hold: `TIMM22`, `TIMM23`. |
| Atoms carried MF ids and gene identifiers but no family or domain selector, so a proteome oracle had nothing to scan for. | Atoms carry `family_ids` and `domain_ids` from the participant selector. |
| Variant-set `axis` is free text, and the engine kept only the set id and selection rule, so a gap could not be labelled by layer. | A variant set may declare `variant_kind: REALIZER` or `ROUTE`. When it is omitted, the compiler infers `REALIZER` if every variant carries the same single MF. Each gap is labelled `REALIZER`, `ROUTE` or `UNCLASSIFIED`, and `abduce` narrows its hypotheses for declared layers. |

Across the 448 variant sets in the 717 modules that do not use `module_ref`,
the compiler infers 165 as realizer choices. One, the acetoacetate activation
choice in `ketone_body_oxidation` (SCOT versus AACS, two different
activities), is declared `ROUTE`. The other 282 stay unclassified until a
curator declares them; their gaps get both layers' hypotheses, as before.

A step with a single listed carrier, like each step of the import module, is
reported `UNCLASSIFIED`. Its structure cannot tell an undetected carrier from
an unmodelled route: for a GTEx expression gap such as G6PC1 in intestinal
gluconeogenesis, "a route the module does not model" is the live explanation,
and "a divergent homolog went undetected" barely applies. Inferred labels
likewise keep both explanations, because inference from the modelled
alternatives says nothing about routes the module does not model. Only a
declared `variant_kind` narrows them. So the TIM23 and TIM22 gaps are located
precisely, but their layer becomes explicit only once those steps are written
as declared realizer choices, as the kinetoplastid plan item will do.

## Options

1. **Controlled kind on variant sets.** Done, with structural inference
   so that existing modules gain labels without edits.
2. **A realizer set on the annoton.** Not done. Allowing an OR of
   participant selectors on one annoton would make layer 2 explicit in the
   data rather than in a label, at the cost of a schema change to
   `participant` and to every consumer of it. Worth revisiting once
   proteome runs show how often realizer choices are written as variant sets.
3. **Compile realizers into the circuit.** Done for family and domain ids.
   An HMM-based oracle that evaluates them is still to be written, as part of
   the reference-proteome plan item.

## Refinement: layer 1 is not perfectly binary either

Reduced lineages can lose parts of a step, as mitosomes lose most import
motor accessories. That is still handled at layer 1, by optional parts and
lineage variants, as an explicit curated claim, not by loosening the realizer
layer.
