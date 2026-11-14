# PA3933 (BetT2, Q9HX83) notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9HX83 --alias PA3933`; accession matches the worklist. No gene
name in UniProt; folder and symbol use the locus tag. No deep-research provider was used. The cached
PMID:21478341 is abstract-only; the full text was read on PMC (PMC3133218) and quotes marked "full text"
are copied verbatim from it. Chen & Beattie 2008 (PMID:18156257) full text could not be retrieved.

### Which PAO1 gene is BetT2?

- Malek et al. (full text): "three BCCTs, designated BetT1, BetT2, and BetT3 (PA14_70980, PA14_12990, and PA14_69850, respectively)".
- `genes/PSEAE/PA5291/PA5291-bioinformatics/RESULTS.md`: PA14_12990 is 100% identical to PAO1 PA3933;
  PA14_69850 is 100% identical to PAO1 PA5291. So PA3933 is BetT2, and BetT3 is PA5291.

### What is known about BetT2 (PA3933)

- Malek et al. (full text), summarising Chen & Beattie 2008: "We previously showed that BetT2 and BetT3 transport GB and choline, respectively, and confer osmoprotection when expressed in P. syringae in a hyperosmolar environment ( 6 )."
- In Malek et al. BetT2 appears only in the expression survey (full text): "Neither choline nor GB affected levels of betT2 and opuCA transcripts in MOPS-P medium".
  No mutant, uptake or growth experiment in that paper involves BetT2. Every functional experiment is on
  BetT1, BetT3 and CbcXWV.

### PseudoCAP rows on PA3933 citing PMID:21478341

All four (GO:0005275, GO:0033265, GO:0042426, GO:0071475) describe BetT3 data: choline uptake, growth on
choline, and the role at high osmolarity [PMID:21478341 "BetT3 was the major choline transporter under hyperosmolar conditions"].
They were attached to PA3933 instead of PA5291, apparently by a PA14-to-PAO1 locus mismapping. Verdict
WRONG, CONFIRMED (full text read; sequence identity checked). Each row gets a PSEUDOCAP
WRONG_GENE_PRODUCT defect (REPOINT to Q9HTR3). The mirror error, glycine betaine rows from PMID:18156257
on PA5291 that most likely belong here, is recorded on `genes/PSEAE/PA5291/` (PROBABLE).

### Annotation decisions

- GO:0005275, GO:0033265, GO:0042426, GO:0071475 (IDA, PMID:21478341): REMOVE + PSEUDOCAP defects.
- GO:0015837 amine transport (IEA, inferred from the removed GO:0005275 row): REMOVE.
- GO:0022857 IBA, IEA: ACCEPT. The family term is as precise as the evidence on PA3933 itself allows:
  glycine betaine transport is reported only through a secondary summary of a paper not read in full.
- GO:0055085 IEA: ACCEPT. GO:0005886 IBA, IEA: ACCEPT. GO:0016020 IEA: MODIFY to GO:0005886.
- Action counts: REMOVE 5, ACCEPT 5, MODIFY 1. Source defects: PSEUDOCAP 4 (CONFIRMED).

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001247333 | GO:0022857 transmembrane transporter activity | 5 | 34 (19 taxa) | GO:0005275, IDA, PMID:21478341 (PseudoCAP) | WRONG | Full text read: the paper does no functional work on BetT2 (PA3933); the transport data are BetT3 (PA5291) and BetT1. Wrong gene product. | E. coli BetT P0ABC9 and CaiT P31553 (experimental); BetT1 Q9HTI9 (SOUND); BetT3 Q9HTR3 (SOUND) | Yes |

Node-level: no GO_CENTRAL defect. Four sound seeds remain, and GO:0022857 suits the BCCT clade. PA3933
itself is still likely a transporter (glycine betaine, per the 2008 work), so its own IBA is accepted.
