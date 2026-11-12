# Rv3395c / ImuA' (P9WKZ9) curation notes

- No provider deep research is available for this gene; no `-deep-research-*.md` file was
  generated in this session. The review rests on PMID:20615954 (full text cached) and the
  UniProt record.
- Rv3395c is NOT a homolog of proteobacterial ImuA. It is largely actinomycete-restricted
  and was designated imuA' for that reason.
  [PMID:20615954, "which encodes a protein of unknown function restricted primarily to actinomycetes"]
  The Caulobacter paper makes the same point from the other side.
  [PMID:15886391, "Although proteins with significant similarity to ImuA cannot be found in Actinomycetales, the genomic context analysis suggests that the RecA-like protein encoded by M."]
  This non-homologous replacement is why the module models the accessory role as a variant
  set (proteobacterial ImuA vs actinobacterial ImuA') rather than one family.
- ImuA' resembles RecA structurally but lacks RecA's C-terminal domain and the
  nucleotide-binding motif.
  [PMID:20615954, "Mtb ImuA′ resembles RecA at a structural level, but lacks the characteristic C-terminal domain."]
- It binds ImuB through the C-terminal regions of both proteins and does not self-associate.
  [PMID:20615954, "We observed the direct interaction of ImuA′ with ImuB involving the C-terminal regions of both proteins; however, no evidence of ImuA′ self-association was detected that might indicate RecA-like filamentation ( 40 )."]
- Membrane row (GO:0016020): the only basis is a predicted TM helix at 63-83 (ECO:0000255)
  plus a curator inference (ECO:0000305). Marked over-annotated, not removed, and recorded
  as a CC_DARK knowledge gap; there is no experimental localization either way.
- Evidence-code issue: the MTBBASE row from PMID:20615954 is coded IDA, but the evidence is
  a deletion/complementation phenotype (IMP). Recorded as a source_defect.


## 2026-11-07 annotation-reviewer consultation

Reassessed every inherited row and core claim against PMID20615954 publisher Results/Methods, cached primary evidence, PMID37530405 and PMID39706264. Assay species are separated in [source-scope.md](../../../analysis/module_audits/bacterial_imuabc_damage_induced_mutagenesis/mycobacteria-consultation/source-scope.md). Earlier statements that all 2010 experiments were in M. tuberculosis are superseded: target deletions and yeast interactions coexist with M. smegmatis individual-deletion and catalytic/clamp-mutant assays. Newer accessory assembly and imaging experiments also use M. smegmatis. No Myxococcus ATPase result is transferred to ImuA′, and no new proposal is added. Original payloads/order and inherited proposal presence are preserved.

Actual Falcon attempt failed with HTTP 403 authentication; manual primary-source fallback was used without creating a provider-named report. PAINT-loss checks found no IRD/IKR on the inspected ImuB/DnaE2 lineages; Rv3395c has no PANTHER family and was not assessable. Ontology check shows TLS is part of DNA replication, so absence of a major replicase role cannot refute that parent. Focused validation and preservation evidence are recorded in the consultation directory.
