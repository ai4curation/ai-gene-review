---
title: "ICAM-3 receptor activity obsoletion"
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

# ICAM-3 receptor activity obsoletion

GO:0030369 → GO:0004888 + `has_input` ICAM3

<span class="small">AI Gene Review · projects/ICAM3_RECEPTOR_ACTIVITY_OBSOLETION · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- GO **obsoleted GO:0030369** because ICAM3 binds several unrelated receptors; one ligand-named term fits none of them precisely.
- **3 human rows** move to **GO:0004888** with the ligand as an extension: ITGAL, ITGB2 (IMP) and CLEC4M (NAS); ~155 IEA rows follow.
- **Scoped, not yet started:** none of these genes is reviewed here; CLEC4M's NAS row is the one to question.

---

## One ligand, unrelated receptors

![h:470](icam3-receptors.svg)

---

## Old term → proposed home

![h:480](term-map.svg)

---

## Why a ligand-named term fails

- Integrins **LFA-1** (ITGAL:ITGB2) and **αD/β2** bind the ICAM3 protein.
- C-type lectins **CLEC4M** and **CD209** bind its high-mannose **glycans**.
- OLS obsoletion note: the term is "more specific than the specificity of any known gene product".
- The receptor activity stays in GO:0004888; `has_input` records the ligand, as in GO-CAM.

---

## Next steps

1. Review **ITGAL** and **ITGB2** together (shared PMID:19029120); LFA-1's core MF is adhesion-molecule binding.
2. Then **CLEC4M**: check whether PMID:11257134 supports an ICAM3 receptor claim; D-mannose binding (GO:0005537) is the likely core.
3. Optional: CD209, ITGAD, ICAM3 itself.

**Upstream:** go-annotation#6442 · go-ontology#30560
**Read more:** `projects/ICAM3_RECEPTOR_ACTIVITY_OBSOLETION.md`
