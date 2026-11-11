# ach1 notes

- `ach1` is `Q9UUJ9`, the single `Schizosaccharomyces pombe` entry in `PTHR43609:SF1`. The PTHR43609 entry table places it with the fungal Ach1 proteins from `Saccharomyces cerevisiae`, `Candida albicans`, `Neurospora crassa`, and other ascomycetes.
- The PAINT family has two relevant nodes for this review. `PANTHER:PTN000484586` carries `GO:0003986` acetyl-CoA hydrolase activity, `GO:0008775` acetate CoA-transferase activity, and `GO:0006083` acetate metabolic process. `PANTHER:PTN000484602` carries the Ascomycota-scoped `GO:0005739` mitochondrion placement.
- The key biochemical update is Fleck and Brock's re-characterization of budding-yeast Ach1p: "Ach1p showed highest specific activity for the CoASH transfer from succinyl-CoA to acetate and only a minor acetyl-CoA-hydrolase activity." [PMID:19298859]
- This means the acetate CoA-transferase and acetate metabolism rows should be core `ACCEPT`, while the older acetyl-CoA hydrolase rows are defensible but secondary (`KEEP_AS_NON_CORE`) rather than false.
- Mitochondrial localization is supported three ways: S. pombe HDA from the Matsuyama ORFeome/YFP localization survey [PMID:16823372], S. cerevisiae fractionation and immunofluorescence in Buu et al. [PMID:12606555], and the `PTN000484602` Ascomycota IBA.
- The UniProt SubCell `cytoplasm` row is only a broad ancestor relative to `mitochondrion` and `mitochondrial matrix`; the generic `GO:0008410` CoA-transferase activity row is likewise only a broad parent beside `GO:0008775`.
- The ISO to `GO:0008260` succinyl-CoA:3-oxo-acid CoA-transferase activity should be removed. Its donor, `UniProtKB:P55809`, is a 3-oxo-acid CoA-transferase source, while Ach1's supported reaction is succinyl-CoA plus acetate to succinate plus acetyl-CoA.
