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

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

This re-review does not use ProtNLM2 output, the earlier phmmer donor record, or any prediction sidecar.

- **Deep research:** `just deep-research NEUCR NCU04937 --provider falcon` was rerun on 2026-10-21 and failed with "Exception: Failed to authenticate". No provider report exists. Europe PMC returns 0 hits for "NCU04937", so no gene-specific literature exists.
- **GOA:** 0 rows, so no existing annotation needs adjudication.
- **Identity:** Q7S3T0 (114 aa, SV3) is the only UniProt entry for the locus, so it is the canonical product and not a fragment or isoform. The gene model has been revised: UniParc UPI00015C37E0 is the earlier 124-aa version, which shares residues 1-104 and then has a different C-terminal tail. The polyQ run is 50 residues (55-104) [file:NEUCR/NCU04937/NCU04937-bioinformatics/RESULTS-rereview.md "A single uninterrupted polyglutamine run of 50 residues starts at position 55"].
- **Family:** InterPro gives only PANTHER PTHR13270:SF14 ("SEX DETERMINATION AND DOSAGE COMPENSATION PROTEIN SDC-2"; family name "PROTEIN C20ORF116-RELATED") over residues 38-104, with score 3.7e-05. That span is the polyQ run, so the match is driven by low complexity. Nothing is transferred from this placement. No PAINT/IBA annotations exist. No PANTHER family review covers PTHR13270 under interpro/panther/, and no module mentions this gene.
- **Homology:** BLASTP of the polyQ-collapsed sequence (unfiltered, UniProtKB) finds only self, then Q-rich noise at E >= 0.009. There are no Neurospora or Sordariomycete homologs, so the gene is an orphan ORF. No characterised relative can be chosen on phylogenetic grounds.
- **Review changes:** I rewrote the description with the polyQ length, the family-match caveat, the orphan status and the gene-model revision. core_functions remain empty. I added the bioinformatics reference, a question on whether this is a real coding gene, and an experiment to validate the gene model.
