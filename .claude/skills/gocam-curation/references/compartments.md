# Locations and compartments

Every activity's `occurs_in` should place it in one distinct compartment, and
causally connected activities should be in the same or adjacent compartments.
The automated check finds leads for you to investigate:

```bash
just gocam-compartments <model_id>
```

It resolves each `occurs_in` through `is_a`/`part_of` against a fixed set of
pairwise-disjoint compartments (`src/ai_gene_review/data/gocam_compartments.yaml`):
extracellular region, plasma membrane, cytosol, nuclear envelope, nuclear lumen,
and the membrane and lumen of each organelle (plus chloroplast, periplasm and
the bacterial outer membrane). Background: `projects/GOCAM_COMPARTMENTS.md`.

**A finding is a lead, not a verdict.** Never copy the check's output into a
review as flags. For each finding, read the model's evidence for that edge or
location and decide. Record a QC flag only when you agree, and name the missing
step. When you reject a finding (a deliberate summary edge, a location the
evidence cannot resolve), say so in `notes` so it is not reopened. When the same
pattern recurs across models (receptor kinase → nuclear transcription factor),
treat it as a possible curation convention: raise it once as a question, not as
one defect per model.

## Location status

| Status | Meaning | What to do |
|---|---|---|
| `RESOLVED` | the term sits in one compartment | nothing |
| `COARSE` | the term spans several (cytoplasm, mitochondrion, nucleus) | fine when the evidence cannot resolve further; note it if the mechanism fixes the side |
| `UNRESOLVED` | no path reaches any compartment (chromatin, cytoskeleton, a complex term) | check what the evidence locates; if the location is real but unstated, flag `UNRESOLVED_COMPARTMENT`. The report's `hint` gives the usual location and, where one exists, a term that states it (chromatin → `GO:0000228` nuclear chromosome) |
| `MISSING` | no `occurs_in` | flag `MISSING_LOCATION` |

`UNRESOLVED` is a finding about the model, not about the biology. The location is
usually obvious (a transcription factor on chromatin is in the nucleus), but GO
puts `chromosome` outside the nucleus because prokaryotes have chromosomes, so
nothing in the model says the activity is nuclear.

## Edge status

Adjacent compartments share a boundary: a membrane and the aqueous space on each
side. Two lumens are never adjacent, and the cytosol is not adjacent to the
nuclear lumen (the envelope is between them).

| Status | Meaning |
|---|---|
| `SAME` / `ADJACENT` | physically possible as drawn |
| `BRIDGED` | two membranes bordering the same space (ER membrane → Golgi membrane, outer → inner mitochondrial membrane); possible at a contact site or on vesicle docking, so lower priority |
| `EXPLAINED` | the edge skips compartments, but a module pinned to both activities has a path through a transport step whose declared locations touch both ends; the report gives the path and the compartments spanned. Not a lead, though it rests on the module being right. An explanation with `spans_edge: false` was offered but refused: the edge stays `NONADJACENT` |
| `RELOCATING` | a direct regulation edge that skips compartments, where the downstream protein is known to sit next to the regulator (it is acted on there, then moves). Not a lead, but no module says how it moves yet |
| `NONADJACENT` | the edge skips one or more compartments and nothing explains it (`distance` = steps in the adjacency graph) |
| `INDETERMINATE` | an end is `UNRESOLVED` or `MISSING` |

A `NONADJACENT` edge with a **direct** predicate (`directly positively/negatively
regulates`, `directly provides input for`) is the strong signal: direct action
needs contact. Check the cited evidence. If it confirms a skipped step, flag
`NONADJACENT_COMPARTMENTS` on the upstream activity and name the step. Typical
causes:

- **Secretion skipped.** CASP1 (cytosol) → IL1B cytokine activity (extracellular
  region) in `59cc772c00000000`: CASP1 cleaves pro-IL-1β in the cytosol; release
  through the plasma membrane is a separate step the model omits.
- **Translocation skipped.** A receptor kinase at the plasma membrane →
  transcription factor activity in the nucleus: the phosphorylation happens in
  the cytosol and the factor then enters the nucleus.
- **A wrong `occurs_in`.** One end placed by default (e.g. cytoplasm for a
  luminal enzyme).

**Regulation is not material flow.** A direct regulation edge means the two
proteins touch; the downstream activity can still happen elsewhere afterwards
(a STAT phosphorylated at the membrane binds DNA in the nucleus). A
"directly provides input for" edge passes a molecule, which must cross every
membrane in between, so a jump there means a missing transporter.

**Prefer a module to a per-model flag** when the same jump recurs across many
models. Write the missing steps into the module (reusing a transport module by
`module_ref`), pin the GO-CAM activities at both ends with `gocam_associations`
(`model` plus `activity`), and rerun the check: the edges become `EXPLAINED`.
`karyopherin_nuclear_protein_import` and the JAK-STAT, BMP and TGF-beta modules
are the worked example; see `projects/GOCAM_COMPARTMENTS.md`.

An indirect edge (`indirectly ...`, `causally upstream of ...`) across
compartments may be a deliberate summary of a transport step; record it in
`notes` but do not flag it unless the summary hides a mechanism the model
claims elsewhere.
