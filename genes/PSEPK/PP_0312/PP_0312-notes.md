# PP_0312 notes

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


## Independent module audit — 2026-11-06

All three rows reviewed. FAD binding and heterodimer electron transfer remain supported; partner order remains hypothetical. Preserve the TreeGrafter beta-oxidation over-annotation judgment based on a distinct pathway-associated paralog and uncertain acyl-CoA partnership. Seed count is not evidence against PAINT. The helper could not resolve Q88R22 as a tree leaf; do not interpret its final no-loss wording as a verified lineage result.

Sources: [PMID:32631860] full text: “DMGDH activity was measured with the dye-linked assay systems, with PMS as the electron intermediator and DCPIP or NBT as the terminal electron acceptor.” The mechanism paragraph explicitly says “a possible reaction mechanism of DdhC toward DMG was proposed”. [PMID:17951379] full text: PA14 mutants, PAO1 locus numbering, direct NMR on dgcB and soxA. KT2440 functional transfer remains an orthology inference.

All original annotation payloads and inherited NEW rows retained unchanged. No NEW rows added. Raw UniProt/GOA and existing provider artifacts preserved. Default Falcon research genuinely attempted; failed with HTTP 403 authentication/access error. Manual source assessment is recorded here; no provider report was fabricated.
