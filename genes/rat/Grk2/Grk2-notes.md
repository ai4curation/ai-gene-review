# Grk2 (rat) review notes

## Session 1

- Fetched P26817 (GRK2_RAT; RGD:2062; GeneID 25238). UniProt timed out on the first several
  fetch attempts, then succeeded; GOA has 112 rows (39 references).
- No deep-research API; literature synthesis written by hand in `Grk2-deep-research-manual.md`.
- PMID:17908240 (Willets et al. 2007) is full text: dominant-negative D110A,K220R GRK2 reduces
  M1 mAChR desensitization in rat hippocampal neurons [PMID:17908240 "Our current data also
  emphasize that the role of GRK2 in this regulation is dependent on its kinase activity."].
- Most other rat papers are abstract-only. Human GRK2 review (`genes/human/GRK2`) used for
  alignment of ISO-derived terms.

### Decisions worth flagging

- `nucleus` IEA (GO_REF:0000108) is a logical inference from `maintenance of protein location
  in nucleus` (PMID:28759639), where the nuclear protein is NFAT, not GRK2; removed as an
  inter-ontology mis-inference.
- `vasodilation` IMP (PMID:23913704) and `positive regulation of vasoconstriction` IMP
  (PMID:28882814): the papers show GRK2 opposes insulin-induced and light-induced relaxation;
  modified to `negative regulation of vasodilation` / `negative regulation of relaxation of
  smooth muscle`.
- `regulation of inositol trisphosphate biosynthetic process` (PMID:20705669) refined to the
  negative-regulation child: GRK2 desensitizes P2Y2-PLC signaling.
- `apical`/`basolateral plasma membrane` IDA (PMID:16899567): the abstract reports only
  cytoplasm-to-plasma-membrane recruitment by sucrose gradient; sub-domain cannot be verified
  from the abstract, left UNDECIDED.
- Expression-change (IEP) "response to X" rows marked over-annotated: they show GRK2 levels
  change, not that GRK2 does work in the response.
- No NEW terms proposed.

## 2026-10-28 review-fix pass

- Removed supported_by self-citations of the gene's own -deep-research-manual.md where a primary citation in the same block already supports the row (the reviewer's own conclusion is not independent evidence). The validator now warns that no annotation cites the deep-research file; that warning is accepted deliberately, which sets the status to DRAFT.
