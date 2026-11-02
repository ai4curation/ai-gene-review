# Det (Deterin / Survivin, Drosophila melanogaster) curation notes

Accession: Q9VEM2 (FBgn0264291).

Deep research: `Det-deep-research-falcon.md` (falcon; the wrapper logged a 600 s timeout but the run completed and wrote the file). It describes Deterin as the fly Survivin and CPC targeting subunit (scapolo = P86S in the BIR), notes a role in acentrosomal oocyte spindle assembly (Deterin RNAi resembles Incenp/aurB depletion), and characterizes the anti-apoptotic activity as demonstrated only in cultured-cell expression assays. This supports keeping the apoptosis rows as non-core.

## Literature journal

- First described as an anti-apoptotic single-BIR protein in transfected Sf9/S2 cells
  [PMID:10764741 "the expressed protein acts in the cytoplasm to inhibit or deter cells from apoptosis otherwise induced by the caspase-dependent apoptosis activator reaper or by cytotoxicants"]
  [PMID:10764741 "A loss of function phenotype for deterin of cell death was indicated by transfections with either a dominant negative deterin mutant or with inhibitory RNA (RNAi) for deterin"].
- Passenger localization [PMID:21865602 "Survivin accumulated at kinetochores during metaphase, concentrated at the interdigitating central spindle microtubules upon anaphase entry, and was enriched in the central spindle midzone by late anaphase and telophase"].
- scapolo separation-of-function allele: anaphase CPC targeting and cytokinesis
  [PMID:21865602 "Survivin is essential to target the CPC and the mitotic kinesin-like protein 1 orthologue Pavarotti (Pav) to the central spindle and equatorial cell cortex during anaphase in both larval neuroblasts and spermatocytes"]
  [PMID:21865602 "Survivin also enabled localization of Polo kinase and Rho at the equatorial cortex in spermatocytes, critical for contractile ring assembly"]
  [PMID:21865602 "indicating failure of cytokinesis during both meiotic divisions"]
  [PMID:21865602 "a robust central spindle failed to form"].
- With Aurora B, inhibits abscission in germline cysts [PMID:23948252 "Aurora B and Survivin regulate the number of germ cells in each Drosophila egg chamber by inhibiting abscission during differentiation"].

## Decisions

- CPC membership, kinetochore/centromere/midzone, cytokinesis (mitotic and male meiotic) accepted.
- All negative regulation of apoptotic process rows (IMP, ISS, TAS x2, IBA) kept as non-core: real in transfection assays but in vivo requirements are CPC functions.
- Metal ion binding -> zinc ion binding (BIR zinc ligands); spindle assembly (screen IMP) -> meiotic spindle midzone assembly; spindle and chromosome segregation -> spindle midzone, mitotic sister chromatid segregation.
- No MF in core function: Det's activity in the CPC is a localization/targeting role with no adequate GO MF term.
