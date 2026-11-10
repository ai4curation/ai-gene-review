# Slc25a4 (rat) review notes

## Session 2026-10-28

- `just fetch-gene rat Slc25a4` resolved Q05962 (ADT1_RAT, RGD:620352,
  GeneID 85333) with 54 GOA rows. No deep-research API keys; literature work
  is in `Slc25a4-deep-research-manual.md`.
- Additional cached papers for ortholog support: PMID:31341297 (Bertholet 2019,
  AAC H+ transport), PMID:31618756 (Hoshino 2019, ANT and mitophagy),
  PMID:14749836 (Kokoszka 2004, ANT not essential for mPTP), PMID:37278158
  (human SLC25A4 ping-pong kinetics). PMID:18251717 (Parker 2008) read in full:
  rat skeletal-muscle proton leak partly ANT-catalysed (CAT/BKA sensitive)
  [PMID:18251717 "proton conductance catalysed partly by UCP3 and partly by
  the adenine nucleotide translocase"]. This paper underlies the RGD IMP to
  GO:2000277 shown in the UniProt DR lines, which is not in the current GOA
  file, so it is not reviewed as a row.

### Decisions

- Core: ATP:ADP antiporter activity in the mitochondrial inner membrane
  (mitochondrial ADP import / ATP export); secondary core: fatty-acid-dependent
  H+ leak (oxidative phosphorylation uncoupler activity).
- mPTP complex, regulation of membrane permeability, apoptosis/necroptosis,
  mitophagy, adaptive thermogenesis: non-core, consistent with the human
  SLC25A4 review.
- IEP developmental rows (heart, liver development) are expression
  correlations: MARK_AS_OVER_ANNOTATED.
- Outer membrane IDA (PMID:18385140): the paper explains ANT in OM fractions
  as contact-site co-fractionation of an IM marker; MARK_AS_OVER_ANNOTATED with
  a WRONG_TERM source defect (CHECK).
- Membrane raft IDA (PMID:14499952): abstract-only, abstract does not mention
  ANT; detergent-resistant membrane proteomics often co-purifies mitochondrial
  carriers. UNDECIDED.
- Isoform caveat: several rat experimental rows (9820802 liver IMM; 18385140)
  use pan-ANT reagents, so the specific isoform is unclear.
