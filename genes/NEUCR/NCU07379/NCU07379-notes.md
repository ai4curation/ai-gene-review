# NCU07379 research notes

Review date: 2026-09-09T03:17:51.839101+00:00. Target: V5IQW8, NEUCR, 395 residues. Identity is anchored to the frozen current UniProt accession and gene record. The accession-specific fetch seeded all 8 current GOA rows.

## Evidence basis

NCU07379 encodes an AP-1-like bZIP transcription factor related to fungal Yap1 proteins. Conserved family placement supports binding to transcriptional regulatory DNA and activation of RNA polymerase II transcription in the nucleus. Its physiological target genes and regulatory inputs in Neurospora crassa remain incompletely characterized.

- file:NEUCR/NCU07379/NCU07379-uniprot.txt: “DR   PANTHER; PTHR40621:SF6; AP-1-LIKE TRANSCRIPTION FACTOR YAP1-RELATED; 1.”
- PMID:2542125: “Disruption of the YAP1 gene demonstrates this gene is not essential but is required for AP-1 recognition element-dependent transcriptional activation.”

## Source claim provenance

The full API prediction JSON is preserved without deleting any fields. Function and location reports retain original words, SL identifiers and entire evidence objects. GO sidecars preserve all emitted GO IDs and labels; main reviews assess the independent current GOA rows.

- GO:0003700: [{"evidenceCode": "ECO:0008006", "id": "ProtNLM2", "properties": [{"key": "model_score", "value": "1.00"}, {"key": "string_match_text", "value": "GO:0001228"}, {"key": "string_match_location", "value": "GO"}, {"key": "string_match_type", "value": "hydrated"}], "source": "Google"}]

## Research execution

The original Falcon attempt failed with HTTP 429 (rate limit), and the configured Perplexity-lite fallback failed with HTTP 401 (insufficient quota). No provider report was returned for this gene, and no duplicate provider request was submitted. The companion deep-research-manual.md is an explicitly manual synthesis of inspected sources, not provider output.

## Subfamily inference and limits

The sequence-based PANTHER assignment PTHR40621:SF6 is AP-1-LIKE TRANSCRIPTION FACTOR YAP1-RELATED and InterPro identifies AP-1-like/bZIP. PMID:2542125 establishes element-dependent transcriptional activation by fungal Yap1. This supports the conserved molecular property in combination with the PAINT assertion, not a direct assay on NCU07379. Search by exact NCU locus recovered no decisive target-specific DNA-binding or localization experiment. A polysaccharide transcriptome study (DOI:10.1111/mmi.12459) lists NCU07379 among mostly putative TFs; expression in a cluster alone does not establish an essential pectin-response function. No nap-1 synonym or oxidative-stress pathway is assigned without verified mapping.
