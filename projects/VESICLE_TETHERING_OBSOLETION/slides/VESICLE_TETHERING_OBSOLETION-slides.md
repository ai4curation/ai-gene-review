---
title: "Vesicle tethering subtree obsoletion"
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

# Vesicle tethering subtree obsoletion

GO:0099022 and 4 children → MF GO:7770062 vesicle membrane tethering activity

<span class="small">AI Gene Review · projects/VESICLE_TETHERING_OBSOLETION · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- GO **obsoleted vesicle tethering** (5 process terms) and minted **GO:7770062** vesicle membrane tethering activity.
- **8 TRAPP reviews** already MODIFY their obsolete GO:0099022 row to GO:0006888 ER to Golgi transport.
- **TMF1 fixed in #3237 (open):** its MF moves to **GO:7770062**, and the obsolete GO:0099041 row, core BP and new-term request are removed.

---

## Tethering is the first contact

![h:480](vesicle-steps.svg)

---

## Why tethering became a function

- Upstream: the terms **represent a molecular function**, the bridging of vesicle and target membranes.
- Obsoleted: GO:0099022, **GO:0099041** to Golgi, GO:0099044 to ER, GO:0090522 exocytosis, GO:0099069 synaptic exocytosis.
- Pattern (ValWood): **MF part_of the transport BP**, e.g. GO:7770062 part_of GO:0006888.
- InterPro removed the exocyst mappings (IPR007225, IPR039682) and 2 UniRules to GO:0090522; IPR028280 → GO:0099041 was flagged too.

---

## Who holds the rows

![h:470](groups.svg)

---

## What changed in this repo

![h:480](repo-outcomes.svg)

---

## Next steps

1. Merge **#3237** (TMF1 and USO1 → **GO:7770062**).
2. New reviews: **EXOC4, EXOC6** (exocyst; InterPro-flagged), then golgins **TRIP11, GOLGA5, GORAB**.
3. Keep wording consistent with the docking trackers; EXOC4 is shared, host it once.

**Siblings:** `VESICLE_DOCKING_OBSOLETION` (#6379) · `SYNAPTIC_VESICLE_DOCKING_OBSOLETION` (#6415) · `VESICLE_TARGETING_OBSOLETION` (#6424)
**Upstream:** go-annotation#6375 · go-ontology#31868, #31871, #31872, #31881
