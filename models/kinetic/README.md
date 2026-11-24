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
    README.md                   # provenance: source, retrieval date, checksum, licence, results
    mapping_to_modules.yaml     # reviewed bridge: module elements <-> model species
```

`model.xml` is pinned by the checksum in its folder's README and is excluded from
the whitespace-fixing pre-commit hooks so that it stays byte-identical to the
download.

## Requirements

The reader needs `python-libsbml` and `sympy`. They are not core dependencies of
`ai_gene_review`; in this repository they come with `cobra` in the dev group, so
`uv sync --group dev` installs them. Without them the command stops with a
message naming the missing packages.

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
2. **Sign of each effector.** Every species in the rate law, or listed as a
   modifier, whose entity is not a target is an effector. That includes an
   enzyme written on both sides of a one-step catalysis (`E + S → E + P`): its
   activity does not change, so it is not a target, but it drives the
   conversion. An effector's sign is the sign of the partial derivative of the
   rate with respect to it. The derivative is evaluated at the model's own
   parameter values, over a log-uniform sample of species concentrations
   (10⁻³–10³). If the derivative is positive at some points and negative at
   others, the sign is `?`.
3. **Edge.** The edge `effector → target` takes the product of the two signs. So
   an activator of a deactivating reaction, such as a phosphatase, is an
   inhibitor of the target.

An inactive form (level 0) in a rate law is listed in the extraction notes, not
counted. Rules, events, unparsable rate laws, reactions that change no entity's
activity and effectors whose derivative could not be evaluated at any sample
point are listed there too, so nothing is dropped silently.

A `?` model sign still counts as agreement with the module's sign in the diff
(the same rule the Boolean comparison uses), so the report marks such rows
`model sign undetermined`. The report also prints the sampling seed and sample
count; re-run with `--seed` or `--samples` to check whether a `?` is robust.

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

Options: `--module-key` (the mapping's `modules:` key, default the module file
stem), `--seed` and `--samples` (derivative sampling).

## Models

| Folder | Model | Compared with | Result |
|---|---|---|---|
| [`biomd0000000010`](biomd0000000010/README.md) | Kholodenko 2000 MAPK cascade | `erk_cascade` | 3 agree, 0 conflicts |

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
- **Rate laws are parsed as text.** libsbml writes each rate law as an L3 infix
  string, which is parsed with sympy's `parse_expr`. That function evaluates
  Python, so a formula containing anything other than identifier characters,
  digits, whitespace and arithmetic, comparison and grouping symbols is refused
  and noted. Piecewise and boolean functions are not translated and end up in
  the extraction notes as unparsable. `log` follows the SBML L3 convention
  (`log10(x)`, and `log(b, x)` for log base *b* of *x*), not sympy's.
