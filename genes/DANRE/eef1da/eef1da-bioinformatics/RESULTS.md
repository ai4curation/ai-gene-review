# eef1da / eef1db protein and expression comparison

Script: `compare_eef1d.py` (run with
`uv run python genes/DANRE/eef1da/eef1da-bioinformatics/compare_eef1d.py > genes/DANRE/eef1da/eef1da-bioinformatics/output.txt`).
Raw output: `output.txt` (run 2026-09-28). Global alignments: Biopython PairwiseAligner,
BLOSUM62, gap open -10, extend -0.5. All zebrafish entries for each gene, human EEF1D
(P29692) isoforms and features, and spotted gar EEF1D (W5MPR4) are fetched from UniProt
REST. Expression calls come from the Bgee REST API and the ZFIN
`wildtype-expression_fish.txt` download.

## Background used for the design

Human EEF1D is made as a 281-aa isoform (isoform 1, the eEF1B complex subunit with a
leucine zipper and a C-terminal GEF domain) and a 647-aa isoform (isoform 2, eEF1BdeltaL)
that adds a 366-aa N-terminal extension (UniProt P29692 alternative products). The two
accessions under review are long RefSeq-model isoforms: eef1da A0A8M6Z1P2 (463 aa) and
eef1db A0A8M2B7W1 (578 aa). UniProt also holds short isoforms of both genes (eef1da
245-291 aa; eef1db 274-298 aa) and further long models (eef1da 417-441 aa; eef1db 554 aa).

## Protein

- **Whole-protein identity is misleading.** The two reviewed long isoforms are 40.5%
  identical over 582 columns. The two shortest isoforms (eef1da A0A0R4IA30, 245 aa;
  eef1db A0AC58I3M7, 274 aa) are 62.8% identical.
- **The core is conserved.** Projected onto human isoform-2 coordinates, the reviewed pair is
  identical at 187/260 core positions aligned in both (71.9%), at 22/36 in the leucine
  zipper (61.1%) and at **97/109 in the catalytic GEF region (89.0%)**.
- **Each copy vs human:** GEF region eef1da 78.0% (85/109), eef1db 80.7% (88/109), gar
  83.5% (91/109); leucine zipper eef1da 47.2%, eef1db 52.8%, gar 55.6%; whole core about
  65% (eef1da) and 67-68% (eef1db). No copy has lost any part of the GEF region (109/109
  positions aligned in every entry).
- **The N-terminal extension (eEF1BdeltaL-like region).** Long models of both genes align
  to part of the human 366-aa extension (eef1da 169 positions, 36.7% identical; eef1db 259
  positions, 34.7%; gar 290 positions, 44.5%). The region is compositionally biased, so a
  shuffle control was run (20 shuffles of the N-terminal segment, re-aligned):
  - gar W5MPR4: observed 44.5% vs shuffled mean 30.9%, max 36.9%: above background;
  - eef1db A0A8M2B7W1: observed 34.7% vs shuffled mean 27.9%, max 31.8%: modestly above;
  - eef1da A0A8M6Z1P2: observed 36.7% vs shuffled mean 30.9%, max 38.2%: **not
    distinguishable from background**.
  Between the two paralogs, only 28/123 extension positions aligned in both are identical
  (22.8%).

## Expression (Bgee, anatomical entities, all data types)

- Both genes have 29 expressed entities, all shared; neither has a gene-specific entity.
- Scores are high for both in almost every tissue (top entities > 97 for both): both are
  broadly and strongly expressed, as expected for translation factors.
- eef1da scores higher in 22/29 shared entities (median difference 1.5). The largest
  differences favour eef1da in maternal and early stages: cleaving embryo 91.6 vs 64.7,
  mature ovarian follicle 98.2 vs 73.0, early embryo 97.1 vs 74.5, blastula 96.6 vs 76.1;
  and in head kidney (83.3 vs 65.8) and swim bladder (79.6 vs 65.0). eef1db is slightly
  higher in retina, brain, somite, presomitic mesoderm, eye and head (differences 2.5-5.3).
- ZFIN curated rows: one high-throughput in situ entry each (ZDB-PUB-040907-1), whole
  organism, 1-cell to pec-fin stages.

## Interpretation

- Both paralogs keep the conserved eEF1Bdelta core, and in particular the GEF region, at
  high identity to each other and to human and gar. Both are expected to act as the delta
  subunit of eEF1B, a nucleotide-exchange factor for eEF1A. No catalytic-region loss is seen.
- Both genes are predicted (RefSeq models) to make long isoforms with an N-terminal extension,
  as gar does. This conflicts with the published statement that eEF1BdeltaL is restricted
  to birds and mammals (PMID:25686034). It is not proof that zebrafish or gar make a
  functional long isoform: the models are computational and the eef1da extension is not
  distinguishable from a composition-matched background. The extensions of the two
  paralogs have diverged strongly from each other.
- Expression overlaps completely at the level of Bgee anatomical entities. The one
  quantitative pattern is a higher maternal/early-embryo signal for eef1da. This is a
  quantitative bias, not a partition.
