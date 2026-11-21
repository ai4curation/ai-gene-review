# Expanded DeepTMHMM2 results — 2026-11-05

Ran **31 canonical human proteins** (29 newly run locally plus the original SPTLC2/DPM1 controls), totaling **16,266 residues**, from **110 to 1938 aa**. The panel combines all 23 audited S20 cases with eight additional controls selected before inference. This is a selected sanity-check panel, not an unbiased or training-independent accuracy estimate.

## Cost on this workstation

Apple M1 Max, 64 GiB RAM, CPU only, eight threads; PyTorch 2.10.0 and DeepTMHMM2 predictor 0.1.0 at commit `526f6c60f93c0868c7315413da8e669d12373cc3`. Both runs used the full five-member ensemble and cached weights. Inference processes ran sequentially.

| Measurement | Observed |
|---|---|
| API pass 1, 31 proteins | 49.70 s inference |
| API pass 2, 31 proteins | 49.30 s inference |
| API process, two passes including startup/export | 110.58 s |
| API peak RSS | 5.24 GiB |
| Unmodified CLI, one pass including startup/export | 183.80 s |
| CLI peak RSS | 4.99 GiB |
| API imports / cached model load | 4.02 s / 6.38 s |

API timings include fresh ESM embeddings for every sequence and repeat, but exclude output serialization. The API uses the previously documented singleton-unbatching adapter. The unmodified CLI uses batch size 1. The paths have different execution policies: the CLI wraps task-model inference in CPU autocast, while the API does not. The observed speed difference is reported separately; the full-panel timing comparison alone does not isolate its cause. Peak RSS is cumulative within each process, not an estimate per protein.

The longest input, ATG2A (1,938 aa), took **6.161;5.461 s** in the two API runs. Long proteins were not truncated: every returned topology covers the full input. The pinned embedding implementation chunks inputs beyond 1,022 residues; ATG2A, CFTR and EGFR exercise that path. Successful execution does not establish preservation of biological information across chunk boundaries.

These measurements support inexpensive local panels. A naive 20,000-protein scaling of this selected panel's average API time is approximately 8.9 wall-clock hours on this CPU configuration with the model already loaded. That is arithmetic, not a measured human-proteome runtime: sequence composition, long proteins beyond this panel, batching and machine load could change it substantially. No proteome-wide job was launched.

## Reproduction and software checks

- **31/31** agree exactly between API repeats.
- **28/31** agree between API and the unmodified CLI after normalizing their different JSON segment representations. The comparison includes the complete topology string, segment boundaries, protein type, membrane labels and exported scores rounded to two decimal places.
- **23/23** reproduce the S20 IF/RE, signal and transit-peptide coordinates exactly. Generic compartment-label text is excluded from this comparison. The source table has no sequence hashes, so this is coordinate reproduction rather than proof of identical author input sequences.
- CLI-exported sequences match our input hashes, all input taxa are human, and all topology lengths and segment coverage checks pass.

The broad protein class and selected membrane labels agree for all 31 proteins, and complete topology strings agree for 29/31. Three exported outputs differ:

| Gene | Default API | Unmodified CLI |
|---|---|---|
| COQ5 | IF258–272 | IF255–272 |
| TOMM40 | One beta strand begins at 188 | The same strand begins at 189; still 19 strands |
| SPTLC1 | ER score 0.72 | ER score 0.71; same selected location and topology |

A controlled rerun of just these three proteins enabled CPU autocast only around the API task models, leaving ESM embedding generation unchanged. **All three then matched the CLI exactly**, including the exported scores. This isolates task-model precision as sufficient to reproduce these observed differences; it does not establish which residue boundary is biologically correct. The default API matches all 23 S20 feature predictions; the CLI matches 22/23 because of COQ5. See `api_cli_differences.json`, `precision/` and the `just precision` recipe.

Reproduction of S20 includes its known biological failures; agreement with a published prediction is not validation of that prediction.

## Additional controls

| Gene | Prediction | Interpretation against existing sources |
|---|---|---|
| EGFR | Signal 1–24; TM 644–668; plasma, endosome, vesicle and lysosome membrane labels | Broad architecture and primary membrane location agree. The extra labels require separate trafficking/context evidence. |
| CFTR | 12 TM helices; plasma and endosome membrane labels; IF70–74 and IF846–854 | Recovers the 12-pass channel architecture. IF calls and additional compartments are not independent functional discoveries. |
| TOMM40 | 19 beta strands; mitochondrial outer membrane | Recovers the expected beta-barrel architecture and membrane class. |
| COX4I1 | Transit peptide 1–22; TM101–121; mitochondrial inner membrane | Recovers targeting plus a single inner-membrane helix. |
| SPTLC1 | One TM at 26–36; ER membrane | Correct broad class, but the span is only 11 residues versus UniProt's 16–36 segment. Do not treat exact endpoints as established. |
| CALR | Signal 1–17; no TM; no membrane-type assignment | Compatible with a soluble ER-luminal protein. Generic `outside` does not mean extracellular secretion. |
| INS | Signal 1–24; no TM; no membrane-type assignment | Compatible with entry of the full preproinsulin precursor into the secretory pathway. Mature hormone cleavage/processing is not modeled. |
| GAPDH | Globular; no IF/RE/TM; no membrane-type assignment | Compatible with the soluble enzyme; this does not exclude transient or regulated membrane interactions. |

Expected properties come from the existing gene reviews and cached UniProt features. Input-source paths, feature coordinates and hashes are in `inputs.tsv`; the original source files were not edited. Exact residue-boundary accuracy was not scored against structures.

## What the expanded run changes in our assessment

**Useful for topology screening:** the controls recover several distinct architectures, and the candidate panel reproduces the interfacial/reentrant calls that led us to the earlier literature-backed corrections. A contrasting pair is SPTLC1, which is called transmembrane/ER, and SPTLC2, which is called non-spanning with IF72–87.

**Insufficient for automatic localization:** 26 of 31 outputs have no membrane-type assignment because the software suppresses those assignments for non-TM proteins. That includes the membrane-associated S20 candidates and both CALR and INS. A transit-peptide or signal-peptide call alone cannot determine a precise compartment or distinguish ER retention from secretion. LPCAT1 again receives a five-residue transit-peptide call despite its established ER/lipid-droplet biology.

**Established topology can be missed:** TOMM22, SUN2 and CYP46A1 again receive non-spanning predictions. Retain their independently supported topology. ADCK2, LPCAT4 and RDH5 remain unresolved candidates; repeated deterministic predictions are not independent biological evidence.

**No new molecular-function claim follows:** membrane geometry can constrain a mechanistic interpretation but does not identify catalytic specificity, substrate, or physiological process. This run adds computational evidence and performance measurements; it does not introduce new GO annotations or revise the curated reviews.

## Per-protein output

Coordinates are one-based and inclusive. `seconds` is the median of two API measurements. The complete named segments, including predicted sidedness, and both timings are in [summary.tsv](summary.tsv). Raw outputs are in `api/` and `cli/`.

| Gene | Length | Type | Predicted IF/RE/SP/TP/TM features | Seconds |
|---|---:|---|---|---:|
| ACSL4 | 711 | Globular | interfacial(10-31) | 2.565 |
| ADCK2 | 626 | Globular + TP | transit_peptide(1-72);interfacial(97-120);interfacial(129-139) | 1.963 |
| ATG2A | 1938 | Globular | reentrant(1894-1902) | 5.811 |
| CALR | 417 | Globular + SP | signal(1-17) | 1.199 |
| CFTR | 1480 | Alpha TM | 12 TM helices; IF70–74; IF846–854 | 4.691 |
| COQ5 | 327 | Globular + TP | transit_peptide(1-43);interfacial(258-272) | 1.28 |
| COQ7 | 217 | Globular + TP | transit_peptide(1-35);interfacial(118-125);interfacial(198-214) | 0.589 |
| COQ8B | 544 | Globular + TP | transit_peptide(1-45);interfacial(93-114) | 1.596 |
| COX4I1 | 169 | Alpha TM + TP | transit_peptide(1-22);TMhelix(101-121) | 0.597 |
| CYP46A1 | 500 | Globular | interfacial(6-17) | 1.545 |
| DHRS3 | 302 | Globular | interfacial(7-26) | 0.851 |
| DPM1 | 260 | Globular | interfacial(160-175);interfacial(246-259) | 0.659 |
| EGFR | 1210 | Alpha TM + SP | signal(1-24);TMhelix(644-668) | 3.38 |
| GAPDH | 335 | Globular | None | 0.854 |
| GPAM | 828 | Globular | interfacial(378-383) | 2.251 |
| INS | 110 | Globular + SP | signal(1-24) | 0.477 |
| LPCAT1 | 534 | Globular + TP | transit_peptide(1-5);interfacial(41-66);interfacial(98-110);interfacial(255-261) | 1.562 |
| LPCAT4 | 524 | Globular | interfacial(34-60);interfacial(88-105);interfacial(250-258) | 1.502 |
| NDUFA12 | 145 | Globular | interfacial(7-15);interfacial(21-28) | 0.623 |
| PKMYT1 | 499 | Globular | interfacial(387-397) | 1.595 |
| PNPLA2 | 504 | Globular | interfacial(345-354) | 1.612 |
| PNPLA3 | 481 | Globular | interfacial(218-222) | 1.604 |
| RDH5 | 318 | Globular | interfacial(5-18);interfacial(289-297) | 0.976 |
| SPRY1 | 319 | Globular | reentrant(257-275) | 1.074 |
| SPRY2 | 315 | Globular | reentrant(252-272) | 1.078 |
| SPTLC1 | 473 | Alpha TM | TMhelix(26-36) | 1.559 |
| SPTLC2 | 562 | Globular | interfacial(72-87) | 1.524 |
| STOML1 | 398 | Globular | interfacial(57-70) | 1.042 |
| SUN2 | 717 | Globular | interfacial(198-203) | 2.049 |
| TOMM22 | 142 | Globular | interfacial(48-84) | 0.491 |
| TOMM40 | 361 | Beta Barrel | 19 beta strands (see raw output) | 0.9 |

## Reproducibility checklist

- [x] Preparation, inference and comparison scripts take explicit input/output arguments.
- [x] Exercised on 31 proteins spanning 110–1,938 residues and several topology classes.
- [x] Both API repeats and the unmodified CLI completed successfully.
- [x] Raw predictions, sequence hashes, timings, resource logs and source/checkpoint provenance retained.
- [x] Full-length coverage, repeat consistency and API/CLI agreement checked.
- [x] Biological interpretation distinguishes model reproduction from experimental evidence.

Training exclusion, population-level accuracy and whole-proteome CPU cost were not established. These limits do not invalidate the measured executions or source comparisons. See [README.md](README.md) for exact rerun commands and [the preceding audit](../../../../../../projects/DEEPTMHMM2.md) for primary-literature adjudication of the 23 S20 genes.
