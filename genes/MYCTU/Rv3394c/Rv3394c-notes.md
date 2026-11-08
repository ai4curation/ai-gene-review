# Rv3394c / ImuB (O50419) curation notes

- No provider deep research is available for this gene; no `-deep-research-*.md` file was
  generated in this session. The review rests on PMID:20615954 (full text cached), the
  PTHR35369 PAINT data and the UniProt record.
- UniProt itself records the loss of the catalytic residues, which is the single most useful
  statement for rejecting any polymerase annotation on this protein.
  [file:MYCTU/Rv3394c/Rv3394c-uniprot.txt, "CC   -!- CAUTION: Lacks conserved residue(s) required for the propagation of"]
  The paper states the same for ImuB proteins generally.
  [PMID:20615954, "Despite retaining structural features characteristic of Y-family members, ImuB homologs lack conserved active-site amino acids required for polymerase activity."]
- The clamp-binding motif is functionally required: the AAAAGG allele abolishes cassette
  function, which is what makes the adaptor role a real molecular function rather than an
  interaction list.
  [PMID:20615954, "Notably, disruption of this motif in the imuB AAAAGG allele eliminated cassette function, strongly implying that ImuB—through β—is required to mediate access of DnaE2 to the replication fork."]
- IBA row: the gene is its own IBD seed at PTN002176549. Per repository policy this is the
  expected marker of experimental grounding on the target, NOT circularity, so the row is
  kept and refined (GRANULARITY_MISMATCH) rather than removed. The node's breadth across the
  SulA-containing family is adjudicated in interpro/panther/PTHR35369/PTHR35369-review.yaml.
- Evidence-code issue: the MTBBASE row is coded IDA for deletion/motif-mutant data (IMP).
  Recorded as a source_defect.


## 2026-11-07 annotation-reviewer consultation

Reassessed every inherited row and core claim against PMID20615954 publisher Results/Methods, cached primary evidence, PMID37530405 and PMID39706264. Assay species are separated in [source-scope.md](../../../analysis/module_audits/bacterial_imuabc_damage_induced_mutagenesis/mycobacteria-consultation/source-scope.md). Earlier statements that all 2010 experiments were in M. tuberculosis are superseded: target deletions and yeast interactions coexist with M. smegmatis individual-deletion and catalytic/clamp-mutant assays. Newer accessory assembly and imaging experiments also use M. smegmatis. No Myxococcus ATPase result is transferred to ImuA′, and no new proposal is added. Original payloads/order and inherited proposal presence are preserved.

Actual Falcon attempt failed with HTTP 403 authentication; manual primary-source fallback was used without creating a provider-named report. PAINT-loss checks found no IRD/IKR on the inspected ImuB/DnaE2 lineages; Rv3395c has no PANTHER family and was not assessable. Ontology check shows TLS is part of DNA replication, so absence of a major replicase role cannot refute that parent. Focused validation and preservation evidence are recorded in the consultation directory.
