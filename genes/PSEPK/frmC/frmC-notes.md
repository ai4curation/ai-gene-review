# frmC evidence notes

## 2026-08-11

UniProt assigns PP_1617/Q88MF4 to the S-formylglutathione hydrolase family and
EC 3.1.2.12, but the record is unreviewed and inferred from homology. The
reaction-level assignment therefore remains a high-confidence family inference,
not a direct KT2440 enzyme assay.

The cached full-text KT2440 study reports that PP_1617 is induced 2.597-fold by
0.5 mM formaldehyde and that the PP_1617 mutant has an 8.7-hour doubling time
at 1.5 mM formaldehyde versus 2.1 hours for the parent. This supports a role in
formaldehyde tolerance, but the paper calls PP_1617 an esterase and does not
assign it to the FrmA-FrmC glutathione route. [PMID:21261833 "PP_1617Esterase,
putative2.597Y"; PMID:21261833 "PP_1617Esterase, putative8.7"]

The same study recovered a PP_3970 mutant in a separate formaldehyde-sensitivity
screen and called the locus `fhdA` and glutathione-dependent, but it did not
biochemically assay that assignment. [PMID:21261833 "the fhdA gene encoding a
glutathione‐dependent formaldehyde dehydrogenase (PP3970)"] The earlier KT2440
genetic study uses `fdhB` during a comparative sequence-annotation analysis.
[PMCID:PMC2687156 "The PP0328 gene was annotated as fdhA, whereas the PP3970
gene was called fdhB (Table 1)."] Its knockout experiment supports a
contribution of PP_3970 to labeled-formaldehyde mineralization, not the proposed
substrate chemistry or glutathione dependence. [PMID:19304846 "The results
showed that both enzymes contributed to formaldehyde catabolism."] The current
exact UniProt record, Q88FV8, instead names the locus `ybdR` and assigns only a
generic zinc-dependent, NAD(P)-binding oxidoreductase function. The name,
formaldehyde-dehydrogenase chemistry, and glutathione dependence of PP_3970
therefore remain unresolved. PP_3970 is outside the FrmA-FrmC module because it
is not evidence for either defined FrmA/FrmC step, not because it has been
proven glutathione-independent. [UniProtKB:Q88FV8]

Direct enzyme assays and isotope-resolved genetics are still needed to establish
whether PP_1616 and PP_1617 operate consecutively in vivo.
