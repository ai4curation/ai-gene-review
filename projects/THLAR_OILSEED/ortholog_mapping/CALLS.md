---
title: "Pennycress ortholog calls"
species: [THLAR, ARATH]
autolink_gene_symbols: false
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
| MAM condensation | MAM1 | single MAM gene, read as MAM1 ortholog | A0AAU9RP64 (TAV2_LOCUS6842) | 84.8% id. Strictly this is the co-ortholog topology (it is also the best hit of MAM3), as for CYP79F1/F2. It is read as the MAM1 ortholog because it maps back to MAM1 and no MAM3 counterpart exists, which fits the one-turn sinigrin profile. A second, partial MAM1-like model (TAV2_LOCUS5676, 395 aa) also maps back to MAM1 |
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
| Alkenylation | AOP2 | 1:1, gene model wrong | A0AAU9SS97 (TAV2_LOCUS22152) | AOP2-type: 84.1% id to Brassica rapa AOP2 (GSL-ALK). The predicted protein is a fragment, but the genome carries the complete coding sequence (see "AOP2 gene model" below) |
| Myrosinase | TGG1 | one-to-many | TAV2_LOCUS12773-12775 (tandem), 3697, 12474 | at least five TGG1-like genes |
| Myrosinase | TGG2 | reverse-confirmed | TAV2_LOCUS5741, 25952 | two candidates map back to TGG2 |
| Specifier | ESP | not an ESP ortholog | A0AAU9T6G1 (TAV2_LOCUS23048) | strict RBH to ESP, but 83.8% identical to pennycress TFP versus 73% to Arabidopsis ESP: a TFP-like paralog |
| Specifier | NSP1 | unresolved | none | best hit maps back to NSP4 |
| Specifier | TFP (pennycress exemplar) | same protein | A0AAU9R9U8 (TAV2_LOCUS671) | 99.4% id to Swiss-Prot G1FNI6; TFP-like paralogs at TAV2_LOCUS676 and 23048 |

## Fatty acid elongation module

| Step | Arabidopsis | Pennycress call | Entry (locus) | Notes |
|---|---|---|---|---|
| KCS condensation | FAE1 | 1:1 | A0AAU9T3A1 (TAV2_LOCUS26079) | same protein as V9XY07 (99.8% id), which is already the pennycress member in the module, so not added again |
| KCS condensation | CUT1/KCS6 | 1:1 | A0AAU9SM40 (TAV2_LOCUS17730) | 95.8% id; added to the module KCS variant |
| Ketoreduction | KCR1 | 1:1 | A0AAU9SJ87 (TAV2_LOCUS16128) | 89.9% id |
| Dehydration | PAS2 | gene-model fusion | TAV2_LOCUS20000 | 94.9% id, but the 833 aa model is fused to an MSL2-like channel, so the reverse search lands on MSL2 |
| Enoyl reduction | ECR | 1:1 | A0AAU9SFC3 (TAV2_LOCUS15241) | 96.1% id |

## Not added to the modules

Of the 13 one-to-one calls, 11 are module members: the 10 single-copy glucosinolate and elongase
enzymes plus pennycress CUT1/KCS6. The pennycress FAE1 entry (A0AAU9T3A1) is the same protein as
the V9XY07 member already listed. CYP83A1 (and the CYP79F co-ortholog) are omitted for the
reason below.

The CYP79F and CYP83A1 pennycress orthologs (A0AAU9RCD6, A0AAU9TBL5) are 1:1 or co-ortholog calls
but are not listed as module representative members. UniProt assigns them PANTHER families
(PTHR47944:SF19, PTHR47955:SF22) that differ from the families the module uses for the Arabidopsis
proteins (PTHR24298:SF684, PTHR47956:SF11, from PANTHER's Arabidopsis classification). This looks
like a PANTHER version difference between sources, and the module validator requires a
representative member to belong to the declared family, so the family ids are left unchanged and
these two members omitted. Partial, fused, one-to-many and unresolved calls are also omitted.

## AOP2 gene model

Analyses: `aop2_check.py` (output `AOP2_RESULTS.md`) and `aop2_genomic.py` (output
`AOP2_GENOMIC_RESULTS.md`).

- **AOP2-type gene.** TAV2_LOCUS22152 (UniProt A0AAU9SS97, flagged "Fragment") is AOP2-type. It is
  84.1% identical to Brassica rapa AOP2 (GSL-ALK, B5KJ58), compared with 65.6-69.0% to Arabidopsis
  AOP1, AOP2 and AOP3.
- **What the predicted protein misses.** It aligns only to B. rapa residues 3-179 and 318-430. Its
  catalytic 2OG-Fe(II) domain lacks the first 41 positions of the Pfam model (PF03171).
- **The genome has the missing sequence.** Six-frame translation of the locus (OU466862.2,
  chromosome 6) finds three stop-free stretches on the gene's strand. Together they cover B. rapa
  AOP2 residues 3-430: residues 3-122 (85.8% id), residues 123-347 (71.6% id,
  E = 3e-91), and residues 344-430 (80.5% id). The middle stretch
  (60999889-61000710) contains 568 bp that the gene model annotates as intron, mostly a 474 bp
  "intron" at 61000111-61000584. That stretch encodes the residues the predicted protein lacks.
- **Conclusion.** The fragment results from an annotation error (a false intron), not from a
  truncated gene. The genome carries a complete AOP2-type coding sequence, consistent with
  pennycress allylglucosinolate (sinigrin) chemistry. These are coding exons in different genomic frames
  separated by introns, not a single open reading frame.
- **Caveats.** Splice sites of the corrected model were not checked; no transcript evidence was
  used; enzyme activity has not been tested; and the model's first two annotated exons
  (60999055-60999090, 60999145-60999203) are not covered by any AOP2-aligned segment, so its
  5' end is probably also mis-predicted.
- **Adjacent AOP1-like model.** TAV2_LOCUS20419 (A0AAU9SRQ3, 631 aa, CDS CAH2071850) lies on the
  same chromosome sequence, on the opposite strand, 2,443 bp upstream of the AOP2 model
  (`AOP2_GENOMIC_RESULTS.md`). It is a fusion: a fragmentary AOP-like unit followed by a complete
  AOP1-like unit (73.5% id to Arabidopsis AOP1 over 99.7% of it). The locus is therefore an
  adjacent, inverted AOP gene pair, as in Arabidopsis, where AOP1, AOP2 and AOP3 are in tandem
  and inverted.

The AOP2 entry is not added to the module as a representative member, because its UniProt
sequence is the mis-predicted fragment.
