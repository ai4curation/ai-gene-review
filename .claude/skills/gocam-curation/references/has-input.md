# `has input`

`has input` names the molecule or entity an activity **targets or transforms**.
It is one of the easiest fields to misread; the wrong filler is QC flag
`HAS_INPUT_MISUSE`.

## Correct filler by activity type

| Activity | `has input` is… | NOT |
|---|---|---|
| Enzyme | the **substrate** being modified | the product |
| Transcription factor | the **target gene** | the DNA molecule itself |
| Receptor | the **downstream effector** it activates | the ligand |
| Transporter | the **cargo** moved | the membrane/compartment |

## The classic error: ligand→receptor

Do **not** use `has input` to record a ligand binding a receptor. The ligand is
an **upstream causal regulator** of the receptor's activity — model it as a
causal edge (ligand activity → receptor activity), not as the receptor's input.
See `causal-relations.md`.

## Rule of thumb

`has input` answers "what does this activity act **on** to do its job?" If the
candidate filler is what *triggers* the activity (a ligand, an upstream signal),
it belongs on a causal edge, not in `has input`.
