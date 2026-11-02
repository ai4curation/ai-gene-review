# SNCA review notes

## Session 1 (2026-10-28)

- fetch-gene resolved P37840 (SYUA_HUMAN, reviewed); GOA has 399 rows, 197 of them bare
  GO:0005515 (145 from the PMID:32814053 interactome screen).
- No deep-research API available; manual synthesis in `SNCA-deep-research-manual.md`.
- PMID:22219196 was flagged as a key paper by the task but is a Drosophila GSTO1/parkin
  study [PMID:22219196 "We further identified the ATP synthase β subunit as a novel in vivo target of DmGSTO1."]; it does not address SNCA function. Recorded with relevance NONE.

### Synthesis used for actions
- Core: membrane (anionic, curved phospholipid) binding via the N-terminal amphipathic
  helix; as membrane-bound multimer, chaperones SNARE-complex assembly by binding VAMP2
  [PMID:20798282; PMID:25246573]; modulates SV exocytosis (fusion pore dilation
  [PMID:28288128]) and dopamine release [PMID:10707987].
- Copper binding is a robust biochemical property [PMID:21319811] with uncertain
  physiological role.
- Transporter/enzyme modulation, metal effects on aggregation, nuclear roles, and
  inflammatory expression changes are kept as non-core or marked over-annotated.

### Upstream issues recorded as source_defects
- GO:0010642 (PDGF receptor signalling) and GO:0070495 (thrombin receptor signalling)
  from PMID:12239163: the paper measures alpha-granule secretion, also inhibited with
  ionomycin; receptor-signalling terms look mis-chosen.
- GO:0004869 caspase inhibitor activity from PMID:10818098: cellular caspase activity
  readout, not direct inhibition.
- GO:1904715 negative regulation of CMA from PMID:20697033: abstract shows SNCA as a CMA
  substrate.
- TAS rows from PMID:21320589 (dopamine biosynthesis, dopamine uptake, epinephrine
  response): the paper is a bioinorganic study of the alpha-Syn-Cu complex and MT-3.
- PMID:16176937 carries a 2024 expression of concern (kinesin/dynein binding rows UNDECIDED).

## 2026-10-28: core function locations

The self-association core function listed Lewy body as its location, while the Lewy body IDA row is KEEP_AS_NON_CORE as a disease aggregation state. The location was dropped from the core function so the two agree; the core function itself (homo-oligomerisation and fibril formation) is unchanged.

## 2026-10-28: action corrections (PR #5693 review)

- GO:0008017 microtubule binding (IEA) was marked over-annotated as if it were more general than tubulin binding. It is the child of GO:0015631, and microtubule binding is shown directly (PMID:27628239, PMID:11698390), so the row is now ACCEPT.
- Membrane (two rows) and enzyme binding (two rows) were KEEP_AS_NON_CORE or MARK_AS_OVER_ANNOTATED with reasons saying they were true but generic. They are now TOO_GENERAL: plasma membrane and synaptic vesicle membrane, and phospholipase binding, are asserted descendants.
- Protein domain specific binding has no asserted descendant, so TOO_GENERAL does not apply; it is UNDECIDED pending a look at the rat source row.
- The caspase inhibitor activity reason now says the full text was not available.
- Lipid binding (three EXP rows) stays ACCEPT: the cited assays include detergent micelles as well as lipid vesicles, so lipid binding is as specific as those papers support; phospholipid binding is carried on its own rows and in the core functions.
- Follow-up (same review): the microtubule binding row now cites only PMID:27628239, with its quote; PMID:11698390 does not mention microtubules. The beta-tubulin binding and cytoplasmic vesicle membrane reasons no longer argue subsumption, and the protein domain specific binding source status is UNRESOLVED to match its root cause.
