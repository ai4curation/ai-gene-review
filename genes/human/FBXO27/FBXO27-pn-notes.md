# FBXO27 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q8NI29
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-13
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/FBXO27/FBXO27-ai-review.yaml](FBXO27-ai-review.yaml)
- AIGR review HTML: missing - genes/human/FBXO27/FBXO27-ai-review.html
- Gene notes: missing - genes/human/FBXO27/FBXO27-notes.md
- GOA TSV: present - [genes/human/FBXO27/FBXO27-goa.tsv](FBXO27-goa.tsv)
- UniProt record: present - [genes/human/FBXO27/FBXO27-uniprot.txt](FBXO27-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/FBXO27.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/FBXO27.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXO27.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXO27.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/FBXO27/FBXO27-deep-research-falcon.md](FBXO27-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: FBXO27 (FBG5, FBX27) is a member of the FBA/FBG (F-box-associated, "sugar recognition") subfamily of F-box proteins that act as the substrate-recognition receptor of SCF (SKP1-CUL1-F-box)-type E3 ubiquitin ligase complexes. Like its paralogs FBXO2, FBXO6, FBXO17 and FBXO44, FBXO27 contains an N-terminal F-box domain that docks the protein onto SKP1 (and thereby onto the CUL1-RBX1 catalytic core) and a C-terminal FBA/G domain that functions as a lectin, recognizing N-linked oligosaccharides on glycoproteins through a conserved hydrophobic pocket (the aromatic Phe-Trp pair at positions 262-263 is required for high-affinity glycan binding). As an F-box protein, FBXO27 has no intrinsic catalytic activity; it confers substrate specificity to the assembled SCF complex, in which the RING subunit RBX1 recruits the ubiquitin-charged E2 enzyme and catalyzes ubiquitin transfer onto the bound glycoprotein. By binding glycans normally hidden inside the secretory pathway, FBXO27 contributes to recognition of N-glycosylated proteins that become aberrantly exposed to the cytosol. Its best-characterized cellular role is in the endo-lysosomal damage response: unlike its mostly cytosolic paralogs, FBXO27 is N-terminally myristoylated and membrane-associated, and after lysosomal membrane rupture it is recruited to damaged lysosomes where luminal glycans become exposed to the cytosol. There SCF(FBXO27) ubiquitinates the exposed luminal glycans of lysosomal membrane glycoproteins, most prominently LAMP2 (and LAMP1) along with other candidate damaged-lysosome glycoproteins, triggering recruitment of the autophagy adaptors p62/SQSTM1 and LC3 and promoting selective autophagy of the damaged lysosome (lysophagy). This couples a physical damage cue (cytosolic glycan exposure) to ubiquitin signaling and autophagic clearance; the same LAMP2-directed activity has been implicated in cardiomyocyte and neuronal autophagy/lysosomal quality control. FBXO27 may also act on misfolded glycoproteins retrotranslocated from the ER, but it contributes only partially to lysosomal ubiquitylation and shows cell-type-specific (brain, heart, kidney) expression, consistent with redundancy among lysophagy E3 ligases.
- Existing/core annotation action counts: ACCEPT: 16; KEEP_AS_NON_CORE: 6; MODIFY: 1

## PN Consistency Summary

- **Consistency:** Good, with a deliberate divergence. As an FBA/FBG lectin F-box, the review (correctly) does NOT make GO:1990756 the core MF; instead core MF = GO:0030246 carbohydrate binding (+ proposed GO:0005537 D-mannose binding), with GO:0006516 glycoprotein catabolic process and lysophagy as core BP. Deep research (Yoshida/Fbs3 lysophagy of LAMP2/LAMP1), UniProt (2008 lectin/SCF data), and GOA agree. The contributes_to GO:0061630 IBA is reasonably kept non-core. No internal contradictions.
- **PN story / NEW pressure:** PN's generic GO:1990756 adaptor target does NOT match this gene's informative MF (glycan binding) — a known special case the prompt flagged. Review adds the lysophagy/damaged-lysosome-glycoprotein role (LAMP2/LAMP1, p62/LC3, N-myristoylation) absent from GOA. KEY ISSUE: review proposes "lysophagy" as a NEW term, but **GO:0062093 lysophagy already exists** (verified; child of GO:0016236 macroautophagy, def. "selective autophagy…damaged lysosome…by macroautophagy"). So this is ALREADY CAPTURED in GO, not new. Also GO:0097466 "ubiquitin-dependent glycoprotein ERAD pathway" exists as a more specific option than the ERAD IBA.
- **Evidence alignment:** PN cites only "15340381 / rev". Review anchored on PMID:18203720 (FBA lectin family, full text) + Falcon (Yoshida PNAS lysophagy) + PMID:34445249. PN reference disjoint from review's; review evidence is far richer and substrate-validated.
- **Verdict:** CONSISTENT (with lectin caveat); ONE FIX — replace the proposed-new "lysophagy" with existing GO:0062093.

## Full Consistency Review

- **UniProt:** Q8NI29 · **batch:** proteostasis-batch-2026-06-13 · **review status:** COMPLETE (well-developed; SPECIAL CASE — lectin F-box)
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|FBA` (aux domain IPR007397) ; **PN-node mapping:** group=mapped GO:1990756; subtype/type/branch=no_mapping; class=context_only (GO:0061630).
- **Consistency:** Good, with a deliberate divergence. As an FBA/FBG lectin F-box, the review (correctly) does NOT make GO:1990756 the core MF; instead core MF = GO:0030246 carbohydrate binding (+ proposed GO:0005537 D-mannose binding), with GO:0006516 glycoprotein catabolic process and lysophagy as core BP. Deep research (Yoshida/Fbs3 lysophagy of LAMP2/LAMP1), UniProt (2008 lectin/SCF data), and GOA agree. The contributes_to GO:0061630 IBA is reasonably kept non-core. No internal contradictions.
- **PN story / NEW pressure:** PN's generic GO:1990756 adaptor target does NOT match this gene's informative MF (glycan binding) — a known special case the prompt flagged. Review adds the lysophagy/damaged-lysosome-glycoprotein role (LAMP2/LAMP1, p62/LC3, N-myristoylation) absent from GOA. KEY ISSUE: review proposes "lysophagy" as a NEW term, but **GO:0062093 lysophagy already exists** (verified; child of GO:0016236 macroautophagy, def. "selective autophagy…damaged lysosome…by macroautophagy"). So this is ALREADY CAPTURED in GO, not new. Also GO:0097466 "ubiquitin-dependent glycoprotein ERAD pathway" exists as a more specific option than the ERAD IBA.
- **Mapping strategy:** Node mapping is fine for the family, but PN's GO:1990756 over-reaches/under-describes FBXO27 specifically — glycan binding is the real MF. Reviewer already handled this at the gene level (MODIFY protein-binding → carbohydrate binding). No node change needed; flag FBXO27 as the lectin exception to the GO:1990756 default.
- **Evidence alignment:** PN cites only "15340381 / rev". Review anchored on PMID:18203720 (FBA lectin family, full text) + Falcon (Yoshida PNAS lysophagy) + PMID:34445249. PN reference disjoint from review's; review evidence is far richer and substrate-validated.
- **Verdict:** CONSISTENT (with lectin caveat); ONE FIX — replace the proposed-new "lysophagy" with existing GO:0062093.
- **Recommended edits:** [YAML] In FBXO27-ai-review.yaml, replace the `proposed_new_terms` "lysophagy" entry with a reference to existing **GO:0062093 lysophagy** (verified real), and set core_function #3 `directly_involved_in` to GO:0062093 (more specific than GO:0016236 macroautophagy). [YAML] Optionally MODIFY the ERAD IBA (GO:0036503) toward **GO:0097466 ubiquitin-dependent glycoprotein ERAD pathway** if retained.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-13
- review_yaml: genes/human/FBXO27/FBXO27-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul1 substrate receptor | F-box | FBA
- UniProt: Q8NI29
- In branches: UPS
- Signature domains: IPR001810
- Auxiliary domains: IPR007397
- PN references (titles):
    - 15340381 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|FBA
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower substrate-receptor, adaptor, domain, or family subdivision already covered by the curated parent adaptor/receptor mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower substrate-receptor, adaptor, domain, or family subdivision already covered by the curated parent adaptor/receptor mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor
        status=mapped scope=ok_for_propagation_to_go GO=[GO:1990756 ubiquitin-like ligase-substrate adaptor activity]
        rationale: This PN group captures substrate receptors/adaptors for cullin/UBL ligase systems. The shared GO molecular-function target is ubiquitin-like ligase-substrate adaptor activity.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:1990756 ubiquitin-like ligase-substrate adaptor activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
