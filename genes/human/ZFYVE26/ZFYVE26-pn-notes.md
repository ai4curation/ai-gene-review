# ZFYVE26 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q68DK2
- AIGR review status: COMPLETE
- Review batch: proteostasis-pr-1217 (PR 1217)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ZFYVE26/ZFYVE26-ai-review.yaml](ZFYVE26-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ZFYVE26/ZFYVE26-ai-review.html](ZFYVE26-ai-review.html)
- Gene notes: present - [genes/human/ZFYVE26/ZFYVE26-notes.md](ZFYVE26-notes.md)
- GOA TSV: present - [genes/human/ZFYVE26/ZFYVE26-goa.tsv](ZFYVE26-goa.tsv)
- UniProt record: present - [genes/human/ZFYVE26/ZFYVE26-uniprot.txt](ZFYVE26-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ZFYVE26.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ZFYVE26.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ZFYVE26.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ZFYVE26.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: ZFYVE26 encodes spastizin/SPG15, a FYVE-domain PI3P-binding protein that functions with SPG11/spatacsin and AP-5 in endolysosomal membrane remodeling. The strongest protein-homeostasis evidence supports a core role in autophagic lysosome reformation, lysosomal membrane organization, membrane bending, and autophagosome maturation through PI3P-dependent recruitment to lysosomal/late-endosomal membranes. ZFYVE26 also has experimentally supported cytokinesis and HR-DSBR roles, but its principal cellular role is endolysosomal membrane remodeling.
- Existing/core annotation action counts: ACCEPT: 16; KEEP_AS_NON_CORE: 12; MARK_AS_OVER_ANNOTATED: 1; MODIFY: 8; NEW: 1; UNDECIDED: 1

## PN Consistency Summary

- **Consistency:** Strongly consistent. Deep-research notes, review YAML, PN notes, and PN mappings all converge: core = PI3P-binding FYVE protein in AP5-SPG11-SPG15 endolysosomal membrane remodeling / ALR / autophagosome maturation. The PN note's "Beclin1-UVRAG-Rubicon… required for autophagosome maturation" matches the review's NEW GO:0097352 row. No contradictions.
- **PN story / NEW pressure:** PN asserts (a) class III PI3K complex *modulation* — review correctly does NOT claim complex membership, using GO:0032266 PI3P binding + lysosome organization instead (matches PN's context_only decision); and (b) ALR with "specific function unknown." Review supplies the mechanism: GO:0007040, GO:0097212 lysosomal membrane organization, GO:0097753 membrane bending, plus NEW GO:0097352 autophagosome maturation (**OLS-verified real**). ALR itself has **no GO term** (OLS search empty) — review's `proposed_new_terms` "autophagic lysosome reformation" under GO:0007040 is well-justified. **Conclusion: NEW term (ALR) defensible; autophagosome maturation is a defensible ADD already in review; class-III-PI3K membership correctly NOT added.**
- **Evidence alignment:** Both PN refs are in the review. PN "Defective autophagy in spastizin… HSP type 15" = PMID:24030950 (autophagosome maturation); PN "spastizin and spatacsin mediate ALR" = PMID:25365221 (lysosome organization/ALR). Review adds PMID:40175557 (2025 structure), 23825025 (AP-5), 37871017, 20208530 the PN rows omit.
- **Verdict:** Fully consistent; **review enriches the PN "function unknown" ALR node with verified terms** (GO:0097352 add + ALR proposed-new-term). Mappings sound; no demotions needed.

## Full Consistency Review

- **UniProt:** Q68DK2 (spastizin/SPG15/FYVE-CENT) · **batch:** proteostasis-pr-1217 · **review status:** COMPLETE
- **PN placement:** `ALP|Autophagosome closure maturation and lysosome fusion|Class 3 PI3K complex 2, direct|Modulator of class 3 PI3K complex 2 activity` and `ALP|Autophagic lysosome reformation|Specific function… unknown` ; **PN-node mapping:** PI3K-complex nodes all context_only/too_broad → GO:0035032 (class III PI3K complex), explicitly "should not project CC membership"; ALR group = no_mapping (unknown); ALR class = context_only → GO:0007040 lysosome organization.
- **Consistency:** Strongly consistent. Deep-research notes, review YAML, PN notes, and PN mappings all converge: core = PI3P-binding FYVE protein in AP5-SPG11-SPG15 endolysosomal membrane remodeling / ALR / autophagosome maturation. The PN note's "Beclin1-UVRAG-Rubicon… required for autophagosome maturation" matches the review's NEW GO:0097352 row. No contradictions.
- **PN story / NEW pressure:** PN asserts (a) class III PI3K complex *modulation* — review correctly does NOT claim complex membership, using GO:0032266 PI3P binding + lysosome organization instead (matches PN's context_only decision); and (b) ALR with "specific function unknown." Review supplies the mechanism: GO:0007040, GO:0097212 lysosomal membrane organization, GO:0097753 membrane bending, plus NEW GO:0097352 autophagosome maturation (**OLS-verified real**). ALR itself has **no GO term** (OLS search empty) — review's `proposed_new_terms` "autophagic lysosome reformation" under GO:0007040 is well-justified. **Conclusion: NEW term (ALR) defensible; autophagosome maturation is a defensible ADD already in review; class-III-PI3K membership correctly NOT added.**
- **Mapping strategy:** No change needed to PI3K nodes (context_only is right; precedent-aligned — narrower review terms, no spurious CC propagation). ALR group could be upgraded from no_mapping toward GO:0007040 lysosome organization (the review's accepted core, and the class-node target), but PN's "unknown specific function" caution is reasonable; review is narrower than the PN class-level GO:0007040, never broader.
- **Evidence alignment:** Both PN refs are in the review. PN "Defective autophagy in spastizin… HSP type 15" = PMID:24030950 (autophagosome maturation); PN "spastizin and spatacsin mediate ALR" = PMID:25365221 (lysosome organization/ALR). Review adds PMID:40175557 (2025 structure), 23825025 (AP-5), 37871017, 20208530 the PN rows omit.
- **Verdict:** Fully consistent; **review enriches the PN "function unknown" ALR node with verified terms** (GO:0097352 add + ALR proposed-new-term). Mappings sound; no demotions needed.

## PN Dossier Context

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/ZFYVE26/ZFYVE26-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Autophagosome closure maturation and lysosome fusion | Class 3 PI3K complex 2, direct | Modulator of class 3 PI3K complex 2 activity
- UniProt: Q68DK2
- In branches: ALP
- Notes: aka FYVE-CENT, SPG15, and spastizin. Spastizin interacts with the autophagy related Beclin 1-UVRAG-Rubicon multiprotein complex and is required for autophagosome maturation. In cells lacking spastizin or with mutated forms of the protein, spastizin interaction with Beclin 1 is lost although the formation of the Beclin 1-UVRAG-Rubicon complex can still be observed. However, in these cells there is an impairment of autophagosome maturation and an accumulation of immature autophagosomes. Also important in autophagic lysosomal reformation.
- PN references (titles):
    - Defective autophagy in spastizin mutated patients with hereditary spastic paraparesis type 15 | Brain | Oxford Academic (oup.com)
    - JCI - Spastic paraplegia proteins spastizin and spatacsin mediate autophagic lysosome reformation
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Class 3 PI3K complex 2, direct|Modulator of class 3 PI3K complex 2 activity
        status=context_only scope=too_broad_to_propagate GO=[GO:0035032 phosphatidylinositol 3-kinase complex, class III]
        rationale: Reviewed as a class-III PI3K complex context or regulator bucket. This node is useful for curator interpretation, but it should not project cellular-component membership; only explicit complex-component leaves propagate to GO complex terms.
    - [group] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Class 3 PI3K complex 2, direct
        status=context_only scope=too_broad_to_propagate GO=[GO:0035032 phosphatidylinositol 3-kinase complex, class III]
        rationale: Reviewed as a class-III PI3K complex context or regulator bucket. This node is useful for curator interpretation, but it should not project cellular-component membership; only explicit complex-component leaves propagate to GO complex terms.
    - [class] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion
        status=context_only scope=too_broad_to_propagate GO=[GO:0016236 macroautophagy]
        rationale: This class is a late macroautophagy context, but the subtree mixes docking, fusion, localization, membrane-composition, and unknown late-stage roles. The class-level relation is useful for display while propagation is restricted to narrower mechanism nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 2: Autophagy-Lysosome Pathway | Autophagic lysosome reformation | Specific function in autophagic lysosome reformation unknown
- UniProt: Q68DK2
- In branches: ALP
- Notes: aka FYVE-CENT, SPG15, and spastizin. Spastizin interacts with the autophagy related Beclin 1-UVRAG-Rubicon multiprotein complex and is required for autophagosome maturation. In cells lacking spastizin or with mutated forms of the protein, spastizin interaction with Beclin 1 is lost although the formation of the Beclin 1-UVRAG-Rubicon complex can still be observed. However, in these cells there is an impairment of autophagosome maturation and an accumulation of immature autophagosomes. Also important in autophagic lysosomal reformation.
- PN references (titles):
    - Defective autophagy in spastizin mutated patients with hereditary spastic paraparesis type 15 | Brain | Oxford Academic (oup.com)
    - JCI - Spastic paraplegia proteins spastizin and spatacsin mediate autophagic lysosome reformation
- PN-node mapping records (path + ancestors):
    - [group] Autophagy-Lysosome Pathway|Autophagic lysosome reformation|Specific function in autophagic lysosome reformation unknown
        status=no_mapping scope= GO=[]
        rationale: This PN group explicitly states that the specific role within autophagic lysosome reformation is unknown. That makes GO propagation unsafe until a narrower mechanistic interpretation is available.
    - [class] Autophagy-Lysosome Pathway|Autophagic lysosome reformation
        status=context_only scope=too_broad_to_propagate GO=[GO:0007040 lysosome organization]
        rationale: Autophagic lysosome reformation is the lysosome-regeneration phase that follows autolysosome formation and cargo degradation. As a class, it is better aligned to lysosome organization than to generic autophagy, but the PN members are mechanistically mixed across membrane remodeling, tubulation, product efflux, and unknown late-stage roles, so class-level propagation would still over-annotate.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
