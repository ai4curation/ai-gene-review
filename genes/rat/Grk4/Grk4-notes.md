# Grk4 (rat) review notes

## 2026-10-28 session

- fetch-gene resolved P70507 (RGD:61858, GeneID 59077); 22 GOA rows.
- All GOA experimental papers (PMID:9607785, 11099476, 12519791, 15166006) and UniProt's PMID:16636192 are
  abstract-only in the cache. PMID:19520868 and PMID:18957817 are full text.
- PMID:17908240 was supplied as a key paper but does not mention GRK4 at all (GRK2 study; lists GRKs 2, 3,
  5, 6 in hippocampal cultures). Recorded as relevance NONE.
- Core function: GPCR kinase activity (GO:0004703) acting on agonist-occupied receptors (mGlu1, D1R, D3R),
  leading to homologous desensitization (GO:0002029) and GPCR internalization (GO:0002031).
- Generic kinase rows (GO:0004672, GO:0004674) MODIFY to GO:0004703. Rhodopsin kinase activity
  (IDA, PMID:9607785) MODIFY to GO:0004703: rhodopsin is the surrogate assay substrate
  [PMID:9607785 "GRKs4A and B are both functional protein kinases, as demonstrated in a rhodopsin
  phosphorylation assay."]; source_defects WRONG_TERM (SUSPECTED) recorded.
- GO:0009966 IBA -> MODIFY to GO:0002029 (is_a ancestor checked with OAK).
- GO:0031623 ISO -> MODIFY to GO:0002031 (is_a child checked with OAK).
- GO:0007165 signal transduction: GRK4 terminates signalling, it is not a transducer; MARK_AS_OVER_ANNOTATED.
- Cytoplasm (IBA, IEA) -> MODIFY to cytosol + cell cortex (both carried by the gene).
- No NEW rows: plasma membrane / membrane raft localization is shown for human GRK4 in hPTCs, not directly
  for rat; renal sodium excretion / blood pressure effects are downstream physiology (necessity evidence).
