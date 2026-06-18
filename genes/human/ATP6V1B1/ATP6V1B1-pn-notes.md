# ATP6V1B1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: P15313
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ATP6V1B1/ATP6V1B1-ai-review.yaml](ATP6V1B1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ATP6V1B1/ATP6V1B1-ai-review.html](ATP6V1B1-ai-review.html)
- Gene notes: present - [genes/human/ATP6V1B1/ATP6V1B1-notes.md](ATP6V1B1-notes.md)
- GOA TSV: present - [genes/human/ATP6V1B1/ATP6V1B1-goa.tsv](ATP6V1B1-goa.tsv)
- UniProt record: present - [genes/human/ATP6V1B1/ATP6V1B1-uniprot.txt](ATP6V1B1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ATP6V1B1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ATP6V1B1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATP6V1B1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATP6V1B1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: ATP6V1B1 encodes the B1 isoform of the non-catalytic B subunit of the V1 peripheral domain of the vacuolar H+-ATPase (V-ATPase). Three copies of the B subunit alternate with three catalytic A subunits to form the (AB)3 heterohexameric head of the cytoplasmic V1 complex, which hydrolyzes ATP to drive proton translocation through the membrane-embedded V0 domain. The B subunit binds ATP at non-catalytic nucleotide sites and is essential for proper assembly and activity of the holoenzyme. ATP6V1B1 is the tissue-restricted (kidney, inner ear, epididymis, salivary gland) paralog of the ubiquitously expressed B2 subunit. In the kidney it localizes to the apical plasma membrane of intercalated cells (and other early distal nephron segments), where the plasma-membrane V-ATPase secretes protons into the urine to mediate distal urinary acidification; it is also expressed in the cochlea and endolymphatic sac, where V-ATPase activity maintains endolymph pH. A C-terminal PDZ-binding motif mediates interactions (e.g. with NHERF1 and the bicarbonate transporter SLC4A7) implicated in apical membrane targeting and scaffolding. Loss-of-function mutations cause autosomal recessive distal renal tubular acidosis with progressive sensorineural hearing loss (DRTA2).
- Existing/core annotation action counts: ACCEPT: 22; KEEP_AS_NON_CORE: 29; MARK_AS_OVER_ANNOTATED: 12

## PN Consistency Summary

- **Consistency:** PARTIAL CONFLICT. Deep research/notes and the review establish B1 as the kidney/inner-ear-restricted, non-catalytic B subunit whose functionally relevant site is the **apical plasma membrane** (intercalated cells; IDA PMID:16769747, PMID:29993276), driving urinary acid secretion (renal tubular secretion, dRTA; PMID:12414817). The review explicitly MARKs_AS_OVER_ANNOTATED a synaptic-vesicle annotation as an inappropriate cross-isoform transfer, and never asserts a lysosomal role. The PN places B1 under "lysosomal v-ATPase" and projects **lysosomal** lumen acidification + lysosomal V1 domain — which the gene biology does not support. PN Notes ("V1 cytosolic component … pumps protons into the lysosome") mis-frame this plasma-membrane isoform.
- **PN story / NEW pressure:** PN's lysosomal acidification claim OVER-REACHES for B1. GO:0046612/GO:0007042 are verified real but are the wrong specialization: B1's evidenced compartment is apical plasma membrane, not lysosome. Already captured (correctly) by review: GO:0016324 apical plasma membrane, GO:0097254 renal tubular secretion, GO:0006885 regulation of pH. **Lysosomal projection should NOT be propagated to B1.**
- **Evidence alignment:** No overlap. PN cites generic V-ATPase/mTORC1 reviews; review is richly sourced with B1-specific genetics/structure (PMID:12414817, 16769747, 29993276, 33065002, 9916796). Review strongly better-evidenced.
- **Verdict:** OVER-REACH — PN lysosomal projection (GO:0046612/GO:0007042) is wrong-compartment for this apical-plasma-membrane kidney isoform. **Recommended edits:** [MAP] exempt ATP6V1B1 from lysosomal-acidification/lysosomal-V1 projection; restrict to vacuolar V1 domain + plasma-membrane/renal acid-secretion terms already in the review.

## Full Consistency Review

- **UniProt:** P15313 · **batch:** proteostasis-batch-2026-06-07 · **review status:** COMPLETE
- **PN placement:** two ALP leaves "V1 lysosomal v-ATPase proton pump component" (Nutrient sensing; Lysosomal acidification). **PN-node mapping:** leaf→GO:0046612 lysosomal V1 domain (more_specific_than_existing_goa); leaf→GO:0033176 V-type ATPase complex (entailed_by_goa_closure); type→GO:0007042 lysosomal lumen acidification (more_specific_than_existing_goa).
- **Consistency:** PARTIAL CONFLICT. Deep research/notes and the review establish B1 as the kidney/inner-ear-restricted, non-catalytic B subunit whose functionally relevant site is the **apical plasma membrane** (intercalated cells; IDA PMID:16769747, PMID:29993276), driving urinary acid secretion (renal tubular secretion, dRTA; PMID:12414817). The review explicitly MARKs_AS_OVER_ANNOTATED a synaptic-vesicle annotation as an inappropriate cross-isoform transfer, and never asserts a lysosomal role. The PN places B1 under "lysosomal v-ATPase" and projects **lysosomal** lumen acidification + lysosomal V1 domain — which the gene biology does not support. PN Notes ("V1 cytosolic component … pumps protons into the lysosome") mis-frame this plasma-membrane isoform.
- **PN story / NEW pressure:** PN's lysosomal acidification claim OVER-REACHES for B1. GO:0046612/GO:0007042 are verified real but are the wrong specialization: B1's evidenced compartment is apical plasma membrane, not lysosome. Already captured (correctly) by review: GO:0016324 apical plasma membrane, GO:0097254 renal tubular secretion, GO:0006885 regulation of pH. **Lysosomal projection should NOT be propagated to B1.**
- **Mapping strategy:** The shared V-ATPase node maps to lysosomal terms generically, but B1 is a tissue-restricted plasma-membrane isoform — analogous to the TOMM20/HSPA8/RAB7A "too broad" precedent. **[MAP]** flag B1 as an exception to lysosomal projection (scope=too_broad/wrong_compartment for this isoform); the generic vacuolar V1 term (GO:0000221, already in review) is the safe target.
- **Evidence alignment:** No overlap. PN cites generic V-ATPase/mTORC1 reviews; review is richly sourced with B1-specific genetics/structure (PMID:12414817, 16769747, 29993276, 33065002, 9916796). Review strongly better-evidenced.
- **Verdict:** OVER-REACH — PN lysosomal projection (GO:0046612/GO:0007042) is wrong-compartment for this apical-plasma-membrane kidney isoform. **Recommended edits:** [MAP] exempt ATP6V1B1 from lysosomal-acidification/lysosomal-V1 projection; restrict to vacuolar V1 domain + plasma-membrane/renal acid-secretion terms already in the review.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07
- review_yaml: genes/human/ATP6V1B1/ATP6V1B1-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Pre-initiation autophagy signaling | mTORC1 pathway, upstream | Nutrient sensing | V1 lysosomal v-ATPase proton pump component
- UniProt: P15313
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
- UniProt: P15313
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
- GO:0007042 lysosomal lumen acidification | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Autophagy-Lysosome Pathway|Lysosomal catabolism|Regulation of lysosomal environment|Lysosomal acidification
- GO:0033176 proton-transporting V-type ATPase complex | scope=ok_for_propagation_to_go | goa_status=entailed_by_goa_closure | from=Autophagy-Lysosome Pathway|Lysosomal catabolism|Regulation of lysosomal environment|Lysosomal acidification|V1 lysosomal v-ATPase proton pump component

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
