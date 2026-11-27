# Curation notes: *Escherichia coli* K-12 fadA (P21151, b3845)

Reviewed as the E. coli exemplar of the FadA thiolase step in
`modules/bacterial_fatty_acid_beta_oxidation.yaml`.

## Sources

- No provider deep-research report was generated for this gene in this session;
  the review rests on the reviewed UniProt entry and the cached GOA-cited
  publications. No `-deep-research-*.md` file exists for it.
- Cached publications are abstract-only (PMID:368024, PMID:8454629,
  PMID:3286611, PMID:334745, PMID:12535077) or title-only (PMID:4861587,
  PMID:4919548, PMID:4928881). For the title-only papers the experimental
  rows are accepted by deferring to the EcoCyc curator, because the claimed
  function is independently established for FadA.

## Decisions

- GO:0003988 acetyl-CoA C-acyltransferase activity is the core function
  (UniProt reaction with physiological direction right-to-left, Km values from
  PMID:8454629).
- GO:0010124 phenylacetate catabolic process (IBA, PTN001823071) is removed:
  the only seed for that term is E. coli PaaJ (P0C7L2), the paa-pathway
  thiolase, and FadA is in the FadA-specific subfamily PTHR43853:SF11. Recorded
  as a GO_CENTRAL source defect. The local PAINT snapshot
  (`interpro/panther/PTHR43853/PTHR43853-paint.tsv`) does not list this IBD,
  so the node assertion is visible only in the GOA row.
- GO:0005515 protein binding (IPI with FadB) is removed under the
  protein-binding policy; complex membership is kept through GO:0036125.
- Broad parents (acyltransferase, fatty acid metabolic process, fatty acid
  catabolic process, lipid catabolic process) are TOO_GENERAL beside the
  accepted GO:0003988 and GO:0006635.

## 2026-11-06 comparative enterobacterial review

All seeded non-review annotation fields and inherited authored NEW rows are preserved. Default Falcon was attempted for this target and returned an authentication HTTP403; no provider report was fabricated. Manual evidence review used the frozen UniProt record, the cached primary abstracts, full PMC full texts of PMID12057976/16385050 captures, and comparative review35892328. Existing shared publications were not refreshed.

The reference protein is E. coli K-12; the 2002 work uses MG1655 derivatives, whereas the 2006 comparative work mainly uses UB1005/MC1061 backgrounds. No identity between all strain experiments is silently asserted. WT utilization, fadR derepression, intracellular acyl-CoA chemistry and full fatty-acid consumption are distinct claims. LT2 paired fadBA exchange does not separate FadA and FadB efficiencies. No PA14/Pa10348 purified-enzyme kinetics are transferred. The 2006 CoA pools demonstrate condition-specific comparative outcomes, not universal complete oxidation by any protein alone.

Phenylacetate participation is UNDECIDED: a dedicated PaaJ and the canonical FadA role are not proof of exclusion. The exact GOA phenylacetate node assertion is missing from the frozen PAINT snapshot, so no categorical source defect or evolutionary loss is asserted. Thiolase chemistry and beta-oxidation core remain supported. Bare protein binding is removed only where present under the repository policy.

All six PAINT lineage checks found no IRD/IKR losses. Broad true terms are refined rather than rejected. No new biological-process annotations were manufactured, and no additional annotation rows were needed for this audit. Specific core complex/location roles can be inferred without claiming new target-specific localization measurements. Full acquisition files remain ignored; scoped quotations and source hashes are in ECOLI/fadE/fadE-source-analysis/enterobacterial-evidence.md.
