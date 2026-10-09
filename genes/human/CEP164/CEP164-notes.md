# CEP164 review notes

## 2026-10-03: sources and scope

- GOA snapshot 48 rows (21 Reactome cytosol TAS); UniProt Q9UPV0. All 11 GOA PMIDs cached.
- Additional papers: PMID:24982133 (Cajanek and Nigg 2014), PMID:25297623 (Oda et al. 2014), PMID:34499853 (CEP164-TTBK2 structure), PMID:23253480 (vesicle docking, Rabin8/Rab8), PMID:26916822 (PI4P regulation), PMID:18283122 (DDR claim), PMID:26966185 (CEP164-null cells: no DDR role), PMID:29789620.
- Deep research: the coordinator's falcon run (restarted with `--timeout 2400`) succeeded (`CEP164-deep-research-falcon.md`).

## Functional synthesis

- CEP164 was identified in an siRNA screen and localized to distal appendages by immunogold EM [PMID:17954613 "One newly identified protein, Cep164, was indispensable for PC formation and hence characterized in detail. By immunogold electron microscopy, Cep164 could be localized to the distal appendages of mature centrioles."]
- It forms the blade tip near the membrane [PMID:29789620 "CEP83, CEP89, SCLT1, and CEP164 form the backbone of pinwheel blades, with CEP83 confined at the root and CEP164 extending to the tip near the membrane-docking site."]
- Main function: recruit TTBK2 [PMID:24982133 "These findings indicate that one of the major functions of Cep164 in ciliogenesis is to recruit active TTBK2 to centrioles."]; a TTBK2-CEP164 targeting chimera rescues ciliogenesis [PMID:24982133 "Remarkably, ciliogenesis can be restored in Cep164-depleted cells by expression of chimeric proteins in which TTBK2 is fused to the C-terminal centriole-targeting domain of Cep164."]. Binding is via the CEP164 N-terminal WW domain and a TTBK2 proline-rich region [PMID:34499853 "TTBK2 recruitment requires a conserved WW domain in the N-terminal region of CEP164 and a proline-rich region in TTBK2"]. PI4P at the centrosome weakens the interaction [PMID:26916822 "PtdIns(4)P binding to TTBK2 and the distal appendage protein CEP164 compromises the TTBK2-CEP164 interaction and inhibits the recruitment of TTBK2."]
- Vesicle docking via Rabin8/Rab8 [PMID:23253480 "We show that Cep164 was indispensable for the docking of vesicles at the mother centriole."]
- Disease: NPHP15 (PMID:22863007). The DNA damage response role (PMID:18283122) was not reproduced [PMID:26966185 "Furthermore, we observed no localisation of CEP164 to the nucleus using immunofluorescence microscopy and analysis of multiple tagged forms of CEP164. Our data suggest that CEP164 is not required in the DDR."]

- Deep research agrees with this picture and adds: TTBK2 also phosphorylates CEP164 [file:human/CEP164/CEP164-deep-research-falcon.md "TTBK2 also phosphorylates CEP164; CEP164 should therefore be annotated as a"]; conditional mouse knockouts show roles in multiciliogenesis (Siller 2017) and in maintaining IFT at photoreceptor connecting cilia (Reed 2022); a 2023 study assigns the centrosomal DNA-repair role to CEP170, not CEP164 [file:human/CEP164/CEP164-deep-research-falcon.md "a subsequent genome-editing study reported CEP164-null cells with defective ciliation but"]. These extra papers were not cached or annotated.

## Annotation decisions

- TTBK2 protein binding rows (two): MODIFY to protein kinase binding (GO:0019901), which is also the core MF. Other bare protein binding rows (NPHP3, NPHP4, CCDC92, DVL3, CEP83, CLP1): remove.
- Nucleus (IEA) and nucleoplasm (HPA IDA): UNDECIDED because the evidence conflicts.
- Extracellular region (tear proteomics HDA): over-annotated.
- 21 Reactome cytosol TAS rows: non-core (14 come from mitotic centrosome-maturation reactions in which CEP164 is only a member of the centrosome entity).
- Centriole/centrosome/transition fiber/cilium assembly: accept.

## HPA cilium atlas vs module role

- Module role: "distal appendage component; TTBK2 recruitment".
- HPA v25: Primary cilium transition zone (Uncertain); Centrosome (Supported); main locations centrosome, primary cilium transition zone, and sperm principal piece.
- Comparison: centrosome (Supported) and a transition-zone-level signal fit a distal appendage/transition fiber protein at the ciliary base. HPA does not reach the resolution of the appendage tip. The module role matches the literature exactly; core_functions (protein kinase binding/TTBK2 recruitment, plus vesicle docking) are consistent with it. The principal-piece signal in sperm is not explained by known CEP164 biology and is not used. No disagreement.
