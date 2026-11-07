# kdpD receptor review notes

## 2026-11-04 — cyclic di-AMP receptor audit

PTHR45569-paint.tsv was checked: PTN001976096 IBD GO:0000155 and GO:0005886 are grounded in P21865. The target retains its characteristic architecture. PMID:26195599 assays receptor binding and expression, not direct c-di-AMP inhibition of KdpD autokinase activity. Experiments on S. aureus strains are interpreted with the conserved Q2FWH7 sensor architecture and its curated UniProt linkage, not as a claim that every KdpD in bacteria binds this ligand.

Falcon deep research was attempted using `just deep-research-falcon STAA8 kdpD` and failed with HTTP 403 authentication failure. This is manual primary-source research, not a provider-generated report. The original machine annotation payloads and raw UniProt/GOA files are retained. No NEW annotation rows were added in the initial pass; the follow-up below records the final recommendation.

- [PMID:26195599](https://pubmed.ncbi.nlm.nih.gov/26195599/): KdpD is the sensor component of the KdpD/KdpE system. "The sensor kinase KdpD forms a two-component signaling system with the response regulator KdpE and regulates the expression of the kdpDE genes and the kdpFABC operon"
- [PMID:26195599](https://pubmed.ncbi.nlm.nih.gov/26195599/): Cyclic di-AMP binds its cytoplasmic USP domain. "the S. aureus KdpD protein binds c-di-AMP specifically and with an affinity in the micromolar range through its universal stress protein (USP) domain."
- [PMID:26195599](https://pubmed.ncbi.nlm.nih.gov/26195599/): The measured downstream consequence is reduced salt-stress induction of kdpFABC. "c-di-AMP binding to KdpD inhibits the upregulation of the kdpFABC operon under salt stress"

Module membership: `MODULE:bacterial_c_di_amp_signaling`, receptor arm. No unsupported top-level association slot is used.

The required `just paint-losses STAA8 kdpD` query completed successfully on 2026-11-04: no IRD or IKR loss on the Q2FWH7 lineage. Positive IBD records were checked independently in the family paint.tsv; the tree query checks whether a subsequent lineage-specific loss blocks them.

## 2026-11-04 — PR #5997 review follow-up

Added NEW GO:0180001 with ISS evidence from PMID:26195599. That paper uses LAC* KdpD and also tests a distinct MRSA252 KdpD2; the latter is not the transfer donor. A live UniProt REST query (`gene:kdpD AND organism_id:367830`, JSON sequence field) on 2026-11-04 identifies A0A0H2XIE2, SAUSA300_2035. Comparing its complete sequence to the immutable local Q2FWH7 UniProt SQ section gives 885/885 identical residues. This explicitly grounds transfer of the directly measured binding to the NCTC 8325 record. The original assays are not relabeled as target-strain IDA, and expression effects remain distinct from direct autokinase inhibition.

Sequence-transfer audit (retrieved 2026-11-04): donor [A0A0H2XIE2](https://rest.uniprot.org/uniprotkb/A0A0H2XIE2.json), target [Q2FWH7](https://rest.uniprot.org/uniprotkb/Q2FWH7.json). The target sequence was read from the preserved local UniProt record; the donor sequence was retrieved through the REST search described above. Both sequences contain 885 amino acids, with 885/885 identity and no gaps. SHA256 of each uppercase amino-acid sequence, with no whitespace: `6a036e38a808b27f32e42a9e665aa58bd376e3a9765bd0cfa5e0efe4c605ec2d`. Reproduce by extracting `sequence.value` from the donor JSON, joining the residue lines below the target `SQ` line, comparing equality, and hashing their UTF-8 bytes.


## 2026-11-07 regulatory comparator audit

All ten historical rows and the inherited ISS NEW action are preserved. The USA300 A0A0H2XIE2 donor and Q2FWH7 are 885/885 identical; LAC* expression phenotypes and MRSA252 KdpD2 remain distinguished. PMID33989637 provides isolated-domain structural corroboration, not an NCTC 8325 physiological assay.

Default Falcon research was attempted and failed with HTTP 403; no provider output was fabricated. Manual full-primary reading supports this review. PAINT-loss checks completed; STAA8 target has no IRD/IKR, while Q1J2K3 is absent from the cached tree and no target loss is inferred. Baseline, source hashes, ontology snapshots and reproducible sequence comparison are retained under analysis/module_audits/bacterial_kdp_potassium_homeostasis/regulatory-comparators/.
