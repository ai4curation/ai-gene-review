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
