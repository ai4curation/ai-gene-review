# Mesau_02205 (UniProtKB:L0KKS2) — Mesorhizobium australicum WSM2073 PgeF — review notes

Reviewed 2026-10-28. No provider deep-research file exists for this gene; these notes are the
manual literature research (PubMed searches for "PgeF peptidoglycan", "YfiH Escherichia coli",
"FAMIN purine nucleoside phosphorylase", "Mesorhizobium australicum T-G1").

## Identity

- L0KKS2_MESAW, 264 aa, TrEMBL, PE 3, reference proteome UP000010998, ordered locus Mesau_02205
  (EMBL AGB44643.1, RefSeq WP_015316093.1). No gene symbol in UniProt; the folder is named for the
  locus tag.
- Family: PgeF/LACC1 family (YfiH, DUF152; Pfam PF02578 "Cu-oxidase_4"; InterPro IPR003730
  "Cu_polyphenol_OxRdtase"; NCBIfam TIGR00726 "peptidoglycan editing factor PgeF"; PANTHER
  PTHR30616:SF2; CDD cd16833 YfiH).
- The species-level fragment A0A0K2YWP2 (strain T-G1, 54 aa) is a different sequence (different
  UniParc id, 88.9% identity over L0KKS2 207-260); it has its own review in
  `genes/9HYPH/A0A0K2YWP2/` and its bioinformatics folder holds the comparison
  (`file:9HYPH/A0A0K2YWP2/A0A0K2YWP2-bioinformatics/RESULTS.md`).
- L0KKS2 aligns with E. coli PgeF (P33644) at 42.8% identity, and the catalytic Cys107 of E. coli PgeF
  aligns with L0KKS2 Cys117 (same script).

## What the family does

- E. coli YfiH was renamed PgeF after loss of yfiH caused L-Ser/Gly to replace L-Ala in PG
  [PMID:28612943 "absence of yfiH results in incorporation of non-canonical amino acids, L-serine or glycine in place of L-alanine in PG sacculi leading to β-lactam - sensitivity"].
- Biochemistry (2025): PgeF is a proofreading hydrolase acting on cytoplasmic UDP-MurNAc-peptide
  precursors
  [PMID:40632566 "Detailed biochemical analysis of several bacterial PgeF homologs reveals that PgeF specifically cleaves serine or glycine but not alanine from the PG precursors."]
  and the bond cleaved is the MurNAc–peptide amide
  [PMID:40632566 "confirming that PgeF cleaves the amide bond between UDP-MurNAc and the peptide"].
  The catalytic cysteine is required
  [PMID:40632566 "the precursor levels remained unchanged upon treatment with PgeFEc C107A, confirming that C107 is crucial for the catalytic activity"].
  The homologs tested were from E. coli, Salmonella, B. subtilis and G. stearothermophilus — no
  alphaproteobacterial (rhizobial) PgeF has been tested. The Mesorhizobium assignment therefore rests on
  family membership (TIGR00726) and the conserved catalytic cysteine.
- Purine metabolism: FAMIN/LACC1 and bacterial YfiH/YlmD have adenosine deaminase, PNP and MTA
  phosphorylase activities in vitro
  [PMID:31978345 "FAMIN and its prokaryotic orthologs additionally have adenosine deaminase, purine nucleoside phosphorylase, and S-methyl-5'-thioadenosine phosphorylase activity"],
  but in bacteria these are weak and physiologically unimportant
  [PMID:40632566 "Here, we find that they indeed have a weak PNP activity, but with no physiological relevance in bacterial systems."].
  The UniProt record carries an EC-mapped S-methyl-5-thioadenosine phosphorylase GO line (not in the
  GOA file used here). I did not propose any purine-enzyme term for L0KKS2.
- Laccase / multicopper oxidase: Beloqui et al. 2006 reported laccase activity and copper for
  metagenomic RL5 and for E. coli YfiH
  [PMID:16740638 "the hypothetical proteins from Bacteroides thetaiotaomicron and from E. coli, which are closely related to the deduced protein encoded by the RL5 gene, are also multicopper proteins with polyphenol oxidase activity"].
  This is the origin of the "Cu-oxidase_4"/"Cu_polyphenol_OxRdtase" family names. Cader et al. 2020
  could not reproduce it
  [PMID:31978345 "In a sensitive LC-MS method (Perna et al., 2018), laccase end-products were only detected with a conventional laccase but not with YlmD, YfiH, or FAMIN254I"].
  PgeF/YfiH has no cupredoxin domains; it is not a multicopper oxidase of the laccase/CueO/MnxG/McoA
  type. The copper ion binding IEA (TreeGrafter, PTN000770205) goes back to that disputed copper claim.

## CMMMech context (bixbyite-mn.yaml): claims stronger than the evidence

CMMMech `data/records/bixbyite-mn.yaml` grounds the causal-graph node
`tg1_acidic_mn_oxidase_factor` ("proteinase-K-sensitive laccase-like factor (Mesau_02205)") to
L0KKS2 and A0A0K2YWP2, and the graph description refers to "laccase-like / multicopper oxidase activity
and the Mesau_02205-targeted locus". Bohu et al. 2015 is the only source:

- Bohu et al. chose mesau_02205 through an annotation keyword search
  [PMID:26236307 "MCO genes were identified by key word searches against the annotated genome in the GenBank and Kyoto Encyclopedia of Genes and Genomes (KEGG) databases"]
  [PMID:26236307 "Only one laccase-like MCO gene, mesau_02205, was detected."].
  The "MCO" label comes from the misleading DUF152 name ("multicopper polyphenol oxidase"). By current
  family assignment (TIGR00726, PgeF/LACC1) the gene encodes a peptidoglycan-editing hydrolase, not a
  multicopper oxidase. A genuine MCO search of WSM2073 (cupredoxin domains PF00394/PF07731/PF07732) was
  not done in that paper, so "only one MCO" is unsupported.
- The ABTS "MCO activity" was measured on whole-cell protein extracts
  [PMID:26236307 "Whole cell protein of T-G1 extracted from different growth phase and pH was subjected to the MCO activity assay."].
  It cannot be attributed to Mesau_02205. The Proteinase-K sensitivity shows only that some protein is
  involved.
- The only gene-specific data are transcript abundance (qRT-PCR with primers designed on WSM2073 and
  applied to T-G1). This is correlation, without knockout, purified protein or Mn(II)-oxidation assay
  of the gene product.
- CMMMech already marks its evidence `supports: partial` and states there is no knockout or purified
  enzyme, which is correct. But naming the node a "laccase-like factor (Mesau_02205)" with
  `protein_grounding_status: GROUNDED`, and calling the domain "Cu-oxidase_4 ... putative multicopper
  polyphenol oxidase", repeats the misnaming. Family knowledge argues against a direct Mn(II)-oxidase
  role: PgeF homologs have no laccase activity in sensitive LC-MS assays (PMID:31978345) and their
  established function is cytoplasmic PG precursor editing (PMID:40632566). A cytoplasmic PG-editing
  enzyme could not plausibly oxidize extracellular Mn(II) directly.
- CMMMech's `annotation_note` for A0A0K2YWP2 attributes the PgeF name to "ARBA/RuleBase". For
  A0A0K2YWP2 it is ARBA only (ARBA00096633). For L0KKS2 it is ARBA plus RuleBase RU361274, which is correct.
- CMMMech's `gene_symbol: Mesau_02205` on A0A0K2YWP2 is a WSM2073 locus tag applied to a T-G1 fragment.
  The fragment record has no gene name, and Bohu et al. themselves call the T-G1 sequence "the
  orthologs of mesau_02205".
- Recommendation for CMMMech curators (not edited here): the node should be "unidentified
  proteinase-K-sensitive Mn(II)-oxidizing factor" with grounding status at most CANDIDATE/UNRESOLVED.
  Mesau_02205 should be reframed as a pH-responsive transcript that was misannotated as an MCO.

## Decisions

- copper ion binding (IEA TreeGrafter) -> MARK_AS_OVER_ANNOTATED (the only basis is the disputed
  Beloqui EPR/laccase result; no copper is needed for the established Cys-dependent editing chemistry).
- cytoplasm (IEA SubCell) -> ACCEPT (PgeF acts on cytoplasmic UDP-MurNAc-peptide precursors).
- NEW peptidoglycan biosynthetic process (ISS from E. coli PgeF, PMID:40632566). PgeF does work in the
  pathway: it hydrolyses misligated intermediates of the cytoplasmic stage. E. coli P33644 carries
  peptidoglycan metabolic process (IMP, PMID:28612943), so the process area is already used for the
  family.
- Core MF: no GO term exists for this hydrolysis of UDP-MurNAc-peptide precursors. GO:0008745
  N-acetylmuramoyl-L-alanine amidase is defined on cell-wall glycopeptides and sits under peptidoglycan
  muralytic activity, so it does not fit. A new term is proposed under GO:0016811.
