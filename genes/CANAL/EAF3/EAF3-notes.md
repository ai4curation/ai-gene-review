# EAF3 curation notes

## 2026-11-06

- Fetched `CANAL/EAF3` from UniProt/GOA. The seed contains 11 rows covering
  broad MRG-domain IEAs, a CGD NuA4 IDA row, an IC from NuA4 membership to
  `contributes_to` histone H4 acetyltransferase activity, the fungal Rpd3S IBA
  from `PTN000853816`, and the three broad-root MRG-family IBAs from
  `PTN000093963`.
- Checked newer literature for Candida Eaf3 and the Rpd3/Rpd31/Rco1 branch. No
  newer Candida EAF3-specific experiment superseded the 2008 NuA4 curation
  [PMID:18685084, "Based on the Candida Genome Database, orthologues of all but
  one of the subunits of the S. cerevisiae NuA4 complex exist in C. albicans"].
  The local cache drops the rows of Table 4, so I checked the PMC rendering;
  the table lists `EAF3`/`orf19.2660` as the Candida ortholog of budding-yeast
  `EAF3`.
- The 2016 Rpd3/Rpd31 paper is relevant but not enough to remove the Rpd3S PAINT
  inference. Xie et al. did not recover Eaf3/Rco1 in their initial Rpd3/Rpd31
  purifications, then used targeted co-IP to show that Rco1 interacts with
  Rpd31 rather than Rpd3 [PMID:27935838, "Rpd31 but not Rpd3 represents the HDAC
  component of the CaRpd31S regulatory complex"]. This supports a divergent
  Candida Rpd31S-like complex, not a demonstrated Eaf3 loss from the complex.
- `PTN000853816` is a fungal PAINT node for `GO:0032221 Rpd3S complex` seeded by
  direct PomBase alp13 and SGD EAF3 evidence. The donor list is short but
  biologically appropriate, and Candida Eaf3 belongs to the same fungal
  `PTHR10880:SF15` Eaf3/Alp13 branch.
- `PTN000093963`, the eukaryotic MRG root, needs term-specific handling.
  `GO:0035267 NuA4 histone acetyltransferase complex` and `GO:0006357
  regulation of transcription by RNA polymerase II` remain appropriate for
  Candida Eaf3. `GO:1990841 promoter-specific chromatin binding` is
  over-propagated from only Arabidopsis MRG seeds and should not be transferred
  to fungal Eaf3 proteins.
- I did not add `GO:0140003 histone H3K36me3 reader activity` for this Candida
  review. The term is biologically plausible by analogy to budding and fission
  yeast, but the current Candida seed set lacks direct evidence that C. albicans
  Eaf3 recognizes H3K36-methylated chromatin.
