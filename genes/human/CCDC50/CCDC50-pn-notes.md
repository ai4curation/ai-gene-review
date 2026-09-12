# CCDC50 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q8IVM0
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-14
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/CCDC50/CCDC50-ai-review.yaml](CCDC50-ai-review.yaml)
- AIGR review HTML: missing - genes/human/CCDC50/CCDC50-ai-review.html
- Gene notes: present - [genes/human/CCDC50/CCDC50-notes.md](CCDC50-notes.md)
- GOA TSV: present - [genes/human/CCDC50/CCDC50-goa.tsv](CCDC50-goa.tsv)
- UniProt record: present - [genes/human/CCDC50/CCDC50-uniprot.txt](CCDC50-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/CCDC50.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/CCDC50.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CCDC50.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CCDC50.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: CCDC50 (Coiled-coil domain-containing protein 50), also known as Ymer, is a soluble, predominantly cytoplasmic/cytosolic protein with an N-terminal coiled-coil region and a large disordered, basic C-terminal region. It is a ubiquitin-binding adapter that recognizes lysine-63-linked polyubiquitin chains and functions in ubiquitin-dependent signaling and receptor trafficking. CCDC50/Ymer is rapidly tyrosine-phosphorylated upon epidermal growth factor (EGF) stimulation and modulates EGF receptor (EGFR) signaling; it associates with the RING E3 ubiquitin ligase RNF126 and participates in ubiquitin-dependent endosomal sorting of activated EGFR. Through its interaction with the deubiquitinase/ubiquitin-editing enzyme A20 (TNFAIP3) and binding to K63-linked polyubiquitin on RIPK1, CCDC50/Ymer negatively regulates NF-kB signaling. It has additionally been reported (in literature beyond the current annotation set) to act as a TBK1-binding selective autophagy receptor that links K63-polyubiquitinated cargo to LC3 in aggrephagy/reticulophagy and in restraint of antiviral innate immunity. CCDC50 is associated with microtubules of the cytoskeleton and mitotic apparatus. It is broadly expressed, with isoform 1 (the major isoform) detected in most tissues; in the adult inner ear its expression is restricted to cochlear pillar cells, the stria vascularis, and the vestibular sensory epithelia. Mutations in CCDC50 cause autosomal dominant progressive non-syndromic hearing loss (DFNA44).
- Existing/core annotation action counts: ACCEPT: 3; KEEP_AS_NON_CORE: 5

## PN Consistency Summary

- **Consistency:** Consistent at the conclusion level but with an evidence-source divergence. PN row 1 rests on ONE paper — "CCDC50 suppresses NLRP3 inflammasome... autophagic degradation of NLRP3" (EMBO reports) — delivering ubiquitinated NLRP3 to autophagosomes. The review/notes do NOT cite that EMBO paper; instead the autophagy-receptor role is built from K63-polyUb binding (PMID:18029035), RNF126/EGFR sorting (PMID:23418353), and a literature-level "TBK1-binding SLR in aggrephagy/reticulophagy / RIG-I-MAVS turnover" framing (Hou et al. Autophagy 2021, not cached). Both routes converge on the same MF.
- **PN story / NEW pressure:** PN and review AGREE on the new MF: GO:0160247 autophagy cargo adaptor activity (verified real) is **new_to_goa** in PN and **proposed_new_terms** in the review (proposed child "K63-linked polyubiquitin selective autophagy receptor activity" under GO:0160247, supported_by PMID:18029035). Clear ADD, well-justified — current GOA has only ubiquitin-ligase binding (GO:0031625) and bare protein binding.
- **Evidence alignment:** DIVERGENT references — PN cites the EMBO NLRP3 paper; review cites NF-kB/EGFR/K63 papers. Same destination, different supporting literature; the EMBO NLRP3 paper would strengthen the review's NEW-term justification.
- **Verdict:** CONSISTENT conclusion (GO:0160247 ADD agreed by both); evidence sources diverge. **Recommended edits:** [REF] add the CCDC50/NLRP3 autophagic-degradation EMBO reports paper to the review references and as supporting_text for the proposed GO:0160247 receptor MF.

## Full Consistency Review

- **UniProt:** Q8IVM0 (Ymer) · **batch:** proteostasis-batch-2026-06-14 · **review status:** COMPLETE (~239 lines, small)
- **PN placement:** ALP `Autophagy substrate selection|Selective autophagy receptor|Individual substrates` + UPS `Ubiquitin and UBL binding|trafficking|macroautophagy|MIU` ; **PN-node mapping:** Individual substrates→GO:0160247 cargo adaptor (new_to_goa); UPS macroautophagy type→GO:0016236 context_only; ancestors no_mapping/context_only.
- **Consistency:** Consistent at the conclusion level but with an evidence-source divergence. PN row 1 rests on ONE paper — "CCDC50 suppresses NLRP3 inflammasome... autophagic degradation of NLRP3" (EMBO reports) — delivering ubiquitinated NLRP3 to autophagosomes. The review/notes do NOT cite that EMBO paper; instead the autophagy-receptor role is built from K63-polyUb binding (PMID:18029035), RNF126/EGFR sorting (PMID:23418353), and a literature-level "TBK1-binding SLR in aggrephagy/reticulophagy / RIG-I-MAVS turnover" framing (Hou et al. Autophagy 2021, not cached). Both routes converge on the same MF.
- **PN story / NEW pressure:** PN and review AGREE on the new MF: GO:0160247 autophagy cargo adaptor activity (verified real) is **new_to_goa** in PN and **proposed_new_terms** in the review (proposed child "K63-linked polyubiquitin selective autophagy receptor activity" under GO:0160247, supported_by PMID:18029035). Clear ADD, well-justified — current GOA has only ubiquitin-ligase binding (GO:0031625) and bare protein binding.
- **Mapping strategy:** Mapping is correct (KEY PATTERN: elevate cargo-adaptor MF over bare protein binding, ~2 IPI kept non-core). PN GO:0160247 = review proposed parent. Sound, not an over-reach.
- **Evidence alignment:** DIVERGENT references — PN cites the EMBO NLRP3 paper; review cites NF-kB/EGFR/K63 papers. Same destination, different supporting literature; the EMBO NLRP3 paper would strengthen the review's NEW-term justification.
- **Verdict:** CONSISTENT conclusion (GO:0160247 ADD agreed by both); evidence sources diverge. **Recommended edits:** [REF] add the CCDC50/NLRP3 autophagic-degradation EMBO reports paper to the review references and as supporting_text for the proposed GO:0160247 receptor MF.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-14
- review_yaml: genes/human/CCDC50/CCDC50-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Autophagy substrate selection | Selective autophagy receptor | Individual substrates
- UniProt: Q8IVM0
- In branches: ALP, UPS
- Notes: Delivers ubiquitinated NLRP3 inflammasome to autophagosome for degradation
- PN references (titles):
    - CCDC50 suppresses NLRP3 inflammasome activity by mediating autophagic degradation of NLRP3 | EMBO reports (embopress.org)
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Individual substrates
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0160247 autophagy cargo adaptor activity]
        rationale: This PN category groups receptors such as TRIM-family factors that bind specific substrates and recruit autophagy components for their turnover. That aligns best with autophagy cargo adaptor activity rather than with a single selective-autophagy process term.
    - [group] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagy substrate selection
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad substrate-selection container. GO has useful targets for specific receptor, cargo-adaptor, and selective-autophagy leaves, but this class mixes marking, recognition, receptor regulation, and unknown roles and should not propagate as one term.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 2: Ubiquitin Proteasome System | Ubiquitin and UBL binding | trafficking | macroautophagy | MIU
- UniProt: Q8IVM0
- In branches: ALP, UPS
- Signature domains: PMID: 16499958
- Auxiliary domains: (none)
- PN references (titles):
    - 16499958
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|Ubiquitin and UBL binding|trafficking|macroautophagy|MIU
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a selective-autophagy or trafficking subdivision under a UPS binding context. The autophagy context is real, but this node is too indirect for automatic GO propagation.
    - [type] Ubiquitin Proteasome System|Ubiquitin and UBL binding|trafficking|macroautophagy
        status=context_only scope=too_broad_to_propagate GO=[GO:0016236 macroautophagy]
        rationale: This PN type is an autophagy-related trafficking context, but the earlier TRAPP review showed that generic autophagy propagation from component or binding-context buckets can be too strong. Keep as context unless gene-level evidence supports macroautophagy.
    - [group] Ubiquitin Proteasome System|Ubiquitin and UBL binding|trafficking
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a UPS taxonomy container. Its descendants mix catalytic roles, complex membership, binding domains, regulators, adaptors, and substrate-context labels, so a single propagating GO assertion would overstate the shared biology.
    - [class] Ubiquitin Proteasome System|Ubiquitin and UBL binding
        status=context_only scope=too_broad_to_propagate GO=[GO:0140036 ubiquitin-modified protein reader activity]
        rationale: This class records ubiquitin/UBL-reader context, but the subtree mixes ubiquitin, SUMO, UBL-domain, domain-architecture, catalytic, signaling, trafficking, and nucleic-acid process buckets. It is useful context, not a safe direct propagation.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:0160247 autophagy cargo adaptor activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Individual substrates

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
