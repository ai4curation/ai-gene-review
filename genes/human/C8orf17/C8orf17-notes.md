# C8orf17 (MOST-1) notes

## 2026-10-08 Tier 4 microprotein review

### Locus and existence
- UniProt Q9NRJ1 (MOST1_HUMAN), 99 aa, PE1 (protein-level, from an antibody raised to a
  synthetic peptide in PMID:17143515). No InterPro/Pfam domain; no PANTHER family; "PAN-GO: 0
  GO annotations based on evolutionary models". Reference proteome lists it as "Unplaced".
  UniProt CAUTION: "Encoded in an intron of the TRAPPC9 gene."
- HGNC (REST, 2026-10-08): locus_type **unknown**, name "chromosome 8 putative open reading
  frame 17", alias MOST-1.
- Ensembl ENSG00000250733: single transcript ENST00000507535, biotype **TEC** (to be
  experimentally confirmed), no annotated translation; Ensembl REST returns no orthologues.
- Discovery paper: intronless gene, 297-bp ORF in a 2.8-kb cDNA, "encoding a putative
  hydrophilic polypeptide of 99 amino acids" [PMID:12665628]; "No notable amino acid
  sequence motifs were evident." [PMID:12665628]. Northern blot could not detect the
  transcript [PMID:12665628 "inability to detect MOST-1 transcripts by northern blot
  analysis"]. A mouse fragment identical to the human ORF was reported from NS-1 myeloma
  cDNA, but a 100% identical mouse sequence is more consistent with contamination than an
  ortholog, and no ortholog is annotated in Ensembl.

### Function evidence (all from one lab, 2003 and 2007)
- PMID:17143515 (abstract only): cytoplasmic localisation in four cell lines; knockdown in
  DU145 "resulted in reduced cell proliferation but enhanced apoptosis"; Y2H with seven
  proteins; co-IP validated "ferritin light chain, peripheral benzodiazepine receptor, and
  immunoglobulin C (mu) and C (delta) heavy chain". Abstract does not mention nucleus or ER;
  UniProt's microsome/ER membrane lines cite this paper, presumably from full text.
- PubMed search "C8orf17" (2026-10-08): 3 hits; the third (PMID:18000363) is an 8q array CGH
  study, not functional.

### Decisions
- Two bare protein binding IPI rows: REMOVE (uninformative; interactions not disputed).
- cytoplasm IDA + IEA: ACCEPT.
- nucleus IDA, ER membrane IEA: UNDECIDED (full text unavailable; abstract reports cytoplasm
  only; a hydrophilic 99-aa protein with no TM segment).
- proliferation / anti-apoptosis NAS: MARK_AS_OVER_ANNOTATED (single knockdown in one cancer
  line, transcript is TEC with no ortholog; RNA- vs protein-level effect not separable).
- No MF, no NEW.
