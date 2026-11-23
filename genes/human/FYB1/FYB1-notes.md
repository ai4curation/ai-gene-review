# FYB1 biological notes

## 2026-11-01 — adaptor mechanism and experimental scope

FYB1/ADAP organizes intracellular signaling complexes rather than catalyzing a reaction. Phosphorylated FYB recruits FYN-T and SLP-76 SH2 domains ([PMID:10409671](https://pubmed.ncbi.nlm.nih.gov/10409671/), “recruitment of FYN-T and SLP-76 SH2 domain binding.”; [PMID:10570256](https://pubmed.ncbi.nlm.nih.gov/10570256/)). FYB peptides also bind the tested FYN/NCK1 SH3 domains in the source-specific peptide array ([PMID:17474147](https://pubmed.ncbi.nlm.nih.gov/17474147/), curated Table S2 records). This ligand-to-domain orientation differs from the secondary ADAP SH3c-domain interaction with a SKAP55 motif ([PMID:16461356](https://pubmed.ncbi.nlm.nih.gov/16461356/)).

Human FYB association with Ena/VASP and SLP-76/Nck/WASP machinery supports an actin-linked adaptor role ([PMID:10747096](https://pubmed.ncbi.nlm.nih.gov/10747096/), Figures 3–9). The later human Jurkat/primary T-cell studies connect ADAP/SKAP-dependent recruitment of Rap1-associated machinery to inside-out adhesion ([PMID:16980616](https://pubmed.ncbi.nlm.nih.gov/16980616/), Figures 3–7; [PMID:17403904](https://pmc.ncbi.nlm.nih.gov/articles/PMC1900018/), Figures 4 and 7). Recruitment is distinct from Rap1 nucleotide loading, and SKAP-mediated linkage does not establish direct FYB–RIAM or FYB–Rap1 contact. The earlier FYN/SLP-76 studies are not cited as Rap1 experiments.

The outside-in evidence is separate: original mouse ADAP platelet experiments show defective contact growth/spreading under shear even with direct integrin activation ([PMID:19996090](https://pmc.ncbi.nlm.nih.gov/articles/PMC2844019/), Figure 3F–G). Human cell results and murine platelet results are not interchangeable. Authentic original abstracts additionally support binding-dependent stabilization of SKAP55 in human Jurkat cells ([PMID:15849195](https://pubmed.ncbi.nlm.nih.gov/15849195/)); its quantitative protection result is not extended to SKAP2.

ADAP hSH3 regions bind acidic phospholipids, including phosphatidylserine and PI(4,5)P2-containing membranes ([PMID:15843031](https://pubmed.ncbi.nlm.nih.gov/15843031/); [PMID:16831444](https://pubmed.ncbi.nlm.nih.gov/16831444/)). These authentic abstracts establish named ligand classes, not an exclusive preference, equal affinity or identical behavior of all three documented protein products. Natural sequences of 783, 829 and 839 residues remain distinct from historical short/long proteins, mutants, tags and isolated domains.

Two nuclear annotations and the exact FYB1 comparison in the FYB2/ARAP paper remain unresolved. These are explicit access/assay gaps, not negative-localization or wrong-gene findings. Product-specific functions and any conditional nuclear pool remain experimental questions. The [source guide](FYB1-source-guide.md) summarizes the selected reading, while the [compact source evidence](FYB1-source-evidence.yaml) preserves the original contexts, actual native joins, products, source access and exact quotation locators. Current judgments remain in the review YAML.

<details>
<summary>Earlier dated journal, retained verbatim as historical provenance</summary>

The following records describe the proposal, acquisition and validation stages before this amendment. Their planning statements and original action totals are historical; the current scientific account above and current review YAML govern. The earlier grouped Rap1 citation is superseded by the separated source attribution above.

```text
# FYB1 biological notes

## 2026-11-01 — signaling organization and source-specific boundaries

FYB1/ADAP is a nonenzymatic intracellular adaptor. Human association and perturbation studies link FYN/SLP-76, SKAP proteins and actin regulators; ADAP/SKAP-dependent membrane recruitment of Rap1 machinery is distinct from Rap1 activation itself (PMID:10409671, PMID:10747096, PMID:16980616, PMID:17403904). The receptor-binding annotation is best represented by signaling adaptor activity, without inventing a direct receptor contact.

The ligand-initiated integrin term needs outside-in evidence. Selected original mouse ADAP platelet experiments under shear supply that evidence, independently of TCR-driven inside-out adhesion (PMID:19996090). The actual ancestral donor MGI:3576625 is mouse Pram1, whose distinct neutrophil study also assays outside-in responses (PMID:15572693). The valid phylogenetic node and each literal donor remain intact.

Phospholipid binding is supported by authentic ADAP hSH3 abstracts and exact InterPro target mapping (PMID:15843031, PMID:16831444). The evidence does not establish an exclusive lipid preference or equal activity of all three documented FYB1 products. Noncanonical SKAP binding and altered conventional SH3 recognition are compatible findings.

Cytosolic, membrane-associated and actin-associated pools fit the central adaptor role. Specialized podocyte junctional localization remains non-core (PMID:21881001). Nuclear motifs, a PROSITE prediction and a database-derived table label do not establish a directly observed FYB nuclear pool; both nuclear assertions remain unresolved. The unrecovered FYB1 comparison in the FYB2/ARAP paper also remains unresolved (PMID:27335501), without alleging wrong-gene curation.

Positive interaction observations retain the tested peptide, tag, kinase and host scope. Curated IntAct target records are distinguished from original supplements actually read. Gene loss, phosphorylation or detection in a survey does not by itself imply an enzymatic activity or direct participation in every affected process. No new annotation is proposed.

This is a private scientific proposal. Native acquisition, source-cache title and quotation validation, history and scoped validation have not run for FYB1. The current lane remains reserved for completion of FUT8 and the tracker reconciliation.

## 2026-11-01 — genuine native acquisition and reconciliation

The preceding private-stage paragraph records the earlier planning state. FYB1 has now been acquired in the existing F lane after independently accepted FXYD2. All 35 original contexts reconcile to the genuine 16-column TSV and native seed. The 47 normal sources comprise 25 unchanged main files and 22 newly acquired files, including two Reactome summaries. Four immutable PAINT rows match the retained literal IBD placements. Three declared product sequences remain distinct.

The two approved excerpts now match exact native-cache bytes; PMID:10747096 retains the original words with the cache’s newline before “present.” The optional unavailable flag for PMID:25516138 is omitted because native full text is now available; its selected-reading assessment is unchanged. Question context is retained within the schema-supported question text. See the [source guide](FYB1-source-guide.md) and [compact evidence record](FYB1-review-evidence.json) for provenance. Authored application, history and validation are the next stage.

## Validation outcomes on 2026-11-01

Default schema, ontology, reference and best-practice validation passed with 14 advisories, all for retained generic protein-binding annotations. These positive associations remain non-core under the campaign policy. Strict GOA reconciliation confirms all 35 annotations. The native status audit computed DRAFT; the initial status was updated to that value and checked again. Three source-specific contexts remain UNDECIDED. The genuine CREATE history and private rendered preview passed. All 47 normal sources remain byte-identical to their acquisition record, and both short excerpts remain exact native-cache substrings. No new annotation was added.

```

</details>

## Amendment validation on 2026-11-01

Default schema, ontology, reference and best-practice checks pass with 10 advisories, all for the remaining positive generic-binding annotations. Strict GOA reconciliation preserves all 35 original contexts; the review additionally contains two manually supported process annotations, for 37 entries in total. The native status audit remains DRAFT. All nine supporting-text associations are exact cache substrings, and the three UNDECIDED contexts remain unchanged. Native EDIT history and the private rendered review pass. The 47 scientific sources, original CREATE history and GO term cache remain unchanged; the compact evidence archive is now YAML.
