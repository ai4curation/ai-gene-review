# ktrA receptor review notes

## 2026-11-04 — cyclic di-AMP receptor audit

The raw UniProt gene name is trkA; ktrA is the experimental literature name for SAUSA300_0988. No protein pore activity is assigned. The two original transport-process rows are refined to regulation of potassium transport, while the incorrect independent transporter MF is refined to regulator activity.

Falcon deep research was attempted using `just deep-research-falcon STAA3 ktrA` and failed with HTTP 403 authentication failure. This is manual primary-source research, not a provider-generated report. The original machine annotation payloads and raw UniProt/GOA files are retained. No NEW annotation rows were added in the initial pass; the follow-up below records the final recommendation.

- [PMID:23671116](https://pubmed.ncbi.nlm.nih.gov/23671116/): KtrA is the potassium transporter-gating component and a direct c-di-AMP receptor. "Using an affinity pull-down assay we identified the potassium transporter-gating component KtrA as a c-di-AMP receptor protein"
- [PMID:23671116](https://pubmed.ncbi.nlm.nih.gov/23671116/): The RCK_C domain contains the c-di-AMP binding site. "We defined the c-di-AMP binding activity within KtrA to the RCK_C (regulator of conductance of K(+)) domain."

Module membership: `MODULE:bacterial_c_di_amp_signaling`, receptor arm. No unsupported top-level association slot is used.
The process actions refine direct regulator roles to regulation of potassium transport; membrane translocation remains the partner activity.

## 2026-11-04 — PR #5997 review follow-up

Added NEW GO:0180001 (IDA; PMID:23671116) for the directly measured RCK_C ligand-binding activity. The primary study identifies SAUSA300_0988 from the USA300 LAC* strain.

Retained GO:0015459 potassium channel regulator activity after checking the [QuickGO definition](https://www.ebi.ac.uk/QuickGO/term/GO:0015459): “Binds to and modulates the activity of a potassium channel.” The broader [GO:0141108 transporter regulator activity](https://www.ebi.ac.uk/QuickGO/term/GO:0141108) covers modulation of a transporter. The target-specific primary study in USA300 LAC calls this a system with “one regulatory protein and two ion-conducting channels” and concludes that KtrA regulates KtrB/KtrD ([PMID:23815639](https://pubmed.ncbi.nlm.nih.gov/23815639/), full text fetched). This supports the more specific existing term, while preserving the distinction between regulator and conducting subunit. CabP's inspected study establishes interaction with SPD_0076 and uptake modulation; its broader term reflects that evidence. KhtT regulates a cation/proton antiporter, so it is not an equivalent channel-regulator comparator.
