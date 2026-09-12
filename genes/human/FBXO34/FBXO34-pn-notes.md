# FBXO34 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9NWN3
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-13
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/FBXO34/FBXO34-ai-review.yaml](FBXO34-ai-review.yaml)
- AIGR review HTML: missing - genes/human/FBXO34/FBXO34-ai-review.html
- Gene notes: missing - genes/human/FBXO34/FBXO34-notes.md
- GOA TSV: present - [genes/human/FBXO34/FBXO34-goa.tsv](FBXO34-goa.tsv)
- UniProt record: present - [genes/human/FBXO34/FBXO34-uniprot.txt](FBXO34-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/FBXO34.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/FBXO34.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXO34.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXO34.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/FBXO34/FBXO34-deep-research-falcon.md](FBXO34-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: FBXO34 (F-box only protein 34, FBX34) is a 711-amino-acid F-box protein that serves as the substrate-recognition subunit of an SCF (SKP1-CUL1-F-box protein) E3 ubiquitin-protein ligase complex. Its C-terminal F-box domain (residues ~572-624) docks onto SKP1, linking the complex (via CUL1 and the catalytic RING subunit RBX1) to specific substrates that FBXO34 selects for K48-linked polyubiquitination and proteasomal degradation; FBXO34 itself is the substrate receptor and is not the catalytic core. Reported substrates and roles are still sparse: it promotes ubiquitination and degradation of the RNA- binding protein HNRNPU (hnRNP U), and through this can modulate latent HIV-1 reactivation. hnRNP U normally binds the HIV-1 mRNA Rev element region and suppresses HIV-1 translation to maintain latency; FBXO34-driven degradation of hnRNP U abolishes this interaction and relieves the translational block, so FBXO34 was identified in a CRISPR-activation screen as a host factor promoting latency reversal. By similarity to its rodent ortholog (where it localizes mainly to the nucleus and colocalizes with F-actin in oocytes) it has been implicated in cell-cycle control of the G2/M transition and anaphase entry in meiotic oocytes, acting upstream of CCNB1/MPF (Fbxo34 depletion lowers MPF activity and is rescued by exogenous CCNB1, whereas overexpression triggers spindle-assembly-checkpoint activation and metaphase-I arrest); a direct cell-cycle substrate has not been identified. Much of the N-terminal half of the protein is intrinsically disordered, and the protein is broadly expressed across tissues with low tissue specificity. Overall FBXO34 is a poorly characterized member of the large F-box protein family whose best-supported molecular function is acting as an SCF substrate-recognition adaptor.
- Existing/core annotation action counts: ACCEPT: 2; KEEP_AS_NON_CORE: 3

## PN Consistency Summary

- **Consistency:** Strong. Deep research (Falcon → HNRNPU substrate, HIV-1 latency reversal; mouse meiotic CCNB1/MPF role), UniProt and GOA agree on SCF substrate-receptor role. Review core MF = GO:1990756. No contradictions. PMID:36285453 (HNRNPU/HIV) verified, is the UniProt FUNCTION source.
- **PN story / NEW pressure:** PN asserts only the generic adaptor MF. Like FBXO33, FBXO34's GOA has NO ubiquitin-ligase/transferase MF to MODIFY — only protein binding IPI (mostly sticky Y2H KRTAPs), SCF complex CC and SCF catabolism BP (both NAS/ComplexPortal). So GO:1990756 is **inferred-only** here too, justified by the HNRNPU degradation evidence. Substrate repertoire thin (one human substrate); review correctly proposes no substrate-specific NEW terms (proposed_new_terms empty). Conclusion: PN adaptor claim = defensible ADD to GOA (GO:1990756 verified real); flag adaptor MF as inferred-only with a single validated substrate.
- **Evidence alignment:** PN cites only "15340381 / rev". Review anchored on PMID:36285453 (HNRNPU/HIV, verified) + Falcon (Yang 2022 human; Zhao 2021/Kinterova 2022 mouse meiosis, orthology-based UNVERIFIED) + interactome PMIDs + PMID:34445249. PN reference disjoint from review's.
- **Verdict:** CONSISTENT — no edits required; flag GO:1990756 core MF as inferred-only (one validated substrate, HNRNPU).

## Full Consistency Review

- **UniProt:** Q9NWN3 · **batch:** proteostasis-batch-2026-06-13 · **review status:** COMPLETE (developed; poorly characterized gene, sparse GOA)
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|other` ; **PN-node mapping:** group=mapped GO:1990756; subtype/type/branch=no_mapping; class=context_only (GO:0061630).
- **Consistency:** Strong. Deep research (Falcon → HNRNPU substrate, HIV-1 latency reversal; mouse meiotic CCNB1/MPF role), UniProt and GOA agree on SCF substrate-receptor role. Review core MF = GO:1990756. No contradictions. PMID:36285453 (HNRNPU/HIV) verified, is the UniProt FUNCTION source.
- **PN story / NEW pressure:** PN asserts only the generic adaptor MF. Like FBXO33, FBXO34's GOA has NO ubiquitin-ligase/transferase MF to MODIFY — only protein binding IPI (mostly sticky Y2H KRTAPs), SCF complex CC and SCF catabolism BP (both NAS/ComplexPortal). So GO:1990756 is **inferred-only** here too, justified by the HNRNPU degradation evidence. Substrate repertoire thin (one human substrate); review correctly proposes no substrate-specific NEW terms (proposed_new_terms empty). Conclusion: PN adaptor claim = defensible ADD to GOA (GO:1990756 verified real); flag adaptor MF as inferred-only with a single validated substrate.
- **Mapping strategy:** Correct; gene does not change the node. GO:1990756 equals the review's core MF and genuinely adds value (no MF in GOA). The large block of high-throughput protein-binding IPIs (KRTAPs, MTUS2, KRT40) are correctly kept non-core / flagged as likely non-physiological.
- **Evidence alignment:** PN cites only "15340381 / rev". Review anchored on PMID:36285453 (HNRNPU/HIV, verified) + Falcon (Yang 2022 human; Zhao 2021/Kinterova 2022 mouse meiosis, orthology-based UNVERIFIED) + interactome PMIDs + PMID:34445249. PN reference disjoint from review's.
- **Verdict:** CONSISTENT — no edits required; flag GO:1990756 core MF as inferred-only (one validated substrate, HNRNPU).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-13
- review_yaml: genes/human/FBXO34/FBXO34-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul1 substrate receptor | F-box | other
- UniProt: Q9NWN3
- In branches: UPS
- Signature domains: IPR001810
- Auxiliary domains: (none)
- PN references (titles):
    - 15340381 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|other
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
