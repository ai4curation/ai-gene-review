# PSEPK nitrogen-regulatory PTS review, 2026-11-07

Complete manual review of PtsP Q88CN5 (PP_5145), NPr/ptsH Q88PA2 (literature ptsO; PP_0948), and PtsN Q88PA0 (PP_0950), all KT2440. All 18 original ordered rows remain: 11 machine rows and seven historical NEW rows. Six historical proposals remain active; one redundant NPr phosphorus-transfer proposal is retired in place. No newly authored rows. All six raw files, existing generated research, original qualifiers and other original payload fields are unchanged. Full earlier reviews, including superseded core assertions/reference assessments, remain in before.json.

## Decisions and module handoff

- PtsP: accept native PEP-dependent activity GO:0008965; broad GO:0016772 becomes MODIFY to that existing activity. Historical protein-phosphorylation proposal remains. Cytoplasm is inferred from native intracellular function and architecture, not ARBA-only text or an unperformed localization assay.
- NPr: both kinase GO:0016301 and generic transferase GO:0016740 become MODIFY to GO:0016775, phosphotransferase activity, nitrogenous group as acceptor; core uses GO:0016775. Kinase is not rejected because the donor is phosphohistidine: the definition allows non-ATP donors. GO:0016775 is a chemical-acceptor refinement across branches relative to kinase, and a verified descendant relative to transferase. Historical NEW GO:0016772 is retired because it is an ancestor of this supplied refinement. The old NEW action/payload/order is preserved. No specific immediate child accurately describes NPr His-to-His transfer. ATP-dependent histidine kinase and hybrid-kinase/response-regulator transfer terms are inappropriate.
- PtsN: carbohydrate-transfer/transport annotations remain REMOVE, supported by native separation of the regulatory and sugar-transport branches. Kinase activator GO:0030295 is UNDECIDED, and the prior kinase-regulator replacement/core is withdrawn: native KdpD interaction plus transporter-promoter repression does not distinguish kinase inhibition from phosphatase activation or another mechanism. Retain historical potassium-transport regulation as control of transporter expression, not measured potassium flux. Retain PDH enzyme-inhibitor activity with native cellular/extract scope. The core uses PDH inhibition with intracellular signaling context; being a phosphoacceptor alone is not the participation argument. All four PtsN historical NEW rows remain active.

Native pathway continuity is PEP → PtsP → NPr → PtsN. Do not model it as a permanently assembled complex, universally obligatory route under all media, carbohydrate transport, or universal conserved terminal-output mechanism. Fructose enables FruB cross-talk, including bypass of the PtsP route. The native paper's Figure 4 distinguishes inferred arrows from prediction and says reverse NPr/PtsN transfer has not been proved in vivo. Target-specific GAF ligands are unresolved.

## Evidence and exact snippets

PMID:18296519 canonical cache contains abstract/Discussion; the independently archived complete PMC body adds Methods, Results and figure captions. Experiments use MAD2, a KT2440 derivative, with nonpolar PTS mutants and plasmid-expressed E-tagged PtsN. This is native-strain physiological phosphostate evidence, not homogeneous purified-target kinetic evidence.

> Our results show that the source of phosphate available to the system is PEP and that the primary flow of phosphate through the N/C-sensing PTS proceeds from PEP to EI(Ntr) to NPr to EIIA(Ntr).

Full Results, scoped to the carbohydrate-free condition:

> This indicated that PtsO is the only phosphate-delivering protein for PtsN under these conditions.

PMID:26224366 accessible primary abstract:

> Measurements of kdpFp promoter activity in different pts mutants showed that PtsN is responsible for repression of kdpFABC transcription.

> Bacterial two-hybrid assays demonstrated that kdpFp regulation is implemented through direct interaction of the PtsN protein with the sensor kinase KdpD of the KdpD/KdpE two-component system.

These observations support a signaling interaction but do not measure the target kinase/phosphatase activities separately. PMID:19400808 is E. coli evidence and cannot supply the missing target catalytic direction.

PMID:21236318 accessible primary abstract:

> Both genetic and biochemical evidence revealed that the non-phosphorylated form of PtsN is the protein species that inhibits PDH.

> Expression of PtsN and AceE proteins fused to different fluorescent moieties and confocal laser microscopy indicated a significant co-localization of the two proteins in the bacterial cytoplasm.

Reported methods are co-immunoprecipitation/MS and PDH activity in isogenic cellular extracts, not a demonstrated purified binary affinity/inhibition experiment. Both target abstracts remain full-text-unavailable after central acquisition attempts. The existing OpenScientist report remains intact as secondary literature discovery; centralized Falcon authentication failed HTTP 403, and no invented provider report was substituted.

## Checks and limits

Focused production schema, reference quotations/titles, GOA and best-practices validation passed all three genes with zero errors. Record-section backfill added six provenance section tags. Initial batch summary reported two warnings; diagnostic single-file checks returned zero for PtsP and one for PtsN. Final PtsN advisory verbatim:

`No annotations reference available deep research files (ptsN-deep-research-openscientist.md)`

The report is assessed as a secondary reference; primary evidence is cited directly, so no artificial provider quotation was added to silence that advisory. Three helper-generated codex/gpt-6 histories passed LinkML history validation. Three derived HTML renders passed. Ordered payload, historical NEW lifecycle and protected byte/mode checks pass in preservation-proof.json.

After the parent confirmed that the shared ontology environment was reusable, all three full per-gene `just validate PSEPK <gene>` commands passed, including `--terms` ontology labels/branches, schema, references, GOA and best practices. PtsP and PtsH have zero warnings; PtsN has only the provider-citation advisory quoted above. No new environment or large ontology build was created. Full-corpus validation was not run. Small official QuickGO definition/ancestor/child responses are frozen with retrieval URLs and SHA256s and establish the specific refinement/retirement relationships. The source-closure ledger resolves local and PMID sources explicitly; GO_REF entries are method provenance. No module/family/project/git-state edits were made.
