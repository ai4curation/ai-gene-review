# TWNK review notes

## 2026-10-28 session

- Fetched with `just fetch-gene human TWNK`; UniProt Q96RR1 (PEO1_HUMAN, GeneID 56652),
  61 GOA rows. Cached GOA PMIDs plus PMID:22952820 (Drosophila adPEO models) and
  PMID:23393161 (mouse Twnk conditional knockout).
- No deep-research API keys: literature synthesis in `TWNK-deep-research-manual.md`.
- Core function: hexameric 5'->3' DNA helicase of the mtDNA replisome, coupling NTP
  (ATP/UTP) hydrolysis to unwinding [PMID:12975372 "TWINKLE is a DNA helicase with 5' to
  3' directionality and distinct substrate requirements"]; acts with POLG and SSBP1
  [PMID:15167897 "Our findings provide the first biochemical evidence that TWINKLE is the
  helicase at the mitochondrial DNA replication fork."].
- Decisions:
  - GO:0003678 DNA helicase activity (IBA, IEA) -> MODIFY to GO:0043139 5'-3' DNA helicase
    activity, which the gene already carries by many EXP/IDA rows.
  - GO:0006260 / GO:0006261 -> MODIFY to GO:0006264 mitochondrial DNA replication.
  - GO:0006390 mitochondrial transcription (IMP, PMID:18971204): full text read; the
    transcript decrease after mutant expression is a downstream phenotype; no Twinkle
    activity in transcription shown -> MARK_AS_OVER_ANNOTATED with a WRONG_TERM CHECK
    source defect.
  - PMID:34950192 is mainly about Drosophila, but full text shows human full-length
    Twinkle was purified and assayed for liposome binding and ATPase (Fig. 4), so the
    human IDA rows are legitimate. The 5'-3' helicase IDA from this paper rests only on an
    ATPase readout; the activity itself is established by many other papers, so ACCEPT.
  - Bare protein binding (LGALS3BP HT-Y2H) REMOVE per policy.
- No NEW terms proposed: apoptosis (PMID:22952820) and transcript effects are indirect.
