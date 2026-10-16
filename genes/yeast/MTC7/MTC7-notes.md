# MTC7 rereview notes

## 2026-09-28 re-review

- MTC7 has no IBA annotations in `MTC7-goa.tsv`; the GOA rows are membrane IEA, two duplicate molecular-function ND rows, cellular-component ND, and biological-process ND.
- Re-read the MTC7 review, UniProt record, Falcon deep-research report, prior manual deep-research report, local bioinformatics summary, and the cached full text of Addinall et al. 2008 [PMID:18845848].
- Searched newer literature for `MTC7`, `YEL033W`, and `Maintenance of telomere capping`. The hits were database pages, theses, older screen papers, or broad studies in which MTC7 appears only in a table; no newer primary paper establishes a molecular function or direct pathway role for Mtc7.
- Fetched Askree et al. 2004 [PMID:15161972] after a search found the earlier telomere-length screen. That paper is important counterevidence: YEL033W was the one tested hit whose short-telomere phenotype did not cosegregate with the deletion marker.
- UniProt records MTC7 as PE 4 (Predicted), so the broad GO:0016020 membrane row was retained only as a sequence-prediction annotation. Follow UniProt and the local topology analysis over the Falcon statement that Mtc7 lacks predicted transmembrane segments: both the UniProt feature table and `MTC7-bioinformatics/RESULTS.md` support two N-terminal hydrophobic helices.
- Retracted the proposed `GO:0016233 telomere capping` assertion. Addinall et al. justify MTC7 as a telomere-biology candidate, but a high-throughput `cdc13-1` modifier phenotype does not show that Mtc7 itself carries out chromosome-end capping or acts directly at telomeres.
- Rewrote `MTC7-pathway.md` to mark MTC7 as pathway-unresolved instead of modeling unproven nuclear shuttling, telomerase regulation, telomeric chromatin interaction, and short-telomere causality.
