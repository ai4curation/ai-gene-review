# Independent scientific review of the Mla draft

Reviewed 2026-11-07. This is a read-only scientific review of the current module, root reference assessment, eighteen gene syntheses, six family assessments, and the capacity consultation. No curated files, frozen receipts, sources, or shared code were changed. `reviewed-inputs.json` records the exact 71-file snapshot. Family and capacity work was still being finalized, so this is not an unconditional release approval.

## Assessment of the biological model

The three-interface architecture and the two sampled inner-membrane realizations are supported. I found no new biological contradiction requiring removal of a sampled exemplar or reversal of the ATP-coupled retrograde interpretation. The draft appropriately avoids a universal bacterial occurrence claim, a universal named porin, a complete PAO1 pathway claim from its carrier alone, and treating passive reverse exchange as equally established ATP-driven anterograde transport.

The literature objective is substantively met: PMID36459067, PMID38802775 and PMID35850151 are three genuine reviews, with distinct contributions (directional evidence; MlaA and lineage organization; comparison with other lipid-transfer systems). The last is a 2022 review despite its later PMC deposit. Primary evidence is mined near the outer interface, carrier interface, assembly variants and connections rather than relying entirely on reviews.

All eighteen representatives are meaningful: six E. coli, six KT2440, five Bordetella reference-locus members, and the directly studied PAO1 carrier. These are three matched architecture panels plus a partial biochemical comparator, not eighteen independently assayed complete pathways. The six official classifications are appropriate selectors for the named exemplars; the unusual chloroplast-related official label of PTHR30188:SF4 must remain verbatim. Mixed cargo and cellular contexts within several subfamilies prohibit a family-only capacity grant. The older Q88P90 flat file lacks the current MlaB classification; the separately archived official snapshot supplies that bridge without changing the frozen source.

Bordetella is reasonably modeled as an assembly **without an identifiable MlaB homolog**, supported by the five-gene locus and B213 physiology. It is not a purified demonstration that three isolated F/E/D proteins alone suffice. The primary perturbation is MlaF, with the strongest lipid-asymmetry phenotype involving the parallel OMPLA pathway; the other four roles rely on specific architecture and cognate locus evidence, with direct deposited carrier-binding evidence added independently. The B213-to-Tohama I lineage bridge is correctly weaker than whole-construct sequence identity. The E. coli overexpressed-MlaF rescue is a separately acknowledged conditional context, not a license to omit B from arbitrary panels.

Both directional edges are explicitly bounded to E. coli experiments. The first describes outer-complex loading of MlaC; the second describes carrier delivery to the ATP-coupled inner assembly. Their truth does not require a claim of directly measured native KT2440 or Bordetella directional flux. PMID28388411 is correctly restricted to physical interaction/model evidence, and the NBD-PE correction uses the actual figure caption without changing the erroneous source prose.

## Material release dependency: declaration-aware capacity checks

In the checker snapshot first inspected, `unit_ok` called `core_activity(member, role)`, which tested hardcoded biological-role requirements, but did not compare them with the current `annoton.function` or `active_unit.function`. `structural_contract` checked role/atom inventory and routes, not function declarations. A changed MlaF unit function or deleted carrier function could therefore escape these tests even though it altered the module's scientific assertion.

Recommended correction: independently bind each encoded function declaration to its source-supported role and corresponding reviewed core, and add changed/deleted declaration mutation witnesses. Retain the existing source, identity, location, assembly, cargo, ATP and matched-panel gates. The capacity owner acknowledged this and was implementing it; their final receipt and rerun must be inspected before publication. This finding does not mean the current declared activities are wrong.

The source gate is deliberately a curated finite-panel gate, not automated literature entailment. Cross-panel failures mean compatibility was not established for that profile, not that all mixed-species combinations are biologically impossible. The production compiler's omission of active-unit/context/edge semantics remains an explicit limitation; the wrapper must not be presented as a genome-wide classifier or native-flux assay.

## Concrete source and wording improvements

1. **Use fuller step-specific excerpts.** Current statements are scientifically supported, but several excerpts are too short to carry their full meaning. Replace the PMID28388411 fragment with its complete BLI sentence:

   > We observed robust and specific binding of both MlaFEDB (Figure 4F) and MlaA-OmpF assemblies (Figure 4G) to MlaC, as well as a direct interaction between MlaC and MlaD (Figure S4I).

   For PMID39080293 use the caption sentence already verified in the member consultation:

   > Fluorescence increase corresponds to a reduction in NBD-PE FRET quenching by Rhodamine-PE as lipids are transferred from the MlaA proteoliposome to the MlaFEDB proteoliposome.

   For the first directional edge use PMID40168124:

   > We demonstrate that OmpF3–MlaA simultaneously recruits apo MlaC and phospholipids, thus greatly enhancing lipid transfer to MlaC in solution.

   For the second edge add PMID34873038's positive result rather than relying only on the negative anterograde statement:

   > We reveal that MlaC spontaneously transfers PLs to the IM transporter in an MlaD-dependent manner that can be further enhanced by coupled ATP hydrolysis.

   The capacity ledger's original PG-enrichment quote supported cargo profiling rather than the adjacent loading claim. Its owner is replacing that quote with the loading sentence above.

2. **Make the PAO1 inference boundary explicit in `reference-assessment.yaml`.** The current “direct work ... establishes a ... carrier” wording is reasonable biological synthesis but can be read as a direct intermembrane-transfer assay. Suggested replacement: “PAO1 Ttg2D has direct structural, binding/reloading and native-host periplasmic cargo evidence. These data and its specific MlaC architecture support a carrier role; this study does not directly reconstitute membrane-to-membrane transfer or establish complete native pathway direction.” The module's carrier-step evidence already approaches this distinction. The target deletion/complementing expression and heterologous structural construct should remain distinguished.

3. **Add the step-local PMID29848551 to the reference-assessment ledger.** The module cites it at the outer-interface complex, but the root ledger currently assesses fifteen other PMIDs and omits it. Its full cached primary text supports the OmpC-adjacent integral MlaA channel; it is not a cross-species porin assignment. This is a coverage/provenance omission, not a reason to discard the supported step.

4. **Bound the remaining universal knowledge-gap wording.** The module near line568 says no STAS-domain NTP-binding or regulatory activity has been demonstrated for MlaB orthologs outside E. coli. No exhaustive negative literature survey is supplied for that assertion. Prefer: “The precise effects of the sampled non-E. coli MlaB-like proteins on cognate ATPase stability and activity remain inferred; no independent catalytic activity is assigned here.” The lack of a known kinase or demonstrated phosphorylation should not be converted into absence of all regulatory contribution.

5. **Clarify descriptive activity scope, not a new autonomous-function claim.** `ModuleAnnoton` explicitly says its function/process fields are role descriptors rather than direct GO annotation exports. Therefore the outer and inner interfaces' GO0120014 descriptors, read with their contribution language and required carrier node, need not imply that isolated MlaA or MlaFEDB completes the entire aqueous carrier reaction. Still, preferred wording such as “contribution to phospholipid transfer at the outer interface” would reduce ambiguity. Do not export these descriptors as independent enables annotations: the gene syntheses correctly retain contribution cores and distinguish MlaD's real donor handoff from the complete carrier definition.

6. **Resolve family receipt dependencies and stale completion prose.** The family owner was preparing an additive correction to residual universal MCE-partner wording in PTHR43023 GO0043190 and old substrate-pruning language in the MlaE/MlaD lipid-transport reasons. These are not evidence to reject the named members. Require their final receipt before declaring family review complete. Update the module's “consultations remain pending” note only after the actual releases; a green schema alone does not resolve these scientific and provenance dependencies.

## Conclusion

The draft's current biological route and taxon limits are defensible. Publication closure remains conditional on the declaration-aware capacity rerun and final family receipt, plus the bounded source/wording corrections above. No additional gene annotation, invented activity, universal MlaB requirement, or new anterograde variant is recommended. Existing gene handoffs remain frozen.
