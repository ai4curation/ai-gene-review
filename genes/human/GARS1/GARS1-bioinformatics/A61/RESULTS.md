# Historical A61 sequence versus current mouse Gars1

The 342-nt historical clone U64446.1 has a strong **reverse-complement** correspondence to nucleotides **1456–1796 of mouse Gars1 NM_180678.3**. It is not an exact full-length match in either orientation. The interval lies wholly inside the RefSeq coding sequence, **42–2231**, not either UTR. The source records and exact differences remain preserved; this result does not identify the protein purified in PMID:8939962.

## Records and calculations

- The retained original GenBank record describes mouse AtT-20 clone A61, a partial CDS on the submitted plus strand, codon start 1, and AAC52893.1. Translation of its 342 nt reproduces its declared 114-aa peptide exactly.
- The original NCBI RefSeq record retrieved in this analysis is NM_180678.3, 2390 nt, dated 4 August 2026. Its CDS produces NP_851009.2, 729 aa. Translation reproduces the declared protein and the retained official UniProt Q9CZD3 sequence exactly.
- NM_180678.3 itself explicitly lists PMID:8939962 as reference 10 and uses Sgrp23 among its gene synonyms. This database association is retained; absent cross-references in a different record are not evidence of a wrong-gene assignment.
- Complete exact substring searches found no 342-nt match on either strand. Full-query affine-gap fitting then compared each orientation directly with this one transcript, without BLAST or a name-based identity assignment. Scores were match +2, substitution −3, gap open −7 and extension −1, with free transcript flanks and every query base included.
- The reverse-complement fit scores 630. All four optimal alignments span target 1456–1796 and contain **334 matching bases, five substitutions, three query-only bases and two target-only bases**. Thus 334/342 query bases match (97.66%); using all 344 alignment columns gives 97.09%. The four optima differ only in placement of the two target-only A bases within target 1649–1653. Each complete alignment, original-query coordinate and difference is recorded in [results/fitting-v2.json](results/fitting-v2.json).
- A 129-nt uninterrupted exact block independently matches reverse-complement query positions 4–132 to transcript 1457–1585. Five additional exact blocks of at least 10 nt are retained in [results/literal-replay-v2.json](results/literal-replay-v2.json); these were checked by literal sequence slicing independently of the alignment score.
- The forced full-query forward fit is poor (score −142; 178 matches, 74 substitutions and 126 inserted bases across the two sequences). It is not interpreted as a biological mapping.

## Strand and reading-frame limits

The stored A61 CDS is translated in the submitted plus orientation. Its nucleotide correspondence to Gars1 runs in the **opposite orientation**. Target 1456 is the second base of Gars1 codon 472; the aligned interval overlaps Gars1 codons 472–585. This describes the target coding coordinates only: internal gaps and the opposite orientation prevent treating the A61 peptide as the same reading-frame fragment. The complete declared 114-aa A61 peptide is absent as an exact contiguous substring of current Gars1.

The data establish a near-identical antisense-oriented nucleotide correspondence within the current Gars1 CDS. They do **not** establish why the historical submission differs, whether it reflects clone orientation, sequencing or another source issue, or whether the purified granule protein was full-length Gars1, a processed product or another entity. No natural antisense transcript, alternative Gars1 protein, biological loss or functional misattribution is asserted. No genome-wide uniqueness search or examination of original chromatograms was performed. The positive original fractionation and five-residue peptide observations in [PMID:8939962](https://pubmed.ncbi.nlm.nih.gov/8939962/) remain relevant and are not negated by this analysis.

## Reproduction and checks

The [README](README.md) gives four offline commands using Biopython 1.85. All three official input records are included unchanged in [inputs](inputs/); their hashes and record URLs are in [input-manifest.yaml](input-manifest.yaml). The scripts compute the results without expected sequence coordinates or counts embedded in the analysis code. The self-comparison positive control and independent sequence-slice replay are included.

The portable replay reproduces the original computed objects exactly except for relative input-path strings. The historical first fit and its successor that enumerates all four reverse optima remain preserved in the original private analysis; this package contains the governing second fit. No new alignment method, source retrieval, genome-wide search or biological identity claim was added during packaging.
