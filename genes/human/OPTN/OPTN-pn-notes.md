# OPTN PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q96CV9
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-14
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/OPTN/OPTN-ai-review.yaml](OPTN-ai-review.yaml)
- AIGR review HTML: missing - genes/human/OPTN/OPTN-ai-review.html
- Gene notes: present - [genes/human/OPTN/OPTN-notes.md](OPTN-notes.md)
- GOA TSV: present - [genes/human/OPTN/OPTN-goa.tsv](OPTN-goa.tsv)
- UniProt record: present - [genes/human/OPTN/OPTN-uniprot.txt](OPTN-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/OPTN.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/OPTN.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/OPTN.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/OPTN.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: Optineurin (OPTN) is a ubiquitously expressed, predominantly cytoplasmic coiled-coil adaptor protein that functions as a selective autophagy receptor. It carries two functional cargo-recognition modules: an LC3-interacting region (LIR motif, residues 176-181, with the critical Phe178) that binds ATG8-family modifiers (MAP1LC3A/B, GABARAP, GABARAPL1, GABARAPL2), and a UBAN (ubiquitin binding in ABIN and NEMO) motif (residues 474-479, with the essential Asp474/Phe475) that binds linear (M1) and K63-linked polyubiquitin chains. By simultaneously engaging ubiquitinated cargo and ATG8 proteins on the nascent autophagosomal membrane, OPTN bridges cargo to the autophagy machinery. Its C-terminus contains a CCHC NOA-type zinc finger (residues 547-577) that coordinates Zn2+. OPTN partners with and is activated by the kinase TBK1, which phosphorylates OPTN at Ser177 adjacent to the LIR, markedly increasing LC3 binding affinity and thereby driving cargo-selective autophagy. Through this mechanism OPTN mediates antibacterial xenophagy of ubiquitin-coated cytosolic bacteria (e.g. Salmonella) and PINK1/Parkin-dependent mitophagy of damaged mitochondria, acting alongside the related receptors SQSTM1/p62 and CALCOCO2/NDP52. As a NEMO-related protein, OPTN also regulates innate immune and inflammatory signaling: it negatively regulates canonical NF-kB signaling (competing for polyubiquitin within the TNFR1 complex) and dampens virus-triggered IFN-beta induction, while recruiting and activating TBK1 at the Golgi after RNA-virus sensing. Independently, OPTN links myosin VI and GTP-Rab8 to the Golgi complex, contributing to Golgi ribbon organization, post-Golgi exocytosis, and Rab8/TBC1D17-dependent endocytic recycling (e.g. of the transferrin receptor). OPTN mutations cause primary open-angle glaucoma (GLC1E; e.g. E50K), normal-pressure glaucoma, and amyotrophic lateral sclerosis with or without frontotemporal dementia (ALS12; e.g. the UBAN mutant E478G and the truncation Q398X), linking impaired selective autophagy and vesicular trafficking to neurodegeneration.
- Existing/core annotation action counts: ACCEPT: 22; KEEP_AS_NON_CORE: 71

## PN Consistency Summary

- **Consistency:** Strong on mitophagy + xenophagy. Deep research/notes (Wild 2011 PMID:21617041 Salmonella/TBK1-S177; Wong&Holzbaur 2014 PMID:25294927 Parkin mitophagy, UBAN E478G) match review. Review uses **more specific terms than PN**: GO:0061734 type 2 mitophagy (IMP; verified child of GO:0000423) and GO:1904417 positive regulation of xenophagy (IMP) — both already in GOA. One divergence: PN row 3 projects GO:0035973 aggrephagy as new_to_goa, but neither the review nor the notes assert OPTN aggrephagy — the notes/refs document mitophagy and xenophagy, not aggregate clearance.
- **PN story / NEW pressure:** PN's mitophagy/xenophagy are already captured (more precisely) — not new pressure. The only genuinely NEW PN assertion is aggrephagy (GO:0035973). This **over-reaches** on current OPTN evidence: aggrephagy appears to be carried over from the generic "Selective autophagy receptor" group notes (shared verbatim across receptors) rather than OPTN-specific data. Candidate at best; do not ADD without OPTN-specific aggrephagy evidence.
- **Evidence alignment:** Excellent overlap on the two shared papers (21617041, 25294927). No paper supports the PN aggrephagy leaf.
- **Verdict:** CONSISTENT on mitophagy/xenophagy (review more specific); PN aggrephagy (GO:0035973) over-reaches / likely group-note carryover. **Recommended edits:** [MAP] reconsider OPTN membership in the Aggrephagy receptor leaf (GO:0035973 new_to_goa) — unsupported by OPTN-specific evidence; demote to context or drop.

## Full Consistency Review

- **UniProt:** Q96CV9 (optineurin) · **batch:** proteostasis-batch-2026-06-14 · **review status:** COMPLETE (~1708 lines)
- **PN placement:** ALP `Autophagy substrate selection|Selective autophagy receptor|{Mitophagy,Xenophagy,Aggrephagy}` + UPS `Ubiquitin and UBL binding|trafficking|selective autophagy|UBAN, NEMO-type ZnF` ; **PN-node mapping:** Mitophagy→GO:0000423 (entailed_by_goa_closure), Xenophagy→GO:0098792 (supported_by_goa_regulation), Aggrephagy→GO:0035973 (new_to_goa); ancestors no_mapping/context_only.
- **Consistency:** Strong on mitophagy + xenophagy. Deep research/notes (Wild 2011 PMID:21617041 Salmonella/TBK1-S177; Wong&Holzbaur 2014 PMID:25294927 Parkin mitophagy, UBAN E478G) match review. Review uses **more specific terms than PN**: GO:0061734 type 2 mitophagy (IMP; verified child of GO:0000423) and GO:1904417 positive regulation of xenophagy (IMP) — both already in GOA. One divergence: PN row 3 projects GO:0035973 aggrephagy as new_to_goa, but neither the review nor the notes assert OPTN aggrephagy — the notes/refs document mitophagy and xenophagy, not aggregate clearance.
- **PN story / NEW pressure:** PN's mitophagy/xenophagy are already captured (more precisely) — not new pressure. The only genuinely NEW PN assertion is aggrephagy (GO:0035973). This **over-reaches** on current OPTN evidence: aggrephagy appears to be carried over from the generic "Selective autophagy receptor" group notes (shared verbatim across receptors) rather than OPTN-specific data. Candidate at best; do not ADD without OPTN-specific aggrephagy evidence.
- **Mapping strategy:** Mappings reasonable but the aggrephagy leaf membership for OPTN looks like a group-note artifact. TOMM20/HSPA8/RAB7A precedent: review's GO:0061734/GO:1904417 (narrower) are preferred over PN's broader GO:0000423/GO:0098792 — review is already better. KEY PATTERN: review keeps ~40 IPI protein binding non-core and uses GO:0030674 adaptor as core MF (not GO:0160247, but functionally equivalent elevation).
- **Evidence alignment:** Excellent overlap on the two shared papers (21617041, 25294927). No paper supports the PN aggrephagy leaf.
- **Verdict:** CONSISTENT on mitophagy/xenophagy (review more specific); PN aggrephagy (GO:0035973) over-reaches / likely group-note carryover. **Recommended edits:** [MAP] reconsider OPTN membership in the Aggrephagy receptor leaf (GO:0035973 new_to_goa) — unsupported by OPTN-specific evidence; demote to context or drop.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-14
- review_yaml: genes/human/OPTN/OPTN-ai-review.yaml
- PN workbook rows: 4

## PN row 1: Autophagy-Lysosome Pathway | Autophagy substrate selection | Selective autophagy receptor | Mitophagy
- UniProt: Q96CV9
- In branches: ALP, UPS
- Notes: Receptor for selective autophagy. Binds to ATG8 and ubiquitinated or degron-contaning substrates. Active in aggrephagy, Ub-dependent mitophagy, xenophagy. Can bind specifically to PINK1 to mediate parkin-mediated mitophagy. In xenophagy, its phosphorylation by TANK binding kinase 1 at serine-177 enhances its LC3 binding affinity and promoted selective autophagy of ubiquitin-coated cytosolic Salmonella enterica.
- PN references (titles):
    - Selective Autophagy: ATG8 Family Proteins, LIR Motifs and Cargo Receptors - ScienceDirect
    - The ubiquitin kinase PINK1 recruits autophagy receptors to induce mitophagy
    - Phosphorylation of the Autophagy Receptor Optineurin Restricts Salmonella Growth
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Mitophagy
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0000423 mitophagy]
        rationale: This PN path denotes selective-autophagy receptors for mitochondrial cargo. The source category is a mechanistic sub-role within mitophagy, so propagation rather than exact equivalence is the correct scope.
    - [group] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagy substrate selection
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad substrate-selection container. GO has useful targets for specific receptor, cargo-adaptor, and selective-autophagy leaves, but this class mixes marking, recognition, receptor regulation, and unknown roles and should not propagate as one term.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 2: Autophagy-Lysosome Pathway | Autophagy substrate selection | Selective autophagy receptor | Xenophagy
- UniProt: Q96CV9
- In branches: ALP, UPS
- Notes: Receptor for selective autophagy. Binds to ATG8 and ubiquitinated or degron-contaning substrates. Active in aggrephagy, Ub-dependent mitophagy, xenophagy. Can bind specifically to PINK1 to mediate parkin-mediated mitophagy. In xenophagy, its phosphorylation by TANK binding kinase 1 at serine-177 enhances its LC3 binding affinity and promoted selective autophagy of ubiquitin-coated cytosolic Salmonella enterica.
- PN references (titles):
    - Selective Autophagy: ATG8 Family Proteins, LIR Motifs and Cargo Receptors - ScienceDirect
    - The ubiquitin kinase PINK1 recruits autophagy receptors to induce mitophagy
    - Phosphorylation of the Autophagy Receptor Optineurin Restricts Salmonella Growth
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Xenophagy
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0098792 xenophagy]
        rationale: This PN category captures receptors for selective autophagy of pathogens or pathogen-derived material. The receptor class is narrower than the GO xenophagy process, so this is a propagation mapping.
    - [group] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagy substrate selection
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad substrate-selection container. GO has useful targets for specific receptor, cargo-adaptor, and selective-autophagy leaves, but this class mixes marking, recognition, receptor regulation, and unknown roles and should not propagate as one term.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 3: Autophagy-Lysosome Pathway | Autophagy substrate selection | Selective autophagy receptor | Aggrephagy
- UniProt: Q96CV9
- In branches: ALP, UPS
- Notes: Receptor for selective autophagy. Binds to ATG8 and ubiquitinated or degron-contaning substrates. Active in aggrephagy, Ub-dependent mitophagy, xenophagy. Can bind specifically to PINK1 to mediate parkin-mediated mitophagy. In xenophagy, its phosphorylation by TANK binding kinase 1 at serine-177 enhances its LC3 binding affinity and promoted selective autophagy of ubiquitin-coated cytosolic Salmonella enterica.
- PN references (titles):
    - Selective Autophagy: ATG8 Family Proteins, LIR Motifs and Cargo Receptors - ScienceDirect
    - The ubiquitin kinase PINK1 recruits autophagy receptors to induce mitophagy
    - Phosphorylation of the Autophagy Receptor Optineurin Restricts Salmonella Growth
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Aggrephagy
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0035973 aggrephagy]
        rationale: This PN path denotes receptors that recognize aggregation cargo for the aggrephagy pathway. The category is not identical to the GO process term, but propagation to aggrephagy is appropriate because membership in this receptor class implies direct participation in that process.
    - [group] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagy substrate selection
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad substrate-selection container. GO has useful targets for specific receptor, cargo-adaptor, and selective-autophagy leaves, but this class mixes marking, recognition, receptor regulation, and unknown roles and should not propagate as one term.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 4: Ubiquitin Proteasome System | Ubiquitin and UBL binding | trafficking | selective autophagy | UBAN, NEMO-type ZnF
- UniProt: Q96CV9
- In branches: ALP, UPS
- Signature domains: IPR032419, IPR034735
- Auxiliary domains: (none)
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|Ubiquitin and UBL binding|trafficking|selective autophagy|UBAN, NEMO-type ZnF
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a selective-autophagy or trafficking subdivision under a UPS binding context. The autophagy context is real, but this node is too indirect for automatic GO propagation.
    - [type] Ubiquitin Proteasome System|Ubiquitin and UBL binding|trafficking|selective autophagy
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a UPS taxonomy container. Its descendants mix catalytic roles, complex membership, binding domains, regulators, adaptors, and substrate-context labels, so a single propagating GO assertion would overstate the shared biology.
    - [group] Ubiquitin Proteasome System|Ubiquitin and UBL binding|trafficking
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a UPS taxonomy container. Its descendants mix catalytic roles, complex membership, binding domains, regulators, adaptors, and substrate-context labels, so a single propagating GO assertion would overstate the shared biology.
    - [class] Ubiquitin Proteasome System|Ubiquitin and UBL binding
        status=context_only scope=too_broad_to_propagate GO=[GO:0140036 ubiquitin-modified protein reader activity]
        rationale: This class records ubiquitin/UBL-reader context, but the subtree mixes ubiquitin, SUMO, UBL-domain, domain-architecture, catalytic, signaling, trafficking, and nucleic-acid process buckets. It is useful context, not a safe direct propagation.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (3)
- GO:0000423 mitophagy | scope=ok_for_propagation_to_go | goa_status=entailed_by_goa_closure | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Mitophagy
- GO:0098792 xenophagy | scope=ok_for_propagation_to_go | goa_status=supported_by_goa_regulation | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Xenophagy
- GO:0035973 aggrephagy | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Aggrephagy

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
