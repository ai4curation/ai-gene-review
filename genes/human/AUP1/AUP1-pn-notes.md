# AUP1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9Y679
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-06
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/AUP1/AUP1-ai-review.yaml](AUP1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/AUP1/AUP1-ai-review.html](AUP1-ai-review.html)
- Gene notes: present - [genes/human/AUP1/AUP1-notes.md](AUP1-notes.md)
- GOA TSV: present - [genes/human/AUP1/AUP1-goa.tsv](AUP1-goa.tsv)
- UniProt record: present - [genes/human/AUP1/AUP1-uniprot.txt](AUP1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/AUP1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/AUP1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/AUP1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/AUP1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/AUP1/AUP1-deep-research-falcon.md](AUP1-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: AUP1 (Ancient Ubiquitous Protein 1) is a conserved, ubiquitously expressed monotopic membrane protein that resides on the cytosolic face of the endoplasmic reticulum membrane and on the lipid droplet surface monolayer, inserting via an N-terminal hydrophobic hairpin so that both termini face the cytosol. Its principal molecular role is to act as an adaptor that recruits the soluble E2 ubiquitin-conjugating enzyme UBE2G2 (via a C-terminal G2 binding region) to ER-associated degradation (ERAD) ubiquitin ligase machinery, including the HRD1-SEL1L complex and the lipid-droplet/ER E3 ligases gp78/AMFR and TRC8/RNF139. Through this activity AUP1 couples substrate ubiquitination to dislocation and proteasomal degradation of misfolded ER proteins, and drives sterol-regulated ubiquitination and ERAD of HMGCR, INSIG1, SREBF1 and SREBF2. AUP1 also has lipid-droplet-regulatory functions: it binds ubiquitin through an internal CUE domain, is itself monoubiquitinated in a CUE-dependent manner to promote lipid droplet clustering, and its level controls lipid droplet abundance. Additional reported roles include hepatic VLDL/apolipoprotein B assembly and secretion. AUP1 is exploited by flaviviruses, whose NS4A protein relocalizes it to autophagosomes to trigger lipophagy.
- Existing/core annotation action counts: ACCEPT: 30; KEEP_AS_NON_CORE: 5; MARK_AS_OVER_ANNOTATED: 6

## PN Consistency Summary

- **Consistency:** Strong agreement across all sources. Deep research (falcon), review YAML, and PN annotations all converge on AUP1 as an ER/lipid-droplet monotopic membrane adaptor that recruits the E2 UBE2G2 (via G2BR) and binds ubiquitin (CUE) to drive ERAD, with secondary LD-clustering and (virus-induced) lipophagy roles. No contradictions. The three PN branch rows (ER/ALP/UPS) each map to a function the review independently accepts as core (ERAD, ubiquitin binding/E2 recruitment) or non-core (lipophagy).
- **PN story / NEW pressure:** No NEW GO pressure. All three projected terms are already captured. GO:0036503 ERAD pathway and GO:0061724 lipophagy are present in GOA and ACCEPT/KEEP_AS_NON_CORE in the review (lipophagy correctly flagged virus-context, non-core). GO:0097466 ubiquitin-dependent glycoprotein ERAD pathway (verified real) is NOT in GOA and is more specific; the review does not list it but its parent GO:0036503 is accepted. Review's `proposed_new_terms` is empty — appropriate.
- **Evidence alignment:** PN row 2 cites Spandl 2011 (PMID:21127063), which is in the review (G2BR/Ube2g2 binding). PN otherwise cites few papers; the review is far richer (Klemm 2011 PMID:21857022, Jo 2013 PMID:23223569, Smith 2021 PMID:34879065, Frachon 2024 PMID:38474353, flavivirus PMID:29902443). No divergence — review is a strict superset.
- **Verdict:** Consistent and well-curated; no NEW term, no mapping change. Optional: GO:0097466 could be added to the review as a more-specific ERAD term but is not required.

## Full Consistency Review

- **UniProt:** Q9Y679 · **batch:** proteostasis-batch-2026-06-06 · **review status:** COMPLETE (thorough; 40 annotations reviewed)
- **PN placement:** `ER proteostasis|...|ER associated degradation|Retrotranslocation channel complex`; `ALP|...|Lipophagy|Ubiquitination of lipid droplet surface proteins`; `UPS|Ubiquitin and UBL binding|protein quality control|ERAD cofactor|CUE`. PN-node mappings: ERAD group=mapped/exact GO:0036503; Lipophagy type=mapped/propagation GO:0061724; ERAD-cofactor type=mapped/propagation GO:0097466; broader ancestors=no_mapping or context_only.
- **Consistency:** Strong agreement across all sources. Deep research (falcon), review YAML, and PN annotations all converge on AUP1 as an ER/lipid-droplet monotopic membrane adaptor that recruits the E2 UBE2G2 (via G2BR) and binds ubiquitin (CUE) to drive ERAD, with secondary LD-clustering and (virus-induced) lipophagy roles. No contradictions. The three PN branch rows (ER/ALP/UPS) each map to a function the review independently accepts as core (ERAD, ubiquitin binding/E2 recruitment) or non-core (lipophagy).
- **PN story / NEW pressure:** No NEW GO pressure. All three projected terms are already captured. GO:0036503 ERAD pathway and GO:0061724 lipophagy are present in GOA and ACCEPT/KEEP_AS_NON_CORE in the review (lipophagy correctly flagged virus-context, non-core). GO:0097466 ubiquitin-dependent glycoprotein ERAD pathway (verified real) is NOT in GOA and is more specific; the review does not list it but its parent GO:0036503 is accepted. Review's `proposed_new_terms` is empty — appropriate.
- **Mapping strategy:** No change warranted. ERAD group=mapped/exact is well justified (AUP1 is a bona fide ERAD factor). The two propagation-scope mappings (lipophagy, glycoprotein-ERAD) are defensible at gene level for AUP1; the no_mapping/context_only calls on broad UPS/ALP ancestors are consistent with the TOMM20/HSPA8 "too broad" precedent.
- **Evidence alignment:** PN row 2 cites Spandl 2011 (PMID:21127063), which is in the review (G2BR/Ube2g2 binding). PN otherwise cites few papers; the review is far richer (Klemm 2011 PMID:21857022, Jo 2013 PMID:23223569, Smith 2021 PMID:34879065, Frachon 2024 PMID:38474353, flavivirus PMID:29902443). No divergence — review is a strict superset.
- **Verdict:** Consistent and well-curated; no NEW term, no mapping change. Optional: GO:0097466 could be added to the review as a more-specific ERAD term but is not required.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-06
- review_yaml: genes/human/AUP1/AUP1-ai-review.yaml
- PN workbook rows: 3

## PN row 1: ER proteostasis | Organelle-specific protein degradation | ER associated degradation | Retrotranslocation channel complex
- UniProt: Q9Y679
- In branches: ER, ALP, UPS
- PN-node mapping records (path + ancestors):
    - [type] ER proteostasis|Organelle-specific protein degradation|ER associated degradation|Retrotranslocation channel complex
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower taxonomy bucket already covered by a curated parent mapping or by gene-level annotations. No additional direct GO mapping is appropriate from this node.
    - [group] ER proteostasis|Organelle-specific protein degradation|ER associated degradation
        status=mapped scope=exact GO=[GO:0036503 ERAD pathway]
        rationale: The PN group "ER associated degradation" is a direct lexical and biological match to the GO ERAD pathway term. The additional branch and class context disambiguates the source string from any broader degradation language.
    - [class] ER proteostasis|Organelle-specific protein degradation
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## PN row 2: Autophagy-Lysosome Pathway | Autophagy substrate selection | Marking substrates for selective autophagy | Lipophagy | Ubiquitination of lipid droplet surface proteins
- UniProt: Q9Y679
- In branches: ER, ALP, UPS
- Notes: Recruits E2-ligase UBE2G2 to lipid droplets to ubiquitinate surface proteins for lipophagy
- PN references (titles):
    - Ancient Ubiquitous Protein 1 (AUP1) Localizes to Lipid Droplets and Binds the E2 Ubiquitin Conjugase G2 (Ube2g2) via Its G2 Binding Region* ♦ - Journal of Biological Chemistry (jbc.org)
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy|Lipophagy|Ubiquitination of lipid droplet surface proteins
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a contextual PN role. The label is useful for curator triage, but by itself does not support a universal GO assertion for all member genes beyond curated ancestor or child mappings.
    - [type] Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy|Lipophagy
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061724 lipophagy]
        rationale: This PN type denotes factors that mark lipid cargo for selective autophagy. The category is narrower than the full lipophagy process, so propagation scope is the correct fit.
    - [group] Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagy substrate selection
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad substrate-selection container. GO has useful targets for specific receptor, cargo-adaptor, and selective-autophagy leaves, but this class mixes marking, recognition, receptor regulation, and unknown roles and should not propagate as one term.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 3: Ubiquitin Proteasome System | Ubiquitin and UBL binding | protein quality control | ERAD cofactor | CUE
- UniProt: Q9Y679
- In branches: ER, ALP, UPS
- Signature domains: IPR003892
- Auxiliary domains: (none)
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|Ubiquitin and UBL binding|protein quality control|ERAD cofactor|CUE
        status=no_mapping scope= GO=[]
        rationale: Reviewed manually as a UPS source node. No single GO term is appropriate for direct propagation from this PN label without narrower context or gene-level evidence.
    - [type] Ubiquitin Proteasome System|Ubiquitin and UBL binding|protein quality control|ERAD cofactor
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0097466 ubiquitin-dependent glycoprotein ERAD pathway]
        rationale: This PN type groups ubiquitin/UBL-binding factors that act as ERAD cofactors in protein-quality-control contexts. The best available GO target in the local cache is ubiquitin-dependent glycoprotein ERAD pathway, used here at propagation scope.
    - [group] Ubiquitin Proteasome System|Ubiquitin and UBL binding|protein quality control
        status=context_only scope=too_broad_to_propagate GO=[GO:0043161 proteasome-mediated ubiquitin-dependent protein catabolic process]
        rationale: This PN group is a protein-quality-control context bucket, but its descendants include ERAD cofactors, HSP70 cochaperone context, stalled-chain recognition, and other mixed roles. Direct propagation should come from narrower nodes such as ERAD cofactor.
    - [class] Ubiquitin Proteasome System|Ubiquitin and UBL binding
        status=context_only scope=too_broad_to_propagate GO=[GO:0140036 ubiquitin-modified protein reader activity]
        rationale: This class records ubiquitin/UBL-reader context, but the subtree mixes ubiquitin, SUMO, UBL-domain, domain-architecture, catalytic, signaling, trafficking, and nucleic-acid process buckets. It is useful context, not a safe direct propagation.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (3)
- GO:0036503 ERAD pathway | scope=exact | goa_status=already_in_goa_exact | from=ER proteostasis|Organelle-specific protein degradation|ER associated degradation
- GO:0061724 lipophagy | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy|Lipophagy
- GO:0097466 ubiquitin-dependent glycoprotein ERAD pathway | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Ubiquitin Proteasome System|Ubiquitin and UBL binding|protein quality control|ERAD cofactor

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
