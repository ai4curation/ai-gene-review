# APP - Amyloid Precursor Protein (Human) Notes

## Overview

Human APP (P05067) is the ortholog of mouse App. The biology is essentially identical - a type I transmembrane protein that undergoes regulated intramembrane proteolysis (RIP) to produce multiple bioactive fragments.

**Key difference from mouse**: Human APP is directly relevant to Alzheimer's disease pathology. The human Abeta sequence differs slightly from mouse, and human Abeta is more prone to aggregation. AD mouse models often use humanized APP.

## Splice Isoforms

| Isoform | UniProt | Length | Domains | Expression |
|---------|---------|--------|---------|------------|
| APP770 | P05067-1 | 770 AA | KPI + OX-2 | Peripheral, microglia |
| APP751 | P05067-6 | 751 AA | KPI only | Peripheral tissues |
| APP695 | P05067-4 | 695 AA | No KPI | Neuronal (predominant in brain) |
| L-APP677 | P05067-3 | 677 AA | No KPI | Leukocytes |
| APP305 | P05067-2 | 305 AA | Truncated | Limited data |

## Cleavage Products

Same as mouse - see mouse App notes for details:
- sAPPalpha (neuroprotective)
- sAPPbeta (less neurotrophic, DR6 binding)
- Abeta40/42 (neurotoxic, AD pathogenic)
- AICD (nuclear signaling)
- N-APP (axon pruning via DR6)

## Familial AD Mutations

Human APP mutations cause familial Alzheimer's disease by increasing Abeta42/Abeta40 ratio:

| Mutation | Position | Effect |
|----------|----------|--------|
| Swedish | K670N/M671L | Increases total Abeta |
| London | V717I | Increases Abeta42/40 ratio |
| Flemish | A692G | Increases Abeta aggregation |
| Arctic | E693G | Increases protofibril formation |
| Iowa | D694N | Increases cerebral amyloid angiopathy |

## Key Human-Specific Points

1. Human Abeta sequence at positions 5, 10, 13 differs from rodent - more aggregation-prone
2. Most AD mouse models use human APP transgenes
3. Down syndrome (trisomy 21) causes AD due to APP gene triplication on chromosome 21
4. Protective mutation (A673T, "Icelandic") reduces Abeta production and AD risk

## References

- PMID:2881207 - Original APP cloning
- PMID:8886002 - Swedish mutation characterization
- PMID:23150908 - Icelandic protective mutation

## 2026-06-20 Second-Pass Review Notes

Second-pass cleanup separated normal APP biology from Alzheimer disease mechanism
context. The review description now emphasizes full-length APP receptor/adhesion
activity, regulated proteolytic processing, APP751/770 KPI-domain protease
inhibitor activity, and copper/metal-binding biology.

Key evidence anchors:
- UniProt supports full-length APP receptor/adhesion biology: "Functions as a
  cell surface receptor" and "neuronal adhesion and axonogenesis"
  [file:human/APP/APP-uniprot.txt].
- UniProt supports APP-family synaptic adhesion output: "promotes synaptogenesis"
  [file:human/APP/APP-uniprot.txt].
- UniProt supports copper/metal biology: "Extracellular binding and reduction of
  copper" and "Amyloid-beta peptides are lipophilic metal chelators"
  [file:human/APP/APP-uniprot.txt].

Second-pass curation decisions:
- Added NEW review entries for GO:0098631 cell adhesion mediator activity,
  GO:0050839 cell adhesion molecule binding, and GO:0005507 copper ion binding
  so authored core-function terms are represented in the annotation block.
- Harmonized GO:1900272 negative regulation of long-term synaptic potentiation
  as KEEP_AS_NON_CORE. The evidence is credible for amyloid-beta cleavage-product
  effects on plasticity, but this is not the core evolved function of full-length
  APP.
- Harmonized broad GO:0051247 positive regulation of protein metabolic process
  and GO:0070555 response to interleukin-1 as MARK_AS_OVER_ANNOTATED.
- Added knowledge-gap questions and suggested experiments focused on evolved
  in-vivo APP isoform, fragment, adhesion, trophic-signaling, metal-binding, and
  intracellular-domain biology.
