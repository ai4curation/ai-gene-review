# Pgd notes

- 2026-10-09: Initial review of Pgd (P41572, Swiss-Prot), 6-phosphogluconate dehydrogenase.
- UniProt: "Catalyzes the oxidative decarboxylation of 6-phosphogluconate to ribulose 5-phosphate and
  CO(2), with concomitant reduction of NADP to NADPH." (ECO:0000250) [file:DROME/Pgd/Pgd-uniprot.txt]
- Experimental papers (PMID:5972220, PMID:817945) are title-only in the cache; accepted in deference
  to curators. Glucome RNAi screen [PMID:25994086] glucose homeostasis kept as non-core.
- Convention for the NADPH regeneration module: specific oxidative PPP (GO:0009051) replaces generic
  PPP; NADP binding kept non-core (same as G6pd). No NADP+ metabolic row exists for Pgd, so core
  function lists only the oxidative PPP.
- Falcon deep research (Pgd-deep-research-falcon.md): purified fly 6PGD kinetics (Km 81 uM 6PG,
  22.3 uM NADP+); severe Pgd alleles are deleterious mainly through 6-phosphogluconate accumulation;
  oxidative PPP supports lamellocyte responses to parasitoids and astrocytic long-term memory. Not
  used to change annotations (no corresponding GOA rows; sources not cached).
