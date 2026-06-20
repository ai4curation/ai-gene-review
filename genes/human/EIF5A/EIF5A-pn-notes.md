# EIF5A PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: P63241
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07c
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/EIF5A/EIF5A-ai-review.yaml](EIF5A-ai-review.yaml)
- AIGR review HTML: present - [genes/human/EIF5A/EIF5A-ai-review.html](EIF5A-ai-review.html)
- Gene notes: present - [genes/human/EIF5A/EIF5A-notes.md](EIF5A-notes.md)
- GOA TSV: present - [genes/human/EIF5A/EIF5A-goa.tsv](EIF5A-goa.tsv)
- UniProt record: present - [genes/human/EIF5A/EIF5A-uniprot.txt](EIF5A-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/EIF5A.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/EIF5A.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/EIF5A.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/EIF5A.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: EIF5A (eukaryotic translation initiation factor 5A-1, historically eIF-4D and "Rev-binding factor") is a small, highly conserved translation factor that, despite its legacy "initiation factor" name, acts mainly in translation elongation and termination. It is the only cellular protein to carry hypusine, a unique post-translational modification formed at Lys-50 by deoxyhypusine synthase (DHPS) and deoxyhypusine hydroxylase (DOHH) using spermidine; this modification is essential for its activity. eIF5A binds the 80S ribosome between the exit (E) and peptidyl (P) tRNA sites and stimulates peptide-bond formation at sequences that are intrinsically difficult to translate, most notably consecutive prolines (polyproline tracts) and other stalling motifs, thereby promoting efficient elongation through these contexts and resolving ribosome stalling. eIF5A and eEF2 bind translating ribosomes in a mutually exclusive manner. Through this elongation-promoting activity it supports specific cellular programs, including autophagy (by enabling translation of ATG3) and broad proteome synthesis. eIF5A is predominantly cytoplasmic and ribosome-associated, with a hypusine- and XPO4/RanGTP-dependent nucleocytoplasmic shuttling pool that can localize to the nucleus, nuclear pore and annulate lamellae. Hypusine-dependent localization and abundance changes underlie additional context-dependent roles in apoptosis and stress responses, and eIF5A serves as a cellular cofactor for retroviral (HIV-1 Rev / HTLV-1 Rex) mRNA export. Loss-of-function variants cause the autosomal dominant Faundes-Banka syndrome.
- Existing/core annotation action counts: ACCEPT: 19; KEEP_AS_NON_CORE: 28; MARK_AS_OVER_ANNOTATED: 2; MODIFY: 2

## PN Consistency Summary

- **Consistency:** Strong and mutually consistent on the core. Deep research, notes, and review all establish eIF5A as the hypusine-containing elongation/termination factor that binds the 80S ribosome between E and P sites and resolves stalling at polyproline and other difficult motifs. Review ACCEPTs GO:0003746 (elongation factor activity, IBA/IEA/ISS) and GO:0043022 (ribosome binding) as core — matching the PN elongation-type mapping exactly. No contradiction.
- **PN story / NEW pressure:** The PN RQC node (GO:0006515, new_to_goa, verified real) is the only place PN asserts a role beyond the review's elongation framing. eIF5A is indeed described (UniProt; notes) as an RQC cofactor joining the RQC complex to facilitate peptidyl transfer/CAT-tailing, so an RQC-process annotation is defensible — but the review does NOT carry any RQC/GO:0006515 term, treating eIF5A purely as an elongation factor. This is a mild NEW pressure: GO:0006515 is plausibly addable but is a broad umbrella, and eIF5A's RQC role is supportive rather than a dedicated surveillance function. Leans **already captured / mild over-reach**: the elongation-factor activity is the real shared biology; GO:0006515 risks over-stating a QC role for a general elongation factor.
- **Evidence alignment:** PN dossier lists no reference titles for EIF5A. Review's core PMIDs (27115996 ribosome binding; 29712776 ATG3/autophagy elongation; 33547280 FABAS disease) all anchor the elongation-factor function the PN elongation node encodes. No divergence.
- **Verdict:** Consistent; elongation core fully captured. GO:0006515 RQC umbrella is defensible but mildly over-reaching for a general elongation factor and is absent from the review. **Recommended edits:** [MAP] treat the EIF5A RQC-group→GO:0006515 projection as low-confidence (eIF5A is an elongation factor with a supportive RQC-cofactor role, not a dedicated surveillance factor); optionally [YAML] consider adding eIF5A's RQC-cofactor role only if curator deems UniProt's CAT-tailing statement annotation-worthy.

## Full Consistency Review

- **UniProt:** P63241 · **batch:** proteostasis-batch-2026-06-07c · **review status:** COMPLETE
- **PN placement:** `Translation|Cytosolic translation|Translation elongation|assorted elongation factors` AND `Translation|Cytosolic translation|Ribosome-associated QC|other RQC processes` ; **PN-node mapping:** elongation type=mapped→GO:0003746 (translation elongation factor activity); elongation group=context_only (GO:0006414); RQC group=mapped→GO:0006515; RQC type=no_mapping; class/branch context_only (GO:0002181/GO:0006412 too_broad).
- **Consistency:** Strong and mutually consistent on the core. Deep research, notes, and review all establish eIF5A as the hypusine-containing elongation/termination factor that binds the 80S ribosome between E and P sites and resolves stalling at polyproline and other difficult motifs. Review ACCEPTs GO:0003746 (elongation factor activity, IBA/IEA/ISS) and GO:0043022 (ribosome binding) as core — matching the PN elongation-type mapping exactly. No contradiction.
- **PN story / NEW pressure:** The PN RQC node (GO:0006515, new_to_goa, verified real) is the only place PN asserts a role beyond the review's elongation framing. eIF5A is indeed described (UniProt; notes) as an RQC cofactor joining the RQC complex to facilitate peptidyl transfer/CAT-tailing, so an RQC-process annotation is defensible — but the review does NOT carry any RQC/GO:0006515 term, treating eIF5A purely as an elongation factor. This is a mild NEW pressure: GO:0006515 is plausibly addable but is a broad umbrella, and eIF5A's RQC role is supportive rather than a dedicated surveillance function. Leans **already captured / mild over-reach**: the elongation-factor activity is the real shared biology; GO:0006515 risks over-stating a QC role for a general elongation factor.
- **Mapping strategy:** Elongation type→GO:0003746 is correct and present in GOA/review. The RQC group→GO:0006515 projection is the borderline call: defensible by UniProt's RQC-cofactor statement, but broad. The group's context_only demotion to GO:0006414 (elongation) is appropriate (the group also houses tRNA synthetases/deacylases). No mapping change required for the elongation node.
- **Evidence alignment:** PN dossier lists no reference titles for EIF5A. Review's core PMIDs (27115996 ribosome binding; 29712776 ATG3/autophagy elongation; 33547280 FABAS disease) all anchor the elongation-factor function the PN elongation node encodes. No divergence.
- **Verdict:** Consistent; elongation core fully captured. GO:0006515 RQC umbrella is defensible but mildly over-reaching for a general elongation factor and is absent from the review. **Recommended edits:** [MAP] treat the EIF5A RQC-group→GO:0006515 projection as low-confidence (eIF5A is an elongation factor with a supportive RQC-cofactor role, not a dedicated surveillance factor); optionally [YAML] consider adding eIF5A's RQC-cofactor role only if curator deems UniProt's CAT-tailing statement annotation-worthy.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/EIF5A/EIF5A-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Translation | Cytosolic translation | Translation elongation | assorted elongation factors
- UniProt: P63241
- In branches: TR
- PN-node mapping records (path + ancestors):
    - [type] Translation|Cytosolic translation|Translation elongation|assorted elongation factors
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0003746 translation elongation factor activity]
        rationale: This PN type groups cytosolic elongation factors. Translation elongation factor activity is the shared molecular-function target.
    - [group] Translation|Cytosolic translation|Translation elongation
        status=context_only scope=too_broad_to_propagate GO=[GO:0006414 translational elongation]
        rationale: This PN group is an elongation-context bucket, but it also contains tRNA synthetases, tRNA deacylases, and multisynthetase-complex members whose direct shared assertions are narrower molecular functions or complexes. The elongation relationship is retained as context only.
    - [class] Translation|Cytosolic translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0002181 cytoplasmic translation]
        rationale: The PN class Cytosolic translation is centered on the cytoplasmic translation apparatus and process, but it also houses supporting machinery such as ribosome biogenesis factors. The GO process term is a useful high-level label for the class, but propagating it to all members would over-annotate genes whose PN placement is through assembly or maturation context rather than core cytoplasmic translation.
    - [branch] Translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0006412 translation]
        rationale: The PN Translation branch is organized around the translation apparatus and immediately associated cotranslational quality-control systems. GO translation is the closest high-level process label, but the PN branch also contains adjacent machinery such as ribosome biogenesis and nascent-chain handling. Keeping this relationship is useful for interpretation, but it is too broad to project safely onto every member.

## PN row 2: Translation | Cytosolic translation | Ribosome-associated QC | other RQC processes
- UniProt: P63241
- In branches: TR
- PN-node mapping records (path + ancestors):
    - [type] Translation|Cytosolic translation|Ribosome-associated QC|other RQC processes
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [group] Translation|Cytosolic translation|Ribosome-associated QC
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0006515 protein quality control for misfolded or incompletely synthesized proteins]
        rationale: The PN ribosome-associated quality-control group covers surveillance and disposal of stalled or defective nascent-chain translation products. GO lacks a dedicated ribosome-associated QC term in the local cache, so the broader protein-quality-control process is the best supported target.
    - [class] Translation|Cytosolic translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0002181 cytoplasmic translation]
        rationale: The PN class Cytosolic translation is centered on the cytoplasmic translation apparatus and process, but it also houses supporting machinery such as ribosome biogenesis factors. The GO process term is a useful high-level label for the class, but propagating it to all members would over-annotate genes whose PN placement is through assembly or maturation context rather than core cytoplasmic translation.
    - [branch] Translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0006412 translation]
        rationale: The PN Translation branch is organized around the translation apparatus and immediately associated cotranslational quality-control systems. GO translation is the closest high-level process label, but the PN branch also contains adjacent machinery such as ribosome biogenesis and nascent-chain handling. Keeping this relationship is useful for interpretation, but it is too broad to project safely onto every member.

## Projected GO annotations (2)
- GO:0003746 translation elongation factor activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Translation|Cytosolic translation|Translation elongation|assorted elongation factors
- GO:0006515 protein quality control for misfolded or incompletely synthesized proteins | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Ribosome-associated QC

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
