# ptxR (PA2258, P72131) review notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE P72131 --alias ptxR`; accession matches the worklist.
No deep-research provider was used; PubMed esearch unavailable (NCBI SOLR errors), Europe PMC
used. Cached: PMID:22844393 (full text read), PMID:8843437 and PMID:16803594 (abstract only).

### Literature

- PMID:8843437 (Hamood et al. 1996): ptxR found as a gene raising exotoxin A production;
  [PMID:8843437 "The deduced amino acid sequence of PtxR is homologous to that of several members
  of the LysR family of transcriptional activators."]; ptxR mutants have less exotoxin A
  activity; [PMID:8843437 "ptxR increases toxA and regA transcription"].
- PMID:22844393 (Daddaoua et al. 2012, full text): DNaseI footprint and ITC of PtxR on PtoxA
  (palindrome CGCCGCCGCG overlapping -35) and Pkgu/Pgad; [PMID:22844393 "In this study we
  confirmed that in a ΔptxR background, expression of toxA is almost three-fold lower than in the
  parental strain, an observation which confirms the positive role of PtxR."]; PtxS binds PtxR.
- PMID:16803594 (Carty et al. 2006): [PMID:16803594 "Mutation of ptxR in PAO1 increased pyocyanin
  production."]; PtxR reduces phzA1-G1 and pqsABCDE expression; ptxR mutation lowers lasB.

### Annotation decisions

- GO:0045893 (IDA, seed), GO:0001216 (IPI), GO:0000976 (IBA, IPI): ACCEPT.
- GO:0006355 (IBA, IEA), GO:0003700 (IEA): TOO_GENERAL.
- GO:0032993 (IPI): KEEP_AS_NON_CORE.
- GO:0003950 NAD+ poly-ADP-ribosyltransferase activity (IMP, PMID:8843437): REMOVE; it is the
  activity of the target toxin ToxA. PSEUDOCAP WRONG_TERM defect, CONFIRMED (the abstract states
  PtxR is a LysR regulator and the readout was exotoxin A activity).
- GO:0045862 positive regulation of proteolysis (IMP): MARK_AS_OVER_ANNOTATED (lasB expression,
  probably via QS; abstract only).
- GO:1900377 (IMP): MODIFY to GO:1900981 negative regulation of phenazine biosynthetic process.
- Action counts: ACCEPT 4, TOO_GENERAL 3, KEEP_AS_NON_CORE 1, REMOVE 1, MARK_AS_OVER_ANNOTATED 1,
  MODIFY 1.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001248394 | GO:0006355 regulation of DNA-templated transcription | 7 | 202 (30 taxa) | GO:0045893, IDA, PMID:22844393 (PseudoCAP) | SOUND | Full text read: PtxR footprints a -35 palindrome at PtoxA (and Pkgu, Pgad) and toxA expression falls three-fold in the deletion. Generic term suits a LysR clade. | E. coli MetR, YjiE, AaeR, YhaJ; P. aeruginosa CysB (G3XCU6) and Q9I1R1 | Yes |

Consistent with the cysB review (`genes/PSEAE/cysB/cysB-notes.md`), which also judged this node
SOUND. No GO_CENTRAL defect. The PSEUDOCAP defect on GO:0003950 concerns a non-seed row.
