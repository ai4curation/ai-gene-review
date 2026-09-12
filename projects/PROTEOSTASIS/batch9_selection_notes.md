---
title: "Proteostasis Review Batch 9 — Gene Selection"
---

# Proteostasis Review Batch 9 — Gene Selection

Date: 2026-06-14
Branch: `claude/proteostasis-network-genes-o9mnh5`

## Context

Batches 1–8 are complete (`pr-1217`, `2026-06-03`, `2026-06-06`, `2026-06-07`,
`2026-06-07b`, `2026-06-07c`, `2026-06-11`, `2026-06-13`). Batch 8 covered the
**UPS branch** Cullin–RING ligase substrate-recognition & assembly modules
(F-box SCF/CRL1 receptors, CRL4 core, CAND2/GLMN). Batch 9 moves into the
**Autophagy–Lysosome Pathway (ALP) branch**, which is the best-supported PN
branch for row-level reuse (per-row notes and references for ~1001/1003 rows).

## Theme: Selective autophagy cargo recognition

This batch walks the **substrate-selection** machinery of selective autophagy —
the receptors that read ubiquitin/cargo marks and bridge them to the Atg8/LC3
conjugation machinery, the kinase axis that activates those receptors, the
TRIM-family receptors/regulators, and the ubiquitin-tagging E3 ligases that
generate the autophagy signal. It exercises the PN ALP-branch
`Autophagy substrate selection -> {Selective autophagy receptor, Marking
substrates for selective autophagy, Autophagy receptor regulation}` types,
selected from the `ok_for_propagation_to_go` candidate-addition pool with no
prior `*-ai-review.yaml`.

### Selected genes (20)

#### Core selective autophagy receptors (6)
1. `SQSTM1` (p62/sequestosome-1) — prototypical SAR; PB1/ZZ/TB/LIR/KIR/UBA;
   aggrephagy/mitophagy/xenophagy + KEAP1-NRF2 + NF-κB/mTORC1 scaffolding
2. `NBR1` — PB1/ZZ/UBA/LIR receptor; aggrephagy & pexophagy, parallels p62
3. `OPTN` (optineurin) — LIR + UBAN ubiquitin-binding receptor; mitophagy &
   xenophagy; TBK1 partner; ALS/glaucoma
4. `CCDC50` (Ymer) — TBK1-binding K63-polyUb autophagy receptor
5. `NUFIP1` — ribophagy receptor (LIR, binds LC3B) + snoRNP assembly
6. `RETREG2` (FAM134A) — reticulophagy/ER-phagy receptor (RHD + LIR)

#### TBK1 activation axis (3)
7. `TBK1` — Ser/Thr kinase; phosphorylates OPTN/SQSTM1/NDP52 to drive selective
   autophagy + master innate antiviral/IFN kinase
8. `AZI2` (NAP1) — TBK1/IKKε adaptor, positive regulator
9. `TANK` — TBK1/IKKε adaptor/scaffold (IFN induction) + NF-κB restraint

#### TRIM-family receptors/regulators (4)
10. `TRIM5` (TRIM5α) — retroviral-capsid PRR; RING E3; precision-autophagy
11. `TRIM13` (RFP2) — ER-anchored RING E3; ERAD & reticulophagy
12. `TRIM16` — RING-less; galectin-3-interacting lysophagy/aggrephagy receptor
13. `TRIM17` — RING E3; neuronal apoptosis (MCL1) + target-selective autophagy

#### Ubiquitin-tagging E3 ligases feeding selective autophagy (4)
14. `SIAH1` — RING E3; α-synuclein/synphilin; Parkin-independent mitophagy
15. `RNF41` (NRDP1) — RING E3; ErbB3/BIRC6/Parkin/USP8; receptor turnover
16. `RNF166` — RING E3; K29/K33 ubiquitination promoting xenophagy
17. `LRSAM1` — RING + LRR E3; ubiquitinates intracellular bacteria for xenophagy

#### Other selective-autophagy regulators (3)
18. `MEFV` (pyrin/TRIM20) — inflammasome sensor; precision autophagy of
    inflammasome components; FMF
19. `NLRX1` — mitochondrial NLR; TUFM-dependent autophagy + MAVS regulation
20. `MAP1S` — MAP1 family; bridges LC3/LRPPRC to microtubules/mitochondria

### Deferred

`HUWE1` (mega/pleiotropic UPS hub, deferred since batch 6/8) and `DNM1L`,
`MFN1`, `VDAC1`, `USP30`, `MARCHF5`, `MUL1`, `PARL`, `PGAM5`, `TSPO`, `IMMT`,
`TUFM`, `SLC25A4/A5`, `TBC1D15/17`, `RAB26`, `BNIP1`, `SNCAIP`, `HK2`, `SREBF1/2`
and related mitophagy/lysosomal-environment ALP candidates were left for a
dedicated mitophagy/CMA batch.

## Results

All `20` review YAMLs pass schema, term (label + verbatim-quote), and
best-practices validation (`uv run ai-gene-review validate --terms`). Across
`1222` reviewed annotations the action mix was:

| Action | Count |
|--------|------:|
| KEEP_AS_NON_CORE | 690 |
| ACCEPT | 505 |
| MARK_AS_OVER_ANNOTATED | 19 |
| NEW | 5 |
| UNDECIDED | 2 |
| REMOVE | 1 |

### Notable curation calls

- **Receptor MF framing.** The recurring core call is the selective-autophagy
  **cargo-adaptor/receptor** function: ubiquitin binding (UBA/UBAN/ZZ) +
  Atg8/LC3 (LIR) binding bridging cargo to the autophagosome. Bare
  `protein binding` (GO:0005515) — abundant on these hub genes (e.g. ~70 IPI
  entries on each of SQSTM1, OPTN, TBK1) — was uniformly kept **non-core** in
  favor of the informative adaptor/receptor MF (`GO:0030674`,
  `GO:0140036`/`GO:0160247`).
- **RING vs RING-less E3 catalysis.** Genuine catalytic RING E3s (SIAH1, RNF41,
  RNF166, LRSAM1, TRIM5/13/17) kept catalytic `ubiquitin protein ligase
  activity` as core. The **RING-less TRIMs** were handled conservatively:
  `TRIM16` ACCEPTed only the experimentally-supported atypical B-box
  autoubiquitination MF (PMID:22629402) and kept the EC-based IEA copy non-core;
  `MEFV`/pyrin's IBA `ubiquitin protein ligase activity` (no functional RING)
  was MARK_AS_OVER_ANNOTATED as a TRIM-family phylogenetic over-propagation.
- **NEW terms for receptor functions absent from GOA.** Verified via QuickGO and
  added as `NEW`/`proposed_new_terms`: `GO:0034517` ribophagy + `GO:0160247`
  autophagy cargo adaptor activity (NUFIP1, CCDC50), `GO:0035973` aggrephagy +
  `GO:0160247` (NBR1), xenophagy/defense/IFN terms (RNF166), and
  `GO:0010508` positive regulation of autophagy (NLRX1).
- **Disputed-direction regulatory terms left in place but flagged.** NLRX1 IBA
  `negative regulation of NF-κB` and AZI2 ortholog-IEA `negative regulation of
  canonical NF-κB` conflict with the human literature (both can be positive
  regulators); per guardrails these mouse/IBA electronic annotations were
  MARK_AS_OVER_ANNOTATED / kept non-core rather than removed.
- **The single REMOVE** is NBR1 `mitochondrial intermembrane space` (GO:0005758,
  IEA/Ensembl-Compara) — biologically implausible for a cytosolic receptor with
  no mitochondrial import signal.
- **UNDECIDED (2).** NBR1 `signaling receptor complex` (GO:0043235, IDA) and
  RNF41 `small GTPase binding` (GO:0030695, IPI) — experimental annotations
  whose full text could not be verified from the abstract-only cache; deferred
  to curators rather than removed.
- **Citation issues flagged in `reference_review`.** SIAH1 `zinc ion binding`
  IDA cites PMID:11863358 (an APOBEC RNA-editing paper with no SIAH1 mention) —
  marked `WRONG_IDENTIFIER`/`relevance: NONE`; the annotation itself was
  ACCEPTed because zinc binding is independently established (PMID:16085652).

The mega-hub `HUWE1` and the dedicated mitophagy/CMA effector set were left out
of scope for a future batch.
