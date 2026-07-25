# Backlog slice — Affinage deep-research first-pass over the human backlog

A demonstration run of [`affinage_deep_research.py`](../affinage_deep_research.py) over a
slice of the human backlog (human genes with a review but **no** existing deep-research
file — 794 such genes at time of writing). Running the tool with `--write` writes
`genes/human/<GENE>/<GENE>-deep-research-affinage.md`, which the AIGR review workflow
already ingests — so no pipeline change is needed to "wire in" Affinage.

**Where the committed examples live.** We do **not** commit the generated files into the
live `genes/human/` tree. Two reasons: (1) the repo PR template asks not to commit
`*-deep-research-*.md`; (2) more importantly, a file in a gene folder is *ingested by a
future review of that gene* — and some Affinage records describe the **wrong protein**
(symbol collisions, see below), so an in-tree file would feed wrong-gene biology into a
later review despite its CAUTION banner. The committed examples therefore live here under
`results/example-<GENE>-deep-research-affinage.md` (5 genes), mirroring the existing
`example-GPX4` demo. Use `--write` locally when you actually intend a file to seed a
specific gene's review.

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

Every example file is clearly marked as **external, LLM-generated preliminary research**
(not a curated annotation), records the mechanism-profile GO ids **for reference only**
(with a "do not import directly" note), and surfaces any tripped gate as a ⚠️ CAUTION
banner at the top.

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
