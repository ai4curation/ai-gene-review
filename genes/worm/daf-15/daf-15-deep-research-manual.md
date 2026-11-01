# daf-15 (C. elegans Raptor) - manual literature research

No deep-research API was available in this session; this file was compiled by hand from
cached publications (publications/PMID_*.md) and PubMed searches ("daf-15 raptor elegans").

## Identity

- UniProt G5EEV7 (unreviewed TrEMBL), WormBase WBGene00000911, ORF C10C5.6, GeneID 177770, 1782 aa.
- Domain content: Raptor N-terminal CASPase-like (RNC) domain (SMART SM01302, residues 67-223),
  ARM/HEAT-like repeat region and C-terminal WD40 repeat superfamily; InterPro IPR004083 (Raptor),
  PANTHER PTHR12848 "REGULATORY-ASSOCIATED PROTEIN OF MTOR" [file:worm/daf-15/daf-15-uniprot.txt].
- Ortholog of human RPTOR (Q8N122), Drosophila raptor, yeast KOG1.

## Literature

1. Albert & Riddle 1988 (PMID:3350212, abstract only). Isolation of daf-15(m81): mutants form
   dauer-like larvae, cannot exit, and daf-15 is epistatic to dauer-defective mutations,
   "indicating that these two genes act late in the pathway leading to" dauer formation.
2. Jia, Chen & Riddle 2004 (PMID:15253933, abstract only cached). Molecular identification of
   daf-15 as raptor: "mutations in the genes encoding CeTOR and raptor result in dauer-like larval
   arrest"; "raptor mutations extend adult life span"; "daf-15 transcription is regulated by
   DAF-16, a FOXO transcription factor".
3. Sheaffer, Updike & Mango 2008 (PMID:18804378, full text). "C. elegans possesses homologues of
   TOR complex 1 (TORC1) components, including TOR kinase (let-363 [21]), Raptor (daf-15; [15])
   and LST8". Combined let-363 + daf-15 RNAi from L4 extends lifespan and this requires pha-4/FoxA
   ("pha-4(ts); let-363(RNAi); daf-15(RNAi) animals had shorter life spans than pha-4(ts) alone").
   daf-15 mutants have small nucleoli and increased intestinal lipid, like let-363.
4. Zhu et al. 2013 (PMID:23705068, full text). Sphingolipid (d17iso-GlcCer)-TORC1 pathway for
   postembryonic growth. A DAF-15::RAP-1(22) fusion (Raptor tethered via the Rap1 C-terminal
   lysosome-targeting signal, after Sancak et al. 2010) acts as a constitutively active TORC1
   transgene that bypasses elo-5 L1 arrest: "This indicates that hyperactivation of TORC1 was
   sufficient to support L1 growth in mmBCFA-depleted animals." This is the best functional
   evidence in the worm that DAF-15 acts as the TOR-recruiting subunit of TORC1, mirroring the
   mammalian mechanism.
5. Korta et al. 2012 (PMID:22278922, S6K germline paper):
   reducing let-363 or daf-15 reduces the germline progenitor pool similarly to rsks-1; ife-1
   double mutants. Context for TORC1 output in germline.
6. Other hits (PMID:25789174 royal jelly 10-HDA lifespan; PMID:28239780 sesamin lifespan) use
   daf-15 only as a TOR-pathway genetic tool; low relevance.

## Synthesis

DAF-15 is the C. elegans Raptor, the defining non-catalytic scaffold subunit of TORC1. By orthology
it binds LET-363/TOR and presents substrates (RSKS-1/S6K, IFE/4E-BP pathway) and tethers TORC1 to
the lysosomal Rag GTPase platform. Genetically it is required for larval growth past the L2/L3
(dauer-like arrest), lipid homeostasis, nucleolar size/ribosome biogenesis and germline
proliferation; reduced function extends adult lifespan (pha-4 dependent). Its transcription is
repressed by DAF-16/FOXO, linking insulin/IGF signaling to TORC1.
