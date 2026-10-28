# trpl review notes

- fetch-gene by symbol timed out (UniProt gene_exact search); re-ran with `--uniprot-id P48994`, which is the expected accession (FlyBase FBgn0005614, GeneID 36003).
- No deep-research provider; see `trpl-deep-research-manual.md`.
- Key decisions:
  - Core MF: monoatomic cation channel activity (non-selective, Ca2+-permeable); calcium channel activity also accepted.
  - Store-operated calcium channel activity (IBA, NAS): over-annotated; TRPL alone is constitutively active [PMID:9215637 "In vitro studies indicate that TRP is a SOC, but that the related retinal protein, TRPL, is constitutively active."]. The axonal SOC data of PMID:22952921 come only from trpl;trp double mutants.
  - IP3 binding (IBA): over-annotated; no direct binding shown.
  - TRP-TRPL heterodimerization (IPI): over-annotated given PMID:23687378 in vivo homomultimer data.
  - Bare protein binding rows removed per policy.
  - Hearing (IMP, PMID:22939627): UNDECIDED, abstract only.
  - NEW: detection of chemical stimulus involved in sensory perception of taste (PMID:24013593; TRPL is itself activated by camphor in S2 cells and confers camphor responses on misexpression, so it passes the participation test). NEW: axon (PMID:22952921 immunostaining). Did not add exocytosis/neurotransmitter release process terms: evidence is double-mutant necessity only.
