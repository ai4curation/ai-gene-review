# NCU02539 research notes

Review date: 2026-09-09T03:17:51.839101+00:00. Target: Q7SHS5, NEUCR, 1013 residues. Identity is anchored to the frozen current UniProt accession and gene record. The accession-specific fetch seeded all 37 current GOA rows.

## Evidence basis

NCU02539 encodes the Mcm4 subunit of the conserved Mcm2-7 replicative helicase. Mcm4 contributes to DNA binding and ATP-dependent DNA unwinding in a multisubunit complex, participating in origin licensing, initiation and elongation of nuclear DNA replication. Its domain architecture includes the MCM N-terminal and OB-fold regions, an AAA+ ATPase domain and an Mcm4 winged-helix region.

- file:NEUCR/NCU02539/NCU02539-uniprot.txt: “DR   InterPro; IPR008047; MCM_4.”
- PMID:19896182: “The licensing of eukaryotic DNA replication origins, which ensures once-per-cell-cycle replication, involves the loading of six related minichromosome maintenance proteins (Mcm2-7) into prereplicative complexes (pre-RCs).”
- PMID:10567526: “the Mcm4 protein may play a role in the single-stranded DNA binding activity of the complex.”

## Source claim provenance

The full API prediction JSON is preserved without deleting any fields. Function and location reports retain original words, SL identifiers and entire evidence objects. GO sidecars preserve all emitted GO IDs and labels; main reviews assess the independent current GOA rows.

- GO:0033260: [{"evidenceCode": "ECO:0008006", "id": "ProtNLM2", "properties": [{"key": "model_score", "value": "0.83"}, {"key": "string_match_text", "value": "GO:0006279"}, {"key": "string_match_location", "value": "GO"}, {"key": "string_match_type", "value": "hydrated"}], "source": "Google"}]
- GO:0006270: [{"evidenceCode": "ECO:0008006", "id": "ProtNLM2", "properties": [{"key": "model_score", "value": "0.97"}, {"key": "string_match_text", "value": "GO:1902975"}, {"key": "string_match_location", "value": "GO"}, {"key": "string_match_type", "value": "hydrated"}], "source": "Google"}]
- GO:0003677: [{"evidenceCode": "ECO:0008006", "id": "ProtNLM2", "properties": [{"key": "model_score", "value": "0.98"}, {"key": "string_match_text", "value": "GO:0003697"}, {"key": "string_match_location", "value": "GO"}, {"key": "string_match_type", "value": "hydrated"}], "source": "Google"}]

## Research execution

The original Falcon report returned and was inspected. Publication caching ran concurrently. The report is retained as received; consequential claims are checked against primary sources and sequence evidence below.

## Falcon report appraisal and catalytic caution

The returned Falcon report correctly supports Mcm4 identity through the subfamily-specific MCM_4 signature, distinguishes complex-level DNA unwinding from an autonomous monomer and finds no direct NCU02539 experiment. Its broad review-derived mechanism agrees with the independently cached primary reconstitution PMID:19896182 and Mcm4-containing-complex mutant analysis PMID:10567526. The additional mammalian cancer/application and quantitative claims are not transferred to this fungal gene. RNA/hybrid helicase activity, four-way-junction unwinding and rDNA protrusion residence are unresolved electronic transfers. The PROSITE statement “Lacks conserved residue(s) required for the propagation of feature annotation” is generic: the current record retains Walker A 662–669 and Walker B 726–729 annotations. It does not establish a pseudoenzyme and does not refute replication participation.
