# Primary identity of Myxococcus ImuA

The ImuA assayed in the 2021 DK1622 study is MXAN_3991, encoding
ABF92318.1 / UniProt Q1D5A2. This conclusion uses the primary figure's
gene-labeled sequence, not a patent or the database's automated RecA name.

Figure 1A of [PMID:34190612](https://doi.org/10.1128/AEM.00919-21)
shows an imuA promoter sequence. Its two displayed nucleotide blocks,
concatenated without alignment-gap characters, match a single 58-nt segment
of the 9,139,763-bp DK1622 reference CP000113.1, on the reverse strand at
4,860,557–4,860,614 (one-based inclusive). There are 47 intervening bases
between that segment and the upstream edge of the minus-strand MXAN_3991
CDS, 4,859,637–4,860,509. That CDS encodes ABF92318.1, and its 290-residue
translation is exactly the seeded Q1D5A2 UniProt sequence.

An independent 34-nt imuB promoter block from the same figure was processed
as a control. It also has one genomic match, reverse strand
4,859,566–4,859,599, 36 intervening bases upstream of MXAN_3990. The control
translation correctly does not equal Q1D5A2. Supplementary Table S1 independently
labels MXAN_3990 as ImuB. This control checks the matching procedure and the
interpretation of strand and promoter orientation; it is not a review of ImuB.

The raw genome still names MXAN_3991 a putative RecA protein, and the current
UniProt name/family note is ARBA-derived. Neither label was used as functional
evidence. The primary sequence bridge resolves which locus the authors call
ImuA, while the functional judgments come from their experiments.

The 2024 paper identifies its protein as M. xanthus ImuA and compares it with
the 2021 study. Its 290-residue protein and reported R71/T72 positions agree
with this sequence. The downloaded supplement does not expose a complete
synthetic-construct sequence or accession; that particular construct-to-accession
link is therefore an inference from the named protein, length, residue positions,
and the established 2021 identity, not a second independently verified complete
sequence match. No Myxococcus biochemical claim is transferred to ImuA′.

## Reproducibility checklist

- [x] Generic script takes genome, query file, UniProt record and output path as arguments.
- [x] Query sequences are separately transcribed primary-source data, not embedded conclusions.
- [x] The same procedure was tested on a second gene, imuB.
- [x] Analysis completed; direct output is `identity-results.json`.
- [x] Source URLs, file hashes and access limitations are recorded in `access-receipt.json`.
- [x] Genome/CDS translation was compared against the actual seeded UniProt sequence.

See `README.md` and `justfile` for reproduction. This is identity verification,
not a predictor of catalytic activity or whole-module completeness.
