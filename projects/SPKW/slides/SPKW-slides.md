---
title: "SPKW: what UniProt keyword mappings got right and wrong"
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

# SwissProt keyword (SPKW) annotations

A retrospective audit of GO_REF:0000043, where a UniProt keyword was the only source

<span class="small">AI Gene Review · projects/SPKW · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- **Eukaryotic process keywords were unsafe**: 79–100% of reviewed SPKW-only apoptosis, autophagy, rhythm and *S. pombe* meiosis rows were over-annotations.
- **Bacterial keyword rows were mostly sound**; plant SPKW-unique terms carried real risk in only **~15%** of cases.
- GOA **retired SPKW for cellular organisms (~April 2026)**. That removed the bad rows and also correct ones, e.g. DELLA GA signalling (RHT1), patatin storage (PATB1).

---

## What we asked

- A keyword such as *Apoptosis* maps to a GO term via `GO_REF:0000043`. For many genes it was the **only** evidence.
- Closure filter: a row counts only if **no other source** supports that term **or a more specific one**.
- 12 downstream subprojects: human apoptosis / rhythm / autophagy; *S. pombe*, *Drosophila*, *Anopheles*, *P. putida*, *Arabidopsis*; phage T4, *E. coli* O157, virus clades; non-Arabidopsis plants.
- Swiss-Prot keywords are **manually assigned**, so errors in reviewed organisms sit in the **keyword→GO mapping**, not keyword choice.

---

## Issue rates by subproject

![h:470](spkw-issue-rates.svg)

---

## One keyword, several verdicts

![h:470](spkw-position-verdicts.svg)

---

## Recurring failure patterns

| Pattern | Example |
|---|---|
| Regulatory conflation | AIMP2 → apoptotic process (MODIFY) |
| Caspase substrate ≠ apoptosis | AIMP1, BCAP31 (over-annotated) |
| Process conflation | *S. pombe* ATG genes → meiosis |
| Eukaryote-centric terms on phage | T4 DAM → innate immune response |
| Enzyme-class keyword → bare process | Methyltransferase → methylation (plant MTases) |
| Expression ≠ function | rhythmic-process genes; ENOD2A nodulation |

---

## The repository-wide picture

![h:470](spkw-repo-actions.svg)

<span class="small">All SPKW rows reviewed anywhere in this repo, not only this project. Nearly half were accepted as they stand.</span>

---

## What retirement cost

- Plants: 214 SPKW-unique terms tiered. **Tier A (over-annotation risk) 15%**; **Tier B+C (correct) ~79%**.
- Correct facts lost where the keyword was the only carrier: **RHT1** GA signalling, **PATB1** nutrient reservoir, **NSP1** nodulation, EME1 endonuclease, PR1B1 defense.
- Lesson for any mapping source: tier terms by risk and review by gene position, rather than keep-all or drop-all.

---

## Status

- **Mature** as a retrospective: 12 downstream subprojects, 137 genes in the results table; ViralZone is active upstream follow-up.
- Side finding: 265/550 plant `file:` quotes were non-verbatim because the validator skips `file:` refs; all fixed, no action changes.
- Methods and SQL: `projects/SPKW/SPKW-METHODOLOGY.md`.

**Read more:** `projects/SPKW.md` · `projects/SPKW/SPKW-PLANTS.md` · `projects/SPKW/SPKW-APOPTOSIS.md`
