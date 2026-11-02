# ECHS1 source-record replay results

The unchanged extractor was run on the three bundled source inputs. It selected five of 87 IntAct records, six of 15 MINT records and two literal P30084/ECHS1 workbook rows. The full selected fields remain in [records.json](records.json). These are curated database records and measured source-table entries, not additional experimental replicates.

## Interaction identities

| Database | Physical line | Participant A | Participant B | Publication | Interaction identifier |
| --- | ---: | --- | --- | --- | --- |
| intact | 35 | uniprotkb:Q5S007 | uniprotkb:P30084 | [PMID:31046837](https://pubmed.ncbi.nlm.nih.gov/31046837/) | intact:EBI-21360986; imex:IM-26684-48 |
| intact | 36 | uniprotkb:Q5S007 | uniprotkb:P30084 | [PMID:31046837](https://pubmed.ncbi.nlm.nih.gov/31046837/) | intact:EBI-21364596; imex:IM-26684-50 |
| intact | 57 | uniprotkb:Q38SD2 | uniprotkb:P30084 | [PMID:24947832](https://pubmed.ncbi.nlm.nih.gov/24947832/) | intact:EBI-9659265; imex:IM-22653-21 |
| intact | 58 | uniprotkb:P30084 | uniprotkb:Q5S007 | [PMID:24947832](https://pubmed.ncbi.nlm.nih.gov/24947832/) | intact:EBI-9659799; imex:IM-22653-62 |
| intact | 64 | uniprotkb:Q5S007 | uniprotkb:P30084 | [PMID:24510904](https://pubmed.ncbi.nlm.nih.gov/24510904/) | intact:EBI-9247290; imex:IM-22223-39 |
| mint | 5 | uniprotkb:P30084 | uniprotkb:P40763 | [PMID:23416296](https://pubmed.ncbi.nlm.nih.gov/23416296/) | intact:EBI-8427285; mint:MINT-8413534 |
| mint | 6 | uniprotkb:P40763 | uniprotkb:P30084 | [PMID:23416296](https://pubmed.ncbi.nlm.nih.gov/23416296/) | intact:EBI-8427327; mint:MINT-8413549 |
| mint | 7 | uniprotkb:P30084 | uniprotkb:P42227 | [PMID:23416296](https://pubmed.ncbi.nlm.nih.gov/23416296/) | intact:EBI-8427418; mint:MINT-8413567 |
| mint | 8 | uniprotkb:P30084 | uniprotkb:P42227 | [PMID:23416296](https://pubmed.ncbi.nlm.nih.gov/23416296/) | intact:EBI-8427453; mint:MINT-8413580 |
| mint | 9 | uniprotkb:P30084 | uniprotkb:P42227 | [PMID:23416296](https://pubmed.ncbi.nlm.nih.gov/23416296/) | intact:EBI-8427512; mint:MINT-8413597 |
| mint | 10 | uniprotkb:P30084 | uniprotkb:P40763 | [PMID:23416296](https://pubmed.ncbi.nlm.nih.gov/23416296/) | intact:EBI-8427571; mint:MINT-8413615 |

The LRRK2 assertion joins Q5S007. The additional LRRK1/Q38SD2 record from PMID:24947832 is retained as source context and is not substituted for that assertion. Human STAT3/P40763 and mouse Stat3/P42227 are distinct participants; a human assay host does not change a mouse construct into a human protein. Complete MITAB fields preserve participant and host species, methods, features and source identifiers. Positive partner-class binding does not establish ECHS1 phosphorylation, transcription-factor activity or an unmeasured native pathway.

## MitoCoP identities

| Worksheet | Physical row | Protein group | Accession | Gene |
| --- | ---: | ---: | --- | --- |
| (A) All protein groups | 337 | 4415 | P30084 | ECHS1 |
| (B) MitoCoP (1,134 genes) | 305 | 4415 | P30084 | ECHS1 |

The selected workbook fields identify ECHS1 as mitochondrial in the study inventory. They do not independently establish matrix topology or a specific processed form. [PMID:34800366](https://pubmed.ncbi.nlm.nih.gov/34800366/) and the [evidence guide](../ECHS1-source-guide.md) supply the experimental context.

The archive extraction and unchanged `reproduce.py` generated records byte-identical to the committed file. [README.md](README.md) gives the offline commands; [source-manifest.json](source-manifest.json) and [source-receipts.json](source-receipts.json) bind source bytes and acquisition URLs.
