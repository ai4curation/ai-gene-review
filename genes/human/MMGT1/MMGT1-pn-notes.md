# MMGT1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q8N4V1
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-11
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/MMGT1/MMGT1-ai-review.yaml](MMGT1-ai-review.yaml)
- AIGR review HTML: missing - genes/human/MMGT1/MMGT1-ai-review.html
- Gene notes: present - [genes/human/MMGT1/MMGT1-notes.md](MMGT1-notes.md)
- GOA TSV: present - [genes/human/MMGT1/MMGT1-goa.tsv](MMGT1-goa.tsv)
- UniProt record: present - [genes/human/MMGT1/MMGT1-uniprot.txt](MMGT1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/MMGT1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/MMGT1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/MMGT1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/MMGT1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/MMGT1/MMGT1-deep-research-falcon.md](MMGT1-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: MMGT1 (ER membrane protein complex subunit 5, EMC5; also known as membrane magnesium transporter 1 / TMEM32) is a small (131 aa) polytopic ER membrane protein with two transmembrane helices and cytoplasmic N- and C-termini. It is a constitutive subunit of the ER membrane protein complex (EMC), a conserved transmembrane-domain insertase and membrane-protein chaperone of the endoplasmic reticulum. Within the complex, EMC5 packs against the catalytic insertase subunits EMC3 and EMC6 that form the hydrophilic membrane vestibule through which substrate transmembrane domains are inserted. The EMC enables the energy-independent insertion of newly synthesized membrane proteins into the ER membrane, with a preference for transmembrane domains that are weakly hydrophobic or contain destabilizing charged or aromatic residues. It mediates post-translational insertion of tail-anchored proteins and cotranslational insertion and topogenesis of multipass membrane proteins, including setting the N-exo topology of the first transmembrane domain of G protein-coupled receptors. MMGT1 localizes to the ER membrane and is broadly expressed. Its legacy designation as a membrane magnesium transporter derives from overexpression studies of the rodent ortholog and is not supported by a defined transport mechanism for the human protein.
- Existing/core annotation action counts: ACCEPT: 13; KEEP_AS_NON_CORE: 24; MARK_AS_OVER_ANNOTATED: 14

## PN Consistency Summary

- **Consistency:** Mostly consistent, but MMGT1 is the gene where the legacy-name trap is live. Review, deep research, and PN annotation all treat MMGT1 as EMC5 (an EMC insertase subunit), and the review systematically MARK_AS_OVER_ANNOTATED the legacy metal-transport terms (GO:0015095 Mg, GO:0006824 Co, GO:0034755 Fe, GO:0022857, GO:0055085, GO:1903830, etc.) derived from rodent-ortholog By-similarity. GO:0072546 + ER membrane + insertion BPs captured. No contradiction with PN, which places it firmly as an EMC component.
- **PN story / NEW pressure:** PN asserts only EMC-component/import role — no new pressure; fully captured by GO:0072546 and the insertion BPs. Conclusion: already captured.
- **Evidence alignment:** Good overlap on EMC papers (PMID:22119785, PMID:29242231, PMID:38517390 — EMC5 used as Strep handle). Review adds the MMGT1-specific MtB persistence/lipid-droplet axis PMID:37269834 (mechanism unresolved, kept as context). PN cites no row-1 titles; no divergence.
- **Verdict:** Consistent on EMC identity; legacy Mg/metal-transporter terms correctly over-annotated; PN adds no NEW pressure; note the misleading `more_specific_than_existing_goa` framing (compared against a rejected transport term).

## Full Consistency Review

- **UniProt:** Q8N4V1 (EMC5; legacy "membrane magnesium transporter 1" / TMEM32) · **batch:** proteostasis-batch-2026-06-11 · **review status:** COMPLETE (very thorough; ~40 annotations including a large block of legacy transporter terms all adjudicated)
- **PN placement:** `ER proteostasis | Protein transport | Transmembrane protein import | EMC complex component`; **PN-node mapping:** type=mapped/ok_for_propagation → GO:0072546 EMC complex (already_in_goa_exact); group→GO:0044743 (goa_status=more_specific_than_existing_goa); class→GO:0015031 (new_to_goa); branch=no_mapping.
- **Consistency:** Mostly consistent, but MMGT1 is the gene where the legacy-name trap is live. Review, deep research, and PN annotation all treat MMGT1 as EMC5 (an EMC insertase subunit), and the review systematically MARK_AS_OVER_ANNOTATED the legacy metal-transport terms (GO:0015095 Mg, GO:0006824 Co, GO:0034755 Fe, GO:0022857, GO:0055085, GO:1903830, etc.) derived from rodent-ortholog By-similarity. GO:0072546 + ER membrane + insertion BPs captured. No contradiction with PN, which places it firmly as an EMC component.
- **PN story / NEW pressure:** PN asserts only EMC-component/import role — no new pressure; fully captured by GO:0072546 and the insertion BPs. Conclusion: already captured.
- **Mapping strategy:** Subtle. The dossier flags group→GO:0044743 as `more_specific_than_existing_goa`. MMGT1's existing GOA "transport" terms are GO:0055085 (transmembrane transport, IEA) and metal-transport terms — which the review is actively flagging as OVER-ANNOTATED (legacy magnesium-transporter artifact, not protein import). So the PN projection (GO:0044743 protein transmembrane *import*) is conceptually correct (insertion) but the `more_specific_than_existing_goa` comparison is being made against a transport term the review rejects, not against a genuine import annotation — the framing is misleading. type→GO:0072546 is exact/correct. Projected GO:0044743/GO:0015031 are broader than the review's specific insertion terms (broader-ancestor pattern, cf. TOMM20/HSPA8/RAB7A).
- **Evidence alignment:** Good overlap on EMC papers (PMID:22119785, PMID:29242231, PMID:38517390 — EMC5 used as Strep handle). Review adds the MMGT1-specific MtB persistence/lipid-droplet axis PMID:37269834 (mechanism unresolved, kept as context). PN cites no row-1 titles; no divergence.
- **Verdict:** Consistent on EMC identity; legacy Mg/metal-transporter terms correctly over-annotated; PN adds no NEW pressure; note the misleading `more_specific_than_existing_goa` framing (compared against a rejected transport term).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/MMGT1/MMGT1-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Protein transport | Transmembrane protein import | EMC complex component
- UniProt: Q8N4V1
- In branches: ER
- PN-node mapping records (path + ancestors):
    - [type] ER proteostasis|Protein transport|Transmembrane protein import|EMC complex component
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0072546 EMC complex]
        rationale: This PN type denotes ER membrane protein complex components. The GO EMC complex cellular-component term is the direct target.
    - [group] ER proteostasis|Protein transport|Transmembrane protein import
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0044743 protein transmembrane import into intracellular organelle]
        rationale: This PN group covers ER transmembrane-protein insertion/import systems such as EMC- and PAT-related pathways. The local GO cache does not expose an ER-specific matching term, so the broader intracellular-organelle transmembrane-import process is the best supported propagation target.
    - [class] ER proteostasis|Protein transport
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0015031 protein transport]
        rationale: The PN ER Protein transport class groups ER-targeting and ER-insertion pathways. GO protein transport is the appropriate propagation target, while the source class remains ER-specific and broader than any single GO transport subtype.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (3)
- GO:0015031 protein transport | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=ER proteostasis|Protein transport
- GO:0044743 protein transmembrane import into intracellular organelle | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=ER proteostasis|Protein transport|Transmembrane protein import
- GO:0072546 EMC complex | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=ER proteostasis|Protein transport|Transmembrane protein import|EMC complex component

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
