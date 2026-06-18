# HSPA13 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: P48723
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07b
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/HSPA13/HSPA13-ai-review.yaml](HSPA13-ai-review.yaml)
- AIGR review HTML: present - [genes/human/HSPA13/HSPA13-ai-review.html](HSPA13-ai-review.html)
- Gene notes: present - [genes/human/HSPA13/HSPA13-notes.md](HSPA13-notes.md)
- GOA TSV: present - [genes/human/HSPA13/HSPA13-goa.tsv](HSPA13-goa.tsv)
- UniProt record: present - [genes/human/HSPA13/HSPA13-uniprot.txt](HSPA13-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/HSPA13.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/HSPA13.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/HSPA13.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/HSPA13.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: HSPA13 (heat shock 70 kDa protein 13, also called STCH, "stress-70 protein chaperone microsome-associated") is an atypical, non-canonical member of the HSP70 family. It contains an N-terminal signal/leader sequence and the HSP70 nucleotide-binding (ATPase) domain, but it carries a ~50-residue insertion within the ATP-binding domain and truncates the C-terminal substrate (peptide)-binding region characteristic of canonical HSP70 chaperones. Accordingly its ATPase activity is peptide-independent (not stimulated by substrate, unlike BiP or DnaK), and it is not expected to act as a classical substrate-refolding foldase. HSPA13 is a microsome/endoplasmic-reticulum-associated protein that is constitutively expressed in all tissues and induced by calcium ionophore rather than by heat shock. It binds ubiquitin-like (UbL-domain) shuttle proteins including ubiquilins (UBQLN1/2/4) through a short peptide in its ATPase domain, and the SGT co-chaperones SGTA/SGTB, implicating it in protein quality control linked to the ubiquitin-proteasome system rather than in autonomous protein folding.
- Existing/core annotation action counts: ACCEPT: 4; KEEP_AS_NON_CORE: 11; MARK_AS_OVER_ANNOTATED: 5

## PN Consistency Summary

- **Consistency:** Notes ↔ review strongly consistent and DIRECTLY contradict the PN mapping. STCH is an atypical HSP70 that carries a ~50-residue ATPase-domain insertion and TRUNCATES the C-terminal substrate/peptide-binding domain; its ATPase is peptide-INDEPENDENT, so it is not a classical foldase (PMID:8131751). Its characterized partners are ubiquilins (UBQLN1/2/4) and SGTA/B, linking it to UPS-associated quality control, not autonomous folding (PMID:10675567). The review MARK_AS_OVER_ANNOTATED on both GOA's GO:0044183 (protein folding chaperone, IBA) and GO:0042026 (protein refolding, IBA) for exactly this reason.
- **PN story / NEW pressure:** PN projects GO:0140662 ATP-dependent protein folding chaperone (verified real; OLS = foldase driven by ATP hydrolysis; child of GO:0044183). The review already rejects the GO:0044183 parent as over-annotation, so projecting the MORE specific foldase child is a sharper over-reach (labeled "more_specific_than_existing_goa" — but more specific in the wrong direction). The evidence-backed MFs are GO:0016887 ATP hydrolysis activity (peptide-independent) and GO:0032182 ubiquitin-like protein binding. This is a clear MS1-flagged atypical-HSP70 case where the PN family label mismaps.
- **Evidence alignment:** PN row carries no reference titles; review PMIDs (8131751 STCH ATPase core; 10675567 UbL binding; interactome set) all describe peptide-independent ATPase + ubiquilin/SGT binding — none supports ATP-dependent folding, diverging from the PN projection.
- **Verdict:** Atypical HSP70; PN's GO:0140662 foldase projection is contradicted by the truncated SBD and peptide-independent ATPase — over-reaches. **Recommended edits:** [MAP] do not project GO:0140662 ATP-dependent protein folding chaperone (nor GO:0044183) onto P48723 (PMID:8131751 truncated peptide-binding domain, peptide-independent ATPase); its evidenced MFs are GO:0016887 ATP hydrolysis activity and GO:0032182 ubiquitin-like protein binding.

## Full Consistency Review

- **UniProt:** P48723 (STCH) · **batch:** proteostasis-batch-2026-06-07b · **review status:** COMPLETE
- **PN placement:** one row — `ER proteostasis|Chaperone|HSP70 system|HSP70` (type) ; **PN-node mapping:** HSP70 type → mapped/ok_for_propagation_to_go GO:0140662 ATP-dependent protein folding chaperone (more_specific_than_existing_goa); group/class/branch no_mapping.
- **Consistency:** Notes ↔ review strongly consistent and DIRECTLY contradict the PN mapping. STCH is an atypical HSP70 that carries a ~50-residue ATPase-domain insertion and TRUNCATES the C-terminal substrate/peptide-binding domain; its ATPase is peptide-INDEPENDENT, so it is not a classical foldase (PMID:8131751). Its characterized partners are ubiquilins (UBQLN1/2/4) and SGTA/B, linking it to UPS-associated quality control, not autonomous folding (PMID:10675567). The review MARK_AS_OVER_ANNOTATED on both GOA's GO:0044183 (protein folding chaperone, IBA) and GO:0042026 (protein refolding, IBA) for exactly this reason.
- **PN story / NEW pressure:** PN projects GO:0140662 ATP-dependent protein folding chaperone (verified real; OLS = foldase driven by ATP hydrolysis; child of GO:0044183). The review already rejects the GO:0044183 parent as over-annotation, so projecting the MORE specific foldase child is a sharper over-reach (labeled "more_specific_than_existing_goa" — but more specific in the wrong direction). The evidence-backed MFs are GO:0016887 ATP hydrolysis activity (peptide-independent) and GO:0032182 ubiquitin-like protein binding. This is a clear MS1-flagged atypical-HSP70 case where the PN family label mismaps.
- **Mapping strategy:** This gene should CHANGE the node's behavior: do not propagate GO:0140662 (or GO:0044183) onto P48723. The PN-projected term is narrower-but-wrong (asserts ATP-driven foldase activity the protein cannot perform with a truncated SBD). Per TOMM20/HSPA8/RAB7A precedent, flag HSPA13 as an HSP70-node exception.
- **Evidence alignment:** PN row carries no reference titles; review PMIDs (8131751 STCH ATPase core; 10675567 UbL binding; interactome set) all describe peptide-independent ATPase + ubiquilin/SGT binding — none supports ATP-dependent folding, diverging from the PN projection.
- **Verdict:** Atypical HSP70; PN's GO:0140662 foldase projection is contradicted by the truncated SBD and peptide-independent ATPase — over-reaches. **Recommended edits:** [MAP] do not project GO:0140662 ATP-dependent protein folding chaperone (nor GO:0044183) onto P48723 (PMID:8131751 truncated peptide-binding domain, peptide-independent ATPase); its evidenced MFs are GO:0016887 ATP hydrolysis activity and GO:0032182 ubiquitin-like protein binding.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/HSPA13/HSPA13-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Chaperone | HSP70 system | HSP70
- UniProt: P48723
- In branches: ER
- PN-node mapping records (path + ancestors):
    - [type] ER proteostasis|Chaperone|HSP70 system|HSP70
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0140662 ATP-dependent protein folding chaperone]
        rationale: In the PN hierarchy, the type label HSP70 within the chaperone/HSP70-system context denotes canonical HSP70 chaperones. Propagation to the GO molecular function ATP-dependent protein folding chaperone is appropriate for curation, but the PN family label is not itself a strict GO-equivalent class.
    - [group] ER proteostasis|Chaperone|HSP70 system
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [class] ER proteostasis|Chaperone
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (1)
- GO:0140662 ATP-dependent protein folding chaperone | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=ER proteostasis|Chaperone|HSP70 system|HSP70

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
