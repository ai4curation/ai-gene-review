---
title: "Assay to function: which readouts license which GO terms"
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

# Assay to function

Which experimental readouts support a GO annotation, and which inflate it

<span class="small">AI Gene Review · projects/ASSAY_TO_FUNCTION · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- Evidence codes hide **how close a readout is to the gene's own activity**. We catalogued **60 readout classes** and mined the papers behind every PMID-backed reviewed annotation.
- Aligned annotations: molecular readouts **77% MF** (567/738), phenotypic hubs **8% MF** (90/1,087), nearly all of it TF reporters.
- Hub readouts are rarely wrong; they get **demoted to non-core**. Rubric + flagger → **6** rows in 4 genes moved to KEEP_AS_NON_CORE.

---

## The hidden axis

![h:470](readout-chain.svg)

---

## How we measured it

- `mine_readouts.py`: regex catalogue over review prose. **Failed usefully**: curators write synthesis, not methods (CellROX/DCFDA/MitoSOX matched zero reviews).
- `mine_papers.py`: the same catalogue over the **cached publications**, joined to GO aspect and action; 36,660 PMID-backed annotations.
- **Thematic alignment**: keep only rows whose GO term is about the process the readout reports.
- QC on matched strings caught `HyPer`→"hyper-", `ERSE`→"diverse", `MTS`→"MTs", `OCR`→*ocr-2*.

---

## The proximity axis holds across 60 classes

![h:480](mf-share-by-readout.svg)

---

## Correct but peripheral

| Readout (aligned) | Reviewed | ACCEPT | NON_CORE | rm/OA% |
|---|--:|--:|--:|--:|
| Viability / proliferation | 90 | 21 | **58** | 9% |
| Apoptosis / caspase | 63 | 25 | **34** | 3% |
| Mito. membrane potential | 165 | 98 | 20 | **21%** |
| Transcriptional reporter | 207 | 146 | 36 | 7% |
| Autophagy flux | 124 | 80 | 20 | 5% |

<span class="small">First publications pass. Hard removal rates are comparable to molecular controls; the signal is demotion to non-core.</span>

---

## From rubric to edits

- **Rule:** a convergent phenotypic readout licenses at most a BP/CC term, never a regulatory MF, default non-core; promote only for machinery or a signature output.
- **Flagger:** Tier 1 = MF from a hub; Tier 2 = core hub-aligned BP/CC. Current file: **443** candidates (5 + 438).
- **Edits (verified in YAML):** PDGFB GO:0072126 ×2, HMGB1 GO:0007204, mouse Sirt2 GO:0051781, VEGFA GO:0043066 ×2 → KEEP_AS_NON_CORE.
- IL21 GO:0042102 → KEEP_AS_NON_CORE after an OpenScientist run (#1558); STAT3 GO:0030335 ×2 still **UNDECIDED** (#1422).

---

## What re-review taught us

1. All 7 original Tier-1 flags were **defensible**: binding MF is direct evidence (Calm2, HRC), and coregulator MF is fine for real coregulators.
2. Almost every standing-ACCEPT Tier-2 flag was **machinery** (CDK1, RB1, BRCA1, PSMA1) or a **signature output** (VEGFA → angiogenesis).
3. The flagger's value is on **unreviewed** annotations, not re-litigating accepted core calls.

---

## Status and next steps

- ✅ 60-class catalogue, rubric (`RUBRIC.md`, `rubric.yaml`), flagger, 6 edits. Mature.
- ⬜ Curator triage of `flagged_candidates.tsv`, starting with `indirect_ligand`.
- ⬜ Generalise the machinery discriminator beyond signalling ligands.
- ⬜ Decide STAT3 migration (#1422).

**Read more:** `projects/ASSAY_TO_FUNCTION.md` · `projects/ASSAY_TO_FUNCTION/RUBRIC.md` · `reports/catalog_table.md`
