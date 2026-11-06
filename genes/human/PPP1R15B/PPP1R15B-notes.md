# PPP1R15B (CReP) review notes

## Literature search (no deep-research provider available)
Sources checked: UniProt Q5SWA1 (curated FUNCTION, SUBUNIT, DISEASE); all 11 GOA-cited PMIDs cached via
`just fetch-gene-pmids`; PMID:14638860 (Jousse et al. 2003, CReP discovery; already cached for the ISR module).
Context only: integrated stress response module, crep_pp1_regulator annoton (module proposed in ai4curation/ai-gene-review#5904).

## Key findings
- Constitutive eIF2alpha phosphatase subunit: [PMID:14638860 "Here, we report on identification of a regulatory subunit of a constitutive eIF2α phosphatase complex that regulates basal levels of eIF2α phosphorylation."] (work largely in rodent cells)
- Human genetics: [PMID:26307080 "We show that patient cells have greatly diminished levels of PPP1R15B-PPP1C interaction, which results in increased eIF2α phosphorylation and resistance to cellular stress."]
- Substrate recruitment: [PMID:38159565 "We found that R15B binds eIF2 with high affinity, without requiring PP1 or any other factors."]; [PMID:38159565 "H1 and H2 form a clamp that grasps the substrate in a region remote from the phosphorylated residue."]
- Localization: no PPP1R15B-specific compartment found in these sources; ER rests only on IBA (GADD34-type targeting).

## Source defect found
DisProt IPI rows (PMID:34847777, PMID:38159565) list UniProtKB:Q9BY44 (EIF2A, eIF-2A) as the eIF2 partner;
correct partner is EIF2S1 (P05198) (and EIF2S3 for the trimer contacts). Same issue as PPP1R15A.

## Decisions
- PP1c protein-binding rows -> protein phosphatase 1 binding; TRIM23 HuRI row removed.
- negative regulation of protein phosphorylation (IMP) -> GO:0036496 (acts by dephosphorylation).
- molecular adaptor activity -> enzyme-substrate adaptor activity (GO:0140767).
