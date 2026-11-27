# Arrb1 (rat) review notes

## Session 1 (initial review)

- fetch-gene resolved P29066 (ARRB1_RAT, Swiss-Prot, RGD:2156, GeneID 25387). 136 GOA rows
  in the stub (138 in the tsv; the two duplicated SynGO rows for postsynaptic density and
  glutamatergic synapse were merged by the stub generator).
- No deep-research provider available; literature synthesis is in `Arrb1-deep-research-manual.md`.
- Papers read in full text: PMID:10725339, 19171933, 19254952, 19339617, 20650893, 20705669,
  23604254, 37209686, 38175886. All others abstract-only.

### Framing

Beta-arrestin-1 is a GPCR adaptor: it binds GRK-phosphorylated, agonist-activated receptors
(desensitization), links them to clathrin/AP-2 (internalization), and scaffolds signaling
(ERK, Src, AKT) and E3 ligases (AIP4/ITCH, MDM2) [PMID:20650893 "β-Arrestin 1 interacts with, and acts as an adaptor
for AIP4, an E3 ubiquitin ligase responsible for TRPV4 ubiquitination."]. Nuclear/transcriptional roles
(p300 recruitment, CREB, LEF) are real but secondary.

### Decisions worth flagging

- Phototransduction ISO (from mouse IMP PMID:11853756): the paper uses rod arrestin (Sag)
  knockouts [PMID:11853756 "mice with rod arrestin deleted (arrestin -/-)"]. QuickGO shows the
  mouse IMP is on Arrb1 (with MGI:2388373) and not on Sag for this paper. Looks like a gene
  mis-attribution at MGI; rat ISO row REMOVEd and a source defect recorded.
- Cysteine-type endopeptidase inhibitor activity ISO (from mouse IMP PMID:19915011): the
  mechanism shown is ERK1/2-p90RSK phosphorylation of Bad, not caspase inhibition. REMOVEd.
- GTPase activator activity ISO (from human IMP PMID:15611106, RhoA activation with Gq):
  RhoA activation is GTP loading, not GAP activity. MARK_AS_OVER_ANNOTATED.
- Negative regulation of ERK1/2 IMP (PMID:19254952): beta-arrestin-1 siRNA raised ERK only at
  the 2-min point [PMID:19254952 "with significantly elevated levels of activation at the 2-min time point"];
  consistent with the reciprocal regulation in UniProt. Kept non-core.
- PMID:19171933 (beta-arrestin-2 anti-apoptotic): beta-arrestin-1 knockdown reduced caspase-3
  cleavage in rat VSMCs [PMID:19171933 "knocking-down β-arrestin-1
 leads to decreases in apoptotic reagent-induced caspase-3 cleavage"], opposite sign to the
  astrocyte IMP (PMID:24378649). Apoptosis effects of beta-arrestin-1 are cell-context
  dependent; all apoptosis rows kept non-core, no NEW apoptosis terms.
- No NEW terms proposed for processes; the only NEW row is the MF "ubiquitin-like
  ligase-substrate adaptor activity" (GO:1990756) for the AIP4-TRPV4 adaptor function, which
  is direct participation (the paper shows beta-arrestin-1 bridges the ligase to its substrate).

## 2026-10-28 review-fix pass

- Phototransduction ISO row: softened 'Beta-arrestin-1 is not studied' to what the abstract of PMID:11853756 (abstract only) supports, namely that it describes rod-arrestin-deleted and transducin-deleted mice and does not mention beta-arrestin-1.
- source_defects corrected_value is now MGI:MGI:98227 (mouse Sag, S-arrestin; MGI cross-reference of UniProt P20443), with the name in corrected_label.
- Removed supported_by self-citations of the gene's own -deep-research-manual.md where a primary citation in the same block already supports the row (the reviewer's own conclusion is not independent evidence). The validator now warns that no annotation cites the deep-research file; that warning is accepted deliberately, which sets the status to DRAFT.
