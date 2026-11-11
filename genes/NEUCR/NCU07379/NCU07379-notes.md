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

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not consulted for this re-review (no *-protnlm-* file or prediction-evidence folder was opened).

### Identity

- V5IQW8 is the full-length, canonical product of NCU07379: 395 aa, with an N-terminal bZIP region at about residues 60-120. It is not a fragment or an isoform. UniProt merges two EMBL CDS (ESA44189.1, ESA44190.1) and two RefSeq models (XP_011393156.1, XP_011393157.1) into this one accession. Orthologs in the closest species are similar in length (Sordaria macrospora F7VKT3, 416 aa; N. intermedia, 407 aa).
- A cold-shock screen (PMC5940138, PMID:29563189) lists NCU07379 as "transcription factor-5 / tcf-5". That symbol was not adopted here.

### Phylogenetic placement (main correction)

- The earlier review called NCU07379 "related to fungal Yap1" and used S. cerevisiae YAP1 (PMID:2542125) as its main support. N. crassa, however, has two PTHR40621:SF6 members: NCU07379 and NCU03905 (F5HEL0, 577 aa). The new analysis (NCU07379-bioinformatics/sf6_placement_rereview.py, RESULTS-rereview.md) gives:
  - NCU07379 falls in a FlbB clade with 100% bootstrap support (A. nidulans FlbB C8VBM8, M. oryzae MGG_00342, C. militaris CCM_01128, S. macrospora F7VKT3), at 47% local identity to FlbB.
  - NCU03905 falls in the Yap1/NapA clade (100%, with MGG_12814, A. fumigatus Yap1 and NapA). It is therefore the N. crassa Yap1 ortholog.
  - [PMID:21423749 "The gross phenotype of a knockout of the FlbB ortholog in Ncras (NCU07379) was characterized by the Neurospora Genome Project (NGP)"] [PMID:21423749 "This mutant conidiates normally."]
- Both clades descend from PAINT node PTN008082960. The three IBA rows (cis-regulatory binding, Pol II activator, Pol II regulator complex) therefore stand, but Yap1-specific biology (peroxide sensing, oxidative-stress regulon) must not be transferred.
- FlbB evidence for the same clade:
  - [PMID:17993569 "FlbB accumulates at the hyphal apex during early vegetative growth but is later found in apical nuclei"]
  - [PMID:20132447 "activates the expression of c-Myb transcription factor FlbD"]
- I add no conidiation process term. The N. crassa deletion conidiates normally, and the FlbB-FlbD branch is dispensable in N. crassa (PMID:21423749). The FlbB hyphal-tip location is also not added, because there is no Neurospora data and PAINT did not propagate it.

### Actions

- ACCEPT: GO:0000976 (IBA and IEA), GO:0001228 (IBA, core), GO:0005634, GO:0045944.
- MODIFY: GO:0003700 -> GO:0001228, and GO:0006355 -> GO:0045944 (correct but general).
- KEEP_AS_NON_CORE: GO:0090575 (complex partner unknown).
- PMID:2542125 is retained in the references but is no longer used as support (see its reference_review).

### Relative, family and modules

- Next relative: A. nidulans flbB (C8VBM8), genes/EMENI/flbB. Its review has status DRAFT with terse reasons, so it needs a full review.
- The family review interpro/panther/PTHR40621 describes SF6 as a Yap1/Pap1-type subfamily and does not mention the FlbB clade. The SF6 assignment itself is not in dispute, but SF6 contains at least two well-separated clades (Yap1/NapA and FlbB), and the family review should note this.
- Module: modules/conidiation_regulatory_cascade.yaml uses FlbB (C8VBM8) as the bZIP participant. NCU07379 is its ortholog, but the role is not conserved in N. crassa.
