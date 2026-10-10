# CANAL CHS7 review notes

## Literature and source search

- `just deep-research-falcon CANAL CHS7 --fallback perplexity-lite` could not run in this
  workspace because no `agentapi` executable or Falcon/Perplexity/OpenAI API keys were
  available.
- `just fetch-gene-pmids CANAL CHS7` found the single direct PMID already seeded from CGD,
  PMID:16079341.
- Manual PubMed/web searches for `Candida albicans CHS7`, `CAL0000175393`, `Q5AA40`,
  and recent `CHS7` plus `Candida albicans` papers recovered the direct 2005 deletion
  study and a direct 2007 promoter-heterozygosity follow-up. Newer papers mentioning
  `CHS7` were primarily cell-wall-stress or antifungal-response expression studies and did
  not add direct CHS7 function evidence.
- PMID:16079341 is the key direct CGD paper for CaChs7. The cached record is abstract-only,
  but the abstract explicitly reports that "most chitin synthesis in Candida albicans,
  one of the fungi most commonly isolated from opportunistic mycoses and infections,
  depends on CHS7"; that `C. albicans chs7` null mutants have "reduced levels of chitin
  and CS activity"; that yeast cells have minor septum defects and "an increased tendency
  to form filaments"; and that mutant hyphae "were very curved and had irregular lateral
  walls" with reduced murine virulence and a high clearance rate [PMID:16079341, Candida
  albicans strains deficient in CHS7, a key regulator of chitin synthase III, exhibit
  morphogenetic alterations and attenuated virulence.].
- PMID:17559412 is the only CHS7-specific follow-up found in PubMed. It supports the same
  CHS7-to-chitin and CHS7-to-morphology connection by showing that natural promoter
  heterozygosity in SC5314 changes CaCHS7 transcript output and that the lower-expressing
  allele caused "reduced levels of chitin, a partial resistance to calcofluor, and a
  moderate degree of morphogenetic alterations in hypha-inducing media" [PMID:17559412,
  Promoter heterozygosity at the Candida albicans CHS7 gene is translated into differential
  expression between alleles.].

## PAINT and GOA interpretation

- `interpro/panther/PTHR35329/PTHR35329-entries.csv` places C. albicans CHS7/Q5AA40, S.
  cerevisiae CHS7/P38843, and N. crassa CSE-7/Q7SB92 in subfamily `PTHR35329:SF2`.
- `interpro/panther/PTHR35329/PTHR35329-paint.tsv` has a single fungal CHS7 ancestor,
  `PTN002175570`, with IBD assertions for endoplasmic reticulum membrane, chitin biosynthetic
  process, protein folding, and protein folding chaperone activity.
- Q5AA40's own CGD identifier, `CGD:CAL0000175393`, is a seed for the 2026
  `GO:0006031 chitin biosynthetic process` IBD at `PTN002175570`. That is legitimate
  self-support for PAINT, not circularity: the CGD experimental row grounds the node and the
  IBA says the function is inherited in the fungal CHS7 family.

## Curation decisions

- The conserved role is the same client-specific export-chaperone function seen in budding
  yeast and Neurospora: CHS7/Chs7 is a multipass ER membrane protein that promotes productive
  folding/export of class IV chitin synthase and thereby enables normal chitin synthesis.
- The Candida GOA file has direct phenotype rows for chitin biosynthesis, filamentous growth,
  and flocculation from an abstract-only CGD paper. The abstract confirms chitin and hyphal
  morphogenesis defects, but full-text inspection would be needed to separate the two
  flocculation rows and to verify exactly how CGD distinguished broad filamentous growth from
  negative regulation of filamentous growth of a population.
