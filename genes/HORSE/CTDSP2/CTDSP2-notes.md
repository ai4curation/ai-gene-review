# CTDSP2: exact-sequence caution

The selected horse F7A4N8 is 174 aa and maps to VGNC:16932 / ENSECAG00000018788. Human CTDSP2 O14595 is 271 aa with an FCP1-homology domain and catalytic Asp107/Asp109. The alignment matches the horse N-terminus through about residue 84; the remainder diverges and does not retain the human catalytic domain. No InterPro phosphatase or kinase domain is listed in the selected horse record. Absence of an annotation alone is not proof of absent function, but the actual sequence discontinuity makes ordinary whole-protein functional transfer unsafe.

[PMID:12721286](https://pubmed.ncbi.nlm.nih.gov/12721286/), DOI [10.1074/jbc.M301791200](https://doi.org/10.1074/jbc.M301791200), describes the small CTD phosphatase family: “preferentially catalyze the dephosphorylation of Ser5 within the consensus repeat.” The abstract foregrounds SCP1; it cannot alone establish which CTDSP2 assays were performed. The existing human CTDSP2 experimental annotation is retained with this access limitation rather than rejected for paralog misattribution. [PMID:15681389](https://pubmed.ncbi.nlm.nih.gov/15681389/) is the REST/neuronal silencing source in the curated record.

The abnormal horse model does not establish evolutionary loss or a pseudoenzyme: transcript/exon validation and an alternative full-length horse product are needed before distinguishing a genuine isoform from a gene-model problem. The input used at prediction time is not separately recovered. Do not label this WRONG_INPUT_SEQUENCE without such evidence. A completed human Falcon report has been inspected; horse-specific Edison is not indicated by the genome-only identification sources.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

**Deep research.** `just deep-research-falcon HORSE CTDSP2 --fallback perplexity-lite` failed: falcon raised "Failed to authenticate", and the perplexity-lite fallback returned HTTP 401 (insufficient quota). No horse deep-research file exists. This review relies on the curated human record, the two cached SCP papers, and a new sequence and gene-model analysis.

**GOA.** F7A4N8 has no GO annotations: the GOA file has a header and no rows. There are no existing annotations to adjudicate.

**Identity of the benchmark accession: an alternative-transcript product.** The analysis is `CTDSP2-bioinformatics/compare_sequences_rereview.py`, which writes `RESULTS-rereview.md` and `results-rereview.json`. Its sequences and Ensembl model are saved beside it. The existing `align.py`, `RESULTS.md` and `results.json` were not changed.
- The horse CTDSP2 gene, ENSECAG00000018788 on chr6, has three protein-coding transcripts:
  - ENSECAT00000107019 is the Ensembl canonical transcript. It encodes 312 aa, UniProt A0A9L0T5X1 (unreviewed, no gene name in UniProt).
  - ENSECAT00000138494 encodes 252 aa, UniProt A0A9L0R207.
  - ENSECAT00000020049 encodes 174 aa, UniProt **F7A4N8**, the benchmark accession.
- F7A4N8 matches human CTDSP2 (O14595, 271 aa) over its first 84 residues. Its sixth exon is 375 bp, 76298535-76298161. The other two transcripts use a 102-bp exon, 76298262-76298161, so F7A4N8's exon extends 273 nt upstream of their acceptor site. That extra sequence encodes 90 residues unrelated to CTDSP2 (GIRFWGTARV...) and then a stop codon. Four exon junctions follow the stop, so this transcript is a likely target of nonsense-mediated decay.
- F7A4N8 lacks the whole FCP1-homology domain (human 97-255). It has no DxDx(T/V) motif and no counterpart of the catalytic Asp107 (nucleophile) or Asp109 (proton donor). The only features UniProt predicts on it are a MobiDB disordered or low-complexity stretch in the novel tail.
- The earlier `RESULTS.md` reported 57.1% identity over 170 paired residues. That figure comes from forcing a global alignment onto the unrelated tail. The real picture is a nearly identical 84-residue prefix followed by unrelated sequence.
- Neither full-length horse model reproduces the human architecture exactly. A0A9L0T5X1 has an N-terminal extension that does not start with Met and lacks the 13-aa SDLLQCLQYQFYQ exon. A0A9L0R207 keeps that exon but lacks the 19-aa exon after DLDETLVHSSFK. Both keep the catalytic DLDET motif, at positions 148 and 107 respectively.

**Evolutionary grounding.** Horse is not among the PANTHER 19.0 reference proteomes, and InterPro gives only the family PTHR12210 for A0A9L0T5X1, with no subfamily. PANTHER places human, mouse, cow, rat and Xenopus CTDSP2 in PTHR12210:SF187, separately from CTDSP1 (SF139) and CTDSPL (SF43). In a neighbour-joining tree of the catalytic region, A0A9L0T5X1 groups with human, cow and mouse CTDSP2 at 97-100% identity. CTDSP1 is at 78% and CTDSPL at 81%. The VGNC orthology assignment and the tree agree, so the full-length horse product is the CTDSP2 ortholog. PAINT node PTN000954535 (GO:0008420, seeded by O14595 and Q9GZU7) would apply to the full-length product. It cannot apply to F7A4N8, because F7A4N8 lacks the domain that defines the inherited activity.

**Decisions.**
- The description was rewritten to say that this is a truncated alternative-transcript product of a gene that also encodes a full-length catalytic CTDSP2.
- No core function was asserted. Phosphatase activity, nuclear localisation and REST-dependent silencing all belong to the full-length product and are not transferred to F7A4N8. The validator's "no core functions" warning is expected, and the status is DRAFT.
- The suggested questions and experiments were updated to cover transcript support and NMD sensitivity, and to ask which full-length model is right.
- The GN-line finding was replaced with the Ensembl DR line and the MobiDB feature. The DE/SubName quote, a label imported from Ensembl, was replaced with the PE line.

**Relative to review next.** A0A9L0T5X1, the full-length catalytic product of the same horse gene (Ensembl canonical), would go in `genes/HORSE/CTDSP2__A0A9L0T5X1`. It has no review. The human ortholog CTDSP2 (O14595, `genes/human/CTDSP2/`) has every annotation actioned.

**Modules.** No module under `modules/` mentions CTDSP2 or O14595. `gocams/index.tsv` has no entries for these accessions.
