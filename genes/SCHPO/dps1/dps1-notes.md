# dps1 (O43091, SPBPJ4664.01) review notes

## Sources

No deep-research provider output is available for this gene (no provider API keys in
this environment), and no PomBase hand-written description is fetched for S. pombe.
The review rests on the UniProt record and the cached PomBase-cited literature.

## Literature

- Cloning and disruption: the dps disruptant has no ubiquinone and no decaprenyl
  diphosphate synthase activity [PMID:9133618 "This disruptant was not able to
  synthesize ubiquinone and had no detectable decaprenyl diphosphate synthase activity,
  indicating that the dps gene is unique and responsible for ubiquinone biosynthesis."]
  It also shows antioxidant dependence [PMID:9133618 "The dps-deficient strain required
  cysteine or glutathione for full growth on the minimal medium."]
- Heterotetramer with Dlp1 [PMID:14519123 "Furthermore, the two proteins were shown to
  form a heterotetrameric complex."] and both subunits are needed [PMID:14519123 "This
  indicates that both dps1 and dlp1 are required for the S. pombe enzymatic activity."]
- Mitochondrial localisation of Dps1-GFP [PMID:24911838 "The Dps1, Ppt1/Coq2, Coq3, Coq4,
  Coq5, Coq6, Coq7, Coq8, and Coq9 GFP fusion proteins also localized to the mitochondria"]
- Cross-species IPI with E. coli IspB [PMID:20051244 "IspB interacted with Dlp1 (or Dps1),
  forming a high-molecular weight complex that stabilized IspB, leading to full
  functionality."]

## Audit decisions (2026-11)

- GO:0008299 isoprenoid biosynthetic process: GO:0006744 is not an is_a/part_of
  descendant of GO:0008299 (checked in QuickGO ancestors), so the earlier TOO_GENERAL
  was not valid. Changed all four rows to KEEP_AS_NON_CORE, matching dlp1 and human
  PDSS1/PDSS2.
- GO:0045337 FPP biosynthetic process (PomBase IMP, PMID:9133618): FPP is the
  substrate of the enzyme; MARK_AS_OVER_ANNOTATED (not REMOVE, since the full text is not
  cached), with a suggested question.
- Bare protein binding rows removed under the protein-binding policy.
- Core function agrees with the module annoton (Dps1/PDSS1 catalytic subunit of the
  GO:0097269 heterotetramer).
