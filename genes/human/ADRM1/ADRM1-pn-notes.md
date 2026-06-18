# ADRM1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q16186
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-03 (PR 1344)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ADRM1/ADRM1-ai-review.yaml](ADRM1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ADRM1/ADRM1-ai-review.html](ADRM1-ai-review.html)
- Gene notes: present - [genes/human/ADRM1/ADRM1-notes.md](ADRM1-notes.md)
- GOA TSV: present - [genes/human/ADRM1/ADRM1-goa.tsv](ADRM1-goa.tsv)
- UniProt record: present - [genes/human/ADRM1/ADRM1-uniprot.txt](ADRM1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ADRM1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ADRM1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ADRM1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ADRM1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/ADRM1/ADRM1-deep-research-manual.md](ADRM1-deep-research-manual.md)

## AIGR Review Snapshot

- Description: ADRM1 encodes the human proteasomal ubiquitin receptor Rpn13, a 19S regulatory-particle subunit/cofactor of the 26S proteasome. Its N-terminal Pru domain binds ubiquitin signals and the Rpn2/PSMD1 proteasome scaffold, while its C-terminal DEUBAD region binds the UCHL5/UCH37 deubiquitinase. Through these interactions ADRM1 helps recruit ubiquitinated substrates and coordinate deubiquitinase activity during proteasome-mediated protein degradation in cytosolic and nuclear proteostasis.
- Existing/core annotation action counts: ACCEPT: 90; MARK_AS_OVER_ANNOTATED: 16; MODIFY: 10; REMOVE: 1

## PN Consistency Summary

- **Consistency:** Deep research (manual), notes, review YAML, and all PN-node mappings are mutually consistent. ADRM1/Rpn13 is a 19S regulatory-particle ubiquitin receptor (Pru domain) that binds Rpn2/PSMD1 and recruits/activates the UCHL5/UCH37 DUB (PMID:16990800, 17139257, 18497817, 20471946, 29636472). No contradictions.
- **PN story / NEW pressure:** PN's key non-trivial assertion is base- (not lid-) subcomplex membership (GO:0008540, OLS-verified real). GOA carried an IBA GO:0008541 **lid** subcomplex annotation; the review **MODIFIES** it to GO:0008540 base subcomplex, citing Rpn13/Rpn10 as base ubiquitin receptors (PMID:29636472, 33729481) — exactly executing the PN projection. Other projected terms (GO:0000502, GO:0005838) already captured/entailed. Review also adds specific MFs beyond PN (GO:0035800 deubiquitinase activator via MODIFY of GO:0061133; GO:0043130 ubiquitin binding; GO:0070628 proteasome binding; GO:1990381 ubiquitin-specific protease binding). Conclusion: PN base-subcomplex correction = legitimate ADD/MODIFY, executed; rest already captured.
- **Evidence alignment:** PN references (PMID:19145068, 19489727, 18497827, 32160516) overlap the review's Rpn13/Pru/DEUBAD evidence base; the review additionally uses the foundational identification and structural papers (16990800, 17139257, 18497817, 20471946, 29636472, 33729481). Strong overlap, review enriched — no conflict.
- **Verdict:** Fully consistent; PN's lid→base correction and regulatory-particle/proteasome-complex mappings all validated and executed in the review. **Recommended edits:** none (mapping and review aligned).

## Full Consistency Review

- **UniProt:** Q16186 (Rpn13) · **batch:** proteostasis-batch-2026-06-03 · **review status:** COMPLETE
- **PN placement:** `UPS|Proteasome and associated proteins|proteasome regulatory particle subunit|base, nonATPase|PRU, DEUBAD` (row 1) and `UPS|Ubiquitin and UBL binding|proteasomal subunits|regulatory particle|idiosyncratic Ub binding / PRU` (row 2) ; **PN-node mapping:** type `base, nonATPase`=mapped→**GO:0008540 base subcomplex** (more_specific_than_existing_goa); group `regulatory particle subunit`=mapped→**GO:0005838 regulatory particle**; group `proteasomal subunits`=mapped→**GO:0000502 proteasome complex** (already_in_goa_exact); ub-binding classes=context_only.
- **Consistency:** Deep research (manual), notes, review YAML, and all PN-node mappings are mutually consistent. ADRM1/Rpn13 is a 19S regulatory-particle ubiquitin receptor (Pru domain) that binds Rpn2/PSMD1 and recruits/activates the UCHL5/UCH37 DUB (PMID:16990800, 17139257, 18497817, 20471946, 29636472). No contradictions.
- **PN story / NEW pressure:** PN's key non-trivial assertion is base- (not lid-) subcomplex membership (GO:0008540, OLS-verified real). GOA carried an IBA GO:0008541 **lid** subcomplex annotation; the review **MODIFIES** it to GO:0008540 base subcomplex, citing Rpn13/Rpn10 as base ubiquitin receptors (PMID:29636472, 33729481) — exactly executing the PN projection. Other projected terms (GO:0000502, GO:0005838) already captured/entailed. Review also adds specific MFs beyond PN (GO:0035800 deubiquitinase activator via MODIFY of GO:0061133; GO:0043130 ubiquitin binding; GO:0070628 proteasome binding; GO:1990381 ubiquitin-specific protease binding). Conclusion: PN base-subcomplex correction = legitimate ADD/MODIFY, executed; rest already captured.
- **Mapping strategy:** This gene **confirms** the base-subcomplex mapping (lid→base is a genuine GOA correction, not over-reach). All PN scopes are correctly leveled (CC membership terms, no over-broad propagation). No change needed.
- **Evidence alignment:** PN references (PMID:19145068, 19489727, 18497827, 32160516) overlap the review's Rpn13/Pru/DEUBAD evidence base; the review additionally uses the foundational identification and structural papers (16990800, 17139257, 18497817, 20471946, 29636472, 33729481). Strong overlap, review enriched — no conflict.
- **Verdict:** Fully consistent; PN's lid→base correction and regulatory-particle/proteasome-complex mappings all validated and executed in the review. **Recommended edits:** none (mapping and review aligned).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/ADRM1/ADRM1-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Ubiquitin Proteasome System | Proteasome and associated proteins | proteasome regulatory particle subunit | base, nonATPase | PRU, DEUBAD
- UniProt: Q16186
- In branches: UPS
- Signature domains: (none)
- Auxiliary domains: IPR044868, IPR044867
- PN references (titles):
    - 19145068 / rev
    - 19489727 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|Proteasome and associated proteins|proteasome regulatory particle subunit|base, nonATPase|PRU, DEUBAD
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower proteasome component, chaperone, adaptor, domain, or isoform subdivision already covered by a curated parent proteasome mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|Proteasome and associated proteins|proteasome regulatory particle subunit|base, nonATPase
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0008540 proteasome regulatory particle, base subcomplex]
        rationale: This PN type captures base subunits of the proteasome regulatory particle. The matching GO cellular-component term is proteasome regulatory particle, base subcomplex.
    - [group] Ubiquitin Proteasome System|Proteasome and associated proteins|proteasome regulatory particle subunit
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0005838 proteasome regulatory particle]
        rationale: This PN group captures proteasome regulatory particle subunits. The matching GO cellular-component term is proteasome regulatory particle.
    - [class] Ubiquitin Proteasome System|Proteasome and associated proteins
        status=context_only scope=too_broad_to_propagate GO=[GO:0000502 proteasome complex]
        rationale: This class records the proteasome branch context, but descendants include core and regulatory particle subunits, activators, assembly chaperones, adaptors, DUBs, E3 ligases, enzymes, and transcriptional regulators. Propagation should come from narrower nodes.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## PN row 2: Ubiquitin Proteasome System | Ubiquitin and UBL binding | proteasomal subunits | regulatory particle | idiosyncratic Ub binding / PRU
- UniProt: Q16186
- In branches: UPS
- Signature domains: PMID: 18497827, PMID: 32160516 (IPR044868)
- Auxiliary domains: IPR044867
- PN references (titles):
    - 18497827
    - 32160516
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|Ubiquitin and UBL binding|proteasomal subunits|regulatory particle|idiosyncratic Ub binding / PRU
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0005838 proteasome regulatory particle]
        rationale: This PN type/subtype is a ubiquitin-binding regulatory-particle subunit bucket. The safe GO target is proteasome regulatory particle.
    - [type] Ubiquitin Proteasome System|Ubiquitin and UBL binding|proteasomal subunits|regulatory particle
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0005838 proteasome regulatory particle]
        rationale: This PN type/subtype is a ubiquitin-binding regulatory-particle subunit bucket. The safe GO target is proteasome regulatory particle.
    - [group] Ubiquitin Proteasome System|Ubiquitin and UBL binding|proteasomal subunits
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0000502 proteasome complex]
        rationale: This PN group captures ubiquitin/UBL-binding proteasomal subunits. The shared GO target is proteasome complex.
    - [class] Ubiquitin Proteasome System|Ubiquitin and UBL binding
        status=context_only scope=too_broad_to_propagate GO=[GO:0140036 ubiquitin-modified protein reader activity]
        rationale: This class records ubiquitin/UBL-reader context, but the subtree mixes ubiquitin, SUMO, UBL-domain, domain-architecture, catalytic, signaling, trafficking, and nucleic-acid process buckets. It is useful context, not a safe direct propagation.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (5)
- GO:0005838 proteasome regulatory particle | scope=ok_for_propagation_to_go | goa_status=entailed_by_goa_closure | from=Ubiquitin Proteasome System|Proteasome and associated proteins|proteasome regulatory particle subunit
- GO:0008540 proteasome regulatory particle, base subcomplex | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Ubiquitin Proteasome System|Proteasome and associated proteins|proteasome regulatory particle subunit|base, nonATPase
- GO:0000502 proteasome complex | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|Ubiquitin and UBL binding|proteasomal subunits
- GO:0005838 proteasome regulatory particle | scope=ok_for_propagation_to_go | goa_status=entailed_by_goa_closure | from=Ubiquitin Proteasome System|Ubiquitin and UBL binding|proteasomal subunits|regulatory particle
- GO:0005838 proteasome regulatory particle | scope=ok_for_propagation_to_go | goa_status=entailed_by_goa_closure | from=Ubiquitin Proteasome System|Ubiquitin and UBL binding|proteasomal subunits|regulatory particle|idiosyncratic Ub binding / PRU

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
