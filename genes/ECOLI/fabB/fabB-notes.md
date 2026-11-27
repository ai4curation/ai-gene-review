# fabB (Escherichia coli K-12, P0A953) curation notes

## 2026-11-13

- FabB is 3-oxoacyl-ACP synthase I (KAS I). Its unique role is to elongate
  the cis-3-decenoyl-ACP made by FabA
  [PMID:19679654 "These data indicate that the key reaction in UFA synthesis catalyzed by FabB is elongation of the cis-3-decenoyl-ACP produced by FabA."],
  and fabB mutants need unsaturated fatty acids
  [PMID:19679654 "Strains lacking FabB are UFA auxotrophs indicating that the enzyme catalyzes an essential step in UFA synthesis."].
- Partitioning into the unsaturated branch depends on FabB's affinity for the
  FabA product, not on a FabA-FabB complex
  [PMID:8910376 "the channeling of intermediates toward unsaturated fatty acid synthesis by FabB was attributed to the affinity of the condensing enzyme for cis-decenoyl-ACP"].
- The NEW GO:0006636 row is not redundant with the accepted GO:1903966
  (monounsaturated fatty acid biosynthetic process). In the current GO
  release (local go.db, checked 2026-11-14) GO:1903966 has the single direct
  parent GO:0006633, and GO:0006636 is not among its is_a ancestors.
- Used as the FabA/FabB-route exemplar in
  `modules/bacterial_unsaturated_fatty_acid_biosynthesis.yaml`, beside the
  P. putida KT2440 ortholog Q88FC3; family placement PTHR11712:SF306.
