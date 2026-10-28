# Lpl (rat) review notes

## Session 1: initial review

- `just fetch-gene rat Lpl` resolved Q06000 (LIPL_RAT); 85 GOA rows. The first two attempts timed out against rest.uniprot.org; the third succeeded.
- No deep-research provider is available, so the literature summary is in `Lpl-deep-research-manual.md`.
- PMID:18722549 is not in GOA but was read in full: rat heart LPL activity (heparin-releasable and residual) rises with cold acclimation [PMID:18722549 "Cold acclimation significantly increased heparin-releasable LPL (P<0.05) and tissue residual LPL (P<0.01)."]. It supports the activity and the endothelial-surface pool. No NEW annotation was needed because cell surface, extracellular region and lipoprotein lipase activity are already present.

### Decisions

- Core: lipoprotein lipase activity (GO:0004465); triglyceride catabolic process, chylomicron remodeling, VLDL remodeling and VLDL clearance; extracellular region and cell surface.
- General parents (triacylglycerol lipase activity, lipase activity, carboxylic ester hydrolase activity, lipid metabolic/catabolic process, triglyceride metabolic process) were changed with MODIFY to the specific terms the gene already carries.
- Over-annotations: fatty acid biosynthetic process (IBA/ISO; LPL releases fatty acids and synthesises none); HDL remodeling (IBA; the PTN000906454 donors are LIPC/LIPG only); catalytic complex (ISO); triglyceride biosynthetic process (IMP, PMID:11788374, abstract-only; LPL supplies fatty acids upstream of re-esterification and performs no synthetic step); response to xenobiotic stimulus (IEP, pharmacological).
- Non-core: PLA1 activity, calcium binding, homodimerization, signaling receptor binding, triglyceride binding, inflammatory/cytokine terms, adipogenesis terms, nutrient/fatty acid response terms, and negative regulation of cellular response to insulin stimulus (the IMP from L6 knockdown is sound, but the effect is indirect, through fatty acid supply).
- No REMOVE actions.
- No NEW terms. A GPIHBP1-dependent protein-membrane adaptor role (accepted in the human review as TAS) has no rat-specific evidence and is not proposed here.

## 2026-10-28 correction: extracellular space is obsolete

- GO:0005615 extracellular space is obsolete in the current GO release. The GO:0005576
  extracellular region rows that had been MODIFIED to it are now ACCEPT (the extracellular
  location is correct and core), and core_functions locations use GO:0005576 extracellular region.
