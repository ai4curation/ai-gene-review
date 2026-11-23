# spm1 / pmk1 review notes

## Scope and evidence

`spm1` / `pmk1` encodes the terminal MAP kinase of the fission-yeast cell integrity MAPK pathway. The direct cascade evidence is consistent across the foundational papers: `PMID:8943330` cloned `pmk1+` and tied deletion to cell wall weakness, cell-shape, cytokinesis, and cation phenotypes; `PMID:9135147` independently isolated `spm1+` as a stress-activated MAPK required for morphogenesis and wall remodeling; `PMID:10365961` identified Pek1 as the MAPKK for Pmk1; and `PMID:10591634` showed that Mkh1, Skh1/Pek1, and Spm1 form the MAPKKK-MAPKK-MAPK module.

Deep research was attempted with Falcon after `just fetch-gene SCHPO spm1`, but the run could not proceed because the local deep-research tool had no usable provider credential (`OPENAI_API_KEY`, `EDISON_API_KEY`, `ASTA_API_KEY`, or `PERPLEXITY_API_KEY`). I therefore used the cached publications, the UniProt record, PANTHER PAINT export for `PTHR24055`, and manual literature search rather than writing a synthetic `spm1-deep-research-{provider}.md` file.

## IBA and PAINT

The `GO:0004707` IBA is placed at `PANTHER:PTN001171896`, a fungi-scoped PAINT node with CGD, PomBase, and SGD fungal MAPKs as descendant evidence. `PomBase:SPBC119.08` appearing in its own `WITH/FROM` is expected: the Pmk1 experimental annotation is one of the descendant assertions used to place the ancestral fungal MAPK activity.

The `GO:0005634`, `GO:0005737`, and `GO:0035556` IBAs are placed at the broad `PANTHER:PTN000622075` MAPK-family root node. That node is wide across fungal, plant, animal, and slime-mold MAPKs, but it is a reasonable placement for nucleocytoplasmic localization and generic intracellular signaling. I marked the CC rows as `ACCEPT` because `PMID:16291757` directly placed Pmk1 in the nucleus and cytoplasm, and the broad BP row as `KEEP_AS_NON_CORE` because `intracellular signal transduction` is true but less informative than `cell integrity MAPK cascade`.

## Existing row decisions

- Generic MF parents:
  - `GO:0004672` protein kinase activity is true but under-specific, so it is `MODIFY -> GO:0004707`.
  - `GO:0106310` protein serine kinase activity captures only the serine half of the MAPK's Ser/Thr chemistry and is `MODIFY -> GO:0004707`.
  - `GO:0005524` ATP binding is valid for the kinase domain but generic, so it is `KEEP_AS_NON_CORE`.
- Bare IPI:
  - `GO:0005515` protein binding from `PMID:10591634` is specifically Spm1 binding its upstream MAPKK Skh1/Pek1, so it is `MODIFY -> GO:0031434` mitogen-activated protein kinase kinase binding.
- Cell wall/cytokinesis/calcium/glucose outputs:
  - The PomBase rows for Pmk1-dependent cell wall organization, Nrd1/Cdc4 cytokinesis control, Yam8/Cch1-dependent calcium import, and TORC2-Gad8 glucose signaling are all biologically supported. I kept the calcium, glucose, and Nrd1/Cdc4 rows non-core to keep the single synthesized core function focused on the cell-integrity MAPK cascade.
- `PMID:34198697`:
  - The paper title foregrounds *S. japonicus*, but the full text includes *S. pombe* Pmk1/Pmk1Sj swap assays; the PomBase `GO:0032995` IMP row is credible and was retained.
- `PMID:29689193`:
  - The local cache is abstract-only and does not expose the Pmk1-specific figure, but the row is direct PomBase experimental curation and the abstract's cell wall integrity pathway result is consistent with direct Pmk1 literature. I retained the row and did not claim a mis-citation.

## Newer literature search

Manual web/PubMed search found two newer primary papers that extend the Pmk1 story but do not require new GO annotations in this review:

- `PMID:38523261` (2024) identifies Pmk1 control of mitotic exit and Cdc20/Slp1 turnover under stress. This is direct Spm1 biology but did not map cleanly to any existing row, and proposing a new mitotic-checkpoint process term would be premature without a PomBase annotation or comparator check.
- `PMID:40543417` (2025) reports that Ola1 interacts with Pmk1 and Pek1 and inhibits Pmk1 signaling to restrain mitochondrial ROS. This is newer context for MAPK/Pmk1 signaling, not a reason to broaden Spm1 to an antioxidant-response process term.
