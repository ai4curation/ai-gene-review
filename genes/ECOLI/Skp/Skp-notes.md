# Skp review notes

## 2026-08-30 comprehensive annotation review

- Refreshed the gene inputs with `just fetch-gene ECOLI Skp`, backfilled GOA
  qualifiers through the public wrapper, and fetched current PAINT provenance with
  `just fetch-panther-paint PTHR35089 --extra-uniprot P0AEU7`.
- GOA contains 36 physical rows that collapse to 34 qualifier-aware review
  signatures. `just validate-goa ECOLI Skp` confirms all 34 are represented exactly.
- Current PTHR35089 PAINT places both GO:0006457 and GO:0050821 at
  PTN002170712, seeded by UniProtKB:P0AEU7. Skp's appearance in its own IBA
  WITH/FROM is expected descendant evidence, not circularity.
- Skp is a periplasmic ATP-independent carrier-holdase for unfolded beta-barrel
  outer-membrane proteins. It maintains clients in soluble, unfolded states during
  transit toward outer-membrane assembly [PMID:10455120 "Skp is a molecular
  chaperone involved in generating and maintaining the solubility of early folding
  intermediates of outer membrane proteins in the periplasmic space of Gram-negative
  bacteria"; PMID:19181847 "while bound to Skp, the beta-barrel domain of OmpA is
  maintained in an unfolded state"].
- The final action distribution is 18 ACCEPT, 12 MODIFY, 3 KEEP_AS_NON_CORE,
  and 1 UNDECIDED. Protein-folding process rows are accepted because they assert
  Skp's experimentally supported participation in the pathway rather than foldase
  catalysis; generic protein-maturation rows are modified to GO:0043165. Obsolete
  GO:0051082 and substrate-specific GO:0005515 rows are modified to GO:0140309.
- Homotrimerization is valid but retained as non-core: the three subunits form the
  functional cavity [PMID:15304217 "The structure of the Skp trimer resembles a
  jellyfish with alpha-helical tentacles protruding from a beta barrel body defining
  a central cavity"].
- PMID:17908933 and PMID:16858726 are abstract-only. The broad outer-membrane
  assembly term supported by PMID:17908933 is accepted with an explicit caveat that
  the abstract foregrounds direct SurA-YaeT interaction; the curator had access to
  fuller evidence. The cached PMID:16858726 abstract does not expose the Skp-specific
  cytosol row, so that location annotation remains UNDECIDED rather than removed.
- Only PMID:23796519 has full cached text among the 14 PMID records. The other 13
  references are marked `full_text_unavailable: true`; reference-review judgments
  distinguish direct abstract support from row-level evidence that could not be checked.
- The project source records that "GO:0051082 is now formally obsolete" and assigns
  Skp to the carrier-holdase replacement class [file:projects/UNFOLDED_PROTEIN_BINDING.md].
- The Falcon deep-research synthesis independently describes Skp as an
  "ATP-independent periplasmic holdase chaperone" [file:ECOLI/Skp/Skp-deep-research-falcon.md].
