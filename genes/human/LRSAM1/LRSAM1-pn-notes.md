# LRSAM1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q6UWE0
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-14
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/LRSAM1/LRSAM1-ai-review.yaml](LRSAM1-ai-review.yaml)
- AIGR review HTML: missing - genes/human/LRSAM1/LRSAM1-ai-review.html
- Gene notes: present - [genes/human/LRSAM1/LRSAM1-notes.md](LRSAM1-notes.md)
- GOA TSV: present - [genes/human/LRSAM1/LRSAM1-goa.tsv](LRSAM1-goa.tsv)
- UniProt record: present - [genes/human/LRSAM1/LRSAM1-uniprot.txt](LRSAM1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/LRSAM1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/LRSAM1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/LRSAM1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/LRSAM1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: LRSAM1 (leucine-rich repeat and sterile alpha motif-containing protein 1; also called Tal, the Tsg101-associated ligase) is a cytoplasmic RING-type E3 ubiquitin-protein ligase (EC 2.3.2.27). Its domain architecture comprises N-terminal leucine-rich repeats (LRRs) that mediate target recognition, central coiled-coil and SAM (sterile alpha motif) domains, and a C-terminal RING-type zinc finger that provides catalytic E3 ligase activity. LRSAM1 has two principal, experimentally established functions. First, it is a bacterial recognition protein and the E3 ligase responsible for antibacterial autophagy (xenophagy): it localizes to cytosolic intracellular bacterial pathogens (such as Salmonella Typhimurium) via its LRRs and generates the polyubiquitin signal around the bacteria via its RING domain, recruiting autophagy adaptors and machinery to target the bacteria for lysosomal degradation; this activity is required for bacteria-associated ubiquitination but is dispensable for ubiquitination of protein aggregates. Second, as Tal it monoubiquitinates the ESCRT-I component TSG101 at multiple sites, inactivating TSG101's ability to sort endocytic (EGF receptor) and exocytic (HIV-1 viral protein) cargos, thereby regulating receptor endocytosis and retroviral budding. LRSAM1 displays a punctate cytoplasmic distribution and a submembranal ring, and relocalizes to intracellular bacteria during infection. Its abundance is controlled by PHF23, which promotes LRSAM1 ubiquitination and degradation to negatively regulate autophagy. Mutations in LRSAM1 cause Charcot-Marie-Tooth disease type 2P (CMT2P), an axonal peripheral neuropathy.
- Existing/core annotation action counts: ACCEPT: 13; KEEP_AS_NON_CORE: 22

## PN Consistency Summary

- **Consistency:** Excellent. Deep research, review and PN all agree LRSAM1 is a genuine catalytic RING E3 (EC 2.3.2.27) that (a) recognizes cytosolic bacteria via LRRs and generates the bacteria-associated polyUb signal via its RING to drive xenophagy (PMID:23245322), and (b) as Tal monoubiquitinates TSG101 (ESCRT) controlling endocytosis/retroviral budding. PN row2 ("genuine catalytic RING E3") matches the review's ACCEPT of GO:0061630/GO:0004842 as CORE. No contradictions.
- **PN story / NEW pressure:** Row1 projects GO:0098792 xenophagy (verified real; ABSENT from GOA as the base process). PN flags it goa_status=supported_by_goa_regulation — confirmed: GOA carries GO:1904417 positive regulation of xenophagy (IMP, PMID:23245322) but NOT the parent GO:0098792. The review accepts GO:1904417 as core and never adds the base xenophagy term. So GO:0098792 is a defensible **ADD** (the regulation term already in GOA strongly supports it). Row2 GO:0061630 is correctly already_in_goa_exact (EXP/IDA/IEA all present) — keep the catalytic ligase MF as core (matches the KEY PATTERN: LRSAM1 generates the autophagy ubiquitin signal).
- **Evidence alignment:** Strong. PN row1 ref (LRR+RING LRSAM1 E3 xenophagy of Salmonella = PMID:23245322) is the review's HIGH/VERIFIED anchor. PN row2 "19489725 / rev" is a family-review pointer not in the review.
- **Verdict:** Fully consistent and mutually reinforcing; catalytic ligase MF is core (already in GOA); base xenophagy BP is a justified ADD the review omits (regulation child already curated).

## Full Consistency Review

- **UniProt:** Q6UWE0 (Tal) · **batch:** proteostasis-batch-2026-06-14 · **review status:** COMPLETE (thorough; catalytic RING E3; xenophagy + TSG101/ESCRT; CMT2P; 2 PN rows)
- **PN placement:** row1 `ALP|...|Marking substrates for selective autophagy|Xenophagy|Intracellular pathogen ubiquitination`; row2 `UPS|E3 ubiquitin and UBL ligases|RING|other|LRR`. **PN-node mapping:** row1 Xenophagy type→mapped GO:0098792 xenophagy (subtype contextual no_mapping); row2 RING group→mapped GO:0061630 ubiquitin protein ligase activity (class context_only/too_broad).
- **Consistency:** Excellent. Deep research, review and PN all agree LRSAM1 is a genuine catalytic RING E3 (EC 2.3.2.27) that (a) recognizes cytosolic bacteria via LRRs and generates the bacteria-associated polyUb signal via its RING to drive xenophagy (PMID:23245322), and (b) as Tal monoubiquitinates TSG101 (ESCRT) controlling endocytosis/retroviral budding. PN row2 ("genuine catalytic RING E3") matches the review's ACCEPT of GO:0061630/GO:0004842 as CORE. No contradictions.
- **PN story / NEW pressure:** Row1 projects GO:0098792 xenophagy (verified real; ABSENT from GOA as the base process). PN flags it goa_status=supported_by_goa_regulation — confirmed: GOA carries GO:1904417 positive regulation of xenophagy (IMP, PMID:23245322) but NOT the parent GO:0098792. The review accepts GO:1904417 as core and never adds the base xenophagy term. So GO:0098792 is a defensible **ADD** (the regulation term already in GOA strongly supports it). Row2 GO:0061630 is correctly already_in_goa_exact (EXP/IDA/IEA all present) — keep the catalytic ligase MF as core (matches the KEY PATTERN: LRSAM1 generates the autophagy ubiquitin signal).
- **Mapping strategy:** Correct. Catalytic RING→GO:0061630 (exact, in GOA); Xenophagy type→GO:0098792 (narrower-but-inside the process). The contextual "Intracellular pathogen ubiquitination" subtype is appropriately no_mapping. The xenophagy process projection is consistent with — not broader than — the review's accepted GO:1904417; no TOMM20-style over-reach.
- **Evidence alignment:** Strong. PN row1 ref (LRR+RING LRSAM1 E3 xenophagy of Salmonella = PMID:23245322) is the review's HIGH/VERIFIED anchor. PN row2 "19489725 / rev" is a family-review pointer not in the review.
- **Verdict:** Fully consistent and mutually reinforcing; catalytic ligase MF is core (already in GOA); base xenophagy BP is a justified ADD the review omits (regulation child already curated).
- **Recommended edits:** [YAML] add GO:0098792 xenophagy (BP, involved_in) — the base process is absent though GO:1904417 (its positive-regulation child) is already accepted as core; cite PMID:23245322.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-14
- review_yaml: genes/human/LRSAM1/LRSAM1-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Autophagy substrate selection | Marking substrates for selective autophagy | Xenophagy | Intracellular pathogen ubiquitination
- UniProt: Q6UWE0
- In branches: ALP, UPS
- Notes: E3 ligase involved in ubiquitin-dependent autophagy of intracellular pathogens
- PN references (titles):
    - The LRR and RING Domain Protein LRSAM1 Is an E3 Ligase Crucial for Ubiquitin-Dependent Autophagy of Intracellular Salmonella Typhimurium - ScienceDirect
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy|Xenophagy|Intracellular pathogen ubiquitination
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

## PN row 2: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | RING | other | LRR
- UniProt: Q6UWE0
- In branches: ALP, UPS
- Signature domains: IPR001841
- Auxiliary domains: IPR001611
- PN references (titles):
    - 19489725 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING|other|LRR
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower E3-ligase architecture, component, or domain subdivision already covered by the curated parent E3 mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING|other
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

## Projected GO annotations (2)
- GO:0098792 xenophagy | scope=ok_for_propagation_to_go | goa_status=supported_by_goa_regulation | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy|Xenophagy
- GO:0061630 ubiquitin protein ligase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
