# kdpD receptor review notes

## 2026-11-04 — cyclic di-AMP receptor audit

PTHR45569-paint.tsv was checked: PTN001976096 IBD GO0000155 and GO0005886 are grounded in P21865. The target retains its characteristic architecture. PMID26195599 assays receptor binding and expression, not direct c-di-AMP inhibition of KdpD autokinase activity. Experiments on S. aureus strains are interpreted with the conserved Q2FWH7 sensor architecture and its curated UniProt linkage, not as a claim that every KdpD in bacteria binds this ligand.

Falcon deep research was attempted using `just deep-research-falcon STAA8 kdpD` and failed with HTTP403 authentication failure. This is manual primary-source research, not a provider-generated report. The original machine annotation payloads and raw UniProt/GOA files are retained. No NEW annotation rows are added.

- [PMID:26195599](https://pubmed.ncbi.nlm.nih.gov/26195599/): KdpD is the sensor component of the KdpD/KdpE system. "The sensor kinase KdpD forms a two-component signaling system with the response regulator KdpE and regulates the expression of the kdpDE genes and the kdpFABC operon"
- [PMID:26195599](https://pubmed.ncbi.nlm.nih.gov/26195599/): Cyclic di-AMP binds its cytoplasmic USP domain. "the S. aureus KdpD protein binds c-di-AMP specifically and with an affinity in the micromolar range through its universal stress protein (USP) domain."
- [PMID:26195599](https://pubmed.ncbi.nlm.nih.gov/26195599/): The measured downstream consequence is reduced salt-stress induction of kdpFABC. "c-di-AMP binding to KdpD inhibits the upregulation of the kdpFABC operon under salt stress"

Module membership: `MODULE:bacterial_c_di_amp_signaling`, receptor arm. No unsupported top-level association slot is used.

The required `just paint-losses STAA8 kdpD` query completed successfully on2026-11-04: no IRD or IKR loss on the Q2FWH7 lineage. Positive IBD records were checked independently in the family paint.tsv; the tree query checks whether a subsequent lineage-specific loss blocks them.
