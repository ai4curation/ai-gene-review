# EAF3 curation notes

## 2026-11-06

- Fetched `CANGA/EAF3` from GOA/UniProt. The seed contains 22 rows covering
  broad MRG-domain IEAs, EnsemblFungi transfers from budding-yeast EAF3, UniProt
  combined-IEA calls to NuA4 and Rpd3S complex membership, ARBA parent-complex
  inferences, and a CGD molecular-function ND row.
- Searched for newer direct C. glabrata/Nakaseomyces EAF3 literature with
  `"Candida glabrata" EAF3`, `"CAGL0K02321g"`, `"Q6FN68" EAF3`, and
  `"Nakaseomyces glabratus" EAF3 Rpd3S NuA4`. No newer paper describing a
  C. glabrata or N. glabratus EAF3-specific experiment was found.
- C. glabrata Q6FN68 is in the same PANTHER `PTHR10880:SF15` branch as
  budding-yeast EAF3, fission-yeast alp13, and C. albicans EAF3, so the
  EnsemblFungi transfers from SGD EAF3 and the NuA4/Rpd3S combined IEAs are
  biologically plausible.
- The current PAINT cache has a clean fungal `PTN000853816` IBD for
  `GO:0032221 Rpd3S complex`, seeded by PomBase alp13 and SGD EAF3. This is
  appropriate for C. glabrata EAF3; the short donor list is not weak evidence.
- `PTN000093963`, the broad MRG-family root, places `GO:0035267 NuA4 histone
  acetyltransferase complex` and `GO:0006357 regulation of transcription by RNA
  polymerase II` at a node compatible with the fungal branch. The plant-seeded
  `PTN008955946` `GO:0140003 histone H3K36me3 reader activity` placement is not
  the basis for the C. glabrata H3K36me3 reader inference; the local GOA row is
  an EnsemblFungi transfer from experimentally characterized S. cerevisiae EAF3.
- The `GO:0043487 regulation of RNA stability` row looks suspect on the source
  side because the cached PMID:31694990 abstract describes rDNA stability, not
  RNA stability. Because the source is an SGD IMP annotation and the local cache
  is abstract-only, the row is left `UNDECIDED`.
