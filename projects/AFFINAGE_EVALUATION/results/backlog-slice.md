# Backlog slice — Affinage deep-research files landed in gene folders

A demonstration bulk-run of [`affinage_deep_research.py`](../affinage_deep_research.py)
over a slice of the human backlog (human genes with a review but **no** existing
deep-research file — 794 such genes at time of writing). Each run fetches the Affinage
record and writes `genes/human/<GENE>/<GENE>-deep-research-affinage.md`.

**10 genes were generated; 3 representative ones are committed** (the session's git
transport only allows small pushes — the tool itself scales to the full backlog; run it
in a normal `git push` environment to land more). The committed slice is chosen to show
the full range of gate behaviour, not just the clean cases: one clean win plus the two
collision types the gates caught.

| Gene | pairwise | gates | Committed | Why |
|------|----------|:-----:|:---------:|-----|
| **ABCA1** | win  | ✅ pass | ✔ | clean record — lands with no caution |
| **ADA**   | loss | ⚠️ flag | ✔ | **organism collision** — narrative opens on *E. coli* Ada; banner warns |
| **ACAT1** | win  | ⚠️ flag | ✔ | **accession collision** — local review is thiolase `P24752`, Affinage resolved "ACAT1" to `P35610` (SOAT1/cholesterol acyltransferase); banner warns |
| ACADM  | win  | ✅ pass | — | (generated, clean) |
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

**The gates earn their keep.** In a 10-gene random-ish slice they caught two genuine
wrong-protein/low-trust situations that a naive import would have silently accepted:

- **ACAT1** — the accession-mismatch gate caught that Affinage's "ACAT1" record is about
  a *different protein* (SOAT1/ACAT cholesterol acyltransferase, P35610) than the reviewed
  mitochondrial acetyl-CoA acetyltransferase (thiolase, P24752). A textbook symbol
  collision the organism scan alone would have missed.
- **ADA** — the organism-token gate + `pairwise = loss` flagged the three-entity chimera
  (see the [project page](../AFFINAGE_EVALUATION.md) §3).

Every landed file is clearly marked as **external, LLM-generated preliminary research**
(not a curated annotation), records the mechanism-profile GO ids **for reference only**
(with a "do not import directly" note), and surfaces any tripped gate as a ⚠️ CAUTION
banner at the top — so a curator sees the caveat before the content.

## Reproduce / extend

```bash
# one gene
python projects/AFFINAGE_EVALUATION/affinage_deep_research.py human ABCA1 --write

# a slice of the backlog (bash)
for g in $(...list of human genes lacking deep research...); do
  python projects/AFFINAGE_EVALUATION/affinage_deep_research.py human "$g" --write
done
```
