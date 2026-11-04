# Locations and compartments

Every activity's `occurs_in` should place it in one distinct compartment, and
causally connected activities should be in the same or adjacent compartments.
Run the automated check first:

```bash
just gocam-compartments <model_id>
```

It resolves each `occurs_in` through `is_a`/`part_of` against a fixed set of
pairwise-disjoint compartments (`src/ai_gene_review/data/gocam_compartments.yaml`):
extracellular region, plasma membrane, cytosol, nuclear envelope, nuclear lumen,
and the membrane and lumen of each organelle (plus chloroplast, periplasm and
the bacterial outer membrane). Background: `projects/GOCAM_COMPARTMENTS.md`.

## Location status

| Status | Meaning | What to do |
|---|---|---|
| `RESOLVED` | the term sits in one compartment | nothing |
| `COARSE` | the term spans several (cytoplasm, mitochondrion, nucleus) | fine when the evidence cannot resolve further; note it if the mechanism fixes the side |
| `UNRESOLVED` | no path reaches any compartment (chromatin, cytoskeleton, a complex term) | flag `UNRESOLVED_COMPARTMENT`; the report's `hint` gives the usual location and, where one exists, a term that states it (chromatin → `GO:0000228` nuclear chromosome) |
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
| `NONADJACENT` | the edge skips one or more compartments (`distance` = steps in the adjacency graph) |
| `INDETERMINATE` | an end is `UNRESOLVED` or `MISSING` |

A `NONADJACENT` edge with a **direct** predicate (`directly positively/negatively
regulates`, `directly provides input for`) is the strong signal: direct action
needs contact. Flag `NONADJACENT_COMPARTMENTS` on the upstream activity and say
which step is missing. Typical causes:

- **Secretion skipped.** CASP1 (cytosol) → IL1B cytokine activity (extracellular
  region) in `59cc772c00000000`: CASP1 cleaves pro-IL-1β in the cytosol; release
  through the plasma membrane is a separate step the model omits.
- **Translocation skipped.** A receptor kinase at the plasma membrane →
  transcription factor activity in the nucleus: the phosphorylation happens in
  the cytosol and the factor then enters the nucleus.
- **A wrong `occurs_in`.** One end placed by default (e.g. cytoplasm for a
  luminal enzyme).

An indirect edge (`indirectly ...`, `causally upstream of ...`) across
compartments may be a deliberate summary of a transport step; record it in
`notes` but do not flag it unless the summary hides a mechanism the model
claims elsewhere.
