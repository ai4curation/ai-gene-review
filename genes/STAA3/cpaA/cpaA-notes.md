# cpaA receptor review notes

## 2026-11-04 — cyclic di-AMP receptor audit

Primary PMID:26171638 was available as an abstract; ACS full text returned HTTP 403. Its erratum PMID:29984582 (publisher DOI 10.1021/acs.biochem.8b00686) corrects only the PDB code to 5F29. Do not infer transport direction or K+/Na+ specificity from the RCK domain name. Two potassium-specific IEA process rows remain UNDECIDED. The family assignment supports cation/proton exchange, not a separate potassium-channel regulator role.

Falcon deep research was attempted using `just deep-research-falcon STAA3 cpaA` and failed with HTTP 403 authentication failure. This is manual primary-source research, not a provider-generated report. The original machine annotation payloads and raw UniProt/GOA files are retained. No NEW annotation rows were added in the initial pass; the follow-up below records the final recommendation.

- [PMID:23671116](https://pubmed.ncbi.nlm.nih.gov/23671116/): CpaA directly binds c-di-AMP through its regulatory region. "a predicted cation/proton antiporter, CpaA, which as we show here also directly binds c-di-AMP."
- [PMID:26171638](https://pubmed.ncbi.nlm.nih.gov/26171638/): The full-length CpaA antiporter responds to c-di-AMP in proteoliposomes; the abstract does not identify the ion or sign. "proteoliposome activity assay using the full-length SaCpaA membrane protein indicated that c-di-AMP binding alters its antiporter activity by approximately 40%."

Module membership: `MODULE:bacterial_c_di_amp_signaling`, receptor arm. No unsupported top-level association slot is used.

## 2026-11-04 — PR #5997 review follow-up

Clarified why the KtrA channel-regulator term does not transfer merely from a shared RCK domain: CpaA has a fused membrane antiporter module, whereas KtrA is a separate gating component of the KtrB/KtrD system. The existing MODIFY already proposes GO:0180001, so no redundant NEW binding row was added. The UniProt PANTHER cross-reference PTHR43562:SF1 is named “NA(+)_H(+) ANTIPORTER YJBQ-RELATED”; this is family-classification context that cautions against automatic potassium specificity, not experimental proof of sodium selectivity. The two potassium-specific process rows remain UNDECIDED because the accessible primary abstract does not resolve the transported ion.
