# GUSB (Beta-glucuronidase, P08236) — review notes

## Summary of gene function

GUSB encodes **beta-glucuronidase** (EC 3.2.1.31), a lysosomal exoglycosidase of the
glycoside hydrolase family 2 (GH2). It hydrolyses terminal, non-reducing beta-D-glucuronic
acid residues from glycosaminoglycans (GAGs) as part of the stepwise exolytic lysosomal
degradation of heparan sulfate, dermatan sulfate, chondroitin sulfate, and hyaluronan.

- Catalytic reaction (UniProt / Rhea RHEA:17633): `a beta-D-glucuronoside + H2O = D-glucuronate + an alcohol`, EC=3.2.1.31 [ECO:0000305|PubMed:3355537]. `file:human/GUSB/GUSB-uniprot.txt`
- UniProt FUNCTION: "Plays an important role in the degradation of dermatan and keratan sulfates." `file:human/GUSB/GUSB-uniprot.txt`
- SUBUNIT: Homotetramer. SUBCELLULAR LOCATION: Lysosome. `file:human/GUSB/GUSB-uniprot.txt`
- SIMILARITY: Belongs to the glycosyl hydrolase 2 family. CAZy: GH2. `file:human/GUSB/GUSB-uniprot.txt`
- Active site Asp451 (proton donor); N-glycosylated (Asn173, 272, 420, 631). PDB 1BHG, 3HN3 (homotetramer). `file:human/GUSB/GUSB-uniprot.txt`
- Cloned/sequenced from human placenta; EC 3.2.1.31 = beta-D-glucuronoside glucuronosohydrolase [PMID:3468507 "the cDNA sequence for human placental beta-glucuronidase (beta-D-glucuronoside glucuronosohydrolase, EC 3.2.1.31)"].

## Substrate breadth (glycosaminoglycans)

[PMID:7354065 "Both forms of these enzymes are active on 4-methyl umbelliferyl-beta-D-glucuronide and on the hexasaccharides of chondroitin-6-SO4, chondroitin, and hyaluronic acid"] — purified human placental beta-glucuronidase acts on chondroitin-6-SO4, chondroitin, and hyaluronic acid oligosaccharides. This underpins the chondroitin/dermatan sulfate and hyaluronan catabolic-process annotations, and is the IDA (PMID:7354065, assigned by MGI) support for the catalytic activity and hyaluronan catabolism annotations.

## Disease

Inherited deficiency causes **Mucopolysaccharidosis type VII (Sly syndrome)**, an autosomal
recessive lysosomal storage disease with GAG accumulation; phenotype ranges from lethal
hydrops fetalis to mild adult forms. `file:human/GUSB/GUSB-uniprot.txt` (DISEASE: MPS7, MIM:253220);
also demonstrated in the murine model [PMID:1465145 "An inherited deficiency of beta-glucuronidase in humans, mice and dogs causes mucopolysaccharidosis VII (Sly syndrome), a progressive degenerative disease ... results from lysosomal storage of undegraded glycosaminoglycans"].

## Notable non-catalytic / peripheral annotations

- **CI-MPR (mannose-6-phosphate receptor, P08169) binding** (IPI, PMID:20028034): GUSB is a
  M6P-tagged lysosomal enzyme purified on a CI-MPR affinity column in this study; the paper's
  focus is the CI-MPR's plasminogen-binding site, with GUSB used as an M6P-binding reference
  ligand. Captured as `signaling receptor binding` (GO:0005102) and `protein domain specific
  binding` (GO:0019904). These are the classic M6P-receptor/lysosomal-enzyme recognition,
  not a signaling function of GUSB — bare protein-binding terms, treated as over-annotation.
- **Extracellular / exosome / membrane / granule-lumen** CC terms come from secretion,
  neutrophil degranulation (azurophil/ficolin-1-rich granule lumen; Reactome), and large-scale
  proteomics of exosomes (PMID:23533145, PMID:19056867) and NK-cell membrane fraction
  (PMID:19946888). Real but peripheral to the core lysosomal catabolic role.

## Core function decision

- Core MF: **GO:0004566 beta-glucuronidase activity** (exact GOA term/label).
- Core BP: **GO:0006027 glycosaminoglycan catabolic process** (verified; also the more
  specific HS/CS/DS/hyaluronan catabolic processes).
- Core CC: **lysosomal lumen (GO:0043202)** / lysosome (GO:0005764).
</content>
</invoke>
