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

## ProtNLM pre-release paragraph assessment

The exact source paragraph and eleven atomic claims are recorded in spt16-protnlm-function-review.md. Established complex membership, transcription/replication roles and chromatin reassembly are supported. The asserted dissociation of exactly one H2A-H2B dimer is not required by the mechanistic literature: [PMID:19683499 "Second, increased nuclease sensitivity can occur without displacement of dimers from the nucleosome."]. The main biological description therefore describes nucleosome reorganization without making dimer eviction obligatory.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Scope: re-examined all 34 GOA rows, the description and core functions without consulting any ProtNLM2 output.

### Identity
- Benchmark accession O94267 is the canonical, reviewed (Swiss-Prot) UniProt entry for spt16 (SPBP8B7.19), 1019 aa, full length. It is not an isoform, fragment or alternative gene model. All domains are present (N-terminal aminopeptidase P-like domain with structure 3CB5/3CB6, dimerization and middle domains, acidic C-terminus).

### Evolutionary grounding
- PANTHER PTHR13980 (CDC68 RELATED), subfamily PTHR13980:SF15 (FACT COMPLEX SUBUNIT SPT16). The subfamily holds the Spt16 orthologs from fungi, plants, animals and Dictyostelium, including S. cerevisiae SPT16 (P32558), human SUPT16H (Q9Y5B9), Drosophila dre4 (Q8IRG6) (interpro/panther/PTHR13980/PTHR13980-entries.csv).
- PAINT node PTN000360139 (taxon Eukaryota) carries IBD for GO:0035101 FACT complex, GO:0000511 H2A-H2B chaperone (seeded by pombe spt16 itself), GO:0031491 nucleosome binding (seed dre4) and GO:0140673 (seed SUPT16H) (interpro/panther/PTHR13980/PTHR13980-paint.tsv). The IBA rows in GOA descend from this node, and O94267 sits inside it, so they transfer correctly.
- The family review interpro/panther/PTHR13980/PTHR13980-review.yaml uses O94267 as reference protein in SF15. It agrees with this placement.

### Changes relative to the previous review
- GO:0005515 rows: 8 IPI rows with histone partners from PMID:18579787 (pombe H4 P09322, H3 P09988, H3.3 P10651, Drosophila H3 P02299 and H4 P84040; partner identities checked against UniProt) changed from KEEP_AS_NON_CORE to MODIFY -> GO:0042393 histone binding. Spt16-N is a dedicated H3-H4 binding module [PMID:18579787 "the highly conserved fold directly binds histones H3-H4 through a tight interaction with their globular core domains, as well as with their N-terminal tails"]. The Pob3 IPI row (PMID:17614284) is now REMOVE: it is an intra-complex contact already covered by the FACT complex IDA.
- GO:0010468 regulation of gene expression (ARBA): KEEP_AS_NON_CORE -> MODIFY to GO:0032784 (an is_a descendant, checked with runoak ancestors).
- GO:0006325 chromatin organization (EXP, PMID:23028377): KEEP_AS_NON_CORE -> MODIFY to GO:0140673 and GO:0034728.
- GO:0006261 DNA-templated DNA replication (NAS): still KEEP_AS_NON_CORE, but the reason has been rewritten. GO:0006335 is NOT a descendant of GO:0006261 (its ancestors are chromatin organization only), so "less specific" was the wrong justification.
- GO:0000791 euchromatin: the old quote did not support the location. It now cites the Spt16/Pob3 ChIP-seq distribution [PMID:34731638 "showed the highest levels of FACT at euchromatin, lower levels at subtelomeres, and the lowest levels at pericentromeres"].
- GO:0000511 EXP PMID:31837996 (contributes_to): kept as ACCEPT, but a SUSPECTED WRONG_EVIDENCE_CODE source defect (CHECK) has been added for PomBase. The in vitro EMSA and chaperoning assays used recombinant human FACT [PMID:31837996 "Recombinant human FACT was purified similarly as published before"].
- GO:0000511 EXP PMID:34731638: kept as ACCEPT, deferring to the curator. Note that the paper measures H3 turnover in vivo and has no H2A-H2B-specific assay.
- GO:0006337 IBA: added pombe support (PMID:28218250) and the phylogenetic rationale.
- New core function: histone binding (GO:0042393) by the N-terminal domain.
- The description has been rewritten as a standalone biological summary.

### Not added (deliberately)
- The Spt16 peptidase-like domain binds the Swi6 chromo-shadow domain (cited in the falcon deep research to Takahata et al. 2023, a review). The primary paper is not cached, so no annotation is proposed. That binding would be a protein-binding MF anyway.
- FACT preventing ectopic CENP-A deposition (PMID:23028377) follows from its role in H3 chromatin maintenance. It is not a separate process that Spt16 performs, so no NEW term is proposed.

### Relative
- Closest characterised relative in the same subfamily (SF15) and PAINT node: S. cerevisiae SPT16 (P32558), reviewed at genes/yeast/SPT16/SPT16-ai-review.yaml (all 65 annotations actioned, core_functions present, status DRAFT). Human SUPT16H (Q9Y5B9) has no review in the repo.
- GO-CAM gomodel:6796b94c00000168 (pombe transcription elongation by RNAPII) has spt16 enabling GO:0000511, part of GO:0140673, in the FACT complex. This is consistent with the core function here.
