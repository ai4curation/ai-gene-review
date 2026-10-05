# kal-1 research notes

Review date: 2026-09-09T03:17:51.839101+00:00. Target: Q7S7W0, NEUCR, 615 residues. Identity is anchored to the frozen current UniProt accession and gene record. The accession-specific fetch seeded all 8 current GOA rows.

## Evidence basis

KAL-1 is a homeodomain-containing transcriptional regulator in Neurospora crassa. Its conserved homeodomain supports sequence-specific DNA binding and nuclear transcriptional regulation. Deletion of kal-1 alters colony morphology, connecting its regulatory role to fungal growth and differentiation.

- file:NEUCR/kal-1/kal-1-uniprot.txt: “DR   Pfam; PF00046; Homeodomain; 1.”

## Source claim provenance

The full API prediction JSON is preserved without deleting any fields. Function and location reports retain original words, SL identifiers and entire evidence objects. GO sidecars preserve all emitted GO IDs and labels; main reviews assess the independent current GOA rows.

- GO:0003677: [{"evidenceCode": "ECO:0008006", "id": "ProtNLM2", "properties": [{"key": "model_score", "value": "0.97"}, {"key": "string_match_text", "value": "GO:0000978"}, {"key": "string_match_location", "value": "GO"}, {"key": "string_match_type", "value": "hydrated"}], "source": "Google"}]

## Research execution

The original Falcon attempt failed with HTTP 429 (rate limit), and the configured Perplexity-lite fallback failed with HTTP 401 (insufficient quota). No provider report was returned for this gene, and no duplicate provider request was submitted. The companion deep-research-manual.md is an explicitly manual synthesis of inspected sources, not provider output.

## Primary phenotype scope

PMID:16801547 is cached with abstract only; its PubMed figures were separately inspected at https://pubmed.ncbi.nlm.nih.gov/16801547/. Figure 3 includes the exact caption excerpt: “Colony morphology of wild type and Δkal-1:NCU03593.” This confirms the locus-to-symbol mapping and a colony phenotype comparison, not a biochemical DNA-binding assay. Figure 2 identifies NCU03593 as a homeobox gene. DNA-binding function is supported by the diagnostic homeodomain and curated phylogenetic inference; the PANTHER family’s HHEX name does not transfer mammalian tissue biology. The full paper could not be downloaded through the cache/PMC route; no unseen promoter specificity is claimed.
