# ASPDH notes

- Bioinformatics (ASPDH-bioinformatics/RESULTS.md): the catalytic His is probably retained (H223), and there is no mammalian quinolinate synthase (EC 2.5.1.72, with an E. coli positive control). The cofactor preference cannot be called: the first version claimed the NAD-specific ribose Asp was lost, but window checks (requested in PR #4318 review) show a plausible counterpart at D43, so the claim is withdrawn.
- NAD+ biosynthesis IEA is removed (pathway context). The AspDH, oxidoreductase and NADP-binding IEAs are UNDECIDED.
- NAADP binding [PMID:35841763 "Isothermal titration calorimetry (ITC) experiment using the recombinantly expressed protein shows a 1:1 binding stoichiometry and a Kd of 455 nM between NAADP and mouse ASPDH."] has no specific GO term (searched QuickGO "NAADP binding", 2026-10-05; only the NAADP-sensitive channel term), so no NEW row.
- NAADP binding is not proposed as an NTR: it rests on a single abstract-only report with recombinant mouse protein that also contradicts the earlier JPT2/LSM12 receptor studies. It is recorded in the description and gap instead.
