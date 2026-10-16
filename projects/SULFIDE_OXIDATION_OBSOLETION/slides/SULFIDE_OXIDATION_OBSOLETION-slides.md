---
title: "Sulfide oxidation children obsoletion"
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

# Sulfide oxidation children obsoletion

GO:0070221 · GO:0070222 · GO:0070223 → GO:0019418 sulfide oxidation

<span class="small">AI Gene Review · projects/SULFIDE_OXIDATION_OBSOLETION · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- GO **obsoleted three enzyme-specific children** of sulfide oxidation; all three ontology PRs are **merged**.
- Only **GO:0070221** (via SQOR) had annotations: human SQOR (IDA), TSTD1 (TAS), SLC25A10 (TAS), plus rodent Sqor ISO/ISS.
- **Partly done:** SLC25A10 is now reviewed (row on GO:0019418, over-annotated); **SQOR and TSTD1 are unreviewed**.

---

## Three children collapse into the parent

![h:480](term-map.svg)

---

## Why the children went

- Each child named **the enzyme that does the oxidation**, which is more specific than any gene product needs.
- **GO:0070222** and **GO:0070223** had **zero** direct annotations.
- The mechanism stays expressible through the MF, e.g. **GO:0070224** sulfide:quinone oxidoreductase activity.
- Upstream cleanup: InterPro dropped **IPR042457 → GO:0070221**; Reactome migrated its 2 rows; IBA rows follow PAINT.

---

## Who does the oxidising

![h:480](pathway.svg)

---

## State in this repo

| Gene | Former row / current state | Current review state |
|---|---|---|
| SQOR (Q9Y6N5) | IDA + IBA | none |
| TSTD1 (Q8NFU3) | TAS + IEA | none |
| SLC25A10 (Q9UBX3) | TAS, now on GO:0019418 (Reactome) | `genes/human/SLC25A10`: MARK_AS_OVER_ANNOTATED |

<span class="small">SLC25A10 was reviewed in the mitochondrial carrier work (#2093), after this page was written. The carrier exchanges sulfate and thiosulfate for phosphate; it does not oxidise sulfide.</span>

---

## Next steps

1. `just fetch-gene human SQOR`: anchor MF on GO:0070224 and BP on GO:0019418; SQOR deficiency makes it clinically relevant.
2. Then **TSTD1**: is GO:0019418 right for a thiosulfate sulfurtransferase, or was the TAS weak?
3. Leave S. pombe hmt2 and bacterial homologs to IBA remapping.

**Upstream:** go-annotation#6388 (closed) · go-ontology#31842 (closed) · PRs #31949, #32025, #32068 (merged)

**Read more:** `projects/SULFIDE_OXIDATION_OBSOLETION.md`
