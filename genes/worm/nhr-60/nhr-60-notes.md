# nhr-60 review notes

## 2026-10-28 session

- Fetched with `just fetch-gene worm nhr-60`; UniProt O17898 (Swiss-Prot, NHR60_CAEEL),
  WormBase WBGene00003650, GeneID 180059 - matches the requested entry.
- 14 GOA rows: IBA (nucleus, Pol II cis-regulatory DNA binding, nuclear receptor activity,
  regulation of Pol II transcription, cell differentiation), InterPro/SubCell IEA rows,
  EXP nucleus and IDA nuclear envelope from PMID:17579999.
- PMID:17579999 is abstract-only in the cache. The nuclear-envelope IDA row is left to the
  curator (KEEP_AS_NON_CORE); the abstract says "localization on the nuclear periphery".
- PMID:23484030 (full text) shows GST-NHR-60 pulls down the GEI-8 (NCoR/SMRT homologue)
  NR1-box-containing C-terminal domain [PMID:23484030 "the C-terminal region I of GEI-8 that
  includes the predicted NR1 binding site showed affinity to GST-NHR-60"]. Proposed as NEW
  MF GO:0001222 transcription corepressor binding (IPI). Not core: in vitro only.
- General IEA terms (DNA-binding TF activity, sequence-specific DNA binding, regulation of
  DNA-templated transcription) MODIFY to the specific terms the gene already carries
  (checked with OAK ancestors: GO:0004879 is_a ... GO:0003700; GO:0000978 is_a ...
  GO:0043565; GO:0006357 is_a GO:0006355).
- No NEW process term proposed: seam cell / morphogenesis phenotypes are necessity evidence
  without a known mechanism or targets.
- See nhr-60-deep-research-manual.md for literature summary.
