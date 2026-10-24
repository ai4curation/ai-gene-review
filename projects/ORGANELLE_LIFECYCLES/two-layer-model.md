---
title: "Two-layer model: steps need activities, activities need realizers"
---

# Two-layer model: steps need activities, activities need realizers

[Back to Organelle Lifecycle Modules](../ORGANELLE_LIFECYCLES.md)

**Bottom line:** a module used as a rule should make two different kinds of
claim, and the engine should keep them apart. A process step requires a
molecular function (MF); that requirement is close to binary. An MF is
carried out by one of several families, domains or complexes; that mapping is
open-world and gappy. Today both are written as `variant_sets` and compiled to
the same OR, so a genome that fails a rule cannot say which kind of gap it hit.

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

## What the engine does today

Checked against `ai_gene_review.module_logic` on `main`, running the
mitochondrion umbrella with TIM23 and TIM22 absent:

- **The gap is reported at the umbrella stage only.** `unsatisfied_steps`
  returns `protein_import`; on the import module itself it returns
  `tim23_translocation` and `tim22_insertion`. Locating a gap inside a
  referenced module needs a recursive report.
- **The gap candidates are not filtered to absent atoms.** `abduce` builds
  `gap_candidates` from every atom under the failed step, so the
  `protein_import` gap lists all 16 import symbols, including the 14 that
  were present. The `Abduction.gap_candidates` comment says "the canonical atoms
  all absent", so this is a mismatch between code and documentation.
- **Atoms carry no realizer.** An `Atom` holds the MF ids (`function_ids`),
  a gene symbol and representative UniProt accessions, but not the family or
  domain selector. An oracle that scans a new proteome with PANTHER HMMs has
  nothing to scan for; layer 2 exists in the YAML but not in the compiled
  circuit.
- **Variant-set axes are free text.** `axis` is a string, and the engine
  keeps only `set_id` and `selection`. Across the 406 variant sets in
  `modules/` there are 248 distinct axis strings. A keyword sort (rough, not a
  curated classification) puts about 117 on the realizer side ("enzyme
  family", "enzyme architecture", "paralog"), about 101 on the route or
  context side ("route", "compartment", "taxon"), 54 that mix both, and 134
  with no axis or one the heuristic cannot place.

## Options

1. **Controlled axis values.** Add an enum used alongside the free-text
   `axis` (for example `REALIZER` vs `ROUTE` / `TAXON` / `COMPARTMENT`), carry
   it into `Or`, and let gap reports label each gap by layer and attach only
   that layer's hypotheses. Smallest change; existing modules keep working
   and can be classified gradually.
2. **A realizer set on the annoton.** Allow an OR of participant selectors
   on one annoton, so one MF step lists its realizers directly. This makes
   layer 2 explicit in the data rather than in a label, at the cost of a
   schema change to `participant` and to every consumer of it.
3. **Compile realizers into the circuit.** Whichever of the above, carry the
   family or domain selector on each `Atom` so an HMM-based oracle can
   evaluate it. This is required before umbrellas can be run on reference
   proteomes, which is already on the plan.

Options 1 and 3 can be taken without reworking existing modules. Option 2 is
the cleaner end state, and option 1 is a reasonable first step towards it.

## Refinement: layer 1 is not perfectly binary either

Reduced lineages can lose parts of a step, as mitosomes lose most import
motor accessories. That is still handled at layer 1, by optional parts and
lineage variants, as an explicit curated claim, not by loosening the realizer
layer.
