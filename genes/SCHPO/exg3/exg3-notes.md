# SCHPO exg3 review notes

## 2026-10-11

- Seeded the review with `UV_FROZEN=1 just fetch-gene SCHPO exg3`.
- Cached the three GOA PMIDs with
  `UV_FROZEN=1 just fetch-gene-pmids SCHPO exg3`. PMID:20852022 and
  PMID:25825517 are available as cached full text; PMID:16823372 is
  abstract-only in the local cache.
- `UV_FROZEN=1 just deep-research-falcon SCHPO exg3 --fallback
  perplexity-lite` failed because no deep-research provider credentials are
  configured.
- Manual live searches for `Schizosaccharomyces pombe exg3`,
  `SPBC2D10.05`, and `O74799` found the cached 2010 GH5 characterization,
  BioGRID/PomBase/STRING aggregation, and antibody/product pages, but no newer
  Exg3-specific primary functional paper beyond the 2015 mating fusion-focus
  paper already present in GOA.

Direct evidence:

- The main vegetative characterization is PMID:20852022. Exg3 lacks a signal
  peptide or predicted membrane anchor and localized by HA fractionation and
  live Exg3-GFP imaging as a diffuse cytoplasmic protein excluded from the
  nucleus: [PMID:20852022 Characterization of glycoside hydrolase family 5
  proteins in Schizosaccharomyces pombe, "Exg3 was found mainly in the
  cytoplasm (supernatant) of the cell extracts"] and [PMID:20852022
  Characterization of glycoside hydrolase family 5 proteins in
  Schizosaccharomyces pombe, "Exg3, we found that this was a cytoplasmic
  protein"].
- The same paper supports Exg3 as a beta-1,6-glucanase: overexpression of
  `exg1` and `exg3`, but not `exg2`, increased pustulan-hydrolyzing activity:
  [PMID:20852022 Characterization of glycoside hydrolase family 5 proteins in
  Schizosaccharomyces pombe, "overexpression of exg1 + and exg3 + produced a
  3-fold and 6-fold increase in activity"].
- The normal vegetative role of Exg3 is not genetically resolved. Single
  `exg1`, `exg2`, `exg3`, and triple-deletion strains lacked detectable
  vegetative growth and wall-stress phenotypes in PMID:20852022, so the
  fungal-type cell-wall beta-glucan metabolic process rows should be retained
  as non-core rather than promoted into `core_functions`.
- PMID:25825517 places Exg3 with the other assayed fission-yeast glucanases at
  the mating fusion focus: [PMID:25825517 A formin-nucleated actin aster
  concentrates cell wall hydrolases for cell fusion in fission yeast,
  "Remarkably, all seven colocalized with Myo52-tdTomato at the fusion focus"].
  The exg3 single-deletion effect was measured in a sensitized `fus1Delta`
  cross, so the mating projection rows are supported but non-core.

PTHR31297 PAINT notes:

- Exg3 is in `PTHR31297:SF43`, PANTHER's
  `GLUCAN 1,3-BETA-GLUCOSIDASE 3` subfamily.
- The `PANTHER:PTN001262669` cytoplasm, glucan endo-1,6-beta-glucosidase
  activity, and fungal cell-wall beta-glucan metabolic process rows are the
  Exg3/YBR056W branch, seeded directly by PomBase `SPBC2D10.05` and SGD
  `YBR056W` annotations. This is not the Exg1 secreted glucanase node or the
  Exg2 membrane branch.
