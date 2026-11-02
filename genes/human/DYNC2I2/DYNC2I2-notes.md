# DYNC2I2 (Q96EX3) research notes

Cytoplasmic dynein 2 intermediate chain 2 (WDR34; FAP133 homolog), human.

## Deep research status
Falcon deep research succeeded (`DYNC2I2-deep-research-falcon.md`; the first attempt with the 600 s default timed out, and the rerun with --timeout 2400 succeeded). Its summary agrees with the publication-based review below. The review's supporting quotes come from the cached publications.

## Summary of function
- A dynein-2 intermediate chain. [PMID:25205765 "The above data indicate that both WDR34 and WDR60 are intermediate chains of the dynein-2 complex."] Localization: [PMID:25205765 "mGFP–WDR34 localizes to centrosomes and primary cilia in serum-starved cells as well as showing a diffuse cytoplasmic distribution."]
- Light-chain binding sites: [PMID:30649997 "In this study, we demonstrated that the WDR34 intermediate chain interacts with the two light chains, DYNLL1/DYNLL2 and DYNLRB1/DYNLRB2, via its distinct sites."; "These observations together indicate that interactions of WDR34 with both DYNLL1/DYNLL2 and DYNLRB1/DYNLRB2 are essential for dynein-2–mediated retrograde trafficking of ciliary proteins."]
- KO phenotype: [PMID:30320547 "we show that WDR34 KO cells can assemble a dynein-2 motor complex that binds IFT proteins yet fails to extend an axoneme, indicating complex function is stalled"]
- Structure: WDR34 propeller binds heavy chain B (PMID:31451806).
- Non-ciliary report: TAK1-associated suppressor of IL-1R/TLR NF-kB signalling. [PMID:19521662 "Our findings suggest that WDR34 is a TAK1-associated inhibitor of the IL-1R/TLR3/TLR4-induced NF-kappaB activation pathway."] GOA carries no annotation for this (only cytoplasm EXP from this paper). It is mentioned in the description and in a suggested question.
- Disease: SRTD11 (Jeune/SRPS).

## Key curation decisions
- Protein binding: WDR60 rows changed (MODIFY) to dynein intermediate chain binding. DYNLL2 and DYNLRB1 rows changed to dynein light chain binding. HT Y2H rows (COIL, TRIM54, MEOX2 partners) REMOVE.
- Filopodium (IEA from mouse): UNDECIDED, because the primary evidence could not be accessed.
- Retrograde IFT IMP cited to PMID:29742051: WDR34-specific data were not found in the cached text. Accepted on the strength of PMID:30649997.

## HPA cilium atlas vs module role
- Module stage 4: dynein-2 intermediate chain; retrograde IFT motor.
- HPA v25: Primary cilium (Approved), Basal body (Supported), Centrosome (Supported); main locations Basal body, Centrosome and Nucleoplasm. GOA HPA rows: centrosome (non-core), cytosol (non-core), ciliary basal body (ACCEPT).
- Assessment: consistent with the module role and with published basal-body accumulation. The HPA nucleoplasm signal has no published functional counterpart and is not annotated in GOA. core_functions: contributes_to minus-end-directed MT motor activity, retrograde IFT, dynein light chain binding, cilium assembly. No disagreement.


## 2026-10-18 evidence audit and integrated mechanism

All 57 imported source assertions were preserved. The current decisions are 26 ACCEPT, 19 MODIFY, 11 KEEP_AS_NON_CORE and one UNDECIDED, with no NEW annotation. The three historical overlapping cores are consolidated into one integrated dynein-2 motor mechanism with three complementary binding activities: light-chain, heavy-chain and intermediate-chain binding; motor activity and the two processes are represented once. Ciliary basal body, nonmembrane interior and modeled tip states are complementary locations; the two existing process assertions describe nonredundant retrograde transport and cilium assembly.

The main human WDR34 light-chain study distinguishes early and later predicted frameshift clones, including elongated versus vestigial cilia, and identifies binding-site-dependent rescue (PMID:30649997). These results should not be compressed into a universal absence-of-axoneme claim. Independent structural and cell-biological readings of PMID:31451806 and PMID:30320547 informed the core; the latter used crosslinked complex capture and did not obtain reliable quantitative IFT measurements. The official product remains unsuffixed Q96EX3, 536 amino acids. Experimental fragments and knockout alleles are not additional natural isoforms.

The positive human TAK1 signaling report (PMID:19521662) remains biological context. Its inactive-complex sequestration model is not a purified kinase-inhibition mechanism, and Methods prints the same targeting sequence for two named RNAi plasmids. The mouse GFP-Wdr34 filopodial observations in PMID:28379358 were directly recovered and read; endogenous human filopodial function remains open.

The previous suggestion that PMID:36973253 lacks Wdr34 evidence is corrected: Supplementary Figure 2b contains a positive mouse Wdr34 light-chain interaction hit. That does not reconstruct the human male-germ-cell nuclear assertion, which remains UNDECIDED. HPA's uncertain nuclear observations are separately retained and are not promoted from the overall reliability score.

The positive TRIM54 and MEOX2 screen associations support informative partner-class refinements without assigning DYNC2I2 ligase or transcription-factor activity. TRIM54's current human ligase-class record is IBA, and the literal MEOX2 participant is Q6FHY5. Stable IntAct records, assay methods, feature sides and sequence checks are exposed in the [source guide](DYNC2I2-source-guide.md) and [reproducible analysis](DYNC2I2-bioinformatics/evidence-audit/RESULTS.md). The AP-MS edge and Reactome paths are likewise distinguished from binary-contact and direct-imaging experiments.

The new ordinary Falcon research attempt failed authentication; its genuine perplexity-lite fallback failed quota authorization. The historical report and all machine caches remain untouched, and manual primary reading supplies the evidence assessment. Independent core consultation by the coordinating reviewer is recorded in the private read manifest; source-specific scientific conclusions and public locators are provided here.

All inherited annotation and earlier-note excerpts are preserved. Consolidation removes only the four historical core excerpt occurrences (93 words), with no relocation, rewriting or new quotation. The full disposition ledger remains with the review provenance. Final workflow status, ordinary validation, rendering and append-only history are handled during publication.


## 2026-10-18 review follow-up and superseded decisions

This section supersedes the earlier Key curation decisions bullets and the preceding action totals. The earlier entries remain historical notes. Coilin is supported non-core binding under the explicit CLINGEN_MENDELIAN project instruction; TRIM54 and MEOX2 retain the independently supported binding-class refinements. These assert what WDR34 binds, not the partner's catalytic or transcriptional activity. Current GO definitions distinguish those claims. The literal MEOX2 record remains Q6FHY5; the single length difference from P50222 is an insertion outside the preserved homeobox.

The recovered mouse GFP-Wdr34 fluorescence remains positive, but the electronic human filopodium assertion is now MARK_AS_OVER_ANNOTATED. The paper calls the protrusions filopodia-like and images GFP/acetylated tubulin rather than independently resolving an actin-based filopodium compartment. This limits the transfer without calling the fluorescence an artifact or demanding an assigned function for a localization annotation (PMID:28379358).

The intraciliary-transport refinement remains retrograde. Effects on both directions of the coupled transport system do not establish that dynein-2 performs the anterograde step; the row now explicitly cites the WDR34 binding/rescue and human structural evidence (PMID:30649997; PMID:31451806). The inherited bidirectional excerpt is unchanged. The already accepted axonemal association is now included among core locations, with no dynein-arm claim. GO_REF method references have LOW biological relevance and distinct method-specific explanations.

The male-germ-cell nucleus remains UNDECIDED: access to a full paper does not resolve the human compartment claim when its positive Wdr34 hit is a mouse interaction screen and the localization reagents concern different dynein components. All 57 source assertions and 23 inherited row excerpts remain exact. Current actions are 26 ACCEPT, 19 MODIFY, 10 KEEP_AS_NON_CORE, one MARK_AS_OVER_ANNOTATED and one UNDECIDED. There are no NEW annotations or new quotations.
