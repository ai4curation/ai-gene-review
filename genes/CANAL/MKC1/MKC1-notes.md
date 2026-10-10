# MKC1 curation notes

## 2026-10-10

- Fetched the `CANAL/MKC1` review, GOA, UniProt, and nine GOA-cited
  publications for the fungal PTHR24055 MAPK PAINT project.
- Deep research via Falcon with `perplexity-lite` fallback could not run in this
  environment because no provider API key was configured. The review therefore
  used the cached primary publications, UniProt, the local PTHR24055 PAINT
  export, the annotation-reviewer pass over all 34 seeded rows, and a fresh
  literature search for newer `MKC1`/`Mkc1` papers.
- Accepted the direct Candida cell-wall-integrity biology for Mkc1:
  complementation of *S. cerevisiae* `slt2`, `mkc1` weak-cell-wall and heat
  phenotypes, Mkk2-dependent Mkc1 phosphorylation after oxidative and cell-wall
  stresses, contact-dependent invasive filamentation and biofilm maturation, and
  caspofungin-induced chitin synthesis and beta-glucan unmasking.
- Accepted the `PANTHER:PTN001171896` IBA for `GO:0004707` MAP kinase activity.
  MKC1 itself is one of the Candida CGD seeds at this fungal PAINT node, and the
  node transfers only the conserved MAPK catalytic function.
- Accepted the broader `PANTHER:PTN000622075` IBA rows for nucleus, cytoplasm,
  and intracellular signal transduction as broad MAPK-family placements. These
  were not scored as weak because the ancestral PAINT placement, not donor
  count, is the evidence that matters.
- Removed the four EnsemblFungi/Compara transfers that point from the
  fission-yeast cell-integrity MAPK Spm1 to *C. albicans* Mkc1 for calcium
  signaling/import, mitotic cytokinesis, and glucose-mediated signaling. These
  are not PAINT rows and overextend Spm1-specific process outputs to a Candida
  MAPK whose direct literature supports cell-wall integrity, contact responses,
  and caspofungin-induced cell-wall remodeling instead.
- Modified the generic `filamentous growth` row from the 2005 surface-contact
  paper to `GO:0036267 invasive filamentous growth`, because the assay tested
  agar invasion by colonies. Modified the direct biofilm-formation row to the
  existing `GO:1900231 regulation of single-species biofilm formation on
  inanimate substrate`, because `mkc1` mutants adhered normally at 4 h but
  formed abnormal 48 h biofilms with reduced filamentation.
- Modified the `cellular response to reactive oxygen species` row from the 2005
  infection paper to `GO:0071732 cellular response to nitric oxide`; the cached
  abstract supports nitric-oxide sensitivity and macrophage NO effects, not a
  reactive-oxygen-species assay.
- Kept the 2005 and 2010 caspofungin rows as non-core xenobiotic outputs of the
  same wall-integrity pathway. A current literature search found newer work on
  paradoxical growth and pathway activation that agrees with the MKC1
  caspofungin connection, but the existing cached caspofungin and 2023 chitin
  papers were already sufficient for the GOA rows reviewed here.
