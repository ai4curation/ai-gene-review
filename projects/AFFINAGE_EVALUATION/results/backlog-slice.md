# Backlog slice — Affinage deep-research first-pass over the human backlog

A demonstration run of [`affinage_deep_research.py`](../affinage_deep_research.py) over a
slice of the human backlog (human genes with a review but **no** existing deep-research
file — 794 such genes at time of writing). Running the tool with `--write` writes
`genes/human/<GENE>/<GENE>-deep-research-affinage.md`, which the AIGR review workflow
already ingests — so no pipeline change is needed to "wire in" Affinage.

**Where the committed examples live, and what gates an in-tree write.** The 5 demo genes
of this slice are committed *here*, under `results/example-<GENE>-deep-research-affinage.md`,
mirroring the existing `example-GPX4` demo — they illustrate the tool's output (including
the two collision cases) without seeding any gene's review. That is separate from the
backlog campaign, which *does* write into the live tree: there are 58
`genes/human/*/*-deep-research-affinage.md` files committed at time of writing, one per
gene actually being reviewed.

The care needed is because a file in a gene folder is *ingested by a future review of that
gene* — and some Affinage records describe the **wrong protein** (symbol collisions, see
below). The file itself carries no in-file warning: it is a faithful provider record, and
the trust-gate judgment belongs in the review's `reference_review`, not in the source file.
So the safety check lives in the **tool** instead — `--write`/`--out` into `genes/` is
**refused** (non-zero exit) when a wrong-protein gate trips (accession mismatch or a
non-human organism token in the narrative opening), unless `--force` is passed. The soft
`pairwise` signal only warns; it is already in the frontmatter as
`self_evaluation_pairwise`. Use `--write` when you actually intend a file to seed a
specific gene's review, and record your assessment of the record in that review's
`references[].reference_review`.

## The 10-gene slice (gates make the case)

| Gene | pairwise | gates | Example committed | Note |
|------|----------|:-----:|:-----------------:|------|
| GPX4   | win  | ✅ pass | ✔ `results/example-GPX4-…`  | clean worked example |
| ABCA1  | win  | ✅ pass | ✔ `results/example-ABCA1-…` | clean win |
| ACADM  | win  | ✅ pass | ✔ `results/example-ACADM-…` | clean win |
| **ADA**   | loss | ⚠️ flag | ✔ `results/example-ADA-…`   | **organism collision** — narrative is *E. coli* Ada / SAGA, not human adenosine deaminase |
| **ACAT1** | win  | ⚠️ flag | ✔ `results/example-ACAT1-…` | **accession collision** — Affinage "ACAT1" = SOAT1 `P35610`, not the reviewed thiolase `P24752` |
| ADSL   | tie  | ⚠️ flag | — | (generated; low-confidence self-eval) |
| ACLY   | win  | ✅ pass | — | (generated, clean) |
| ACOX1  | win  | ✅ pass | — | (generated, clean) |
| ADAM10 | win  | ✅ pass | — | (generated, clean) |
| AANAT  | tie  | ⚠️ flag | — | (generated; tie) |
| AASS   | tie  | ⚠️ flag | — | (generated; tie) |

Of the 10-gene slice, **5/10 passed all gates cleanly** (`win` + no collision); the other
5 were flagged (2 `tie`, plus the ADA organism collision and the ACAT1 accession
collision) — a ~50% clean rate on a random-ish backlog slice, underlining that the gates
are load-bearing, not decorative.

**The gates earn their keep.** In this slice they caught two genuine wrong-protein cases
that a naive import would have silently accepted:

- **ACAT1** — the accession-mismatch gate caught that Affinage's "ACAT1" record is about a
  *different protein* (SOAT1/ACAT cholesterol acyltransferase, P35610) than the reviewed
  mitochondrial acetyl-CoA acetyltransferase (thiolase, P24752). A textbook symbol
  collision the organism scan alone would have missed.
- **ADA** — the organism-token gate + `pairwise = loss` flagged the multi-entity chimera
  (see the [project page](../AFFINAGE_EVALUATION.md) §3).

Every example file is a **faithful, unedited rendering** of the Affinage record — clearly
marked in its frontmatter as
**external, LLM-generated preliminary research** (not a curated annotation) and reproducing
Affinage's own mechanism-profile GO ids as-is. It carries **no AIGR interpretation**: the
trust gates print to **stderr** (see the ADA/ACAT1 runs above), and the reviewer records the
resulting judgment — including whether to import the GO grounding — in the gene review's
`references[].reference_review`, never in the source file.

## Reproduce / extend

```bash
# preview one gene (stdout)
python projects/AFFINAGE_EVALUATION/affinage_deep_research.py human ABCA1

# actually seed a specific gene's review (writes into the gene folder)
python projects/AFFINAGE_EVALUATION/affinage_deep_research.py human ABCA1 --write

# regenerate the committed examples
for g in GPX4 ABCA1 ACADM ADA ACAT1; do
  python projects/AFFINAGE_EVALUATION/affinage_deep_research.py human "$g" \
    --out projects/AFFINAGE_EVALUATION/results/example-$g-deep-research-affinage.md
done
```
