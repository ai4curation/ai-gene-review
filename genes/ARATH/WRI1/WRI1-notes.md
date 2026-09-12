# WRI1 / WRINKLED1 (ASML1) — Arabidopsis thaliana — review notes

UniProt: Q6X5Y6 · At3g54320 · Taxon 3702 · AP2/EREB transcription factor
Relevance: master transcriptional regulator of seed oil biosynthesis — a top-level DOE/BER
lever for engineering oil yield in oilseed feedstocks.

## Core function
- **AP2/ERF-family transcription factor** with **two tandem AP2 DNA-binding domains** and a
  nuclear localization signal. Nuclear gene-expression regulator, not an enzyme.
  [file:ARATH/WRI1/WRI1-deep-research-falcon.md; PMID:10948255]
- **Master positive regulator of seed oil biosynthesis**: transcriptionally activates suites
  of **glycolytic and fatty acid synthesis genes**, coordinating carbon allocation into
  fatty acids and downstream TAG accumulation. wri1 loss-of-function mutants have **~80%
  lower seed oil** (wrinkled-seed phenotype). [PMID:15500472; PMID:9733529;
  file:ARATH/WRI1/WRI1-deep-research-falcon.md]
- Binds the **AW-box** cis-element ([CnTnG](n)7[CG]) in target promoters (direct DNA
  binding demonstrated; high-affinity, many sites Kd < 25 nM). Direct/predicted targets
  include plastidic pyruvate kinase, sucrose synthase, FRK3, PGI1, BCCP/FA-synthesis genes.
  [PMID:19719479; file:ARATH/WRI1/WRI1-deep-research-falcon.md]

## Localization
- **Nucleus** — correct and well-supported (IC PMID:10948255, plus IEA/ISM). Note: unlike
  the FAE1/FAD2/DGAT1 enzymes, here the AtSubP ISM nucleus prediction is corroborated and
  is ACCEPTED.

## Regulation (non-core interactions)
- Regulated post-translationally by **SnRK1/KIN10** kinase (sugar-status axis controlling
  WRI1 stability) -> underlies the kinase binding (IPI, PMID:28314829) annotation; also
  14-3-3 proteins, bZIP52 (repressor), and upstream LEC1/LEC2/FUS3.
  [PMID:28314829; file:ARATH/WRI1/WRI1-deep-research-falcon.md]

## Annotation review decisions
- GO:0003700 DNA-binding transcription factor activity (IEA/ISS x2) -> ACCEPT (core MF)
- GO:0003677 DNA binding (IDA/IEA) -> ACCEPT (core MF; AW-box binding)
- GO:0006355 regulation of DNA-templated transcription (IBA/IEA) -> ACCEPT (core BP)
- GO:0006110 regulation of glycolytic process (IMP) -> ACCEPT (core BP)
- GO:0006109 regulation of carbohydrate metabolic process (IMP) -> ACCEPT
- GO:0008610 lipid biosynthetic process (IMP) -> ACCEPT (core BP)
- GO:0006629 lipid metabolic process (IMP) -> ACCEPT (general)
- GO:0019432 triglyceride biosynthetic process (IMP x2) -> ACCEPT (core BP, regulatory)
- GO:0005634 nucleus (IC/IEA/ISM x3) -> ACCEPT (core location)
- GO:0019900 kinase binding (IPI) -> KEEP_AS_NON_CORE (SnRK1/KIN10 regulation)
- GO:1901959 positive regulation of cutin biosynthetic process (IGI) -> KEEP_AS_NON_CORE
- GO:0009744 response to sucrose (IEP) -> KEEP_AS_NON_CORE (expression response)

## DOE/BER relevance
WRI1 overexpression boosts oil accumulation (including ectopically in vegetative tissue);
it is the master switch for partitioning carbon into oil and a prime target for raising
feedstock oil yield. Its SnRK1/sugar-regulated stability is a tuning point.
