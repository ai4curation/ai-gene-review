# PP_0313 notes

## 2026-11-04 session (Claude, AI-assisted)

Provider deep research was not generated in this session (no API keys). Sources:
cached publications, UniProt flat files, PTHR43153/PTHR21294 PAINT files, a UniProt
REST query for the ETF genes in each genome, and the pairwise-identity analysis in
`genes/PSEPK/PP_0312/PP_0312-bioinformatics/RESULTS.md`.

- This review builds on the main-branch DRAFT. Open PR #2493 (refs/tmp/etf) was read as leads only.
- Differences from PR #2493: no NEW part_of GO:0045251 was added. Its GO definition specifies electron transfer "from an acyl-CoA molecule to ubiquinone", which does not fit a dimethylglycine-locus ETF. This was raised as a suggested question instead.
- Other differences: the GO:0033539 reasoning now rests on PAINT node placement and paralog identity, not on KEGG maps. The KEGG/project-TSV arguments of the PR were not used.
- Agreement with the PR: both keep GO:0033539 as MARK_AS_OVER_ANNOTATED, matching projects/TREEGRAFTER/rereview-2026-09-24/batch-02.yaml, so no supersession was needed. Both record the core function as FAD binding (alpha) contributing to GO:0009055.
- Paralog analysis: genes/PSEPK/PP_0312/PP_0312-bioinformatics/ (paralog_identity.py, RESULTS.md).
- KT2440 also has a second ETF pair, PP_4201/PP_4202 (etfA/etfB). It is 62% identical to human ETFA/ETFB. PP_0312/PP_0313 are about 33% identical to the human proteins.
