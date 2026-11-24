# HAO2 (Q9NYQ3) review notes

## 2026-11-24

- Deep research could not be generated in this sparse checkout: `falcon` and the
  `perplexity-lite` fallback were unavailable to `deep-research-client`. I therefore
  reviewed HAO2 from the freshly fetched UniProt/GOA files, the cached GOA PMID
  references, Reactome records, PANTHER entries, and the completed HAO1 sibling review.
- HAO2/HAOX2 is a compact sibling of HAO1. PMID:10777549 is the key primary paper:
  it reports that HAOX1, HAOX2 and HAOX3 encode peroxisomal 2-hydroxy-acid oxidases,
  that HAOX2 is expressed mainly in liver and kidney, and that HAOX2 has highest
  activity toward 2-hydroxypalmitate. The cache is abstract-only but names HAOX2
  directly.
- UniProt curates HAO2 as inactive on glycolate and glyoxylate, separating it from
  HAO1/glycolate oxidase. HAO2 therefore should not inherit the HAO1 PAINT glycolate
  catabolic process or glyoxylate oxidase activity rows at `PANTHER:PTN008948292`.
- The two Reactome cytosol TAS rows come from PEX5 cargo binding/translocation events,
  as in HAO1. They describe the transient cytosolic cargo pool for a matrix enzyme,
  so they over-annotate transit rather than a mature cytosolic HAO2 function.
- No HAO2 production GO-CAM is indexed in `gocams/index.tsv`; Reactome covers the
  single HAO2 2-hydroxypalmitate oxidation reaction. The existing
  `glyoxylate_oxalate_metabolism` module is intentionally HAO1/glyoxylate-specific,
  so HAO2 does not extend it.
