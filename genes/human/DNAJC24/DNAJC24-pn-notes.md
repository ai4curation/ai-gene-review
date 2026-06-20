# DNAJC24 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q6P3W2
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07b
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/DNAJC24/DNAJC24-ai-review.yaml](DNAJC24-ai-review.yaml)
- AIGR review HTML: present - [genes/human/DNAJC24/DNAJC24-ai-review.html](DNAJC24-ai-review.html)
- Gene notes: present - [genes/human/DNAJC24/DNAJC24-notes.md](DNAJC24-notes.md)
- GOA TSV: present - [genes/human/DNAJC24/DNAJC24-goa.tsv](DNAJC24-goa.tsv)
- UniProt record: present - [genes/human/DNAJC24/DNAJC24-uniprot.txt](DNAJC24-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJC24.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJC24.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJC24.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJC24.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: DNAJC24 (DnaJ homolog subfamily C member 24; also DPH4 / ZCSL3, Diphthamide biosynthesis protein 4) is a small cytoplasmic J-domain co-chaperone of the HSP70 system that also functions in diphthamide biosynthesis. It comprises an N-terminal J-domain (with the canonical HPD motif) and a C-terminal DPH-type CSL metal-binding domain that can coordinate either zinc or iron. Through its J-domain it stimulates the ATPase activity of HSP70-type chaperones; its CSL domain binds metal ions, and iron binding promotes oligomerization and confers redox/electron-carrier activity. DNAJC24 participates in the conserved multi-step diphthamide pathway that installs the diphthamide modification on a specific histidine of translation elongation factor 2 (EEF2), the residue targeted by diphtheria toxin and Pseudomonas exotoxin A.
- Existing/core annotation action counts: ACCEPT: 6; KEEP_AS_NON_CORE: 3; MARK_AS_OVER_ANNOTATED: 1

## PN Consistency Summary

- **Consistency:** Deep research, notes, and review YAML are fully self-consistent: DPH4 is a J-domain co-chaperone that stimulates HSP70 ATPase (IDA + IBA, PMID:22367199) and a diphthamide-biosynthesis factor (GO:0017183). The PN "J-domain HSP70 cochaperone" placement agrees with the review's HSP70-cochaperone framing. No contradictions.
- **PN story / NEW pressure:** PN asserts Hsp70 protein binding (GO:0030544, verified real). GOA does NOT contain GO:0030544; closest is GO:0001671 ATPase activator activity (IDA). DPH4's J-domain HSP70 interaction is experimentally supported, so GO:0030544 is a defensible, specific ADD (J-proteins bind Hsp70). Not over-reaching for this gene — but note GO:0001671 already captures the functional consequence; GO:0030544 would be a complementary, narrower MF.
- **Evidence alignment:** PN row carries no reference titles; review anchors on PMID:22367199 (structure/iron-mediated moonlighting) and PMID:22509046 (diphthamide/EF2). Both VERIFIED in YAML. No divergence.
- **Verdict:** Consistent. GO:0030544 is a defensible ADD (new_to_goa). Diphthamide role correctly kept distinct from chaperone family inference.

## Full Consistency Review

- **UniProt:** Q6P3W2 (DPH4 / ZCSL3) · **batch:** proteostasis-batch-2026-06-07b · **review status:** COMPLETE
- **PN placement:** `Cytonuclear proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone` ; **PN-node mapping:** type=mapped, scope=ok_for_propagation_to_go, GO:0030544 Hsp70 protein binding (projected new_to_goa); group/class/branch=no_mapping.
- **Consistency:** Deep research, notes, and review YAML are fully self-consistent: DPH4 is a J-domain co-chaperone that stimulates HSP70 ATPase (IDA + IBA, PMID:22367199) and a diphthamide-biosynthesis factor (GO:0017183). The PN "J-domain HSP70 cochaperone" placement agrees with the review's HSP70-cochaperone framing. No contradictions.
- **PN story / NEW pressure:** PN asserts Hsp70 protein binding (GO:0030544, verified real). GOA does NOT contain GO:0030544; closest is GO:0001671 ATPase activator activity (IDA). DPH4's J-domain HSP70 interaction is experimentally supported, so GO:0030544 is a defensible, specific ADD (J-proteins bind Hsp70). Not over-reaching for this gene — but note GO:0001671 already captures the functional consequence; GO:0030544 would be a complementary, narrower MF.
- **Mapping strategy:** Does not change node status. Projection (new_to_goa) is accurate — GO:0030544 genuinely absent from GOA. Term is appropriately specific (not over-broad), since DPH4's HSP70 interaction is real.
- **Evidence alignment:** PN row carries no reference titles; review anchors on PMID:22367199 (structure/iron-mediated moonlighting) and PMID:22509046 (diphthamide/EF2). Both VERIFIED in YAML. No divergence.
- **Verdict:** Consistent. GO:0030544 is a defensible ADD (new_to_goa). Diphthamide role correctly kept distinct from chaperone family inference.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/DNAJC24/DNAJC24-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Cytonuclear proteostasis | Chaperone | HSP70 system | J-domain containing HSP70 cochaperone
- UniProt: Q6P3W2
- In branches: CY
- PN-node mapping records (path + ancestors):
    - [type] Cytonuclear proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0030544 Hsp70 protein binding]
        rationale: In the PN hierarchy, this type denotes J-domain cochaperones assigned to the HSP70 system. Their shared mechanistic role is direct interaction with HSP70-family chaperones, making Hsp70 protein binding the most defensible GO target in the current cache.
    - [group] Cytonuclear proteostasis|Chaperone|HSP70 system
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a specific GO class. The member genes span multiple activities, complexes, or contexts, so propagation from this node would overstate the shared biology; use narrower child or gene-level curations.
    - [class] Cytonuclear proteostasis|Chaperone
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a specific GO class. The member genes span multiple activities, complexes, or contexts, so propagation from this node would overstate the shared biology; use narrower child or gene-level curations.
    - [branch] Cytonuclear proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (1)
- GO:0030544 Hsp70 protein binding | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Cytonuclear proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
