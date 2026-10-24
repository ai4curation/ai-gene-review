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


## 2026-10-10: substantive campaign audit (supersedes earlier decisions)

The published 48 assertion objects, two product records, GOA, UniProt, 41 existing reference caches and genuine older provider report are preserved. Normal fresh intake reproduced the same assertion objects/products. The new bounded Falcon/fallback attempt failed; this audit uses manually inspected primary evidence, documented in [the source ledger](CEP164-manual-evidence.md) and [bounded machine-field extract](CEP164-source-evidence.yaml).

The six earlier generic-binding removals are superseded by KEEP_AS_NON_CORE for supported associations under the [standing ClinGen instruction at the authenticated baseline](https://github.com/ai4curation/ai-gene-review/blob/498c72e4bea435fe5f11cd82010fe5024c3dd791/projects/CLINGEN_MENDELIAN.md). Exact target records, tagged constructs and assay hosts are distinguished. TTBK2-specific annotations still MODIFY to protein kinase binding. The NPHP3/NPHP4 and DVL3 assays are actually present in the original full paper; the short anchor [PMID:22863007 "CEP164 with NPHP3"] identifies the relevant target passage without repeating its whole text.

Tear proteomics is now KEEP_AS_NON_CORE: original full XML Table II names CE164_HUMAN/CEP164. This overturns the earlier reasoning from an omitted table and a hypothetical debris explanation. Detection is retained without claiming secretion or an extracellular function.

The main core is TTBK2 binding and recruitment at the mother-centriole distal appendage. Direct Rabin8 binding and the vesicle-docking role remain in the biological synthesis, but extract-associated Rab8 is not relabeled a direct purified interaction: [PMID:23253480 "Rabin8, but not Rab8"]. Nor does kinase recruitment imply activation. Human construct/mutant/rescue scope, peptide-fusion structural limits and unresolved local Rabin8 imaging are recorded in the source ledger. A separate MF-free duplicate core is unnecessary.

Centrosome/centriole/transition-fiber and cilium-assembly annotations remain core. The IBA activity qualifiers are supported by actual localized recruitment work, not location alone. Source-specific human microscopy is separated from mouse/worm experiments; the original human centrosome source describes [PMID:21399614 "appendage structures of the mature centriole"]. Reactome cytosol remains broad non-core location with authentic event identities and compartment fields, without transferring other proteins' catalytic roles.

The two nuclear annotations remain UNDECIDED after inspecting positive primary/HPA evidence and the later genome-editing study. This is a substantive context/reagent conflict, not simply failed retrieval. No universal negative nuclear function or proven cross-reactivity is asserted.

No NEW annotation or new product assignment is made. The existing source coverage already contains cilium assembly and the relevant locations; no missing-process claim is inferred from necessity alone. The previous notes are preserved byte-for-byte above as required by the append-only journal policy. Duplicate YAML quotations are removed; sources already over budget solely in that inherited prefix receive zero new quoted words. Current additions stay within the remaining per-source budget, with legacy excess explicitly disclosed rather than silently rewriting the old journal.

A later primary study refines the docking model: [PMID:42288497 "CEP164 knockout blocks ciliogenesis at the DAV stage"]. The new reference and narrow finding dispute preserve the older binding evidence; all original annotation actions remain unchanged.


## 2026-10-10: PR #4508 evidence-anchor follow-up

The accepted biological decisions and all 48 original assertion objects remain unchanged. Short exact publication anchors now identify the TTBK2 complex/recruitment evidence in PMID:24982133, the isolated binding and kinase-activation boundary in PMID:34499853, the primary ciliation result in PMID:17954613, appendage-complex membership in PMID:29789620, direct purified Rabin8 binding in PMID:23253480, and the negative nuclear-localization observation in PMID:26966185. The latter appears on both UNDECIDED nuclear rows and remains scoped to the tested contexts; positive primary/HPA evidence is retained. These are excerpts from the exact unchanged publication caches, not substituted file-reference quotations.

The 25-word-per-source limit is an authoring constraint for this follow-up, not a repository validation rule. The earlier journal discussion that assigned no new excerpts to papers with long inherited-note quotations is superseded for this follow-up: the complete inherited notes remain an exact byte prefix, and the current YAML plus this newly authored append are counted separately, including every repeated excerpt. The six newly anchored sources total 18, 21, 20, 18, 17 and 9 words respectively for PMIDs 24982133, 17954613, 29789620, 26966185, 34499853 and 23253480. This append introduces no further literature quotations. It does not claim the unchanged historical notes meet a retrospective quotation limit.

PMID:26966185 is removed from the 21 cytosol supported_by lists because it supports the nuclear-localization conflict rather than the event-specific Reactome compartment. Each row retains its original Reactome reference and genuine source extract. The HDA tear-fluid detection remains non-core with its existing detection, secretion and localization limits; comparisons with other genes do not replace the target-specific source assessment. The Rabin8 interaction remains distinct from the TTBK2 molecular-function core and does not establish a separate GEF or defined ternary-adaptor activity. No new annotation, changed action, product assignment or source-cache edit is made.
