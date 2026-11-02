# Cxcr3 (mouse, O88410): does the mouse locus encode a CXCR3-B counterpart?

Script: `cxcr3b_exon_search.py` (run with `uv run --script cxcr3b_exon_search.py`; dependencies declared inline).
Raw output: `results-cxcr3b.json`. Run on 2026-10-20 against the Ensembl REST API
(current release at that date).

## Question

Human CXCR3 has a splice isoform, CXCR3-B (P49682-2), in which the first four
residues of CXCR3-A (MVLE) are replaced by a 51-residue N-terminal extension
(UniProt VSP_015684). Several human GO annotations were made on CXCR3-B
(negative regulation of endothelial cell proliferation, negative regulation of
angiogenesis, adenylate cyclase-activating GPCR signalling, positive regulation of
execution phase of apoptosis, positive regulation of transcription by RNA
polymerase II). These reach mouse Cxcr3 by orthology transfer. The question is
whether the mouse genome can encode a CXCR3-B-like protein at all.

## Method

The 51-residue CXCR3-B replacement peptide was read from the human UniProt file and
aligned locally (BLOSUM62, gap open -11, extend -1) against six-frame translations
of the human CXCR3 and mouse Cxcr3 gene regions (gene span plus 5 kb each side, in
gene orientation). Scores were calibrated against 200 shuffled copies of the peptide
aligned to the same region.

## Results

| | Human CXCR3 (positive control) | Mouse Cxcr3 |
|---|---|---|
| Ensembl protein-coding transcripts | 3 (translations of 415, 368, 368 aa) | 1 (367 aa) |
| Best local score of the CXCR3-B peptide | 262 | 35 |
| Aligned length / identities | 51 / 51 | 10 / 7 |
| Shuffled-peptide mean (SD), max | 41.5 (4.6), 59 | 39.7 (4.1), 56 |
| z-score vs shuffled | 48.4 | -1.2 |

- Human: the full 51-residue peptide is found with 100% identity, in frame and
  running straight into the shared CXCR3 sequence (`...PFPPSQ` then `VSDHQVLND`).
  The 415-aa Ensembl transcript ENST00000373691 is the CXCR3-B model.
- Mouse: the best hit covers only the first 10 residues (`MELRKYGPGR` vs
  `MELRRCGPRR`), scores below the shuffled-peptide mean, and the mouse reading frame
  that carries it reaches a stop codon after 20 codons
  (`MELRRCGPRRERVSSGSGYC*`). No mouse frame encodes a counterpart of the
  extension, and Ensembl annotates only one mouse Cxcr3 transcript (the
  CXCR3-A-like 367-aa protein; the UniProt entry O88410 also lists no alternative
  products).
- Canonical mouse O88410 and human P49682 share 318 identical positions in a global
  alignment (86.4% over the human length), consistent with the 86% identity reported
  at cloning.

## Interpretation

The upstream ATG used by human CXCR3-B appears to be conserved positionally in
mouse, but the downstream coding sequence is not, and the mouse frame is
interrupted by a stop codon. The mouse locus therefore cannot produce a
CXCR3-B-like isoform from this region. Human annotations that were made
specifically on CXCR3-B should not be transferred to mouse Cxcr3 on the basis of
gene-level orthology. This analysis does not rule out other mouse transcripts
or mechanisms that produce angiostatic signalling through mouse Cxcr3. It only
shows that the human isoform-B coding sequence has no mouse counterpart.

Limitations: this is a sequence search of one genomic window, not a transcriptomic
analysis. A mouse transcript could in principle use a different, unrelated exon.
Such a transcript is not annotated in Ensembl, and no isoform is listed in UniProt.
