# gmhA curation notes

- Q88N89 carries the exact phosphoheptose-isomerase reaction, EC 5.3.1.28, and
  GmhA-specific HAMAP/InterPro signatures
  [file:PSEPK/gmhA/gmhA-uniprot.txt, "Catalyzes the isomerization of
  sedoheptulose 7-phosphate"].
- The same record maps Q88N89 to `PTHR30390:SF6` with the label "DNAA
  INITIATOR-ASSOCIATING PROTEIN DIAA", but this conflicts with the exact
  catalytic, pathway, and GmhA-family evidence
  [file:PSEPK/gmhA/gmhA-uniprot.txt, "PTHR30390:SF6; DNAA
  INITIATOR-ASSOCIATING PROTEIN DIAA"]. The module therefore uses the
  GmhA-specific InterPro selector rather than transferring a DiaA role.
- The broad carbohydrate-binding rows are not used as core functions; the
  exact GO:0008968 reaction and GO:2001061 product process carry the biological
  assertions.
