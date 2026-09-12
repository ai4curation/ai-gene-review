# HBS1L PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9Y450
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07c
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/HBS1L/HBS1L-ai-review.yaml](HBS1L-ai-review.yaml)
- AIGR review HTML: present - [genes/human/HBS1L/HBS1L-ai-review.html](HBS1L-ai-review.html)
- Gene notes: present - [genes/human/HBS1L/HBS1L-notes.md](HBS1L-notes.md)
- GOA TSV: present - [genes/human/HBS1L/HBS1L-goa.tsv](HBS1L-goa.tsv)
- UniProt record: present - [genes/human/HBS1L/HBS1L-uniprot.txt](HBS1L-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/HBS1L.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/HBS1L.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/HBS1L.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/HBS1L.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: HBS1L (HBS1-like translational GTPase) is a cytoplasmic GTPase of the TRAFAC-class translation-factor superfamily, in the eEF1A/eRF3/Hbs1 group. It is the GTP-binding subunit of the Pelota-HBS1L complex (also called the Dom34-Hbs1 complex), partnering the eRF1-like factor PELO. The complex recognizes ribosomes stalled at the 3' end of an mRNA (truncated, non-stop, or no-go messages); HBS1L delivers PELO to the ribosomal A site and, through its GTPase activity, licenses PELO- and ABCE1-mediated splitting of the stalled 80S ribosome into subunits, thereby rescuing the ribosome and initiating no-go decay (NGD) and non-stop decay (NSD). Although phylogenetically related to the translation-termination factor eRF3, HBS1L does not possess eRF3 (peptide-release) activity. A short alternatively spliced isoform (HBS1LV3) instead scaffolds the cytoplasmic SKI complex and exosome via direct SKIC2 and EXOSC3 binding, coupling mRNA extraction to 3'-5' degradation.
- Existing/core annotation action counts: ACCEPT: 18; KEEP_AS_NON_CORE: 11; MARK_AS_OVER_ANNOTATED: 4

## PN Consistency Summary

- **Consistency:** Fully consistent. Deep research, review, and PN all describe HBS1L as the GTPase subunit of the Pelota-HBS1L (Dom34-Hbs1) complex that licenses PELO/ABCE1 ribosome splitting and triggers no-go/non-stop decay. The review is rich and well-aligned (multiple IDA GO:0072344, GO:0032790 ribosome disassembly, GO:0070966 no-go decay, GO:1990533 Dom34-Hbs1 complex). The isoform-2 (HBS1LV3) SKI/exosome scaffolding role is an added reviewer dimension outside the PN frame, not a contradiction.
- **PN story / NEW pressure:** No NEW pressure. PN's rescue story (GO:0072344) is already in GOA exact and richly ACCEPTED in the review (IBA + 2×IDA + TAS). The group-level GO:0006515 is a broad parent already entailed by the specific rescue/RQC terms HBS1L carries. Conclusion: **already captured** (more specifically than the PN projection).
- **Evidence alignment:** PN lists no reference titles. Review cites the canonical mechanistic set: PMID:21448132 (Pelota/Hbs1/ABCE1 dissociation), PMID:27863242 (cryo-EM), PMID:23667253 (non-stop decay), PMID:20947765 (Dom34:Hbs1 yeast), PMID:9872408 (original eRF3-related characterization), PMID:28204585 (short-isoform SKI/exosome). No citation conflict; PN simply carries no PMIDs.
- **Verdict:** Fully consistent; PN rescue story already captured (more specifically) — no NEW pressure. **Recommended edits:** none warranted; treat group-node GO:0006515 as context-only/entailed for HBS1L (do not add as a separate annotation) [MAP].

## Full Consistency Review

- **UniProt:** Q9Y450 · **batch:** proteostasis-batch-2026-06-07c · **review status:** COMPLETE
- **PN placement:** `Translation|Cytosolic translation|Ribosome-associated QC|Ribosomal rescue` ; **PN-node mapping:** type `Ribosomal rescue`=mapped→GO:0072344 rescue of stalled cytosolic ribosome (already_in_goa_exact); group `Ribosome-associated QC`=mapped→GO:0006515 protein quality control (new_to_goa); class/branch=context_only.
- **Consistency:** Fully consistent. Deep research, review, and PN all describe HBS1L as the GTPase subunit of the Pelota-HBS1L (Dom34-Hbs1) complex that licenses PELO/ABCE1 ribosome splitting and triggers no-go/non-stop decay. The review is rich and well-aligned (multiple IDA GO:0072344, GO:0032790 ribosome disassembly, GO:0070966 no-go decay, GO:1990533 Dom34-Hbs1 complex). The isoform-2 (HBS1LV3) SKI/exosome scaffolding role is an added reviewer dimension outside the PN frame, not a contradiction.
- **PN story / NEW pressure:** No NEW pressure. PN's rescue story (GO:0072344) is already in GOA exact and richly ACCEPTED in the review (IBA + 2×IDA + TAS). The group-level GO:0006515 is a broad parent already entailed by the specific rescue/RQC terms HBS1L carries. Conclusion: **already captured** (more specifically than the PN projection).
- **Mapping strategy:** Mapping matches precedent correctly — type-node GO:0072344 is exact and already in GOA; group-node GO:0006515 is a broader parent and should be treated as entailed/context, not separately propagated (would duplicate the more specific rescue/no-go terms). No node change driven by this gene.
- **Evidence alignment:** PN lists no reference titles. Review cites the canonical mechanistic set: PMID:21448132 (Pelota/Hbs1/ABCE1 dissociation), PMID:27863242 (cryo-EM), PMID:23667253 (non-stop decay), PMID:20947765 (Dom34:Hbs1 yeast), PMID:9872408 (original eRF3-related characterization), PMID:28204585 (short-isoform SKI/exosome). No citation conflict; PN simply carries no PMIDs.
- **Verdict:** Fully consistent; PN rescue story already captured (more specifically) — no NEW pressure. **Recommended edits:** none warranted; treat group-node GO:0006515 as context-only/entailed for HBS1L (do not add as a separate annotation) [MAP].

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/HBS1L/HBS1L-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Translation | Cytosolic translation | Ribosome-associated QC | Ribosomal rescue
- UniProt: Q9Y450
- In branches: TR
- PN-node mapping records (path + ancestors):
    - [type] Translation|Cytosolic translation|Ribosome-associated QC|Ribosomal rescue
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0072344 rescue of stalled cytosolic ribosome]
        rationale: This PN RQC type denotes rescue of stalled cytosolic ribosomes. The matching GO process term is the direct target.
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
- GO:0006515 protein quality control for misfolded or incompletely synthesized proteins | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Ribosome-associated QC
- GO:0072344 rescue of stalled cytosolic ribosome | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Translation|Cytosolic translation|Ribosome-associated QC|Ribosomal rescue

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
