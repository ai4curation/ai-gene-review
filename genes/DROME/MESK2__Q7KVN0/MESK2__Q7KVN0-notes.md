# MESK2 (Q7KVN0, isoform I; CG15669, FBgn0043070) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

No ProtNLM2 file or prediction-evidence folder was opened. Sources: GOA/UniProt for Q7KVN0,
PANTHER 19.0 classification files, PAINT (interpro/panther/PTHR11034/), the cached literature,
the full text of PMID:33827210 (fetched from PMC), and the sequence analysis already done in the
sibling isoform folder genes/DROME/MESK2 (keyed to Q8T0V2).

### Setup

- `just fetch-gene DROME Q7KVN0 --alias MESK2__Q7KVN0`: one GOA row on Q7KVN0 (HDA serine
  hydrolase activity, PMID:33827210, FlyBase).
- `just deep-research-falcon DROME MESK2__Q7KVN0 --fallback perplexity-lite` FAILED: falcon
  "Failed to authenticate"; perplexity-lite fallback HTTP 401 insufficient quota. No deep-research
  file exists in this folder. The falcon report for the same gene in genes/DROME/MESK2/ was used
  as a literature pointer; its primary citations were re-checked in publications/.

### Record identity

- Q7KVN0 (TrEMBL, 485 aa, isoform I) is the UP000000803 gene-centric canonical. It is
  sequence-identical to Q9GU50 [file:DROME/MESK2/MESK2-bioinformatics/RESULTS-rereview.md
  "Q7KVN0 == Q9GU50: True"]. Q9GU50 carries the gene's two IBA rows (cytoplasm, signal
  transduction, from PTN000867215); Q7KVN0 carries only the HDA row.

### Evolutionary placement

- PANTHER 19.0: MESK2 (via Q9GU50) is in PTHR11034:SF56 (GH09802P); human NDRG1/2/3/4 are in
  SF18/SF17/SF20/SF21 [file:DROME/MESK2__Q7KVN0/MESK2__Q7KVN0-bioinformatics/RESULTS.md]. So
  no paralog-specific NDRG function is transferred.
- PAINT PTN000867215 (Eumetazoa): IBD cytoplasm (seeds NDRG1-4 of human/mouse/rat) and IBD
  signal transduction (seed human NDRG1 only). PTN002592750 (Euteleostomi, ERK1/2 cascade,
  seed NDRG4) is not ancestral to MESK2; that omission is treated as deliberate.

### HDA serine hydrolase activity (PMID:33827210)

- Full text read (PMC7610703 via NCBI efetch; extraction script
  MESK2__Q7KVN0-bioinformatics/abpp_fulltext_extract.py). MESK2 is in Table 1 ("List of SHs
  showing sexual dimorphism in activities in adult fly"): "MESK2 | Unknown hydrolase | Male |
  Head". Identification is protein-level peptide counts after FP-biotin/avidin enrichment;
  heat-denatured controls are described only for gel ABPP. No probe-site peptide, competition or
  MESK2 follow-up.
- Q7KVN0 has Gly152 at the nucleophile elbow (IGFGVGAGANI), as human NDRG2, whose structure
  lacks the Ser-His-Asp triad [PMID:21247902]. GO:0017171 is defined by a serine nucleophile
  in a triad (definition checked in OLS).
- Decision: MARK_AS_OVER_ANNOTATED. Probe recovery is a genuine observation but does not establish
  triad catalysis; not a core function and not to be transferred.
- Note: I tried `cache_publication(force=True)` for PMID:33827210 to get the full text into
  publications/, but it changed the cached title (HTML entities removed), which would affect
  eight other reviews citing that PMID. I restored the original cached file byte-for-byte and
  recorded the full-text extraction in this gene's bioinformatics folder instead.

### Biology (genetic/phenotypic only)

- Misexpression modifier of RAS1/KSR signalling in eye (PMID:11063696); glial RNAi reduces
  circadian rhythmicity (PMID:29487148); recessive lethal insertion alleles. All necessity or
  overexpression evidence; no process annotation proposed (CLAUDE.md participation rule).

### Decisions

- GO:0017171 HDA: MARK_AS_OVER_ANNOTATED.
- NEW GO:0005737 cytoplasm (IBA, GO_REF:0000033): inherited from PTN000867215, already on the
  sequence-identical Q9GU50.
- Signal transduction IBD (on Q9GU50) not added as NEW: the term is very broad and the fly
  evidence is misexpression-only; raised as a suggested question instead.
- Core function: noncatalytic NDRG alpha/beta-hydrolase-fold protein of unknown activity, in
  cytoplasm (inferred). For transfer purposes: nothing about MESK2 molecular function is
  experimentally established; location is phylogenetically inferred; phenotypes are genetic.
