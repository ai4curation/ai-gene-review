# NCU08990 evidence notes

NCU08990 encodes eL39, a small basic structural protein of the cytosolic large ribosomal subunit. It is present in the experimentally determined Neurospora 80S ribosome and participates in cytoplasmic protein synthesis. Characterized fungal eL39 contributes to ribosome integrity and translational accuracy.

## Identity and provenance

The exact current accession is Q7S2X9; NCU08990 is retained as the current locus identifier. No independently established formal gene-symbol replacement was found. Original claims are preserved in NCU08990-protnlm-source.json from the live API snapshot retrieved 2026-09-09T03:00:51.831347+00:00. The current sequence is not proven to be the prediction-time input, and placeholder API dates do not establish release or training membership.

## Primary evidence and justified transfer

- [PMID:34815343] "We elucidated CHX's mechanism of action based on
the cryo-electron microscopy structure of actively translating Neurospora crassa
ribosomes bound with CHX at 2.7-Å resolution."
- [PMID:10852723] "Each of the two L39 mutants displayed a
4-fold increase of their error frequencies over the wild type."

The specific domain/family observation used is `DR   InterPro; IPR000077; Ribosomal_eL39.`. Family membership and characterized relatives establish the inference; ARBA or AI-generated names are not independent functional evidence. PAINT is a curator-reviewed ancestral assertion, not donor-count evidence.

## Unresolved assertions

No unresolved GOA assertion remains at the reviewed level of specificity. Experimental observations on relatives are distinguished from target observations.

PDB 7R81 entity 74 is L39, chain VB (author chain n1), 51 residues, mapped explicitly to Q7S2X9 by RCSB. Its raw entity JSON is retained in NCU08990-7R81-entity74.json. This identifies the target protein in the Neurospora translating 80S complex despite the paper abstract foregrounding drug-binding proteins. Source: https://www.rcsb.org/structure/7R81 and https://data.rcsb.org/rest/v1/core/polymer_entity/7R81/74.

## Falcon report appraisal

The actual Falcon report arrived after the wrapper timeout and was inspected. It supports the eL39 family role but missed the direct Neurospora translating-ribosome structure (PMID:34815343; PDB 7R81). Its statement that direct incorporation evidence was not located describes its search, not the full evidence now available: retained RCSB entity 74 explicitly maps the structure to Q7S2X9. The direct target model therefore supplies stronger support than the report's distant-family examples. No untested specialized-ribosome or chaperone-regulation role is added. The wrapper reported a 600-second timeout and fallback HTTP 401 insufficient quota, but the original child completed without duplicate submission.
