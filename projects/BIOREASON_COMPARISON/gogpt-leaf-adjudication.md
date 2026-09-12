---
title: GO-GPT leaf predictions — OpenScientist adjudication
---
# OpenScientist adjudication of GO-GPT specific molecular-function predictions

[← back to BioReason-Pro / GO-GPT comparison](../BIOREASON_COMPARISON.md)

## Bottom line

GO-GPT (the upstream ESM2-based predictor whose GO terms feed BioReason-Pro) emits ~6.3k
raw GO predictions across ARGO139, most left at `UNC` in the bulk
[leaf evaluation](gogpt-eval.html). We sampled **7 of its most informative, *specific*
molecular-function leaf calls** — one per gene, spread across kinase, protease, transferase,
lipid-transfer, adaptor, and chaperone functions in five organisms — and re-tested each as an
**independent, blinded gene-function hypothesis** with an OpenScientist agent (structure +
comparative genomics; the suspected answer withheld from the prompt).

**Not one was a genuinely-novel correct prediction (0/7 `COR`).** Every GO-GPT leaf call in the
sample is a *mirror of GOA*:

- **The 4 correct calls all re-derive an annotation GOA already has** — either exactly (2 ×
  `CNN`, Correct-but-Not-Novel: the term is already in GOA with IMP/IDA) or as a coarse parent of
  an existing, more specific curated child (2 × `LSP`, Less-Specific-than-existing).
- **The 3 wrong calls are `NPI`** (refuted). Two reproduce an *anomalous* existing GOA annotation
  (an inverted kinase-**inhibitor** call, and a lone rat-specific adaptor IDA that is really a
  different subunit's function) → `TRAINING_DATA_CONTAMINATION`. The third is the only call that
  ventures *beyond* GOA — and it is wrong: it hands one complex subunit's catalytic chemistry to a
  non-catalytic sister subunit → a subunit-level misassignment (`FREQUENCY_BIAS`).

So where GOA is right, GO-GPT recovers it (at equal or coarser resolution); where GOA is wrong,
GO-GPT recapitulates the error; and the one time it proposes something *not* in GOA, it over-generalizes
from complex/family context. This is exactly what you expect from a model trained to reproduce
curated annotations: it adds **no new correct molecular-function biology** at the leaf level in this
sample, and it is not a safe source of *novel* specific-function hypotheses.

The recurring failure mode worth flagging for downstream users is **subunit-level misattribution** —
assigning a protein-complex's catalytic (or scaffolding) function to the wrong member (Prkaa2 α2 vs β;
gaa1 vs Gpi8). Both look confidently specific and both are wrong. The schema has no dedicated
`error_type` for this pattern, so it is recorded as the closest available bucket (`FREQUENCY_BIAS` for
gaa1's novel misassignment; `TRAINING_DATA_CONTAMINATION` for Prkaa2, whose term is already in GOA).
Because it recurs, a dedicated `COMPLEX_CONTEXT_MISATTRIBUTION` (sibling-subunit) error type would be a
reasonable schema follow-up.

## The sample

| Gene (accession) | GO-GPT MF leaf call | Verdict | Assessment | Why |
|---|---|---|---|---|
| ECOLI/Spy (P77754) | protein folding chaperone (GO:0044183) | Correct, redundant | **`CNN`** | Founding member of the Spy/CpxP chaperone family; ATP-independent holdase+foldase. **Already in GOA as IDA.** Recovers established knowledge. |
| BACSU/spoIIGA (P13801) | aspartic-type endopeptidase (GO:0004190) | Correct, redundant | **`CNN`** | Pro-σE processing protease; Asp183 in a D-S-G motif, dimerizes like HIV-1 protease. **Already in GOA as IMP** (PMID:18378688). Divergent retropepsin fold is a nuance, not an error. |
| SCHPO/atg2 (O94649) | lipid transfer activity (GO:0120013) | Correct, over-general | **`LSP`** | Founding Atg2 bridge-like LTP; the *S. pombe* ortholog established the activity (Osawa 2019). But GO:0120013 is a **parent** of PomBase's curated children GO:0120014 / GO:0140344. Coarser than existing curation. |
| worm/ire-1 (Q09499) | hydrolase, acting on ester bonds (GO:0016788) | Correct, over-general | **`LSP`** | Its endoribonuclease cleaves xbp-1 mRNA phosphodiester bonds — so GO:0016788 is a true but **high-level parent** of the curated child GO:0004521 (RNA endonuclease, IMP). Redundant. |
| rat/Akt1 (P47196) | protein serine/threonine kinase **inhibitor** activity (GO:0030291) | Refuted | **`NPI`** | rat/Akt1 is an active kinase, not a kinase *inhibitor*. The call **reproduces an inverted existing GOA annotation** rather than novel biology. → `TRAINING_DATA_CONTAMINATION` |
| rat/Prkaa2 (Q09137) | protein-macromolecule adaptor activity (GO:0030674) | Refuted | **`NPI`** | Prkaa2 is the AMPK α2 **catalytic** subunit (Ser/Thr kinase); the adaptor/scaffold role belongs to the **β** subunit. The call reproduces a **lone rat IDA** (PMID:15695819, itself a β-subunit paper) absent from ortholog and all paralogs. → `TRAINING_DATA_CONTAMINATION` |
| SCHPO/gaa1 (Q9US48) | cysteine-type endopeptidase activity (GO:0004197) | Refuted | **`NPI`** | gaa1 is the **non-catalytic** GPI-transamidase subunit; the catalytic cysteine protease is **Gpi8/PIG-K** (Cys-His-Asn triad; cryo-EM PMID:35165458/41085069). **Not in GOA** — the one *novel* call, and it is a subunit misassignment. → `FREQUENCY_BIAS` |

Full reports live under each gene's `*-hypotheses/<slug>/openscientist.md`.

### Relationship to the deterministic benchmark

This page is an **independent expert-adjudication overlay** on the automated GO-GPT leaf benchmark;
it does **not** rewrite the committed `*-gogpt-leaf-predictions.yaml` files. That benchmark scores each
prediction *deterministically* by exact-matching the GO-GPT term against the current local AIGR
review's action (`ACCEPT`→`CNN`, `REMOVE`→`NPI`, …), and leaves terms with no matching action as
`UNC` pending. The two layers are consistent:

- For the **4 terms the benchmark already resolves**, our blinded verdict **agrees** with its
  deterministic call — Spy/spoIIGA `CNN` (the local review `ACCEPT`s them) and rat/Akt1, rat/Prkaa2 `NPI` (the
  local review `REMOVE`s them). We add the *biological mechanism* and OpenScientist evidence behind
  each.
- For the **3 terms the benchmark leaves `UNC`** (gaa1 GO:0004197, atg2 GO:0120013, ire-1 GO:0016788 —
  no matching action, in gaa1's case because the term is not in the local review at all), our
  adjudication supplies the expert resolution (`NPI`, `LSP`, `LSP`).

These three resolutions are candidates to fold back into the benchmark as a follow-up — by recording
the corresponding action in each gene's local `*-ai-review.yaml` and re-running the deterministic
scorer + `just stats`, so the benchmark's counts stay self-consistent.

## Scoring

de Crécy-Lagard prediction scores (CS): `CNN`/`LSP` = 2, `NPI` = 0. Sample mean CS ≈ **1.1**.
Distribution: **3 `NPI` · 2 `CNN` · 2 `LSP` · 0 `COR`**.

## Method & scope

- One informative, *specific* MF leaf term per gene was chosen (broad parents like "cellular
  metabolic process" were skipped as uninformative). Genes were picked to span functional classes
  and organisms, not at random, so this is a **qualitative probe of the specific-MF tail**, not an
  unbiased accuracy estimate over all 6.3k predictions.
- Each hypothesis was phrased neutrally ("assess whether G has function F, or whether …"), with the
  competing interpretation stated so the agent could resolve either way. Local
  `*-bioinformatics/RESULTS.md` holdout evidence was not fed to the agent.
- The finding — GO-GPT specific-MF calls mirror GOA and add no novel correct biology at the leaf
  level — is consistent across all seven and with the main evaluation's conclusion that the pipeline
  "restates what existing annotations already say."
