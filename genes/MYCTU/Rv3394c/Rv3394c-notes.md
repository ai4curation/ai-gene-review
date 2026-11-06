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
