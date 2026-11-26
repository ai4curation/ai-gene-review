# Cpt1a (rat) review notes

## Session 1 (2026-10-28)
- `just fetch-gene rat Cpt1a` resolved P32198 (CPT1A_RAT, RGD:2396, GeneID 25757); 79 GOA rows.
- No deep-research provider available; manual synthesis in `Cpt1a-deep-research-manual.md`.
- Core: carnitine O-palmitoyltransferase activity (GO:0004095) at the mitochondrial outer
  membrane, within the carnitine shuttle / fatty acid beta-oxidation. Massive IDA support
  (mutagenesis papers by Hegardt/Serra/Asins, Woldegiorgis, Zammit, Prip-Buus groups).
- Decisions:
  - GO:0016746 acyltransferase (InterPro2GO) -> MODIFY to GO:0004095.
  - GO:0006631 fatty acid metabolic process (IBA/IDA/IEP) -> MODIFY to GO:0001676
    long-chain fatty acid metabolic process (already carried).
  - Mitochondrion root rows kept (ORGANELLES policy), MOM rows accepted.
  - NOT ER membrane (PMID:12401113) accepted; the paper's title states the conclusion.
  - regulation-of-FA-oxidation terms (TAS/IMP): over-annotations; CPT1A is the
    regulated enzyme of the pathway, its participation is captured by beta-oxidation.
    Over-expression raising flux is not regulation [PMID:19302064, PMID:11988095].
  - glucose metabolic process and liver regeneration: MARK_AS_OVER_ANNOTATED (indirect).
  - epithelial cell differentiation (ISO/IEA from human IEP): MARK_AS_OVER_ANNOTATED.
  - IEP "response to" rows: KEEP_AS_NON_CORE (expression responses).
  - Adaptor activity / positive regulation of innate immune response (from human
    ZDHHC4-MAVS work): KEEP_AS_NON_CORE, untested in rat.
  - NEW: GO:0006853 carnitine shuttle (IC). Comparator: human CPT1A, CPT2, SLC25A20 carry
    it; CPT1A performs the acylcarnitine-forming step, so it does part of the work.
- Not added: peptide-lysine-N-succinyltransferase (only by similarity to human).
