# Mtap notes

- 2026-10-09: Initial review of Mtap (Q9V813, Swiss-Prot), 5'-methylthioadenosine phosphorylase.
- UniProt (HAMAP MF_03155): "Responsible for the first step in the methionine salvage pathway after MTA
  has been generated from S-adenosylmethionine." Homotrimer. Embryonic fat body and visceral mesoderm
  expression; no auditory phenotype of mutants (PMID:17534888, cited in UniProt, not cached).
- Fly enzyme kinetics: Shugart et al. [PMID:6786932] (title only).
- Module-wide convention (methionine salvage): GO:0033353 "L-methionine cycle" is defined as the SAM
  cycle; GO made it the replacement for obsolete GO:0019509 "L-methionine salvage from
  methylthioadenosine", so salvage enzymes inherited it. MODIFY to GO:0071267 L-methionine salvage
  for all five enzymes; cytoplasm -> cytosol (IC present); nucleus kept non-core.
- identical protein binding IPI (Y2H, PMID:16603075) kept non-core: consistent with homotrimer.
