# hippo (Salpingoeca rosetta, F2UQC7, PTSG_10780) - curation notes

**Automated deep research was unavailable** (no deep-research provider key in this
environment). These notes are built manually on 2026-10-01 from cached publications in
`publications/` and from database lookups (UniProt REST, InterPro, PANTHER 19 treeinfo
API, QuickGO). No `-deep-research-*.md` file exists for this gene.

## Identity

- UniProt F2UQC7 (TrEMBL), 459 aa, ORF PTSG_10780, EMBL EGD79795.1, RefSeq XP_004988744.1.
- Locus-to-gene mapping: the knockout preprint (DOI:10.1101/2024.07.13.603360) designed
  gRNAs against "the S. rosetta homologs of Hippo (PTSG_10780), Warts (PTSG_04961) and
  Yorkie (PTSG_06057)" per the project coordinator's reading of the preprint. The version
  cached in `publications/` (v1, PDF text) does not contain the PTSG IDs; its Fig. 5
  legend says the orthologs were "identified by (Sebé-Pedrós et al., 2012). Sequences
  were retrieved from UniProt". Independent check: a UniProt query for S. rosetta proteins
  with InterPro IPR024205 (Mst1/2 SARAH) returns only F2UQC7, so it is the only MST-type
  kinase+SARAH protein in the proteome (two other SARAH-domain proteins, F2TX21 and
  F2TZ10, lack the MST signature).

## Domains (UniProt / CDD / InterPro)

- Protein kinase 24-275, ATP-binding K53; CDD cd06612 STKc_MST1_2; SARAH 406-453,
  CDD cd21884 SARAH_MST_Hpo; disordered 297-322.
- Hpo homologs are defined by this architecture
  [PMID:22832104 "Our searches further identified homologues of Hpo, defined by the presence of a Ste20-like kinase domain and a SARAH domain"].
- The M. brevicollis Hippo gene is predicted to be truncated
  [PMID:38729842 "Further, the M. brevicollis Hippo gene contains an insertion that is predicted to truncate the protein at the beginning of the kinase domain [65]."]
  F2UQC7 has an intact kinase domain.

## PANTHER placement

- PTHR48012:SF10 "FI20177P1"; Drosophila hpo and human STK3 are in PTHR48012:SF2.
- The TreeGrafter node in GOA rows is PTN004698602, a DUPLICATION node whose leaves (PANTHER 19,
  filtered to human/fly/worm/yeast/M. brevicollis) are SLK, STK10, STK24/25/26, STK39,
  OXSR1, MAP4K1-5, fly Slik/fray/hppy/GckIII, worm gck-1..4, yeast KIC1 - i.e. a deep
  germinal-centre kinase node, not the MST1/2 clade. Its propagated terms (Ser/Thr kinase
  activity, cytoplasm) are generic enough that this does not matter.

## Experimental findings (Combredet & Brunet preprint, full text cached)

- Two KO clones per gene [DOI:10.1101/2024.07.13.603360 "isolated two knockout clones for each gene by insertion"].
- hippo and warts KO proliferate more slowly
  [DOI:10.1101/2024.07.13.603360 "On the other hand, hippopac1 and warts pac1 KO clones proliferated markedly slower"]
  (doubling time about 11.7 h for hippo versus about 8.1 h for wild type, per the same paragraph).
- hippo KO rosettes are normal in size
  [DOI:10.1101/2024.07.13.603360 "The size of hippopac1 and yorkiepac1 rosettes did not significantly differ from wild type (11.6 ± 1.7 cells and 9.8 ± 3.1 cells"].
- All KO clones form rosettes
  [DOI:10.1101/2024.07.13.603360 "all six KO clones reliably developed into rosettes, as did wild-type cells"].
- Authors' framing: slower growth is the opposite of the animal loss-of-function phenotype
  [DOI:10.1101/2024.07.13.603360 "down proliferation in S. rosetta, which is the opposite of their animal loss-of-function phenotype"].
- The published version (PMID:41037400, abstract only cached) mentions only warts and
  yorkie knockouts in the abstract.

## Capsaspora context

- Co-Hpo activates the fly cascade
  [PMID:22832104 "Interestingly, Co-Hpo also stimulated the phosphorylation of Dm-Wts and Dm-Yki, as revealed by phospho-specific antibodies against P-Dm-Wts-T1077 and P-Dm-Yki-S168, respectively (Figure 4D)."]
- coWts loss has the stronger Yki-localization phenotype than coHpo loss
  [PMID:38517944 "Interestingly, we found that coWts-/- cells were significantly more likely to show nuclear mScarlet-coYki localization than coHpo-/- cells (Figure 1D)"].

## Review decisions (summary)

- Ser/Thr kinase activity, ATP binding, cytoplasm, signal transduction: ACCEPT (domain /
  family-level). Nucleotide binding: KEEP_AS_NON_CORE.
- No NEW terms. hippo signaling not added: no S. rosetta evidence that Hippo acts
  upstream of Warts, and the KO phenotypes diverge (only warts affects rosette size).

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
