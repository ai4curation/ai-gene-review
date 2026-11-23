# fabA (PA1610, O33877) review notes

No deep-research provider was available. Sources: UniProt record (O33877),
cached PMID:9286984 (abstract only; PMC full text body not returned by the
PubMed MCP). fabB (PA1609) was reviewed earlier and shares the biology.

## Function

- Dual dehydratase/isomerase of type II FAS; the isomerase introduces cis
  unsaturation [file:PSEAE/fabA/fabA-uniprot.txt "Necessary for the introduction of
  cis unsaturation into fatty acids. Catalyzes the dehydration of
  (3R)-3-hydroxydecanoyl-ACP to E-(2)-decenoyl-ACP and then its isomerization to
  Z-(3)-decenoyl-ACP"].
- fabA/fabB cloned; chromosomal fabA mutants auxotrophic for UFA; fabAB operon
  [PMID:9286984 "the mutants were auxotrophic for unsaturated fatty acids";
  "fabA and fabB are cotranscribed"].

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN008624492 | GO:0006633 fatty acid biosynthetic process | 3 | 124 (73 taxa) | GO:0006636 unsaturated fatty acid biosynthetic process, IMP, PMID:9286984 (PseudoCAP) | SOUND | The seed is the UFA auxotrophy of fabA mutants, but for fabA phenotype and catalysis coincide: its isomerase makes the cis-3-decenoyl-ACP intermediate, the committed step of UFA synthesis. The node term is the parent GO:0006633, right for a FabA/FabZ dehydratase clade; the seed's GO:0006636 is a descendant. | E. coli FabA P0A6Q3, E. coli FabZ P0A6Q6 (and Arabidopsis AT2G22230 for the GO:0019171 IBD) | Yes; E. coli FabA and FabZ carry strong experimental support. No GO_CENTRAL defect. |

Same node also carries the GO:0019171 (3R)-hydroxyacyl-ACP dehydratase activity
IBD (P0A6Q3, P0A6Q6, AT2G22230) - sound, family-defining activity. This mirrors
the reviewed fabB (PTN000918584): a wet-lab auxotrophy that coincides with the
enzyme's own committed catalytic step, not an indirect phenotype.

PseudoCAP defects from this gene: none.
