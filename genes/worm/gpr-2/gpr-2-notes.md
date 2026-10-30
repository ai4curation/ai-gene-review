# gpr-2 review notes

- Fetch: `just fetch-gene worm gpr-2` failed repeatedly with a read timeout on the UniProt
  gene-symbol stream search (a direct curl of that search also timed out at 90 s, while the
  accession endpoint answered in <1 s). Ran `just fetch-gene worm Q03569 --alias gpr-2`;
  confirmed id Q03569 (GPR2_CAEEL, gene gpr-2 / C38C10.4), 13 GOA rows.
- No deep-research provider available; literature compiled manually in
  `gpr-2-deep-research-manual.md`.
- All functional data are for GPR-1/2 jointly (near-identical paralogs; RNAi/antibodies
  cross-react) [PMID:16247027 "We used a dsRNA that depletes two highly homologous G-protein
  regulators, GPR-1 and GPR-2"]. Statements about GPR-1/2 are treated as applying to gpr-2, as
  WormBase and ComplexPortal curators do. Kept consistent with the gpr-1 review
  (`genes/worm/gpr-1/gpr-1-ai-review.yaml`).
- PMID:16247027 (key paper requested): full text read; only an RNAi tool use of gpr-1/2 to
  abolish pulling forces. LOW relevance, not a GOA source for gpr-2.
- Core: GoLoco GDI for GOA-1/GPA-16 (IDA x2: PMID:16162648, PMID:18984596; plus PMID:12814548),
  in the cortical Galpha-GPR-1/2-LIN-5 force generator positioning the mitotic spindle.
- GO:0008277 regulation of GPCR signaling pathway: GPR-1/2 act receptor-independently
  [PMID:12814548 "the Galpha subunits are regulated by a receptor-independent mechanism"];
  marked over-annotated (same as gpr-1).
- No NEW terms. G-protein alpha-subunit binding (GO:0001965) is on gpr-1 by IPI but not gpr-2;
  it is entailed functionally by the GDI activity and not added. Spindle orientation in
  EMS/P2 rests on RNAi phenotype plus localization; left as a question.
