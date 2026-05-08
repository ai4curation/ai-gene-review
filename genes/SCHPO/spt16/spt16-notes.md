# spt16 (S. pombe) - Research Notes

## Gene Identity
- UniProt: O94267
- PomBase: SPBP8B7.19
- Essential gene in S. pombe [PMID:17614284 "the S. pombe ortholog for the large FACT subunit, spt16+, is essential"]
- 1019 AA, chromosome II

## FACT Complex Composition in S. pombe
- Spt16 (large subunit, essential) + Pob3 (small subunit, non-essential) form the core heterodimer [PMID:17614284 "Pob3 and Spt16 associate in vivo...SDS-PAGE analysis reveals two specific bands...Mass spectrometry analysis identifies the two bands as Pob3 and Spt16"]
- In S. pombe, pob3 deletion is viable (unlike S. cerevisiae where both subunits are essential) [PMID:17614284 "a strain bearing the deletion of pob3+ is viable"]
- nhp6 associates weakly to form the complete FACT complex (by similarity to other organisms)

## Structural Biology
- Crystal structures of N-terminal "peptidase" domain at 2.05A and 1.84A (PDB: 3CB5, 3CB6) [PMID:18579787]
- N-terminal domain has aminopeptidase P fold but lacks enzymatic activity - repurposed for histone binding [PMID:18579787 "Spt16-N reveals an aminopeptidase P fold whose enzymatic activity has been lost"]
- Spt16-N binds H3-H4 through globular core domains and N-terminal tails [PMID:18579787 "the highly conserved fold directly binds histones H3-H4 through a tight interaction with their globular core domains, as well as with their N-terminal tails"]
- Spt16-M domain required for interaction with Pob3 [PMID:17614284 "the interaction requires the Spt16-M domain"]
- C-terminal acidic tail (residues 930-1019) characteristic of histone chaperones

## Core Functions

### 1. Histone Chaperone Activity
- H2A-H2B chaperone activity: directly demonstrated [PMID:31837996 EXP with contributes_to qualifier; PMID:34731638 EXP]
- H3-H4 binding via N-terminal domain [PMID:18579787]
- General histone chaperone activity [PMID:23028377 IMP]
- Maintains H3 chromatin integrity during transcription - prevents promiscuous CENP-A(Cnp1) deposition [PMID:23028377 "Mutations in the histone chaperone FACT impair the maintenance of H3 chromatin on transcribed regions and promote widespread CENP-A(Cnp1) incorporation at non-centromeric sites"]

### 2. Transcription Elongation
- Facilitates RNA Pol II passage through chromatin by transiently destabilizing nucleosomes [PMID:28218250 "facilitates the passage of RNA polymerase II and transcription by promoting the dissociation of one histone H2A-H2B dimer from the nucleosome"]
- Cooperates with Fun30/Fft3 chromatin remodeler for nucleosome disassembly at transcribing regions [PMID:28218250]
- Globally represses antisense transcripts near 5' end of genes [PMID:31837996 "FACT and H2Bub globally repress antisense transcripts near the 5' end of genes"]
- In absence of Pob3, Spt16 alone controls 3' end of genes [PMID:31837996]

### 3. Heterochromatin Functions
- Required for centromeric heterochromatin integrity, independently of RNAi [PMID:17614284 "FACT is required for centromeric-heterochromatin integrity and accurate chromosome segregation...SpFACT complex in heterochromatin integrity at centromeres"]
- Facilitates heterochromatin spreading by regulating histone turnover and H3K9 methylation states [PMID:34731638 "FACT promotes spreading by repressing heterochromatic histone turnover, which is crucial for the H3K9me2 to me3 transition that enables spreading"]
- Constitutive heterochromatin formation role demonstrated by IMP [PMID:34731638]
- Concentrates on euchromatin but affects heterochromatin boundaries [PMID:34731638]

### 4. Chromatin Organization and Genome Architecture
- Maintains nucleosomes in subtelomeric regions, crucial for their compaction [PMID:31837996 "FACT maintains nucleosomes in subtelomeric regions, which is crucial for their compaction"]
- H2Bub is required for FACT activity in genic regions [PMID:31837996]
- Chromatin remodeling demonstrated by IMP [PMID:31837996]

### 5. DNA Replication-coupled Functions
- FACT regulates parental histone transfer to both DNA strands during replication [PMID:38479839 "the FACT histone chaperone regulates parental histone transfer to both strands and collaborates with Mcm2 and Dpb3/4 to maintain parental histone H3-H4 density and faithful heterochromatin inheritance"]
- Collaborates with Mcm2 and Dpb3/4 for epigenetic inheritance [PMID:38479839]

## Localization
- Nuclear: IDA [PMID:17614284 "Pob3-GFP and Spt16-GFP are nuclear factors"], HDA [PMID:16823372]
- FACT complex: IDA [PMID:17614284]
- Euchromatin: EXP [PMID:34731638]
- Chromosome: by similarity

## Protein Interactions
- Pob3 (FACT complex partner) [PMID:17614284]
- Histone H3/H4 [PMID:18579787]
- Abo1 (bromodomain AAA-ATPase) [UniProt, PMID:26582768]
- Fft3 (Fun30 chromatin remodeler) [PMID:28218250]

## Reference Verification
All PMIDs cited in existing GOA annotations verified as real:
- PMID:16823372 - ORFeome localization study (2006, Nat Biotechnol) - REAL
- PMID:17614284 - FACT contributes to centromeric heterochromatin (2007, Curr Biol) - REAL
- PMID:18579787 - Spt16 peptidase domain binds H3-H4 (2008, PNAS) - REAL
- PMID:23028377 - FACT prevents promiscuous CENP-A deposition (2012, PLoS Genet) - REAL
- PMID:31837996 - FACT and H2Bub maintain genome architecture (2020, Mol Cell) - REAL
- PMID:34731638 - FACT facilitates heterochromatin spreading (2021, Cell Rep) - REAL
- PMID:38479839 - Histone chaperone coordination during replication (2024, Genes Dev) - REAL

PMID:28218250 cited in UniProt (not in GOA):
- Lee et al. 2017, Nat Commun - Fun30/Fft3 and FACT cooperation - REAL
