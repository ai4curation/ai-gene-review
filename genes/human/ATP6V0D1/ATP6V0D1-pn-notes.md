# ATP6V0D1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: P61421
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-03 (PR 1389)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ATP6V0D1/ATP6V0D1-ai-review.yaml](ATP6V0D1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ATP6V0D1/ATP6V0D1-ai-review.html](ATP6V0D1-ai-review.html)
- Gene notes: present - [genes/human/ATP6V0D1/ATP6V0D1-notes.md](ATP6V0D1-notes.md)
- GOA TSV: present - [genes/human/ATP6V0D1/ATP6V0D1-goa.tsv](ATP6V0D1-goa.tsv)
- UniProt record: present - [genes/human/ATP6V0D1/ATP6V0D1-uniprot.txt](ATP6V0D1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ATP6V0D1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ATP6V0D1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATP6V0D1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATP6V0D1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/ATP6V0D1/ATP6V0D1-deep-research-manual.md](ATP6V0D1-deep-research-manual.md)

## AIGR Review Snapshot

- Description: ATP6V0D1 encodes the ubiquitous d1 isoform of the V0 d subunit of the vacuolar H+-ATPase (V-ATPase). The protein is a peripheral component of the membrane-embedded V0 sector and helps couple the V1 ATP-hydrolysis motor to V0 proton translocation. ATP6V0D1-containing V-ATPase complexes acidify lysosomes, endosomes, phagosomes, synaptic vesicles, and other intracellular compartments, thereby supporting vesicle traffic, lysosomal degradation, nutrient-dependent mTORC1 signaling, and ion homeostasis.
- Existing/core annotation action counts: ACCEPT: 31; KEEP_AS_NON_CORE: 18; MARK_AS_OVER_ANNOTATED: 10; MODIFY: 1

## PN Consistency Summary

- **Consistency:** Consistent. Notes, deep-research-manual, review, PN row and PN-node mapping all treat ATP6V0D1 as the d1 V0-sector subunit acidifying endolysosomal compartments. The review carries the mTORC1/Ragulator role as directly-evidenced (PMID:22053050, IDA) but KEEP_AS_NON_CORE, matching the PN ancestor `no_mapping`. No contradictions.
- **PN story / NEW pressure:** Unlike ATP6V0A2, ATP6V0D1 GOA already captures the lysosomal-specific terms: GO:0046611 lysosomal V-ATPase complex (IDA, PMID:22053050, ACCEPT) and GO:0007035 vacuolar acidification (IBA, ACCEPT) plus GO:1902600 proton transport. The two PN projected GO terms GO:0007042/GO:0046610 (both verified real via OLS) are therefore "more_specific" but the gene already has equivalent-or-adjacent coverage — review adds NO NEW terms (proposed_new_terms: []). No NEW pressure; the story is already captured. PN nutrient-sensing context is correctly represented only as non-core mTORC1 signaling, not promoted.
- **Evidence alignment:** Strong primary-evidence base, diverging from PN's review-title citations. Load-bearing PMIDs: 18752060 (d subunit central rotary role), 33065002 (human V-ATPase cryo-EM), 22053050 (mTORC1 amino-acid sensing, V0-d1/p18 interaction), 28296633 (iron/HIF), 11118322 (gene structure, full_text_unavailable flagged). PN's V-ATPase-structure and mTORC1 themes overlap conceptually but cite secondary reviews.
- **Verdict:** Consistent; PN projected terms already captured in GOA (GO:0046611/GO:0007035), so review correctly adds nothing; mTORC1 context kept non-core. No edits required.

## Full Consistency Review

- **UniProt:** P61421 · **batch:** proteostasis-batch-2026-06-03 · **review status:** COMPLETE
- **PN placement:** two ALP rows — `ALP|Pre-initiation autophagy signaling|mTORC1 pathway, upstream|Nutrient sensing|V0 lysosomal v-ATPase proton pump component` and `ALP|Lysosomal catabolism|Regulation of lysosomal environment|Lysosomal acidification|V0 lysosomal v-ATPase proton pump component` ; **PN-node mapping:** identical to ATP6V0A2 — V0 subtype leaves `mapped/ok_for_propagation` → GO:0046610, GO:0033179; Lysosomal-acidification type → GO:0007042; mTORC1/nutrient-sensing ancestors `no_mapping`; Pre-initiation class `context_only/too_broad` (GO:0010506).
- **Consistency:** Consistent. Notes, deep-research-manual, review, PN row and PN-node mapping all treat ATP6V0D1 as the d1 V0-sector subunit acidifying endolysosomal compartments. The review carries the mTORC1/Ragulator role as directly-evidenced (PMID:22053050, IDA) but KEEP_AS_NON_CORE, matching the PN ancestor `no_mapping`. No contradictions.
- **PN story / NEW pressure:** Unlike ATP6V0A2, ATP6V0D1 GOA already captures the lysosomal-specific terms: GO:0046611 lysosomal V-ATPase complex (IDA, PMID:22053050, ACCEPT) and GO:0007035 vacuolar acidification (IBA, ACCEPT) plus GO:1902600 proton transport. The two PN projected GO terms GO:0007042/GO:0046610 (both verified real via OLS) are therefore "more_specific" but the gene already has equivalent-or-adjacent coverage — review adds NO NEW terms (proposed_new_terms: []). No NEW pressure; the story is already captured. PN nutrient-sensing context is correctly represented only as non-core mTORC1 signaling, not promoted.
- **Mapping strategy:** No change. The node mapping is shared with ATP6V0A2 and stands; ATP6V0D1 does not push the node broader. Conservative `no_mapping` ancestors correct.
- **Evidence alignment:** Strong primary-evidence base, diverging from PN's review-title citations. Load-bearing PMIDs: 18752060 (d subunit central rotary role), 33065002 (human V-ATPase cryo-EM), 22053050 (mTORC1 amino-acid sensing, V0-d1/p18 interaction), 28296633 (iron/HIF), 11118322 (gene structure, full_text_unavailable flagged). PN's V-ATPase-structure and mTORC1 themes overlap conceptually but cite secondary reviews.
- **Verdict:** Consistent; PN projected terms already captured in GOA (GO:0046611/GO:0007035), so review correctly adds nothing; mTORC1 context kept non-core. No edits required.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/ATP6V0D1/ATP6V0D1-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Pre-initiation autophagy signaling | mTORC1 pathway, upstream | Nutrient sensing | V0 lysosomal v-ATPase proton pump component
- UniProt: P61421
- In branches: ALP
- Notes: Subunit of the V0 (lysosomal membrane bound) component of the lysosomal v-ATPase. The V0 and V1 components of the v-ATPase assemble during amino acid starvation creating the active v-ATPase that pumps protons into the lysosome for acidification. The v-ATPase also engages in amino acid-dependent interactions with the Ragulator complex. In the presence of amino acids, the v-ATPase-Ragulator complex undergoes a conformational change that results in Ragulator exerting its GEF activity on RAGA/B.
- PN references (titles):
    - Regulation of mTORC1 by amino acids - ScienceDirect
    - Cells | Free Full-Text | SEA and GATOR 10 Years Later | HTML (mdpi.com)
    - Eukaryotic V-ATPase: Novel structural findings and functional insights - ScienceDirect
    - The emerging roles of vacuolar-type ATPase-dependent Lysosomal acidification in neurodegenerative diseases | Translational Neurodegeneration | Full Text (biomedcentral.com)
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Pre-initiation autophagy signaling|mTORC1 pathway, upstream|Nutrient sensing|V0 lysosomal v-ATPase proton pump component
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0046610 lysosomal proton-transporting V-type ATPase, V0 domain]
        rationale: This PN leaf is restricted to V0-sector lysosomal V-ATPase components. The GO lysosomal V0-domain component term is the direct target.
    - [type] Autophagy-Lysosome Pathway|Pre-initiation autophagy signaling|mTORC1 pathway, upstream|Nutrient sensing
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a contextual PN role. The label is useful for curator triage, but by itself does not support a universal GO assertion for all member genes beyond curated ancestor or child mappings.
    - [group] Autophagy-Lysosome Pathway|Pre-initiation autophagy signaling|mTORC1 pathway, upstream
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Pre-initiation autophagy signaling
        status=context_only scope=too_broad_to_propagate GO=[GO:0010506 regulation of autophagy]
        rationale: This class organizes upstream signaling inputs to autophagy initiation. Because the subtree contains generic insulin, AMPK, mTORC1, nutrient-sensing, and miscellaneous signaling components, class-level propagation to regulation of autophagy would over-annotate many genes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 2: Autophagy-Lysosome Pathway | Lysosomal catabolism | Regulation of lysosomal environment | Lysosomal acidification | V0 lysosomal v-ATPase proton pump component
- UniProt: P61421
- In branches: ALP
- Notes: Subunit of the V0 (lysosomal membrane bound) component of the lysosomal v-ATPase. The V0 and V1 components of the v-ATPase assemble during amino acid starvation creating the active v-ATPase that pumps protons into the lysosome for acidification. The v-ATPase also engages in amino acid-dependent interactions with the Ragulator complex. In the presence of amino acids, the v-ATPase-Ragulator complex undergoes a conformational change that results in Ragulator exerting its GEF activity on RAGA/B.
- PN references (titles):
    - Regulation of mTORC1 by amino acids - ScienceDirect
    - Cells | Free Full-Text | SEA and GATOR 10 Years Later | HTML (mdpi.com)
    - Eukaryotic V-ATPase: Novel structural findings and functional insights - ScienceDirect
    - The emerging roles of vacuolar-type ATPase-dependent Lysosomal acidification in neurodegenerative diseases | Translational Neurodegeneration | Full Text (biomedcentral.com)
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Lysosomal catabolism|Regulation of lysosomal environment|Lysosomal acidification|V0 lysosomal v-ATPase proton pump component
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0033179 proton-transporting V-type ATPase, V0 domain]
        rationale: This PN subtype denotes the V0-sector component of the lysosomal V-type ATPase. The GO V0-domain component term is the appropriate propagation target.
    - [type] Autophagy-Lysosome Pathway|Lysosomal catabolism|Regulation of lysosomal environment|Lysosomal acidification
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0007042 lysosomal lumen acidification]
        rationale: This PN group directly names the lysosomal acidification mechanism. Propagation to the GO lysosomal lumen acidification term is an exact mechanistic match.
    - [group] Autophagy-Lysosome Pathway|Lysosomal catabolism|Regulation of lysosomal environment
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Lysosomal catabolism
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad lysosomal-degradation container. The subtree includes carbohydrate, lipid, protein, nuclease, phosphatase, sulfatase, and environment-regulation roles, so mapping should occur at the enzyme or process subtype level.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Projected GO annotations (3)
- GO:0046610 lysosomal proton-transporting V-type ATPase, V0 domain | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Autophagy-Lysosome Pathway|Pre-initiation autophagy signaling|mTORC1 pathway, upstream|Nutrient sensing|V0 lysosomal v-ATPase proton pump component
- GO:0007042 lysosomal lumen acidification | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Autophagy-Lysosome Pathway|Lysosomal catabolism|Regulation of lysosomal environment|Lysosomal acidification
- GO:0033179 proton-transporting V-type ATPase, V0 domain | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Lysosomal catabolism|Regulation of lysosomal environment|Lysosomal acidification|V0 lysosomal v-ATPase proton pump component

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
