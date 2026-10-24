---
title: Remaining pombe ProtNLM genes
species: [SCHPO]
tags: [EVALUATION, ML_PREDICTIONS]
autolink_gene_symbols: false
---
# Remaining pombe ProtNLM genes

**Eight unreviewed pombe genes remain in the identified ProtNLM dataset.** They contain eight protein-name outputs and four localization statements; none has a GO prediction or function paragraph. All eight currently return exact-accession predictions through the API. They are ready for review as a separate name/localization tier.

[Confirmed queue](pombe-benchmark/remaining/cohort.csv) · [Exact statements and evidence metadata](pombe-benchmark/remaining/prediction-statements.csv) · [Availability manifest](pombe-benchmark/remaining/manifest.json) · [Completed 20-gene cohort](pombe.md)

| Gene | Exact accession | Emitted name | Emitted localization |
|---|---|---|---|
| [spo2](https://www.pombase.org/gene/SPBC16C6.14) | [C6Y4C2](https://rest.uniprot.org/uniprotkb/protnlm/C6Y4C2) | Uncharacterized protein | Membrane |
| [trm402](https://www.pombase.org/gene/SPAC23C4.17) | [O13935](https://rest.uniprot.org/uniprotkb/protnlm/O13935) | tRNA (cytosine(34)-C(5))-methyltransferase | Nucleolus |
| [gpi16](https://www.pombase.org/gene/SPBC1604.15) | [O94380](https://rest.uniprot.org/uniprotkb/protnlm/O94380) | GPI transamidase component PIG-T | None |
| [nip7](https://www.pombase.org/gene/SPCC320.11c) | [Q1MTQ9](https://rest.uniprot.org/uniprotkb/protnlm/Q1MTQ9) | 60S ribosome subunit biogenesis protein NIP7 | None |
| [cis4](https://www.pombase.org/gene/SPAC17D4.03c) | [Q9HGQ3](https://rest.uniprot.org/uniprotkb/protnlm/Q9HGQ3) | Zinc transporter | Membrane |
| [cao1](https://www.pombase.org/gene/SPAC2E1P3.04) | [Q9P7F2](https://rest.uniprot.org/uniprotkb/protnlm/Q9P7F2) | Amine oxidase | None |
| [SPAC25B8.09](https://www.pombase.org/gene/SPAC25B8.09) | [Q9UTA9](https://rest.uniprot.org/uniprotkb/protnlm/Q9UTA9) | Methyltransferase type 11 domain-containing protein | None |
| [sec59](https://www.pombase.org/gene/SPCC63.10c) | [Q9Y7T6](https://rest.uniprot.org/uniprotkb/protnlm/Q9Y7T6) | dolichol kinase | Membrane |

The review questions in the queue distinguish substrate specificity, protein-complex participation and membrane residence from broad names or process associations. The outputs are preserved as names and UniProt SL locations; no GO claims are invented from them.

## Availability checks

The refreshed [published-list check](pombe-benchmark/remaining/published-list-check.json) finds zero pombe records by organism name and the species/972-strain taxon identifiers. The original export supplies 28 pombe entries, with 20 already reviewed. Its prior primary/secondary-accession search finds no additional matches.

A new [API check](pombe-benchmark/remaining/availability.jsonl.gz) confirms the eight remaining entries and tests [21 additional metabolic candidates](pombe-benchmark/remaining/additional-probe-candidates.json), covering glycolysis, the TCA cycle, pentose-phosphate metabolism, nucleotide/amino-acid synthesis and ATP synthesis. All 21 additional candidates return HTTP 404. These probes are a sample, not an exhaustive scan of the API.

A 20-gene expansion therefore requires twelve additional prediction-bearing genes from another source, or an explicitly separate comparison tier without ProtNLM predictions. Neither is represented as an already selected prediction cohort here.
