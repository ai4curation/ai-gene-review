# COQ1 (YBR003W, P18900) notes

Hexaprenyl diphosphate synthase.

- coq1 strain lacking hexaprenyl pyrophosphate synthetase activity complemented by COQ1 [PMID:2198286 "both glycerol growth and hexaprenyl pyrophosphate synthetase activity were restored"].
- coq1 mutants expressing heterologous synthases make UQ5-UQ10 [PMID:9708911 "different types of prenyl diphosphate synthases were expressed in a S. cerevisiae COQ1 mutant defective for hexaprenyl diphosphate synthesis"].
- Peripheral, matrix side of inner membrane [PMID:15548532 "Coq1p is peripherally associated with the inner membrane on the matrix side."].
- GOA IMP GO:0000010 "heptaprenyl diphosphate synthase activity" is wrong chain length (C35 vs C30); its synonym "trans-hexaprenyltranstransferase activity" likely caused the mis-mapping. MODIFY -> GO:0036423 hexaprenyl-diphosphate synthase ((2E,6E)-FPP specific) activity, matching modules/ubiquinone_biosynthesis.yaml. Primer specificity (FPP vs GGPP) untested for yeast Coq1p; YeastPathways draws geranylfarnesyl-PP + IPP.
- UniProt has no catalytic-activity line for COQ1.
- IBA part_of polyprenyl diphosphate synthase complex: seeded from heteromeric PDSS1/2, Dps1/Dlp1; no second subunit known in S. cerevisiae -> non-core.
- protein binding IPI (Gavin 2006) -> over-annotated.
