# HAL (Histidine ammonia-lyase / histidase) — review notes

UniProt: P42357 (HUTH_HUMAN); gene HAL (syn. HIS); HGNC:4806; GeneID 3034;
chromosome 12q. 657 aa. EC 4.3.1.3. Evidence at protein level (PE 1).

## Core biology

- **Molecular function.** Histidine ammonia-lyase (histidase): catalyzes the
  non-oxidative deamination of L-histidine to trans-urocanate + ammonia.
  [file:human/HAL/HAL-uniprot.txt "RecName: Full=Histidine ammonia-lyase;"]
  [file:human/HAL/HAL-uniprot.txt "Reaction=L-histidine = trans-urocanate + NH4(+); Xref=Rhea:RHEA:21232,"]
  Core MF term = **GO:0004397 histidine ammonia-lyase activity** (label verified
  current in local go.db; MF branch confirmed via entailed ancestors).

- **Catalytic mechanism.** Uses an autocatalytically formed MIO
  (4-methylideneimidazol-5-one) prosthetic group, made by cyclization/dehydration
  of an internal Ala-Ser-Gly tripeptide (crosslink FT 253..255; MOD_RES 254
  2,3-didehydroalanine).
  [file:human/HAL/HAL-uniprot.txt "Contains an active site 4-methylidene-imidazol-5-one (MIO), which"]

- **Pathway / BP.** First step (step 1/3) of L-histidine degradation to
  L-glutamate.
  [file:human/HAL/HAL-uniprot.txt "glutamate; N-formimidoyl-L-glutamate from L-histidine: step 1/3."]
  Core BP term = **GO:0006548 L-histidine catabolic process** (current; BP branch
  confirmed). Note: UniProt DR lines also carry GO:0019556 / GO:0019557
  ("...to glutamate and formamide/formate"), but both are now **obsolete** in
  go.db and are NOT in the GOA-seeded existing_annotations, so not used.

- **Location.** Soluble cytosolic enzyme (homotetramer). Reactome localizes to
  cytosol. Core CC = **GO:0005829 cytosol** (CC branch confirmed); the InterPro
  IEA "cytoplasm" (GO:0005737) is the less-specific parent.
  [Reactome:R-HSA-70899 "Cytosolic histidine ammonia lyase (HAL) catalyzes the reaction of histidine to form urocanate and NH4+"]

- **Expression.** Group-enriched in liver and skin.
  [file:human/HAL/HAL-uniprot.txt "Group enriched (liver, skin)"] Epidermal
  urocanate (the product) is a major UV chromophore of the stratum corneum
  (background biology, not separately quoted).

- **Family.** PAL/histidase (aromatic amino acid ammonia-lyase) family; shares
  the MIO mechanism with phenylalanine ammonia-lyase.
  [file:human/HAL/HAL-uniprot.txt "Belongs to the PAL/histidase family."]

- **Disease.** Histidinemia (HISTID; MIM 235800), autosomal recessive, caused by
  HAL loss of function; elevated histidine, decreased urocanate.
  [file:human/HAL/HAL-uniprot.txt "Histidinemia (HISTID) [MIM:235800]: Autosomal recessive"]
  [PMID:15806399 "and decreased urocanic acid in blood and skin and results from histidase"]
  Four disease missense mutations (R322P, P259L, R206T, R208L) in the human HAL
  gene were the first coding-region mutations reported.
  [PMID:15806399 "report describes the first mutations occurring in the coding region of the"]

## Annotation review summary

Actions (13 existing annotations):
- ACCEPT (7): GO:0004397 IBA, GO:0004397 IEA, GO:0004397 EXP (core MF);
  GO:0006548 IBA, GO:0006548 IEA, GO:0006548 TAS (core BP); GO:0005829 cytosol TAS
  (core CC).
- MARK_AS_OVER_ANNOTATED (5): GO:0003824 catalytic activity IEA (root),
  GO:0016841 ammonia-lyase activity IEA (parent of specific MF), GO:0005515
  protein binding IPI x2 (RPS19BP1/Q86WX3 high-throughput), GO:0031670 cellular
  response to nutrient IEA (ortholog-transferred, vague/non-core).
- MODIFY (1): GO:0005737 cytoplasm IEA -> GO:0005829 cytosol (more specific;
  matches Reactome CC).

Note per curation policy: the two GO:0005515 "protein binding" IPI annotations
are experimental (IPI) — marked OVER_ANNOTATED, not REMOVED. The single interactor
in both screens is RPS19BP1 (Q86WX3), matching the UniProt INTERACTION line
(NbExp=2). No established biological role for a HAL-RPS19BP1 interaction.

## Reference notes

- PMID:15806399 — histidinemia mutation study; abstract-only cache
  (full_text_available: false). PubMed-verified. Supports core MF + disease link
  (genetic evidence, not a direct in vitro kinetic assay).
- PMID:33961781 (BioPlex 3.0) and PMID:40205054 (multimodal U2OS cell map) —
  proteome-scale interactome screens; source of the two "protein binding" IPI
  annotations to RPS19BP1. The literal "HAL" occurrences in PMID:40205054 full
  text are the "HALT protease inhibitor" reagent, not the gene.
- Reactome R-HSA-70899 (reaction) and R-HSA-70921 (pathway) — cached; titles left
  exactly as fetched.
