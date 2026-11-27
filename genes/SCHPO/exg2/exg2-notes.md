# SCHPO exg2 review notes

## 2026-10-11

- Seeded the review with `UV_FROZEN=1 just fetch-gene SCHPO exg2`.
- Cached the two GOA PMIDs with
  `UV_FROZEN=1 just fetch-gene-pmids SCHPO exg2`; both cited papers are full
  text locally.
- `UV_FROZEN=1 just deep-research-falcon SCHPO exg2 --fallback perplexity-lite`
  failed because no deep-research provider credentials are configured.
- Manual live search for `Schizosaccharomyces pombe exg2`, `SPAC12B10.11`, and
  `Q10444` found the already cached fission-yeast GH5 paper, YRC/STRING/PomBase
  aggregation, a 2024 antibody-catalog hit, and thesis/table mentions, but no
  primary exg2 functional paper newer than the 2015 mating fusion-focus paper.

Direct evidence:

- The main vegetative characterization is PMID:20852022. Exg2 has a predicted
  N-terminal transmembrane segment, fractionates with the membrane/cell-wall
  pellet, and is integral by extraction tests: [PMID:20852022
  Characterization of glycoside hydrolase family 5 proteins in
  Schizosaccharomyces pombe, "Exg2 is indeed an integral membrane protein that
  fractionates in the detergent-resistant membrane fraction"].
- Endogenously expressed Exg2-GFP was too dim to detect, but mildly
  overexpressed Exg2-GFP localized to growth zones: [PMID:20852022
  Characterization of glycoside hydrolase family 5 proteins in
  Schizosaccharomyces pombe, "Exg2 was localized at the sites of cell growth,
  that is, the poles of the cell and the septum"].
- Exg2 should not be treated as an established catalytic
  endo-1,6-beta-glucanase just because Exg1 and Exg3 have that activity.
  Exg1/Exg3 overexpression increased pustulan activity, but Exg2 did not:
  [PMID:20852022 Characterization of glycoside hydrolase family 5 proteins in
  Schizosaccharomyces pombe, "no activity could be detected in cells
  overexpressing exg2"]. The overexpression phenotype also survived catalytic
  site mutations: [PMID:20852022 Characterization of glycoside hydrolase family
  5 proteins in Schizosaccharomyces pombe, "the N-terminal region and the GH5
  domains are required to induce abnormal glucan synthesis but that the
  catalytic activity, if present, is not essential"].
- The only vegetative phenotype is an overexpression phenotype. Full-length
  Exg2 overexpression causes abnormal, beta-glucan-containing wall material at
  poles and septa, while single and triple `exg` deletion strains lack obvious
  growth or wall-stress phenotypes. Treat the `PMID:20852022` IMP for
  fungal-type cell wall organization as direct but not as evidence that the
  normal core function is known.
- PMID:25825517 places Exg2 with the other fission-yeast glucanases at the
  mating fusion focus: [PMID:25825517 A formin-nucleated actin aster
  concentrates cell wall hydrolases for cell fusion in fission yeast,
  "Remarkably, all seven colocalized with Myo52-tdTomato at the fusion focus"].
  The single-deletion phenotype was visible in a sensitized `fus1Delta` cross,
  so the mating projection rows are supported but non-core.

PTHR31297 PAINT notes:

- Exg2 is in `PTHR31297:SF34`, PANTHER's
  `GLUCAN 1,3-BETA-GLUCOSIDASE 2` subfamily, while the fission-yeast Exg1
  enzyme is in `PTHR31297:SF1`.
- The only PTHR31297 IBA currently inherited by Exg2 is
  `PANTHER:PTN001262628` for `GO:0009251 glucan catabolic process`, seeded by
  Aspergillus nidulans ExgD/Q5AVZ7 and ExgB/Q5B6Q3. This is broad fungal GH5
  inheritance rather than an Exg2-specific catalytic claim; it is retained as
  non-core because the direct vegetative Exg2 data show abnormal wall
  deposition after overexpression but do not demonstrate normal glucan
  catabolism.
- The narrower fungal extracellular/cell-wall node `PANTHER:PTN001262686` and
  Saccharomycetales exo-1,3-beta-glucosidase node `PANTHER:PTN001262687` do
  not hit S. pombe Exg2. The fission-yeast-specific `PANTHER:PTN008631699`
  division-septum and endo-1,6-beta-glucosidase rows are Exg1-specific and
  likewise should not hit Exg2.
