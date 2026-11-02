# PPR10 notes (MAIZE, B8Y6I0)

- 2026-10-28: fetched with `just fetch-gene MAIZE PPR10`; accession B8Y6I0 confirmed (Swiss-Prot, GeneID 100302579). 9 GOA rows.
- Cached PMIDs: 19424177 and 24162847 (abstract-only), 21173259, 22156165, 25609698, 25231995, 30125002 (full text).
- Literature synthesis in PPR10-deep-research-manual.md (no deep-research API available).

## Key conclusions
- Core MF: sequence-specific single-stranded RNA binding to atpH 5'-UTR and psaJ 3'-UTR elements
  [PMID:21173259 "the minimal PPR10-binding site spans 17 nt"]. The IBA mRNA binding row is refined to
  GO:1990825 sequence-specific mRNA binding (is_a mRNA binding, checked with OAK).
- Core BP: mRNA stabilization (barrier to 5'->3' and 3'->5' exonucleases) [PMID:19424177 "PPR10 serves as a barrier to RNA decay from either the 5' or 3' direction"].
- Second BP: positive regulation of translation of atpH via RBS remodelling [PMID:21173259]. PPR10 itself does
  the work (it sequesters the RNA segment that would pair with the Shine-Dalgarno-like element), so this passes
  the NEW bar; it is not merely a mutant phenotype.
- regulation of gene expression and regulation of RNA metabolic process (ARBA IEA) are ancestors of mRNA
  stabilization (checked with OAK `ancestors -p i,p GO:0048255`), so MODIFY to GO:0048255.
- chloroplast (ARBA IEA): plastids are not covered by the organelle policy; correct but general; MODIFY to chloroplast stroma.
- Homodimer (IPI, crystal): seen in crystals but RNA-bound PPR10 is monomeric in solution [PMID:25609698]; keep as non-core.
- Considered but not added: GO:0010239 chloroplast mRNA processing. PPR10 defines processed termini by
  blocking exonucleases, but the nucleolytic work is done by RNases; left as a suggested question.
