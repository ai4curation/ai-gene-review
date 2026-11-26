# GIPC3 manual evidence and species boundaries

## HuRI source pairs

[PMID:32296183](https://pubmed.ncbi.nlm.nih.gov/32296183/), HuRI.psi SHA256: `d6e8185519d18ce18cfa66f5eab66ecb1e711113f0b62810e0a145dd33a9ee12`.

| Incoming partner | Source partner and clone | Original line numbers | Screen |
| --- | --- | --- | --- |
| Q96JF0-2, ST6GAL2 | Q96JF0-2; ORF 2832 | 22754, 62390, 141011 | 3 |
| Q9HB19, PLEKHA2 | A8K727; ORF 100066365 | 89911, 113090, 149815 | 2 |

ORF 54149 has partial DNA identification. Three method projections (MI:0397/MI:1112/MI:1356) per pair are not independent experiments. Official [ST6GAL2](https://www.uniprot.org/uniprotkb/Q96JF0/entry) and [PLEKHA2](https://www.uniprot.org/uniprotkb/Q9HB19/entry) cross-references resolve identifiers without proving full clone equivalence.

## MYO6 binding and orthology

Mouse constructs bind MYO6 in purified pulldowns and MYO18A in cellular assays. Simultaneous force coupling remains a model. Results report HA tagging; Methods specify MBP.

Original locators: [final article](https://pmc.ncbi.nlm.nih.gov/articles/PMC10234109/), MYO6 Results, purification/pulldown Methods, Figure 3 and supplementary Table S1 (page 9). Other supplementary panels were not inspected.

The [official Ensembl orthology response](https://rest.ensembl.org/homology/id/human/ENSG00000179855?target_species=mus_musculus;type=orthologues;sequence=none;content-type=application/json) identifies a one-to-one relationship. The versionless Ensembl identifiers map to the following versioned official UniProt cross-references.

| Product | Ensembl gene | Ensembl protein |
| --- | --- | --- |
| Human Q8TF64 | ENSG00000179855.10 | ENSP00000493901.2 |
| Mouse Q8R5M0 | ENSMUSG00000034872.7 | ENSMUSP00000049236.6 |

The retained [PTHR12259 member table](../../../interpro/panther/PTHR12259/PTHR12259-entries.csv) places human Q8TF64 and mouse Q8R5M0 in PTHR12259:SF2, distinct from the GIPC1 and GIPC2 subfamilies. Its mouse length is 297 residues, agreeing with the full-length mouse construct in Table S1. This classification corroborates the independent orthology call; it is not an experimental activity annotation.

This verifies orthology, not direct human activity. The proposed [GO:0070853](https://www.ebi.ac.uk/QuickGO/term/GO:0070853) ISO annotation requires prior mouse IPI curation. The retained donor snapshot has ND roots only. The [GO annotation guide](https://pmc.ncbi.nlm.nih.gov/articles/PMC3706743/), WITH/FROM section, calls for an experimental donor annotation; changing ISO to ISS would not resolve that omission. The current [GORULE:0000038](https://github.com/geneontology/go-site/blob/master/metadata/rules/gorule-0000038.md) is proposed, report-only and soft, not a hard validation gate. The prerequisite here is a conservative curation ordering.

Mouse localization is not directly established in human hair cells. Broader myosin binding would add no independent GO coverage.

## Human genetics and products

[PMID:21326233](https://pmc.ncbi.nlm.nih.gov/articles/PMC3105340/) combines mouse auditory phenotypes and rescue with human recessive variants. Its trafficking discussion is mechanistic background, not a direct binding assay. The unresolved 37-kDa mouse band does not define a human isoform.

[PMID:21660509](https://pmc.ncbi.nlm.nih.gov/articles/PMC3303183/) reports seven human variant families, six with LOD scores above 3. Original Methods and Table 1 concern clinical evaluation, linkage and sequencing; no construct assay was performed. Mouse and GIPC1 mechanisms in its Discussion are cited background.

[PMID:11836571](https://doi.org/10.3892/ijo.20.3.577) remains abstract-only: human fetal-lung cloning and RNA expression establish identity, while related-protein signaling examples do not establish GIPC3 pathways. The official human record specifies one 312-residue product; its AAC24304.1 warning concerns a separate erroneous genomic prediction. Engineered mouse deletions and patient variants are not additional natural products.

## Retained donor annotation snapshot

The [official QuickGO query](https://www.ebi.ac.uk/QuickGO/services/annotation/search?geneProductId=Q8R5M0&taxonId=10090&limit=200), captured on 2026-11-05 at 12:01:50 UTC, returned the two records below. The exact response objects are retained under `donor_annotation_snapshot` in the source archive. This dated snapshot is not a new mouse review or an assertion that the literature lacks experimental evidence.

| Product | GO term | Evidence | Reference | Assigned by | Annotation date |
| --- | --- | --- | --- | --- | --- |
| Q8R5M0 | GO:0003674 | ND | GO_REF:0000015 | MGI | 2010-02-09 |
| Q8R5M0 | GO:0008150 | ND | GO_REF:0000015 | MGI | 2010-02-09 |
