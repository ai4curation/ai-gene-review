---
title: "Hypochlorous acid process term obsoletion"
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

# Hypochlorous acid process term obsoletion

GO:0002148, GO:0002149, GO:0002150: all three now obsolete

<span class="small">AI Gene Review · projects/HYPOCHLOROUS_ACID_OBSOLETION · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- GO **obsoleted all three HOCl process terms**; the two children because each "represents a MF term".
- Only **one experimental row** is affected: mouse **Mpo** IMP (PMID:10085024), plus a rat ISO copy.
- **Scoped, not yet started:** Mpo is not reviewed here, and the MF anchor an earlier draft proposed (**GO:0140825**) is *lactoperoxidase activity* in OLS, so it must not be used; the right MF is still to be found.

---

## Where HOCl comes from

![h:470](hocl-burst.svg)

---

## The three terms

![h:480](term-map.svg)

---

## Why the terms went

- **GO:0002148** sat under *organic acid metabolic process*; HOCl has no carbon (go-ontology#22891).
- HOCl formation is **one reaction** by one enzyme, so a process term only restates the activity.
- The catabolic term had **no direct protein annotations**.
- No replacement term is named; the Mpo row needs an **MF** decision.

---

## Next steps

1. `just fetch-gene mouse Mpo` and a full review (peroxidase MF, granule CC, defense BP).
2. Find the GO MF term for HOCl-forming peroxidase activity (RHEA:43232) with OLS; do not reuse GO:0140825 without checking.
3. The rat ISO row follows the mouse row; human MPO is optional.

**Upstream:** go-annotation#6404 · go-ontology#22891 · go-ontology#30524
**Read more:** `projects/HYPOCHLOROUS_ACID_OBSOLETION.md`
