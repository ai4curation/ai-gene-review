# CASP6 notes

## 2026-09-30

- Re-audited the completed CASP6 review after refreshing GOA and UniProt. GOA
  still has the same 256 source rows and the YAML has no stale or missing rows.
  Tightened the two remaining broad `GO:0006915` apoptotic-process assertions
  to `GO:0097194 execution phase of apoptosis` while keeping separate
  intrinsic-apoptotic-signaling and ZBP1/RIPK3 PANoptosis entries for the
  RIPK1/BID feedback and viral innate-immunity contexts.
- Completed a manual CASP6 review from cached PubMed records, Reactome events,
  UniProt, GOA, the PTHR10454 PAINT context, and the existing
  `Liver apoptosis regulation by CASP6` GO-CAM after provider-backed deep
  research was unavailable.
- Accepted CASP6's core Asp-directed cysteine endopeptidase activity,
  proteolytic self-activation, broad apoptotic role, RIPK1 cleavage in intrinsic
  apoptosis, and BID/hepatocyte and lamina/SATB1/vimentin substrate contexts as
  valid protease biology.
- Added a conservative `NEW` `GO:0060090 molecular adaptor activity` assertion
  for the protease-independent RIPK3/ZBP1 scaffolding role in influenza
  A-induced PANoptosis, supported by PMID:32298652.
- Removed 201 of 202 generic `GO:0005515 protein binding` rows and modified the
  SATB1 row to the informative CASP6 cysteine endopeptidase activity. Most
  removed rows came from the PMID:32814053 systematic yeast two-hybrid
  neurodegeneration interactome or other high-throughput interactome maps.
- Treated several evidence gaps cautiously: the ATP11C/flippase cleavage row,
  the Caco-2 epithelial differentiation row, the HSP70/GATA1 cytosol row, and
  the Human Protein Atlas fibrillar-center localization row are `UNDECIDED`
  pending full-text, supplemental, or image-level confirmation.
- Accepted the valid Reactome cytosol and nucleoplasm localization rows as
  core CASP6 compartment evidence. The remaining mixed-action warnings are
  intentional source-specific exceptions: an abstract-only ATP11C row, an
  abstract-only HSP70/GATA1 cytosol row, a TP53 expression event that projects
  CASP6 as product rather than actor, and a CAFA row from a DFF40/CAD paper
  without CASP6-specific evidence.
- Marked the HIP14 palmitoylation row as `MARK_AS_OVER_ANNOTATED` for CASP6
  because CASP6 is the inhibited target in that experiment, removed the TP53
  expression Reactome cytosol projection, and removed the CAFA staurosporine
  row from the DFF40/CAD paper because the cached full text contains no
  CASP6-specific evidence.

## 2026-09-28

- Seeded the human CASP6 review with `just fetch-gene human CASP6`, creating
  `CASP6-uniprot.txt`, `CASP6-goa.tsv`, and a 256-row
  `CASP6-ai-review.yaml` stub.
- Attempted Falcon deep research with `just deep-research-falcon human CASP6`,
  but no deep-research provider API keys were configured
  (`OPENAI_API_KEY`, `EDISON_API_KEY`, `ASTA_API_KEY`, `PERPLEXITY_API_KEY`),
  so no `CASP6-deep-research-falcon.md` was generated.
