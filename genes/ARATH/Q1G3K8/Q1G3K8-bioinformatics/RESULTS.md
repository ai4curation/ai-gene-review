# RIC7 sequence identity and experimental primer mapping

Analysis date: 2026-09-07. [Reproduction instructions and input provenance](README.md).
Computed output: [results.json](results.json). Coordinates below are 1-based,
inclusive, on the supplied transcript sequence.

## Finding

The published RIC7 primer pairs from Wu et al. (2001), Hong et al.
(online 2015/issue 2016), and Zhu et al. (2021) map to the AT4G28556 transcript NM_001036663.2,
which encodes the CRIB protein Q1G3K8. None of the six primers has an exact
3′ match of 14 or more bases in the AT4G28560 transcript NM_118998.1.
The comparison strongly assigns these experimental targets to the CRIB locus.
It is a comparison of the two candidate loci, not a genome-wide specificity test.

## Sequence identity

| Sequence | Comparator | Result |
|---|---|---|
| F4JLB7 | NP_194585.1 | Exact equality, 450 aa |
| F4JLB7 | Translation of NC_003075.7 reverse interval 14116015–14117367 | Exact equality, 450 aa |
| Q1G3K8 | NP_001031740.1 | Exact equality, 216 aa |
| Q1G3K8 | DQ487576.1 annotated CDS translation | Exact equality, 216 aa |

## Primer mapping

| Primer | Matched bases | Removed 5′ bases | NM_001036663.2 match |
|---|---|---|---|
| Wu2001 RIC7 forward | 21 | 7 | 660–680 |
| Wu2001 RIC7 reverse | 23 | 0 | 1281–1303, reverse complement |
| Hong2016 RIC7 forward | 29 | 0 | 705–733 |
| Hong2016 RIC7 reverse | 29 | 0 | 1256–1284, reverse complement |
| Zhu2021 RIC7 forward | 22 | 0 | 804–825 |
| Zhu2021 RIC7 reverse | 22 | 0 | 917–938, reverse complement |

Primer sequences and source URLs are in [data/primers.tsv](data/primers.tsv):
[Wu et al., Table 4, DOI:10.1105/tpc.010218](https://doi.org/10.1105/tpc.010218)
and [Hong et al., RT-PCR methods, DOI:10.1111/nph.13625](https://doi.org/10.1111/nph.13625).
Forward and reverse matches have the expected inward-facing orientation. Each
primer has one longest-suffix hit on this transcript. The Wu forward primer's
removed 5′ sequence contains a BamHI cloning site.

The four Wu/Hong primers also match the cDNA DQ487576.1: forward/reverse positions
10–30 and 631–651 for Wu, and 55–83 and 606–634 for Hong. The Wu reverse
primer matches 21 bases at the cDNA end, requiring two 5′ bases to be discarded;
its entire 23 bases match the longer RefSeq transcript. No matching hits were
found in NM_118998.1 under the same rules.

The Wu forward primer matches near, rather than exactly at, the start of the
current Q1G3K8 CDS. These results identify the locus but do not establish that
the original fusion expressed exactly the current 216-residue protein. Hong's
primers are transcript-assay primers; they do not independently sequence every
expression construct, promoter fragment, or mutant insertion.

## Verification checklist

- [x] The analysis code reads sequences, primer sequences, directions and comparison pairs from input files; it contains no hardcoded biological conclusions or expected matches.
- [x] The same matching code was run on a separate biological input, the AT4G28560 transcript, as well as the AT4G28556 transcript and DQ487576 cDNA.
- [x] Synthetic forward, reverse-complement, 5′-tail, multiple-occurrence and no-hit checks passed.
- [x] All comparisons completed; direct machine-readable results are retained.
- [x] Input sources, sequence versions, methods, dependency version and limitations are documented.
Original physical clones, promoter fragments and insertion sites were not resequenced or fully reconstructed; these are outside the scope of the sequence comparison.

The Zhu et al. (2021) qRT-PCR primers match DQ487576.1 at 154–175
and 267–288 respectively (all 22 bases each), with no hits in NM_118998.1.
The methods were read in cached full text
[PMID:33586611](https://doi.org/10.1080/15592324.2021.1876379).
