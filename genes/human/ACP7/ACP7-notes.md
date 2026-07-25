# ACP7 (acid phosphatase type 7) — review notes

PAINT no-IBA project review, using the `affinage` deep-research provider plus UniProt Q6ZNF0
and the GOA TSV.

## A completely predicted gene

Four annotations, **all IEA**, and no experimental data of any kind exists for this protein.

The provenance is worth stating precisely, because it applies to every annotation:

| Statement | Evidence |
|---|---|
| FUNCTION (metallophosphoesterase, purple acid phosphatase family) | `ECO:0000250` → **P80366** |
| EC 3.1.3.2, CATALYTIC ACTIVITY (RHEA:15017) | `ECO:0000250` → **P80366** |
| COFACTOR Fe cation; COFACTOR Zn²⁺ | `ECO:0000250` → **P80366** |
| SUBCELLULAR LOCATION Secreted | `ECO:0000305` (curator inference) |
| SIGNAL 1–26 | `ECO:0000255` (prediction) |

**`P80366` is `PPAF_PHAVU` — the Fe(3+)-Zn(2+) purple acid phosphatase of the kidney bean,
*Phaseolus vulgaris*.** A plant enzyme is a distant source for a human function assignment, and
it is the sole source for this gene's catalytic activity, EC number and both cofactors.

Two independent corroborations that this is genuine darkness rather than a gap in my searching:

- UniProt's own line: `PAN-GO; Q6ZNF0; 0 GO annotations based on evolutionary models`
- The affinage record returns **"No mechanistic discoveries found in literature"** with an empty
  citation list — the only gene in this campaign so far for which the provider found *nothing*.

That empty record is informative rather than useless. Affinage covers every human protein-coding
gene, so an empty result is positive evidence that the primary literature is absent.

## Actions

| Term | Action | Reason |
|---|---|---|
| `GO:0003993` acid phosphatase activity | ACCEPT | best available inference; fold, family and metal residues all well supported — but a prediction from a plant homolog |
| `GO:0046872` metal ion binding | ACCEPT | **best-supported of the four** — residue-level `BINDING` features for Fe and Zn; the binuclear centre defines the family |
| `GO:0016787` hydrolase activity | KEEP_AS_NON_CORE | two levels above the specific term from the same prediction |
| `GO:0005576` extracellular region | ACCEPT | plausible, but `ECO:0000305` inferred from an `ECO:0000255` predicted signal peptide — a prediction resting on a prediction |

Nothing is removed. All four are reasonable inferences from a real, well-supported fold. The
review's contribution is to record **what kind of knowledge this is**: the gene is annotated
entirely by prediction, and `core_functions` says so explicitly rather than presenting the
activity as established.

## Cache gotcha, hit again

`just validate` rewrote `cache/go/terms.csv` and dropped **18 rows** added to main by other
merged PRs. Caught by `git diff origin/main -- cache/go/terms.csv | grep '^-GO:'` before
committing; fixed with `git checkout origin/main -- cache/go/terms.csv`. Second occurrence in
this campaign (see PR #2227) — worth checking on every gene.
