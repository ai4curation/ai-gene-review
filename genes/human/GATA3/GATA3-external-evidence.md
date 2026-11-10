# GATA3: selected original evidence beyond the publication cache

These selected observations come from original supplements or original article text. They are distinct from the text available in `publications/PMID_*.md`. Spreadsheet row numbers below are one-based Excel rows, including headers. Hashes identify the exact original files inspected; the selected cells make the target assignments inspectable without private workspace files. They do not claim that every experiment, image or supplement was read.

## ECM1 receptor binding and GATA3 transcriptional regulation

[PMID:21217760](https://pubmed.ncbi.nlm.nih.gov/21217760/), [original article](https://doi.org/10.1038/ni.1983), and [publisher supplement](https://static-content.springer.com/esm/art%3A10.1038%2Fni.1983/MediaObjects/41590_2011_BFni1983_MOESM6_ESM.pdf).

The original supplement is 646,888 bytes, SHA-256 `ec4fb24da2a189cc170094aa68bd425025903d8f0a2da84fd28ec5989c30f8b6`. Supplementary Figure 10 on PDF page 11 separates nuclear GATA3 regulation of Ecm1 from secreted ECM1 interaction with the IL-2 receptor. That page's diagram and caption were inspected; the other nine supplemental legends were read as text. This is external original evidence, not content claimed to be in the abstract-only cache.

Selected original main text was accessible through the [author-uploaded article](https://www.researchgate.net/publication/49739513_ECM1_controls_TH2_cell_egress_from_lymph_nodes_through_re-expression_of_S1P1). Figure 2 describes GATA3 regulation of Ecm1; Figure 8d and its caption identify ECM1 as the protein tested with CD25, CD122 and CD132 in HEK293T cells, with CD122 association reported. The selected IP Methods were read. The publisher main page was paywalled and the direct local author-page request failed; this was a selected public text rendering, not a complete main-paper or main-image inspection.

The review's short literal abstract anchor is in the IL-2-receptor-binding row. The source distinction supports a query about the traced GATA3 annotation; it does not establish that GATA3 can never bind any receptor.

## Positive target pairs in original interaction tables

[PMID:25910212](https://pubmed.ncbi.nlm.nih.gov/25910212/): [original Table S3 workbook](https://www.ebi.ac.uk/biostudies/files/S-EPMC4441215/NIHMS680142-supplement-11.xlsx), 281,392 bytes, SHA-256 `c401dffd03b173062a91ecb9dfcbd424319582d70498cef269bbce0af13492ec`.

Selected factual cells from sheet `Table S3A`:

| Excel row | Tested allele | Gene ID | Partner | Partner gene ID | Y2H score |
|---|---|---:|---|---:|---:|
| 42 | ACTN2, 88_0 | 88 | GATA3 | 2625 | 1 |
| 70 | ACTN2, p.Q9R | 88 | GATA3 | 2625 | 0 |
| 98 | ACTN2, p.D475N | 88 | GATA3 | 2625 | 0 |
| 126 | ACTN2, p.M604V | 88 | GATA3 | 2625 | 0 |

The table supports the positive wild-type screen pair and allele-dependent assay differences. It does not establish an endogenous ACTN2-dependent function for GATA3 or equivalent behavior of modern GATA3 products. The functional-information judgment on generic protein binding preserves this measured interaction.

[PMID:32814053](https://pubmed.ncbi.nlm.nih.gov/32814053/): [original institutional supplement archive](https://edoc.mdc-berlin.de/id/eprint/19322/2/19322suppl.zip), 17,880,130 bytes, SHA-256 `51d6e36f2c7befb3ef518dc916e67306fb42e69885d4cf314d053e1507d233f8`. Its workbook `1-s2.0-S2211124720310354-mmc3.xlsx` is 1,828,047 bytes, SHA-256 `8022031dc6c71bd15b149e2768fe510c45057f3921921b2c658ced53cb77f8bb`.

Selected factual cells from sheet `NN1.0`:

| Excel row | Gene A | Gene ID A | Gene B | Gene ID B |
|---|---|---:|---|---:|
| 3715 | CHAT | 1103 | GATA3 | 2625 |
| 3716 | EGR2 | 1959 | GATA3 | 2625 |
| 3717 | FGFR3 | 2261 | GATA3 | 2625 |

The same pairs occur in `NN1.0ext`, rows 8110–8112. These are target-specific positive screen records. They do not by themselves establish a native signaling complex, a catalytic role for GATA3, binding to an assembled receptor complex or target-specific validation in every orthogonal assay described by the paper.

## GATA3 constructs and sequence-specific DNA recognition

[PMID:28473536](https://pubmed.ncbi.nlm.nih.gov/28473536/): [original supplementary tables S1–S6](https://www.ebi.ac.uk/biostudies/files/S-EPMC8009048/NIHMS1670407-supplement-Supplemental_tables_S1-6.xlsx), 5,712,247 bytes, SHA-256 `4994eb7b3e33eb301541cf7d53d8be0936d5bdb6b504f5d63719e133f40004a6`.

`S1 sequence information`, Excel row 295, identifies GATA3 and supplies two construct sequences. After removal of the table's terminal stop marker, the full-length sequence is exactly the 444-residue P23771-2 sequence. The extended DNA-binding construct is 144 residues and exactly matches P23771-1 residues 238–381; it lacks the extra glutamate present in product 2. These comparisons use the complete sequences preserved in [the source-evidence file](GATA3-source-evidence.yaml).

`S2 PWM models`, rows 8198, 8203, 8208 and 8213, provide GATA3 full-length methylated/unmethylated model records. S3 rows 36 and 549 record the full-length methylation classification. The table's final/bisulfite classification and methyl-SELEX classification are kept distinct; no equality of the two natural products is inferred.

Selected original Methods describe tagged recombinant human transcription-factor constructs expressed in bacteria, purification, double-stranded selection libraries and enrichment-based motif inference. These target records support sequence-specific DNA recognition. They do not independently establish promoter specificity, precise affinity constants, endogenous product-specific functions or a GATA3 crystal structure. Promoter specificity and transcriptional activity in the review use separate primary evidence.

## Development of cochlear wiring

[PMID:23426694](https://pubmed.ncbi.nlm.nih.gov/23426694/) · [original PMC article](https://pmc.ncbi.nlm.nih.gov/articles/PMC3613247/).
Original HTML: 226,533 bytes; SHA-256 `2be9fec2f6025db6862b9a057690238aec68c00f16d346826fd6f2c378e5c55c`.

Mouse Bhlhb5-Cre deletion after auditory-neuron specification disrupts peripheral radial bundles, neurite-growth timing and developmental transcription. Gross cochlear size/shape and initial auditory identity remain largely preserved. Inspected Methods and Results, including textual Figures 2–7 captions, establish developmental work within the cochlea; they do not demonstrate initial organ-specification failure. Images and full supplements were not independently inspected. The normal cache remains partial.

## Construction of the nascent nephric duct

[PMID:16319112](https://pubmed.ncbi.nlm.nih.gov/16319112/) · [publisher DOI](https://doi.org/10.1242/dev.02184) · [author-uploaded original](https://www.researchgate.net/publication/7450103_Pax_28-regulated_Gata_3_expression_is_necessary_for_morphogenesis_and_guidance_of_the_nephric_duct_in_the_developing_kidney).

The author-indexed original Methods, ectopic-duct Results, Figure 6 caption and Discussion describe mouse germline exon-4 deletion. During E9.0–9.5, multiple disorganized E-cadherin/GFP-positive structures replace one organized nascent tube. The authors favor disturbed tubulogenesis/proliferation with specification markers retained. The normal cache remains abstract-only. Local HTML/PDF attempts failed; indexed original text was readable. Figure images and all later budding assays were not independently inspected.
