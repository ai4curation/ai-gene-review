# Curation notes: *Escherichia coli* K-12 fadE (Q47146, b0221, formerly yafH)

Reviewed as the E. coli exemplar of the acyl-CoA dehydrogenase step in
`modules/bacterial_fatty_acid_beta_oxidation.yaml`.

## Sources

- No provider deep-research report was generated for this gene in this session;
  the review rests on the reviewed UniProt entry and the cached GOA-cited
  publications. No `-deep-research-*.md` file exists for it.
- PMID:12057976 (Campbell & Cronan 2002) and PMID:334745 are abstract-only in
  the cache; PMID:4928881 is title-only.

## Decisions

- Core functions: GO:0004466 long-chain and GO:0070991 medium-chain fatty
  acyl-CoA dehydrogenase activity (UniProt reactions curated from
  PMID:12057976; the mutant fails on C8, C10, C12 and C18:1 fatty acids).
- GO:0003995 acyl-CoA dehydrogenase activity is kept (ACCEPT) on every row:
  it names the reaction class and is the module's term for this step.
- GO:0005737 cytoplasm is accepted. FadE (like Pseudomonas putida FadE) has a
  hydrophobic N-terminal stretch, but UniProt curates no transmembrane segment
  and the activity was recovered in the soluble fraction (PMID:334745).
  Membrane association is left as an open question.
- GO:0016627 and GO:0009062 are TOO_GENERAL.

## 2026-11-06 comparative enterobacterial review

All seeded non-review annotation fields and inherited authored NEW rows are preserved. Default Falcon was attempted for this target and returned an authentication HTTP403; no provider report was fabricated. Manual evidence review used the frozen UniProt record, the cached primary abstracts, full PMC full texts of PMID12057976/16385050 captures, and comparative review35892328. Existing shared publications were not refreshed.

The reference protein is E. coli K-12; the 2002 work uses MG1655 derivatives, whereas the 2006 comparative work mainly uses UB1005/MC1061 backgrounds. No identity between all strain experiments is silently asserted. WT utilization, fadR derepression, intracellular acyl-CoA chemistry and full fatty-acid consumption are distinct claims. LT2 paired fadBA exchange does not separate FadA and FadB efficiencies. No PA14/Pa10348 purified-enzyme kinetics are transferred. The 2006 CoA pools demonstrate condition-specific comparative outcomes, not universal complete oxidation by any protein alone.

All ETF-defined dehydrogenase terms are refined to the acceptor-unspecified proposed reaction. This retains acyl-CoA oxidation and assay-qualified medium/long-chain use, without claiming ETF is either demonstrated or impossible. Primary12057976 short-chain loss uses fadR613::Tn10; WT octanoate growth cannot be assumed. The physiological electron relay remains a real mechanistic gap.

All six PAINT lineage checks found no IRD/IKR losses. Broad true terms are refined rather than rejected. No new biological-process annotations were manufactured, and no additional annotation rows were needed for this audit. Specific core complex/location roles can be inferred without claiming new target-specific localization measurements. Full acquisition files remain ignored; scoped quotations and source hashes are in ECOLI/fadE/fadE-source-analysis/enterobacterial-evidence.md.

## 2026-11-06 — PR6136 substrate and acceptor dimensions

Chain-resolved proposed activities retain the supported substrate classes independently of the unresolved net acceptor. Bound FAD is not evidence that the net reaction uses a flavin acceptor. Artificial-acceptor turnover, native growth and exact strain/construct evidence remain distinct. See the round1 source adjudication for ontology and primary-source comparisons.
