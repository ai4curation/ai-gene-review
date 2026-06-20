# CWC27 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q6UX04
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/CWC27/CWC27-ai-review.yaml](CWC27-ai-review.yaml)
- AIGR review HTML: present - [genes/human/CWC27/CWC27-ai-review.html](CWC27-ai-review.html)
- Gene notes: present - [genes/human/CWC27/CWC27-notes.md](CWC27-notes.md)
- GOA TSV: present - [genes/human/CWC27/CWC27-goa.tsv](CWC27-goa.tsv)
- UniProt record: present - [genes/human/CWC27/CWC27-uniprot.txt](CWC27-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/CWC27.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/CWC27.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CWC27.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CWC27.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: CWC27 (also known as NY-CO-10 and SDCCAG10) is a nuclear, spliceosome-associated protein of the cyclophilin-type peptidyl-prolyl isomerase (PPIase) family. It has an N-terminal cyclophilin-like domain followed by a long disordered, partly coiled-coil C-terminal region. Although it belongs to the cyclophilin family, the CWC27 cyclophilin domain is a degenerate (catalytically inactive) pseudo-enzyme: it carries a glutamate in place of a conserved active-site residue and shows no detectable peptidyl-prolyl cis-trans isomerase activity and no cyclosporin binding. Functionally, CWC27 is a structural/scaffold component of the spliceosome. It is recruited during spliceosome activation as part of the activated Bact complex of the major (U2-type) spliceosome and is among the first factors released during the Bact-to-B* transition; it is also a component of the activated minor (U12-type) spliceosome, contributing to splicing of U12-type introns. In the major spliceosome the endonuclease-like domain of PRP8 contacts CWC27, and CWC27 works with its partner CWC22 in pre-mRNA splicing and exon junction complex deposition. Biallelic loss-of-function variants in CWC27 cause autosomal-recessive retinitis pigmentosa with or without skeletal and other developmental anomalies (RPSKA), underscoring its essential role in pre-mRNA splicing.
- Existing/core annotation action counts: ACCEPT: 12; KEEP_AS_NON_CORE: 3; MARK_AS_OVER_ANNOTATED: 1

## PN Consistency Summary

- **Consistency:** CONTRADICTION. PN classifies CWC27 as an active cyclophilin-type peptidyl-prolyl isomerase and propagates GO:0003755 PPIase activity. But the review, UniProt CAUTION, and the GOA all establish CWC27 is a catalytically DEAD pseudo-PPIase: GOA carries GO:0003755 as **NOT|enables** (IDA, PMID:20676357 — no isomerase activity, no cyclosporin binding, Glu at a conserved active-site position). The PN-projected positive GO:0003755 directly contradicts the curated negated annotation.
- **PN story / NEW pressure:** PN asserts PPIase catalysis that the gene-level evidence refutes. GO:0003755 is a real term (it is in the GOA — negated). This is not an ADD candidate; it is a **family-membership over-reach** (IPR cyclophilin signature ignores loss of catalytic residues). The review's true core is structural/scaffold spliceosome membership (GO:0000398 mRNA splicing, GO:0071005 U2-type precatalytic spliceosome, GO:0005681) — a different branch entirely from "folding enzyme."
- **Evidence alignment:** PN row references "17588513 rev"-style entries are absent for CWC27 (dossier shows no titles). Review evidence (PMID:20676357 dead-PPIase; PMID:29360106, PMID:33509932, PMID:39068178 spliceosome cryo-EM; PMID:28285769 disease) is all spliceosome/pseudoenzyme. The PPIase-activity claim has no supporting paper for this gene; the only relevant paper (PMID:20676357) refutes it.
- **Verdict:** Inconsistent — PN propagates positive GO:0003755 PPIase activity onto a curated dead pseudo-enzyme that GOA annotates as NOT|GO:0003755. **Recommended edits:** [MAP] exclude CWC27 from the cyclophilin-type GO:0003755 propagation (CWC27 is a catalytically inactive pseudo-PPIase; GOA = NOT|GO:0003755, PMID:20676357); represent CWC27 via its scaffold/spliceosome role instead.

## Full Consistency Review

- **UniProt:** Q6UX04 · **batch:** proteostasis-batch-2026-06-07 · **review status:** COMPLETE
- **PN placement:** `Cytonuclear proteostasis | Folding enzyme | Peptidyl-prolyl isomerases | Cyclophilin type` ; **PN-node mapping:** group AND type both mapped, scope=ok_for_propagation_to_go, GO:0003755 peptidyl-prolyl cis-trans isomerase activity (class/branch = no_mapping)
- **Consistency:** CONTRADICTION. PN classifies CWC27 as an active cyclophilin-type peptidyl-prolyl isomerase and propagates GO:0003755 PPIase activity. But the review, UniProt CAUTION, and the GOA all establish CWC27 is a catalytically DEAD pseudo-PPIase: GOA carries GO:0003755 as **NOT|enables** (IDA, PMID:20676357 — no isomerase activity, no cyclosporin binding, Glu at a conserved active-site position). The PN-projected positive GO:0003755 directly contradicts the curated negated annotation.
- **PN story / NEW pressure:** PN asserts PPIase catalysis that the gene-level evidence refutes. GO:0003755 is a real term (it is in the GOA — negated). This is not an ADD candidate; it is a **family-membership over-reach** (IPR cyclophilin signature ignores loss of catalytic residues). The review's true core is structural/scaffold spliceosome membership (GO:0000398 mRNA splicing, GO:0071005 U2-type precatalytic spliceosome, GO:0005681) — a different branch entirely from "folding enzyme."
- **Mapping strategy:** The Peptidyl-prolyl-isomerase group/type → GO:0003755 mapping is reasonable for active cyclophilins generally, but CWC27 is a pseudoenzyme exception and must NOT inherit the positive GO:0003755. Propagating it here would create a false-positive that conflicts with an existing NOT annotation — a worse outcome than the TOMM20/HSPA8 "too broad" cases. Recommend excluding CWC27 from this node's GO:0003755 propagation.
- **Evidence alignment:** PN row references "17588513 rev"-style entries are absent for CWC27 (dossier shows no titles). Review evidence (PMID:20676357 dead-PPIase; PMID:29360106, PMID:33509932, PMID:39068178 spliceosome cryo-EM; PMID:28285769 disease) is all spliceosome/pseudoenzyme. The PPIase-activity claim has no supporting paper for this gene; the only relevant paper (PMID:20676357) refutes it.
- **Verdict:** Inconsistent — PN propagates positive GO:0003755 PPIase activity onto a curated dead pseudo-enzyme that GOA annotates as NOT|GO:0003755. **Recommended edits:** [MAP] exclude CWC27 from the cyclophilin-type GO:0003755 propagation (CWC27 is a catalytically inactive pseudo-PPIase; GOA = NOT|GO:0003755, PMID:20676357); represent CWC27 via its scaffold/spliceosome role instead.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07
- review_yaml: genes/human/CWC27/CWC27-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Cytonuclear proteostasis | Folding enzyme | Peptidyl-prolyl isomerases | Cyclophilin type
- UniProt: Q6UX04
- In branches: CY
- PN-node mapping records (path + ancestors):
    - [type] Cytonuclear proteostasis|Folding enzyme|Peptidyl-prolyl isomerases|Cyclophilin type
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0003755 peptidyl-prolyl cis-trans isomerase activity]
        rationale: This PN type denotes cyclophilin-family peptidyl-prolyl isomerases. The matching GO molecular-function term is appropriate for propagation.
    - [group] Cytonuclear proteostasis|Folding enzyme|Peptidyl-prolyl isomerases
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0003755 peptidyl-prolyl cis-trans isomerase activity]
        rationale: This PN group is the cytonuclear peptidyl-prolyl isomerase branch. The matching GO molecular-function term is appropriate for propagation.
    - [class] Cytonuclear proteostasis|Folding enzyme
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a specific GO class. The member genes span multiple activities, complexes, or contexts, so propagation from this node would overstate the shared biology; use narrower child or gene-level curations.
    - [branch] Cytonuclear proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (2)
- GO:0003755 peptidyl-prolyl cis-trans isomerase activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Cytonuclear proteostasis|Folding enzyme|Peptidyl-prolyl isomerases
- GO:0003755 peptidyl-prolyl cis-trans isomerase activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Cytonuclear proteostasis|Folding enzyme|Peptidyl-prolyl isomerases|Cyclophilin type

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
