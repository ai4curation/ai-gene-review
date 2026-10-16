---
title: "KW-1110: remapping a viral TRAF-inhibition keyword"
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

# KW-1110 → GO remapping

"Inhibition of host TRAFs by virus": tracking an upstream keyword-to-GO change

<span class="small">AI Gene Review · projects/KW_1110_TRAF_KW2GO · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- KW-1110 was mapped to **GO:0039527**, now **obsolete**: "TRAF-mediated signal transduction" is not one pathway.
- The mapping now points to **GO:0140476** (suppression of host cytoplasmic PRR signaling via TRAF inhibition), matching parent keyword **KW-1113**.
- **Zero** gene reviews in this repo carry either term or the keyword. Upstream has shipped; nothing to rework.

---

## Why the old term went

![h:470](traf-hub.svg)

---

## Old term → new terms

![h:470](kw1110-remapping.svg)

---

## Status

- Created 2026-07-04 as a **watch-list** entry (blocker: GO:0140476 not yet minted).
- 2026-09-26: OLS resolves GO:0140476; GO:0039527 obsolete; `uniprotkb_kw2go` (2026/07/06) maps KW-1110 → GO:0140476.
- Re-ran `grep` for GO:0039527, GO:0140476, KW-1110 in `genes/`: **no matches**.
- If a TRAF-interfering effector is reviewed later: use GO:0140476 for RLR evidence, GO:0140470 for TLR evidence.

**Upstream:** go-annotation#6470 · go-ontology#29238 · **Read more:** `projects/KW_1110_TRAF_KW2GO.md`
