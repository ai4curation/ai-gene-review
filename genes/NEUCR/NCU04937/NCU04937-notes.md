# NCU04937 research notes

Review date: 2026-09-09T03:17:51.839101+00:00. Target: Q7S3T0, NEUCR, 114 residues. Identity is anchored to the frozen current UniProt accession and gene record. The accession-specific fetch seeded all 0 current GOA rows.

## Evidence basis

NCU04937 encodes a predicted 114-residue protein dominated by a glutamine-rich region. The current sequence carries a predicted coiled-coil segment but no assigned DNA-binding domain. Its molecular function and subcellular localization are uncharacterized.

- file:NEUCR/NCU04937/NCU04937-uniprot.txt: “FT   COILED          52..104”

## Source claim provenance

The full API prediction JSON is preserved without deleting any fields. Function and location reports retain original words, SL identifiers and entire evidence objects. GO sidecars preserve all emitted GO IDs and labels; main reviews assess the independent current GOA rows.

- GO:0003677: [{"evidenceCode": "ECO:0008006", "id": "ProtNLM2", "properties": [{"key": "model_score", "value": "0.12"}, {"key": "phmmer_accession", "value": "Q96EK4"}, {"key": "phmmer_score", "value": "29.1"}], "source": "Google"}]

## Research execution

The original Falcon attempt failed with HTTP 429 (rate limit), and the configured Perplexity-lite fallback failed with HTTP 401 (insufficient quota). No provider report was returned for this gene, and no duplicate provider request was submitted. The companion deep-research-manual.md is an explicitly manual synthesis of inspected sources, not provider output.

## Limits of the short sequence

The current sequence is 114 residues with an extended polyglutamine tract and SAM:Coils prediction at 52–104. No DNA-binding domain is annotated in the complete inspected current record. The donor Q96EK4 is human THAP11 (314 residues); its transcript-regulator biology cannot be inferred from small low-complexity matches alone. No alignment demonstrating conservation of a DNA-binding module was emitted. The recorded phmmer score is 29.1 and model scores differ sharply for DNA binding (0.12) and nucleus (0.91); neither score is experimental evidence. The genome paper PMID:12712197 establishes the organism-level sequence resource but supplies no NCU04937 function assay. Absence of a domain is insufficient to refute DNA binding; both external claims remain UNC. Core functions are left empty.
