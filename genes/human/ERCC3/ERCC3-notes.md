# ERCC3 annotation notes

## Biological interpretation

XPB is the ATP-driven duplex-DNA motor of the TFIIH core. Human recombinant and native-complex experiments distinguish ATP hydrolysis, measured 3′–5′ unwinding capacity, repair opening and transcriptional outputs. ATPase-defective XPB fails repair opening; selected mutants with reduced unwinding retain ATPase and repair. Human PIC structures place XPB on downstream duplex DNA, and newer human repair reconstructions show motor-dependent bubble enlargement. These findings support translocation as the principal motor interpretation without denying the historical unwinding assays. [PMID:8663148](https://repub.eur.nl/pub/56489/15898.full.pdf), [PMID:17466626](https://doi.org/10.1016/j.molcel.2007.03.009), [PMID:27193682](https://pmc.ncbi.nlm.nih.gov/articles/PMC4940141/), [PMID:41673165](https://pmc.ncbi.nlm.nih.gov/articles/PMC13378019/).

ATP hydrolysis remains accepted as separately measured chemistry. The broad hydrolase mapping is refined to ATP hydrolysis; broad helicase is refined to DNA translocase. Specific directional helicase rows remain non-core. The current GO:0043138 label and definition have inconsistent directionality, independently captured in QuickGO and OLS; imported identifiers and labels are unchanged, and experimental direction comes from the original assay.

Transcription initiation and promoter clearance are distinct supported phases. The broad Reactome transcription row is refined to both, preserving its whole pathway hierarchy. Neither phase is used to infer RNA polymerization by XPB. Acute human HAP1 depletion shows variable promoter dependence with residual protein, so the synthesis avoids universal claims of XPB necessity or dispensability. [PMID:35947745](https://pmc.ncbi.nlm.nih.gov/articles/PMC9458433/).

## Scope and source decisions

The 162 imported contexts have no PENDING decisions. TFIIH complex membership and nucleoplasmic localization are supported. The TFIID annotation citing PMID:27193682 is refined to TFIIH from the actual preparation, with a machine-readable WRONG_TERM proposal marked NOT_REPORTED. No upstream report has been submitted. The DNA-topological-change term requires linking-number change, which the cited unwinding/repair experiments do not establish. Lesion-containing structural scaffolds do not establish preferential damaged-DNA binding.

All seven PAINT target paths were traced through the actual family tree and IBD records. Self-WITH human evidence is valid. The rat developmental-expression source supports expression during organogenesis but does not establish an XPB-executed organ-development step. Hair-cell differentiation remains unresolved without assuming that the term is restricted to inner-ear cells. Reactome participant routes explicitly reach human P19447; event-level chemistry is not assigned to XPB merely because its complex is present.

Supported generic binding is retained as non-core unless a specific evidence-backed function permits refinement. Native human and experimental mouse SUG1 association support ATPase binding. Actual liver, HI-II-14, variant-screen and HuRI records were checked. The imported ADAMTSL4 -3 context remains uncertain because the inspected HuRI record maps -1. Uninspected pair-specific AP-MS data are distinguished from independent human evidence for the same partner. No interaction alone makes XPB the partner’s enzyme, transcription factor or transport receptor.

## Research and access

The genuine Falcon research attempt and perplexity-lite fallback failed with access/quota errors. No provider-generated research file was fabricated; the companion manual research and source guide document the actual work. Thirty-three directly cited source groups were assessed, with operative originals read for 21 and 12 complete originals unavailable. Additional donor and mechanistic originals have separate precise read scopes in the source guide. Failed downloads and preview/challenge pages were not treated as article access.

The 2017 liver-paper correction changes an author name, and the 2012 TFIIH-review correction changes XPD helicase direction. The linked 1996 correction to PMID:8692841 was identified, but its page-image body remains unread. Cache metadata and cached publication bytes were preserved throughout.

The single supplied natural protein is canonical P19447, 782 aa. Engineered truncations, affinity tags, disease alleles, cross-species interaction constructs and host expression cells do not create additional natural isoforms or establish equivalent activity for unreported products.

## Review outcome

The annotation review contains 93 ACCEPT, 12 MODIFY, 8 UNDECIDED, 47 KEEP_AS_NON_CORE, 2 MARK_AS_OVER_ANNOTATED. It preserves all 162 source objects, the single protein boundary, 57 original publication caches, 69 original Reactome caches and two PANTHER auxiliary records. Eight genuinely acquired additional publication caches are tracked separately. No new publication quotations or new annotations were added. One core function summarizes ATP-driven DNA translocation in repair, transcription initiation and promoter clearance, while preserving the separately supported ATPase annotation and measured non-core helicase activity.


## Validation outcome

Schema, reference, GOA and best-practice checks passed with 36 advisories: 35 concern supported generic interactions retained as non-core, and one recommends citing the manual synthesis directly (the source guide is cited). The computed status is DRAFT; all 162 annotations are reviewed. The accepted core passed strict ontology label and branch validation, and the HTML review rendered successfully.

Whole-document live term validation could not finish because the OLS taxonomy service timed out on NCBITaxon:9606. Offline validation confirmed the GO core branches but could not establish the taxonomy enum because its full closure was not materialized; this is recorded as an incomplete check, not a successful whole-document term check. The official NCBI taxonomy page independently confirmed that 9606 denotes Homo sapiens. Exact existing validator-cache bytes were reused with provenance; source publication and database caches were not edited.

The subsequent canonical check on 2026-10-24 passed both `just validate human ERCC3` and the strict whole-document `just validate-terms` command. Separate component checks, computed-status verification and rendering also passed. The earlier private-workspace failures remain recorded above as provenance; the canonical retry resolved that validation limitation. All 112 normal-source dependencies retained their accepted bytes, and all 326 description, annotation-review and core narratives were present in the generated HTML.


## 2026-10-24 PR review follow-up

The current ontology distinguishes ATP hydrolysis (GO:0016887) from ATP-driven DNA translocation (GO:0015616): neither is an is_a ancestor of the other, and the ATPase term recommends retaining the overall ATP-dependent function as well. The synthesis now represents both activities of the same coupled XPB motor. The new ATPase entry adds no duplicate process assertions and is grounded in the previously inspected human assays of PMID:8663148, PMID:17466626 and PMID:41673165. The source guide remains provenance; primary sources directly support the core entries.

The two exact KPNA3 interaction contexts are refined to importin-alpha family protein binding (GO:0061676), which describes the partner class and does not make XPB a transport receptor. The broad helicase refinement now lists both the translocase and the already-supported directional unwinding activity. Retaining the latter still entails the broad helicase ancestor; the review does not claim otherwise. The standalone description now states the biological activity directly; experimental separation of hydrolysis and unwinding remains documented here and in the source guide.

The standing campaign instructions retain supported generic binding as non-core unless a more specific supported function is available, and prohibit adding publication quotations. Accordingly, 33 generic-binding contexts remain non-core, the corresponding validator advisories remain visible, and no quotations were introduced. This follows the task-specific instructions without changing the repository validator. Final actions are 93 ACCEPT, 45 KEEP_AS_NON_CORE, 14 MODIFY, eight UNDECIDED and two MARK_AS_OVER_ANNOTATED; all 162 source contexts and the natural-product boundary are unchanged.

Canonical follow-up validation passed: normal, strict whole-document terms, components, status and rendering. DRAFT retains 34 advisories (33 supported generic-binding rows and one optional manual-synthesis citation). All 327 description/review/core narratives were present in the generated HTML; the 112 normal-source dependencies retained their accepted bytes.
