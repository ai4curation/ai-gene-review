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
