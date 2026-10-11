# Sqor notes

- 2026-10-09: Initial review of Sqor (Q9VZF6), sulfide:quinone oxidoreductase.
- No functional fly study. Martelli et al. 2024 [PMID:38416643]: "Genes dysregulated in shop larvae on
  100% Cys diet (Eip55E [CTH], Sam-s [MatI-III], and Sqor [SQOR]) were largely normalized by the
  Cys-free diet".
- GO:0070224 (bacterial-type, sulfane product) MODIFY -> GO:0106436 glutathione-dependent SQOR activity
  (UniProt RHEA:55156; siblings in GO). Mitochondrion -> mitochondrial inner membrane (ubiquinone
  reduction requires the inner membrane quinone pool). FAD binding non-core.
- Falcon deep research (Sqor-deep-research-falcon.md, arrived after initial commit): human SQOR is
  anchored in the inner mitochondrial membrane with its catalytic face toward the matrix (supports the
  inner-membrane MODIFY); GSH is probably the physiological acceptor and sulfite the more efficient one
  in vitro (supports GO:0106436). Possible hydrogen selenide oxidation and ferroptosis-suppression
  role in mammals; untested in flies. No annotation changes.
