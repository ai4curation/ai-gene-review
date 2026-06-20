# SIAH1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q8IUQ4
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-14
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/SIAH1/SIAH1-ai-review.yaml](SIAH1-ai-review.yaml)
- AIGR review HTML: missing - genes/human/SIAH1/SIAH1-ai-review.html
- Gene notes: present - [genes/human/SIAH1/SIAH1-notes.md](SIAH1-notes.md)
- GOA TSV: present - [genes/human/SIAH1/SIAH1-goa.tsv](SIAH1-goa.tsv)
- UniProt record: present - [genes/human/SIAH1/SIAH1-uniprot.txt](SIAH1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/SIAH1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/SIAH1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/SIAH1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/SIAH1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: SIAH1 (seven in absentia homolog 1) is a RING-type E3 ubiquitin-protein ligase (EC 2.3.2.27) that catalyzes ubiquitination and subsequent proteasomal degradation of a broad set of substrates. It is built from an N-terminal RING-type zinc finger that recruits a ubiquitin-charged E2 conjugating enzyme (e.g. UBE2D1, UBE2E2, UBE2I, UBE2L6) and a C-terminal SIAH-type substrate-binding domain containing additional zinc fingers that recognizes substrate degrons, typically a Pro-x-Ala-x-Val-x-Pro (PxAxVxP) motif. SIAH1 functions as a homodimer (and can heterodimerize with the closely related SIAH2), and can act either by binding substrates directly or as the RING subunit of larger multiprotein E3 complexes. Its best-characterized substrates and pathways include: DCC (the netrin receptor deleted in colorectal cancer), establishing a role in nervous-system development and axon guidance; beta-catenin (CTNNB1), which SIAH1 degrades via a p53-inducible, GSK3beta/beta-TrCP-independent pathway acting with APC, the adaptor SIP/CACYBP, SKP1 and Ebi/TBL1X as part of a beta-catenin destruction complex; AXIN1, whose Wnt-induced degradation by SIAH1 provides a feed-forward boost to canonical Wnt/beta-catenin signaling; alpha-synuclein (SNCA, monoubiquitylation) and synphilin-1 (SNCAIP), linking SIAH1 to Lewy-body/inclusion formation in Parkinson disease; XIAP (via the ARTS adaptor) and other apoptotic regulators, promoting intrinsic apoptosis; the kinase HIPK2 (constitutive, DAZAP2-assisted degradation in the DNA-damage/p53 response); and the prolyl hydroxylases EGLN2/EGLN3, coupling SIAH1 to the hypoxic/unfolded-protein response. SIAH1 is predominantly cytoplasmic with a partial nuclear pool, is itself p53-inducible, and contributes to apoptosis, tumor suppression, transcriptional regulation, and Wnt signaling.
- Existing/core annotation action counts: ACCEPT: 34; KEEP_AS_NON_CORE: 39; MARK_AS_OVER_ANNOTATED: 2

## PN Consistency Summary

- **Consistency:** Review YAML, notes and PN UPS annotation are fully aligned on the catalytic RING E3 identity (GO:0061630 core; EC 2.3.2.27; zinc fingers; homodimer). The ALP/mitophagy PN row is the one divergence: the review contains NO autophagy/mitophagy annotation, GOA has none, and SIAH1-uniprot.txt mentions SNCA/SNCAIP ubiquitination but not mitophagy or PINK1. The deep-research notes likewise do not mention the PINK1-SIAH1-synphilin mitophagy pathway.
- **PN story / NEW pressure:** PN asserts a PRKN-independent PINK1-SIAH1-SNCAIP mitophagy role absent from existing GO. The supporting paper (Szargel et al. 2016 HMG, "PINK1, synphilin-1 and SIAH-1 complex constitutes a novel mitophagy pathway") is real and not in the publications cache or the review. GO:0000423 mitophagy is a verified real term (OLS). This is a defensible ADD candidate, but it rests on a single primary paper not yet read in full and not in cache — propose as a NEW annotation pending full-text verification, not a slam-dunk.
- **Evidence alignment:** Strong overlap on the UPS side conceptually but NOT by PMID — the PN UPS row cites only "19489725 / rev" (a review), while the review's ligase support is PMID:9334332/19224863/28546513/33591310. The PN ALP row cites the Szargel HMG mitophagy paper + a tandfonline PRKN-independent-mitophagy review, neither of which appears in the review references. Divergence is total on the mitophagy evidence.
- **Verdict:** Catalytic E3 mapping consistent and correct; mitophagy is a genuine NEW-GO opportunity (GO:0000423, verified) currently missing from review and GOA. The PMID:11863358 zinc-binding citation is correctly flagged WRONG_IDENTIFIER in reference_review (APOBEC RNA-editing paper, zero SIAH1 mention); SIAH1 zinc binding itself is correct (PMID:16085652), so ACCEPT of the term is sound — no change to that call.

## Full Consistency Review

- **UniProt:** Q8IUQ4 · **batch:** proteostasis-batch-2026-06-14 · **review status:** COMPLETE (dual UPS + ALP placement)
- **PN placement:** UPS row `E3 ubiquitin and UBL ligases|RING|SIAH / SINA|SIA TRAF-like` and ALP row `Autophagy substrate selection|Marking substrates for selective autophagy|Mitophagy|PINK/PRKN pathway` ; **PN-node mapping:** UPS group `mapped`/ok_for_propagation = GO:0061630 ubiquitin protein ligase activity (already_in_goa_exact); ALP type `mapped`/ok_for_propagation = GO:0000423 mitophagy (flagged new_to_goa).
- **Consistency:** Review YAML, notes and PN UPS annotation are fully aligned on the catalytic RING E3 identity (GO:0061630 core; EC 2.3.2.27; zinc fingers; homodimer). The ALP/mitophagy PN row is the one divergence: the review contains NO autophagy/mitophagy annotation, GOA has none, and SIAH1-uniprot.txt mentions SNCA/SNCAIP ubiquitination but not mitophagy or PINK1. The deep-research notes likewise do not mention the PINK1-SIAH1-synphilin mitophagy pathway.
- **PN story / NEW pressure:** PN asserts a PRKN-independent PINK1-SIAH1-SNCAIP mitophagy role absent from existing GO. The supporting paper (Szargel et al. 2016 HMG, "PINK1, synphilin-1 and SIAH-1 complex constitutes a novel mitophagy pathway") is real and not in the publications cache or the review. GO:0000423 mitophagy is a verified real term (OLS). This is a defensible ADD candidate, but it rests on a single primary paper not yet read in full and not in cache — propose as a NEW annotation pending full-text verification, not a slam-dunk.
- **Mapping strategy:** This gene does not require changing either node's status. The UPS group mapping to GO:0061630 is exact and correct (catalytic ligase kept as core, per the SIAH1 KEY PATTERN). The ALP type→GO:0000423 propagation is reasonable IF the Szargel evidence is verified; scope ok_for_propagation is acceptable. The zinc ion binding IDA was ACCEPTed and the wrong citation already flagged correctly (see below) — no re-mapping needed.
- **Evidence alignment:** Strong overlap on the UPS side conceptually but NOT by PMID — the PN UPS row cites only "19489725 / rev" (a review), while the review's ligase support is PMID:9334332/19224863/28546513/33591310. The PN ALP row cites the Szargel HMG mitophagy paper + a tandfonline PRKN-independent-mitophagy review, neither of which appears in the review references. Divergence is total on the mitophagy evidence.
- **Verdict:** Catalytic E3 mapping consistent and correct; mitophagy is a genuine NEW-GO opportunity (GO:0000423, verified) currently missing from review and GOA. The PMID:11863358 zinc-binding citation is correctly flagged WRONG_IDENTIFIER in reference_review (APOBEC RNA-editing paper, zero SIAH1 mention); SIAH1 zinc binding itself is correct (PMID:16085652), so ACCEPT of the term is sound — no change to that call.
  **Recommended edits:** [YAML] Add a mitophagy annotation `GO:0000423` (NEW, qualifier involved_in) for the PINK1-SIAH1-SNCAIP PRKN-independent pathway, supported_by the Szargel et al. 2016 HMG paper — first fetch/verify the PMID (Szargel HMG 2016; cache currently lacks it) and add it to `references`; mark UNDECIDED→NEW only after full-text confirmation. [REF] Keep the existing PMID:11863358 WRONG_IDENTIFIER flag (no change); optionally re-anchor the zinc IDA's primary support note to PMID:16085652.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-14
- review_yaml: genes/human/SIAH1/SIAH1-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Autophagy substrate selection | Marking substrates for selective autophagy | Mitophagy | PINK/PRKN pathway
- UniProt: Q8IUQ4
- In branches: ALP, UPS
- Notes: Part of a PINK1-SIAH1-SNCAIP complex that induces mitophagy in a PRKN-independent manner.
- PN references (titles):
    - Full article: Regulation of PRKN-independent mitophagy (tandfonline.com)
    - PINK1, synphilin-1 and SIAH-1 complex constitutes a novel mitophagy pathway | Human Molecular Genetics | Oxford Academic (oup.com)
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy|Mitophagy|PINK/PRKN pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a contextual PN role. The label is useful for curator triage, but by itself does not support a universal GO assertion for all member genes beyond curated ancestor or child mappings.
    - [type] Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy|Mitophagy
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0000423 mitophagy]
        rationale: The PN marking category for mitophagy captures upstream cargo-marking steps that commit mitochondrial substrates to the mitophagy pathway. That supports propagation to mitophagy.
    - [group] Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagy substrate selection
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad substrate-selection container. GO has useful targets for specific receptor, cargo-adaptor, and selective-autophagy leaves, but this class mixes marking, recognition, receptor regulation, and unknown roles and should not propagate as one term.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 2: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | RING | SIAH / SINA | SIA TRAF-like
- UniProt: Q8IUQ4
- In branches: ALP, UPS
- Signature domains: IPR001841
- Auxiliary domains: IPR013010, IPR018121
- PN references (titles):
    - 19489725 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING|SIAH / SINA|SIA TRAF-like
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower E3-ligase architecture, component, or domain subdivision already covered by the curated parent E3 mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING|SIAH / SINA
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
- GO:0000423 mitophagy | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy|Mitophagy
- GO:0061630 ubiquitin protein ligase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
