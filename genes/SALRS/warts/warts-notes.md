# warts (Salpingoeca rosetta, F2U943, PTSG_04961) - curation notes

**Automated deep research was unavailable** (no deep-research provider key in this
environment). These notes are built manually on 2026-10-01 from cached publications in
`publications/` and from database lookups (UniProt REST, InterPro API, PANTHER 19 treeinfo
API, QuickGO). No `-deep-research-*.md` file exists for this gene.

## Identity

- UniProt F2U943 (TrEMBL), 833 aa, ORF PTSG_04961, EMBL EGD73246.1, RefSeq XP_004994277.1.
- Locus mapping per the coordinator's reading of the preprint gRNA sentence (PTSG_04961 =
  Warts). The cached preprint text (v1) does not contain PTSG IDs. Independent check:
  F2U943 is the only S. rosetta protein in PANTHER subfamily PTHR24356:SF418 "SERINE_THREONINE-PROTEIN
  KINASE WARTS" (UniProt query, 2026-10-01; other S. rosetta PTHR24356 members are in SF1,
  SF163, SF414).

## Domains

- Disordered N-terminal region (1-345, several low-complexity segments); protein kinase
  456-763 (Pfam split 457-616 / 654-763, i.e. an insert between the lobes, typical of
  NDR/LATS kinases); ATP-binding K485; catalytic D579; AGC C-terminal 764-833; predicted
  phosphoserine 810. No CDD MOB-binding (MobB_LATS) hit is reported for this entry, unlike
  Capsaspora coWts.

## PANTHER placement - Track C

- F2U943 is in PTHR24356:SF418 with human LATS1 (O95835, SF138 in members table) - the
  LATS family, unlike Capsaspora coWts (PTHR22988:SF71, Rho-effector kinases).
- GOA rows cite PTN001220369. In the PANTHER 19 tree this is the **M. brevicollis Warts
  leaf (MONBRDRAFT_1233)**; F2U943 was grafted onto it. Its parent is **PTN002390470**,
  a SPECIATION node with species label "Metazoa-Choanoflagellida", whose descendants (with
  a human/fly/Nematostella/M. brevicollis filter) are LATS1, LATS2, wts, the Nematostella
  Warts and the M. brevicollis Warts.
- QuickGO: PTN002390470 is the with/from of 224 annotations, IBA for GO:0000082, GO:0035329,
  GO:0043065 and GO:0046620 across bilaterians, Nematostella (45351), Trichoplax (10228)
  and M. brevicollis (81824). PTN001220369 is the with/from of only the 6 S. rosetta IEA rows.
- IBA donors (from the LATS1 IBA rows): G1/S - MGI:1354386 (Lats2), UniProtKB Q9NRM7
  (LATS2); hippo signaling - FBgn0011739 (wts), MGI:1333883 (Lats1), MGI:1354386,
  O95835, Q9NRM7; positive regulation of apoptotic process - FBgn0011739 (wts);
  regulation of organ growth - MGI:1354386 (Lats2).
- So the PAINT curator placed an organ-growth outcome term at a node that includes
  unicellular choanoflagellates. GO:0046620 taxon constraints exclude only Bacteria,
  Archaea, S. pombe and S. cerevisiae (QuickGO, 2026-10-01). Organ-level terms on a
  choanoflagellate are a clear LINEAGE_OR_TAXON_MISMATCH.

## Experimental findings (Combredet & Brunet preprint, full text cached)

- Rosette size: [DOI:10.1101/2024.07.13.603360 "warts pac1 cells grew into giant rosettes containing about twice as many cells as wild-type ones (21.1 ± 4.4 versus 10.9 ± 3.8 cells per rosette, respectively)"];
  maxima [DOI:10.1101/2024.07.13.603360 "as many as 60 cells, while their wild type counterparts did not exceed 25 cells"].
- ECM: [DOI:10.1101/2024.07.13.603360 "that ECM core appeared larger and with a more conspicuously branched geometry in warts pac1"].
- Growth: [DOI:10.1101/2024.07.13.603360 "On the other hand, hippopac1 and warts pac1 KO clones proliferated markedly slower"]
  (doubling about 10.2 h versus 8.1 h wild type).
- Rosettes still form: [DOI:10.1101/2024.07.13.603360 "all six KO clones reliably developed into rosettes, as did wild-type cells"].
- Authors' conclusion: [DOI:10.1101/2024.07.13.603360 "These observations pinpoint warts as a genetic regulator of S. rosetta rosette size"].
- Published version adds RNA-seq: [PMID:41037400 "RNA sequencing revealed that Warts and Yorkie regulated several extracellular matrix genes involved in multicellularity (including couscous)"];
  [PMID:41037400 "suggesting that Hippo signaling regulates multicellular size in choanoflagellates by modulating matrix secretion"].
- Not measured: Warts kinase activity, Yorkie phosphorylation or localization, Warts
  localization, Hippo-to-Warts phosphorylation, cell death.

## Review decisions (summary)

| Term | Action | Reason |
|---|---|---|
| G1/S transition of mitotic cell cycle | MARK_AS_OVER_ANNOTATED | vertebrate LATS2 donor; no S. rosetta cell-cycle data; KO slows growth |
| nucleotide binding | KEEP_AS_NON_CORE | uninformative parent |
| protein kinase activity | KEEP_AS_NON_CORE | parent of Ser/Thr kinase |
| protein serine/threonine kinase activity | ACCEPT | LATS-clade kinase, catalytic residues intact |
| ATP binding | ACCEPT | domain-level |
| cytoplasm | ACCEPT | expected for Warts/LATS |
| kinase activity, transferase activity | KEEP_AS_NON_CORE | general parents |
| hippo signaling | ACCEPT | IBD at Choanozoa node consistent with Capsaspora evidence |
| intracellular signal transduction | KEEP_AS_NON_CORE | parent of hippo signaling |
| positive regulation of apoptotic process | MARK_AS_OVER_ANNOTATED | fly tissue-growth donor; no choanoflagellate apoptosis data |
| regulation of organ growth | REMOVE | choanoflagellates have no organs; IBD node too deep for this outcome term |
| cell periphery | UNDECIDED | ARBA rule, no data |

No NEW rows. A hippo signaling IMP was considered and rejected: the rosette-size and
growth phenotypes are downstream outcomes, not tests of Warts doing a step of the cascade
in S. rosetta. No rosette-size term exists in GO (see rosetteless NTR).

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
