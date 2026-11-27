# RYR3 notes

## 2026-11-26 Codex review

Perplexity deep research was unavailable for this batch; see the RYR1 notes for
the exact failure mode. This review uses the fetched UniProt/GOA data, PAINT
node rows and cached primary literature.

RYR3 is a third ryanodine-receptor paralog that forms homotetrameric
calcium-release channels in sarcoplasmic/endoplasmic-reticulum membranes.
Compared with RYR1 and RYR2, human RYR3 has a smaller GOA surface and fewer
direct human rows; its kept core annotations are therefore deliberately focused
on the conserved ryanodine-sensitive Ca2+-release channel activity and SR/ER
membrane location [file:human/RYR3/RYR3-uniprot.txt].

Main curation decisions:

- Keep the conserved PAINT/InterPro-supported channel activity and
  sarcoplasmic-reticulum membrane rows, because RYR3 retains the same large
  calcium-release channel architecture as RYR1 and RYR2.
- Treat generic ion-channel, intracellularly gated calcium-channel and
  ion-transport rows as less informative than the ryanodine-sensitive
  Ca2+-release channel annotations.
- Keep caffeine, calcium, ATP and magnesium response rows only as non-core
  activity-regulation contexts.
- Mark sarcolemma, Z-disc and junctional-membrane-complex propagation as
  over-annotated for human RYR3 unless a source directly establishes that
  subcellular site for this paralog.
