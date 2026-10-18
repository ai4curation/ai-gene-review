# Manual curation benchmark datasets

Item-level data behind published assessments of manual (literature) curation,
cross-checked against the GOA rows and reviews in `genes/`.

## Datasets

| Study | What was checked | Data here | Source |
|---|---|---|---|
| Keseler et al. 2014 (PMID:24923819) | 634 EcoCyc/CGD facts (~165 GO) checked against the cited paper | `raw/keseler2014/Supplemental.xlsx`: every fact, validator score, adjudication, both comments | OUP supplementary zip |
| Cusick et al. 2009 (PMID:19116613) | Literature-curated PPIs re-curated from the source paper | `raw/cusick2009/dataset1-4.xls`: yeast 100 pairs; human LC-multiple 822 and LC-random 360 curation units; Arabidopsis 331, each with error category | PMC open-data S3 bucket (`pmc-oa-opendata`, PMC2683745.1) |
| Camon et al. 2005 (PMID:15960829) | 30 papers annotated blind by two GOA curators | `camon2005_iaa.yaml`, transcribed from `raw/PMC1869009/1471-2105-6-S1-S17-S1.jpg`; counts per paper only (the GO terms were never published) | Europe PMC supplementary files |
| Van Auken et al. 2014, BC4GO (PMID:25070993) | 8 curators, 200 full-text papers | **not obtained**; see below | |

Not obtained:
- **BC4GO corpus.** The registered URL `biocreative.org/resources/corpora/bc-iv-go-task-corpus/`
  now redirects to an unrelated site (the domain has lapsed), and the UDel mirror
  (`biocreative.bioinformatics.udel.edu`) returns HTTP 403 to this environment. The paper says
  the corpus is for non-commercial use; contact Zhiyong Lu (NCBI).
- **Salwinski et al. 2009** (PMID:19935838) is a letter; its re-scoring of the Cusick data is
  not in the supplements above.

## Cross-check

`crosscheck.py` writes `crosscheck/{keseler2014,cusick2009,camon2005}.yaml`: every benchmark item,
plus any GOA row in `genes/` citing the same PMID for the same gene, with our review action.
For Cusick it also records whether the row's WITH/FROM names the partner that Cusick scored
(`with_names_scored_partner`; null when the partner has no review folder here).

    uv run --with xlrd python -I research/curation_benchmarks/crosscheck.py

Overlap with the repo:
- Keseler: none. Its 181 genes do not overlap our 89 ECOLI and CANAL folders.
- Camon: 2 of 30 proteins (DNER, THTPA). Since only counts were published, terms cannot be compared.
- Cusick: 199 of 1,182 human curation units have a GOA row citing the same paper; 4 erroneous
  units have a GOA IPI row naming the same partner.

Those four, checked against the paper:
- **PEX14-PEX19, PEX19-PEX3 (PMID:10704444): the benchmark is wrong.** Cusick scores these
  "No binding partners / tested but not detected", but the paper reports direct PEX19-PEX14
  binding by blot overlay with recombinant protein, measured Kd 350-800 nM, and PEX19-PEX3
  binding by blot overlay and the NLS-mislocalisation assay. The "not detected" fits only the
  yeast two-hybrid screen. Our reviews call the interactions real (MARK_AS_OVER_ANNOTATED or
  MODIFY or REMOVE, under the GO:0005515 policy only).
- **PTPN11-FRS2 (PMID:9632781): wrong species, missed by our reviews.** Cusick records the
  experiment as mouse (3T3 lysates); the title names PC12 (rat) cells. GOA carries human IPI rows
  (IntAct) for both proteins. Our reviews mark them MARK_AS_OVER_ANNOTATED (PTPN11) and MODIFY
  to SH2 domain binding (FRS2) without noting that the evidence is from rodent cells. The paper is
  abstract-only in our cache.

Wrong-partner errors the GO rows avoided: for GRB2 (PMID:12359715), FEN1 (PMID:11430825) and
BCL2L1 (PMID:11060313), the GOA WITH/FROM names the partner Cusick says was actually shown (LAX
Q8IWV1, EP300 Q09472, MOAP1 Q96BY2), not the partner the PPI database curated.
