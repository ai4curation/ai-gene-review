# SCLT1 review notes

## 2026-10-03: sources and scope

- GOA snapshot 20 rows; UniProt Q96NL6. GOA PMIDs cached by `just fetch-gene-pmids` (PMID:23348840 abstract-only; PMID:21399614 full text).
- Additional papers cached: PMID:15797711 (rat CAP-1A/Sclt1 Nav1.8-clathrin linker; source of IEA MF rows), PMID:29789620, PMID:30131441 (LRRC45), PMID:28486600 (Sclt1 knockout mouse), PMID:24882706.
- Deep research: first falcon run timed out at 600 s; the rerun with `--timeout 2400` succeeded (`SCLT1-deep-research-falcon.md`).

## Functional synthesis

- SCLT1 is a distal appendage component recruited by CEP83 and required for FBF1 and CEP164 recruitment [PMID:23348840 "CEP83 recruits both SCLT1 and CEP89 to centrioles. Subsequent recruitment of FBF1 and CEP164 is independent of CEP89 but mediated by SCLT1."]
- It is part of the appendage blade backbone [PMID:29789620 "CEP83, CEP89, SCLT1, and CEP164 form the backbone of pinwheel blades"].
- CEP83 and SCLT1 also recruit LRRC45, which recruits FBF1 [PMID:30131441 "We show that the core appendage proteins Cep83 and SCLT1 recruit LRRC45 to the mother centriole."]
- Sclt1-null mice show ciliopathy phenotypes [PMID:28486600 "The Sclt1-/- mice exhibit typical ciliopathy phenotypes, including cystic kidney, cleft palate and polydactyly."]; SCLT1 variants are linked to OFD syndrome [PMID:24882706 "mutations in two genes encoding DAPs components (CEP164/NPHP15, SCLT1) have been associated with human ciliopathies, namely nephronophthisis and orofaciodigital syndrome"].
- The gene name comes from rat CAP-1A, which binds Nav1.8 and clathrin and lowers Nav1.8 current density in DRG neurons [PMID:15797711 "Coexpression of CAP-1A and Na(v)1.8 in DRG neurons reduces Na(v)1.8 current density by approximately 50% without affecting the endogenous or recombinant tetrodotoxin-sensitive currents."]. Not tested for human SCLT1.

- Deep research adds: a Kanie et al. knockout preprint finds CEP83 localization also depends on SCLT1, suggesting a CEP83-SCLT1 structural module rather than a strict one-way chain [file:human/SCLT1/SCLT1-deep-research-falcon.md "A later SCLT1-knockout analysis found a stronger, reciprocal dependence of CEP83 localization on SCLT1"]; SCLT1 C-terminal coiled coil (554-688) binds LRRC45 in yeast two-hybrid (Kurtulmus 2018); Sclt1 mouse limbs show reduced vesicle docking, TTBK2 recruitment and Hedgehog signalling, which the report treats as downstream [file:human/SCLT1/SCLT1-deep-research-falcon.md "Hedgehog signaling is a downstream consequence of SCLT1-dependent ciliogenesis"]. The OFD IX report had a single SCLT1 case, which needs confirmation.

## Annotation decisions

- Accept centriole, centrosome, basal body (HPA), transition fiber and cilium assembly rows.
- Sodium channel regulator activity and clathrin binding (IEA from rat): keep as non-core.
- Clathrin complex (IEA): over-annotation (adaptor, not a clathrin coat subunit).
- Clustering of voltage-gated sodium channels (IEA): remove; the only data show reduced channel density, not clustering.
- Reactome cytosol TAS rows: non-core.
- NEW structural molecule activity (blade backbone) as core MF.

## HPA cilium atlas vs module role

- Module role: "distal appendage component".
- HPA v25: Basal body (Supported); main locations basal body and cytosol.
- Comparison: a Supported basal body call is fully consistent with SCLT1 being a distal appendage (transition fiber) protein of the basal body. core_functions match the module role. One refinement: knockout data (via deep research) suggest CEP83 and SCLT1 depend on each other, so the module's strict order (CEP83 then SCLT1) is a simplification. No substantive disagreement.
