---
title: "Cross-Study Generality — Four MetaboLights Studies"
---

# Cross-Study Generality — Four MetaboLights Studies

Supporting findings for the
[Metabolomics × GO/GO-CAM project](../METABOLOMICS.md). Before investing in the
[interactive demo](DEMO-PLAN.md), we checked that the
`metabolite → Rhea → GO` bridge and its enrichment hold up beyond the original
MTBLS1 pilot, across different **biofluids, platforms, diseases and metabolite
classes**. All numbers are computed live by the [`probe/`](probe/README.md)
pipeline (`fetch_metabolights.py` → `coverage_probe.py` → `go_enrichment.py` /
`go_bp_enrichment.py`); per-study reports are linked below.

## The four studies

| Study | Biofluid / platform | Phenotype | Metabolites |
|---|---|---|---|
| [MTBLS1](probe/studies/MTBLS1-RESULTS.md) | urine, **NMR** | type-2 diabetes | 64 |
| [MTBLS90](probe/studies/MTBLS90-RESULTS.md) | serum, **LC-MS** | cardiovascular / ageing (PIVUS) | 208 |
| [MTBLS404](probe/studies/MTBLS404-RESULTS.md) | urine, **LC-MS** | age / BMI / sex (Sacurine) | 109 |
| [MTBLS19](probe/studies/MTBLS19-RESULTS.md) | serum, **LC-MS** | hepatocellular carcinoma | 34 |

## Coverage — normalization is essential in every study

| Study | Exact | + protonation | + skeleton | Final % |
|---|---:|---:|---:|---:|
| MTBLS1 | 8/64 | 49/64 | **58/64** | 91% |
| MTBLS90 | 39/208 | 74/208 | **110/208** | 53% |
| MTBLS404 | 5/109 | 60/109 | **71/109** | 65% |
| MTBLS19 | 5/34 | 12/34 | **20/34** | 59% |

Two robust patterns:

1. **Protonation normalization is decisive everywhere** — exact match captures
   only 8–39% of what the two-tier normalization reaches; the protonation tier
   alone multiplies coverage 1.9–12× in every study. The skeleton tier then adds
   a further 5–18 metabolites each (the generic↔stereospecific amino-acid class).
   The headline insight from MTBLS1 is not a one-off.
2. **Final coverage tracks metabolite chemistry, not study quality.** The
   polar-metabolite studies (urine: 91%, 65%) connect better than the lipid-rich
   serum LC-MS studies (53%, 59%). The serum residuals are dominated by
   **complex lipids** (sphingomyelins, phosphatidylcholines, triacylglycerols)
   that Rhea does not carry as discrete reaction participants — a real,
   localisable **gap in the Rhea/GO bridge for lipid metabolism**, not a failure
   of the method. This is itself a useful finding for where curation/representation
   effort would pay off.

## Enrichment recovers each study's own biology

GO biological-process enrichment (via the human enzyme layer; same hypergeometric
test throughout) returns sharply different, **study-appropriate** processes —
strong evidence the signal is real and not an artefact of the pipeline:

| Study | Top GO biological processes (fold, FDR) |
|---|---|
| [MTBLS1](probe/studies/MTBLS1-GO-BP-ENRICHMENT.md) (urine, T2D) | amino acid metabolic process (4.3×, 9e-44); dicarboxylic acid metabolic process (6.0×); amino acid transport (5–7×) |
| [MTBLS404](probe/studies/MTBLS404-GO-BP-ENRICHMENT.md) (urine) | carboxylic/organic acid transport (4.2×, 1e-36); amino acid metabolic process (3.3×); oxoacid metabolic process (2.4×) |
| [MTBLS90](probe/studies/MTBLS90-GO-BP-ENRICHMENT.md) (serum, CVD) | **lipid metabolic process (2.9×, 3e-89)**; fatty acid metabolic process (3.9×); long-chain fatty acid metabolic process (5.5×) |
| [MTBLS19](probe/studies/MTBLS19-GO-BP-ENRICHMENT.md) (serum, HCC) | **lipid metabolic process (4.2×, 3e-63)**; lipid catabolic process (8.3×); glycerolipid catabolic process (15.0×) |

The two **urine** studies surface amino-acid and organic-acid metabolism and
transport; the two **serum LC-MS** studies surface lipid and fatty-acid
metabolism. The pipeline does not impose a template — it reads out the chemistry
that is actually in each sample. (GO molecular-function enrichments per study:
[MTBLS90](probe/studies/MTBLS90-GO-ENRICHMENT.md),
[MTBLS404](probe/studies/MTBLS404-GO-ENRICHMENT.md),
[MTBLS19](probe/studies/MTBLS19-GO-ENRICHMENT.md).)

## Conclusions for the demo

- The bridge + two-tier normalization + GO enrichment **generalise** across
  biofluid, platform and disease; the protonation insight is universal.
- The **lipid coverage gap** in serum LC-MS studies is the clearest next
  methodological target (extend the bridge to lipid classes — e.g. via Rhea's
  generic lipid participants or LIPID MAPS/SwissLipids → ChEBI).
- A demo should therefore include at least one **urine** and one **serum/lipid**
  example so users see both the strong-coverage and the gap cases honestly.

## Reproduce

```bash
for ACC in MTBLS1 MTBLS90 MTBLS404 MTBLS19; do
  uv run python fetch_metabolights.py $ACC
  uv run python coverage_probe.py    --chebi-file studies/$ACC.chebi.txt --out studies/$ACC-RESULTS.md          --source "$ACC"
  uv run python go_enrichment.py     --chebi-file studies/$ACC.chebi.txt --out studies/$ACC-GO-ENRICHMENT.md    --source "$ACC"
  uv run python go_bp_enrichment.py  --chebi-file studies/$ACC.chebi.txt --out studies/$ACC-GO-BP-ENRICHMENT.md --source "$ACC"
done
```
