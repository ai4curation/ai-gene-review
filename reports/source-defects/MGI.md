# Source-record defects for MGI

4 open defect(s), generated from `source_defects` blocks in this repository's reviews. Do not edit by hand.

## 1. WRONG_GENE_PRODUCT (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:P54320!148349945
- **Subject:** UniProtKB:P15502
- **Field:** DB_Object_ID
- **Change:** check UniProtKB:P54320 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/human/ELN/ELN-ai-review.yaml`

The current mouse Eln GO:0071953 IDA donor record cites PMID:17099216. Its recovered Methods and Results use bovine tropoelastin-EGFP in mouse MEF 3T3 cells and state that parental cells lack tropoelastin expression. Please check whether the donor annotation is intended to describe the expressed bovine construct or has separate evidence for endogenous mouse Eln. No replacement accession is asserted. Independent human elastic-fiber localization remains supported; this query concerns the source gene-product attribution, not the location itself.

- **Evidence reference:** PMID:17099216

## 2. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** MGI:MGI:1924104
- **Subject:** UniProtKB:Q99527
- **Field:** GO_ID
- **Change:** check GO:0030284 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/human/GPER1/GPER1-ai-review.yaml`

Human GPER1 receives GO:0030284 nuclear estrogen receptor activity by Ensembl Compara projection from mouse Gper1 (MGI:1924104, Q8BMP4). Gper1 is a seven-transmembrane GPCR without a DNA-binding domain, so a nuclear receptor (DNA-binding transcription factor) activity is the wrong term class; GO:0038054 G protein-coupled estrogen receptor activity is the appropriate replacement. The mouse source annotation was not inspected directly; please check it and repoint.

> Belongs to the G protein-coupled receptor 1 family.
> — file:human/GPER1/GPER1-uniprot.txt

## 3. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:O88559
- **Subject:** UniProtKB:O00255
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0043565
- **Recorded in:** `genes/human/MEN1/MEN1-ai-review.yaml`

Mouse menin (MGI:1316736, O88559) carries GO:0043565 sequence-specific DNA binding, IDA, PMID:20956546. That paper uses ChIP to show the menin-trithorax complex across the Gata3 locus; it does not test DNA sequence specificity. Menin binds DNA in a sequence-independent manner (PMID:15331604). The annotation is projected to human by Ensembl Compara. Suggest withdrawing it; chromatin binding (GO:0003682) or transcription coactivator activity (GO:0003713) describes the finding.

> TrxG complex associated with the TrxG component Menin binds to the whole GATA3 gene locus
> — PMID:20956546

> These results indicate that menin not only binds to DNA in a non-sequence specific fashion
> — PMID:15331604

## 4. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:O88559
- **Subject:** UniProtKB:O00255
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0140608
- **Recorded in:** `genes/human/MEN1/MEN1-ai-review.yaml`

Mouse menin (MGI:1316736, O88559) carries GO:0140608 cysteine-type endopeptidase activator activity, IDA, PMID:14688275. The paper shows that menin loss reduces procaspase 8 expression and complementation restores it; this is an effect on caspase 8 expression, not direct activation of the protease. Projected to human by Ensembl Compara. Suggest withdrawing the row.

> loss of menin reduces the expression of procaspase 8
> — PMID:14688275
