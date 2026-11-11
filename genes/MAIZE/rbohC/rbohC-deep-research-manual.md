# rbohC (Zea mays) - manual literature research

No deep-research API was available; this file records a manual literature search
(PubMed via MCP, cached publications, NCBI Gene, web search) done during the review.

## Identity

- UniProtKB A5H238 (TrEMBL, unreviewed, PE 2 transcript level), 948 aa, from GenBank
  DQ897930 / ABK27631.1 (Lin, Zhao, Jiang, 2006 submission).
- NCBI Gene 100101532 (LOC100101532), "respiratory burst oxidase-like protein C",
  other designation "respiratory burst oxidase3"; aliases Zm00001d038762,
  GRMZM2G043435, rbohC; chromosome 6 (NCBI Gene esummary, retrieved 2026-10-28).
- PeroxiBase/RedoxiBase 5489 = ZmRboh07 (Zm00001d038762 / GRMZM2G043435 / ZmRbohC),
  the same PeroxiBase id that the UniProt record cross-references.
- Cloning paper: Lin et al. 2009 [PMID:19592501 "The ZmrbohC cDNA sequence (3317 bp) had
  an ORF of 2847 nucleotides, encoding a protein of 948 amino acids."] This matches the
  948-aa A5H238 sequence. ZmrbohC is closest to rice OsrbohC [PMID:19592501 "ZmrbohC and
  ZmrbohD had maximal sequence identity to OsrbohC (89.6% identity)"].

## Domain architecture (UniProt A5H238)

- EF-hand (PROSITE PS50222, 263-298) and EF_HAND_1 Ca2+-binding site signature (PS00018).
- NADPH_Ox (PF08414), Ferric_reduct (PF01794), FAD_binding_8 (PF08022), NAD_binding_6
  (PF08030); PRINTS GP91PHOX; InterPro Cyt_b245_heavy_chain (IPR000778).
- Phobius transmembrane helices; PIRSR heme-iron axial ligand histidines at 468, 482, 570, 583.
- PANTHER PTHR11972 (NADPH oxidase), subfamily SF202.
- Lin et al. describe the Zmrboh family as having the six gp91phox transmembrane helices,
  heme-binding histidine pairs and an N-terminal regulatory extension [PMID:19592501 "Moreover,
  the N-terminal regions of these proteins were hydrophilic and contained two Ca2+-binding
  EF-hand motifs"].

## Expression and signalling studies naming ZmrbohC (DQ897930)

- ABA and H2O2 induce ZmrbohA-D transcripts in maize leaves in two phases, the later phase
  depending on a MAPK (ZmMPK5) cascade; plasma membrane NADPH oxidase activity rises in
  parallel [PMID:19592501]. ZmrbohC induction by ABA was weak in phase II [PMID:19592501
  "The expression of ZmrbohA in phase I and ZmrbohC in phase II induced by ABA was slight"].
- Brassinosteroid induces ZmrbohA-D transcripts; late induction requires apoplastic H2O2
  and ZmMPK5 [PMID:20693409 "BR treatment significantly elevated the expression of
  ZmrbohA–ZmrbohD in leaves of maize plants."]. The ZmrbohC primers in this paper cite
  GenBank DQ897930, the A5H238 source. Expression only; no protein assay.

## Genetic studies of ZmRBOHC

- Gao et al. 2022 (Mol Plant) [PMID:36045577, abstract only]: ZmSRO1d mono-ADP-ribosylates
  ZmRBOHC, raising guard-cell ROS and promoting stomatal closure; ZmRBOHC loss-of-function
  mutants have higher yield when well watered and reduced drought resistance. Gene identifier
  not stated in the abstract; web sources (funplantgenes, plantae) associate the Gao ZmRBOHC
  with this locus (ZmRBOHC/ZmRBOH9/rboh3), consistent with NCBI's "respiratory burst oxidase3".
- Fu et al. 2026 (Plant Biotechnol J) [PMID:41792868, full text]: ZmWRKY29 represses
  ZmRBOHC transcription via a W-box; an EMS stop-gained Zmrbohc mutant (stop at aa 384) is
  more susceptible to Gibberella stalk rot and has an attenuated chitin-elicited ROS burst.
  ZmRBOHC is described as the ortholog of OsRBOHC, matching Lin et al.'s ZmrbohC. Gene
  identifier not stated in the text; identity with A5H238 is probable but not verified.

## Orthology-based function (Arabidopsis)

- Plant RBOHs are plasma membrane gp91phox homologues that produce superoxide
  [PMID:11756663 "putative plant plasma membrane NADPH oxidase can produce superoxide"].
- EF-hand Ca2+ binding and phosphorylation activate AtrbohD [PMID:18218618].

## Annotation-relevant conclusions

- Core MF: superoxide-generating NADPH oxidase activity (GO:0106292), plasma membrane.
- Peroxidase activity (InterPro2GO from IPR013623) is a wrong mapping; the derived cellular
  oxidant detoxification row falls with it.
- No direct biochemical assay of ZmrbohC protein has been reported.
