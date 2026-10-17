# STX3 (donkey, A0A9L0J901) notes

## Sequence and record

- Unreviewed TrEMBL entry, 289 aa, "Syntaxin-3"; PANTHER PTHR19957:SF34 (SYNTAXIN-3);
  Syntaxin N-terminal Habc region, t-SNARE (SNARE motif) domain 191..253 and a C-terminal
  transmembrane segment 264..288 (tail-anchored, type IV)
  [file:EQUAS/STX3/STX3-uniprot.txt "Single-pass type IV membrane protein"].
- 15 GOA rows, all IEA (TreeGrafter, InterPro2GO, ARBA and GO_REF:0000120 combined).
- Donkey vs human Q13277 (isoform A, 289 aa): 92.39% identity over the full length, no
  unpaired segments [file:EQUAS/STX3/STX3-bioinformatics/RESULTS.md "with 92.39% identity across 289 paired residues"].
  The donkey sequence corresponds to the canonical, membrane-anchored isoform A, not the
  retina-specific isoform B or the nuclear isoform 3.

## Ortholog biology

- Human STX3: apical plasma-membrane t-SNARE mediating fusion of apical vesicles; loss causes
  microvillus inclusion disease and retinal dystrophy
  [file:EQUAS/STX3/STX3-bioinformatics/human_Q13277-uniprot.txt "Apical receptor involved in membrane fusion of apical vesicles"].
- Partners SNAP25 and VAMP2 (by similarity) [same file, "Interacts with SNAP25 (By similarity)"].
- Mouse Stx3 (Q64704) has SynGO IDA annotations to postsynapse and to exocytic insertion of
  neurotransmitter receptor to postsynaptic membrane, and MGI IDA to dendrite
  [file:EQUAS/STX3/STX3-bioinformatics/mouse_Q64704-uniprot.txt "C:postsynapse; IDA:SynGO."].
  The underlying SynGO paper (PMID:23395379) is not cached, so it is cited only through the
  mouse UniProt cross-reference.

## Decisions

- Core: helical-bundle zippering fusogenic activity (t-SNARE), SNARE binding, SNARE complex,
  plasma membrane, vesicle fusion, exocytosis.
- Broad terms (membrane, vesicle-mediated transport, membrane fusion): TOO_GENERAL.
- Cytoplasm (ARBA): MARK_AS_OVER_ANNOTATED - an integral membrane protein, not a soluble
  cytoplasmic protein.
- Postsynaptic/dendrite/cell-projection terms and intracellular protein transport: non-core.

## ProtNLM2 (donkey40 snapshot)

- GO:0016020 membrane -> LSP (GOA has plasma membrane).
- GO:0016192 vesicle-mediated transport -> LSP (GOA has vesicle fusion and exocytosis).
- Non-GO: subcellular_location "Membrane" (not scored).
