---
title: "ARBA deployment check: when does an activity entail a process?"
---

# ARBA deployment check

[parent project ← Pathway satisfiability](../../PATHWAY_SATISFIABILITY.md)

A runnable prototype that applies the module satisfiability engine to automated
**biological-process** calls from UniProt's ARBA rules (`GO_REF:0000117`).

## The idea

An ARBA process call made from one sequence bundles two inferences:

1. **sequence → activity.** Does the protein catalyse the reaction? This is local
   to the sequence (family, FunFam, catalytic residues).
2. **activity → process ("deployment").** Is that activity used in the process
   *in this organism*? This depends on the rest of the genome: whether the other
   steps exist, whether a paralog does the job, whether the enzyme's role lies
   elsewhere.

GO does not encode the second inference. For example, `GO:0004617`
phosphoglycerate dehydrogenase activity has no `part_of` link to `GO:0006564`
L-serine biosynthetic process; its only non-subclass relations are its
substrates and products. Curated modules do encode it, so the check makes it
explicit:

> Protein P is `involved_in` process T in organism O if (a) P's own
> molecular-function annotations fill a step of a module whose process concept
> is T or a descendant of T, and (b) that module is satisfiable in O. A step
> holds if any O protein has a GOA annotation to the step's activity (QuickGO,
> any evidence, `is_a` descendants included).

Modules with `context.taxa` apply only to organisms inside those taxa.

| Verdict | Meaning |
|---|---|
| `ENTAILED` | P fills a step of an applicable module under T, and that module is satisfiable in O |
| `MODULE_INCOMPLETE` | P fills a step, but every such module has a step with no O protein |
| `NOT_ENTAILED` | modules under T exist, but P's activities fill none of their steps |
| `NO_MODULE` | no applicable module falls under T; not scored |

`exact_concept` in `results.tsv` records whether the module's process concept is
the row's term itself (`True`) rather than a descendant of it.

## Results

Current output is in [RESULTS.md](RESULTS.md); per-row detail is in
[results.tsv](results.tsv). The figures below are from the run of 2026-10-17
(4,058 ARBA process rows in reviewed genes; 1,617 scored), and RESULTS.md
emits the same table on every run.

Share of rows the gene review kept (ACCEPT or KEEP_AS_NON_CORE) or rejected
(REMOVE, MARK_AS_OVER_ANNOTATED or TOO_GENERAL), by verdict:

| Verdict | Module concept | Rows | Kept | Rejected |
|---|---|---:|---:|---:|
| ENTAILED | exact | 220 | 93% | 4% |
| ENTAILED | ancestor of concept | 655 | 62% | 19% |
| MODULE_INCOMPLETE | exact | 26 | 92% | 4% |
| MODULE_INCOMPLETE | ancestor of concept | 55 | 78% | 5% |
| NOT_ENTAILED | exact | 119 | 80% | 10% |
| NOT_ENTAILED | ancestor of concept | 542 | 59% | 27% |

What the numbers say:

- **An exact entailment is a strong positive signal.** When the protein fills a
  step of a satisfiable module whose process is exactly the ARBA term, reviewers
  kept 93% of the rows and removed none outright (8 of 220 were marked
  over-annotated). These rows could be generated from the activity call plus the
  module, which states the grounds for the call.
- **Inherited entailment is true but often uninformative.** A protein that fills
  a step of a satisfiable module is involved in every ancestor of that module's
  process. Reviewers still reject 19% of these rows, mostly as over-annotation
  of vague terms (system development, response to stress, animal organ
  development). This check tests whether a call is grounded, not whether the term
  is specific enough; a specificity filter has to be applied separately.
- **NOT_ENTAILED means no evidence, not evidence against.** Most such rows are
  kept by reviewers. Typical causes: no module covers the protein's actual role
  (chaperones for *response to heat*, *protein refolding*), or the protein's GOA
  activity terms do not reach the module's step term.
- **MODULE_INCOMPLETE is mostly a diagnostic for modules and the oracle.** Two
  recurring causes:
  - Modules without `context.taxa` that are in practice lineage-specific (e.g.
    `bacterial_recbcd_end_resection` scored against human RAD51 paralogs). Adding
    taxa to these modules would remove the noise.
  - Steps whose activity term is not what GOA uses for the organism's own enzyme
    (e.g. `c_elegans_daf2_insulin_signaling` is unsatisfiable in *C. elegans* at
    the AGE-1 and PDK-1 steps). These point at a module term choice or a GOA
    activity gap worth checking.

### The case that motivated this

*P. putida* serA (Q88CM5) and *M. extorquens* serA (C5APD6) receive
`GO:0006564` L-serine biosynthetic process only from ARBA (rule
ARBA00093701, a single CATH FunFam condition); no other pipeline reaches it.
Both are `ENTAILED`: each fills the phosphoglycerate dehydrogenase step of
`phosphorylated_serine_biosynthesis`, and the SerC and SerB steps are filled by
other proteins in each proteome. The ARBA call is therefore backed by the module
rather than being asserted without stated grounds.

## Caveats

- The oracle uses GOA activity annotations, including electronic ones (ARBA,
  EC, Rhea, InterPro2GO). That is deliberate (step 1 is the activity
  inference), but a wrong activity call propagates into the verdict.
- Steps without a GO activity term cannot be tested and are assumed present.
- Presence is not flux: a satisfiable module is permitted, not shown to run.
- Taxon scope comes from each module's `context.taxa`. A module that declares
  no taxa is scored for every organism, so a lineage-specific module without
  taxa can be matched across kingdoms; this affects ENTAILED and NOT_ENTAILED as
  well as MODULE_INCOMPLETE. Before the `dicty_*` and `pqq_biosynthesis` modules
  were given taxa, zebrafish shha was ENTAILED for regulation of developmental
  process solely by the *Dictyostelium* counting-factor module, and human
  CYP21A2 was scored against bacterial PQQ biosynthesis. A module that declares taxa only as free text (no
  NCBITaxon id) is excluded, and RESULTS.md lists those modules; grounding their
  taxa would bring them back.
- The organism-level oracle is stricter than the gene-level test: it asks
  QuickGO for is_a descendants of the step activity with an exact taxon match,
  while the protein's own activity is matched through is_a and part_of
  ancestors. A step can therefore read as absent when its enzyme is annotated
  only at strain level or through part_of.
- Competing modules are not yet weighed. `other_modules` lists modules outside
  T that the protein also fills (e.g. a dehydrogenase that also fits vitamin B6
  biosynthesis), for manual review.

## Reproduce

```bash
uv run python projects/PATHWAY_SATISFIABILITY/arba_deployment/deploy_check.py
```

QuickGO and UniProt taxonomy responses are cached under `.cache/arba_deployment/`
(git-ignored); a first run takes about 20 minutes and makes roughly 11,000
QuickGO requests.
