# CANAL ESA1 manual review notes

## 2026-10-10

`just fetch-gene CANAL ESA1` seeded 48 GOA rows for UniProtKB `Q5A7Q2`, a
reviewed Candida albicans ESA1/MYST histone acetyltransferase in PANTHER
`PTHR10615:SF218` (`HISTONE ACETYLTRANSFERASE ESA1`).

The local PAINT cache has two IBA nodes that matter for this review:

- `PANTHER:PTN000834946`: fungal ESA1-node `GO:0010485 histone H4
  acetyltransferase activity`, seeded by `CGD:CAL0000179231`,
  `SGD:S000005770`, and `UniProtKB:C8VBH4`.
- `PANTHER:PTN004172926`: broad eukaryotic MYST node with chromatin, nucleus,
  chromatin-binding, transcription-coregulator, and Pol II regulation calls.

Deep research via `falcon` with `perplexity-lite` fallback could not run because
no provider API keys are configured. I therefore used the cached full text for
PMID:18685084 and PMID:23355007 plus a web/PubMed search for the newer direct
Candida ESA1 papers.

Newer literature search found two 2025 publications already present as CGD
references:

- PMID:40795216, *Genetics*: "Histone acetylation by SAGA complex but not by
  NuA4 complex is required for filamentation program in Candida albicans." The
  local cache has the abstract only. The abstract and journal page show that the
  paper created an `Esa1E372Q` catalytic mutant; the mutant lowers bulk H4
  acetylation and forms filaments constitutively, while H4 acetylation at the
  assayed hyphal promoters is Gcn5/SAGA-dependent.
- PMID:40988556, *Acta Biochim Biophys Sin*: "Yaf9 conditionally contributes to
  cell size control in Candida albicans." The cached PubMed record has no
  abstract, and a web search did not recover ESA1-specific text. The CGD
  `GO:1900239 regulation of phenotypic switching` row is therefore left
  `UNDECIDED`, per the abstract-only/full-text caution.

Main row-level calls:

- Keep all six IBA rows. `PTN000834946` is the fungal ESA1 branch and Q5A7Q2 is
  itself the CGD seed on that PAINT node; the five `PTN004172926` rows are broad
  root-MYST calls but fit the conserved chromatin HAT role.
- Accept the direct CGD H4, H4K5, H4K12, and NuA4 rows. Wang et al. 2013 show
  the C. albicans ESA1 null strongly lowers H4K5ac/H4K12ac. The H4K16 row is
  weaker in the single mutant, but the sas2/sas2 ESA1-depletion strain loses
  H4K16ac, so it is a redundant activity rather than a wrong row.
- Keep the direct filamentous-growth rows as non-core. ESA1 deletion blocks
  filamentation, while the 2025 `Esa1E372Q` catalytic mutant forms filaments
  constitutively under noninducing conditions.
- Keep broad DNA-damage and cellular-stress rows as non-core. Both the 2013 null
  mutant paper and the 2025 catalytic-mutant paper support Esa1-dependent
  resistance to genotoxic stress, but these remain downstream of the chromatin
  HAT activity rather than distinct enzymatic functions.
- Remove `GO:0000786 nucleosome`: Esa1 acts on nucleosomes but is not itself a
  nucleosome component.
- Modify `GO:0032777 piccolo histone acetyltransferase complex` to
  `GO:0035267 NuA4 histone acetyltransferase complex`; the latter has a direct
  CGD row and is the complex Lu et al. analyze in Candida.
- Mark or remove budding-yeast-specific EnsemblCompara process rows for rDNA
  heterochromatin, triglyceride biosynthesis, and macroautophagy rather than
  letting them stand as Candida ESA1 biology.
