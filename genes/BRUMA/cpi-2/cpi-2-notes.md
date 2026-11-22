# BRUMA cpi-2 notes

## 2026-11-22 cross-check

- `genes/BRUMA/cpi-2/cpi-2-goa.tsv` has six rows for UniProtKB A0A0K0IP23:
  three cysteine-type endopeptidase inhibitor rows, an aspartic-type
  endopeptidase inhibitor row, and TreeGrafter `cytoplasm` and `vesicle`
  cellular-component rows.
- UniProtKB identifies A0A0K0IP23 as reviewed *Brugia malayi* cystatin CPI-2,
  with a predicted residues 1-25 signal peptide, a mature residues 26-161
  chain, PANTHER `PTHR46186:SF2`, and the Asn-77 motif and mutagenesis
  features needed for host LGMN/AEP inhibition.
- PMID:11301256 is cached as an abstract only, but directly supports
  cysteine-type endopeptidase inhibitor activity by showing that Bm-CPI-2
  "inhibits multiple cysteine protease activities" in endosomes/lysosomes from
  human B-lymphocyte lines.
- PMID:15664654 is cached as an abstract only, but directly supports the
  bifunctional papain-like and AEP/legumain inhibitory activities and shows
  that the Asn-77 AEP site distinguishes Bm-CPI-2 from the *C. elegans* CPI-1
  and CPI-2 comparators.
- The PMID:15664654 `GO:0019828` aspartic-type endopeptidase inhibitor row is
  likely an asparaginyl-versus-aspartic term slip. Murray et al. assayed
  asparaginyl endopeptidase, a legumain-family cysteine protease, and UniProt
  already has a cysteine-type endopeptidase inhibitor row from the same paper.
- The TreeGrafter `cytoplasm` and `vesicle` rows appear to be broad
  PANTHER-family propagation onto a secreted cystatin. The N-terminal signal
  peptide and host endosomal/lysosomal targets support secretion, but they do
  not support a mature cytoplasmic pool or vesicle residency for CPI-2.
- This cross-check did not run a remote deep-research provider and did not
  refresh any cached publications. It used the existing initialized BRUMA
  review, local UniProt and GOA snapshots, and the two cached primary-publication
  abstracts.
