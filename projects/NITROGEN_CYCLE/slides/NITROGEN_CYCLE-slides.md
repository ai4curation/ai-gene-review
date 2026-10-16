---
title: "Nitrogen cycle module: scoping"
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

# The nitrogen cycle

Scoping a multi-organism review of the microbial nitrogen-cycle enzymes

<span class="small">AI Gene Review · projects/NITROGEN_CYCLE · scoping</span>

---

<!-- _class: bluf -->

## Bottom line

- **Scoped, no gene reviews started.** The cycle's dissimilatory steps are almost all bacterial or archaeal.
- We chose **27 reviewed Swiss-Prot marker enzymes** across seven arms, plus `nxrA`, which has no reviewed entry.
- A taxon-neutral **module** (`modules/nitrogen_cycle.yaml`, DRAFT) is built; it gives the specific pathway terms that annotations on **GO:0071941** should move to.

---

## The cycle and its markers

![h:500](nitrogen-cycle.svg)

---

## Candidate genes by arm

| Arm | Markers | Model organisms |
|---|---|---|
| Fixation | nifH, nifD, nifK | *K. pneumoniae*, *A. vinelandii* |
| Nitrification | amoA/B/C, hao, cycA; nxrA (no Swiss-Prot) | *N. europaea* |
| Denitrification | narG, napA, nirS, nirK, norB, norC, nosZ | *E. coli*, *P. aeruginosa*, *P. denitrificans* ... |
| DNRA | nrfA | *E. coli* |
| Anammox | hzsA, hzsB, hzsG, hdh | *K. stuttgartiensis* |
| Assimilation | narB, nasA, nirA, nirB, glnA, gltB | *S. elongatus*, *E. coli*, *K. oxytoca* |
| Ammonification | ureC | *K. aerogenes* |

<span class="small">nirS and nirK are convergent solutions to the same NO₂⁻ → NO step; reviewing both makes the either/or distribution explicit.</span>

---

## The draft module

![h:440](nitrogen-cycle-module-page.jpg)

<span class="small">pages/modules/nitrogen_cycle.html: one part per arm, variant sets for convergent enzymes, Swiss-Prot exemplars as grounding.</span>

---

## Status and next steps

- ✅ Marker set chosen and accessions verified (2026-06-20); module drafted.
- ⬜ Resolve an accession for NOB nitrite oxidoreductase (`nxrA`).
- ⬜ `just fetch-gene` each marker under its species code (e.g. NITEU, PARDE, KUEST) and review.
- ⬜ Log any GO:0071941 rows found to the companion obsoletion project.

**Read more:** `projects/NITROGEN_CYCLE.md` · `modules/nitrogen_cycle.yaml` · `projects/NITROGEN_CYCLE_OBSOLETION.md`
