# NOL4 HTH_NOL4 region: computed provenance tables, part 3 (iteration 3)

Continues `nol4_hth_analysis_tables.md` and `nol4_hth_analysis_tables_part2.md`.
All values computed in this run from the QuickGO annotation API and the UniProt
REST API. Figures: `plot_4.png` (evidence-code distribution and cohort keyword
split), `plot_5.png` (four-bar discriminating test).

## Table 14. Resource accessibility check (RNA-binding proteome databases)

| Resource | URL | Result |
|---|---|---|
| RBP2GO | https://rbp2go.dkfz.de/ | HTTP 200, `text/html`, 249,948 bytes. Shiny front end, no documented per-protein JSON endpoint. **Not queryable programmatically.** |
| RBPbase | https://rbpbase.shiny.embl.de/ | HTTP 200, `text/html`, 36,131 bytes. Shiny front end. **Not queryable programmatically.** |
| EuRBPDB | http://EuRBPDB.syshospital.org/ | `ConnectionError`, connection refused. **Not reachable.** |

Consequence: whether NOL4 appears in any mRNA-interactome-capture dataset is
**unknown**, and is reported as a knowledge gap. It is not reported as a negative.

## Table 15. Evidence codes for GO:0003723 (RNA binding) in human

QuickGO, `goUsage=exact`, `taxonId=9606`, `geneProductType=protein`.
Total annotations: **7,547**.

| Evidence | ECO | Annotations | Share |
|---|---|---|---|
| IEA, electronic | ECO:0007669 | 2,397 | 31.76% |
| IDA, direct assay | ECO:0000314 | 1,846 | 24.46% |
| IBA, phylogenetic | ECO:0000318 | 226 | 2.99% |
| **TAS, traceable author statement** | **ECO:0000304** | **117** | **1.55%** |
| IPI | ECO:0000353 | 34 | 0.45% |
| ISS | ECO:0000250 | 16 | 0.21% |
| ISO | ECO:0000266 | 0 | 0.00% |

NOL4's annotation sits in the 1.55% TAS slice. Of the 117 TAS annotations, **102
were assigned by PINC**, a single legacy batch keyed to papers published between
1986 and 2000. PINC contributes 11,555 human GO annotations overall.

## Table 16. NOL4 benchmarked against its own annotation cohort

All 102 PINC / TAS / GO:0003723 human proteins, queried in batched UniProt
requests for `keyword` and `xref_interpro`.

| Criterion | Proteins | Share |
|---|---|---|
| RNA-related UniProt keyword (RNA-binding, Ribosomal protein, Ribonucleoprotein, mRNA processing, mRNA splicing, Translation regulation, Nuclease, Helicase, ...) | 94 | 92.2% |
| Canonical RNA-binding domain by InterPro accession (RRM, KH, dsRBD, CCHC knuckle, Pumilio, La, S1, cold-shock, LSM, ...) | 49 | 48.0% |
| **At least one of the two** | **96** | **94.1%** |
| **Neither** | **6** | **5.9%** |

The residual six:

| Accession | Symbol | Cited reference | Independent RNA link |
|---|---|---|---|
| P52594 | AGFG1 | PMID:7634337 | keyword `mRNA transport` |
| P62495 | ETF1 | PMID:7990965 | keywords `Nonsense-mediated mRNA decay`, `Protein biosynthesis` |
| O00442 | RTCA | PMID:9184239 | RNA 3'-terminal phosphate cyclase, `Ligase` |
| Q15381 | YRRM | PMID:9598316 | entry with 0 InterPro matches and 0 keywords |
| Q16600 | ZNF239 | PMID:9121460 | none; keywords are `DNA-binding`, `Zinc-finger`, `Transcription` |
| **O94818** | **NOL4** | **PMID:9813152** | **none** |

NOL4's complete keyword set: `Alternative splicing`, `Nucleus`,
`Proteomics identification`, `Reference proteome`.
NOL4's complete InterPro set: IPR039788 (NOL4 family), IPR056549 (Nucleolar
protein 4, helical domain). Neither entry carries a GO term.

## Table 17. GO decision table for O94818

| GO term | Aspect | Current evidence | Supported by this analysis | Lead action |
|---|---|---|---|---|
| GO:0003723 RNA binding | MF | TAS, ECO:0000304, PMID:9813152, assigned by PINC | **No.** Source paper has no binding assay; no RBD; no RNA-related keyword; no structural relative; ortholog is ND at MGI | **Remove** (curator verification required) |
| GO:0003677 DNA binding | MF | not annotated | **No.** 0/3 geometry, Foldseek E > 2.9, no CATH/SUPERFAMILY/PROSITE HTH, IPR056549 carries no GO term | **Do not add** |
| GO:0005730 nucleolus | CC | TAS PMID:9813152 + IEA | **Yes.** Deletion mapping in COS-7 localises residues 456-485 (canonical numbering) to the nucleolus | Retain |
| GO:0005654 nucleoplasm | CC | IDA (HPA) | Yes | Retain |
| GO:0003712 transcription coregulator activity | MF | not annotated | Partial, from PMID:25366156 reporter assays in Schneider's Line 2 cells (mouse proteins, insect cells) | Lead only, insufficient for direct assertion |
| GO:0006357 regulation of transcription by RNA polymerase II | BP | not annotated | Partial, same source | Lead only |
| GO:0003674 molecular_function ND | MF | mouse ortholog carries this (MGI, GO_REF:0000015) | Consistent with this analysis | Consider for human after GO:0003723 removal |
