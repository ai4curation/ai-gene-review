# ZNF689__C0HLU2 (SEHBP) review notes

## Identity

- UniProt C0HLU2 (SEHBP_HUMAN), "Transcriptional regulator SEHBP", 46 aa, PE1. UniProt files it
  under the host gene symbol ZNF689 (HGNC:25173); it is a distinct protein from the ZNF689 zinc-finger
  protein, so it is reviewed in its own folder per the alt-ORF convention.
- Encoded by an upstream ORF in the 5' UTR of ZNF689 mRNA
  [PMID:33468658 "SEP10 is found within the 5′UTR of ZNF689 (Zinc Finger Protein 689) and encodes a 46 amino acid gene product that displays high amino acid sequence homology across mammalian species"].
- Translation supported by Ribo-seq in HEK293T, HeLa-S3, K562
  [PMID:33468658 "Ribo-seq–based profiling suggested that the SEP10 sORF has high ribosomal occupancy in these human cell lines"].
- Pfam PF21978 / InterPro IPR054150 (SEHBP family). Ensembl ENSG00000289491 (separate gene id from ZNF689).

## Literature

Only one paper characterises the peptide: Koh et al. 2021 PNAS (PMID:33468658, full text cached).
PubMed searches (SEHBP; ZNF689 + uORF/microprotein/peptide) return only ZNF689 zinc-finger-protein
papers (HCC, TNBC, miR-339 target), which are about the host protein, not the peptide. No
independent replication, no loss-of-function study.

### Findings (Koh et al. 2021)

- Identified in a photo-crosslinking (AbK) AP-MS screen of conserved SEPs ("SEP10"). AP-MS hits:
  H2B, HMGN1-4, NME2, MYCBP
  [PMID:33468658 "SEP10 was found to precipitate histone H2B proteins isoforms (called H2B throughout), multiple members of the high mobility group nucleosome binding domain family (HMGN1, HMGN2, HMGN3, HMGN4)"].
- H2B binding validated: co-IP without crosslinking, reciprocal IP of endogenous H2B, and BLI with
  recombinant proteins, Kd 25 nM
  [PMID:33468658 "recombinant SEHBP and H2B strongly associate in vitro, as biolayer interferometry experiments determined their dissociation constant to be 25 ± 0.4 nM"].
  H3, MYCBP, HMGN1, HMGN4 were NOT recovered by non-crosslinked co-IP
  [PMID:33468658 "H2B alone was efficiently immunoprecipitated from HEK293T cells expressing SEHBP-FLAG without the need for crosslinking"].
- HMGN1/HMGN3: only detected after chemical crosslinking (DSS/EMCS) as high-MW adducts
  [PMID:33468658 "we confirmed that SEHBP additionally interacts with endogenous HMGN1 and HMGN3, as higher molecular weight adducts of these proteins were identified by Western blotting"].
  This is the basis of the two GO:0005515 IPI rows (P05114 HMGN1, Q15651 HMGN3).
- Localisation: tagged SEHBP (eGFP fusion and FLAG) in nucleus and cytoplasm of HEK293T
  [PMID:33468658 "SEHBP localizes in nuclear and cytoplasmic compartments in HEK293T cells"].
- Transcription: overexpression of SEHBP-eGFP altered 16.7% of transcripts, mostly down
  [PMID:33468658 "16.7% of the active transcriptome (1,985 of 11,586 transcripts) was significantly modulated in RNA-seq experiments when compared to a vector control"];
  [PMID:33468658 "the majority of transcripts altered by SEHBP overexpression were down-regulated (84%)"].
- ChIP-seq of overexpressed SEHBP-eGFP: 8,900 loci, 1,786 TSSs
  [PMID:33468658 "SEHBP was associated with 8,900 loci"].
- Mechanism unresolved by authors' own statement
  [PMID:33468658 "Determining whether this transcriptional program is a result of modulating active chromatin or derives from sequence specific targeting through yet-unknown interactions will necessarily be the work of future studies"].

## Assessment

- Evidence is all from one lab, one cell line (HEK293T), overexpressed tagged constructs. No
  knockdown/knockout of the endogenous peptide; no measurement of endogenous protein levels.
- MF: histone binding (H2B) is the best-supported activity (in vitro BLI + co-IP) -> ACCEPT.
  No GO "histone H2B binding" term exists (QuickGO search: only H2B enzyme/reader terms).
  Reader activity (GO:0140071) not justified: no modification specificity shown.
- BP: regulation of transcription by RNA pol II: overexpression RNA-seq + ChIP; direction is
  mainly repressive but cannot separate direct and indirect effects. Keep (ACCEPT) since
  it is the paper's central, curator-supported claim, but flag overexpression-only evidence.
- Protein binding (HMGN1/3): crosslinking-only, bare GO:0005515 is uninformative -> REMOVE.
  No more informative MF is supported (no "HMGN binding" term; chromatin binding would be a
  different assertion based on ChIP of an overexpressed fusion).
- Nucleus/cytoplasm IDA + IEA: ACCEPT (IDA); IEA duplicates ACCEPT (consistent).
- No NEW terms proposed. Chromatin binding (GO:0003682) from ChIP-seq of overexpressed GFP fusion
  is too weak to assert.
