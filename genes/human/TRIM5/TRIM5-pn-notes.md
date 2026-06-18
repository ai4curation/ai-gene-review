# TRIM5 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9C035
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-14
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/TRIM5/TRIM5-ai-review.yaml](TRIM5-ai-review.yaml)
- AIGR review HTML: missing - genes/human/TRIM5/TRIM5-ai-review.html
- Gene notes: present - [genes/human/TRIM5/TRIM5-notes.md](TRIM5-notes.md)
- GOA TSV: present - [genes/human/TRIM5/TRIM5-goa.tsv](TRIM5-goa.tsv)
- UniProt record: present - [genes/human/TRIM5/TRIM5-uniprot.txt](TRIM5-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/TRIM5.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/TRIM5.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/TRIM5.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/TRIM5.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: TRIM5 (tripartite motif-containing protein 5; the antiviral isoform is TRIM5alpha) is a cytoplasmic RING-type E3 ubiquitin ligase of the TRIM/RBCC family that functions both as a capsid-specific retroviral restriction factor and as an innate immune pattern-recognition receptor. Its RBCC architecture comprises an N-terminal RING-type zinc finger that confers E3 ubiquitin ligase activity (EC 2.3.2.27), a B-box-type zinc finger and a coiled-coil that drive the higher- and lower-order self-multimerization required for activity, and a C-terminal B30.2/PRYSPRY (SPRY) domain that directly recognizes the assembled retroviral capsid lattice. Through the PRYSPRY domain TRIM5alpha binds the hexameric capsid lattice of incoming non-host-adapted retroviruses and blocks infection at an early post-entry step, before reverse transcription; polymorphisms in the PRYSPRY domain account for the species-specific spectrum of restriction (human TRIM5alpha restricts N-tropic MLV, EIAV, SIVmac, FIV and BIV but only weakly HIV-1). Capsid lattice binding also triggers TRIM5's RING E3 ligase activity: together with the UBE2V1-UBE2N (UBC13-UEV1A) E2 complex it synthesizes unanchored Lys63-linked polyubiquitin chains that activate the TAK1 (MAP3K7)-TAB2-TAB3 kinase complex by autophosphorylation, inducing NF-kappaB- and AP-1/MAPK-responsive inflammatory genes and thereby acting as a sensor that links capsid detection to innate immune signaling. TRIM5alpha is itself regulated by ubiquitination (RING/UBE2D2-dependent autoubiquitination, monoubiquitination by TRIM21) and undergoes rapid proteasome-dependent turnover upon engaging restriction-sensitive virus. It additionally functions in selective ("precision") autophagy: it acts as a platform that assembles and activates the autophagy regulators ULK1 and BECN1 (Beclin-1, by dissociating it from BCL2 and TAB2) and as a selective autophagy receptor that directly recognizes the HIV-1 capsid protein p24 and delivers it for autophagic degradation, interacting with SQSTM1/p62 and the ATG8 family proteins GABARAP/GABARAPL1/GABARAPL2 and MAP1LC3A/C. TRIM5alpha localizes predominantly to cytoplasmic bodies, where it can form homodimers and homotrimers and colocalizes with proteasomal subunits and SQSTM1.
- Existing/core annotation action counts: ACCEPT: 26; KEEP_AS_NON_CORE: 21; MARK_AS_OVER_ANNOTATED: 5

## PN Consistency Summary

- **Consistency:** Strongly consistent. PN (selective-autophagy receptor for virophagy + catalytic RING E3 ligase), review YAML, and notes all agree: TRIM5alpha is a genuine RING E3 (capsid-triggered K63 chains via UBE2V1-UBE2N → TAK1/NF-kB; PMID:21512573) AND a selective autophagy receptor that delivers HIV-1 capsid for degradation and scaffolds ULK1/BECN1 (PMID:25127057). Both the RING-ligase and the receptor arms are real and confirmed by the review's experimental annotations. TRIM5 has a functional RING (per the critical-distinction guideline) — catalytic ligase MF is correct here.
- **PN story / NEW pressure:** PN xenophagy is genuinely more specific than GOA: GOA carries GO:0006914 autophagy (IDA, PMID:25127057) but NOT GO:0098792 xenophagy (verified real). Virophagy of the HIV-1 capsid is textbook xenophagy → defensible ADD. The RING/ligase node is already_in_goa_exact (GO:0061630 present, IBA+IEA) — already captured. The selective-autophagy-**receptor MF** (cargo adaptor) is captured in the review as GO:0030674 protein-macromolecule adaptor activity (ACCEPT); the more specific GO:0160247 autophagy cargo adaptor activity (verified real, child of GO:0030674) would be a precise upgrade.
- **Evidence alignment:** Strong overlap. PN cites the selective-autophagy/LIR review and the TRIM5-virophagy paper (= PMID:25127057, in review HIGH) plus 33791238/19489725/21490953 (TRIM/E3 reviews). Review's core refs (PMID:21512573, 25127057, 22291694, 18248090) cover both arms.
- **Verdict:** Consistent; xenophagy ADD warranted; RING ligase already captured. **Recommended edits:** [YAML] add GO:0098792 xenophagy (involved_in, supported by PMID:25127057) as a more-specific child of the existing autophagy annotation. [YAML] optionally upgrade the GO:0030674 adaptor MF to the more specific GO:0160247 autophagy cargo adaptor activity for the capsid-receptor role.

## Full Consistency Review

- **UniProt:** Q9C035 (TRIM5alpha) · **batch:** proteostasis-batch-2026-06-14 · **review status:** COMPLETE (very thorough, 40+ annotations)
- **PN placement:** 3 rows — `ALP|Autophagy substrate selection|Selective autophagy receptor|Xenophagy`; `UPS|E3 ubiquitin and UBL ligases|RING|TRIM / class IV|SPRY`; `UPS|Ubiquitin and UBL binding|E3 ligase|RING / TRIM class IV|SIM`. **PN-node mapping:** Xenophagy type → mapped/ok GO:0098792 xenophagy (more_specific_than_existing_goa); RING group → mapped/ok GO:0061630 ubiquitin protein ligase activity (already_in_goa_exact, x2); E3-ligase ancestors = context_only/too_broad or no_mapping.
- **Consistency:** Strongly consistent. PN (selective-autophagy receptor for virophagy + catalytic RING E3 ligase), review YAML, and notes all agree: TRIM5alpha is a genuine RING E3 (capsid-triggered K63 chains via UBE2V1-UBE2N → TAK1/NF-kB; PMID:21512573) AND a selective autophagy receptor that delivers HIV-1 capsid for degradation and scaffolds ULK1/BECN1 (PMID:25127057). Both the RING-ligase and the receptor arms are real and confirmed by the review's experimental annotations. TRIM5 has a functional RING (per the critical-distinction guideline) — catalytic ligase MF is correct here.
- **PN story / NEW pressure:** PN xenophagy is genuinely more specific than GOA: GOA carries GO:0006914 autophagy (IDA, PMID:25127057) but NOT GO:0098792 xenophagy (verified real). Virophagy of the HIV-1 capsid is textbook xenophagy → defensible ADD. The RING/ligase node is already_in_goa_exact (GO:0061630 present, IBA+IEA) — already captured. The selective-autophagy-**receptor MF** (cargo adaptor) is captured in the review as GO:0030674 protein-macromolecule adaptor activity (ACCEPT); the more specific GO:0160247 autophagy cargo adaptor activity (verified real, child of GO:0030674) would be a precise upgrade.
- **Mapping strategy:** No node change needed. Xenophagy projection is correct and appropriately narrower than GOA's bare autophagy. Pattern alert (selective-autophagy receptor → elevate cargo-adaptor MF): review uses GO:0030674; GO:0160247 is the more specific cargo-adaptor term and matches the receptor role.
- **Evidence alignment:** Strong overlap. PN cites the selective-autophagy/LIR review and the TRIM5-virophagy paper (= PMID:25127057, in review HIGH) plus 33791238/19489725/21490953 (TRIM/E3 reviews). Review's core refs (PMID:21512573, 25127057, 22291694, 18248090) cover both arms.
- **Verdict:** Consistent; xenophagy ADD warranted; RING ligase already captured. **Recommended edits:** [YAML] add GO:0098792 xenophagy (involved_in, supported by PMID:25127057) as a more-specific child of the existing autophagy annotation. [YAML] optionally upgrade the GO:0030674 adaptor MF to the more specific GO:0160247 autophagy cargo adaptor activity for the capsid-receptor role.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-14
- review_yaml: genes/human/TRIM5/TRIM5-ai-review.yaml
- PN workbook rows: 3

## PN row 1: Autophagy-Lysosome Pathway | Autophagy substrate selection | Selective autophagy receptor | Xenophagy
- UniProt: Q9C035
- In branches: ALP, UPS
- Notes: Adapter for selective autophagy. Binds to ATG8 and ubiquitinated or degron-contaning substrates. Active in virophagy
- PN references (titles):
    - Selective Autophagy: ATG8 Family Proteins, LIR Motifs and Cargo Receptors - ScienceDirect
    - Full article: TRIM proteins regulate autophagy: TRIM5 is a selective autophagy receptor mediating HIV-1 restriction (tandfonline.com)
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Xenophagy
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0098792 xenophagy]
        rationale: This PN category captures receptors for selective autophagy of pathogens or pathogen-derived material. The receptor class is narrower than the GO xenophagy process, so this is a propagation mapping.
    - [group] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagy substrate selection
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad substrate-selection container. GO has useful targets for specific receptor, cargo-adaptor, and selective-autophagy leaves, but this class mixes marking, recognition, receptor regulation, and unknown roles and should not propagate as one term.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 2: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | RING | TRIM / class IV | SPRY
- UniProt: Q9C035
- In branches: ALP, UPS
- Signature domains: IPR001841
- Auxiliary domains: IPR003877, IPR001870
- PN references (titles):
    - 33791238 / rev
    - 19489725 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING|TRIM / class IV|SPRY
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower E3-ligase architecture, component, or domain subdivision already covered by the curated parent E3 mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING|TRIM / class IV
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

## PN row 3: Ubiquitin Proteasome System | Ubiquitin and UBL binding | E3 ligase | RING / TRIM class IV | SIM
- UniProt: Q9C035
- In branches: ALP, UPS
- Signature domains: PMID: 21490953
- Auxiliary domains: IPR001841
- PN references (titles):
    - 21490953
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|Ubiquitin and UBL binding|E3 ligase|RING / TRIM class IV|SIM
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower enzyme-family, domain, or architecture subdivision already covered by a curated parent enzyme mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|Ubiquitin and UBL binding|E3 ligase|RING / TRIM class IV
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower enzyme-family, domain, or architecture subdivision already covered by a curated parent enzyme mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|Ubiquitin and UBL binding|E3 ligase
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This PN group captures ubiquitin/UBL-binding factors that are E3 ligases. The shared molecular-function target is ubiquitin protein ligase activity.
    - [class] Ubiquitin Proteasome System|Ubiquitin and UBL binding
        status=context_only scope=too_broad_to_propagate GO=[GO:0140036 ubiquitin-modified protein reader activity]
        rationale: This class records ubiquitin/UBL-reader context, but the subtree mixes ubiquitin, SUMO, UBL-domain, domain-architecture, catalytic, signaling, trafficking, and nucleic-acid process buckets. It is useful context, not a safe direct propagation.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (3)
- GO:0098792 xenophagy | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Xenophagy
- GO:0061630 ubiquitin protein ligase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING
- GO:0061630 ubiquitin protein ligase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|Ubiquitin and UBL binding|E3 ligase

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
