# snf-12 (O45813) review notes

Deep research was skipped: the falcon provider times out in this environment and
perplexity-lite is not installed. This review relies on cached publications instead.

- SLC6 family transporter in the epidermis. It is required for nlp-29 AMP induction after
  D. coniospora infection and for STA-2 function [PMID:21575913 "we identify the sodium-neurotransmitter symporter SNF-12, a member of the solute carrier family (SLC6), as being essential for both these immune signaling pathways"].
- Binds STA-2 through its C terminus [PMID:22470487 "STA-2 that physically interacts with the C-terminus of the SLC6 transporter SNF-12"].
- Its transport substrate is unknown [PMID:26716073 "SNF-12/SLC6 is predicted to be a transporter of a bioactive amine, but its endogenous substrate has yet to be identified."].
- It sits in an undefined apical compartment that does not colocalize with plasma-membrane, endosome or lysosome markers, and is recruited to wounds along microtubules [PMID:31995031 "This indicates that SNF-12 is in a yet-to-be defined apical membrane compartment."].

Decisions:
- IBA transporter MF/BP terms: kept as non-core. They are plausible family inheritance but untested.
- Plasma membrane IBA and glycine import IBA: marked as over-annotated, based on the localization data
  and the unknown, non-glycine predicted substrate.
- Core MF: GO:0097677 STAT family protein binding. The module annoton gives no MF, which is
  consistent in spirit, since no catalytic or transport MF is established.
