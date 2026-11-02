# Mad (P42003) review notes

## Session 1 (initial review)

- Fetched with `just fetch-gene DROME Mad`; UniProt P42003 confirmed; 136 GOA rows; 57 PMIDs cached plus
  PMID:22879948 (requested key paper; full text).
- No deep-research provider available; literature synthesis written by hand in
  `Mad-deep-research-manual.md`.
- PMID:22879948 (fussel) is mainly about Fuss; relevant to Mad only in that Fuss binds Medea, not Mad
  ["However, we could not verify an interaction of Fuss with Mad on an in vitro level (data not shown)."]
  and does not block pMad nuclear translocation ["(F–G”) Fuss does not inhibit the nuclear translocation
  of pMad."]. No GOA row cites it; recorded as a MEDIUM-relevance reference.

### Decisions

- Core MF: DNA-binding transcription factor activity, Pol II-specific (activator and, with Shn, repressor
  at silencer elements); co-SMAD binding; Pol II cis-regulatory region binding.
- Core BP: BMP signaling pathway, SMAD protein signal transduction, positive/negative regulation of
  transcription by Pol II.
- Core CC: heteromeric SMAD complex, Pol II transcription repressor complex (Mad/Med/Shn), nucleus,
  cytosol.
- GO:0003713 transcription coactivator activity (PMID:11071761) MODIFY to GO:0001228: coactivators by
  definition do not bind DNA, Mad binds DNA directly [PMID:9230443].
- Bare protein binding: Smurf rows -> ubiquitin protein ligase binding (GO:0031625); Yorkie row ->
  transcription coactivator binding (GO:0001223); dTGIF row -> GO:0061629; Lis1 and eIF4A rows REMOVE
  (Mad is the substrate/client, no informative MF of Mad).
- Developmental process rows (wing, eye, leg, stem cells, NMJ, etc.) kept as non-core: they are outcomes
  of BMP signalling in which Mad is the transcriptional effector.
- Generic ARBA/InterPro IEA rows refined to specific terms the gene already carries, following the
  Medea review (`genes/DROME/Med`).
- No NEW terms proposed: no candidate passes the NEW bar (all candidate processes are BMP-pathway
  outcomes already captured).
