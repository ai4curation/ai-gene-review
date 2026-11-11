# tvp-18 notes

- PubMed exact-token query on 2026-10-17 for `NCU04760`, `tvp-18`,
  `H4H7.080`, or `Q7S693` returned no hits. A broader web search found database
  and clone-catalog records for `NCU04760`, but no direct Neurospora tvp-18
  functional characterization.
- The current GOA set is inherited/mapped evidence only: PAINT propagates
  Golgi membrane from PTN001779222 and vesicle-mediated transport from
  PTN001779219, UniProtKB-SubCell maps the curated UniProt Golgi localization,
  and InterPro2GO contributes only the broad membrane term.
- I did not add a molecular-function core term or propose a NEW channel
  annotation. Drosophila Flower is experimentally characterized as a calcium
  channel in synaptic-vesicle biology, but the Neurospora record only supports
  the conserved fungal Golgi membrane localization and broad vesicle-mediated
  transport role.
- PTHR13314 now places `GO:0005262` calcium channel activity on PTN001779219,
  the same opisthokont node whose `GO:0016192` vesicle-mediated transport IBD
  is accepted here. I did not propagate that molecular-function claim to
  Neurospora because the row is seeded by Drosophila `fwe` alone, the
  ascomycete PTN001779222 subnode carries only Golgi membrane, and the
  metazoan calcium terms `GO:0070588` and `GO:0150008` sit on Eumetazoa node
  PTN000999743.
