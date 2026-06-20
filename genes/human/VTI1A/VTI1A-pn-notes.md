# VTI1A PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q96AJ9
- AIGR review status: COMPLETE
- Review batch: proteostasis-pr-1217 (PR 1217)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/VTI1A/VTI1A-ai-review.yaml](VTI1A-ai-review.yaml)
- AIGR review HTML: present - [genes/human/VTI1A/VTI1A-ai-review.html](VTI1A-ai-review.html)
- Gene notes: present - [genes/human/VTI1A/VTI1A-notes.md](VTI1A-notes.md)
- GOA TSV: present - [genes/human/VTI1A/VTI1A-goa.tsv](VTI1A-goa.tsv)
- UniProt record: present - [genes/human/VTI1A/VTI1A-uniprot.txt](VTI1A-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/VTI1A.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/VTI1A.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/VTI1A.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/VTI1A.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: VTI1A encodes a VTI1-family SNARE that mediates vesicle transport through interactions with target-membrane SNAREs and promotes membrane fusion. Its best-supported core function is SNAP receptor/SNARE-complex activity in retrograde trafficking from endosomes or late endosomes to the trans-Golgi network/Golgi, with related roles in Golgi/TGN membrane traffic and selected non-conventional cell-surface trafficking routes. VTI1A also has direct support in autophagy/autophagosome context through STX13/Vti1a-associated autophagic flux, but it is not an ESCRT-III complex component.
- Existing/core annotation action counts: ACCEPT: 37; KEEP_AS_NON_CORE: 11; MARK_AS_OVER_ANNOTATED: 1; MODIFY: 3; REMOVE: 1

## PN Consistency Summary

- **Consistency:** Mostly consistent on the trafficking/SNARE core (UniProt, PMID:18195106, deep-research notes, and review all agree on endosome→TGN retrograde SNARE function and autophagic-flux involvement via PMID:24095276). One hard contradiction: the PN type-node projects **GO:0000815 ESCRT III complex** as ok_for_propagation, but the review and notes explicitly state VTI1A "is not an ESCRT-III complex component" — it is a SNARE intersecting ESCRT/CHMP2B autophagy phenotypes only via STX13/Vti1a trafficking.
- **PN story / NEW pressure:** PN frames VTI1A as an ESCRT-III modulator/component for phagophore sealing/microautophagy. Verified GO:0000815 (OLS) is a complex-membership CC term; asserting it for a SNARE over-reaches. The genuinely supported autophagy content (autophagy, macroautophagy, autophagosome) is already captured in existing annotations from PMID:24095276. **Conclusion: over-reaches** for ESCRT-III; autophagy role already captured.
- **Evidence alignment:** Strong overlap. PN ref "Syntaxin 13… required for autophagosome maturation" = review PMID:24095276 (autophagy/autophagosome rows). PN "Role of Vti1a… nervous system disorders" (Frontiers review) is not separately cited in the YAML; the YAML adds primary SNARE papers (PMID:18195106, 19138172, 23677696) the PN rows omit.
- **Verdict:** Trafficking core solid; **PN ESCRT-III complex projection (GO:0000815) contradicts the review and is biologically wrong for a SNARE** — demote to context_only/no propagation. Autophagy already captured; no new GO term warranted.

## Full Consistency Review

- **UniProt:** Q96AJ9 · **batch:** proteostasis-pr-1217 · **review status:** COMPLETE
- **PN placement:** `ALP|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane|ESCRT-III complex activity modulator` and `ALP|Microautophagy|General microautophagy machinery|ESCRT-III complex component` ; **PN-node mapping:** group `Sealing` = mapped/ok_for_propagation → GO:0000045 autophagosome assembly; type `ESCRT-III complex component` = mapped/ok_for_propagation → GO:0000815 ESCRT III complex; class nodes context_only.
- **Consistency:** Mostly consistent on the trafficking/SNARE core (UniProt, PMID:18195106, deep-research notes, and review all agree on endosome→TGN retrograde SNARE function and autophagic-flux involvement via PMID:24095276). One hard contradiction: the PN type-node projects **GO:0000815 ESCRT III complex** as ok_for_propagation, but the review and notes explicitly state VTI1A "is not an ESCRT-III complex component" — it is a SNARE intersecting ESCRT/CHMP2B autophagy phenotypes only via STX13/Vti1a trafficking.
- **PN story / NEW pressure:** PN frames VTI1A as an ESCRT-III modulator/component for phagophore sealing/microautophagy. Verified GO:0000815 (OLS) is a complex-membership CC term; asserting it for a SNARE over-reaches. The genuinely supported autophagy content (autophagy, macroautophagy, autophagosome) is already captured in existing annotations from PMID:24095276. **Conclusion: over-reaches** for ESCRT-III; autophagy role already captured.
- **Mapping strategy:** GO:0000815 should NOT propagate to VTI1A (recommend status→context_only for the microautophagy type-node, as the sibling "modulator" node already is). GO:0000045 autophagosome assembly (verified: phagophore-enclosure process) is narrower/different from the review's evidence, which supports flux/maturation (macroautophagy + autophagosome localization), not assembly — projection is a mismatch but at worst broader-context, lower priority than the ESCRT-III error.
- **Evidence alignment:** Strong overlap. PN ref "Syntaxin 13… required for autophagosome maturation" = review PMID:24095276 (autophagy/autophagosome rows). PN "Role of Vti1a… nervous system disorders" (Frontiers review) is not separately cited in the YAML; the YAML adds primary SNARE papers (PMID:18195106, 19138172, 23677696) the PN rows omit.
- **Verdict:** Trafficking core solid; **PN ESCRT-III complex projection (GO:0000815) contradicts the review and is biologically wrong for a SNARE** — demote to context_only/no propagation. Autophagy already captured; no new GO term warranted.

## PN Dossier Context

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/VTI1A/VTI1A-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Autophagosome closure maturation and lysosome fusion | Sealing of autophagophore membrane | ESCRT-III complex activity modulator
- UniProt: Q96AJ9
- In branches: ALP
- Notes: Works with ESCRT-III complex (and is a genetic modifier for mutations in CHMP2B) for autophagosome closure, along with its binding partner STX12. Knockdown of STX12 or its binding partner VTI1A leads to accumulation of the autophagy marker LC3, affects autophagosome maturation, and blocks autophagic flux.
- PN references (titles):
    - Syntaxin 13, a Genetic Modifier of Mutant CHMP2B in Frontotemporal Dementia, Is Required for Autophagosome Maturation - ScienceDirect
    - Frontiers | The Role of Vti1a in Biological Functions and Its Possible Role in Nervous System Disorders (frontiersin.org)
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane|ESCRT-III complex activity modulator
        status=context_only scope=too_broad_to_propagate GO=[GO:0000815 ESCRT III complex]
        rationale: Reviewed as an ESCRT-III activity modulator. It is related to ESCRT-III but should not project ESCRT-III complex membership to all members.
    - [group] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0000045 autophagosome assembly]
        rationale: This group captures autophagophore closure/sealing, a late step in autophagosome assembly. Autophagosome assembly is the safer process target than autophagosome-lysosome fusion.
    - [class] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion
        status=context_only scope=too_broad_to_propagate GO=[GO:0016236 macroautophagy]
        rationale: This class is a late macroautophagy context, but the subtree mixes docking, fusion, localization, membrane-composition, and unknown late-stage roles. The class-level relation is useful for display while propagation is restricted to narrower mechanism nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 2: Autophagy-Lysosome Pathway | Microautophagy | General microautophagy machinery | ESCRT-III complex component
- UniProt: Q96AJ9
- In branches: ALP
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Microautophagy|General microautophagy machinery|ESCRT-III complex component
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0000815 ESCRT III complex]
        rationale: This leaf is a component bucket for ESCRT-III machinery used in microautophagy contexts. The shared GO assertion is ESCRT III complex membership.
    - [group] Autophagy-Lysosome Pathway|Microautophagy|General microautophagy machinery
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Microautophagy
        status=context_only scope=too_broad_to_propagate GO=[GO:0016237 microautophagy]
        rationale: The class names a real GO process, but the subtree includes machinery components and mitochondrion-derived-vesicle contexts as well as process labels. Propagation is restricted to narrower nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Projected GO annotations (2)
- GO:0000045 autophagosome assembly | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane
- GO:0000815 ESCRT III complex | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Autophagy-Lysosome Pathway|Microautophagy|General microautophagy machinery|ESCRT-III complex component

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
