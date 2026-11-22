## 2026-09-30 annotation review

Provider deep research was unavailable for this pass because the Falcon runner
could not find `agentapi` and the OpenAI/Perplexity fallbacks lacked API keys.
The annotation review instead relied on the seeded GOA rows, the cached UniProt
record, cached PMID references, and cached Reactome entries where present.

## Source-defect re-review (2026-11-10)

An independent re-review of this gene's wrong-gene / wrong-reference source defects changed the following; where earlier notes above say otherwise, this section supersedes them.

- GO:0005886 / Reactome:R-DME-432535: defect withdrawn (evidence depth: DB_RECORD). Reactome ContentService shows the reaction's catalyst is the large plasma-membrane complex R-DME-206956 (RAS85D:GTP:SRC42A:...:DSOR1:CK2:PAR-1:PP2A) whose participant list includes Raf (P11346). The defect's premise ("Raf has no stated role") is refuted - Raf is a genuine participant through the catalyst complex, which Reactome locates at the plasma membrane. Deleted the defect and reworded summary/reason; ACCEPT stands.
- GO:0005886 / Reactome:R-DME-432590: defect withdrawn (evidence depth: DB_RECORD). Same as R-DME-432535: the PER-phosphorylation reaction is catalysed by complex R-DME-206956, whose participants include Raf (P11346), located at the plasma membrane. Raf is a participant; premise refuted. Deleted the defect and reworded; ACCEPT stands.
