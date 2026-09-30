# NCU04637 research notes

Review date: 2026-09-09T03:17:51.839101+00:00. Target: Q7S3B9, NEUCR, 467 residues. Identity is anchored to the frozen current UniProt accession and gene record. The accession-specific fetch seeded all 12 current GOA rows.

## Evidence basis

NCU04637 encodes a fungal Rvs167-family endocytic adaptor with an N-terminal BAR domain and a C-terminal SH3 domain. Comparative evidence supports lipid binding and association with cortical actin patches, where Rvs proteins help organize endocytic membrane invaginations and vesicle scission. The detailed localization dynamics and interaction partners of the Neurospora protein remain to be established.

- file:NEUCR/NCU04637/NCU04637-uniprot.txt: “DR   PANTHER; PTHR47174:SF1; REDUCED VIABILITY UPON STARVATION PROTEIN 167; 1.”
- PMID:20610658: “We show that the purified Rvs161-Rvs167 complex binds to liposomes in a curvature-independent manner and promotes tubule formation in vitro.”
- PMID:20610658: “Rvs161 consists solely of a BAR domain, whereas Rvs167 is composed of a BAR domain followed by a region rich in glycine, proline, and alanine (GPA), and an SH3 (Src-homology 3) domain at its C-terminus”

## Source claim provenance

The full API prediction JSON is preserved without deleting any fields. Function and location reports retain original words, SL identifiers and entire evidence objects. GO sidecars preserve all emitted GO IDs and labels; main reviews assess the independent current GOA rows.

- GO:0005737: [{"evidenceCode": "ECO:0008006", "id": "ProtNLM2", "properties": [{"key": "model_score", "value": "1.00"}, {"key": "string_match_text", "value": "GO:0031097"}, {"key": "string_match_location", "value": "GO"}, {"key": "string_match_type", "value": "hydrated"}], "source": "Google"}]

## Research execution

The original Falcon attempt failed with HTTP 429 (rate limit), and the configured Perplexity-lite fallback failed with HTTP 401 (insufficient quota). No provider report was returned for this gene, and no duplicate provider request was submitted. The companion deep-research-manual.md is an explicitly manual synthesis of inspected sources, not provider output.

## Rvs167 and anatomical scope

The target architecture is BAR 17–269 plus SH3 407–467, not simply an unspecified BAR protein. PTHR47174:SF1 is explicitly Rvs167; the broader InterPro BIN3/RVS161-like label is not itself a specific Rvs161 call. PMID:20610658 distinguishes Rvs161 from Rvs167 by the latter’s SH3-containing architecture. The literal fly-derived paragraph is incompatible with fungal anatomy, while its conserved endocytosis component remains well supported. PMID:19596778 reports Candida RVS167 mutant defects in actin patch polarization, supporting the process annotation. The medial-cortex and mating-projection-tip patterns remain uncertain for the Neurospora protein.
