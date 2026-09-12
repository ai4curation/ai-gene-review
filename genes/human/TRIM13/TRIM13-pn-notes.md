# TRIM13 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: O60858
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-14
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/TRIM13/TRIM13-ai-review.yaml](TRIM13-ai-review.yaml)
- AIGR review HTML: missing - genes/human/TRIM13/TRIM13-ai-review.html
- Gene notes: present - [genes/human/TRIM13/TRIM13-notes.md](TRIM13-notes.md)
- GOA TSV: present - [genes/human/TRIM13/TRIM13-goa.tsv](TRIM13-goa.tsv)
- UniProt record: present - [genes/human/TRIM13/TRIM13-uniprot.txt](TRIM13-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/TRIM13.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/TRIM13.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/TRIM13.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/TRIM13.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: TRIM13 (RFP2/Leu5) is an endoplasmic reticulum (ER) membrane-anchored RING-type E3 ubiquitin ligase of the TRIM/RBCC family. Unlike cytosolic TRIMs it has an N-terminal RING-type zinc finger (conferring E3 ubiquitin ligase activity, EC 2.3.2.27, and required for its autopolyubiquitination), a B-box and a coiled-coil (the coiled-coil is required for induction of autophagy during ER stress), and a C-terminal transmembrane domain that anchors it as a single-pass protein in the ER membrane, concentrating at the perinuclear ER. Its best-defined role is in ER-associated degradation (ERAD): it participates in the retrotranslocation and turnover of misfolded membrane and secretory proteins (as well as regulated degradation of some correctly folded proteins) from the ER, working with the AAA-ATPase VCP/p97 (which it binds via its C-terminal domain) to deliver substrates for proteasomal degradation. TRIM13 also regulates ER-stress-induced autophagy/reticulophagy, colocalizing with SQSTM1/p62 and ZFYVE1/DFCP1 at the perinuclear ER and positively regulating macroautophagy, and has been proposed as a tumor suppressor (it lies in the minimal deletion region for B-cell chronic lymphocytic leukemia on chromosome 13). Additional reported activities include enhancing ionizing-radiation-induced p53 stabilization and apoptosis by ubiquitinating and degrading MDM2 and AKT1, and context-dependent modulation of NF-kappaB signaling: it can positively activate NF-kappaB through the TLR2 pathway (K29-linked ubiquitination of TRAF6) and in T-cell receptor signaling, but can also repress TNF-induced NF-kappaB by regulating ubiquitination and turnover of IKBKG/NEMO. It has further been implicated in antiviral responses affecting late stages of the retroviral life cycle.
- Existing/core annotation action counts: ACCEPT: 18; KEEP_AS_NON_CORE: 14; MARK_AS_OVER_ANNOTATED: 3

## PN Consistency Summary

- **Consistency:** Strongly consistent. PN (ER-membrane RING E3 ligase in ERAD + ERphagy marker), review, and notes all agree: TRIM13 is a single-pass ER-membrane RING E3 (functional RING, PMID:17314412) working with VCP/p97 in ERAD, and a positive regulator of ER-stress-induced autophagy/reticulophagy colocalizing with SQSTM1/ZFYVE1 (PMID:22178386). Genuine catalytic RING → catalytic ligase MF is correct. No contradictions.
- **PN story / NEW pressure:** Two stories: (1) ERAD/RING-ligase — already_in_goa_exact (GOA has GO:0036503 ERAD IDA+IBA and GO:0061630/0004842 ligase) → already captured. (2) ERphagy/reticulophagy — GO:0061709 reticulophagy verified real and confirmed NOT in GOA (GOA has only ERAD). The review captures this as GO:0016239 positive regulation of macroautophagy (ACCEPT, IDA PMID:22178386), so the autophagy role is partly captured but at a less specific altitude than reticulophagy. Defensible ADD: GO:0061709 reticulophagy (or regulation thereof, GO:0140500). Note TRIM13's reticulophagy evidence is "positively regulates ER-stress autophagy" → `regulation of reticulophagy` (GO:0140500, verified real) may fit better than the bare process.
- **Evidence alignment:** Strong overlap. PN ERphagy titles (Regulatory events controlling ER-phagy; N-Degron Pathway Mediates ER-phagy) are reviews; the review's reticulophagy anchor is the experimental PMID:22178386. RING-node refs 33791238/19489725 are TRIM/E3 reviews. Review refs (PMID:17314412, 22178386, 21333377, 25152375) cover ERAD + autophagy + substrate + NF-kB arms.
- **Verdict:** Consistent; ERAD/RING already captured; reticulophagy ADD warranted (regulatory framing preferable). **Recommended edits:** [YAML] add GO:0061709 reticulophagy (or GO:0140500 regulation of reticulophagy, matching the regulatory evidence) involved_in, supported by PMID:22178386 — currently new_to_goa and more specific than the existing GO:0016239.

## Full Consistency Review

- **UniProt:** O60858 (RFP2/Leu5) · **batch:** proteostasis-batch-2026-06-14 · **review status:** COMPLETE (thorough)
- **PN placement:** 3 rows — `ER proteostasis|Organelle-specific protein degradation|ER associated degradation|Cytosolic handling of ERAD substrates|ERAD-associated RING E3 ligase`; `ALP|...|Marking substrates for selective autophagy|ERphagy|Ubiquitination of ER proteins`; `UPS|E3 ubiquitin and UBL ligases|RING|TRIM / class XI|transmembrane`. **PN-node mapping:** ERAD group → mapped/exact GO:0036503 ERAD pathway (already_in_goa_exact); ERAD subtype RING → mapped GO:0061630 (already_in_goa_exact); ERphagy type+subtype → mapped/ok GO:0061709 reticulophagy (new_to_goa, x2); RING group → GO:0061630 (already_in_goa_exact).
- **Consistency:** Strongly consistent. PN (ER-membrane RING E3 ligase in ERAD + ERphagy marker), review, and notes all agree: TRIM13 is a single-pass ER-membrane RING E3 (functional RING, PMID:17314412) working with VCP/p97 in ERAD, and a positive regulator of ER-stress-induced autophagy/reticulophagy colocalizing with SQSTM1/ZFYVE1 (PMID:22178386). Genuine catalytic RING → catalytic ligase MF is correct. No contradictions.
- **PN story / NEW pressure:** Two stories: (1) ERAD/RING-ligase — already_in_goa_exact (GOA has GO:0036503 ERAD IDA+IBA and GO:0061630/0004842 ligase) → already captured. (2) ERphagy/reticulophagy — GO:0061709 reticulophagy verified real and confirmed NOT in GOA (GOA has only ERAD). The review captures this as GO:0016239 positive regulation of macroautophagy (ACCEPT, IDA PMID:22178386), so the autophagy role is partly captured but at a less specific altitude than reticulophagy. Defensible ADD: GO:0061709 reticulophagy (or regulation thereof, GO:0140500). Note TRIM13's reticulophagy evidence is "positively regulates ER-stress autophagy" → `regulation of reticulophagy` (GO:0140500, verified real) may fit better than the bare process.
- **Mapping strategy:** No node change needed. ERAD=exact and RING=exact are correct (catalytic RING, genuinely ERAD). The reticulophagy projection is appropriately new_to_goa; consider whether the PN should project `regulation of reticulophagy` given the evidence is regulatory rather than TRIM13-as-receptor.
- **Evidence alignment:** Strong overlap. PN ERphagy titles (Regulatory events controlling ER-phagy; N-Degron Pathway Mediates ER-phagy) are reviews; the review's reticulophagy anchor is the experimental PMID:22178386. RING-node refs 33791238/19489725 are TRIM/E3 reviews. Review refs (PMID:17314412, 22178386, 21333377, 25152375) cover ERAD + autophagy + substrate + NF-kB arms.
- **Verdict:** Consistent; ERAD/RING already captured; reticulophagy ADD warranted (regulatory framing preferable). **Recommended edits:** [YAML] add GO:0061709 reticulophagy (or GO:0140500 regulation of reticulophagy, matching the regulatory evidence) involved_in, supported by PMID:22178386 — currently new_to_goa and more specific than the existing GO:0016239.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-14
- review_yaml: genes/human/TRIM13/TRIM13-ai-review.yaml
- PN workbook rows: 3

## PN row 1: ER proteostasis | Organelle-specific protein degradation | ER associated degradation | Cytosolic handling of ERAD substrates | ERAD-associated RING E3 ligase
- UniProt: O60858
- In branches: ER, ALP, UPS
- PN-node mapping records (path + ancestors):
    - [subtype] ER proteostasis|Organelle-specific protein degradation|ER associated degradation|Cytosolic handling of ERAD substrates|ERAD-associated RING E3 ligase
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This PN subtype denotes ERAD-associated RING E3 ligases. Ubiquitin protein ligase activity is the appropriate shared catalytic target.
    - [type] ER proteostasis|Organelle-specific protein degradation|ER associated degradation|Cytosolic handling of ERAD substrates
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0036503 ERAD pathway]
        rationale: This PN type covers the cytosolic processing steps that receive ERAD substrates after retrotranslocation. These activities remain part of the ERAD pathway, but the source category is a specific mechanistic slice.
    - [group] ER proteostasis|Organelle-specific protein degradation|ER associated degradation
        status=mapped scope=exact GO=[GO:0036503 ERAD pathway]
        rationale: The PN group "ER associated degradation" is a direct lexical and biological match to the GO ERAD pathway term. The additional branch and class context disambiguates the source string from any broader degradation language.
    - [class] ER proteostasis|Organelle-specific protein degradation
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## PN row 2: Autophagy-Lysosome Pathway | Autophagy substrate selection | Marking substrates for selective autophagy | ERphagy | Ubiquitination of ER proteins
- UniProt: O60858
- In branches: ER, ALP, UPS
- Notes: ER-membrane E3-ligase that self-ubiquitinates and recruits SQSTM1 to damaged ER for ERphagy
- PN references (titles):
    - Regulatory events controlling ER-phagy - ScienceDirect
    - The N-Degron Pathway Mediates ER-phagy - ScienceDirect
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy|ERphagy|Ubiquitination of ER proteins
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061709 reticulophagy]
        rationale: This PN subtype denotes ubiquitin-based marking of ER cargo within the ERphagy pathway. The subtype is one mechanistic route into reticulophagy rather than a separate GO process.
    - [type] Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy|ERphagy
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061709 reticulophagy]
        rationale: The PN ERphagy marking category captures factors that mark ER cargo for selective autophagic turnover. GO uses reticulophagy for this pathway, so propagation to reticulophagy is appropriate.
    - [group] Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagy substrate selection
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad substrate-selection container. GO has useful targets for specific receptor, cargo-adaptor, and selective-autophagy leaves, but this class mixes marking, recognition, receptor regulation, and unknown roles and should not propagate as one term.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 3: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | RING | TRIM / class XI | transmembrane
- UniProt: O60858
- In branches: ER, ALP, UPS
- Signature domains: IPR001841
- Auxiliary domains: (none)
- PN references (titles):
    - 33791238 / rev
    - 19489725 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING|TRIM / class XI|transmembrane
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower E3-ligase architecture, component, or domain subdivision already covered by the curated parent E3 mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING|TRIM / class XI
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower E3-ligase architecture, component, or domain subdivision already covered by the curated parent E3 mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This PN group is a catalytic ubiquitin E3 ligase bucket. The shared GO molecular-function target is ubiquitin protein ligase activity.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (6)
- GO:0036503 ERAD pathway | scope=exact | goa_status=already_in_goa_exact | from=ER proteostasis|Organelle-specific protein degradation|ER associated degradation
- GO:0036503 ERAD pathway | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=ER proteostasis|Organelle-specific protein degradation|ER associated degradation|Cytosolic handling of ERAD substrates
- GO:0061630 ubiquitin protein ligase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=ER proteostasis|Organelle-specific protein degradation|ER associated degradation|Cytosolic handling of ERAD substrates|ERAD-associated RING E3 ligase
- GO:0061709 reticulophagy | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy|ERphagy
- GO:0061709 reticulophagy | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy|ERphagy|Ubiquitination of ER proteins
- GO:0061630 ubiquitin protein ligase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
