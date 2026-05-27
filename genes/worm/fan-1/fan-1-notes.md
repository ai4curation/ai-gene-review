# fan-1 (C. elegans) - Research Notes

## Gene Identity

- Gene: fan-1 (C01G5.8)
- UniProt: P90740 (FAN1_CAEEL)
- WormBase: WBGene00015310
- 865 amino acids, single-pass nuclear protein
- Human ortholog: FAN1/KIAA1018 (Q9Y2M0)

## Discovery

FAN1 was identified simultaneously in 2010 by three independent groups:
- MacKay et al. (Cell, 2010) [PMID:20603015 "FAN1 exhibits endonuclease activity toward 5' flaps and has 5' exonuclease activity, and these activities are mediated by an ancient VRR_nuc domain"]
- Kratz et al. (Cell, 2010) [PMID:20603016 "KIAA1018 is a 5'-->3' exonuclease and a structure-specific endonuclease that preferentially incises 5' flaps"]
- Smogorzewska et al. (Mol Cell, 2010) [PMID:20603073 "FAN1 possesses intrinsic 5'-3' exonuclease activity and endonuclease activity that cleaves nicked and branched structures"]

All three papers used C. elegans fan-1 mutants to demonstrate the conserved role in ICL repair.

## Domain Architecture

- N-terminal UBZ4-type zinc finger (residues 35-62): binds ubiquitin, specifically monoubiquitinated FANCD2
- Winged-helix domain (approx 245-305): DNA binding module
- TPR domain (approx 457-609): protein-protein interactions
- C-terminal VRR-NUC domain (742-858): catalytic nuclease core, metal-dependent (Mn2+/Mg2+)

## Key Molecular Functions

1. **5'-3' exonuclease activity**: FAN1 cleaves DNA successively at every third nucleotide from a nick or 5' flap [PMID:25430771 "human FAN1 cleaves DNA successively at every third nucleotide"]
2. **5'-flap endonuclease activity**: Cleaves branched DNA structures, particularly 5' flap substrates [PMID:20603015 "FAN1 exhibits endonuclease activity toward 5' flaps"]
3. **DNA binding**: Binds flap-structured DNA and duplex DNA via winged-helix domain
4. **Ubiquitin binding**: UBZ4 domain binds monoubiquitinated FANCD2 [PMID:20603016 "recruitment to DNA damage through interaction of its UBZ domain with monoubiquitylated FANCD2"]

## Biological Process

- **Interstrand cross-link repair**: Primary function. fan-1 mutant worms show hypersensitivity to cisplatin, nitrogen mustard, and mitomycin C [PMID:20603015, PMID:20603016, PMID:20603073]
- **DNA repair**: General role in genome maintenance

## C. elegans-specific Findings

### Disruption phenotype
- No visible phenotype under normal conditions
- Strong increase in embryonic lethality following cisplatin, nitrogen mustard, or MMC treatment [PMID:20603015, PMID:20603016, PMID:20603073]

### Systematic ICL repair analysis (Wilson et al. 2017)
[PMID:28934497 "The analysis also revealed contributions of homologous recombination (BRC-1/BRCA1), the MUS-81, EXO-1, SLX-1 and FAN-1 nucleases, and the DOG-1 (FANCJ) helicase in ICL resolution, influenced by the replicative-status of the cell/tissue"]
- FAN-1 contributes to ICL resolution in a replication-dependent manner
- No critical role seen for FCD-2 (FANCD2) in this study, suggesting FAN-1 can act partially independently of the canonical FA pathway

### Mutagenic consequences of ICL repair (Verschuren et al. 2025)
[PMID:40082407 "we found these SNVs to depend on the functionality of the Fanconi anemia-associated nuclease FAN1"]
- FAN1 mediates translesion synthesis leading to single nucleotide polymorphisms during psoralen ICL repair
- Disruption of FAN1 eliminates SNV formation from ICL repair
- Suggests FAN-1 is required for error-prone TLS-mediated bypass of ICLs

### Protein interactions
- Interacts with SMO-1 (SUMO) by IntAct data (3 experiments) [UniProt entry]
- High-throughput Y2H interactions from interactome mapping [PMID:14704431, PMID:19123269] - these are generic interactome screens, not FAN-1-specific studies

## Structural Biology (human FAN1)

- Crystal structure solved: Wang et al. 2014 [PMID:25430771] - mechanism of ICL unhooking by 3-nt interval cleavage
- Zhao et al. 2014 [PMID:25500724] - dimeric FAN1 unwinds 5' flap DNA before incision
- Rao et al. 2018 [PMID:29518739] - homodimerization important for long 5' flap cleavage
- Jin et al. 2018 [PMID:29514982] - bacterial FAN1 structure reveals conserved ICL unhooking mechanism

## Subcellular Localization

- Nucleus: IDA evidence from Kratz et al. 2010 [PMID:20603016] - GFP-tagged C. elegans FAN-1 localizes to the nucleus

## Verification of BioReason References

The BioReason deep research file does not cite specific PMIDs. It references domain architecture from InterPro, which is accurate. The reasoning trace is largely sound for this well-characterized protein, though some partner predictions (ERCC4/XPF homologs, PMS family, WRN helicase, DNA polymerase kappa) are speculative extrapolations from human pathway knowledge and are not demonstrated in C. elegans.

## GO Annotation Notes

- GO:0008270 (zinc ion binding) appears in UniProt DR lines but NOT in the GOA TSV. It is a reasonable IEA annotation based on the UBZ4 zinc finger.
- The protein binding (GO:0005515) annotations from PMID:14704431 and PMID:19123269 are from high-throughput interactome screens detecting interaction with SMO-1/SUMO. Per curation guidelines, "protein binding" is uninformative - the interaction with SUMO is more relevant as it may indicate SUMOylation plays a role in FAN-1 regulation.
- Several annotations are duplicated across evidence types (e.g., nucleus from IBA, IEA, and IDA; DNA repair from IEA and IMP; ICL repair from IBA and IEA).
