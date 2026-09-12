# LTN1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: O94822
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07c
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/LTN1/LTN1-ai-review.yaml](LTN1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/LTN1/LTN1-ai-review.html](LTN1-ai-review.html)
- Gene notes: present - [genes/human/LTN1/LTN1-notes.md](LTN1-notes.md)
- GOA TSV: present - [genes/human/LTN1/LTN1-goa.tsv](LTN1-goa.tsv)
- UniProt record: present - [genes/human/LTN1/LTN1-uniprot.txt](LTN1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/LTN1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/LTN1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/LTN1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/LTN1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: LTN1 (Listerin, also RNF160/ZNF294) is a large (1766 aa) cytosolic RING-type E3 ubiquitin-protein ligase (EC 2.3.2.27) that is the catalytic core of the ribosome-associated quality control (RQC) complex. Its N-terminal HEAT/ARM-repeat solenoid wraps around the 60S large ribosomal subunit while its C-terminal RING-CH (RING-type zinc finger) domain catalyzes ubiquitin transfer. When an elongating 80S ribosome stalls and is split into subunits by the rescue factors PELO/HBS1L/ABCE1, the incomplete nascent polypeptide remains attached to a peptidyl-tRNA housed in the 60S subunit; LTN1 is recruited to these 60S-nascent chain complexes by NEMF, which senses the exposed P-site tRNA, and poly-ubiquitinates the trapped nascent chain. This commits aberrant translation products to extraction by the VCP/p97 AAA-ATPase and degradation by the proteasome, preventing accumulation of potentially toxic incomplete proteins. LTN1 thus functions in nascent-chain surveillance and rescue of stalled ribosomes; it is broadly expressed and acts in the cytosol in association with the 60S subunit.
- Existing/core annotation action counts: ACCEPT: 27; KEEP_AS_NON_CORE: 4

## PN Consistency Summary

- **Consistency:** Fully consistent. Deep research, review, and PN all describe LTN1/Listerin as the RING E3 ligase of the RQC complex (LTN1+NEMF+TCF25 on 60S) that poly-ubiquitinates 60S-housed stalled nascent chains for VCP/p97 + proteasomal degradation. Review is comprehensive: GO:0061630 ligase activity (IDA), GO:1990116 RQC catabolic process, GO:1990112 RQC complex, GO:0072344 rescue, GO:0043023 60S binding, GO:0008270 zinc (RING). All PN mappings land on terms LTN1 already holds.
- **PN story / NEW pressure:** No NEW pressure. Every PN-projected term is already in GOA / the review: GO:0016567 protein ubiquitination (already_in_goa_exact), GO:0061630 ligase activity (already_in_goa_exact, ×2 rows), GO:0006515 (broad parent of the specific GO:1990116 LTN1 already holds). Conclusion: **already captured**, and more specifically (LTN1 carries the RQC-specific GO:1990116 / GO:1990112 that the generic PN GO:0006515 / GO:0016567 only approximate).
- **Evidence alignment:** PN row 2 lists "19489725 / rev" as a reference; the review does NOT cite PMID:19489725. The review's definitive structural anchor is PMID:25578875 (RQC complex structure/assembly; LTN1 ligase + NEMF dependence) plus PMID:35452614 (RQC review) and PMID:28757607 (Hel2/40S context, LOW relevance). Minor divergence: the PN row-2 citation (19489725, the original Listerin/neurodegeneration paper) is not in the review's reference set.
- **Verdict:** Fully consistent; PN story already captured (review more specific) — no NEW pressure. **Recommended edits:** none required for terms; treat group-node GO:0006515 as context-only/entailed (LTN1 has the specific GO:1990116) [MAP]; optionally add PMID:19489725 (PN row-2 reference) to `references` if it supports the Listerin RQC/neurodegeneration role [REF].

## Full Consistency Review

- **UniProt:** O94822 · **batch:** proteostasis-batch-2026-06-07c · **review status:** COMPLETE
- **PN placement:** THREE rows. Row 1 (TR) `Translation|Cytosolic translation|Ribosome-associated QC|Ubiquitination` (type=mapped→GO:0016567 protein ubiquitination [already_in_goa_exact]; group→GO:0006515 protein quality control [new_to_goa]). Rows 2 & 3 (UPS) `E3 ubiquitin and UBL ligases|RING ...` and `Ubiquitin and UBL binding|E3 ligase|RING/with UBD|RWD (LTN1)` (group→GO:0061630 ubiquitin protein ligase activity [already_in_goa_exact]; subtype/type=no_mapping; class=context_only).
- **Consistency:** Fully consistent. Deep research, review, and PN all describe LTN1/Listerin as the RING E3 ligase of the RQC complex (LTN1+NEMF+TCF25 on 60S) that poly-ubiquitinates 60S-housed stalled nascent chains for VCP/p97 + proteasomal degradation. Review is comprehensive: GO:0061630 ligase activity (IDA), GO:1990116 RQC catabolic process, GO:1990112 RQC complex, GO:0072344 rescue, GO:0043023 60S binding, GO:0008270 zinc (RING). All PN mappings land on terms LTN1 already holds.
- **PN story / NEW pressure:** No NEW pressure. Every PN-projected term is already in GOA / the review: GO:0016567 protein ubiquitination (already_in_goa_exact), GO:0061630 ligase activity (already_in_goa_exact, ×2 rows), GO:0006515 (broad parent of the specific GO:1990116 LTN1 already holds). Conclusion: **already captured**, and more specifically (LTN1 carries the RQC-specific GO:1990116 / GO:1990112 that the generic PN GO:0006515 / GO:0016567 only approximate).
- **Mapping strategy:** Correctly distinguishes broad from specific per the RQC-branch guidance: group GO:0006515 is the broad parent, and LTN1's own GO:1990116 (ribosome-associated ubiquitin-dependent catabolism) is the specific RQC term — so GO:0006515 should be entailed/context-only, not separately propagated. LTN1 = the RQC E3 ligase, exactly as the branch note states. No node change warranted by this gene.
- **Evidence alignment:** PN row 2 lists "19489725 / rev" as a reference; the review does NOT cite PMID:19489725. The review's definitive structural anchor is PMID:25578875 (RQC complex structure/assembly; LTN1 ligase + NEMF dependence) plus PMID:35452614 (RQC review) and PMID:28757607 (Hel2/40S context, LOW relevance). Minor divergence: the PN row-2 citation (19489725, the original Listerin/neurodegeneration paper) is not in the review's reference set.
- **Verdict:** Fully consistent; PN story already captured (review more specific) — no NEW pressure. **Recommended edits:** none required for terms; treat group-node GO:0006515 as context-only/entailed (LTN1 has the specific GO:1990116) [MAP]; optionally add PMID:19489725 (PN row-2 reference) to `references` if it supports the Listerin RQC/neurodegeneration role [REF].

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/LTN1/LTN1-ai-review.yaml
- PN workbook rows: 3

## PN row 1: Translation | Cytosolic translation | Ribosome-associated QC | Ubiquitination
- UniProt: O94822
- In branches: TR, UPS
- PN-node mapping records (path + ancestors):
    - [type] Translation|Cytosolic translation|Ribosome-associated QC|Ubiquitination
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0016567 protein ubiquitination]
        rationale: This PN RQC type denotes ubiquitination events on stalled translation complexes. Protein ubiquitination is the shared process target.
    - [group] Translation|Cytosolic translation|Ribosome-associated QC
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0006515 protein quality control for misfolded or incompletely synthesized proteins]
        rationale: The PN ribosome-associated quality-control group covers surveillance and disposal of stalled or defective nascent-chain translation products. GO lacks a dedicated ribosome-associated QC term in the local cache, so the broader protein-quality-control process is the best supported target.
    - [class] Translation|Cytosolic translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0002181 cytoplasmic translation]
        rationale: The PN class Cytosolic translation is centered on the cytoplasmic translation apparatus and process, but it also houses supporting machinery such as ribosome biogenesis factors. The GO process term is a useful high-level label for the class, but propagating it to all members would over-annotate genes whose PN placement is through assembly or maturation context rather than core cytoplasmic translation.
    - [branch] Translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0006412 translation]
        rationale: The PN Translation branch is organized around the translation apparatus and immediately associated cotranslational quality-control systems. GO translation is the closest high-level process label, but the PN branch also contains adjacent machinery such as ribosome biogenesis and nascent-chain handling. Keeping this relationship is useful for interpretation, but it is too broad to project safely onto every member.

## PN row 2: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | RING | ubiquitin binding domain | Armadillo-like
- UniProt: O94822
- In branches: TR, UPS
- Signature domains: IPR001841
- Auxiliary domains: IPR011989
- PN references (titles):
    - 19489725 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING|ubiquitin binding domain|Armadillo-like
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower E3-ligase architecture, component, or domain subdivision already covered by the curated parent E3 mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING|ubiquitin binding domain
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

## PN row 3: Ubiquitin Proteasome System | Ubiquitin and UBL binding | E3 ligase | RING / with UBD | RWD (LTN1)
- UniProt: O94822
- In branches: TR, UPS
- Signature domains: IPR054478
- Auxiliary domains: IPR001841
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|Ubiquitin and UBL binding|E3 ligase|RING / with UBD|RWD (LTN1)
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower enzyme-family, domain, or architecture subdivision already covered by a curated parent enzyme mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|Ubiquitin and UBL binding|E3 ligase|RING / with UBD
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

## Projected GO annotations (4)
- GO:0006515 protein quality control for misfolded or incompletely synthesized proteins | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Ribosome-associated QC
- GO:0016567 protein ubiquitination | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Translation|Cytosolic translation|Ribosome-associated QC|Ubiquitination
- GO:0061630 ubiquitin protein ligase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING
- GO:0061630 ubiquitin protein ligase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|Ubiquitin and UBL binding|E3 ligase

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
