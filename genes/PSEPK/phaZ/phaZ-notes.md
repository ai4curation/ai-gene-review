# phaZ Gene Review Notes

## Identifier Mapping

- In KT2440, the literature gene name `phaZ` maps to locus `PP_5004` and UniProt `Q88D24`, even though the UniProt gene line currently says `Name=phaB`. [file:PSEPK/phaZ/phaZ-uniprot.txt, "SubName: Full=Poly(3-hydroxyalkanoate) depolymerase"; "GN   Name=phaB"; "GN   OrderedLocusNames=PP_5004"; "DR   ESTHER; psepu-PHAZ; PHA_depolymerase_arom."]

## Core Function

- PhaZ is the intracellular granule-associated depolymerase that mobilizes stored medium-chain-length PHA in KT2440. [JBC 2007 PDF, "first formal biochemical evidence that PhaZ is certainly an intracellular mcl-PHA depolymerase"; https://pdfs.semanticscholar.org/ae3e/1d24baa56e7222a02f12b2b3b75ee84cee02.pdf]
- Biochemical work on the highly similar KT2442 ortholog showed that 3-hydroxyoctanoate monomer is the main hydrolysis product and classified PhaZ as an endo/exo-mcl-PHA depolymerase. [JBC 2007 PDF, "the monomer of HO was identified as the main product of PhaZ hydrolysis"; "classify PhaZ as an endo/exo-mcl-PHA depolymerase"; https://pdfs.semanticscholar.org/ae3e/1d24baa56e7222a02f12b2b3b75ee84cee02.pdf]
- The best current molecular-function term is GO:0050527 poly(3-hydroxyoctanoate) depolymerase activity rather than triacylglycerol lipase activity. [AmiGO GO:0050527, "poly(3-hydroxyoctanoate) depolymerase activity"; https://amigo.geneontology.org/amigo/term/GO%3A0050527]

## Physiological Role

- Deletion of phaZ increases and stabilizes PHA accumulation, showing that PP_5004 participates in poly(3-hydroxyalkanoate) metabolic process in vivo. [PMC3918157, "the Delta phaZ knockout phenotype suggests that the PhaZ depolymerase is a major determinant of PHA accumulation and maintenance in the cell"; https://pmc.ncbi.nlm.nih.gov/articles/PMC3918157/]
- PhaZ is associated with polyhydroxyalkanoate granules rather than glycerolipid catabolism. [JBC 2007 PDF, "Identification of PhaZ as granule-associated protein"; PMC6922519, "the gene encoding the PHA depolymerase (phaZ; PP_5004) was deleted"; https://pdfs.semanticscholar.org/ae3e/1d24baa56e7222a02f12b2b3b75ee84cee02.pdf; https://pmc.ncbi.nlm.nih.gov/articles/PMC6922519/]

## GO Review Implications

- GO:0004806 triacylglycerol lipase activity is a substrate-misassigned automated annotation and should be replaced by GO:0050527. [file:PSEPK/phaZ/phaZ-uniprot.txt, "SubName: Full=Poly(3-hydroxyalkanoate) depolymerase"; AmiGO GO:0050527, "poly(3-hydroxyoctanoate) depolymerase activity"; https://amigo.geneontology.org/amigo/term/GO%3A0050527]
- GO:0046503 glycerolipid catabolic process is misleading because intracellular PHA mobilization is not glycerolipid catabolism; GO:0042620 poly(3-hydroxyalkanoate) metabolic process is closer, but GO currently lacks a direct poly(3-hydroxyalkanoate) catabolic process term for intracellular PHA mobilization. [AmiGO term graph, "GO:0042620 poly(3-hydroxyalkanoate) metabolic process"; JBC 2007 PDF; https://amigo.geneontology.org/amigo/term/GO%3A0008152; https://pdfs.semanticscholar.org/ae3e/1d24baa56e7222a02f12b2b3b75ee84cee02.pdf]
