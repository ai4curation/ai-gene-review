---
title: "Metabolomics → GO Bridge Coverage Probe"
---

# Metabolomics → GO bridge coverage probe

A small, reproducible probe for the
[Metabolomics × GO/GO-CAM project](../../METABOLOMICS.md). It answers the first
follow-up question: **does the `metabolite → Rhea → rhea2go → GO` bridge actually
connect**, and **how much of it depends on normalizing protonation state?**

## The finding (see [RESULTS.md](RESULTS.md))

On a 26-metabolite stand-in for a central-carbon / amino-acid / nucleotide /
cofactor metabolomics readout, reported by neutral name as a repository would:

- **Exact ChEBI match to Rhea: 0/26.**
- **After protonation normalization: 22/26.**

Rhea writes participants in their major protonation state at pH 7.3
(`citrate(3-)`, `ATP(4-)`, `succinyl-CoA(5-)`…); repositories report the neutral
species. Without normalization the bridge is essentially empty; with it, almost
everything connects — and lands on real GO molecular functions (ATP → 492 GO MF
terms, NAD+ → 447, acetyl-CoA → 385).

The 4 residual misses expose a *second*, distinct ID-mismatch class
(stereochemistry/anomer and generic-vs-structurally-specific ChEBI) that
protonation expansion does not fix — documented in RESULTS.md as a follow-up.

## Real study: MetaboLights MTBLS1 (see [studies/MTBLS1-RESULTS.md](studies/MTBLS1-RESULTS.md))

Run on the 64 curator-assigned ChEBI metabolites of MTBLS1 (Salek et al.,
type-2-diabetes urine NMR), pulled live from the study's MAF:

- **Exact ChEBI match to Rhea: 8/64** → **protonation-normalized: 49/64** (6× uplift).
- The 8 exact matches are the uncharged metabolites (acetone, ethanol,
  adenosine, uridine…) plus one curator-entered anion — i.e. the ones with no
  protonation ambiguity.
- The residual misses are dominated by the **branched-chain amino acids
  (Ile/Leu/Val)** — the canonical diabetes biomarkers — lost because the
  curators used generic (non-stereospecific) ChEBI ids while Rhea uses the
  L-zwitterion. This is the stereochemistry/generic-vs-specific class, the
  motivation for the next follow-up.

## Run it

```bash
uv run python coverage_probe.py                 # built-in demo metabolite set
uv run python coverage_probe.py --write-results # also regenerate RESULTS.md

# Real MetaboLights study, end to end:
uv run python fetch_metabolights.py MTBLS1      # -> studies/MTBLS1.chebi.txt
uv run python coverage_probe.py --chebi-file studies/MTBLS1.chebi.txt \
    --out studies/MTBLS1-RESULTS.md --title "MTBLS1 → GO bridge coverage" \
    --source "MetaboLights MTBLS1"

uv run python coverage_probe.py --names-file my_names.txt   # one metabolite name/line
```

## Files

- [`chebi.py`](chebi.py) — OLS4 ChEBI client; `protonation_family()` walks
  `is_protonated_form_of` / `is_deprotonated_form_of` (charge-filtered).
- [`rhea.py`](rhea.py) — Rhea reaction→participant index + `rhea2go` GO mapping,
  both fetched live (Rhea REST, GO external2go).
- [`coverage_probe.py`](coverage_probe.py) — orchestration + RESULTS.md writer.
- [`fetch_metabolights.py`](fetch_metabolights.py) — pull any MetaboLights
  accession's curated ChEBI metabolites from its MAF into `studies/<ACC>.chebi.txt`.
- `studies/` — per-study inputs + generated results (committed).
- `.cache/` — on-disk cache of all API responses (gitignored; delete to refresh).

Everything is computed live; nothing is hardcoded. With no network the scripts
fail loudly rather than fabricate numbers.
