# Kinetic models: external sources and reviewed bridges

Cached SBML kinetic (ODE) models, with the reviewed mappings that bridge them to
curated modules under `modules/`. They are read by
`ai-gene-review compare-module-sbml` (`src/ai_gene_review/sbml_signed.py`).

Like the Boolean models in [`../boolean/`](../boolean/README.md) and the Maud
model in [`../methionine/`](../methionine/README.md), an external model is
**evidence, not truth**. Its wiring is reduced to signed edges, put in a shared
symbol namespace through the reviewed mapping, and diffed against the module.
Nothing is merged; agreements and disagreements are reported for a curator to
adjudicate.

## Layout

```
models/kinetic/
  README.md
  biomd0000000010/              # one folder per model, named by its BioModels id
    model.xml                   # verbatim SBML from BioModels (DO NOT EDIT)
    mapping_to_modules.yaml     # reviewed bridge: module elements <-> model species
```

## How signed edges are read from a kinetic model

Species are grouped into **entities** (the phosphoforms of one kinase are one
entity), and each species form has an **activity level**: how far it is along
the activation path, 0 for the inactive form. Both come from the mapping.

For each reaction:

1. **Effect on a target.** The reaction's effect on an entity is the change in
   that entity's activity: the sum of level × stoichiometry over its products,
   minus the same over its reactants. MEK → MEK-P raises MEK activity (`+`);
   MEK-P → MEK lowers it (`-`). Entities whose activity does not change are not
   targets.
2. **Sign of each effector.** Every other species in the rate law, or listed as a
   modifier, is an effector. Its sign is the sign of the partial derivative of
   the rate with respect to it. The derivative is evaluated at the model's own
   parameter values, over a log-uniform sample of species concentrations
   (10⁻³–10³). If the derivative is positive at some points and negative at
   others, the sign is `?`.
3. **Edge.** The edge `effector → target` takes the product of the two signs. So
   an activator of a deactivating reaction, such as a phosphatase, is an
   inhibitor of the target.

An inactive form (level 0) in a rate law is listed in the extraction notes, not
counted. Rules, events, unparsable rate laws and reactions that change no
entity's activity are listed there too, so nothing is dropped silently.

## Mapping file format

The same shape as the Boolean mappings, plus `activity_levels`:

```yaml
source: <where the model came from>
publication: PMID:...
modules:                 # module file stem -> {symbol: module element id(s)}
  erk_cascade:
    MEK: mek_map2k
external:                # symbol -> SBML species id(s), every form of the entity
  MEK: [MKK, MKK_P, MKK_PP]
activity_levels:         # SBML species id -> activity level (unlisted species: 1)
  MKK: 0
  MKK_P: 1
  MKK_PP: 2
notes: |
  Why the mapping is what it is.
```

The report also prints each symbol's species annotations (UniProt, ChEBI) from
the SBML, so the grouping can be checked against what the model says the
species are.

## Usage

```bash
ai-gene-review compare-module-sbml \
    modules/erk_cascade.yaml \
    models/kinetic/biomd0000000010/model.xml \
    -m models/kinetic/biomd0000000010/mapping_to_modules.yaml
```

## Models

### biomd0000000010: Kholodenko 2000 MAPK cascade

- **Source:** BioModels [BIOMD0000000010](https://www.ebi.ac.uk/biomodels/BIOMD0000000010),
  "Kholodenko2000 - Ultrasensitivity and negative feedback bring oscillations in
  MAPK cascade"; curated BioModels entry. Publication PMID:10712587.
- **Retrieved:** 2026-11-23 from
  `https://www.ebi.ac.uk/biomodels/model/download/BIOMD0000000010?filename=BIOMD0000000010_url.xml`.
- **SHA-256:** `906964e07ffd570ad94a03c1222e230b54b913cd536b008392bfb6155930a966`
- **Licence:** CC0 1.0 (BioModels public domain dedication).
- **Species:** annotated to *Xenopus laevis* RAF1 (P09560), MEK1 (Q05116) and
  MAPK1 (P26696). The MAPKKK species are named "Mos" in the SBML but annotated
  to RAF1; the mapping follows the annotation.
- **Compared with:** `modules/erk_cascade.yaml`, on the RAF (MAP3K), MEK and ERK
  tiers.

Result: all three edges the model asserts on those tiers agree with the module,
with no sign conflicts and nothing on either side alone. In particular, the
module's ERK ⊣ RAF feedback appears in the model as MAPK-PP in the
MAPKKK-activation rate law (reaction J0):

```
= ERK -| RAF   (model reactions: J0)
= MEK -> ERK   (model reactions: J6, J7)
= RAF -> MEK   (model reactions: J2, J3)
```

The module's other edges (adaptor, SOS, RAS, DUSP, ERK output) involve entities
the model does not contain, so they fall outside the comparison.

## Limits of the current reader

- **Explicit enzyme–substrate complexes are not read.** Mass-action models
  often write a catalytic step as
  `E + S ⇌ ES → E + P`, with the enzyme's role carried by the complex species.
  Sasagawa 2005 (BIOMD0000000049; EGF/NGF-driven ERK signalling in PC12 cells,
  99 species, 150 reactions) is written this way, with species such as
  `c_Raf_Ras_GTP_MEK` and `ppMEK_ERK`, and its species carry no names or
  annotations. Reading it needs a rule that credits the enzyme in a complex
  with the conversion the complex carries out. That is the next extension,
  not attempted here.
- **Sign sampling is a check over a range, not a proof.** A derivative that
  changes sign outside 10⁻³–10³ would be missed. The parameter values are
  the model's own; species concentrations are sampled.
- **Only signs are compared.** Strengths, delays and the quantitative
  behaviour the model was built to show (Kholodenko's oscillations) are not
  part of the comparison.
