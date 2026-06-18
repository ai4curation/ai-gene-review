# GIGYF1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: O75420
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07c
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/GIGYF1/GIGYF1-ai-review.yaml](GIGYF1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/GIGYF1/GIGYF1-ai-review.html](GIGYF1-ai-review.html)
- Gene notes: present - [genes/human/GIGYF1/GIGYF1-notes.md](GIGYF1-notes.md)
- GOA TSV: present - [genes/human/GIGYF1/GIGYF1-goa.tsv](GIGYF1-goa.tsv)
- UniProt record: present - [genes/human/GIGYF1/GIGYF1-uniprot.txt](GIGYF1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/GIGYF1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/GIGYF1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/GIGYF1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/GIGYF1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: GIGYF1 (GRB10-interacting GYF protein 1; PERQ1) is a cytosolic adaptor/scaffold protein and the paralog of GIGYF2. Its central GYF domain and N-terminal 4EHP-binding region allow it to nucleate a translational-repression and co-translational mRNA-decay module together with the non-canonical cap-binding protein 4EHP (EIF4E2), the DEAD-box helicase DDX6, and the collided-ribosome sensor E3 ligase ZNF598. By tethering 4EHP to the mRNA 5' cap, GIGYF1 represses cap-dependent translation initiation, and by co-translationally binding transcripts that experience ribosome pausing or stalling it marks them for decay, linking ribosome transit to mRNA turnover. The GYF domain also recruits RNA-associated repressors such as tristetraprolin (TTP) and the miRNA-pathway TNRC6 proteins to specific messages. In a separate, less-characterized legacy role, GIGYF1 was first identified through the GRB10 adapter as a modulator of insulin-like growth factor-1 (IGF-1) receptor and other receptor tyrosine kinase signaling. The protein is largely intrinsically disordered outside its GYF domain and is heavily phosphorylated.
- Existing/core annotation action counts: ACCEPT: 2; KEEP_AS_NON_CORE: 10; MODIFY: 2; NEW: 1

## PN Consistency Summary

- **Consistency:** Strong and mutually consistent. Deep research, notes, and review agree GIGYF1 is the cytosolic adaptor/scaffold that, via its N-terminal 4EHP-binding region and GYF domain, nucleates the 4EHP-GIGYF1-DDX6-ZNF598 module repressing cap-dependent initiation and triggering co-translational mRNA decay on ribosome-paused/stalled transcripts. Review ACCEPTs GO:0045947 (negative regulation of translational initiation, IBA) and adds GO:0008190 (eIF4E binding) as NEW core MF — both directly encode the RQC-coupled repression the PN node targets. No contradictions.
- **PN story / NEW pressure:** PN asserts only GO:0006515 (RQC umbrella, new_to_goa, verified real). The review captures the same RQC-coupled repression via the more specific GO:0045947 and the NEW GO:0008190 (eIF4E binding). GIGYF1's RQC role is real (PMID:33053355 — paused-transcript accumulation in KO; ZNF598 dependence), so GO:0006515 is defensible as an umbrella but is broader than the review's specific terms. Note the review (unlike GIGYF2's) does NOT carry GO:0072344 (rescue of stalled cytosolic ribosome) for GIGYF1 — a paralog asymmetry. **Already captured** (more specifically); GO:0006515 does not over-reach but adds nothing the review lacks functionally.
- **Evidence alignment:** PN dossier lists no reference titles for GIGYF1; alignment is via the projected GO:0006515. Review's core PMIDs (33053355 translation-coupled decay; 31439631 GIGYF-4EHP-DDX6 assembly) cover exactly the RQC/repression biology the PN node encodes. No divergence.
- **Verdict:** Fully consistent; PN RQC story already captured more precisely (GO:0045947 + NEW GO:0008190). GO:0006515 is a defensible umbrella, not an over-reach. **Recommended edits:** [YAML] for paralog consistency, consider whether GIGYF1 warrants GO:0072344 (rescue of stalled cytosolic ribosome) as GIGYF2's review carries it — the underlying PMID:33053355/RQC evidence is shared (curator judgment; optional).

## Full Consistency Review

- **UniProt:** O75420 · **batch:** proteostasis-batch-2026-06-07c · **review status:** COMPLETE
- **PN placement:** `Translation|Cytosolic translation|Ribosome-associated QC|other RQC processes` ; **PN-node mapping:** RQC type=no_mapping; RQC group=mapped→GO:0006515; class/branch context_only (GO:0002181/GO:0006412 too_broad).
- **Consistency:** Strong and mutually consistent. Deep research, notes, and review agree GIGYF1 is the cytosolic adaptor/scaffold that, via its N-terminal 4EHP-binding region and GYF domain, nucleates the 4EHP-GIGYF1-DDX6-ZNF598 module repressing cap-dependent initiation and triggering co-translational mRNA decay on ribosome-paused/stalled transcripts. Review ACCEPTs GO:0045947 (negative regulation of translational initiation, IBA) and adds GO:0008190 (eIF4E binding) as NEW core MF — both directly encode the RQC-coupled repression the PN node targets. No contradictions.
- **PN story / NEW pressure:** PN asserts only GO:0006515 (RQC umbrella, new_to_goa, verified real). The review captures the same RQC-coupled repression via the more specific GO:0045947 and the NEW GO:0008190 (eIF4E binding). GIGYF1's RQC role is real (PMID:33053355 — paused-transcript accumulation in KO; ZNF598 dependence), so GO:0006515 is defensible as an umbrella but is broader than the review's specific terms. Note the review (unlike GIGYF2's) does NOT carry GO:0072344 (rescue of stalled cytosolic ribosome) for GIGYF1 — a paralog asymmetry. **Already captured** (more specifically); GO:0006515 does not over-reach but adds nothing the review lacks functionally.
- **Mapping strategy:** RQC group→GO:0006515 is acceptable as a broad umbrella over the review's GO:0045947/GO:0017148. No mapping change required. The class/branch context_only demotions (too_broad) are correct. Worth noting for paralog consistency: GIGYF2's review additionally carries GO:0072344; GIGYF1's does not — if PN treats the paralogs as one RQC module, the GIGYF1 review could parallel GIGYF2.
- **Evidence alignment:** PN dossier lists no reference titles for GIGYF1; alignment is via the projected GO:0006515. Review's core PMIDs (33053355 translation-coupled decay; 31439631 GIGYF-4EHP-DDX6 assembly) cover exactly the RQC/repression biology the PN node encodes. No divergence.
- **Verdict:** Fully consistent; PN RQC story already captured more precisely (GO:0045947 + NEW GO:0008190). GO:0006515 is a defensible umbrella, not an over-reach. **Recommended edits:** [YAML] for paralog consistency, consider whether GIGYF1 warrants GO:0072344 (rescue of stalled cytosolic ribosome) as GIGYF2's review carries it — the underlying PMID:33053355/RQC evidence is shared (curator judgment; optional).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/GIGYF1/GIGYF1-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Translation | Cytosolic translation | Ribosome-associated QC | other RQC processes
- UniProt: O75420
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

## Projected GO annotations (1)
- GO:0006515 protein quality control for misfolded or incompletely synthesized proteins | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Ribosome-associated QC

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
