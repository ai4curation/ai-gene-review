# rlmC (RumB/YbjF) - Research Notes

## Gene Identity

- **UniProt (reviewed)**: P75817 (RLMC_ECOLI, E. coli K12/MG1655)
- **UniProt (unreviewed)**: B1X800 (E. coli K12/DH10B) -- same protein, different strain
- **Synonyms**: rumB, ybjF
- **EC**: 2.1.1.189
- **Gene**: b0859 / JW0843
- **Full name**: 23S rRNA (uracil(747)-C(5))-methyltransferase RlmC

## Core Function

RlmC catalyzes the formation of 5-methyluridine at position 747 (m5U747) in 23S rRNA, using S-adenosyl-L-methionine (SAM/AdoMet) as the methyl donor.

## Key Literature

### PMID:12907714 - Madsen et al. 2003, Nucleic Acids Res 31:4738-4746
"Identifying the methyltransferases for m(5)U747 and m(5)U1939 in 23S rRNA using MALDI mass spectrometry."

This is the definitive paper establishing the function of RlmC (then called YbjF). Key findings:
- Three m5U sites in E. coli stable RNAs: U54 in tRNA (TrmA), U747 in 23S rRNA (YbjF/RumB/RlmC), and U1939 in 23S rRNA (YgcA/RumA/RlmD)
- YbjF function was defined in vivo by engineering a ybjF knockout strain [PMID:12907714 "the function of this enzyme was defined in vivo by engineering a ybjF knockout strain"]
- YbjF(-) strains showed ONLY the loss of m5U747 modification [PMID:12907714 "Comparison of the methylation patterns in 23S rRNAs from YbjF(+) and YbjF(-) strains showed that the latter differed only in the lack of the m(5)U747 modification"]
- Could not get recombinant YbjF to retain in vitro activity [PMID:12907714 "We were unable to generate a recombinant version of YbjF that retained in vitro activity"]
- Proposed the name RumB (RNA uridine methyltransferase B)

### PMID:21824914 - Desmolaize et al. 2011, Nucleic Acids Res 39:9368-75
"A single methyltransferase YefA (RlmCD) catalyses both m5U747 and m5U1939 modifications in Bacillus subtilis 23S rRNA."

Key comparative finding:
- In E. coli: three separate COG2265 paralogs (TrmA, RlmC, RlmD) for three m5U sites
- In B. subtilis: a single enzyme YefA/RlmCD handles both m5U747 and m5U1939
- [PMID:21824914 "methylation of U747 and U1939 in B. subtilis rRNA is catalysed by a single enzyme, YefA that is a COG2265 member"]
- [PMID:21824914 "These enzymes belong to the COG2265 cluster, and the Gram-negative bacterium Escherichia coli possesses three paralogues"]
- Suggests evolutionary specialization of COG2265 paralogs

### PMID:21051506 - Auxilien et al. 2011, RNA 17:45-53
"Specificity shifts in the rRNA and tRNA nucleotide targets of archaeal and bacterial m5U methyltransferases."

Key evolutionary findings:
- [PMID:21051506 "The RNA m(5)U methyltransferases appear to have arisen in Bacteria and were then dispersed by horizontal transfer of an rlmD-type gene to the Archaea and Eukaryota"]
- RlmC (formerly RumB) specifically modifies m5U747 in 23S rRNA
- In Pyrococcus abyssi, PAB0760 has RlmC-like activity despite being more closely related to RlmD in sequence

### PMID:30388185 - Jiang et al. 2018, PLoS Pathog 14:e1007379
"Unveiling the structural features that determine the dual methyltransferase activities of Streptococcus pneumoniae RlmCD."

- Structure of S. pneumoniae RlmCD in complex with RNA substrate containing U747 or U1939
- [PMID:30388185 "RlmC is the dedicated enzyme for m5U747 in Escherichia coli"]
- F145 side-chain rearrangement discriminates between U747- and U1939-containing substrates

### PMID:15016356 - Lee et al. 2004, Structure 12:397-407
"Crystal structure of RumA, an iron-sulfur cluster containing E. coli ribosomal RNA 5-methyluridine methyltransferase."

- Structure of the paralog RumA (RlmD) -- relevant by homology to RlmC
- Three domains: N-terminal TRAM domain, central [4Fe-4S] cluster domain, C-terminal SAM-dependent MTase domain
- The [4Fe-4S] cluster is coordinated by four conserved cysteines in a CX5CGGC motif

### PMID:15181002 - Agarwalla et al. 2004, J Biol Chem 279:34123-9
"Redox reactions of the iron-sulfur cluster in a ribosomal RNA methyltransferase, RumA."

- The [4Fe-4S] cluster in RumA/RlmD is redox-active but the methyltransferase reaction does not involve a redox step
- [PMID:15181002 "Sequence data base searches revealed that RumA homologs are widespread in various kingdoms of life and contain a conserved and unique iron-sulfur cluster binding motif, CX(5)CGGC"]
- Oxidation of the cluster leads to decomposition -- potential regulatory mechanism under oxidative stress

### PMID:12003490 - Agarwalla et al. 2002, J Biol Chem 277:8835-8840
Initial characterization of RumA, establishing the presence of a [4Fe-4S] cluster in this family.

### PMID:10369764 - Gregory & Dahlberg 1999, J Mol Biol 289:827-34
"Erythromycin resistance mutations in ribosomal proteins L22 and L4 perturb the higher order structure of 23 S ribosomal RNA."

- L22 mutation influences modification at m5U747 position
- [PMID:10369764 "The L22 mutation influences modification in domain II at positions m5U747, G748, and A1268"]
- This indicates that m5U747 is in domain II of 23S rRNA and its accessibility is influenced by ribosomal protein L22

### PMID:17459887 - Urbonavicius et al. 2007, Nucleic Acids Res 35:3297-305
"Amino acid residues of the E. coli tRNA(m5U54)methyltransferase (TrmA) critical for stability, covalent binding of tRNA and enzymatic activity."

- Establishes conserved residues across COG2265 family (TrmA, RumA/RlmD, RumB/RlmC)
- [PMID:17459887 "the amino acids F188, Q190, G220, D299, R302, C324 and E358, conserved in the C-terminal catalytic domain of several RNA(m5U)methyltransferases of the COG2265 family"]
- Supports modular evolution model: conserved catalytic domain + different RNA-binding domains

## Domain Architecture (from UniProt and InterPro)

- N-terminal region: [4Fe-4S] cluster binding (Cys3, Cys11, Cys14, Cys87) -- HAMAP prediction
- Central/C-terminal: SAM-dependent methyltransferase fold (Rossmann-like)
- Active site: Cys334 (nucleophile for covalent Michael adduct at uracil C6)
- SAM binding: residues 212, 241, 262, 307

## Catalytic Mechanism

The TrmA/RlmC/RlmD family uses a common mechanism:
1. Nucleophilic Cys attacks C6 of the target uracil, forming a covalent Michael adduct
2. This activates C5 for electrophilic methyl transfer from SAM
3. Beta-elimination releases the methylated product (m5U) and regenerates the Cys

## The [4Fe-4S] Cluster Question

UniProt lists RlmC as containing a [4Fe-4S] cluster based on HAMAP rule MF_01012. The binding motif CX5CGGC is present in the N-terminal region (Cys3, Cys11, Cys14, Cys87). This is well-established for the paralog RumA/RlmD (PMID:12003490, PMID:15016356, PMID:15181002) but has not been directly demonstrated experimentally for RlmC. The annotation is based on sequence conservation and is likely correct given the high conservation of the cysteine motif. The role of the [4Fe-4S] cluster is structural rather than catalytic -- the methyltransferase reaction does not involve a redox step (PMID:15181002).

## Biological Significance

- m5U747 is in domain II of 23S rRNA, near the peptidyl transferase center region
- The modification is phylogenetically conserved across bacteria
- In B. subtilis, both m5U747 and m5U1939 are present (catalyzed by a single enzyme RlmCD)
- Loss of m5U747 alone (ybjF/rlmC knockout) was demonstrated without reported growth defects in the original Madsen et al. 2003 study, though detailed phenotypic analysis was not the focus
- The modification likely contributes to local rRNA structural stability and ribosome function
