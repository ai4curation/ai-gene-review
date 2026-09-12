# ATP6V0E1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: O15342
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-06
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ATP6V0E1/ATP6V0E1-ai-review.yaml](ATP6V0E1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ATP6V0E1/ATP6V0E1-ai-review.html](ATP6V0E1-ai-review.html)
- Gene notes: present - [genes/human/ATP6V0E1/ATP6V0E1-notes.md](ATP6V0E1-notes.md)
- GOA TSV: present - [genes/human/ATP6V0E1/ATP6V0E1-goa.tsv](ATP6V0E1-goa.tsv)
- UniProt record: present - [genes/human/ATP6V0E1/ATP6V0E1-uniprot.txt](ATP6V0E1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ATP6V0E1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ATP6V0E1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATP6V0E1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATP6V0E1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: ATP6V0E1 encodes V-type proton ATPase subunit e 1 (81 amino acids, 9.2 kDa), a small dual-transmembrane protein that is a structural component of the V0 membrane-embedded domain of the vacuolar-type H+-ATPase (V-ATPase). The V0 complex contains the proton transport subunit a, a proteolipid c-ring, rotary subunit d, subunits e and f, and accessory subunits ATP6AP1 and ATP6AP2. Subunit e 1 has an N-terminal lumenal segment, two transmembrane helices, a short cytoplasmic loop, and a C-terminal lumenal tail bearing an N-linked glycan at Asn70 that contributes to V-ATPase assembly and stability. Humans have two paralogous e subunits: ATP6V0E1 (e1, ubiquitous) and ATP6V0E2 (e2, restricted to kidney and brain). Both isoforms can complement a yeast e subunit deletion, confirming that the e subunit is essential for proton pump function. ATP6V0E1 localizes to lysosomal and endosomal membranes as part of the assembled V-ATPase holoenzyme. As a V0 structural subunit, it contributes to the proton translocation function of the V-ATPase complex that acidifies lysosomes, endosomes, and other intracellular compartments.
- Existing/core annotation action counts: ACCEPT: 23; KEEP_AS_NON_CORE: 1; MARK_AS_OVER_ANNOTATED: 2; MODIFY: 1

## PN Consistency Summary

- **Consistency:** Consistent. Review, notes, and PN all describe e1 as a small dual-TM V0 structural subunit essential for proton-pump function (yeast complementation, PMID:17350184; cryo-EM, PMID:33065002). PN correctly assigns the V0 sector (vs V1 for G1/H). No contradictions.
- **PN story / NEW pressure:** All projected terms VERIFIED real (OLS). GO:0033179 (generic V0 domain) already in GOA/review (ACCEPT). GO:0046610 "lysosomal V0 domain" is a lysosome-specific sibling of the review's GO:0000220 *vacuolar* V0 — re-specification, already captured at function level. GO:0007042 lysosomal lumen acidification is NOT in the review (review has GO:0007035 vacuolar acidification, a broader parent) → defensible ADD as the precise lysosomal BP. Conclude: GO:0007042 = ADD candidate; GO:0046610 already captured by V0-domain terms.
- **Evidence alignment:** Same pattern as the other V-ATPase subunits: PN cites review-article titles not in the review's PMIDs; review is anchored on primary papers (PMID:9556572 original M9.2 characterization, PMID:17350184 e1/e2 complementation, PMID:33065002 cryo-EM). Complementary, no conflict.
- **Verdict:** Consistent. ADD GO:0007042 (lysosomal lumen acidification) as the lysosome-specific refinement of the existing vacuolar-acidification annotation; GO:0046610 already covered by existing V0-domain terms.

## Full Consistency Review

- **UniProt:** O15342 · **batch:** proteostasis-batch-2026-06-06 · **review status:** COMPLETE (thorough; yeast-complementation + cryo-EM grounded)
- **PN placement:** `Autophagy-Lysosome Pathway` two rows — `…|mTORC1 pathway, upstream|Nutrient sensing|V0 lysosomal v-ATPase proton pump component` and `…|Lysosomal catabolism|Regulation of lysosomal environment|Lysosomal acidification|V0 …component` ; **PN-node mapping:** subtype→GO:0046610 (lysosomal V0 domain, mapped/ok); subtype→GO:0033179 (V0 domain, mapped/ok); type→GO:0007042 (lysosomal lumen acidification, mapped/ok).
- **Consistency:** Consistent. Review, notes, and PN all describe e1 as a small dual-TM V0 structural subunit essential for proton-pump function (yeast complementation, PMID:17350184; cryo-EM, PMID:33065002). PN correctly assigns the V0 sector (vs V1 for G1/H). No contradictions.
- **PN story / NEW pressure:** All projected terms VERIFIED real (OLS). GO:0033179 (generic V0 domain) already in GOA/review (ACCEPT). GO:0046610 "lysosomal V0 domain" is a lysosome-specific sibling of the review's GO:0000220 *vacuolar* V0 — re-specification, already captured at function level. GO:0007042 lysosomal lumen acidification is NOT in the review (review has GO:0007035 vacuolar acidification, a broader parent) → defensible ADD as the precise lysosomal BP. Conclude: GO:0007042 = ADD candidate; GO:0046610 already captured by V0-domain terms.
- **Mapping strategy:** Appropriate; subtype correctly leaf-restricted to V0. PN-projected terms are at/below the review's specificity for CC (lysosomal vs vacuolar) and the BP projection is narrower than the review's vacuolar-acidification — no broader-than-review over-reach.
- **Evidence alignment:** Same pattern as the other V-ATPase subunits: PN cites review-article titles not in the review's PMIDs; review is anchored on primary papers (PMID:9556572 original M9.2 characterization, PMID:17350184 e1/e2 complementation, PMID:33065002 cryo-EM). Complementary, no conflict.
- **Verdict:** Consistent. ADD GO:0007042 (lysosomal lumen acidification) as the lysosome-specific refinement of the existing vacuolar-acidification annotation; GO:0046610 already covered by existing V0-domain terms.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-06
- review_yaml: genes/human/ATP6V0E1/ATP6V0E1-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Pre-initiation autophagy signaling | mTORC1 pathway, upstream | Nutrient sensing | V0 lysosomal v-ATPase proton pump component
- UniProt: O15342
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
- UniProt: O15342
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
