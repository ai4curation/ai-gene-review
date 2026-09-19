---
title: Pombe ProtNLM evaluation
species: [SCHPO]
tags: [EVALUATION, ML_PREDICTIONS]
autolink_gene_symbols: false
---
# Pombe ProtNLM evaluation

**Most pombe GO predictions recover established biology at reduced specificity: 27 are LSP, two CNN and three UNC.** The cohort covers all 20 GO/function-bearing entries among 28 original-export accessions matched to current fission-yeast records: 32 GO claims and 11 function paragraphs. All 28 entries are currently reviewed/Swiss-Prot, providing a well-curated comparison to the predominantly TrEMBL horse and fly cohorts.

[20-gene cohort](pombe-benchmark/functional-cohort.csv) · [Original GO/function statements](pombe-benchmark/functional-predictions.csv) · [Claim provenance](pombe-benchmark/claim-provenance.csv) · [Full 28-record inventory](pombe-benchmark/inventory.csv) · [Coverage audit](pombe-benchmark/review-inventory.json) · [Snapshot provenance](pombe-benchmark/manifest.json) · [Parent project](../PROTNLM_EVALUATION.md)

## Cohort and source identity

The published [ProtNLM2 accession list](https://ftp.ebi.ac.uk/pub/contrib/UniProt/ProtNLM2/List_of_UniProt_accessions_that_have_ProtNLM2_annotations.tsv) contains **zero pombe records**, but all 28 identified original-export entries are accessible through the live ProtNLM API. The [API/source comparison](pombe-benchmark/api-source-comparison.csv) confirms identical GO IDs and labels, and identical function text apart from the final period omitted by the API. Both representations and their evidence metadata are retained.

Membership comes from joining accessions in `post-processed-2026_02_28k.xml` to the current [UniProt pombe taxonomy index](https://rest.uniprot.org/uniprotkb/stream?query=taxonomy_id%3A4896&format=tsv&fields=accession%2Cid%2Corganism_id%2Corganism_name%2Cgene_names%2Clength%2Creviewed). The export's organism, sequence and date fields are placeholders. Current gene symbols and systematic identifiers come from [PomBase](https://www.pombase.org/data/names_and_identifiers/gene_IDs_names_products.tsv): for example, Q09683 is **mre11** (UniProt synonym `rad32`), O42996 is **crt10** (`pi073`), and O94297 is **cem1** (`SPBC887.13c`). The underlying accessions are preserved throughout the reviews.

| Scope | Entries | Claims |
|---|---:|---|
| GO and/or function text | 20 | 32 GO predictions across 18 genes; 11 paragraphs across 10 genes |
| Other outputs only | 8 | Retained in the census, outside this initial function review tier |
| **Original-export pombe cohort** | **28** | Also contains 10 location statements and one keyword across all entries |

The benchmark was constructed **after the predictions were available**. It includes every GO/function-bearing entry identified by this primary-accession join; it is not a prospective test set, random proteome sample, or exhaustive census of every pombe accession the API might serve. A [follow-up accession check](pombe-benchmark/availability-followup/summary.json) including current secondary identifiers also finds only these 28 original-export records. An additional sample of 96 other current primary accessions returned API 404; this does not establish exhaustive absence from the live API. Current sequences are frozen separately and checked against the gene-review records, but they do not establish the exact prediction-time inputs.

## Review findings

The GO claims mostly recover established functions at reduced specificity. The function paragraphs expose more detailed questions about RNA architecture, substrate preference and the activity of a protein complex.

| Assessment | GO claims | Interpretation |
|---|---:|---|
| LSP | 27 | Supported, but an established annotation is more specific |
| CNN | 2 | Supported equivalent biology already known |
| UNC | 3 | Available evidence neither validates nor refutes the exact claim |
| **Total** | **32** | **GO predictions only** |

The two CNN calls are Sws2 RNA binding and Sen15 participation in tRNA splicing. The unresolved GO predictions are Crt10 membership in a Cul4-RING E3 complex, Crt10 response to UV-B, and Wss1 membrane association. No GO claim is classified as COR, PLI, NPI or REP in this cohort. This result concerns these available predictions on well-curated genes; it does not estimate general model accuracy.

All **20 main reviews cover 366 existing GOA annotations**, with no pending actions. All 20 genes have inspected Falcon research reports, with consequential claims checked against primary evidence. The 18 GO sidecars pass schema and source-evidence validation, including 27 title checks and 68 excerpt checks. The 11 original function paragraphs are assessed claim by claim in ten separate reports; their mixed judgments are kept separate from the GO totals. [Validation summary](pombe-benchmark/validation-summary.json) and [per-file prediction evidence checks](pombe-benchmark/prediction-evidence-validation.json) accompany the coverage audit.

## Illustrative findings

| Target | Finding | Evidence and interpretation |
|---|---|---|
| <gene species="SCHPO" symbol="wss1">wss1</gene> | Membrane prediction remains UNC; its recorded source does not support it. | The original XML links the claim to KW-0539, the UniProt **Nucleus** keyword. Nuclear localization does not establish membrane association, and a soluble protein could still have an uncharacterized peripheral membrane interaction. |
| <gene species="SCHPO" symbol="ulp2">ulp2</gene> | Both broad peptidase predictions are LSP. | Direct fission-yeast biochemical experiments establish cleavage of SUMO conjugates. The predictions omit this known substrate specificity. |
| <gene species="SCHPO" symbol="crt10">crt10</gene> | Cul4-complex and UV-B claims remain UNC. | Recorded matches to plant WDR5B and DHU1 do not establish these functions in pombe. Characterized budding-yeast Crt10 participates in Rtt101-Mms1-dependent nonfunctional rRNA decay, providing a plausible cullin connection but not the specified target complex or UV-B phenotype. |
| <gene species="SCHPO" symbol="rpo41">rpo41</gene> and <gene species="SCHPO" symbol="rpa49">rpa49</gene> | The same polymerase sentence needs different protein-level interpretation. | Purified Rpo41 is the catalytic mitochondrial RNA polymerase. Rpa49 is an accessory Pol I subunit whose omission leaves nonspecific transcription intact. Its paragraph describes the associated holoenzyme's chemistry; it does not establish independent Rpa49 catalysis. The process and complex GO predictions remain supported. |
| <gene species="SCHPO" symbol="yml6">yml6</gene> and <gene species="SCHPO" symbol="sws2">sws2</gene> | Conserved mitoribosomal functions are supported; bacterial architectural details require separate assessment. | Yml6 belongs to the uL4 family, whose contribution to the peptide exit tunnel is retained in characterized mitochondrial structures. Pombe experiments identify 15S/21S mitochondrial rRNAs, contradicting the literal bacterial 16S/23S wording. Sws2 bridge geometry and subunit sedimentation designations remain separately unresolved; the missing B1a/B1b bridges in budding-yeast structures do not prove their absence in pombe. |
| <gene species="SCHPO" symbol="spt16">spt16</gene> | General FACT activity is supported; an obligatory one-dimer eviction mechanism remains UNC. | Experiments support nucleosome reorganization during DNA-templated processes. A primary mechanistic study shows that FACT-mediated accessibility need not require H2A–H2B loss, so the paragraph’s fixed eviction model is not a complete account of the mechanism. |
| <gene species="SCHPO" symbol="cem1">cem1</gene> | Conserved mitochondrial fatty-acid synthesis is supported; the exact unsaturated C16 substrate preference and thermoregulation claim remain UNC. | Characterized mitochondrial OXSM elongates acyl-ACP substrates and complements budding-yeast cem1. This supports transfer of the conserved condensation mechanism, while leaving the specified palmitoleoyl/cis-vaccenoyl preference and essential thermal-regulation role unestablished in pombe. |
| <gene species="SCHPO" symbol="vas2">vas2</gene> | ProtNLM's **intracellular** transport prediction is supported and LSP; the main review rejects an **intercellular** ARBA annotation. | Fission-yeast AP-1 experiments establish cargo traffic between compartments inside a cell. The electronic term describes movement between cells, a different process. |
| <gene species="SCHPO" symbol="uch2">uch2</gene> | ProtNLM's broad ubiquitin-dependent catabolic-process prediction is LSP; the main review distinguishes cysteine and metal-dependent DUB chemistry. | Direct proteasome-associated Uch2 experiments and the UCH/JAMM distinction support a cysteine deubiquitinase. The separate NEDD8-AMC result is assessed against the stronger claim of removing NEDD8 from a conjugated protein. |

The linked reviews provide primary citations, original predictions and the limits of each inference. Donor metadata describes a recorded match; it does not reconstruct the model's internal reasoning or make that donor assertion validating evidence.

## Gene reviews

The [remaining eight pombe genes](pombe-remaining.md) form a separate protein-name/localization queue. Current source checks have not identified enough additional prediction-bearing genes for another 20-gene cohort.

Names link to the main gene reviews. Original paragraphs and their individual assessments are retained in each applicable `*-protnlm-function-review.md` file; GO predictions have separate YAML reviews displayed in the external-predictions section.

| Gene | PomBase locus | Exact prediction accession | GO | Function paragraphs |
|---|---|---|---:|---:|
| <gene species="SCHPO" symbol="ulp2">ulp2</gene> | [SPAC17A5.07c](https://www.pombase.org/gene/SPAC17A5.07c) | [O13769](https://rest.uniprot.org/uniprotkb/protnlm/O13769) | 2 | 0 |
| <gene species="SCHPO" symbol="rpo41">rpo41</gene> | [SPAC26H5.12](https://www.pombase.org/gene/SPAC26H5.12) | [O13993](https://rest.uniprot.org/uniprotkb/protnlm/O13993) | 3 | 1 |
| <gene species="SCHPO" symbol="rfc3">rfc3</gene> | [SPAC27E2.10c](https://www.pombase.org/gene/SPAC27E2.10c) | [O14003](https://rest.uniprot.org/uniprotkb/protnlm/O14003) | 1 | 1 |
| <gene species="SCHPO" symbol="rpa49">rpa49</gene> | [SPAC2F3.03c](https://www.pombase.org/gene/SPAC2F3.03c) | [O14086](https://rest.uniprot.org/uniprotkb/protnlm/O14086) | 2 | 1 |
| <gene species="SCHPO" symbol="cbh1">cbh1</gene> | [SPAC9E9.10c](https://www.pombase.org/gene/SPAC9E9.10c) | [O14423](https://rest.uniprot.org/uniprotkb/protnlm/O14423) | 1 | 0 |
| <gene species="SCHPO" symbol="crt10">crt10</gene> | [SPBC27B12.05](https://www.pombase.org/gene/SPBC27B12.05) | [O42996](https://rest.uniprot.org/uniprotkb/protnlm/O42996) | 2 | 0 |
| <gene species="SCHPO" symbol="sws2">sws2</gene> | [SPCC1795.07](https://www.pombase.org/gene/SPCC1795.07) | [O59772](https://rest.uniprot.org/uniprotkb/protnlm/O59772) | 4 | 1 |
| <gene species="SCHPO" symbol="yml6">yml6</gene> | [SPBC2D10.08c](https://www.pombase.org/gene/SPBC2D10.08c) | [O74801](https://rest.uniprot.org/uniprotkb/protnlm/O74801) | 3 | 2 |
| <gene species="SCHPO" symbol="spt16">spt16</gene> | [SPBP8B7.19](https://www.pombase.org/gene/SPBP8B7.19) | [O94267](https://rest.uniprot.org/uniprotkb/protnlm/O94267) | 0 | 1 |
| <gene species="SCHPO" symbol="cem1">cem1</gene> | [SPBC887.13c](https://www.pombase.org/gene/SPBC887.13c) | [O94297](https://rest.uniprot.org/uniprotkb/protnlm/O94297) | 0 | 1 |
| <gene species="SCHPO" symbol="asr1">asr1</gene> | [SPCC126.07c](https://www.pombase.org/gene/SPCC126.07c) | [O94400](https://rest.uniprot.org/uniprotkb/protnlm/O94400) | 1 | 0 |
| <gene species="SCHPO" symbol="mre11">mre11</gene> | [SPAC13C5.07](https://www.pombase.org/gene/SPAC13C5.07) | [Q09683](https://rest.uniprot.org/uniprotkb/protnlm/Q09683) | 3 | 1 |
| <gene species="SCHPO" symbol="pta1">pta1</gene> | [SPAC1071.01c](https://www.pombase.org/gene/SPAC1071.01c) | [Q10222](https://rest.uniprot.org/uniprotkb/protnlm/Q10222) | 1 | 0 |
| <gene species="SCHPO" symbol="sen15">sen15</gene> | [SPAC959.10](https://www.pombase.org/gene/SPAC959.10) | [Q7LKV3](https://rest.uniprot.org/uniprotkb/protnlm/Q7LKV3) | 1 | 0 |
| <gene species="SCHPO" symbol="sus1">sus1</gene> | [SPBC6B1.12c](https://www.pombase.org/gene/SPBC6B1.12c) | [Q7LL15](https://rest.uniprot.org/uniprotkb/protnlm/Q7LL15) | 2 | 0 |
| <gene species="SCHPO" symbol="rrp36">rrp36</gene> | [SPAC823.04](https://www.pombase.org/gene/SPAC823.04) | [Q9P6P2](https://rest.uniprot.org/uniprotkb/protnlm/Q9P6P2) | 2 | 1 |
| <gene species="SCHPO" symbol="wss1">wss1</gene> | [SPAC521.02](https://www.pombase.org/gene/SPAC521.02) | [Q9P7B5](https://rest.uniprot.org/uniprotkb/protnlm/Q9P7B5) | 1 | 0 |
| <gene species="SCHPO" symbol="vas2">vas2</gene> | [SPAP27G11.06c](https://www.pombase.org/gene/SPAP27G11.06c) | [Q9P7N2](https://rest.uniprot.org/uniprotkb/protnlm/Q9P7N2) | 1 | 1 |
| <gene species="SCHPO" symbol="uch2">uch2</gene> | [SPBC409.06](https://www.pombase.org/gene/SPBC409.06) | [Q9UUB6](https://rest.uniprot.org/uniprotkb/protnlm/Q9UUB6) | 1 | 0 |
| <gene species="SCHPO" symbol="lsm6">lsm6</gene> | [SPAC2F3.17c](https://www.pombase.org/gene/SPAC2F3.17c) | [Q9UUI1](https://rest.uniprot.org/uniprotkb/protnlm/Q9UUI1) | 1 | 0 |

## Evidence standards

Pombe-specific primary experiments and PomBase curation anchor the reviews. Conserved-family inference is also useful when the target's family placement and the characterized mechanism justify transfer. Research reports help integrate that evidence; their findings are traced to the underlying papers and sequence or structural observations.

An intrinsic catalytic activity is distinct from a subunit's contribution to the corresponding enzyme complex or biological process. Broad but supported predictions are not biological errors: LSP requires an established, more specific annotation in the same GO aspect. CNN denotes already-known equivalent biology, without asserting independently verified training-set membership.

Experimental PomBase annotations are not rejected because a cached abstract omits a gene or assay. Unavailable decisive evidence is recorded as UNDECIDED in the main review or UNC for a prediction. PAINT/IBA assertions are considered as curated ancestral-function judgments. Prediction agreement, ARBA assertions and repeated generated descriptions do not supply independent biological evidence.

See the [frozen data and reproduction instructions](pombe-benchmark/README.md) for source files, checksums and audit scripts.
