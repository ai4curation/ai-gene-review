# Manual curation benchmark datasets

Item-level data behind published assessments of manual (literature) curation,
cross-checked against the GOA rows and reviews in `genes/`.

## Datasets

| Study | What was checked | Data here | Source |
|---|---|---|---|
| Keseler et al. 2014 (PMID:24923819) | 634 EcoCyc/CGD facts (~165 GO) checked against the cited paper | `raw/keseler2014/Supplemental.xlsx`: every fact, validator score, adjudication, both comments | OUP supplementary zip |
| Cusick et al. 2009 (PMID:19116613) | Literature-curated PPIs re-curated from the source paper | `raw/cusick2009/dataset1-4.xls`: yeast 100 pairs; human LC-multiple 822 and LC-random 360 curation units; Arabidopsis 331, each with error category | PMC open-data S3 bucket (`pmc-oa-opendata`, PMC2683745.1) |
| Camon et al. 2005 (PMID:15960829) | 30 papers annotated blind by two GOA curators | `camon2005_iaa.yaml`, transcribed from `raw/PMC1869009/1471-2105-6-S1-S17-S1.jpg`; counts per paper only (the GO terms were never published) | Europe PMC supplementary files |
| Van Auken et al. 2014, BC4GO (PMID:25070993) | 8 curators, 200 full-text papers | `raw/bc4go/` (gitignored; run `fetch_bc4go.sh`): one consolidated gold set per paper, 5,206 annotations with gene (NCBI Gene id), GO term, evidence code and evidence sentence for the 100 training + 50 development papers; the 50 test papers have no gold | `https://ftp.ncbi.nlm.nih.gov/pub/lu/BC4GO/`, linked from https://www.ncbi.nlm.nih.gov/research/bionlp/biocreative |

BC4GO notes:
- The released corpus has **no per-curator annotations**, so the paper's inter-annotator
  agreement (47% exact GO term) cannot be recomputed from it.
- `goevidence: NONE` (1,624 annotations) marks a "summary" sentence: it states what was
  found but not how, so it cannot support a full annotation alone. Experimental sentences carry
  a code (IMP 1,528, IDA 964, IEP 461, IGI 349, IPI 194, ...).
- The corpus is for non-commercial use and includes full-text articles, so it is not committed.
- The registered URL `biocreative.org/resources/corpora/bc-iv-go-task-corpus/` now goes to an
  unrelated site (the domain lapsed); use the NCBI FTP.

Not obtained:
- **Salwinski et al. 2009** (PMID:19935838) is a letter; its re-scoring of the Cusick data is
  not in the supplements above.

## Cross-check

`crosscheck.py` writes `crosscheck/{keseler2014,cusick2009,camon2005}.yaml`: every benchmark item,
plus any GOA row in `genes/` citing the same PMID for the same gene, with our review action.
For Cusick it also records whether the row's WITH/FROM names the partner that Cusick scored
(`with_names_scored_partner`; null when the partner has no review folder here).

    uv run --with xlrd python -I research/curation_benchmarks/crosscheck.py

BC4GO genes are joined to `genes/` folders on NCBI Gene id (from each folder's UniProt `DR GeneID`
line), never on symbol: PMID:21690310 annotates both fly Cdc42 (32981) and mouse Cdc42 (12540).
Terms obsoleted since 2013 are mapped through `replaced_by`, and parent/child relations use
is_a and part_of in current GO (oaklib `sqlite:obo:go`).

Overlap with the repo:
- BC4GO: 24 paper-gene pairs in 22 folders (66 BC4GO terms). Of the 43 annotations with
  experimental evidence: 20 have the same term in GOA from the same paper, 6 a parent/child term,
  and 17 have no GOA row from that paper. Of these 17, 9 are car-1 (below).
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

BC4GO cases worth a look:
- **car-1 (worm), PMID:16247027.** The BC4GO WormBase curator recorded IMP annotations for spindle
  midzone assembly, cleavage furrow ingression, sister chromatid segregation, spindle assembly,
  embryo development, protein localization, and IDA poly(U) RNA binding. GOA has only P granule and
  ribonucleoprotein complex from this paper, and **no cytokinesis-related process term for car-1
  from any paper**, though the gene name means "Cytokinesis, Apoptosis, RNA-associated". Our review
  discusses the cytokinesis role but proposes no NEW term for it. The IMP evidence here is RNAi
  necessity, so it needs the participation test in CLAUDE.md before any NEW term.
- **SIZ1 (Arabidopsis), PMID:22253727, pollen tube guidance (IMP).** BC4GO and TAIR both
  annotate it; our review marks it MARK_AS_OVER_ANNOTATED, calling the guidance defect a downstream
  consequence of embryo-sac collapse. BC4GO's TAIR curator and TAIR's own GO curation may be the
  same person, so this is not necessarily two independent opinions.
- **Inconsistency within our own reviews, PMID:23144921, response to water deprivation (IEP).**
  Same paper, same kind of expression evidence: CYP79B2 and CYP71B15 are MARK_AS_OVER_ANNOTATED,
  MAM1 is KEEP_AS_NON_CORE.

Wrong-partner errors the GO rows avoided: for GRB2 (PMID:12359715), FEN1 (PMID:11430825) and
BCL2L1 (PMID:11060313), the GOA WITH/FROM names the partner Cusick says was actually shown (LAX
Q8IWV1, EP300 Q09472, MOAP1 Q96BY2), not the partner the PPI database curated.
