# etfA (Q1QYV9, Csal_0992) notes

## 2026-11-04 session (Claude, AI-assisted)

Provider deep research was not generated in this session (no API keys). Sources:
cached publications, UniProt flat files, PTHR43153/PTHR21294 PAINT files, a UniProt
REST query for the ETF genes in each genome, and the pairwise-identity analysis in
`genes/PSEPK/PP_0312/PP_0312-bioinformatics/RESULTS.md`.

- PMID:32631860 (abstract only): "gene disruption and complementation assays indicated that the csal_0990, csal_0991, csal_0992, and csal_0993 genes are responsible for DMG degradation to sarcosine."
- The genome has a second ETF pair, Csal_1613/Csal_1614 (UniProt query for organism_id:290398 and PANTHER PTHR43153/PTHR21294). Both alpha genes are in PTHR43153:SF1.
- Csal_0992 is 65.5% identical to PP_0312 and 32.6% identical to human ETFA. Csal_1614 is 58.4% identical to human ETFA. So the dgc-locus ETF is a distinct paralog group.
- GO:0033539 (TreeGrafter, from the PAINT IBD on PTN000097951 seeded by human ETFA only): MARK_AS_OVER_ANNOTATED, for consistency with PP_0312 and the TreeGrafter re-review. REMOVE was considered, but no data exclude acyl-CoA dehydrogenase partners.
- GO:0009055 and GO:0050660 are ACCEPTed. NEW GO:0031457 (IMP), consistent with ddhC and Csal_0991.
- Core function: FAD binding, contributing to GO:0009055 (the heterodimer activity). This is consistent with the module's ETF annoton (GO:0009055), which is fed by the DgcB/Csal_0991 electron-transfer annoton.


## 2026-11-06 comparative module audit

Persistent marker DMG-CHRI1-etfA-20261106. Reviewed every original row, inherited proposal, core and cited source. Default Falcon was attempted normally because no provider artifact existed; HTTP403 authentication/access failure is logged. These are manual notes, not a fabricated provider report.

- Retained conserved ETF electron-transfer contribution and existing pathway proposal; distinguished ZW4-1 genetics from unmeasured relay biochemistry.

Original machine payloads, inherited NEW rows and raw files are protected by original-members-baseline.json. PMID32631860 is now full text; its assay scope is documented in ../ddhC/ddhC-source-analysis/identity-and-assay-scope.md.
