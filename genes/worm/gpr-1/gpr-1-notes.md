# gpr-1 review notes

- Fetch: `just fetch-gene worm gpr-1` timed out on the UniProt stream endpoint (gene-symbol
  search took ~60 s, above the 30 s client timeout) three times. Ran
  `just fetch-gene worm Q95QJ7 --alias gpr-1` instead; confirmed id Q95QJ7 (GPR1_CAEEL,
  gene gpr-1 / F22B7.13), 17 GOA rows.
- All functional data are for GPR-1/2 jointly (near-identical paralogs; RNAi/antibodies
  cross-react). I treat GPR-1/2 statements as applying to gpr-1, as WormBase curators do.
- PMID:16247027 (Audhya 2005, CAR-1/CGH-1) only uses gpr-1/2(RNAi) as a tool to abolish
  pulling forces [PMID:16247027 "GPR-1 and GPR-2, which are required for the production of
  astral pulling forces"]. Low relevance; corroborates the pulling-force role.
- Core: GoLoco GDI for GOA-1/GPA-16 (IDA x2 plus PMID:12814548), cortical Galpha-GPR-LIN-5
  force generator positioning the mitotic spindle.
- Protein binding rows (LIN-5, GPA-16, KXD-1 Y2H) removed per policy; Galpha binding is
  captured by GO:0001965.
- GO:0008277 regulation of GPCR signaling pathway: GPR-1/2 act receptor-independently
  [PMID:12814548]; marked over-annotated.
- No NEW process terms: establishment of mitotic spindle orientation (EMS/P2) is supported
  mainly by RNAi phenotype and localization; leave as a question.
