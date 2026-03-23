# gcd (PP_1444) - Pseudomonas putida KT2440 - Research Notes

## Gene Identity
- **UniProt:** Q88MX4 (TrEMBL, unreviewed)
- **Gene:** gcd (PP_1444)
- **Product:** Quinoprotein glucose dehydrogenase (mGDH)
- **EC:** 1.1.5.2
- **Organism:** Pseudomonas putida KT2440

## Protein Structure and Localization
- 803 amino acids, 86.6 kDa
- Membrane-bound with 5 predicted transmembrane helices (aa 12-142)
- Large periplasmic PQQ beta-propeller domain (aa 171-778) [PMID:12534463 "Complete genome sequence"]
- Belongs to bacterial PQQ dehydrogenase family (PTHR32303:SF4 = Quinoprotein Glucose Dehydrogenase)
- Domain architecture: N-terminal membrane anchor + C-terminal catalytic PQQ domain facing periplasm
- CDD: cd10280 (PQQ_mGDH) confirms membrane-bound glucose dehydrogenase classification
- InterPro: IPR017511 (PQQ_mDH), IPR018391 (PQQ_b-propeller repeat), IPR002372 (PQQ repeat domain)

## Core Enzymatic Function
- Catalyzes oxidation of D-glucose to D-glucono-1,5-lactone (spontaneously converts to gluconate) in the periplasm
- Uses PQQ (pyrroloquinoline quinone) as a tightly-bound redox cofactor (Km for PQQ <0.1 uM) [PMID:27287323]
- Electrons are transferred to ubiquinone in the membrane (connects to respiratory chain)
- Kinetics: Km for glucose = 4.91 mM, Vmax = 67.64 uM/min [PMID:27287323 "apparent Km for glucose of 4.91"]

## Role in Glucose Catabolism
P. putida uses three convergent peripheral pathways for glucose catabolism, all converging at 6-phosphogluconate [PMID:17483213]:
1. **Glucokinase pathway**: glucose -> G6P -> 6PG (cytoplasmic, via Glk + Zwf)
2. **Direct gluconate pathway**: glucose -> gluconate (via Gcd, periplasmic) -> transport -> 6PG (via GnuK)
3. **2-ketogluconate loop**: glucose -> gluconate -> 2KG (via Gad, periplasmic) -> transport -> 6PG (via KguK + KguD)

Gcd initiates pathways 2 and 3. About 50% of glucose flux goes through the 2-ketogluconate loop [PMID:20581202 "about 50% of glucose is channeled through the 2-ketogluconate peripheral pathway"].

All pathways converge at 6-phosphogluconate which feeds into the Entner-Doudoroff pathway via Edd/Eda.

## Regulation
- gcd expression is highest when glucose is the sole carbon source [PMID:27287323]
- Low phosphate conditions increase both GDH activity and PQQ levels [PMID:27287323 "highest levels of both occurring when glucose is used as the sole carbon source and under conditions of low soluble phosphate"]
- PQQ availability (not enzyme abundance) limits activity under optimal conditions [PMID:27287323]
- PtxS repressor controls compartmentalized glucose metabolism [PMID:20581202]
- GnuR represses gluconate/glucose catabolism genes

## Biological Roles
- **Phosphate solubilization**: Gluconic acid produced by Gcd chelates mineral-bound phosphates (Ca3(PO4)2, hydroxyapatite), making P available for plant uptake [PMID:27287323 "solubilize mineral phosphates by secreting gluconic acid"]
- **Rhizosphere competence**: Key for P. putida's role as rhizosphere bacterium
- **gcd mutant phenotype**: Loss of periplasmic glucose oxidation, no gluconate/2-KG accumulation, significant growth defect on glucose
- **Pyoverdine regulation**: gcd mutants show increased pyoverdine production (siderophore) due to loss of gluconic acid-mediated pH drop [PMID:23392768]

## Biotechnology Applications
- gcd deletion used to redirect glucose flux (avoid gluconate accumulation) for metabolic engineering
- Overexpression of Gcd improves bioelectrochemical system performance [PMID:28921555]
- gcd deletion used for muconic acid production engineering

## Additional Findings from Deep Research (Falcon)

- **Substrate breadth**: Gcd can oxidize mannose (from fructose isomerization) in addition to glucose, indicating broad aldose C-1 oxidation activity [Nguyen et al. 2021, DOI:10.1111/1751-7915.13862]
- **Flux dominance**: Under aerobic growth, ~90% of glucose entering the periplasm is oxidized to gluconate by Gcd [Chen et al. 2024, DOI:10.1111/1751-7915.70059]
- **GnuR regulation**: GnuR (PP_2321) is a newly characterized repressor of peripheral glucose/gluconate catabolism genes; Δgcd mutant used to distinguish glucose vs gluconate transcriptional responses [Chen et al. 2024]
- **BES applications**: Overexpression of gcd increased electron transfer rate by >4x and 2-KG production by 644% in bioelectrochemical systems [Yu et al. 2018, PMID:28921555]
- **Systems engineering**: Weimer et al. 2024 achieved 96% glucose-to-2-KG conversion (mol/mol) using metabolic engineering approaches [DOI:10.1186/s12934-024-02509-8]
- **gcd deletion phenotype**: Complete loss of gluconate/2-KG formation confirmed by Chen et al. 2024; significant growth defect on glucose

## Key References
- PMID:27287323 - An & Moe 2016 - Regulation of PQQ-dependent GDH in P. putida KT2440
- PMID:17483213 - del Castillo et al. 2007 - Convergent peripheral pathways for glucose catabolism
- PMID:20581202 - Compartmentalized glucose metabolism controlled by PtxS
- PMID:12534463 - Nelson et al. 2002 - P. putida KT2440 genome sequence
- PMID:23392768 - Ponraj et al. 2013 - Periplasmic glucose oxidation and pyoverdine synthesis
- PMID:28921555 - Yu et al. 2018 - Bioelectrochemical system with gcd overexpression
