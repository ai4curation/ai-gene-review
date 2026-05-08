# bcp (Peroxiredoxin Bcp) - Research Notes

## Gene Identity

- **UniProt**: P0AE52 (BCP_ECOLI)
- **Gene**: bcp (b2480, JW2465)
- **Organism**: Escherichia coli K12
- **EC**: 1.11.1.24 (thioredoxin-dependent peroxiredoxin)
- **Full name**: Peroxiredoxin Bcp; Bacterioferritin comigratory protein
- **Size**: 156 aa, 17.6 kDa, monomer

## Peroxiredoxin Family Classification

BCP belongs to the BCP/PrxQ subfamily of peroxiredoxins. Based on PubMed article retrieval, Nelson et al. (2011) [PMID:21287625 "existence and location of the resolving cysteine vary in some subfamilies (e.g., Prx5) to a greater degree than previously appreciated"] established the PREX classification system defining six Prx subfamilies: AhpC/Prx1, BCP/PrxQ, Prx5, Prx6, Tpx, and AhpE. E. coli BCP is a founding member of the BCP/PrxQ subfamily.

Note on nomenclature: UniProt states "Belongs to the peroxiredoxin family. BCP/PrxQ subfamily." The PREX database (Soito et al. 2011, PMID:21036863) formally classifies Prx subfamilies. BCP/PrxQ is distinct from Prx5, though both can function as atypical 2-Cys Prxs.

## Key Publications (Verified via PubMed)

### PMID:10644761 - Jeong et al. 2000 (J Biol Chem)
"Thioredoxin-dependent hydroperoxide peroxidase activity of bacterioferritin comigratory protein (BCP) as a new member of the thiol-specific antioxidant protein (TSA)/Alkyl hydroperoxide peroxidase C (AhpC) family."
- First characterization of BCP as a thiol peroxidase
- Thioredoxin-dependent activity demonstrated
- BCP "preferentially reduced linoleic acid hydroperoxide rather than H(2)O(2) and t-butyl hydroperoxide"
- Cys-45 mutation (C45S) caused "complete loss of thiol peroxidase activity"
- BCP is a monomer; Cys-45 exists as cysteine sulfenic acid
- "BCP was induced 3-fold by the oxidative stress given by changing the growth conditions from the anaerobic to aerobic culture"
- bcp null mutant: "grew more slowly than its wild type in aerobic culture and showed the hypersensitivity toward various oxidants"
- IDA evidence for GO:0008379 thioredoxin peroxidase activity
- IMP evidence for GO:0006979 response to oxidative stress

### PMID:19298085 - Clarke et al. 2009 (Biochemistry)
"Interrogating the molecular details of the peroxiredoxin activity of the Escherichia coli bacterioferritin comigratory protein using high-resolution mass spectrometry."
- Classified E. coli BCP as an "atypical 2-Cys peroxiredoxin"
- "A transient sulfenic acid is initially formed on Cys-45, before resolution by the formation of an intramolecular disulfide bond between Cys-45 and Cys-50"
- C50S mutant "adopts a different and novel mechanistic pathway" -- intermolecular disulfide with second BCP molecule
- Both pathways are substrates for thioredoxin reduction

### PMID:21910476 - Reeves et al. 2011 (Biochemistry)
"Kinetic and thermodynamic features reveal that Escherichia coli BCP is an unusually versatile peroxiredoxin."
- BCP is a monomer by analytical ultracentrifugation (both oxidized and reduced)
- Uses multiple reducing substrates: Trx1, Trx2, Grx1, and Grx3
- "high redox potential of -145.9 +/- 3.2 mV, the highest to date observed for a Prx"
- "broad peroxide specificity, with comparable rates for H(2)O(2) and cumene hydroperoxide"
- pKa of ~5.8 for peroxidatic Cys45
- Nonsaturable interaction with Trx1 (Km > 100 uM), consistent with ping-pong mechanism
- BCP described as potentially "a defense enzyme of last resort" -- remains active under highly oxidizing conditions
- NOTE: This contradicts PMID:10644761 on substrate preference. Jeong et al. found preference for linoleic acid hydroperoxide; Reeves et al. found broad specificity with comparable rates for H2O2 and cumene hydroperoxide. Different assay conditions may explain this.

### PMID:15911532 - Lopez-Campistrous et al. 2005 (Mol Cell Proteomics)
- Large-scale E. coli K-12 proteome localization study
- BCP detected in cytosol fraction by 2D-gel/MS
- Basis for IDA annotation to GO:0005829 cytosol

### PMID:18304323 - Ishihama et al. 2008 (BMC Genomics)
- Protein abundance profiling of E. coli cytosol
- BCP identified in cytosolic fraction
- Independent confirmation of cytosolic localization
- Basis for second IDA annotation to GO:0005829 cytosol

### PMID:20078128 - Clarke et al. 2010 (Biochemistry)
"Subdivision of the bacterioferritin comigratory protein family of bacterial peroxiredoxins based on catalytic activity."
- Subdivides BCP family into two classes: atypical 2-Cys (like E. coli BCP with resolving Cys) and 1-Cys (like B. cenocepacia BCP lacking resolving Cys)
- E. coli BCP uses atypical 2-Cys pathway (intramolecular disulfide Cys45-Cys50)
- 1-Cys BCPs prefer glutathione/glutaredoxin as redox partners; 2-Cys BCPs prefer thioredoxin

### PMID:20173000 - Hicks et al. 2010 (J Bacteriol)
- Characterized BCP homolog in Coxiella burnetii
- Demonstrated DNA-binding activity for Coxiella BCP
- Complementation of E. coli bcp mutant confirmed functional conservation

### PMID:10998352 - Kong et al. 2000 (Biochem J)
"A novel peroxiredoxin of the plant Sedum lineare is a homologue of Escherichia coli bacterioferritin co-migratory protein (Bcp)."
- Named the plant homolog "PrxQ" -- origin of the BCP/PrxQ subfamily name
- PrxQ complemented E. coli bcp mutant
- Two conserved cysteines (Cys-44, Cys-49) essential for activity

## E. coli Thiol Peroxidase Network

E. coli has three peroxiredoxins:
1. **AhpC** (AhpC/Prx1 subfamily) - the major scavenger of endogenous H2O2
2. **Tpx** (Tpx subfamily) - thiol peroxidase, primarily periplasmic
3. **BCP** (BCP/PrxQ subfamily) - versatile peroxiredoxin, cytosolic

BCP is distinct from AhpC in several ways: it is monomeric (AhpC forms decamers), has higher redox potential, broader substrate/reductant versatility, and lower abundance. The "enzyme of last resort" model (Reeves et al. 2011) suggests BCP may be particularly important under severe oxidative stress when other systems are comprommed.

## BioReason Assessment Notes

The BioReason deep research file is reasonable but has several issues:
1. States BCP has "a preference for hydrogen peroxide" -- this is oversimplified. Jeong 2000 found preference for linoleic acid hydroperoxide; Reeves 2011 found broad specificity. The BioReason summary in the functional summary section correctly says "with a preference for hydrogen peroxide" but this is based on Reeves et al.'s findings at physiological Trx concentrations, not universal.
2. The "Functional coupling with alkyl hydroperoxide reductase complexes (AhpC/AhpF-type)" is speculative -- no direct evidence for coordination.
3. "Regulatory crosstalk with the accessory protein for GcvA" is speculative -- the bcp gene is adjacent to gcvR on the chromosome but no functional coupling is established.
4. The BioReason file has NO GO term predictions in the MF/BP/CC sections -- this is unusual.
5. The thinking trace is domain-architecture-focused and does a reasonable job connecting domains to function.

## Key Issues for Review

- The GOA file is missing GO:0032843 (hydroperoxide reductase activity) which is annotated IDA in UniProt DR lines from EcoCyc but absent from the QuickGO download. This may be a GOA filtering issue. It is a valid annotation.
- GO:0008379 (thioredoxin peroxidase activity) appears twice: IBA and IDA. Both are appropriate.
- GO:0005829 (cytosol) appears twice from two independent IDA studies. Both are valid.
- GO:0140824 (thioredoxin-dependent peroxiredoxin activity) is more specific than GO:0008379 and represents the EC 1.11.1.24 reaction.
