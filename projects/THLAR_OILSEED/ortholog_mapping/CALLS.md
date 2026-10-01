---
title: "Pennycress ortholog calls"
species: [THLAR, ARATH]
---

# Pennycress ortholog calls for module exemplars (curator judgment)

These calls interpret the generated tables in `results/` (`orthologs.tsv`, `candidates.tsv`,
`native_exemplars.tsv`; summary in `RESULTS.md`). They are judgments, so they live here rather than
in the generated files. Re-running `find_orthologs.py` regenerates the tables but not this file.

Rules used:

- **1:1 ortholog**: strict reciprocal best hit (forward best pennycress hit maps back to the
  query gene), with a full-length, sensibly sized pennycress gene model. Only these are added
  to the modules as pennycress representative members.
- **Co-ortholog**: one pennycress gene is the best hit of two Arabidopsis paralogs and maps back
  to one of them (Arabidopsis-specific duplication or pennycress loss).
- **Reverse-confirmed candidate**: not the forward best hit, but a top-5 candidate that maps back
  to the query gene. Usually seen when the forward best hit is a fused or truncated gene model.
- **Unresolved**: no top-5 candidate maps back to the query gene.

Forward ranking by score alone is misleading in this proteome: several top hits are fused gene
models (UGT74C1 hit 1 is 1023 aa, AOP2 hit 1 is 631 aa, the PAS2 match is in an 833 aa model
fused to an MSL2-like channel).

## Glucosinolate-myrosinase module

| Step | Arabidopsis | Pennycress call | Entry (locus) | Notes |
|---|---|---|---|---|
| Met deamination | BCAT4 | 1:1 | A0AAU9S298 (TAV2_LOCUS10345) | 82.7% id |
| MAM condensation | MAM1 | 1:1 | A0AAU9RP64 (TAV2_LOCUS6842) | 84.8% id; a second, partial MAM1-like model (TAV2_LOCUS5676, 395 aa) also maps back to MAM1 |
| MAM condensation | MAM3 | unresolved | none | MAM3 maps to the same MAM1-like gene; no MAM3 counterpart found. Fits a seed profile dominated by the C3 (one-cycle) allylglucosinolate, but absence from a gene-model set is not proof of loss |
| IPMI | IIL1 | 1:1 | A0AAU9T4X1 (TAV2_LOCUS24872) | 95.3% id |
| IPMI | SSU3 | co-ortholog | A0AAU9S4C4 (TAV2_LOCUS13090) | single small-subunit gene, maps back to SSU2 (SSU2/SSU3 are Arabidopsis paralogs) |
| IPMDH | IMDH1 | 1:1 | A0AAU9SYX6 (TAV2_LOCUS20462) | 90.9% id |
| Transamination | BCAT3 | 1:1 | A0AAU9SEL1 (TAV2_LOCUS15930) | 88.9% id |
| Aldoxime formation | CYP79F1/F2 | co-ortholog | A0AAU9RCD6 (TAV2_LOCUS3842) | one gene for both Arabidopsis paralogs; maps back to CYP79F1 |
| Aldoxime oxidation | CYP83A1 | 1:1 | A0AAU9TBL5 (TAV2_LOCUS25373) | 86.4% id |
| GSH conjugation | GSTU20 | reverse-confirmed | A0AAU9SK66 (TAV2_LOCUS16515) | 89.4% id; forward best is a longer GSTU22-like model |
| GSH conjugation | GSTF11 | reverse-confirmed | A0AAU9S6N1 (TAV2_LOCUS9948) | 83.1% id |
| GGP1 | GGP1 | 1:1 | A0AAU9T3M3 (TAV2_LOCUS24348) | 88.8% id |
| C-S lyase | SUR1 | 1:1 | A0AAU9RX80 (TAV2_LOCUS11381) | 90.9% id |
| S-glucosylation | UGT74C1 | reverse-confirmed | A0AAU9S7H8 (TAV2_LOCUS13692) | 82.5% id over 71% of the query; 327 aa model looks truncated |
| Sulfation | SOT17 | 1:1 | A0AAU9RDZ2 (TAV2_LOCUS415) | 91.9% id |
| Sulfation | SOT18 | one-to-many | TAV2_LOCUS7545, 19075, 7550, 5299 | at least four SOT18-like genes map back to SOT18 |
| S-oxygenation | FMOGS-OX1 | unresolved | none | best hits map back to FMOGS-OX2 and OX5; GS-OX subclade present, OX1 counterpart not resolved |
| Alkenylation | AOP2 | reverse-confirmed | A0AAU9SS97 (TAV2_LOCUS22152) | 68.5% id over 67% of the query; 342 aa model likely partial. Pennycress makes allylglucosinolate, so a functional AOP2 is expected; the gene model needs checking |
| Myrosinase | TGG1 | one-to-many | TAV2_LOCUS12773-12775 (tandem), 3697, 12474 | at least five TGG1-like genes |
| Myrosinase | TGG2 | reverse-confirmed | TAV2_LOCUS5741, 25952 | two candidates map back to TGG2 |
| Specifier | ESP | not an ESP ortholog | A0AAU9T6G1 (TAV2_LOCUS23048) | strict RBH to ESP, but 83.8% identical to pennycress TFP versus 73% to Arabidopsis ESP: a TFP-like paralog |
| Specifier | NSP1 | unresolved | none | best hit maps back to NSP4 |
| Specifier | TFP (pennycress exemplar) | same protein | A0AAU9R9U8 (TAV2_LOCUS671) | 99.4% id to Swiss-Prot G1FNI6; TFP-like paralogs at TAV2_LOCUS676 and 23048 |

## Fatty acid elongation module

| Step | Arabidopsis | Pennycress call | Entry (locus) | Notes |
|---|---|---|---|---|
| KCS condensation | FAE1 | 1:1 | A0AAU9T3A1 (TAV2_LOCUS26079) | same protein as V9XY07 (99.8% id) |
| KCS condensation | CUT1/KCS6 | 1:1 | A0AAU9SM40 (TAV2_LOCUS17730) | 95.8% id |
| Ketoreduction | KCR1 | 1:1 | A0AAU9SJ87 (TAV2_LOCUS16128) | 89.9% id |
| Dehydration | PAS2 | gene-model fusion | TAV2_LOCUS20000 | 94.9% id, but the 833 aa model is fused to an MSL2-like channel, so the reverse search lands on MSL2 |
| Enoyl reduction | ECR | 1:1 | A0AAU9SFC3 (TAV2_LOCUS15241) | 96.1% id |

## Not added to the modules

The CYP79F and CYP83A1 pennycress orthologs (A0AAU9RCD6, A0AAU9TBL5) are 1:1 or co-ortholog calls
but are not listed as module representative members. UniProt assigns them PANTHER families
(PTHR47944:SF19, PTHR47955:SF22) that differ from the families the module uses for the Arabidopsis
proteins (PTHR24298:SF684, PTHR47956:SF11, from PANTHER's Arabidopsis classification). This looks
like a PANTHER version difference between sources, and the module validator requires a
representative member to belong to the declared family, so the family ids are left unchanged and
these two members omitted. Partial, fused, one-to-many and unresolved calls are also omitted.
