# ABTB2 manual deep research fallback

Falcon deep research was attempted with `just deep-research-falcon human ABTB2 --fallback perplexity-lite`. Falcon timed out after 600 seconds, and the configured fallback failed with a Perplexity API quota error. This manual fallback records the evidence used for the ABTB2 Proteostasis PN review.

## Summary

ABTB2 (UniProt Q8N961) encodes a reviewed 1025-aa ankyrin-repeat and BTB/POZ-domain protein. UniProt lists ankyrin repeats, a BTB domain, ABTB2/3 histone-fold-like features, and sparse functional annotation, with the statement that ABTB2 may be involved in initiation of hepatocyte growth [UniProt:Q8N961 "May be involved in the initiation of hepatocyte growth"]. GOA initially contained only InterPro-derived `protein heterodimerization activity`, an IntAct/YWHAE `protein binding` row, and HPA `nucleoplasm` localization.

The Proteostasis PN projection places ABTB2 under the Cul3 substrate-receptor branch and projects `GO:1990756 ubiquitin-like ligase-substrate adaptor activity` [file:projects/PROTEOSTASIS/reports/pn_projection/pn_projected_annotations.tsv "ABTB2		Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul3 substrate receptor|BTB-BACK, variant|ankyrin"]. Because this branch contains domain-based cases, the projection was evaluated against gene-specific evidence.

The strongest direct ABTB2 evidence is the 2025 Molecular Therapy Oncology study in pancreatic ductal adenocarcinoma. The abstract reports that ABTB2 interacts with TRAP1 and promotes TRAP1 ubiquitin-dependent degradation [PMID:41322190 "ABTB2 interacts with tumour necrosis factor receptor-associated protein 1 (TRAP1), promoting its ubiquitin-dependent degradation"]. In the results, anti-ABTB2 immunoprecipitation/mass spectrometry identified TRAP1, reciprocal co-IP confirmed ABTB2-TRAP1 interaction, and ABTB2 overexpression increased pan-protein ubiquitination and mono-ubiquitinated TRAP1 [PMID:41322190 "Co-immunoprecipitation using Abs specific to ABTB2 and TRAP1, followed by western blotting, confirmed the specific interaction between ABTB2 and TRAP1"] [PMID:41322190 "multiple mono-ubiquitinated TRAP1 (Figures 8F and S10) in ABTB2-OE cells"]. The discussion further states that ABTB2 interacts with cullin-3 and interprets ABTB2 as a substrate-specific adaptor for ubiquitin-dependent TRAP1 degradation [PMID:41322190 "We also found that ABTB2 interacts with cullin-3 (Figure S9)"] [PMID:41322190 "Together, these results suggest that ABTB2, like other BTB domain-containing proteins, acts as a substrate-specific adaptor to mediate ubiquitin-dependent degradation of TRAP1"].

The 14-3-3 paper underlying the original `protein binding` row is useful only as interaction-context evidence. It mapped 14-3-3 interactomes and showed that loss of 14-3-3 binding can affect client localization/aggregation [PMID:36931259 "Here, we map the interactomes of all human 14-3-3 paralogs"]. That does not define ABTB2's molecular activity.

Older BPOZ-2 papers report Cul3 and substrate-degradation biology, but they were treated as nomenclature caution rather than primary ABTB2 evidence. The cached TdT paper states that BPOZ-2 bound CUL3 and promoted TdT ubiquitination/degradation [PMID:18429817 "BPOZ-2 bound to E3 ligase CUL3 in vitro and in vivo"]. Current identifier usage overlaps BPOZ-2 with ABTB1, so these papers should not be projected to Q8N961 without identifier-level confirmation.

## Curation conclusions

- Add `GO:1990756 ubiquitin-like ligase-substrate adaptor activity` as a new direct ABTB2 molecular-function annotation, supported by ABTB2-TRAP1 co-IP, TRAP1 ubiquitination/degradation, and reported ABTB2-cullin-3 interaction.
- Add `GO:0016567 protein ubiquitination` as a new biological-process companion annotation, because the core function includes TRAP1 ubiquitination.
- Mark `GO:0046982 protein heterodimerization activity` as over-annotated: it is domain-consistent but less informative than the direct adaptor function.
- Mark `GO:0005515 protein binding` as over-annotated: the YWHAE/14-3-3 interaction is a generic interaction record, not an informative molecular function.
- Keep `GO:0005654 nucleoplasm` as non-core localization.
