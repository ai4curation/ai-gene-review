# RMT2 review notes

## 2026-11-06

- Fetched `yeast/RMT2` with `just fetch-gene yeast RMT2 --uniprot-id Q03305` after the first broad symbol lookup timed out at UniProt. The pinned accession maps to `SGD:S000002873`, ordered locus `YDR465C`, and `PTHR32379:SF1`.
- `just deep-research` was not attempted because this worktree does not include `templates/gene_research_go_focused.md`; as in the Ppn1 sparse worktrees, a provider run would fail before research starts. I used the seeded GOA rows, cached direct papers, UniProt, current PTHR32379 PAINT rows, and manual literature searches instead.
- Manual searches for `RMT2 YDR465C Saccharomyces cerevisiae Rpl12 ribosomal protein methyltransferase` and post-2016 Rmt2/Rpl12 methylation papers found no newer direct S. cerevisiae Rmt2 enzymology after the 2016 ribosomal protein methyltransferase study.
- PAINT separates the broad PTHR32379 eukaryotic localization/generic methyltransferase node (`PTN001282244`), the vertebrate GAMT node for guanidinoacetate methyltransferase and creatine biosynthesis (`PTN001285367`), and the fungal Rmt2 catalytic node for `GO:0019702 protein arginine N5-methyltransferase activity` (`PTN001285370`). The official PANTHER family and subfamily labels are both `GUANIDINOACETATE N-METHYLTRANSFERASE`, so gene reviews should cite the exact PTN rather than trusting the label.
