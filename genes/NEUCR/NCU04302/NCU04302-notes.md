# NCU04302 research notes

Review date: 2026-09-09T03:17:51.839101+00:00. Target: Q1K772, NEUCR, 157 residues. Identity is anchored to the frozen current UniProt accession and gene record. The accession-specific fetch seeded all 13 current GOA rows.

## Evidence basis

NCU04302 encodes a 157-residue Ubc9-family SUMO-conjugating E2 enzyme. Its conserved UBC catalytic domain and phylogenetic placement support transfer of activated SUMO to protein substrates, predominantly in the nucleus. SUMO modification provides a mechanism for regulating nuclear proteins; target-specific substrates and the distribution among nuclear subcompartments remain incompletely characterized.

- file:NEUCR/NCU04302/NCU04302-uniprot.txt: “DR   InterPro; IPR000608; UBC.”
- PMID:9435231: “Moreover, recombinant yeast and mammalian UBC9 enzymes were found to form thioester complexes with SMT3 and SUMO-1, respectively.”

## Source claim provenance

The full API prediction JSON is preserved without deleting any fields. Function and location reports retain original words, SL identifiers and entire evidence objects. GO sidecars preserve all emitted GO IDs and labels; main reviews assess the independent current GOA rows.

- GO:0016740: [{"evidenceCode": "ECO:0008006", "id": "ProtNLM2", "properties": [{"key": "model_score", "value": "0.91"}, {"key": "string_match_text", "value": "GO:0061656"}, {"key": "string_match_location", "value": "GO"}, {"key": "string_match_type", "value": "hydrated"}], "source": "Google"}]

## Research execution

The original Falcon attempt failed with HTTP 429 (rate limit), and the configured Perplexity-lite fallback failed with HTTP 401 (insufficient quota). No provider report was returned for this gene, and no duplicate provider request was submitted. The companion deep-research-manual.md is an explicitly manual synthesis of inspected sources, not provider output.

## Modifier specificity and donor

The PAINT SUMO-E2 node is PANTHER:PTN000629675. The UBC catalytic fold alone is insufficient to discriminate ubiquitin from SUMO. A direct comparative sequence analysis in NCU04302-bioinformatics therefore checks the target against reviewed human/fission-yeast Ubc9 and the recorded Arabidopsis ubiquitin-E2 donor P42745. PMID:9435231 demonstrates Ubc9 SUMO thioesters; PMID:16339806 reports Arabidopsis ubiquitin E2s and includes UBC1–6 activity. The donor’s reviewed function string exactly matches the paragraph. This records sequence/text provenance, not a claim about the model’s internal reasoning. QuickGO definitions cached in NCU04302-go-definitions.json distinguish isoenergetic SUMO and ubiquitin E2 transfer from the ATP-coupled ligase definition; E1 activation is a separate reaction step.

## Ubc9-specific evidence and complex definition

Exact sequence-classification excerpts: “DR   CDD; cd23798; UBCc_UBE2I; 1.” and “DR   FunFam; 3.10.110.10:FF:000035; SUMO-conjugating enzyme ubc9; 1.” The independent full-length reference comparison and all parameters are in NCU04302-bioinformatics/RESULTS.md. PMID:12597774 supplies direct SUMO-conjugation experiments on the 75%-identical fission-yeast Ubc9 reference. GO:0106068 was checked in QuickGO and includes a SUMO-protein transferase with specificity-associated proteins; stable residence is not required. PMID:17466333 describes the conserved SUMO E2 interactions with substrate and E3 ligase during conjugation, supporting broad SUMO ligase-complex membership.
