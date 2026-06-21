# Causal relations

`causal_associations` are directed edges from one activity to a **downstream**
activity. Two things must be right: the **directness** and the **direction**.

## Direct vs indirect

- **Direct** (`directly positively regulates` `RO:0002413`,
  `directly negatively regulates` `RO:0002630`): a **single step** — the upstream
  activity acts immediately on the downstream one (kinase phosphorylates its
  substrate; ligand activity activates a receptor).
- **Indirect** (`positively regulates` `RO:0002213` / `negatively regulates`
  `RO:0002212`, or the explicit `indirectly *` `RO:0002407`/`RO:0002409`): a
  **multi-step** mechanism (transcription factor → gene expression → new protein
  activity).

Asserting direct regulation for a multi-step mechanism (or vice versa) is QC flag
`DIRECT_VS_INDIRECT_CAUSAL`.

## Directionality

Edges read **subject → object**: the regulator (subject) acts on the target
(object). A reversed edge is QC flag `INCORRECT_DIRECTIONALITY`. Sanity-check by
asking "which activity's output changes the other's rate?" — that one is the
subject.

## Mechanism vs phenotype

A knockout/knockdown **phenotype** does not by itself establish a **direct**
mechanistic edge — the effect may be many steps downstream. Reserve direct edges
for direct mechanistic evidence (biochemistry, a measured modification, in vitro
reconstitution); otherwise use an indirect relation or leave the edge out.

## Orphans

An activity with no causal edges to the rest of the model is QC flag
`ORPHAN_ACTIVITY` — usually a sign the model is incomplete or the activity is
mis-scoped.
