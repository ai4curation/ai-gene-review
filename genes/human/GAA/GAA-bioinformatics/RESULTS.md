# GAA selected original proteomics evidence

These selected data preserve the observations used for the membrane and extracellular-vesicle assessments. They are transcribed from retained original sources, not from GO annotation rows. Only the identified target fields are reproduced; the complete tables are not included. The publication caches remain unchanged.

## Human placental lysosomal membranes: PMID17897319

Source: [original publisher Table 1](https://onlinelibrary.wiley.com/doi/10.1111/j.1600-0854.2007.00643.x), row “Lysosomal α-glucosidase,” IPI00293088. The retained selected publisher text has SHA256 `468f84658cc4be1295ac55638850feae57134327714c62b4774901d5695190a8`; its table row is at captured line L259. The direct HTTP attempt failed, while the separately retained publisher-rendered text supplied this row.

| Original accession | Peptides | Coverage (%) | Spectral counts | R_SC | Adjusted P |
| --- | --- | --- | --- | --- | --- |
| IPI00293088 | 24 | 36.2 | 112 | 1.80 | 1E-04 |

The study enriched human placental lysosomal membranes against a dense-pool reference and retained peripheral membrane-associated proteins. These data support fraction association, without establishing integral topology. The original row also lists a historical length of 957 and one predicted transmembrane segment; neither value defines a current natural GAA isoform or proves membrane insertion.

## Urinary exosome dataset: PMID19056867

Source: [original NHLBI expanded table](https://esbl.nhlbi.nih.gov/Databases/UrinaryExosomes/). The retained HTML has SHA256 `e62dbbf0a132cea7b6650ba618f4f257370a56cfbaf42b1949ed02cd28d1cb8c`. The two target records are HTML `tr` indices 441 and 442 (zero-based over all rows); both identify acid alpha-glucosidase preproprotein. The source legend maps reference 1 to PMID15326289 and reference 2 to PMID19056867.

| Original accession | Gene | Peptides | Original reference column |
| --- | --- | --- | --- |
| NP_000143 | GAA | 4 | 1,2 |
| NP_001073272 | GAA | 5 | 2 |

These are target identifications in the preparation. The database’s GO labels are imported annotations, not additional experiments. Historical accessions and protein-group identifications do not resolve current splice products, intravesicular topology, secretion mechanism or an EV-specific function.

## EPS-urine exosome dataset: PMID23533145

Sources: [original main article](https://pmc.ncbi.nlm.nih.gov/articles/PMC3773505/) and [Supplemental Table 2 workbook](https://www.ebi.ac.uk/biostudies/files/S-EPMC3773505/NIHMS502285-supplement-Supplemental_Table_2.xlsx). The retained workbook SHA256 is `6c76b1cd34e709839d8353a5c1584118f0a0c99d8edbfaf361bd1f275f896a70`. Worksheet `SI Table 2`, Excel row 440, supplies the selected fields below. Counts are the original unique-peptide columns for PCa_1, PCa_2, NC_1 and NC_2.

| Protein ID | Gene | PCa_1 | PCa_2 | NC_1 | NC_2 |
| --- | --- | --- | --- | --- | --- |
| P10253 | GAA | 15 | 14 | 29 | 28 |

The source used pools of 12 prostate-cancer and 12 biopsy-negative samples, duplicate mass-spectrometry measurements, differential ultracentrifugation with a DTT/sucrose wash, and identification FDR below 1%. The authors discuss soluble material and possible contaminating proteins. Positive fraction membership supports non-core retention, while purity, vesicle topology and physiological function remain separate questions. The processed-form names in the protein-group cell are not form-specific peptide localization experiments.

## Independent urinary EV immunocapture: PMID27805059

Source: [original article and Table 2](https://pmc.ncbi.nlm.nih.gov/articles/PMC5090863/), DOI10.1038/srep36331. Retained original BioC JSON SHA256 `e05dfb7b61846315b91a6b25d7723dd0a0d5380aef0264862fed4d8e69da7357`; Table 2, GAA row. The newly acquired native publication cache is full XML text.

| Gene | Accession | Coverage range (%) |
| --- | --- | --- |
| GAA | P10253 | 23–39 |

Healthy-human urinary vesicles were immunocaptured with CD9, CD63 and CD81 antibodies. The paper reports 30–100 nm membrane-bounded structures by TEM and uses short detergent-free on-bead digestion. Its 1% FDR, unique-peptide, replicate and above-control-coverage criteria retained 49 proteins across all three captures, including GAA. Here “extraexosomal” means the outer vesicle surface, not a nonvesicular fraction. Carryover and possible aggregates remain limitations. These observations strengthen non-core EV association without establishing integral topology, a universal pool or a physiological EV function. Images, raw spectra and complete supplementary control tables were not independently assessed. The separate historical B7Z5V6 row is not used to define a current natural GAA product.

## Reading and preservation scope

The initial three selected source records and the urinary-table legend were independently checked before the initial review. This portable record makes those observations inspectable without replacing abstract-only caches with external text. The follow-up adds only the qualified native acquisition of PMID27805059. No reanalysis of raw spectra, proteome-wide inference or new experiment is claimed. The full earlier review, journal and all 55 inherited quotation associations remain in the existing inherited archive. New review snippets quote only the selected data rows above.
