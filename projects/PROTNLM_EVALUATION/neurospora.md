---
title: Neurospora ProtNLM evaluation
species: [NEUCR]
tags: [EVALUATION, ML_PREDICTIONS]
autolink_gene_symbols: false
---
# Neurospora ProtNLM evaluation

**Broad GO predictions can be biologically sound while the accompanying function paragraph assigns the wrong substrate or an impossible anatomical context.** This 20-gene Neurospora cohort includes a SUMO-conjugating E2 described as transferring ubiquitin and a fungal endocytic protein assigned a neuromuscular-junction role. Their general transferase and cytoplasm predictions remain supported. The separate judgments expose errors that a GO-only comparison would miss.

[20-gene cohort](neurospora-benchmark/review-cohort.csv) · [Original selected predictions](neurospora-benchmark/review-predictions.csv) · [Full 51-record census](neurospora-benchmark/inventory.csv) · [Claim provenance](neurospora-benchmark/claim-provenance.csv) · [Coverage audit](neurospora-benchmark/review-inventory.json) · [Source manifest](neurospora-benchmark/manifest.json) · [Parent project](../PROTNLM_EVALUATION.md)

## Cohort design

The published [ProtNLM2 accession list](https://ftp.ebi.ac.uk/pub/contrib/UniProt/ProtNLM2/List_of_UniProt_accessions_that_have_ProtNLM2_annotations.tsv) contains 51 Neurospora crassa strain 74-OR23-1A records (taxon 367110). All are currently TrEMBL entries, in contrast to the reviewed/Swiss-Prot pombe cohort. Exact accessions and current sequences are frozen alongside the original API responses.

The cohort was selected **after the predictions were available**. It comprises all 16 genes with GO/function output and four purposively chosen localization cases: a characterized MAP kinase kinase, an AP adaptor beta subunit, an FMO-family protein and a GNAT-family protein. All emitted localizations on those 20 genes are reviewed, including localizations accompanying a GO/function prediction. The other 31 records remain in the census without a claim of completed review.

| Scope | Genes | Selected claims |
|---|---:|---|
| All GO/function-bearing records | 16 | 21 GO predictions and three function paragraphs, plus their four localization claims |
| Additional localization cases | 4 | Six localization claims |
| **Review cohort** | **20** | **21 GO, three paragraphs, ten localization claims** |
| Remaining census | 31 | 14 localization-only records and 17 name-only records |

This is a focused evaluation of the available outputs, not a random proteome sample or a prospective accuracy estimate. CNN denotes supported biology already annotated; it does not establish training-set membership. Current sequences support identity and feature checks but are not proven prediction-time inputs. The [data README](neurospora-benchmark/README.md) documents source dates, explicit selection, accession/name mapping and reproducible census scripts.

## GO prediction results

| Assessment | GO claims | Interpretation |
|---|---:|---|
| LSP | 19 | Supported, with a more specific established annotation |
| CNN | 1 | Supported equivalent biology already annotated: NCU03033 nucleus |
| UNC | 1 | NCU04937 DNA binding lacks decisive supporting or contrary evidence |
| **Total** | **21** | **GO predictions only** |

No GO claim is classified as COR, PLI, NPI or REP. The incorrect claims occur in the function paragraphs, demonstrating why those paragraphs require their own assessment. Across the three paragraphs, ubiquitin transfer and neuronal context are contradicted, glycerol phosphorylation and metabolism are supported, and a strong claim about regulating glycerol uptake remains uncertain. Fragment counts depend on how sentences are divided and are not pooled with GO terms.

The ten localization claims have separate assessments: **four LSP, two COR and four UNC**. The two supported additions are cytoplasmic-vesicle and clathrin-coated-vesicle-membrane association of NCU09721, grounded in conserved fungal AP-1 biology. The uncertain claims are NCU04937 nucleus, NCU06296 ER membrane, NCU12035 nucleus and NCU06005 cytoplasm. For the last case, classical Neurospora literature establishes cytosolic glycerokinase, but an explicit mapping of that historical glp-4 gene to NCU06005 is unresolved. The enzyme-family assignment alone does not settle compartmental targeting.

## Review coverage

All **20 main reviews cover 216 original GOA rows**, with no pending actions, and propose one additional inferred RNA-methylation annotation for NCU11362. Fifteen generated Falcon reports were inspected; five genes have explicitly labeled manual research reports after provider failures. The primary evidence, source identity and limits of each inference remain in the gene notes and supporting artifacts.

The [validation summary](neurospora-benchmark/validation-summary.json) records checks of the main reviews, GO sidecars, source excerpts, histories and rendered links. [Per-file prediction evidence results](neurospora-benchmark/prediction-evidence-validation.json) and the [coverage audit](neurospora-benchmark/review-inventory.json) accompany the frozen inputs. These mechanical checks complement the biological assessments; they do not certify their scientific correctness.

## Illustrative findings

| Target | Prediction | Biological assessment |
|---|---|---|
| <gene species="NEUCR" symbol="NCU04302">NCU04302</gene> | “Accepts the ubiquitin from the E1 complex and catalyzes its covalent attachment to other proteins” | The target belongs to the SUMO E2/Ubc9 lineage. Its conserved reaction transfers SUMO, so both ubiquitin-specific claims are PLI. The broad transferase GO prediction is LSP. The recorded match is Arabidopsis ubiquitin E2 UBC2; agreement with that protein does not establish the target's modifier specificity. |
| <gene species="NEUCR" symbol="NCU04637">NCU04637</gene> | Presynaptic function at a neuromuscular junction; synaptic-vesicle endocytosis | The Rvs167-specific assignment and BAR–SH3 architecture support conserved fungal endocytosis. Neurospora has no neuromuscular junction or synaptic vesicles, making the literal neuronal claims NPI. General cytoplasmic localization remains supported and less precise than the cortical-actin-patch annotation. |
| <gene species="NEUCR" symbol="NCU04937">NCU04937</gene> | DNA binding and nuclear localization | Both remain UNC. This short glutamine-rich protein has no established DNA-binding subfamily placement or recovered target assay. A recorded low-scoring match to human THAP11 does not justify the transfer, while absence of a diagnostic domain does not refute every possible DNA-binding role. |
| <gene species="NEUCR" symbol="NCU11362">NCU11362</gene> | Primary metabolic process | The broad claim is LSP. METTL16-specific placement and characterized fungal U6 methylation support RNA metabolism; a generic METTL16/RlmF fold alone would not identify the RNA substrate. Target-specific mRNA substrates remain unresolved. |
| <gene species="NEUCR" symbol="NCU08990">NCU08990</gene> | Ribosome, ribonucleoprotein complex and cytoplasm | A Neurospora ribosome structure identifies this exact eL39 protein in the cytosolic large subunit. The GO complex predictions are LSP; cytoplasmic localization is supported. This case has direct target structural evidence despite its TrEMBL record status. |
| <gene species="NEUCR" symbol="glt-1">glt-1</gene> | Transmembrane transporter activity and membrane | Both GO claims are LSP against established D-glucose transport and plasma-membrane function. The main review separately questions proton coupling: GLT-1 is assigned to the low-affinity system I described as facilitated diffusion, whereas proton-coupled uptake characterizes system II. |
| <gene species="NEUCR" symbol="NCU06005">NCU06005</gene> | Glycerol phosphorylation; regulation of uptake; cytoplasm | Conserved glycerol-kinase chemistry supports the reaction, while a key regulatory role in uptake remains UNC. The emitted Cytoplasm label has evidence metadata pointing to GO:0005739, mitochondrion. The label is assessed as emitted, with the metadata mismatch preserved; it is not silently replaced by a mitochondrial prediction. |
| <gene species="NEUCR" symbol="mek-1">mek-1</gene> | Cytoplasm | Direct Neurospora MEK-1–GFP imaging provides finer localization at contacts between fusing germlings. The main review distinguishes MAP kinase kinase activity from a separate EC-derived MAP kinase annotation. |

Each linked gene review includes primary citations and supporting excerpts. The original paragraphs are preserved and assessed in separate function reports. Recorded phmmer matches describe source corroboration; they do not reconstruct the model's internal reasoning.

## Gene reviews

Names link to the main reviews. GO sidecars appear in the separate external-predictions section; function and localization reports are available among each gene page's documents. Localization reports preserve the emitted UniProt SL IDs and labels rather than substituting GO IDs from evidence metadata.

| Gene | NCU locus | Exact prediction accession | GO | Function paragraphs | Localization claims |
|---|---|---|---:|---:|---:|
| <gene species="NEUCR" symbol="NCU11362">NCU11362</gene> | NCU11362 | [A7UX10](https://rest.uniprot.org/uniprotkb/protnlm/A7UX10) | 1 | 0 | 0 |
| <gene species="NEUCR" symbol="glt-1">glt-1</gene> | NCU01633 | [Q1K4S3](https://rest.uniprot.org/uniprotkb/protnlm/Q1K4S3) | 2 | 0 | 0 |
| <gene species="NEUCR" symbol="NCU01245">NCU01245</gene> | NCU01245 | [Q1K6K5](https://rest.uniprot.org/uniprotkb/protnlm/Q1K6K5) | 1 | 0 | 0 |
| <gene species="NEUCR" symbol="NCU04302">NCU04302</gene> | NCU04302 | [Q1K772](https://rest.uniprot.org/uniprotkb/protnlm/Q1K772) | 1 | 1 | 0 |
| <gene species="NEUCR" symbol="NCU01540">NCU01540</gene> | NCU01540 | [Q7RWZ3](https://rest.uniprot.org/uniprotkb/protnlm/Q7RWZ3) | 1 | 0 | 0 |
| <gene species="NEUCR" symbol="mek-1">mek-1</gene> | NCU06419 | [Q7RYZ6](https://rest.uniprot.org/uniprotkb/protnlm/Q7RYZ6) | 0 | 0 | 1 |
| <gene species="NEUCR" symbol="NCU09880">NCU09880</gene> | NCU09880 | [Q7S234](https://rest.uniprot.org/uniprotkb/protnlm/Q7S234) | 1 | 0 | 0 |
| <gene species="NEUCR" symbol="NCU06005">NCU06005</gene> | NCU06005 | [Q7S2F2](https://rest.uniprot.org/uniprotkb/protnlm/Q7S2F2) | 1 | 1 | 1 |
| <gene species="NEUCR" symbol="NCU09721">NCU09721</gene> | NCU09721 | [Q7S2Q5](https://rest.uniprot.org/uniprotkb/protnlm/Q7S2Q5) | 0 | 0 | 3 |
| <gene species="NEUCR" symbol="NCU08990">NCU08990</gene> | NCU08990 | [Q7S2X9](https://rest.uniprot.org/uniprotkb/protnlm/Q7S2X9) | 2 | 0 | 1 |
| <gene species="NEUCR" symbol="NCU04637">NCU04637</gene> | NCU04637 | [Q7S3B9](https://rest.uniprot.org/uniprotkb/protnlm/Q7S3B9) | 1 | 1 | 1 |
| <gene species="NEUCR" symbol="NCU04937">NCU04937</gene> | NCU04937 | [Q7S3T0](https://rest.uniprot.org/uniprotkb/protnlm/Q7S3T0) | 1 | 0 | 1 |
| <gene species="NEUCR" symbol="kal-1">kal-1</gene> | NCU03593 | [Q7S7W0](https://rest.uniprot.org/uniprotkb/protnlm/Q7S7W0) | 1 | 0 | 0 |
| <gene species="NEUCR" symbol="NCU06296">NCU06296</gene> | NCU06296 | [Q7SAD4](https://rest.uniprot.org/uniprotkb/protnlm/Q7SAD4) | 0 | 0 | 1 |
| <gene species="NEUCR" symbol="NCU08595">NCU08595</gene> | NCU08595 | [Q7SCN3](https://rest.uniprot.org/uniprotkb/protnlm/Q7SCN3) | 1 | 0 | 0 |
| <gene species="NEUCR" symbol="vtc-4">vtc-4</gene> | NCU08110 | [Q7SCX0](https://rest.uniprot.org/uniprotkb/protnlm/Q7SCX0) | 1 | 0 | 0 |
| <gene species="NEUCR" symbol="NCU03033">NCU03033</gene> | NCU03033 | [Q7SGY4](https://rest.uniprot.org/uniprotkb/protnlm/Q7SGY4) | 2 | 0 | 0 |
| <gene species="NEUCR" symbol="NCU02539">NCU02539</gene> | NCU02539 | [Q7SHS5](https://rest.uniprot.org/uniprotkb/protnlm/Q7SHS5) | 3 | 0 | 0 |
| <gene species="NEUCR" symbol="NCU12035">NCU12035</gene> | NCU12035 | [V5ILC0](https://rest.uniprot.org/uniprotkb/protnlm/V5ILC0) | 0 | 0 | 1 |
| <gene species="NEUCR" symbol="NCU07379">NCU07379</gene> | NCU07379 | [V5IQW8](https://rest.uniprot.org/uniprotkb/protnlm/V5IQW8) | 1 | 0 | 0 |

## Evidence interpretation

Neurospora experiments and structures anchor target-specific claims. Conserved-family transfers also carry weight when the target's subfamily placement and characterized relatives support the exact property. A complex subunit's participation is distinct from autonomous catalysis, and conserved cellular mechanisms do not establish an animal-specific anatomical context.

The main reviews assess existing annotations separately from the external predictions. Experimental annotations are not rejected because an abstract omits the target; PAINT assertions are assessed as curated ancestral-function judgments. Research reports integrate evidence, with consequential findings checked against the underlying papers and sequence or structural observations. ARBA agreement or a generated description repeating a conclusion does not supply independent biological support.
