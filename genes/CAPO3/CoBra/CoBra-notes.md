# CoBra (Capsaspora owczarzaki Brachyury) - curation notes

Automated deep research was unavailable for this gene (no provider keys), so no
`-deep-research-*.md` file exists. These notes are compiled from the cached full
texts of PMID:24043797 and PMID:27114036, the UniProt record and our own locus
assignment analysis.

## Identity and the locus assignment caveat

- UniProt A0A0D2VUC6, ORF CAOG_005512, automatic name "TBX19 protein", 1130 aa,
  one T-box domain at 447-625 (PROSITE PS50252), InterPro IPR002070 (TF_Brachyury)
  [file:CAPO3/CoBra/CoBra-uniprot.txt].
- PMID:24043797 names CoBra but gives no locus ID. The assignment of CoBra to
  A0A0D2VUC6 is our own inference
  [file:projects/ORIGINS_OF_MULTICELLULARITY/capsaspora-tbox/RESULTS.md "A0A0D2VUC6 (CAOG_005512) is CoBra."]:
  - best T-subfamily match (T-box domain scores TBX19 534.5, TBXT 504.5, well above
    the other two Capsaspora T-box proteins);
  - an Arg at the position aligned to Xenopus Bra K149 (context LKLTNRPNTKG), which
    is the residue the paper reports for CoBra
    [PMID:24043797 "despite the presence of an Arginine (R) instead of a Lysine (K) in the CoBra protein"].
  - Caveat: similarity plus one marker residue, not a phylogeny. The gene models in
    UniProt may differ from those used in the paper.
- PANTHER places the protein in PTHR11267:SF181 "OPTOMOTOR-BLIND PROTEIN" (a
  Tbx2-class subfamily name). This disagrees with the Brachyury identity from the
  paper's phylogeny and our domain scoring. None of the GOA rows come from the
  subfamily; the TreeGrafter rows come from PTN000137774, the deep T-box family node
  (the same node that gives human TBXT its IBA cell fate specification row, with
  fly, mouse, worm and zebrafish donors).
- Side note: the paper calls its second tested gene "CoTbx3" but places it in a
  new Tbx7 class [PMID:24043797 "Tbx7 ( CoTbx3 )"]; RESULTS.md matches A0A0D2WSA5 to
  the Tbx2/3 class. Not relevant to CoBra's rows.

## Evidence on the protein

### Phylogeny (PMID:24043797)
- Brachyury is the oldest T-box class; filasterean Bra genes cluster at the base of
  the class and keep most DNA-binding and dimerization residues
  [PMID:24043797 "fungal, and especially filasterean, Brachyury genes have most of the T-box key DNA-binding and dimerization amino acids"].
- T-box genes are absent in choanoflagellates
  [PMID:24043797 "We did not identify T-box genes in either of the two sequenced choanoflagellates"].

### DNA binding in vitro (PMID:24043797, universal PBM)
- [PMID:24043797 "Our results indicate that CoBra has a highly similar motif to that determined in the mouse Bra-homolog, called T"]
- Motif conserved across T-box classes; specificity between classes attributed to
  cofactors [PMID:24043797 "cooperative interactions of T-box genes with different cofactors, as opposed to differences in DNA-binding sequence recognition, are the key means through which members of this family have diverged in function"].

### Heterologous activity in Xenopus (PMID:24043797) - NOT Capsaspora evidence
- Partial rescue of XBra_En dominant-negative embryos (MyoD in situ, qRT-PCR), with
  the authors' own caveat [PMID:24043797 "we can only conclude that both CoBra and CoTbx3 can roughly mimic endogenous XBra function"].
- Overexpression activates all mesendodermal genes tested, unlike metazoan Bra
  [PMID:24043797 "which strongly activated all mesendodermal genes"].
- XBra/CoBra chimeras map the difference to the N- and C-terminal regions
  [PMID:24043797 "N-terminal and C-terminal domains, even though they do not contain any recognizable conserved amino acidic motifs, could largely account for the metazoan Brachyury homologs specificity"].
- "pan-Tbox" behaviour [PMID:24043797 "both CoBra and CoTbx3 (a member of the Tbx7 class) behave as what we call “pan-Tbox” genes"].
- Capsaspora lacks Smad1, the cofactor implicated in restricting metazoan Bra.

### In vivo chromatin occupancy in Capsaspora (PMID:27114036)
- ~900 Bra motif instances in ATAC-defined regulatory sites, mostly first intron and
  5' UTR, associated with filopodial amoeba and aggregative stages and with H3K4me3
  and H3K27ac [PMID:27114036 "these inferred Bra sites are preferentially located at the first intron and 5′ UTR and are predominantly associated with the filopodial amoeba and aggregative stages"].
- Anti-CoBra antibody ChIP-qPCR at 20 sites vs 10 random motif sites
  [PMID:27114036 "The ATAC-defined Bra regulatory sites were strongly enriched in CoBra compared with random motifs (Figure 6G), validating our Bra target prediction approach."].
- Inferred target network: cell polarity, phagocytosis, metabolism, TFs, GPCR
  signalling; 63 orthologs shared with mouse Bra targets, enriched in actin
  cytoskeleton and amoeboid motility [PMID:27114036 "those shared orthologs are enriched in actin cytoskeleton and amoeboidal cell-motility functions"].
- Caveat: the antibody was raised against "CoBra" as defined by that group; which
  UniProt entry it corresponds to is again our inference. Target genes are inferred
  (motif + ATAC), only 20 sites validated by ChIP-qPCR; no knockout of CoBra exists.

## Decisions summary

- MF rows (DNA-binding TF activity, Pol II cis-regulatory DNA binding): ACCEPT.
- Chromatin, nucleus: ACCEPT (ChIP shows chromatin occupancy in Capsaspora).
- Transcription regulation process rows: ACCEPT; positive regulation supported by
  Xenopus activation and by association of Bra sites with active marks.
- Cell fate specification (TreeGrafter from deep T-box node): REMOVE. Embryonic
  fate specification by animal T-box factors; no evidence that CoBra designates a
  cell fate in Capsaspora (which has temporal life stages, not developmental
  lineages), and the Xenopus rescue is heterologous and nonspecific. Propagation
  review: PROPAGATION_BAD / LINEAGE_OR_TAXON_MISMATCH (not a formal taxon-constraint
  violation: GO:0001708 is only_in_taxon cellular organisms, QuickGO 2026-10-01).
- NEW: GO:0043565 sequence-specific DNA binding, IDA, PMID:24043797 (in vitro PBM).
  The Capsaspora ChIP-qPCR (PMID:27114036) would support IDA GO:0000978, but that term
  is already in GOA (IEA), so it is recorded in the review of that row.
