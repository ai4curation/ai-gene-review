# GIPC3 manual evidence and species boundaries

## HuRI source pairs

[PMID:32296183](https://pubmed.ncbi.nlm.nih.gov/32296183/), HuRI.psi SHA256: `d6e8185519d18ce18cfa66f5eab66ecb1e711113f0b62810e0a145dd33a9ee12`.

| Incoming partner | Source partner and clone | Original line numbers | Screen |
| --- | --- | --- | --- |
| Q96JF0-2, ST6GAL2 | Q96JF0-2; ORF 2832 | 22754, 62390, 141011 | 3 |
| Q9HB19, PLEKHA2 | A8K727; ORF 100066365 | 89911, 113090, 149815 | 2 |

ORF 54149 has partial DNA identification. Three method projections (MI:0397/MI:1112/MI:1356) per pair are not independent experiments. Official [ST6GAL2](https://www.uniprot.org/uniprotkb/Q96JF0/entry) and [PLEKHA2](https://www.uniprot.org/uniprotkb/Q9HB19/entry) cross-references resolve identifiers without proving full clone equivalence.

## MYO6 binding and orthology

Table S1 identifies mouse GIPC3 constructs; HeLa is the host. Purified pulldown establishes MYO6 recognition; MYO18A mapping uses cellular NanoSPD/deletion assays. Simultaneous bridging and force transmission remain models. Results describe an HA tag, whereas purified-protein Methods specify MBP; that discrepancy is retained.

Original locators: [final article](https://pmc.ncbi.nlm.nih.gov/articles/PMC10234109/), MYO6 Results, purification/pulldown Methods, Figure 3 and supplementary Table S1 (page 9). Other supplementary panels were not inspected.

The [official Ensembl orthology response](https://rest.ensembl.org/homology/id/human/ENSG00000179855?target_species=mus_musculus;type=orthologues;sequence=none;content-type=application/json) identifies a one-to-one relationship. The versionless Ensembl identifiers map to the following versioned official UniProt cross-references.

| Product | Ensembl gene | Ensembl protein |
| --- | --- | --- |
| Human Q8TF64 | ENSG00000179855.10 | ENSP00000493901.2 |
| Mouse Q8R5M0 | ENSMUSG00000034872.7 | ENSMUSP00000049236.6 |

This is the orthology basis for ISO; it is separate from direct biochemical evidence and does not establish a human assay. The current mouse GO snapshot contains ND roots, so the proposal uses the original experiment rather than an existing donor GO annotation. [GO:0070853](https://www.ebi.ac.uk/QuickGO/term/GO:0070853) denotes myosin VI binding. No separate adaptor, biological-process or localization annotation is proposed.

## Human genetics and products

[PMID:21326233](https://pmc.ncbi.nlm.nih.gov/articles/PMC3105340/) combines mouse auditory phenotypes and rescue with human recessive variants. Its trafficking discussion is mechanistic background, not a direct binding assay. The unresolved 37-kDa mouse band does not define a human isoform.

[PMID:21660509](https://pmc.ncbi.nlm.nih.gov/articles/PMC3303183/) reports seven human variant families, six with LOD scores above 3. Original Methods and Table 1 concern clinical evaluation, linkage and sequencing; no construct assay was performed. Mouse and GIPC1 mechanisms in its Discussion are cited background.

[PMID:11836571](https://doi.org/10.3892/ijo.20.3.577) remains abstract-only: human fetal-lung cloning and RNA expression establish identity, while related-protein signaling examples do not establish GIPC3 pathways. The official human record specifies one 312-residue product. Engineered mouse deletions and patient variants are not additional natural products.
