# Psmc5 (rat) review notes

## Session 1

- Fetched with `just fetch-gene rat Psmc5`; UniProt P62198 (PRS8_RAT), RGD:708376,
  GeneID 81827 confirmed. 53 GOA rows.
- Literature summary in `Psmc5-deep-research-manual.md` (no deep-research API).
- Full text read: PMID:18986984 (Rousseau 2009, rat neurons Rpt6/Rpt4 and polyQ
  inclusions), PMID:41298377 (Kury 2025, PSMC5 proteasomopathy, rat hippocampal
  neuron knockdown). Others are abstract only.

### Upstream problems found

1. GO:0031531 thyrotropin-releasing hormone receptor binding (ISS, ISO, IEA) all
   derive from human P62195 IPI PMID:7870181 with UniProtKB:P10828 (THRB). The
   paper is about the thyroid-hormone receptor [PMID:7870181 "Interaction of
   thyroid-hormone receptor with a conserved transcriptional mediator"]. The
   correct term is GO:0046966 nuclear thyroid hormone receptor binding. Recorded as
   WRONG_TERM source defects (UniProt for the root IPI; RGD for the rat ISS).
2. GO:0005102 signaling receptor binding (ISO, IEA) derives from mouse P62196
   IPI PMID:8598193 with With/From P28700 (RXRA). That abstract says "RXR alpha
   efficiently interacts with TIF1, but not with mSUG1"; the receptors that did
   bind were RARalpha, TR, ER, VDR. Recorded WRONG_WITH_FROM (UniProt). Term is
   lateral-modified to GO:0016922 nuclear receptor binding (not a descendant of
   GO:0005102 in current GO; checked with OAK).
3. GO:0031410 cytoplasmic vesicle (ISO, IEA) derives from human IDA PMID:15885686,
   a TRIM37 paper whose abstract describes overexpression-induced aggresomes that
   are "proteasome subunit-... positive". Aggresome (GO:0016235) is the structure
   described; recorded WRONG_TERM (UniProt, PROBABLE since full text not seen).

### Decisions

- Complex rows (proteasome complex, regulatory particle, accessory complex) are
  refined to GO:0008540 base subcomplex, as for sibling rat Psmc4/Psmc6.
- nucleus -> nucleoplasm; cytoplasm -> cytosol (siblings' convention).
- Core MF: ATP hydrolysis activity (own activity; IDA on rat protein,
  PMID:9287326) plus contributes_to proteasome-activating activity.
- Synaptic vesicle and AMPA receptor rows (PMID:37228199, abstract only):
  UNDECIDED, as for siblings.
- No NEW process terms proposed. Synaptic-plasticity roles (CaMKII-phosphorylated
  Rpt6, PMID:19638347/22496558) are regulation of the proteasome by synaptic
  activity, not Psmc5 performing synaptic processes; knockdown phenotypes in
  PMID:41298377 are necessity evidence. Not annotated.
