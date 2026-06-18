# USP25 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9UHP3
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07c
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/USP25/USP25-ai-review.yaml](USP25-ai-review.yaml)
- AIGR review HTML: present - [genes/human/USP25/USP25-ai-review.html](USP25-ai-review.html)
- Gene notes: present - [genes/human/USP25/USP25-notes.md](USP25-notes.md)
- GOA TSV: present - [genes/human/USP25/USP25-goa.tsv](USP25-goa.tsv)
- UniProt record: present - [genes/human/USP25/USP25-uniprot.txt](USP25-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/USP25.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/USP25.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/USP25.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/USP25.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: USP25 (ubiquitin carboxyl-terminal hydrolase 25; historically called "USP on chromosome 21" / USP21) is a cytoplasmic cysteine (papain-like, peptidase C19 family) deubiquitinating enzyme. It has an N-terminal UBA-like domain and tandem ubiquitin-interacting motifs (UIM) that recognize ubiquitin, a catalytic USP domain (active-site Cys-178), and a C-terminal region that mediates oligomerization, with an inhibited homotetramer and an active homodimer state controlling catalytic output. USP25 hydrolyzes ubiquitin from substrates and can cleave both K48- and K63-linked polyubiquitin chains, thereby protecting specific substrates from proteasomal degradation and modulating signaling. Characterized substrates and pathways include stabilization of the tankyrases TNKS1/TNKS2 to modulate Wnt/beta-catenin signaling, deubiquitination and stabilization of KEAP1 within the KEAP1-NRF2 oxidative-stress axis, removal of K63-linked ubiquitin from TRAF5/TRAF6 to restrain interleukin-17 signaling and inflammation, stabilization of TRAF3 and ERLIN1/2 in innate antiviral responses, and rescue of ERAD substrates by counteracting the HRD1 ubiquitin ligase. Its activity is regulated by sumoylation at Lys-99 (which impairs ubiquitin binding), by SMURF1-mediated K48 ubiquitination targeting it for degradation, by SYK phosphorylation, and by its oligomeric state. A muscle-specific isoform (USP25m) is induced during myocyte differentiation and interacts with sarcomeric proteins (ACTA1, FLNC, MYBPC1). Heterozygous USP25 variants cause idiopathic generalized epilepsy (EIG19).
- Existing/core annotation action counts: ACCEPT: 23; KEEP_AS_NON_CORE: 22; MARK_AS_OVER_ANNOTATED: 5; MODIFY: 4; REMOVE: 2

## PN Consistency Summary

- **Consistency:** Consistent BUT identity is the salient issue. The task framing ("USP25 was the synonym-resolved symbol for USP21") conflates two distinct genes. The folder/review (Q9UHP3) is genuinely USP25 (HGNC:12624), historically aliased "USP21"/"USP on chr 21" (PMID:10644437) — a separate protein from true USP21 (Q9UK80). The notes file documents this collision explicitly. PN dossier (Q9UHP3), review, and notes all agree on the USP25 identity; both PN rows are purely UPS (no TR/RQC row), matching the review's substrate biology (tankyrases/Wnt, KEAP1-NRF2, IL-17/TRAF, ERAD-HRD1). USP25 is NOT an RQC DUB — only true USP21 is.
- **PN story / NEW pressure:** PN asserts only DUB activity (GO:0101005) and ubiquitin/UBL-reader context — all already in GOA/review (GO:0004843, GO:0043130 ubiquitin binding, GO:0032183 SUMO binding). No new-to-GOA projection. Conclude: already captured; no NEW term and no RQC pressure (correctly, since USP25 has no ribosome role).
- **Evidence alignment:** PN row 1 cites "19734957/rev"; row 2 cites PMID:18538659 (paralog-specific sumoylation) — the latter IS in the review (GO:0032183 SUMO binding, GO:0070536/GO:0071108 K63/K48 deubiquitination), good overlap. Review is far richer (KEAP1, IL-17, ERAD, epilepsy PMIDs) than the two PN rows.
- **Verdict:** Consistent; identity confirmed as USP25 (distinct from USP21), no RQC role. PN claims already captured; no NEW term needed.

## Full Consistency Review

- **UniProt:** Q9UHP3 · **batch:** proteostasis-batch-2026-06-07c · **review status:** COMPLETE
- **PN placement:** UPS `DUBs and UBL demodifiers|USP|other|UBA, UIM` and UPS `Ubiquitin and UBL binding|DUB|USP / with UBD|UIM, UBA-like, SIM` ; **PN-node mapping:** DUB-family group→GO:0101005 deubiquitinase activity (mapped, already_in_goa_exact); UBL-binding group→GO:0101005 (context_only, too_broad); UBL-binding class→GO:0140036 ubiquitin-modified protein reader activity (context_only); type/subtype/branch = no_mapping.
- **Consistency:** Consistent BUT identity is the salient issue. The task framing ("USP25 was the synonym-resolved symbol for USP21") conflates two distinct genes. The folder/review (Q9UHP3) is genuinely USP25 (HGNC:12624), historically aliased "USP21"/"USP on chr 21" (PMID:10644437) — a separate protein from true USP21 (Q9UK80). The notes file documents this collision explicitly. PN dossier (Q9UHP3), review, and notes all agree on the USP25 identity; both PN rows are purely UPS (no TR/RQC row), matching the review's substrate biology (tankyrases/Wnt, KEAP1-NRF2, IL-17/TRAF, ERAD-HRD1). USP25 is NOT an RQC DUB — only true USP21 is.
- **PN story / NEW pressure:** PN asserts only DUB activity (GO:0101005) and ubiquitin/UBL-reader context — all already in GOA/review (GO:0004843, GO:0043130 ubiquitin binding, GO:0032183 SUMO binding). No new-to-GOA projection. Conclude: already captured; no NEW term and no RQC pressure (correctly, since USP25 has no ribosome role).
- **Mapping strategy:** USP25 does not change either node. DUB-family group→GO:0101005 is already_in_goa_exact (GOA has GO:0101005 IMP/IDA rows). UBL-binding class→GO:0140036 reader activity is correctly held as context_only/too_broad (USP25's UBA/UIM/SIM read ubiquitin and SUMO, but the class mixes modifiers). Scope/status all appropriate.
- **Evidence alignment:** PN row 1 cites "19734957/rev"; row 2 cites PMID:18538659 (paralog-specific sumoylation) — the latter IS in the review (GO:0032183 SUMO binding, GO:0070536/GO:0071108 K63/K48 deubiquitination), good overlap. Review is far richer (KEAP1, IL-17, ERAD, epilepsy PMIDs) than the two PN rows.
- **Verdict:** Consistent; identity confirmed as USP25 (distinct from USP21), no RQC role. PN claims already captured; no NEW term needed.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/USP25/USP25-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Ubiquitin Proteasome System | DUBs and UBL demodifiers | USP | other | UBA, UIM
- UniProt: Q9UHP3
- In branches: UPS
- Signature domains: IPR028889
- Auxiliary domains: IPR009060, IPR003903
- PN references (titles):
    - 19734957 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|DUBs and UBL demodifiers|USP|other|UBA, UIM
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower active DUB family/domain subdivision already covered by the curated parent DUB-family mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|DUBs and UBL demodifiers|USP|other
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower active DUB family/domain subdivision already covered by the curated parent DUB-family mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|DUBs and UBL demodifiers|USP
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0101005 deubiquitinase activity]
        rationale: This PN group is an active deubiquitinase family bucket. The shared molecular-function assertion is deubiquitinase activity.
    - [class] Ubiquitin Proteasome System|DUBs and UBL demodifiers
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a UPS taxonomy container. Its descendants mix catalytic roles, complex membership, binding domains, regulators, adaptors, and substrate-context labels, so a single propagating GO assertion would overstate the shared biology.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## PN row 2: Ubiquitin Proteasome System | Ubiquitin and UBL binding | DUB | USP / with UBD | UIM, UBA-like, SIM
- UniProt: Q9UHP3
- In branches: UPS
- Signature domains: IPR003903, IPR054109, PMID: 18538659
- Auxiliary domains: IPR028889
- PN references (titles):
    - 18538659
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|Ubiquitin and UBL binding|DUB|USP / with UBD|UIM, UBA-like, SIM
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower UBL-binding DUB-domain subdivision. Because this subtree includes noncatalytic or pseudo-DUB cases, active DUB propagation is handled by the DUB-family branch rather than this binding-domain node.
    - [type] Ubiquitin Proteasome System|Ubiquitin and UBL binding|DUB|USP / with UBD
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower UBL-binding DUB-domain subdivision. Because this subtree includes noncatalytic or pseudo-DUB cases, active DUB propagation is handled by the DUB-family branch rather than this binding-domain node.
    - [group] Ubiquitin Proteasome System|Ubiquitin and UBL binding|DUB
        status=context_only scope=too_broad_to_propagate GO=[GO:0101005 deubiquitinase activity]
        rationale: This UBL-binding group is DUB-related context, but it includes noncatalytic or pseudo-DUB domain cases such as NPLOC4/USP39-like entries. Active DUB propagation is handled from the DUB-family branch.
    - [class] Ubiquitin Proteasome System|Ubiquitin and UBL binding
        status=context_only scope=too_broad_to_propagate GO=[GO:0140036 ubiquitin-modified protein reader activity]
        rationale: This class records ubiquitin/UBL-reader context, but the subtree mixes ubiquitin, SUMO, UBL-domain, domain-architecture, catalytic, signaling, trafficking, and nucleic-acid process buckets. It is useful context, not a safe direct propagation.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:0101005 deubiquitinase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|DUBs and UBL demodifiers|USP

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
