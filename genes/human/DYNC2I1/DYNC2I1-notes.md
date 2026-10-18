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


## 2026-10-18 source-specific augmentation

The 56 historical source assertions and their machine metadata are preserved exactly. Current ordinary fetching reconciled all 56 contexts one-to-one, with no added or retired assertion. The accepted review has 33 ACCEPT, 10 MODIFY, 12 KEEP_AS_NON_CORE and one REMOVE; no NEW annotation is proposed. This entry supersedes the earlier generic-removal recommendation for NUDC and the earlier tear-proteomics over-annotation judgment without rewriting the historical notes above.

The two NUDC associations are refined to protein-folding chaperone binding. Literal human interaction records identify the participants, and independently purified human NUDC suppresses reporter aggregation in PMID:21530541. This describes the partner class, not folding by DYNC2I1 or a demonstrated NUDC-dependent folding pathway for DYNC2I1. TCTEX1D2 and DYNC2I2 pairs are separately refined to light-chain and intermediate-chain binding. The project-specific CLINGEN policy retains supported generic binding as non-core when no justified specific term is available; it does not require removal merely for genericity.

The nuclear NAS decision rests on the actual dynein-1 reagents and nuclear figure caption in PMID:36973253, together with a target-name survey of the original and six supplements. It does not infer impossibility from nuclear topology. The same paper reports mouse Wdr34 among selected Y2H hits; that is positive dynein-2-related evidence, but it does not establish WDR60 nuclear localization. Absence from the selected hit list is not an exhaustive negative binding experiment. By contrast, the original tear-proteomics Table II positively identifies WDR60, so extracellular detection is retained as non-core without inferring secretion, contamination or extracellular function.

The seven PAINT assertions have literal IBD joins on the reconstructed PTHR16022 target lineage, with exact official-sequence agreement. The target appearing among its own experimental descendants is expected. Broad cytoskeleton/cytoplasmic-dynein-complex assertions are refined to the supported cytoplasmic dynein complex. Broad intraflagellar transport is refined to intraciliary retrograde transport. The tip assertions are core-relevant states of the principal transport cycle, with their Reactome-model provenance preserved; no new human residence-time or velocity measurement is asserted. Ciliary base and tip, and cilium assembly and retrograde transport, are each nonredundant pairs under current typed ancestry.

The single integrated core distinguishes the intermediate chain's light-chain binding from its contribution to complex-level motor activity. DYNC2I1 does not supply ATP-driven force. The accepted structural evidence uses recombinant human subunits in insect cells and docking to an algal IFT train; those contexts are not conflated. The human RPE1 knockout study explicitly lacked reliable quantitative IFT measurements, used crosslinking for anti-HA coimmunoprecipitation, and showed distinct WDR60 and WDR34 phenotypes. No autonomous axonemal polymerization or universal loss of cilia is inferred. One official displayed Q8WVS4 product has 1,066 residues. Engineered fragments, disease alleles and knockouts are not natural alternative products.

The earlier successful Falcon report and all of its artifacts remain unchanged. The current configured Falcon attempt failed with HTTP 403; the genuine fallback attempt failed with HTTP 401 and an insufficient-quota response. No replacement provider report was fabricated. Existing publication bytes and availability flags remain unchanged, including short full-text representations; newly obtained fuller copies were used as separately accessed research evidence and were not silently substituted. Only the genuinely fetched, independently used PMID:21530541 cache is proposed as a new publication file. Three additional normal-fetched metadata sources were not needed for the decisions and remain private.

The [source guide](DYNC2I1-source-guide.md) gives primary locators, actual read scopes and access limits. The [portable evidence audit](DYNC2I1-bioinformatics/evidence-audit/RESULTS.md) reproduces the database joins from saved raw inputs. The original notes remain an exact prefix. All 27 inherited row excerpts and eight inherited note excerpts are retained. Four old core excerpts are removed as part of the authorized consolidation of the overlapping cores; no new source quotation is introduced, and no claim is made that the historical excerpt totals fall below a new-quotation budget.
