# Ghr ISO donor trace

Trace performed on 2026-03-21 by matching each mouse `ISO` row in `genes/mouse/Ghr/Ghr-goa.tsv` to the current donor-side annotations on human `GHR` (`UniProtKB:P10912`) or rat `Ghr` (`UniProtKB:P16310`, mapped from `RGD:2687`).

## Human donor `UniProtKB:P10912`

- `GO:0004903 growth hormone receptor activity`: donor retains direct human experimental support. Keep. Mouse also has direct mouse `IDA`, so the ISO edge is redundant and partly circular rather than wrong.
- `GO:0005615 extracellular space`: donor retains direct support, but this mainly fits the soluble GHBP product rather than the signaling receptor. Keep as non-core.
- `GO:0005886 plasma membrane` with mouse qualifier `is_active_in`: donor retains direct support. Keep.
- `GO:0005886 plasma membrane` with mouse qualifier `located_in`: donor retains direct support. Keep.
- `GO:0008289 lipid binding`: donor trace recovers only a non-core human assertion, with no mouse support and no role in established mouse Ghr biology. Remove as over-transfer.
- `GO:0009986 cell surface`: donor retains direct support. Keep.
- `GO:0016020 membrane`: donor support exists, but the term is too broad given the stronger plasma-membrane annotations and GHBP membrane-association context. Keep as non-core.
- `GO:0017046 peptide hormone binding`: donor retains direct support. Keep.
- `GO:0019838 growth factor binding`: no current donor-side support recovered; the specific accepted term is peptide hormone binding. Remove.
- `GO:0031623 receptor internalization`: no current human donor support recovered. Remove.
- `GO:0032355 response to estradiol`: no current human donor support recovered. Remove.
- `GO:0032870 cellular response to hormone stimulus`: donor support is broad endocrine physiology, not a Ghr-specific core function. Mark as over-annotated.
- `GO:0040018 positive regulation of multicellular organism growth`: biologically plausible but phenotype-level and non-core. Keep as non-core.
- `GO:0042445 hormone metabolic process`: broad downstream/endocrine-context term, not direct receptor function. Mark as over-annotated.
- `GO:0042802 identical protein binding`: donor retains direct support for receptor self-association. Keep.
- `GO:0042803 protein homodimerization activity`: donor retains direct support. Keep.
- `GO:0043235 receptor complex`: donor retains direct support. Keep.
- `GO:0046898 response to cycloheximide`: no current human donor support recovered. Remove.
- `GO:0048009 insulin-like growth factor receptor signaling pathway`: this is pathway cross-talk/physiology, not Ghr core function. Remove.
- `GO:0060396 growth hormone receptor signaling pathway`: donor retains direct support. Keep.
- `GO:0070195 growth hormone receptor complex`: donor retains direct support. Keep.
- `GO:0005829 cytosol`: donor trace only recovers non-experimental family-level support. Remove.
- `GO:0036464 cytoplasmic ribonucleoprotein granule`: no current donor-side support recovered. Remove.
- `GO:0043161 proteasome-mediated ubiquitin-dependent protein catabolic process`: no current donor-side support recovered, and the receptor is more plausibly the substrate than the agent of this process. Remove.
- `GO:0060397 growth hormone receptor signaling pathway via JAK-STAT`: no current donor-side support recovered, but mouse has direct `IDA` support for the same term. Keep the term, but do not rely on the ISO edge.
- `GO:0060400 negative regulation of growth hormone receptor signaling pathway`: no current donor-side support recovered and the term reads as a downstream regulatory consequence rather than core receptor function. Remove.

## Rat donor `UniProtKB:P16310` mapped from `RGD:2687`

- `GO:0042976 activation of Janus kinase activity`: donor retains direct rat experimental support. Keep.
- `GO:0004903 growth hormone receptor activity`: donor has direct rat experiments, but also donor-side ISO copies from mouse and human. Keep the term but flag the ISO chain as circular/redundant.
- `GO:0005615 extracellular space`: donor includes direct rat support plus donor-side ISO-from-human copies. Keep as non-core and note circularity.
- `GO:0007259 cell surface receptor signaling pathway via JAK-STAT`: donor retains direct rat support, but the mouse-specific term `GO:0060397` is better. Modify.
- `GO:0009755 hormone-mediated signaling pathway`: donor support is too broad compared with specific growth-hormone signaling terms. Mark as over-annotated.
- `GO:0019901 protein kinase binding`: donor retains rat interaction evidence, but the more precise term on this receptor is protein tyrosine kinase binding. Modify.
- `GO:0019903 protein phosphatase binding`: donor retains rat support for phosphatase interactions. Keep as non-core.
- `GO:0030296 protein tyrosine kinase activator activity`: donor retains direct rat experimental support. Keep.
- `GO:0032107 regulation of response to nutrient levels`: donor support is contextual physiology rather than core receptor function. Remove.
- `GO:0042169 SH2 domain binding`: donor retains direct rat support for phosphotyrosine docking interactions. Keep.
- `GO:0043025 neuronal cell body`: donor support is tissue/context-specific rat neuroanatomy and should not be transferred as a generic mouse Ghr location. Remove.
- `GO:0043410 positive regulation of MAPK cascade`: donor retains direct rat support. Keep.
- `GO:0046427 positive regulation of receptor signaling pathway via JAK-STAT`: donor retains direct rat support. Keep.
- `GO:0060396 growth hormone receptor signaling pathway`: donor includes a direct rat pathway assertion, but also donor-side ISO-from-human copies. Keep the term while flagging the rat ISO chain as circular.
- `GO:1990782 protein tyrosine kinase binding`: donor retains direct rat support. Keep.

## Important circularity and stale-transfer findings

- Rat donor `P16310` carries donor-side `NOT|involved_in` annotations for `GO:0031623 receptor internalization` and `GO:0046898 response to cycloheximide`. Those negatives make the corresponding mouse ISO transfers especially weak.
- Several mouse ISO rows are best interpreted as transfer-of-transfer artifacts: mouse `ISO <- rat ISO <- human`, rather than mouse `ISO <- direct donor experiment`.
- No evidence of classic paralog mix-up with prolactin receptor was needed to explain the worst rows; the bigger problem is cytokine-receptor family over-generalization plus circular donor propagation.
