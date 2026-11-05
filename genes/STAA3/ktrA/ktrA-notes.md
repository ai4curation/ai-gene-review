# ktrA receptor review notes

## 2026-11-04 — cyclic di-AMP receptor audit

The raw UniProt gene name is trkA; ktrA is the experimental literature name for SAUSA300_0988. No protein pore activity is assigned. The two original transport-process rows are refined to regulation of potassium transport, while the incorrect independent transporter MF is refined to regulator activity.

Falcon deep research was attempted using `just deep-research-falcon STAA3 ktrA` and failed with HTTP403 authentication failure. This is manual primary-source research, not a provider-generated report. The original machine annotation payloads and raw UniProt/GOA files are retained. No NEW annotation rows are added.

- [PMID:23671116](https://pubmed.ncbi.nlm.nih.gov/23671116/): KtrA is the potassium transporter-gating component and a direct c-di-AMP receptor. "Using an affinity pull-down assay we identified the potassium transporter-gating component KtrA as a c-di-AMP receptor protein"
- [PMID:23671116](https://pubmed.ncbi.nlm.nih.gov/23671116/): The RCK_C domain contains the c-di-AMP binding site. "We defined the c-di-AMP binding activity within KtrA to the RCK_C (regulator of conductance of K(+)) domain."

Module membership: `MODULE:bacterial_c_di_amp_signaling`, receptor arm. No unsupported top-level association slot is used.
The process actions refine direct regulator roles to regulation of potassium transport; membrane translocation remains the partner activity.
