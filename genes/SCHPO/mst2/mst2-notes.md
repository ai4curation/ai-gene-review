# mst2 review notes

## 2026-10-11

- Created the `SCHPO/mst2` review for the fungal MYST-family PAINT project.
- `PANTHER:PTN004172926` is a broad eukaryotic MYST ancestor. Its inherited
  chromatin, nucleus, histone acetyltransferase, chromatin-binding, transcription
  coregulator, and RNA polymerase II transcription rows are generic enough for
  Mst2 and are not Sas3/KAT7-specific over-propagations.
- `PANTHER:PTN008308138` is the fungal NuA3a complex node seeded by
  *S. cerevisiae* `SAS3`. The seed is sound for budding yeast, but the term is
  too exact for fission yeast: the 2012 Mst2-complex purification shows the
  fission complex differs from NuA3 and contains Mst2, Eaf6, Nto1, Pdp3, Ptf1,
  Ptf2, and Tfg3 rather than the budding-yeast NuA3a assembly.
- The direct heterochromatin literature consistently puts wild-type Mst2 on the
  anti-silencing side. The `GO:0031507 heterochromatin formation` rows were
  therefore changed to `GO:0120262 negative regulation of heterochromatin
  organization`, while the curated `GO:0033696 heterochromatin boundary
  formation` rows were retained.
- Literature search added two useful post-2024 papers. PMID:41786738 updates
  the mechanism by connecting Mst2 H3K14 acetylation to the H3K14ub-H3K9me3
  feedback loop. PMID:39565189 was also inspected; it gives systems-level
  context for Mst2C/NuA3 modules in heterochromatin regulation but did not add a
  mst2-specific annotation beyond the direct Wang/Jia/Grewal papers.
- PR review found three inherited transcription rows whose `supporting_text`
  cited only a generic PMID:22184112 background sentence. Those rows now cite
  the direct telomeric anti-silencing and targeted-Mst2 HAT heterochromatin
  evidence instead. PMID:22184112 also establishes that loss of Mst2/Gcn5-dependent
  H3K14ac impairs DNA-damage checkpoint activation, but `rad3` and `chk1` are
  the local checkpoint-signaling comparators; a suggested question now asks
  whether any non-core checkpoint term belongs on the chromatin-accessibility
  HATs or Mst2-complex subunits.
