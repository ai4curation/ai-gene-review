# Constraint-based modelling task: rbsD (b3748) and growth on D-ribose

This is a **computational task**, not a literature review. The deliverable is an
executed constraint-based simulation with its code and numeric output. Literature
should be used only to justify the model edit described below, not as a substitute
for running the simulation.

## Question

In the *Escherichia coli* K-12 MG1655 genome-scale metabolic model **iML1515**, is
gene **b3748 (rbsD)** required for growth on **D-ribose as the sole carbon source**?

Answer this for two model variants and report the numbers:

- **(a) Published model.** iML1515 exactly as distributed by BiGG Models
  (`http://bigg.ucsd.edu/static/models/iML1515.json`).
- **(b) Reannotated variant.** The same model, edited so that rbsD is represented by
  the reaction it is currently annotated as catalysing in UniProt — **D-ribose
  pyranase, EC 5.4.99.62** (interconversion of β-D-ribopyranose and
  β-D-ribofuranose) — rather than by whatever role it holds in the published model.
  Concretely: add the pyranase reaction with `b3748` as its gene-protein-reaction
  rule, make the downstream ribose-phosphorylating step depend on the pyranase
  product, and remove `b3748` from any gene-protein-reaction rule in which it
  currently appears but which it is not now believed to carry out.

For each variant report:

1. Wild-type predicted growth rate on D-ribose minimal medium (h⁻¹).
2. Predicted growth rate of the `b3748` single-gene deletion on the same medium.
3. The ratio KO / WT.

State plainly whether the two variants give the same answer or different answers.

## How to do it

- Use **COBRApy**. Report the COBRApy version and the solver used.
- Define the medium explicitly: D-ribose as sole carbon source, aerobic. Report the
  exact exchange-reaction identifiers and bounds you set, and confirm that no other
  carbon source is left open.
- Use COBRApy's gene-deletion facilities rather than ad-hoc bound manipulation, and
  do not mutate the loaded model in place across experiments.
- Report the exact identifiers of every reaction you inspected, added, or modified,
  and the GPR strings before and after your edit.
- Sanity-check the base model first (growth on glucose minimal medium) and report
  that number too, so the ribose result can be judged against a known baseline.

## Constraints on reporting

- **Do not fabricate.** If you cannot install COBRApy, cannot reach BiGG, or cannot
  execute code, say so plainly, state exactly which step failed and the error, and
  stop. A truthful "the sandbox could not run this" is a fully acceptable outcome
  and is more useful than a plausible-looking number.
- Do not report a growth rate that you reasoned to rather than computed. Every
  number in the answer must come from a solver call you actually made.
- If the model edit in (b) can be implemented in more than one defensible way,
  pick one, state the choice and why, and note how the result would change under
  the alternative.

## Required output

1. **Result table** — variant × (WT growth, KO growth, KO/WT ratio), plus the
   glucose baseline.
2. **The code you ran**, verbatim, together with its stdout — not a cleaned-up
   summary or a reconstruction.
3. **Interpretation** — does the published model's prediction for a `rbsD` knockout
   on ribose match what is known experimentally about *rbsD* mutants? If the two
   variants disagree, say which one matches the experimental phenotype and cite the
   primary literature (PMID) for that phenotype.
4. **Provenance** — COBRApy version, solver, model source URL and any checksum, and
   the date retrieved.

Save the executed code and its raw output as artifacts alongside the report.
