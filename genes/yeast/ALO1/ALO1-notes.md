# ALO1 review notes

## 2026-10-10 fungal PAINT re-review

### Setup and literature search

- Ran `UV_FROZEN=1 just fetch-gene yeast ALO1`, which seeded 27 current GOA
  rows for the budding-yeast ALO1 protein.
- Tried `UV_FROZEN=1 just deep-research-falcon yeast ALO1 --fallback
  perplexity-lite`; the provider stack was unavailable in this workspace, so I
  used the cached primary publications, UniProt, GOA, the local PANTHER
  PTHR43762 PAINT cache, and manual web/PubMed searches instead.
- Searched for newer ALO1 literature. The important recent paper was already in
  GOA and was cached as `PMID:39775849`: Chelius et al. 2025, which reports that
  Alo1 is a robust Myo2 cargo-binding-domain hit, is located in the mitochondrial
  outer membrane, and that alo1 mutants have mitochondrial morphology and
  inheritance defects.
- Searches did not reveal a newer direct S. cerevisiae ALO1 functional paper
  beyond PMID:39775849.

### Evidence summary

- The primary enzymology paper purified the D-arabinono-1,4-lactone oxidase from
  the mitochondrial fraction of S. cerevisiae and identified YML086C as `ALO1`
  from peptide sequence; its abstract states that alo1 mutants lacked both
  D-erythroascorbate and D-arabinono-1,4-lactone oxidase activity, and that ALO1
  overexpression increased both [PMID:10094636].
- The same paper showed a physiological oxidative-stress phenotype: alo1 mutants
  were more sensitive to oxidative stress, whereas ALO1 overexpression made cells
  more resistant [PMID:10094636].
- Several HDA rows are from large-scale mitochondrial or mitochondrial
  outer-membrane proteomics papers. The cached abstracts for PMID:14576278,
  PMID:16407407, PMID:16689936, PMID:16823961, and PMID:24769239 describe
  purified-mitochondria, purified-outer-membrane, PROMITO, and quantitative
  mitochondrial proteomics workflows, but they do not expose the ALO1-specific
  supplemental rows in the local cache. Retain these rows as curator-extracted
  high-throughput localization evidence because SGD curators had access to the
  relevant full text or supplement.
- Chelius et al. 2025 performed a protein-fragment complementation screen with
  the Myo2 cargo-binding domain and found Alo1 as a robust hit; the abstract
  explicitly links Alo1 to Myo2 recruitment to mitochondria and to mitochondrial
  inheritance defects in alo1 mutants [PMID:39775849]. This supports keeping the
  new `myosin V binding`, `mitochondrion inheritance`, and cytoplasmic-side
  mitochondrial outer-membrane rows, but the cached abstract only exposes
  mitochondrial outer-membrane localization, not the exact cytoplasmic-side assay.
  These are contextual functions rather than a replacement for the core oxidase
  model.
- UniProt records that purified Alo1 can oxidize L-gulono-1,4-lactone and
  L-galactono-1,4-lactone in addition to D-arabinono-1,4-lactone. This makes the
  InterPro-derived `GO:0016899` row a valid non-core parent for the in vitro
  substrate range; the physiological core remains `GO:0003885
  D-arabinono-1,4-lactone oxidase activity` in D-erythroascorbate biosynthesis.

### PAINT / IBA review

- PTHR43762:SF1 contains fungal D-arabinono-1,4-lactone oxidases including
  S. cerevisiae ALO1, Candida albicans ALO1, Neurospora crassa alo-1, and
  Schizosaccharomyces pombe alo1.
- `PANTHER:PTN000356435` carries the exact `GO:0003885
  D-arabinono-1,4-lactone oxidase activity` IBD for the fungal SF1 branch,
  seeded by CGD:CAL0000174500 and SGD:S000004551. The S. cerevisiae seed is
  target-local experimental evidence, not circular evidence.
- `PANTHER:PTN001015900` carries a fungal `GO:0005739 mitochondrion` IBD, also
  seeded by CGD:CAL0000174500 and SGD:S000004551. This is broad but valid for
  budding-yeast ALO1 and is refined by direct outer-membrane rows.
- `PANTHER:PTN001015900` also has an IRD loss for `GO:0019853 L-ascorbic acid
  biosynthetic process`, pruning the broader eukaryotic L-ascorbate assignment
  from fungi. Do not add an ascorbate-process `NEW` row: budding yeast ALO1 is in
  D-erythroascorbate biosynthesis, and that process is already in GOA as
  `GO:0070485`.
- Ask PAINT whether to retain the fungal PTN001015900 loss of ascorbic acid
  biosynthesis while keeping D-erythroascorbate biosynthesis for the ALO1
  subfamily.

### Main curation decisions

- Accepted the exact `GO:0003885` rows from IBA, IDA, IEA, and YeastPathways RCA.
- Accepted D-erythroascorbate biosynthesis as the core biological process.
- Kept broad mitochondrial and membrane rows as true location parents where they
  add secondary support, while accepting the exact mitochondrial outer membrane
  and cytoplasmic-side mitochondrial outer membrane rows.
- Removed the YeastPathways-derived `GO:0005829 cytosol` row. The pathway
  conversion probably modeled the soluble side of the reaction, but Alo1 is a
  membrane-embedded mitochondrial outer-membrane protein.
- Modified the very broad InterPro oxidoreductase parent rows to the exact
  D-arabinono-1,4-lactone oxidase term.
- Kept the Myo2-binding and mitochondrion-inheritance rows as non-core. The 2025
  evidence supports them, but Alo1's defining molecular function remains
  FAD-dependent D-arabinono-1,4-lactone oxidation.
- Did not add any new annotations; current GOA already covers the enzymatic
  activity, D-erythroascorbate biosynthesis, FAD cofactor binding,
  oxidative-stress physiology, mitochondrial/outer-membrane localization, and the
  2025 Myo2-linked mitochondrial-inheritance role.
