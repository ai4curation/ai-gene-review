# DYNC2I1 (Q8WVS4) research notes

Cytoplasmic dynein 2 intermediate chain 1 (WDR60; FAP163 homolog), human.

## Deep research status
Falcon deep research succeeded (`DYNC2I1-deep-research-falcon.md`; the first attempt with the 600 s default timed out, and the rerun with --timeout 2400 succeeded). Its summary agrees with the publication-based review below. The review's supporting quotes come from the cached publications.

## Summary of function
- A bona fide dynein-2 intermediate chain. [PMID:25205765 "We show that the proteins encoded by the ciliopathy genes WDR34 and WDR60 are bona fide dynein-2 intermediate chains and are both required for dynein-2 function."]
- Structure: a WDR60-WDR34 heterodimer and the light chains contort the heavy chains. [PMID:31451806 "dynein-2 heavy chain are contorted into different conformations by a WDR60-WDR34 heterodimer"]; WDR60 propeller binds heavy chain A.
- Light-chain binding: [PMID:29742051 "Although WDR60 did not demonstrate a binary interaction with any other subunit (Figure 1B), we found that it interacts with the TCTEX1D2–DYNLT1/DYNLT3 dimer via its conserved region upstream of the WD40 domain"]
- Retrograde IFT: [PMID:29742051 "These observations indicate that retrograde trafficking of the IFT machinery is severely impaired in the absence of WDR60."]
- Distinct roles of the two ICs: [PMID:30320547 "In contrast, WDR60 KO cells do extend axonemes but show reduced assembly of dynein-2 and binding to IFT proteins."; "Both proteins are required to maintain a functional transition zone and for efficient bidirectional intraflagellar transport."]
- Disease (SRTD8): [PMID:23910462 "We further show that WDR60 localizes at the base of the primary cilium in wild-type human chondrocytes, and analysis of fibroblasts from affected individuals revealed a defect in ciliogenesis"]
- Non-ciliary localization in cycling cells: [PMID:25830415 "Immunofluorescence microscopy of HeLa cells with anti-Tctex1d2 or anti-Wdr60 antibodies indicated that both proteins localized to the MTOC in interphase, the spindle poles during mitosis, and the centrosomes and cytokinetic bridge microtubules during cytokinesis"]

## Key curation decisions
- Protein binding: WDR34 rows changed (MODIFY) to dynein intermediate chain binding. TCTEX1D2 row changed to dynein light chain binding. NUDC rows REMOVE (generic).
- Centrosome IDA cited to PMID:31451806: no centrosome data were found in the cached structure-paper text. Kept as non-core rather than removed.
- Extracellular region (tear proteomics HDA): MARK_AS_OVER_ANNOTATED.
- Spindle pole, interphase MTOC, pericentriolar material and centrosome are KEEP_AS_NON_CORE. Embryonic skeletal morphogenesis (patient IMP) is KEEP_AS_NON_CORE.

## HPA cilium atlas vs module role
- Module stage 4: dynein-2 intermediate chain; retrograde IFT motor.
- HPA v25: Primary cilium (Supported), Basal body (Approved), Centrosome (Supported); main locations Basal body and Centrosome. GOA HPA rows (GO_REF:0000052): cilium (ACCEPT) and centrosome (non-core).
- Assessment: the HPA ciliary-base enrichment matches published data (WDR60 concentrated at the ciliary base) and the module role. core_functions lists contributes_to minus-end-directed MT motor activity in cytoplasmic dynein complex, retrograde IFT, ciliary base and cilium. No disagreement.
