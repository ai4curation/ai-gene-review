# Molecular function typing

The `molecular_function` of an activity should name **what the gene product
does**, as specifically as the evidence allows.

## Specificity

- Use the most specific available GO MF term.
- A generic parent where a child clearly applies is QC flag `GENERIC_MF`
  (e.g. "transcription factor" where "DNA-binding transcription activator"
  applies).

## Binding is not a function

A bare `protein binding` (or any unqualified `*binding`) MF, with no functional
consequence specified, is QC flag `BINDING_AS_FUNCTION`. Binding without a role
does not advance causal understanding.

Co-IP, pull-down, and Y2H demonstrate **interaction only**. They do not, by
themselves, license an "activates"/"regulates" claim — that needs a mechanistic
shift (kinetics, modification, conformational change).

Instead, identify the real role the binding serves:

| Observation | Better MF |
|---|---|
| Enzyme binds and modifies a substrate | the catalytic activity (kinase, phosphatase, ligase, …) |
| Receptor binds a ligand | receptor activity (ligand is a causal upstream regulator) |
| Protein links/bridges two partners | **molecular adaptor activity** (connector/linker) |
| Protein captures / compartmentalizes another | **protein sequestering activity** |

## Adaptors vs sequestering vs catalytic

- **Molecular adaptor activity** — mediates an interaction between two entities
  to bring them together (scaffold/connector). Represent the connecting role
  explicitly rather than as "binding".
- **Protein sequestering activity** — binds and holds a partner away from where
  it would otherwise act (capture/localize/store). Distinct from catalysis.
- **Catalytic activity** — an actual chemical transformation; pair with
  `has input` (the substrate).

When in doubt between adaptor and sequestering: an adaptor **couples** partners
to enable a downstream event; a sequester **withholds** a partner to prevent one.
