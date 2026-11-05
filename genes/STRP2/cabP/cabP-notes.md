# cabP receptor review notes

## 2026-11-04 — cyclic di-AMP receptor audit

The paper explicitly identifies SPD_0077 in D39. No independent membrane-transporter molecular activity is assigned. The native interaction and uptake experiments support regulator activity in core functions; no NEW process annotation is manufactured.

Falcon deep research was attempted using `just deep-research-falcon STRP2 cabP` and failed with HTTP 403 authentication failure. This is manual primary-source research, not a provider-generated report. The original machine annotation payloads and raw UniProt/GOA files are retained. No NEW annotation rows were added in the initial pass; the follow-up below records the final recommendation.

- [PMID:24272783](https://pubmed.ncbi.nlm.nih.gov/24272783/): CabP directly interacts with the potassium transporter SPD_0076. "we showed that CabP directly interacted with a potassium transporter (SPD_0076) and that both proteins were required for pneumococcal growth in media with low concentrations of potassium."
- [PMID:24272783](https://pubmed.ncbi.nlm.nih.gov/24272783/): CabP specifically recognizes cyclic di-AMP. "We demonstrated that CabP specifically bound c-di-AMP"
- [PMID:24272783](https://pubmed.ncbi.nlm.nih.gov/24272783/): Elevated c-di-AMP weakens the interaction and potassium uptake. "the interaction between CabP and SPD_0076 and the efficiency of potassium uptake were impaired by elevated c-di-AMP in pneumococci."

Module membership: `MODULE:bacterial_c_di_amp_signaling`, receptor arm. No unsupported top-level association slot is used.
The process actions refine direct regulator roles to regulation of potassium transport; membrane translocation remains the partner activity.

## 2026-11-04 — PR #5997 review follow-up

Added NEW GO:0180001 (IDA; PMID:24272783) for the directly demonstrated binding by D39 SPD_0077. Retained GO:0141108 transporter regulator activity in the core synthesis: the inspected primary evidence demonstrates interaction with SPD_0076 and modulation of uptake. The more specific potassium-channel regulator term used for S. aureus KtrA has additional target-specific channel-system characterization in PMID:23815639; no independent pore activity is assigned to either regulator.
