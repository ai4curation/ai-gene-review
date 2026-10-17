# GDB1 (YPR184W, Q06625) notes

Glycogen debranching enzyme; bifunctional 4-alpha-glucanotransferase (EC 2.4.1.25) + amylo-alpha-1,6-glucosidase (EC 3.2.1.33). Module context: glycogen_metabolism_fungal (glycogen catabolism).

- Homology: "is 34-39% identical to the mammal, Drosophila melanogaster and Caenorhabditis elegans glycogen debranching enzyme" [PMID:11094287]
- Both activities measured: "Reliable measurement of alpha-1,4-glucanotransferase and alpha-1, 6-glucosidase activity of the yeast debranching enzyme was determined in strains overexpressing YPR184w" [PMID:11094287]
- Transferase prefers maltosyl units: "preferentially transferred maltosyl units than maltotriosyl" [PMID:11094287]
- Genetics: "Deletion of YPR184w prevents glycogen degradation, whereas overexpression had no effect on the rate of glycogen breakdown" [PMID:11094287]
- Regulation: "Yfr017p inhibits Gdb1p activity in vitro" (Igd1) [PMID:21585652]
- Location: cytosolic glycogenolysis "by glycogen phosphorylases (Gph1) and glycogen debranching enzyme (Gdb1) in the cytosol" [PMID:38832010]. Mitochondrial proteome hits (PMID:14576278, PMID:16823961) and UniProt "Mitochondrion" [UniProt:Q06625] treated as over-annotation.

## Curation decisions
- InterPro2GO IPR006421 -> glycogen biosynthetic process: REMOVE (catabolic enzyme).
- ARBA generic hydrolase, IEA carbohydrate metabolic process: MODIFY to specific terms.
- YeastPathways: assigns EC 3.2.1.33 and EC 2.4.1.25 steps; both correct.
