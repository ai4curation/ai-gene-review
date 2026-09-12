# ACP7 (acid phosphatase type 7) — review notes

PAINT no-IBA project review, using the `affinage` deep-research provider plus UniProt Q6ZNF0
and the GOA TSV.

## Uncharacterised, not unstudied

Four annotations, **all IEA**, and **no functional or biochemical data** exists for this protein.
The protein itself is real — UniProt records `PE 1: Evidence at protein level` with proteomics
identification — and there *is* a primary paper.

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

## Correction: the kidney bean template is a *deliberate published choice*

An earlier draft of this review asserted three times that no primary literature exists, reasoning
from an empty affinage record. **That was wrong**, and the refutation was in the UniProt file the
review was itself citing: reference [4] is **PMID:16793224**, *"Identification and molecular
modeling of a novel, plant-like, human purple acid phosphatase"* — the `ECO:0000303` source for
UniProt's own "Purple acid phosphatase long form" AltName.

**An empty affinage record is evidence about affinage's coverage, not proof that no literature
exists.** The correct reading is narrower: affinage found no *mechanistic* discoveries, which fits
a gene whose only paper is a bioinformatic identification plus a structural model rather than a
functional study.

And the paper strengthens the review rather than merely correcting it. It argues ACP7 is the
founding member of a **novel plant-like PAP subfamily** in animals, and builds a structural model
of the human enzyme **on the red kidney bean structure specifically**, showing the catalytic
centre is present. So P80366 is not an arbitrary cross-kingdom hop — it is the considered template
for a protein argued to be plant-like. That makes the `ECO:0000250` chain far better justified
than the first draft implied.

UniProt's `PAN-GO; Q6ZNF0; 0 GO annotations based on evolutionary models` still stands, and is
the accurate statement of what is missing: evolutionary-model annotation, and functional data.

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
