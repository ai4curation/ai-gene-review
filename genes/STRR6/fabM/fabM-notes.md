# fabM (Streptococcus pneumoniae R6, Q8DR19) curation notes

## 2026-11-13

- FabM is a crotonase-fold trans-2/cis-3-decenoyl-ACP isomerase with no
  dehydratase activity
  [PMID:12237320 "carries out the isomerization of trans-2-decenoyl-ACP to cis-3-decenoyl-ACP, but is not capable of catalyzing the dehydration of beta-hydroxy intermediates"],
  unrelated to FabA
  [PMID:12237320 "This tetrameric enzyme, designated FabM, has no similarity to FabA, but rather is a member of the hydratase/isomerase superfamily."].
  The branch point therefore follows trans-2-decenoyl-ACP formation.
- The IBA to fatty acid beta-oxidation (PTN000941828, seeded by mammalian
  ECHS1 orthologs) is removed. The PTHR42964 family review finds the node
  outside the current family tree.
- The UniPathway fatty acid biosynthesis row is refined to GO:0006636.
- PANTHER PTHR42964:SF1 mixes FabM with hydroxycinnamoyl-CoA hydratase-lyases
  and polyketide dehydratases, so the module grounds the FabM route on the
  NCBIfam model NF050134 (trans-2-decenoyl-ACP isomerase) from this entry's
  own UniProt record.
