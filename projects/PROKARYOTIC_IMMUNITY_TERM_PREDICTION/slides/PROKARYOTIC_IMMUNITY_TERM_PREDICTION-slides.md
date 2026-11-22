---
title: "Prokaryotic immunity term prediction (scoping)"
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section { font-family: "Source Sans 3", "Helvetica Neue", Arial, sans-serif; font-size: 26px; color: #15201e; background: #f4f7f6; padding: 56px 64px; }
  h1, h2 { font-family: "Literata", Georgia, serif; color: #0e6b66; font-weight: 600; }
  h1 { font-size: 46px; } h2 { font-size: 34px; margin-bottom: 18px; }
  strong { color: #0e6b66; }
  code { font-family: "IBM Plex Mono", Menlo, monospace; font-size: .85em; background: #e3ece9; padding: 0 .25em; border-radius: 3px; }
  table { font-size: 19px; border-collapse: collapse; } th { background: #dcefec; } td, th { padding: 4px 10px; }
  img { border-radius: 4px; }
  section.lead { justify-content: center; }
  section.lead h1 { font-size: 54px; }
  section.bluf { background: #0e6b66; color: #f4f7f6; }
  section.bluf h2, section.bluf strong { color: #ffffff; }
  section.bluf code { background: rgba(255,255,255,.18); color: #ffffff; }
  footer, header { color: #56655f; font-size: 14px; }
  .small { font-size: 18px; color: #56655f; }
  .cols { display: grid; grid-template-columns: 1fr 1fr; gap: 28px; align-items: start; }
---

<!-- _class: lead -->

# Prokaryotic immunity term prediction

From anti-phage family calls to review-ready GO suggestions

<span class="small">AI Gene Review · projects/PROKARYOTIC_IMMUNITY_TERM_PREDICTION · scoping</span>

---

<!-- _class: bluf -->

## Bottom line

- **Scoped, first unit built:** a registry that maps defense-family calls to stable IDs and a per-family GO policy.
- **Conservative:** only CRISPR-Cas (GO:0099048) and restriction-modification (GO:0009307) map automatically; abortive infection, CBASS and Thoeris are **review-only**.
- **Not connected yet:** no predictor or export code calls the layer.

---

## Why a separate layer

![h:470](defense-go-why.svg)

---

## How it works

![h:470](defense-go-flow.svg)

---

## Status and next steps

- ✅ `defense_go` package, versioned `registry.yaml`, alias conflict detection, 5 tests (April 2026).
- ⬜ Wire into the prokaryotic immunity predictor branch.
- ⬜ Export suggestions as `PredictionReview` YAML.
- ⬜ More families and GO policies; evidence-code and provenance payloads.

**Read more:** `projects/PROKARYOTIC_IMMUNITY_TERM_PREDICTION.md` · `src/ai_gene_review/defense_go/` · `tests/test_defense_go.py`
