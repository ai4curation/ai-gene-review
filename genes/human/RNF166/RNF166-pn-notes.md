# RNF166 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q96A37
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-14
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/RNF166/RNF166-ai-review.yaml](RNF166-ai-review.yaml)
- AIGR review HTML: missing - genes/human/RNF166/RNF166-ai-review.html
- Gene notes: present - [genes/human/RNF166/RNF166-notes.md](RNF166-notes.md)
- GOA TSV: present - [genes/human/RNF166/RNF166-goa.tsv](RNF166-goa.tsv)
- UniProt record: present - [genes/human/RNF166/RNF166-uniprot.txt](RNF166-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/RNF166.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/RNF166.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/RNF166.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/RNF166.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: RNF166 (RING finger protein 166) is a small (237 aa) RING-type E3 ubiquitin-protein ligase (EC 2.3.2.27) of the C3HC4 RING subfamily that also includes RNF114, RNF125 and RNF138. It is built from an N-terminal RING-type zinc finger (residues ~33-73; catalytic Cys33/Cys36) that recruits a ubiquitin-charged E2 conjugating enzyme (UBE2D2/UBE2D family), a central C2HC RNF-type zinc finger (~98-117) that mediates substrate/target binding, and a C-terminal ubiquitin-interacting motif (UIM). RNF166 catalyzes ubiquitin transfer to several substrates using different, largely non-degradative chain linkages. In antibacterial selective autophagy (xenophagy) it directly catalyzes Lys29- and Lys33-linked polyubiquitination of the autophagy adaptor SQSTM1/p62 (at K91 and K189), and is required for the early recruitment of ubiquitin and the autophagy adaptors p62 and NDP52 (and downstream LC3) to cytosol-invading bacteria such as Listeria monocytogenes and Shigella flexneri, thereby restricting their intracellular replication. In innate antiviral immunity RNF166 enhances RNA virus-induced Lys63-linked ubiquitination of the signaling adaptors TRAF3 and TRAF6, acting downstream of the mitochondrial adaptor MAVS/VISA and upstream of TBK1 to potentiate type I interferon (IFN-beta) production. RNF166 is a cytoplasmic protein that forms cytosolic puncta and relocalizes to intracellular bacteria. Its catalytic RING activity (lost in the C33A/C36A ligase-dead mutant) is required for both the xenophagy and antiviral functions.
- Existing/core annotation action counts: ACCEPT: 6; KEEP_AS_NON_CORE: 5; MARK_AS_OVER_ANNOTATED: 1

## PN Consistency Summary

- **Consistency:** Excellent. Deep research, review and PN all agree RNF166 is a genuine catalytic RING E3 (ligase-dead C33A/C36A abolishes activity) that drives xenophagy of cytosolic bacteria by K29/K33-ubiquitinating p62 and recruiting p62/NDP52 (PMID:27880896), and potentiates antiviral type-I-IFN via K63-Ub of TRAF3/TRAF6 (PMID:26456228). PN row1 leaf ("Catalyzes K33-linked ubiquitination of p62") matches the review exactly. Row3's UIM note matches the UniProt C-terminal UIM. No contradictions.
- **PN story / NEW pressure:** Row1 projects GO:0098792 xenophagy (verified real; ABSENT from GOA). This is a strongly defensible **ADD** — and the review itself proposes GO:0098792 as a NEW term (plus GO:0042742 defense response to bacterium and GO:0032481 positive regulation of type I IFN production), fully concordant with the dossier goa_status=new_to_goa. Rows2/3 GO:0061630 = already_in_goa_exact (IBA/EXP/IEA present) — keep catalytic ligase MF as core (matches KEY PATTERN). So PN and review agree: ADD xenophagy; ligase MF already captured.
- **Evidence alignment:** Strong. PN row1 cites "RNF166 Determines Recruitment of Adaptor Proteins during Antibacterial Autophagy" (= PMID:27880896, the review's HIGH/VERIFIED anchor) plus a p62-UBA-Ub review (tandfonline). Row3 cites PMID:17990982 (not in the review). Review additionally anchors the antiviral arm on PMID:26456228 (not in PN). Minor divergence on antiviral evidence only.
- **Verdict:** Fully consistent; xenophagy ADD is justified and the review ALREADY proposes it; catalytic ligase MF already core/in-GOA.

## Full Consistency Review

- **UniProt:** Q96A37 · **batch:** proteostasis-batch-2026-06-14 · **review status:** COMPLETE (thorough; catalytic C3HC4 RING E3; p62 K29/K33 xenophagy + TRAF3/6 K63 antiviral; 3 PN rows)
- **PN placement:** row1 `ALP|...|Marking substrates for selective autophagy|Xenophagy|Catalyzes K33-linked ubiquitination of p62`; row2 `UPS|E3 ligases|RING|TRAC-1`; row3 `UPS|Ubiquitin and UBL binding|E3 ligase|RING / TRAC-1|UIM`. **PN-node mapping:** row1 Xenophagy type→mapped GO:0098792 xenophagy; rows2/3 E3-group→mapped GO:0061630 ubiquitin protein ligase activity (classes context_only/too_broad; subtypes no_mapping).
- **Consistency:** Excellent. Deep research, review and PN all agree RNF166 is a genuine catalytic RING E3 (ligase-dead C33A/C36A abolishes activity) that drives xenophagy of cytosolic bacteria by K29/K33-ubiquitinating p62 and recruiting p62/NDP52 (PMID:27880896), and potentiates antiviral type-I-IFN via K63-Ub of TRAF3/TRAF6 (PMID:26456228). PN row1 leaf ("Catalyzes K33-linked ubiquitination of p62") matches the review exactly. Row3's UIM note matches the UniProt C-terminal UIM. No contradictions.
- **PN story / NEW pressure:** Row1 projects GO:0098792 xenophagy (verified real; ABSENT from GOA). This is a strongly defensible **ADD** — and the review itself proposes GO:0098792 as a NEW term (plus GO:0042742 defense response to bacterium and GO:0032481 positive regulation of type I IFN production), fully concordant with the dossier goa_status=new_to_goa. Rows2/3 GO:0061630 = already_in_goa_exact (IBA/EXP/IEA present) — keep catalytic ligase MF as core (matches KEY PATTERN). So PN and review agree: ADD xenophagy; ligase MF already captured.
- **Mapping strategy:** Correct. Catalytic RING→GO:0061630 (exact, in GOA); Xenophagy type→GO:0098792 (narrower-but-inside). Subtype p62-K33 leaf and the TRAC-1/UIM architecture subdivisions appropriately no_mapping. The two separate RING/E3 rows both projecting GO:0061630 are redundant but harmless (one MF). No over-reach.
- **Evidence alignment:** Strong. PN row1 cites "RNF166 Determines Recruitment of Adaptor Proteins during Antibacterial Autophagy" (= PMID:27880896, the review's HIGH/VERIFIED anchor) plus a p62-UBA-Ub review (tandfonline). Row3 cites PMID:17990982 (not in the review). Review additionally anchors the antiviral arm on PMID:26456228 (not in PN). Minor divergence on antiviral evidence only.
- **Verdict:** Fully consistent; xenophagy ADD is justified and the review ALREADY proposes it; catalytic ligase MF already core/in-GOA.
- **Recommended edits:** [YAML] none required for the PN story — the review already proposes GO:0098792 xenophagy (NEW). Optionally [REF] check PN row3's PMID:17990982 (UIM characterization), absent from the review, if a UIM ubiquitin-reader MF is desired.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-14
- review_yaml: genes/human/RNF166/RNF166-ai-review.yaml
- PN workbook rows: 3

## PN row 1: Autophagy-Lysosome Pathway | Autophagy substrate selection | Marking substrates for selective autophagy | Xenophagy | Catalyzes K33-linked ubiquitination of p62
- UniProt: Q96A37
- In branches: ALP, UPS
- Notes: E3 ubuquitin ligases that ubiquitinate bacteria to enable the recruitment of bacteria cargo by SQSTM1 and CALCOCO2 to ubiquitinated bacteria.
- PN references (titles):
    - Regulation of SQSTM1/p62 via UBA domain ubiquitination and its role in disease (tandfonline.com)
    - RNF166 Determines Recruitment of Adaptor Proteins during Antibacterial Autophagy
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy|Xenophagy|Catalyzes K33-linked ubiquitination of p62
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a contextual PN role. The label is useful for curator triage, but by itself does not support a universal GO assertion for all member genes beyond curated ancestor or child mappings.
    - [type] Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy|Xenophagy
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0098792 xenophagy]
        rationale: This PN type groups xenophagy-specific marking steps that label cargo for selective autophagic clearance. That is narrower than, but clearly inside, the xenophagy process.
    - [group] Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagy substrate selection
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad substrate-selection container. GO has useful targets for specific receptor, cargo-adaptor, and selective-autophagy leaves, but this class mixes marking, recognition, receptor regulation, and unknown roles and should not propagate as one term.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 2: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | RING | TRAC-1
- UniProt: Q96A37
- In branches: ALP, UPS
- Signature domains: IPR001841
- Auxiliary domains: IPR008598, IPR034734
- PN references (titles):
    - 19489725 / rev
- PN-node mapping records (path + ancestors):
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING|TRAC-1
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

## PN row 3: Ubiquitin Proteasome System | Ubiquitin and UBL binding | E3 ligase | RING / TRAC-1 | UIM
- UniProt: Q96A37
- In branches: ALP, UPS
- Signature domains: PMID: 17990982
- Auxiliary domains: IPR001841
- PN references (titles):
    - 17990982
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|Ubiquitin and UBL binding|E3 ligase|RING / TRAC-1|UIM
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower enzyme-family, domain, or architecture subdivision already covered by a curated parent enzyme mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|Ubiquitin and UBL binding|E3 ligase|RING / TRAC-1
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
- GO:0098792 xenophagy | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy|Xenophagy
- GO:0061630 ubiquitin protein ligase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING
- GO:0061630 ubiquitin protein ligase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|Ubiquitin and UBL binding|E3 ligase

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
