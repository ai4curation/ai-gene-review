# yorkie (Salpingoeca rosetta, F2UDK1, PTSG_06057) - curation notes

**Automated deep research was unavailable** (no deep-research provider key in this
environment). These notes are built manually on 2026-10-01 from cached publications in
`publications/`, database lookups (UniProt REST, PANTHER 19 treeinfo API, QuickGO), and
our own sequence analysis in `yorkie-bioinformatics/` (RESULTS.md).

## Identity

- UniProt F2UDK1 (TrEMBL, PE 4), 714 aa, ORF PTSG_06057, EMBL EGD74696.1, RefSeq XP_004992953.1.
- Locus mapping per the coordinator's reading of the preprint gRNA sentence (PTSG_06057 =
  Yorkie). The cached preprint text (v1) does not contain PTSG IDs.
- **Caveat:** PANTHER places F2UDK1 in PTHR10316:SF68 (MAGI-related family), while another
  S. rosetta WW protein, F2U5K0 (PTSG_03848), is classified in the YAP1 family
  (PTHR17616:SF8 "TRANSCRIPTIONAL COACTIVATOR YORKIE", InterPro IPR051583 YAP1).
  Our analysis (RESULTS.md, reviewer's own) supports F2UDK1 as the Yorkie homolog:
  - two WW domains and four HXRXXS motifs (S152, S283, S394, S423), matching
    [PMID:38729842 "like most animals, srYki has 2 WW domains, whereas mbYki has 1, and srYki has 4 putative Warts phosphorylation sites"];
    F2U5K0 has three WW-domain matches and only two HXRXXS-like matches;
  - full-length local alignment scores against YAP1, Yki and coYki are higher for
    F2UDK1 than for F2U5K0 (much of the similarity is in WW domains).
  A phylogeny was not run; this should be confirmed.

## TEAD-binding domain

- Literature: [PMID:38729842 "the srYki TBD shows less conservation with Yorkie/YAP/TAZ than coYki, with srYki lacking conserved residues within the α2 helix that are critical for YAP-TEAD interaction in mammals"];
  [PMID:38729842 "The degree to which choanoflagellate Yorkie orthologs interact with Sd/TEAD proteins is therefore currently unclear"].
- Earlier claim, now disputed for F2UDK1:
  [PMID:22832104 "Importantly, all these non-metazoan Yki homologs contain highly conserved functional sites like the Hippo pathway responsive phosphorylation site S168/127 and the N-terminal homology region that is critical for interaction with Sd/TEAD transcription factor (Figure 2A)."]
- Our motif scan: no LxxLF (YAP alpha1) or PxSFF (omega loop) motif anywhere in F2UDK1;
  alignment of YAP1/Yki TBD segments to the F2UDK1 N-terminus is no better than to an
  unrelated region. Inconclusive about a divergent interface.

## PANTHER placement - Track C

- GOA rows (cytoplasm, signal transduction) cite PTN002569196. PANTHER 19 tree: path
  PTN000817101 (Eumetazoa) > PTN000034930 (Bilateria) > PTN008497523 (Protostomia) >
  PTN008497524 (duplication) > **PTN002569196 (Ecdysozoa)**, leaves Drosophila CG42788,
  Anopheles AGAP003128, Pristionchus WBGene00104942. A choanoflagellate Yorkie homolog
  grafted into an ecdysozoan MAGI-related node: WRONG_ORTHOLOG_OR_PARALOG. The two
  terms are generic and plausible for a Yorkie homolog anyway, so they are kept as non-core.

## Experimental findings (Combredet & Brunet preprint, full text cached)

- [DOI:10.1101/2024.07.13.603360 "Growth curves indicated that yorkiepac1 KO cells proliferated at a similar rate to the wild type"]
  (doubling about 8.5 h versus 8.1 h).
- [DOI:10.1101/2024.07.13.603360 "The size of hippopac1 and yorkiepac1 rosettes did not significantly differ from wild type (11.6 ± 1.7 cells and 9.8 ± 3.1 cells"].
- [PMID:41037400 "RNA sequencing revealed that Warts and Yorkie regulated several extracellular matrix genes involved in multicellularity (including couscous)"] - direction of regulation not in the abstract.

## Review decisions (summary)

- cytoplasm: KEEP_AS_NON_CORE (wrong-family propagation; plausible for Yki/YAP).
- signal transduction: KEEP_AS_NON_CORE (same).
- No NEW rows; no MF asserted in core_functions (coactivator activity and TEAD binding
  untested, TBD poorly conserved).

## Locus-ID provenance (added by the coordinating session)

The cached copy of DOI:10.1101/2024.07.13.603360 is version 1 of the preprint
(July 2024 PDF), which does not name the PTSG loci. Version 2 (January 2025;
read from bioRxiv's JATS XML during this session, not cached) states the
mapping directly: "We designed gRNAs targeting the beginning of the coding
sequence of the S. rosetta homologs of Hippo (PTSG_10780), Warts (PTSG_04961)
and Yorkie (PTSG_06057)". PTSG_10780 = F2UQC7, PTSG_04961 = F2U943 and
PTSG_06057 = F2UDK1 in UniProt. So the paper itself identifies F2UDK1, not the
PANTHER YAP1-family member F2U5K0 (PTSG_03848), as the gene knocked out as
yorkie. Whether F2UDK1 is the true Yorkie ortholog is still open (it lacks the
TEAD-interface motif; see yorkie-bioinformatics/RESULTS.md).
