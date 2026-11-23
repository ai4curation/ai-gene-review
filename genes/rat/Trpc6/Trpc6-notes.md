# Trpc6 (rat) review notes

- Accession check: fetch-gene resolved A0ABK0M635 (RGD:619788, GeneID 89823); GOA keyed to it. No switch.
- No deep-research API; wrote Trpc6-deep-research-manual.md by hand.
- Full text read: PMID:20501650 (key; rat TRPC6A construct, A7r5 siRNA), PMID:19889962, PMID:20479868.
  Abstract only: PMID:11278449, 11788346, 16025302, 22764246 (PMC full text not retrievable via PubMed MCP).

## Decisions worth flagging
- GO:0050774 negative regulation of dendrite morphogenesis (IMP, PMID:22764246): abstract says
  TRPC6/NT-4 Ca2+ influx *promoted* dendritic growth [PMID:22764246 "In contrast, the Ca(2+) influx through TRPC6 induced by NT-4 promoted the dendritic growth"].
  Looks inverted (or TRPC5 result attached to Trpc6). Full text not available -> UNDECIDED +
  source_defect CHECK (suggest GO:0050775).
- GO:0045666 / GO:0030182 (PMID:20479868): paper internally inconsistent (abstract: TRPC6 siRNA no
  effect; results: either siRNA suppressed differentiation). MARK_AS_OVER_ANNOTATED.
- GO:0015279 store-operated (ISO from mouse): rat TRP6 not activated by thapsigargin
  [PMID:11278449]; but PASMC data [PMID:19889962] show SOCE contribution. MARK_AS_OVER_ANNOTATED.
- GO:0070679 IP3 binding (ISO from human; human row IDA PMID:14505576 is a Homer/TRPC1/IP3R paper):
  no evidence TRPC6 binds IP3 itself; source_defect CHECK (SUSPECTED) on BHF-UCL human row.
- GO:0051928 positive regulation of calcium ion transport (ISO; human row from TRPC2 paper
  PMID:10998353 where TRPC6 likely was the positive control): the channel *is* the transport ->
  MODIFY to GO:0070588.
- Actin/actinin/clathrin binding IDA (PMID:16025302 abstract only, co-IP from brain lysate): UNDECIDED.
