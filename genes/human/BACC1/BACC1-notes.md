# BACC1 notes

## 2026-10-05 review (PAINT, affinage)

- The PAINT list gives this gene as BAP18; the current HGNC symbol is BACC1 (Q8IXM2).
- NURF and MLL1 complex rows are accepted. The IDA sources are proteomics papers whose cached abstracts do not name BAP18, so the curators' full-text reading is relied on (UniProt agrees).
- NEW GO:0003713 transcription coactivator activity (IMP), because BAP18 coactivates AR and ERalpha in some cells [PMID:27226492 "BAP18 facilitates the recruitment of MLL1 subcomplex and AR to androgen-response element (ARE) of AR target genes, subsequently increasing histone H3K4 trimethylation and H4K16 acetylation."], and NEW GO:0003714 transcription corepressor activity (IMP), because it corepresses AR in TNBC (PMID:41163225).
- The H3K4me3 reader activity is only stated as prior knowledge in PMID:32986841, so it is not asserted and is raised as a question.

## 2026-10-05 PR 4373 follow-up

- Replaced the generic NEW GO:0003712 parent with separate child activities for the sign-specific evidence: GO:0003713 transcription coactivator activity from the AR/ERalpha papers and GO:0003714 transcription corepressor activity from the AR-positive TNBC SIN3A/HDAC paper.
- Fetched the seven Affinage PMIDs that were missing from `publications/` and corrected the deep-research reference review to match the now-complete cache gate.
- GO:0042802 identical protein binding now cites the UniProt/IntAct BACC1 self-interaction line rather than the unrelated chromatin-complex FUNCTION line.
- PMID:25456412 now supports the DPY30 generic-binding row and both NURF complex rows, because the paper places the BAP18-DPY30 interaction in NURF rather than only MLL1.
- The SANT domain and the SANT-deleted Q8IXM2-2 isoform are recorded in the H3K4me3 reader question and experiment.
