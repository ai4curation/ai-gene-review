# glxR (P77161) tartronate semialdehyde reductase, E. coli K-12: curation notes

## Deep research

- No deep-research provider was available in this environment (perplexity attempt for the
  sibling gene gcl on 2026-10-23 failed: "Provider 'perplexity' not available. Available:
  falcon, openscientist"). Review based on cached primary literature and UniProt.

## Function

- Purified GlxR: NADH-dependent reduction of tartronate semialdehyde and NAD+-dependent oxidation of D-glycerate.
  [PMID:10978349 "The purified recombinant protein very specifically catalyzed the NAD(+)-dependent oxidation of d-glycerate and the NADH-dependent reduction of tartronate semialdehyde"]
- Operon context: downstream of hyi and gcl.
  [PMID:10978349 "producing an operon clearly designed for d-glycerate biosynthesis from tartronate semialdehyde"]
- Genetics: Tn5 mutant JA171 lacks TSR activity and was isolated as unable to use glyoxylate.
  [PMID:10601204 "strain JA171, lacking tartronic semialdehyde reductase activity"]
- Pathway: [PMID:10601204 "tartronic semialdehyde reductase, which converts the semialdehyde into glycerate"]
- Family: HIBADH-related beta-hydroxyacid dehydrogenase (UniProt; TIGR01505). Paralog GarR
  (P0ABQ2) in the galactarate pathway co-seeds the PAINT node.
- UniProt lists both NAD- and NADP-linked Rhea reactions for EC 1.1.1.60; direct E. coli data
  are NAD-linked only.

## Annotation decisions

- Core: GO:0008679 2-hydroxy-3-oxopropionate reductase activity; GO:0009436 glyoxylate catabolic process.
- MODIFY general terms (oxidoreductase activity, GO:0016616, glyoxylate metabolic process) to the specific ones.
- NAD binding and NADP binding kept non-core.
- Glycolate catabolic process kept non-core.
- REMOVE IEP DNA damage response (genome-wide microarray, ~30% of genes changed; not participation).
