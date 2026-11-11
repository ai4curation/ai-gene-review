# Sdhaf2 (Q8C6I2, mouse canonical isoform 1) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Folder created with `just fetch-gene mouse Q8C6I2 --alias Sdhaf2__Q8C6I2`. The sibling folder
`genes/mouse/Sdhaf2` is keyed to the alternative product A0A494B8X4. This folder holds the
reviewed Swiss-Prot canonical product. No ProtNLM2 files or prediction-evidence folders were
opened.

### Deep research

`just deep-research-falcon mouse Sdhaf2__Q8C6I2 --fallback perplexity-lite` failed. Falcon
returned "Failed to authenticate", and the perplexity-lite fallback returned HTTP 401 for
insufficient quota. No deep-research file was produced for this folder. The review therefore
rests on the cached primary literature (below), the UniProt record, PANTHER/PAINT data, and the
complete human SDHAF2 review. I read the same-gene falcon report in `genes/mouse/Sdhaf2/` (not a
ProtNLM file) only to find mouse-specific literature, which led to PMID:38569044. I then read
that paper directly in the cache.

### Evolutionary grounding

- Q8C6I2 is in PANTHER PTHR12469:SF2 ("SUCCINATE DEHYDROGENASE ASSEMBLY FACTOR 2,
  MITOCHONDRIAL"; `interpro/panther/PTHR12469/PTHR12469-entries.csv`), the same subfamily as
  human Q9NX18 and yeast Sdh5.
- PAINT IBDs at PTN000279729 (taxon 2759): GO:0005739, GO:0006099, GO:0006121 and GO:0034553.
  The seeds are yeast Sdh5, human SDHAF2 and Arabidopsis AT5G51040
  (`interpro/panther/PTHR12469/PTHR12469-paint.tsv`). PAINT did not propagate protein-FAD
  linkage or a molecular function at this node. The mouse protein-FAD linkage annotation
  arrives by ISO/ISS from human, not by IBA. I treat it as a sound orthology transfer within
  the same subfamily, and this is recorded as inferred for mouse.
- HAMAP MF_03057 (UniRule) supplies the function, matrix location and family statements in
  UniProt.

### Mouse-specific experimental evidence

1. PMID:18614015 (MitoCarta): Sdhaf2 detected by mass spectrometry of mitochondria from mouse
   tissues (HDA, mitochondrion).
2. PMID:38569044 (Zhou et al. 2024, Sci Adv): in Drp1-deficient mouse muscle and C2C12 cells,
   mitochondrial Sdhaf2 is reduced while total Sdhaf2 is not, and complex II assembly is
   selectively reduced (BN-PAGE). [PMID:38569044 "Muscle Drp1-KD reduced complex II assembly and
   activity as a consequence of diminished mitochondrial translocation of succinate
   dehydrogenase assembly factor 2 (Sdhaf2)."] Sdhaf2 overexpression rescues succinate-dependent
   RCR, fatty-acid oxidation and insulin action in myocytes. Sdhaf2 is present in the cytosolic
   fraction of myotubes. The Drp1-Sdhaf2 interaction was shown by proximity ligation in mouse
   C2C12 cells and with recombinant human proteins in vitro. The in vivo perturbation was Drp1,
   not Sdhaf2.
3. PMID:23983127 (Liu et al. 2013, JBC): [PMID:23983127 "In SDH5 knock-out mice, lung
   epithelial cells exhibited elevated mesenchymal markers, which is characteristic of EMT."]
   The GSK-3beta/beta-catenin mechanism comes mostly from human lung cancer cells. The cache
   lacks the results and figure legends.

Not established in mouse: SDHA binding, covalent flavinylation of SDHA, and chaperone activity.
These are inferred from human SDHAF2 (PMID:19628817, PMID:32887801), yeast Sdh5 and bacterial
SdhE, all in the same family.

### Decisions

- Complex II assembly (GO:0034553) and protein-FAD linkage (GO:0018293): ACCEPT (core).
- Mitochondrial matrix: ACCEPT. Mitochondrion (5 rows): MODIFY to matrix, because the term is
  correct but general.
- TCA cycle and succinate-to-ubiquinone electron transport: MARK_AS_OVER_ANNOTATED. Sdhaf2 is an
  assembly factor, not a catalytic subunit (necessity, not participation), which matches the
  human review.
- Nucleolus (ISO): MARK_AS_OVER_ANNOTATED. The human source annotation is no longer present, and
  a nucleolar pool conflicts with the matrix function and with the mouse fractionation data.
- Cytosol (ISO): KEEP_AS_NON_CORE. A pre-import pool is confirmed in mouse myotubes.
- EMT, Wnt and protein dephosphorylation (IMP/ISO/IEA): KEEP_AS_NON_CORE, deferring to the MGI
  curators. These effects are indirect and context-dependent.
- ND molecular_function: MODIFY to GO:0044183 protein folding chaperone. This is inferred
  through the SF2 subfamily from the human structure; it is not a mouse experiment.
- No NEW annotations. The Drp1 interaction was not added as an MF; "protein binding" is
  uninformative.
