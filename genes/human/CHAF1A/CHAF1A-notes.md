# CHAF1A (Q13111) review notes

## Identity
- CHAF1A = Chromatin Assembly Factor 1 subunit A, the large p150 subunit of CAF-1 (also CAF-I p150, hp150). HGNC:1910, UniProt Q13111, 956 aa, chromosome 19.
- CAF-1 is a heterotrimeric histone H3-H4 chaperone composed of CHAF1A (p150), CHAF1B (p60), and RBBP4 (p48) [PMID:7600578 "Chromatin assembly factor I (CAF-I) from human cell nuclei is a three-subunit protein complex that assembles histone octamers onto replicating DNA in a cell-free system"; PMID:8858152 "a chromatin assembly complex (CAC), which contains the three subunits of CAF-1 (p150, p60, p48)"].

## Core function: replication-coupled nucleosome/chromatin assembly
- CAF-1 performs the first step of nucleosome assembly, depositing newly synthesized histones H3 and H4 onto replicating DNA; H2A/H2B are added subsequently [UniProt FUNCTION; PMID:7600578 "p150 and p60 form complexes with newly synthesized histones H3 and acetylated H4 in human cell extracts, suggesting that such complexes are intermediates between histone synthesis and assembly onto replicating DNA"].
- CAF-1 mediates DNA-synthesis-coupled nucleosome assembly specifically with the replicative histone variant H3.1 (vs HIRA which uses H3.3 for replication-independent deposition) [PMID:14718166 "The H3.1 and H3.3 complexes contain distinct histone chaperones, CAF-1 and HIRA, that we show are necessary to mediate DNA-synthesis-dependent and -independent nucleosome assembly, respectively"; "these complexes possess one molecule each of H3.1/H3.3 and H4"].
- p150 directly interacts with p60 (CHAF1B) and this is required for assembly; deletion of the p60-binding domain abolishes chromatin assembly [PMID:7600578 "p150 and p60 directly interact and are both required for DNA replication-dependent assembly of nucleosomes. Deletion of the p60-binding domain from the p150 protein prevents chromatin assembly"].
- CAF-1 activity is cell-cycle regulated; in S phase p150 and p60 concentrate at intranuclear DNA replication foci; active CAF-1 isolated as a 6.5S complex in G1/S/G2 [PMID:9614144 "During S phase, p150 and p60 are concentrated at sites of intranuclear DNA replication"; "Active CAF-1 can be isolated as a 6.5 S complex from G1, S, and G2 phase nuclei"].
- p150 directly binds histones H3.1, H3.2 and H3.1t [UniProt SUBUNIT, PMID:33857403] and histones H3 and H4 [PMID:21570500 "p150 binds directly to histones H3 and H4"].

## Coupling to replication fork: PCNA
- CAF-1 is recruited to sites of DNA synthesis through direct interaction of p150 with PCNA, the sliding clamp [UniProt SUBUNIT "Interacts with PCNA; the interaction is direct"; PMID:16826239 "its targeting to sites of DNA synthesis involves a physical interaction between its largest subunit, p150, and the homotrimeric sliding clamp, proliferating cell nuclear antigen (PCNA)"]. PCNA-binding region is residues 1-49 (UniProt FT REGION 1..49 "Binds to PCNA").
- The Cdc7-Dbf4 kinase phosphorylates p150 in S phase, shifting it toward a monomer that binds PCNA, coupling assembly to origin firing [PMID:16826239 "the Cdc7-Dbf4 kinase efficiently phosphorylates p150. This event induces a change in p150 oligomerization state, which promotes binding to proliferating cell nuclear antigen (PCNA)"].
- PMID:15805117 (PCNA double-trimer) shows CAF-1 + Pol delta can be simultaneously accommodated on a PCNA double trimer; this is the IPI annotation source (WITH PCNA P12004) supporting bare protein binding.
- The IPI on PMID:16826239 (identical protein binding, WITH Q13111) supports p150 homodimerization, consistent with UniProt "Homodimer" [PMID:11296234 dimerization, EMBO J].

## Heterochromatin / HP1
- p150 contains a PxVxL motif (residues 233-246) that directly binds the chromo shadow domain (CSD) of HP1 proteins (CBX5/HP1alpha) [PMID:15882967 "KAP-1, CAF-1 p150, and NIPBL carry a canonical amino acid motif, PxVxL, which binds directly to the CSD with high affinity"]. Mutation of V240/L242 abolishes CBX5 binding [UniProt MUTAGEN, PMID:20562864].
- CAF-1 may bring newly synthesized CBX/HP1 proteins to heterochromatic DNA replication foci, contributing to heterochromatin maintenance [UniProt FUNCTION "It may play a role in heterochromatin maintenance in proliferating cells by bringing newly synthesized cbx proteins to heterochromatic DNA replication foci"].
- HP1alpha-CAF1-SetDB1 complex monomethylates non-nucleosomal H3K9, proposed to provide H3K9me1 for Suv39-mediated K9me3 at pericentric heterochromatin during replication [PMID:19498464 "the histone H3K9 methyltransferase SetDB1 associates with the specific heterochromatin protein 1alpha (HP1alpha)-chromatin assembly factor 1 (CAF1) chaperone complex"]. (Note: the related MBD1-SetDB1 paper PMID:15327775 was RETRACTED, PMID:30849389; UniProt CAUTION.)

## Repair-coupled assembly
- CAF-1 is the only characterized histone chaperone promoting nucleosome assembly coupled both to DNA replication and to nucleotide excision repair (DNA synthesis at repair sites) [PMID:16826239 "the only characterized histone chaperone that promotes nucleosome assembly coupled to DNA synthesis in the context of DNA replication ... and nucleotide excision repair"]. Supports DNA repair (GO:0006281) keyword/IEA.

## Other interactions (context, not core MF)
- Transcriptional repressor Gfi1: p150 is part of the Gfi1/LSD1/HDAC1 repression complex, may link DNA-bound repressor to histones [PMID:21570500].
- MBD1 [UniProt SUBUNIT, PMID:12697822].

## Bare protein-binding (GO:0005515) IPI annotations
Many GOA `protein binding` IPI annotations derive from high-throughput interactome screens and large-scale studies, which do not convey a specific molecular function:
- PMID:17474147 (SH3 domain peptide array; WITH NCK1 P16333, PIK3R1 P27986)
- PMID:20936779 (MAP kinase interactome; WITH YWHAE P62258)
- PMID:23075851 (DAXX/H3.3 structure; WITH H3-3B P84243, H3C15 Q71DI3) — histone partners but from a DAXX-focused study
- PMID:24981860 (chromatin protein interactions; WITH CBX5 P45973)
- PMID:25416956, PMID:26496610, PMID:32296183, PMID:33961781 (proteome-scale interactome maps)
- PMID:27705803 (Polycomb complexome)
- PMID:31980649 (EGFR/KRAS network)
- PMID:35271311 (OpenCell endogenous tagging)
These are best treated as MARK_AS_OVER_ANNOTATED for the bare `protein binding` term. The specific, biologically meaningful binding activities (histone H3-H4 binding, HP1 chromo shadow domain binding, PCNA binding) are captured by dedicated annotations or should be added as more informative MF terms.

## Specific MF/CC/BP terms supported
- Histone binding (GO:0042393): directly binds H3.1/H3.2/H3.1t and H3/H4 [PMID:33857403; PMID:21570500].
- H3-H4 histone complex chaperone activity (GO:0000510) / histone chaperone activity (GO:0140713): CAF-1 is the H3-H4 chaperone [PMID:7600578; PMID:14718166].
- chromo shadow domain binding (GO:0070087): PxVxL-CSD binding to HP1 [PMID:15882967].
- chromatin binding (GO:0003682): TAS [PMID:7600578].
- CAF-1 complex (GO:0033186): part_of [PMID:9614144, PMID:8858152].
- DNA replication-dependent chromatin assembly (GO:0006335): IDA [PMID:14718166, PMID:9614144, PMID:8858152].
- nucleosome assembly (GO:0006334): supported, present in UniProt GO refs (IDA GO_Central).
- nucleus (GO:0005634) / nucleoplasm (GO:0005654) / chromatin (GO:0000785): subcellular localization, DNA replication foci [PMID:9614144; UniProt SUBCELLULAR LOCATION].

## Conclusion
Core function = histone H3-H4 chaperone (large p150 subunit of CAF-1) mediating replication-coupled (and repair-coupled) nucleosome/chromatin assembly, coupled to the replication fork via direct PCNA binding, and contributing to heterochromatin maintenance via HP1 (chromo shadow domain) binding.
