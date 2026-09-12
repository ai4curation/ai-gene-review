# ATP6V1A PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: P38606
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-06
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ATP6V1A/ATP6V1A-ai-review.yaml](ATP6V1A-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ATP6V1A/ATP6V1A-ai-review.html](ATP6V1A-ai-review.html)
- Gene notes: present - [genes/human/ATP6V1A/ATP6V1A-notes.md](ATP6V1A-notes.md)
- GOA TSV: present - [genes/human/ATP6V1A/ATP6V1A-goa.tsv](ATP6V1A-goa.tsv)
- UniProt record: present - [genes/human/ATP6V1A/ATP6V1A-uniprot.txt](ATP6V1A-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ATP6V1A.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ATP6V1A.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATP6V1A.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATP6V1A.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: ATP6V1A encodes the catalytic A subunit of the V1 peripheral domain of the vacuolar-type H+-ATPase (V-ATPase), the principal ATP-driven proton pump of eukaryotic cells. The V1 domain hydrolyzes ATP; subunit A forms three catalytic AB heterodimers that together with subunit B create the hexameric ring responsible for ATP hydrolysis, whose energy is transduced via a central rotor to drive proton translocation through the membrane-embedded V0 domain. V-ATPase is the primary source of organellar acidification in all eukaryotes, acidifying lysosomes, endosomes, the Golgi apparatus, and secretory vesicles; in specialized cells it is also found at the plasma membrane. ATP6V1A is expressed ubiquitously, with high expression in the skin and neurons. In neurons, V-ATPase plays additional roles in neurotransmitter loading into synaptic vesicles and in regulating synaptic transmission. Through its role in lysosomal acidification, V-ATPase (with subunit A as catalytic core) is required for activation of mTORC1 by amino acids at the lysosomal surface, for intracellular iron homeostasis via endosomal transferrin processing, and for autophagic flux. De novo heterozygous ATP6V1A mutations cause a developmental encephalopathy with epilepsy (IECEE3), while biallelic loss-of-function variants cause autosomal recessive cutis laxa type 2D (ARCL2D).
- Existing/core annotation action counts: ACCEPT: 31; KEEP_AS_NON_CORE: 34; MARK_AS_OVER_ANNOTATED: 10

## PN Consistency Summary

- **Consistency:** Strong. Deep research (notes) ↔ review ↔ PN all converge on: catalytic A subunit of V1, lysosomal/organellar acidification, and the mTORC1 amino-acid-sensing role (PMID:22053050) — the latter is exactly the PN "Nutrient sensing/mTORC1 upstream" story and is ACCEPTed in the review (GO:0071230, GO:0160124, GO:1904263). No contradictions: every PN-projected term is accepted in the review.
- **PN story / NEW pressure:** No new pressure. PN's mTORC1/nutrient-sensing assertion is already captured (3 ACCEPTed mTORC1 annotations). GO:0007042 already in GOA (dossier: already_in_goa_exact; confirmed 2 hits in GOA) and ACCEPTed. GO:0046612 (verified real via OLS, V1-domain lysosomal CC) is absent from GOA — a defensible more-specific ADD.
- **Evidence alignment:** Divergent source sets, same conclusion. PN cites review-article titles (mTORC1 review, SEA/GATOR, Rubinstein V-ATPase review, neurodegeneration review). Review is anchored on primary/structural PMIDs: 33065002 (cryo-EM), 22053050 (Zoncu mTORC1), 32001091 (= Rubinstein review, overlap), 29668857, 28296633. PN's mTORC1-review evidence is the weaker-form counterpart of the review's Zoncu primary paper.
- **Verdict:** Consistent / ADD GO:0046612 (verified) as more-specific CC; no contradictions. **Recommended edits:** [MAP] align subtype complex target GO:0033176 → GO:0046611 (lysosomal V-ATPase complex, already ACCEPTed in review) for specificity.

## Full Consistency Review

- **UniProt:** P38606 · **batch:** proteostasis-batch-2026-06-06 · **review status:** COMPLETE (large, mature review; ~60 annotations curated)
- **PN placement:** `Autophagy-Lysosome Pathway|...|V1 lysosomal v-ATPase proton pump component` (two rows: mTORC1-upstream/Nutrient sensing, and Lysosomal acidification) ; **PN-node mapping:** subtype=mapped/ok GO:0046612 (V1 domain, lysosomal) + GO:0033176 (V-ATPase complex); type=mapped/ok GO:0007042 (lysosomal lumen acidification); ancestors no_mapping/context_only.
- **Consistency:** Strong. Deep research (notes) ↔ review ↔ PN all converge on: catalytic A subunit of V1, lysosomal/organellar acidification, and the mTORC1 amino-acid-sensing role (PMID:22053050) — the latter is exactly the PN "Nutrient sensing/mTORC1 upstream" story and is ACCEPTed in the review (GO:0071230, GO:0160124, GO:1904263). No contradictions: every PN-projected term is accepted in the review.
- **PN story / NEW pressure:** No new pressure. PN's mTORC1/nutrient-sensing assertion is already captured (3 ACCEPTed mTORC1 annotations). GO:0007042 already in GOA (dossier: already_in_goa_exact; confirmed 2 hits in GOA) and ACCEPTed. GO:0046612 (verified real via OLS, V1-domain lysosomal CC) is absent from GOA — a defensible more-specific ADD.
- **Mapping strategy:** A-subunit does not force a change to node mapping, but it sharpens it: review uses the **more specific** GO:0046611 "lysosomal V-type ATPase complex" (ACCEPT, IDA PMID:33065002/22053050), whereas the subtype-complex mapping targets the broader GO:0033176. The V1-domain target GO:0046612 is correctly the most specific.
- **Evidence alignment:** Divergent source sets, same conclusion. PN cites review-article titles (mTORC1 review, SEA/GATOR, Rubinstein V-ATPase review, neurodegeneration review). Review is anchored on primary/structural PMIDs: 33065002 (cryo-EM), 22053050 (Zoncu mTORC1), 32001091 (= Rubinstein review, overlap), 29668857, 28296633. PN's mTORC1-review evidence is the weaker-form counterpart of the review's Zoncu primary paper.
- **Verdict:** Consistent / ADD GO:0046612 (verified) as more-specific CC; no contradictions. **Recommended edits:** [MAP] align subtype complex target GO:0033176 → GO:0046611 (lysosomal V-ATPase complex, already ACCEPTed in review) for specificity.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-06
- review_yaml: genes/human/ATP6V1A/ATP6V1A-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Pre-initiation autophagy signaling | mTORC1 pathway, upstream | Nutrient sensing | V1 lysosomal v-ATPase proton pump component
- UniProt: P38606
- In branches: ALP
- Notes: Subunit of the V1 (cytosolic) component of the lysosomal v-ATPase. The V0 and V1 components of the v-ATPase assemble during amino acid starvation creating the active v-ATPase that pumps protons into the lysosome for acidification. The v-ATPase also engages in amino acid-dependent interactions with the Ragulator complex. In the presence of amino acids, the v-ATPase-Ragulator complex undergoes a conformational change that results in Ragulator exerting its GEF activity on RAGA/B.
- PN references (titles):
    - Regulation of mTORC1 by amino acids - ScienceDirect
    - Cells | Free Full-Text | SEA and GATOR 10 Years Later | HTML (mdpi.com)
    - Eukaryotic V-ATPase: Novel structural findings and functional insights - ScienceDirect
    - The emerging roles of vacuolar-type ATPase-dependent Lysosomal acidification in neurodegenerative diseases | Translational Neurodegeneration | Full Text (biomedcentral.com)
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Pre-initiation autophagy signaling|mTORC1 pathway, upstream|Nutrient sensing|V1 lysosomal v-ATPase proton pump component
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0046612 lysosomal proton-transporting V-type ATPase, V1 domain]
        rationale: This PN leaf is restricted to V1-sector lysosomal V-ATPase components. The GO lysosomal V1-domain component term is the direct target.
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

## PN row 2: Autophagy-Lysosome Pathway | Lysosomal catabolism | Regulation of lysosomal environment | Lysosomal acidification | V1 lysosomal v-ATPase proton pump component
- UniProt: P38606
- In branches: ALP
- Notes: Subunit of the V1 (cytosolic) component of the lysosomal v-ATPase. The V0 and V1 components of the v-ATPase assemble during amino acid starvation creating the active v-ATPase that pumps protons into the lysosome for acidification. The v-ATPase also engages in amino acid-dependent interactions with the Ragulator complex. In the presence of amino acids, the v-ATPase-Ragulator complex undergoes a conformational change that results in Ragulator exerting its GEF activity on RAGA/B.
- PN references (titles):
    - Regulation of mTORC1 by amino acids - ScienceDirect
    - Cells | Free Full-Text | SEA and GATOR 10 Years Later | HTML (mdpi.com)
    - Eukaryotic V-ATPase: Novel structural findings and functional insights - ScienceDirect
    - The emerging roles of vacuolar-type ATPase-dependent Lysosomal acidification in neurodegenerative diseases | Translational Neurodegeneration | Full Text (biomedcentral.com)
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Lysosomal catabolism|Regulation of lysosomal environment|Lysosomal acidification|V1 lysosomal v-ATPase proton pump component
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0033176 proton-transporting V-type ATPase complex]
        rationale: This PN subtype denotes the V1-sector component of the lysosomal V-ATPase. In the current GO cache, the broader V-type ATPase complex is the safest validated target for this component role.
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
- GO:0046612 lysosomal proton-transporting V-type ATPase, V1 domain | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Autophagy-Lysosome Pathway|Pre-initiation autophagy signaling|mTORC1 pathway, upstream|Nutrient sensing|V1 lysosomal v-ATPase proton pump component
- GO:0007042 lysosomal lumen acidification | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Lysosomal catabolism|Regulation of lysosomal environment|Lysosomal acidification
- GO:0033176 proton-transporting V-type ATPase complex | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Lysosomal catabolism|Regulation of lysosomal environment|Lysosomal acidification|V1 lysosomal v-ATPase proton pump component

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
