# P91866 (F32H2.6) manual literature research

No deep-research API was available; this file records a manual literature and database search
(2026-10-28).

## Identity

- UniProtKB P91866 (TrEMBL, unreviewed, PE 4 "Predicted"), 187 aa, ORF F32H2.6,
  WormBase WBGene00009343, GeneID 185214, chromosome I. Protein name "Beta-ketoacyl synthase-like
  N-terminal domain-containing protein" (automatic name from the EMBL submission).
- Domain content: a single Pfam PF00109 (ketoacyl-synt, KS N-terminal) match at residues 28-167;
  InterPro IPR014030 (KAS_N), IPR016039 (Thiolase-like), IPR050091; PANTHER PTHR43775:SF7
  (FATTY ACID SYNTHASE). No PF02801 KS C-terminal domain and none of the other FAS domains
  (UniProt record, `P91866-uniprot.txt`).

## Literature

PubMed searches for "F32H2.6" return no paper about the gene. The only primary paper that mentions it
is Kniazeva et al. 2004 (PMID:15340492, full text cached), on monomethyl branched-chain fatty acids:

- F32H2.6 is a short homolog of the single predicted fatty acid synthase gene F32H2.5 (fasn-1) and
  can encode only its N-terminal part [PMID:15340492 "There is one predicted FAS gene, F32H2.5, and
  its shorter homolog, F32H2.6, in the C. elegans genome. The latter can only encode the N-terminal
  portion of the protein."].
- The two genes share extended nucleotide identity, so RNAi against either may hit both
  [PMID:15340492 "These genes share extended nucleotide identity, and RNAi of one could thus possibly
  affect the other."].
- RNAi "of F32H2.5 and F32H2.6" caused lethal growth arrest (data not shown) without changing fatty
  acid composition [PMID:15340492 "the RNAi-mediated disruption of F32H2.5 and F32H2.6 resulted in
  multiple defects and a lethal growth arrest (unpublished data)"]. Because of the cross-targeting
  caveat, this phenotype cannot be attributed to F32H2.6 rather than fasn-1.

## Sequence analysis (this review)

See `P91866-bioinformatics/RESULTS.md`. P91866 residues 1-167 are 67% identical to FASN-1 residues
28-194 and 40% identical to the start of human FASN, but the similarity ends immediately before the
KS active-site motif (human FASN "DTACSSS", Cys161); the KS catalytic Cys and both catalytic His
residues have no counterpart. The protein is therefore a catalytically incomplete fragment of a KS
domain.
