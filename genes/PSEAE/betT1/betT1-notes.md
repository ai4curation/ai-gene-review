# betT1 (PA5375, Q9HTI9) notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9HTI9 --alias betT1`; accession matches the worklist. No
deep-research provider was used. The cached PMID:21478341 is abstract-only; the full text was read on
PMC (PMC3133218) and the quotes below marked "full text" are copied verbatim from it.

### Literature (Malek et al. 2011, PMID:21478341)

- Names and loci (full text): "three BCCTs, designated BetT1, BetT2, and BetT3 (PA14_70980, PA14_12990, and PA14_69850, respectively)".
  PA14_70980 is 99.2% identical to PAO1 PA5375 (see `genes/PSEAE/PA5291/PA5291-bioinformatics/RESULTS.md`).
- Gene model (full text): "Sequence analysis showed that the N-terminal amino acid sequence of PA5375 (BetT1) lacked 18 amino acids that were present in closely related homologs"
  and "a potential alternative start site was found 54 bp upstream of the annotated start site".
- Transport activity (full text): "A clone expressing betT1 from the alternative start site (p betT1 N) was able take up [ 14 C]choline in M63 medium",
  whereas the clone from the annotated start was inactive (0.02 nmol/mg in 10 min). Sodium-independent
  uptake, "consistent with proton rather than sodium symport activity" (data not shown); high affinity,
  low capacity.
- In P. aeruginosa (full text): "Choline transport was decreased by 52% and 80% in the Δ betT1 and Δ betT3 mutants, respectively".
  Abstract: BetT1 alone cannot support growth on choline [PMID:21478341 "BetT3 and CbcXWV, but not BetT1, were sufficient to support growth on choline."];
  betT1 is repressed by BetI and induced by choline.

### Annotation decisions

- GO:0005275 amine transmembrane transporter (IDA, seed): MODIFY to GO:0015220 choline transmembrane
  transporter activity. GO:0005275 is not an ancestor of GO:0015220 in GO (choline transport sits under
  quaternary ammonium group transmembrane transporter), so MODIFY, not TOO_GENERAL.
- GO:0022857 IBA and IEA: MODIFY to GO:0015220 (as in the E. coli betT review).
- GO:0033265 choline binding (IDA): MARK_AS_OVER_ANNOTATED; no binding assay, substrate binding is part of
  the transport activity.
- GO:0042426 choline catabolic process (IDA): MARK_AS_OVER_ANNOTATED + PSEUDOCAP WRONG_TERM defect
  (PROBABLE), consistent with the PA5377 (CbcW) review of the same paper.
- GO:0015837, GO:0055085 IEA: MODIFY to GO:0015871 choline transport.
- GO:0005886 IBA, IEA: ACCEPT. GO:0016020 IEA: MODIFY to GO:0005886.
- gene_model_issues: WRONG_START_SITE, CONFIRMED (ortholog comparison plus loss of activity of the
  annotated ORF). Q9HTI9 (516 aa) lacks the 18 N-terminal residues needed for activity.
- Action counts: MODIFY 6, MARK_AS_OVER_ANNOTATED 2, ACCEPT 2. Source defects: PSEUDOCAP 1 (PROBABLE).

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001247333 | GO:0022857 transmembrane transporter activity | 5 | 34 (19 taxa) | GO:0005275, IDA, PMID:21478341 (PseudoCAP) | SOUND | Full text read: BetT1 (from the corrected start) takes up [14C]choline in choline-uptake-deficient E. coli MKH13. A transporter is shown; the precise term should be choline transmembrane transporter, but the node term is supported. | E. coli BetT P0ABC9 and CaiT P31553 (experimental); PA5291 BetT3 (SOUND for choline); PA3933 BetT2 (seed WRONG, wrong gene) | Yes |

Node-level: GO:0022857 is the right family-wide term for the BCCT clade, whose members carry choline,
glycine betaine and carnitine. No GO_CENTRAL defect. The shared PA3933/PA5291 swap is recorded on those
genes (see `genes/PSEAE/PA5291/PA5291-notes.md`).
