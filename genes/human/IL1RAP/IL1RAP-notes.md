# IL1RAP notes

## Literature search (2026-11-04)

No deep-research provider was available. Sources checked:

- UniProt Q9NPH3 flat file (curated FUNCTION, SUBUNIT, isoform FUNCTION notes).
- All GOA-cited publications cached via `just fetch-gene-pmids human IL1RAP`
  (20 PMIDs; full text for 22426547, 23847621, 28534174, 31736959, 32822567,
  35922511; abstract only for the rest).
- Context only, not evidence: GO-CAM gomodel:59cc772c00000000. (IL-1 signalling module/GO-CAM review
  proposed in ai4curation/ai-gene-review#5904.)

Queries (grep over cached text): "IL-1RAcP", "IL1RAP", "accessory protein",
"AcPb", "soluble IL-1RAcP", "microglia", "IL-36", "IL-33".

## Findings

- IL1RAP is the shared signalling co-receptor of the IL-1 receptor family.
  It forms ternary complexes with IL-1 + IL1R1 and IL-1 + IL1R2 (decoy)
  [PMID:7775431 "the accessory protein forms a complex with the Type I IL-1R and either IL-1 alpha or IL-1 beta but not IL-1ra"];
  [PMID:22426547 "crystal structure of IL-1β bound to its primary receptor IL-1RI and its receptor accessory protein IL-1RAcP"].
- Required for IL-1 signalling: re-expression in IL1RAP-null EL-4 cells restores IRAK and SAPK activation and NF-kB translocation
  [PMID:9065432 "IL-1RAcP is an indispensible molecule in the IL-1 receptor signal transduction complex"].
- Recruits TOLLIP-IRAK to the activated receptor [PMID:10854325 "recruitment of Tollip-IRAK complexes to the activated receptor complex occurs through association of Tollip with IL-1RAcP"].
- IL-33 co-receptor with ST2/IL1RL1 [PMID:17675517 "IL-33 and ST2 form a complex with IL-1R accessory protein (IL-1RAcP)"].
  Does not bind ligand alone [PMID:23980170 "the rigidity of IL-1RAcP explains its inability to bind ligands directly"].
- IL-36 co-receptor with IL1RL2 [PMID:21965679 "signal through the IL-1 receptor family members IL-1Rrp2 (IL-1RL2) and IL-1RAcP"].
- Soluble isoform enhances IL1R2 decoy [PMID:23847621 "The interaction of ligand-bound soluble IL-1RII with soluble IL-1RAcP increases the affinity for both IL-1α and IL-1β by about two orders of magnitude"].
- Neuronal isoform AcPb and trans-synaptic PTPRD binding are mouse data (UniProt "By similarity").
- NAS rows from PMID:23847621 (monocyte differentiation, negative regulation of IL-1alpha/beta
  production, negative regulation of inflammatory response) describe IL1R2 biology in that review,
  not IL1RAP. PMID:28534174 never mentions IL1RAP.
- PMID:10383454 (IRAK-M cloning) and PMID:10748004 (PI3K/Akt in endothelial cells) are abstract-only;
  the abstracts do not mention IL1RAP, so their IDA rows are deferred to the curators.
- NAD+ nucleosidase (EC 3.2.2.6) is a PROSITE TIR-rule inference only; no IL-1 receptor family TIR
  domain has been shown to hydrolyse NAD+.
- No OLS hit for an IL-36-specific GO receptor/pathway term (searched "interleukin-36", "IL-36 signaling").

## PR #5941 review follow-up (2026-11-06)

Comparator check for the `enables` qualifier on receptor-activity rows (QuickGO MF annotations,
fetched 2026-11-06; raw table kept outside the repo):

- IL18RAP (O95256, IL-1 family accessory chain): `enables` GO:0042008 interleukin-18 receptor activity,
  IBA and IDA (PMID:25500532), plus `enables` GO:0015026 coreceptor activity.
- IL1RL1 (Q01638) and IL1RL2 (Q9HB29), ligand-binding chains: `enables` GO:0002114 / GO:0004908.
- IL2RG (P31785): `contributes_to` IL-2, IL-4, IL-7 receptor activity (TAS); `enables` IL-15 receptor
  activity (IDA) and coreceptor activity.
- CSF2RB (P32927): `contributes_to` IL-3 and IL-5 receptor activity; `enables` coreceptor activity.
- IL6ST (P40189): `contributes_to` IL-6, IL-11, LIF, oncostatin-M receptor activity; `enables`
  oncostatin-M (two IDA), CNTF and IL-27 receptor activity, and coreceptor activity.

Conclusion: practice is mixed, but the IL-1 family convention (IL18RAP, and the PAINT IBA for IL1RAP)
is `enables`. IL1RAP also contacts IL-1beta in the ternary complex (PMID:22426547). The `enables` rows
are accepted, the convention is recorded in their `reason`, and the question of `contributes_to` for
accessory chains is raised in `suggested_questions`.

ComplexPortal decoy-complex propagations are now recorded as `source_defects` (resource OTHER,
ComplexPortal named in the explanation). The soluble isoform (Q9NPH3-2) is recorded in
`functional_isoforms`.
