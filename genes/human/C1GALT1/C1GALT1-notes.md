# C1GALT1 (T-synthase) — curation notes

## 2026-09-17 — de novo review

No `-deep-research-PROVIDER.md`: tooling unavailable (OpenAI key rejected);
nothing self-authored was named as provider output.

### The committed enzyme was missing from its own pathway

C1GALT1's only two biological-process rows in GOA were `angiogenesis` and
`kidney development` — both cited to a case-control SNP association study. It had
**no** mucin-type O-glycosylation process annotation at all, despite performing
the committed galactosylation step.

Ran the comparator check before proposing anything, per CLAUDE.md:

- GALNT1 (immediately upstream) carries `GO:0016266` ✓
- GCNT1 (immediately downstream) carries `GO:0016266` ✓
- C1GALT1C1 / Cosmc — its own **non-catalytic chaperone** — carries the parent
  `GO:0006493` three times ✓

A pathway whose initiating enzyme, branching enzyme and a chaperone are all
annotated to the process, but whose committed enzyme is not, is an omission
rather than a curatorial line. `GO:0016266` added as the single `NEW`. The
participation test is met directly — C1GALT1 catalyses a step — and the term's
definition explicitly covers elongation ("which can be further elongated with the
sequential addition of").

### Citation problem the format checks cannot see

PMID:17228361 is correctly identified, correctly titled, and supports **neither**
annotation drawn from it. It is a case-control association study of 670 IgAN
patients and 494 controls carrying an `IMP` evidence code. Recorded
`correctness: MISCITED`.

### Angiogenesis vs kidney development — why they differ

Both rows cite the same unsupporting reference, so the asymmetry needs its own
evidence. It has it on one side only:

- **Angiogenesis** → `KEEP_AS_NON_CORE`. The T-synthase knockout has a defined
  developmental vascular phenotype: [PMID:14745002 "T-synthase-deficient brains
  formed a chaotic microvascular network with distorted capillary lumens and
  defective association of endothelial cells with pericytes and extracellular
  matrix."] and [PMID:14745002 "Gene-targeted mice lacking T-synthase instead
  expressed the nonsialylated Tn antigen in these cells and developed brain
  hemorrhage that was uniformly fatal by embryonic day 14."] Real but downstream —
  the consequence of altered glycans on other proteins, not something this enzyme
  does during angiogenesis.
- **Kidney development** → `MARK_AS_OVER_ANNOTATED`. No supporting phenotype at
  all; IgA nephropathy is an acquired adult glomerular disease driven by
  under-galactosylated IgA1 from plasma cells, not a developmental defect.

(An earlier draft justified the angiogenesis call by an *uncited* appeal to "the
mouse literature". That was flagged in PR review on #3058 and is why
PMID:14745002 was fetched and cited. Recording it here: an unreferenced appeal to
a body of literature is not support, even when the literature exists.)

### Client of a chaperone

The `protein binding` row (partner Q96EU7 = Cosmc) was MODIFYed to
`GO:0051087 protein-folding chaperone binding` rather than removed — unusually
for a generic `protein binding` row, the cited paper supports a specific
client-side MF: [PMID:21496458 "Core 1 synthase specific molecular chaperone
(Cosmc), a molecular chaperone specific for C1GalT, is essential for the
expression of functional C1GalT in mammalian cells."] The reciprocal chaperone
activity sits on Cosmc.

### Compartment

Three `GO:0016020 membrane` rows collapsed to `GO:0000139 Golgi membrane`.
[PMID:11677243 "The core 1 beta3-Gal-T predicts a 363-amino acid type II
transmembrane protein"] gives the topology; [PMID:37216524 "requires the action
of a single Golgi enzyme T-synthase (encoded by C1GALT1)"] gives the organelle.
Note the contrast with its chaperone, which is ER-resident — the compartment
split between the two is explicit in the same sentence pair.

### Cross-reference

HPA calls C1GALT1 "Nuclear bodies, Cytosol" with no Golgi call — the same
replace-the-Golgi pattern that made GCNT1's nuclear speck annotation an artefact.
Unlike GCNT1's, this one was never imported into GO. See `GCNT1-notes.md`.
