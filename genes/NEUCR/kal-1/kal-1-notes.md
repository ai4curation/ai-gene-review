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

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not opened or used. Deep research: the falcon/perplexity attempts recorded above failed,
and the manual synthesis was superseded by a direct literature search (PubMed eutils) and a new
bioinformatics comparison.

### Identity
- Q7S7W0 is the full-length 615-aa product of NCU03593 (UniProt sequence version 1). It has a homeodomain
  at 77-136 with an intact WFQNRR recognition-helix motif (W124-R129) and a C-terminal PF24818 PH_TRF2_HOY1
  domain. It is not a fragment, an isoform or an alternative gene model.

### Evolutionary placement (kal-1-bioinformatics/RESULTS-rereview.md)
- PANTHER PTHR24324:SF5. This matches the family review interpro/panther/PTHR24324/PTHR24324-review.yaml,
  so there is no subfamily disagreement. The SF5 label "HHEX" reflects the animal members; the subfamily
  also contains the fungal Pho2, S. pombe Yox1/Phx1, Yarrowia HOY1 and Pyricularia TRF2.
- The 1:1 ortholog is Pyricularia oryzae TRF2 / MoC19TRF2 (G4N2B2, MGG_04853). It shares the HOGENOM
  cluster CLU_023524_1_0_1 and OrthoDB group 6159439at2759, is 67% identical over the full length and
  93% over the homeodomain, and has the same architecture. It is the only PF24818 protein in each proteome.
  [PMID:27902426 "found individually to act as negative regulators repressing gene expression of" MoPKS19]
- Yarrowia HOY1 (Q99160) has the same architecture but lies outside the HOGENOM cluster (55% homeodomain
  identity). [PMID:9343389 "deletion prevents the yeast-hypha transition both in liquid and solid media"]
- The yeast and animal IBA donors share only the homeodomain (35-55%), so only the homeodomain activity
  transfers to KAL-1.

### Literature on kal-1 itself
- PMID:28696922 (Carrillo et al. 2017, full text): "the kal-1/NCU03593 homeodomain mutant had an abnormal
  conidiation pattern (Colot et al. 2006)". No DNA-binding or target data exist for KAL-1.

### Changes vs previous review
- GO:0000977 and GO:0003677 changed from ACCEPT to MODIFY, refined to GO:0000978, which is IBA-supported
  and already on the gene.
- GO:0006355 changed from ACCEPT to MODIFY, refined to GO:0006357.
- GO:0000978, GO:0000981, GO:0005634 and GO:0006357 remain ACCEPT, with new supporting evidence.
- GO:0030154 remains KEEP_AS_NON_CORE. All of its donors are animal; the support is now the PMID:28696922
  phenotype, and a conidiation term is not proposed because the evidence shows necessity, not participation.
- The description was rewritten (domains, ortholog, phenotype). Suggested questions and an experiment
  were added. The notes file is kept as a reference but is no longer cited as support.

### Relative to review next
- Pyricularia oryzae TRF2 (G4N2B2). No review exists in the repo (genes/PYRO7 has no TRF2 folder).
