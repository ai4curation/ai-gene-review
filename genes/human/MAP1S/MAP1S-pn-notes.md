# MAP1S PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q66K74
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-14
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/MAP1S/MAP1S-ai-review.yaml](MAP1S-ai-review.yaml)
- AIGR review HTML: missing - genes/human/MAP1S/MAP1S-ai-review.html
- Gene notes: present - [genes/human/MAP1S/MAP1S-notes.md](MAP1S-notes.md)
- GOA TSV: present - [genes/human/MAP1S/MAP1S-goa.tsv](MAP1S-goa.tsv)
- UniProt record: present - [genes/human/MAP1S/MAP1S-uniprot.txt](MAP1S-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/MAP1S.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/MAP1S.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/MAP1S.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/MAP1S.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: MAP1S (microtubule-associated protein 1S; also known as C19orf5, MAP8 and VCY2IP1) is the short, ubiquitously expressed member of the MAP1 family, whose other members (MAP1A and MAP1B) are largely neuron-specific. Like its paralogs, MAP1S is synthesized as a precursor that is proteolytically processed into a heavy chain and a light chain which re-associate into a heterodimer; both chains bind microtubules, and the light chain additionally binds actin. Its core molecular activity is binding tubulin/microtubules and cross-linking and bundling them, contributing to microtubule cytoskeleton organization and stabilization. MAP1S is distinguished functionally by acting as a bridge that couples the autophagy machinery to the microtubule cytoskeleton and to mitochondria: it binds the autophagosome-associated Atg8/LC3 protein and recruits it to stable microtubules, and it binds the mitochondrion-associated protein LRPPRC (which links to the mitophagy initiator Parkin), thereby promoting autophagosome biogenesis, trafficking and degradation and the clearance of defective mitochondria. Consistent with this, loss of MAP1S causes accumulation of defective mitochondria and impaired responses to nutrient stress. MAP1S also has cytoskeletal and mitotic roles, anchoring the microtubule-organizing center to the centrosome and supporting proper spindle organization and chromosome alignment; its depletion causes mitotic abnormalities. It interacts with the microtubule- stabilizing tumor suppressor RASSF1A, with WDR47/Nemitin, with the estrogen receptor ESR1, and with the NMDA-receptor subunit NR3A, and it binds DNA (but has no nuclease activity). MAP1S localizes to the cytosol, microtubules, mitotic spindle, centrosome/microtubule- organizing center, the perinuclear region (where mitochondrial aggregates form), and, as a shuttling pool, to the nucleus; in neurons it is found in cell projections and synapses.
- Existing/core annotation action counts: ACCEPT: 29; KEEP_AS_NON_CORE: 38

## PN Consistency Summary

- **Consistency:** Review YAML, notes and PN annotation agree on MAP1S as a microtubule-associated protein that bridges the autophagy machinery (LC3/Atg8 + LRPPRC→Parkin) to microtubules and mitochondria. Both PN and review trace this to PMID:21262964. The one mismatch: the review captures this only as the generic GO:0006914 autophagy (TAS), whereas PN projects the two specific children mitophagy and aggrephagy. No contradiction, just a granularity gap. PN's "selective autophagy receptor" framing is slightly stronger than the review's "bridge/adaptor" wording, but compatible.
- **PN story / NEW pressure:** PN asserts mitophagy (GO:0000423) and aggrephagy (GO:0035973) — both verified real terms (OLS) and both more specific than the existing GO:0006914. Mitophagy is well supported (PMID:21262964: LRPPRC link to Parkin, Map1s-KO accumulates defective mitochondria). Aggrephagy is supported by the PN-cited Cancer Research paper (MAP1S enhances autophagy to remove aggresomes/aggregates). Existing GOA has ONLY GO:0006914, so both specifics are genuine ADD opportunities, not over-reaches.
- **Evidence alignment:** Good overlap. The PN-cited "MAP1S enhances autophagy to suppress tumorigenesis" (tandfonline) and the Cancer Research hepatocarcinogenesis paper are the autophagy/aggrephagy basis; the review's autophagy annotation rests on PMID:21262964 (the LC3/LRPPRC bridging paper), which is the mechanistic core for mitophagy. The two PN tumor-suppression papers are NOT in the review references — divergence on the aggrephagy/tumor-suppression evidence specifically.
- **Verdict:** Consistent and biologically sound; PN refines (not over-reaches) the review by proposing two verified specific autophagy children. Both are defensible ADDs over the existing generic GO:0006914.

## Full Consistency Review

- **UniProt:** Q66K74 · **batch:** proteostasis-batch-2026-06-14 · **review status:** COMPLETE
- **PN placement:** two ALP rows under `Autophagy substrate selection|Selective autophagy receptor` → `Mitophagy` and `Aggrephagy` ; **PN-node mapping:** type `Mitophagy` `mapped`/ok_for_propagation = GO:0000423 mitophagy (more_specific_than_existing_goa); type `Aggrephagy` `mapped`/ok_for_propagation = GO:0035973 aggrephagy (more_specific_than_existing_goa). Group/class/branch all no_mapping.
- **Consistency:** Review YAML, notes and PN annotation agree on MAP1S as a microtubule-associated protein that bridges the autophagy machinery (LC3/Atg8 + LRPPRC→Parkin) to microtubules and mitochondria. Both PN and review trace this to PMID:21262964. The one mismatch: the review captures this only as the generic GO:0006914 autophagy (TAS), whereas PN projects the two specific children mitophagy and aggrephagy. No contradiction, just a granularity gap. PN's "selective autophagy receptor" framing is slightly stronger than the review's "bridge/adaptor" wording, but compatible.
- **PN story / NEW pressure:** PN asserts mitophagy (GO:0000423) and aggrephagy (GO:0035973) — both verified real terms (OLS) and both more specific than the existing GO:0006914. Mitophagy is well supported (PMID:21262964: LRPPRC link to Parkin, Map1s-KO accumulates defective mitochondria). Aggrephagy is supported by the PN-cited Cancer Research paper (MAP1S enhances autophagy to remove aggresomes/aggregates). Existing GOA has ONLY GO:0006914, so both specifics are genuine ADD opportunities, not over-reaches.
- **Mapping strategy:** This gene does not change either node's status. Both type nodes are correctly `mapped`/ok_for_propagation. Unlike the rejected TOMM20/HSPA8/RAB7A broader-term precedents, here the PN-projected terms are NARROWER than the review's generic autophagy term, so propagation refines rather than over-reaches — consistent with the MAP1S KEY PATTERN (selective-autophagy regulator linking machinery to microtubules/aggregates). Scope is appropriate.
- **Evidence alignment:** Good overlap. The PN-cited "MAP1S enhances autophagy to suppress tumorigenesis" (tandfonline) and the Cancer Research hepatocarcinogenesis paper are the autophagy/aggrephagy basis; the review's autophagy annotation rests on PMID:21262964 (the LC3/LRPPRC bridging paper), which is the mechanistic core for mitophagy. The two PN tumor-suppression papers are NOT in the review references — divergence on the aggrephagy/tumor-suppression evidence specifically.
- **Verdict:** Consistent and biologically sound; PN refines (not over-reaches) the review by proposing two verified specific autophagy children. Both are defensible ADDs over the existing generic GO:0006914.
  **Recommended edits:** [YAML] Add `GO:0000423` mitophagy (involved_in) supported_by PMID:21262964 (LRPPRC/Parkin link; defective-mitochondria accumulation) and `GO:0035973` aggrephagy (involved_in) supported_by the PN-cited tandfonline/Cancer Research MAP1S-autophagy papers — fetch and add those PMIDs to `references` first (verify the tandfonline "MAP1S enhances autophagy to suppress tumorigenesis" PMID and the AACR Cancer Research PMID before citing). [MAP] No mapping-status change needed; both type→GO propagations are correct.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-14
- review_yaml: genes/human/MAP1S/MAP1S-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Autophagy substrate selection | Selective autophagy receptor | Mitophagy
- UniProt: Q66K74
- In branches: ALP
- Notes: Bridges the autophagy machinery to dysfunctional mitochondria for mitophagy with microtubules and enhances autophagy to remove aggresomes and dysfunctional organelles
- PN references (titles):
    - Full article: MAP1S enhances autophagy to suppress tumorigenesis (tandfonline.com)
    - Autophagy Enhanced by Microtubule- and Mitochondrion-Associated MAP1S Suppresses Genome Instability and Hepatocarcinogenesis | Cancer Research | American Association for Cancer Research (aacrjournals.org)
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Mitophagy
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0000423 mitophagy]
        rationale: This PN path denotes selective-autophagy receptors for mitochondrial cargo. The source category is a mechanistic sub-role within mitophagy, so propagation rather than exact equivalence is the correct scope.
    - [group] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagy substrate selection
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad substrate-selection container. GO has useful targets for specific receptor, cargo-adaptor, and selective-autophagy leaves, but this class mixes marking, recognition, receptor regulation, and unknown roles and should not propagate as one term.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 2: Autophagy-Lysosome Pathway | Autophagy substrate selection | Selective autophagy receptor | Aggrephagy
- UniProt: Q66K74
- In branches: ALP
- Notes: Bridges the autophagy machinery to dysfunctional mitochondria for mitophagy with microtubules and enhances autophagy to remove aggresomes and dysfunctional organelles
- PN references (titles):
    - Full article: MAP1S enhances autophagy to suppress tumorigenesis (tandfonline.com)
    - Autophagy Enhanced by Microtubule- and Mitochondrion-Associated MAP1S Suppresses Genome Instability and Hepatocarcinogenesis | Cancer Research | American Association for Cancer Research (aacrjournals.org)
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Aggrephagy
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0035973 aggrephagy]
        rationale: This PN path denotes receptors that recognize aggregation cargo for the aggrephagy pathway. The category is not identical to the GO process term, but propagation to aggrephagy is appropriate because membership in this receptor class implies direct participation in that process.
    - [group] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagy substrate selection
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad substrate-selection container. GO has useful targets for specific receptor, cargo-adaptor, and selective-autophagy leaves, but this class mixes marking, recognition, receptor regulation, and unknown roles and should not propagate as one term.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Projected GO annotations (2)
- GO:0000423 mitophagy | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Mitophagy
- GO:0035973 aggrephagy | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Aggrephagy

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
