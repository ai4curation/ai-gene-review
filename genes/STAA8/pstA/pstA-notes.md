# pstA receptor review notes

## 2026-11-04 — cyclic di-AMP receptor audit

The seeded Q2G229 record contains no GO annotations. The protein is the SAOUHSC_00452 member of PANTHER PTHR38456 and Pfam CdAMP_rec, supporting assignment to experimentally characterized S. aureus PstA. The direct ligand-binding mechanism is recorded as a supported core function, with the annotation gap addressed in the follow-up below. No phosphate-transporter or nitrogen-metabolism claim follows from the gene/fold name.

Falcon deep research was attempted using `just deep-research-falcon STAA8 pstA` and failed with HTTP 403 authentication failure. This is manual primary-source research, not a provider-generated report. The original machine annotation payloads and raw UniProt/GOA files are retained. No NEW annotation rows were added in the initial pass; the follow-up below records the final recommendation.

- [PMID:25505271](https://pubmed.ncbi.nlm.nih.gov/25505271/): The S. aureus PstA trimer contains three intersubunit c-di-AMP binding sites. "The complex structure revealed three identical c-di-AMP-binding sites per trimer with each binding site at a monomer-monomer interface."

Module membership: `MODULE:bacterial_c_di_amp_signaling`, receptor arm. No unsupported top-level association slot is used.

## 2026-11-04 — PR #5997 review follow-up

Added NEW GO:0180001 with ISS evidence from PMID:25505271, so the initially empty GOA record now has a machine-readable ligand-binding recommendation. The paper specifies SAUSA300_0460, not the NCTC 8325 locus. A live UniProt REST query (`gene:SAUSA300_0460`, JSON sequence field) on 2026-11-04 identifies A0A0H2XH20. Comparing its complete sequence against the immutable local Q2G229 UniProt SQ section gives 109/109 identical residues. Combined with the target CdAMP_rec signature, this supports transfer of the directly assayed activity without mislabeling it as a target-strain IDA. Downstream target, nitrogen-metabolism activity, and phosphate-transport activity remain unassigned.

Sequence-transfer audit (retrieved 2026-11-04): donor [A0A0H2XH20](https://rest.uniprot.org/uniprotkb/A0A0H2XH20.json), target [Q2G229](https://rest.uniprot.org/uniprotkb/Q2G229.json). The target sequence was read from the preserved local UniProt record; the donor sequence was retrieved through the REST search described above. Both sequences contain 109 amino acids, with 109/109 identity and no gaps. SHA256 of each uppercase amino-acid sequence, with no whitespace: `d05eec75dc019adfbfc4a49192cb6dc9e885bdc43919f60df5076a59470db38b`. Reproduce by extracting `sequence.value` from the donor JSON, joining the residue lines below the target `SQ` line, comparing equality, and hashing their UTF-8 bytes.
