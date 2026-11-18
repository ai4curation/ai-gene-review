# Mvd (mouse) review notes

UniProt Q99JF5 (MVD1_MOUSE), MGI:2179327, 401 aa (Met1 removed, Ala2 acetylated by similarity).
PANTHER PTHR10977:SF3 (DIPHOSPHOMEVALONATE DECARBOXYLASE), GHMP superfamily. A mouse crystal
structure exists (PDB 3F0N, residues 6-401; no associated publication found). No deep-research
provider file (no provider keys here); these are my own notes.

## Literature search (2026-11-18)

- Europe PMC `(TITLE:"diphosphomevalonate decarboxylase" OR TITLE:"mevalonate pyrophosphate
  decarboxylase" OR TITLE:"mevalonate diphosphate decarboxylase" OR TITLE:"MVD") AND (mouse OR mice
  OR murine OR rat OR mammalian OR human)`: 100 hits, most of them "MVD" as microvessel density,
  microvascular decompression or Marburg virus disease. Mouse primary papers on the enzyme:
  PMID:11913522 (purified mouse liver MPD), PMID:12736493 (localization in B16F10 cells),
  PMID:12913254 (pravastatin induction), PMID:39323215 (epidermal conditional knockout),
  PMID:37227548 (F250S knock-in). Rat localization papers behind the ISO rows: PMID:11725955,
  PMID:11767099, PMID:12081138 (all Michihara lab). Human: PMID:8626466 (cloning), PMID:14972328
  (cytosol), PMID:12646231 (mortalin), PMID:9270019 (6-fluoromevalonate and proliferation).
- The 2024 mouse liver peroxisome proteome (PMID:38247867) does not name MVD in its text.

## Mouse biology

- Enzyme from mouse liver: [PMID:11913522 "The purified enzyme was a homodimer of 46-kDa subunits and
  had an isoelectric point of 5.0"], [PMID:11913522 "Kinetic analysis revealed an apparent Km value
  of 10 microm for mevalonate pyrophosphate"], needing ATP and Mg2+.
- Regulation: statin induces liver MPD protein and activity [PMID:12913254 "MPD was markedly
  increased (9-fold) only in the liver compared with nontreated mice"]; peroxisome proliferators do
  not [PMID:12736493 "No increase in the protein level of MPD was observed in the crude extract of the
  livers of mice administered with peroxisome proliferative drugs"].
- Genetics: keratinocyte-specific deletion gives porokeratosis-like lesions [PMID:39323215 "Skin
  lesions appeared following Mvd deficiency, and pathological examination revealed the characteristic
  cornoid lamella, as well as cutaneous inflammation"]; homozygous F250S knock-ins were not obtained
  [PMID:39323215 "we did not obtain any homozygous Mvd point mutation mice, suggesting that a
  homozygous mutation of Mvd in all organs and cells may cause embryonic lethality in mice"].
- Activity in mouse liver also measured in Pex5-/- liver (PMID:11792727, abstract only).

## Localization

- Mouse, direct: [PMID:12736493 "When the subcellular distribution of MPD in mouse melanoma (B16F10)
  cells was examined by cell fractionation, MPD was detected in the cytosol of B16F10 cells, but not
  in the peroxisomes"]; digitonin released MPD like LDH and unlike catalase.
- Rat sources of the ISO peroxisome and peroxisomal-matrix rows: [PMID:11767099 "Peroxisomal fraction
  contained a small amount of 45-kDa MPD, but not 37-kDa MPD"] and [PMID:11767099 "Also, 45-kDa MPD in
  peroxisome is localized in the matrix"]; the same group then wrote [PMID:12081138 "The relative
  enrichment of 45-kDa MPD in peroxisomes was lower than that of LDH, suggesting the possibility that
  45-kDa MPD of SHRSP did not exist in the peroxisomes"] and concluded rat hepatocyte MPD is
  predominantly cytosolic (PMID:11725955).
- Human: cytosolic, no peroxisomal pool (PMID:14972328).
- Decision: REMOVE both peroxisome ISO rows (mouse-specific direct evidence contradicts them, and the
  rat source is a minor fraction that its own authors doubted). Cytosol and cytoplasm accepted.

## Other projected rows

- Hsp70 protein binding (human mortalin yeast two-hybrid and co-IP, PMID:12646231): over-annotated
  for mouse; a chaperone interaction, not MVD's function.
- Positive regulation of cell population proliferation (human, PMID:9270019): the source used the
  MVD inhibitor 6-fluoromevalonate; the authors attribute growth arrest to a mevalonate metabolite
  proximal to IPP. Indirect; over-annotated.
- Protein homodimerization: supported directly in mouse (PMID:11913522); non-core.

## GO-CAM pathway-edge rows

Same pattern as Mvk (see genes/mouse/Mvk/Mvk-notes.md); cohort source defect recorded on the Mvk
review.
