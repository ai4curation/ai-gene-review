# CBR1 review notes

## Family context

CBR1 and CBR3 are the two reviewed human members of PTHR43963. PANTHER places
CBR1 in PTHR43963:SF2 and CBR3 in PTHR43963:SF3. PAINT asserts broad
oxidoreductase activity at the eukaryotic root and carbonyl reductase activity
at the eumetazoan carbonyl-reductase node; it does not currently assert the
CBR1-specific prostaglandin, S-nitrosoglutathione or glucocorticoid reactions.

`just paint-losses human CBR1` found no IRD or IKR loss on the human CBR1
lineage.

## Evidence notes

- `just deep-research-falcon human CBR1 --fallback perplexity-lite` was
  attempted on 2026-11-28, but neither falcon nor perplexity was available from
  the configured provider list. The review therefore uses the UniProt entry, the
  fetched GOA rows, cached primary literature, Reactome and the existing
  prostanoid module.
- All CBR1 protein-binding GOA rows in this family are bare GO:0005515 IPI rows
  from high-throughput interactome screens and do not identify a molecular
  function more specific than the policy-excluded root protein-binding term.
- The CBR1 extracellular exosome/extracellular vesicle HDA rows are
  high-throughput proteomic body-fluid detections and are peripheral to the
  curated cytosolic short-chain reductase activity; they do not establish CBR1
  as a resident vesicle or secreted enzyme.
- PMID:19442656 is abstract-only in the publication cache and foregrounds
  AKR1C3 in 9,10-phenanthrenequinone redox cycling. Its abstract also describes
  a comparison of 9,10-phenanthrenequinone reduction among ten human reductases,
  so the CBR1 quinone-reductase row is retained based on orthogonal CBR1 quinone
  assays rather than treated as a wrong-gene assertion.
- The Caco-2 epithelial-differentiation row is an expression response in a
  differentiating intestinal cell-line model, not evidence that CBR1 executes
  epithelial cell differentiation.
- Menadione is vitamin K3 and a useful model quinone substrate, but the reviewed
  CBR1 evidence did not establish a direct role in physiological vitamin K
  metabolism.
