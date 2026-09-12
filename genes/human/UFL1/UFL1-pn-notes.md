# UFL1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: O94874
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07c
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/UFL1/UFL1-ai-review.yaml](UFL1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/UFL1/UFL1-ai-review.html](UFL1-ai-review.html)
- Gene notes: present - [genes/human/UFL1/UFL1-notes.md](UFL1-notes.md)
- GOA TSV: present - [genes/human/UFL1/UFL1-goa.tsv](UFL1-goa.tsv)
- UniProt record: present - [genes/human/UFL1/UFL1-uniprot.txt](UFL1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/UFL1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/UFL1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/UFL1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/UFL1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: UFL1 (E3 UFM1-protein ligase 1; also called Maxer, NLBP, RCAD, KIAA0776) is the E3 ligase of the UFM1 (ufmylation) cascade, which catalyzes covalent attachment of the ubiquitin-like modifier UFM1 to substrate lysines. UFL1 is the catalytic component of the UFM1 ribosome E3 ligase (UREL) complex together with its obligate cofactor DDRGK1/UFBP1 and CDK5RAP3; DDRGK1 tethers the complex to the endoplasmic-reticulum membrane. Acting as a non-canonical scaffold-type E3, UFL1 activates the E2 enzyme UFC1 to transfer UFM1 onto substrates. Its principal physiological substrate is the 60S ribosomal protein RPL26/uL24, where mono-ufmylation of RPL26 on ER-bound ribosomes weakens the junction between post-termination or stalled 60S subunits and SEC61 translocons, promoting release and recycling of the large subunit and supporting ribosome-associated protein quality control. UFL1 also drives reticulophagy (ER-phagy) and the response to ER stress through ufmylation of ER proteins such as CYB5R3 and RPN1, participates in the DNA-damage response (ufmylating histone H4 and MRE11 to promote ATM activation), and ufmylates additional substrates including TP53/p53, PD-L1 and PD-1, contributing to protein stabilization and immune regulation. UFL1 acts mainly at the ER membrane but is also recruited to sites of DNA damage in the nucleus.
- Existing/core annotation action counts: ACCEPT: 54; KEEP_AS_NON_CORE: 55; MARK_AS_OVER_ANNOTATED: 1

## PN Consistency Summary

- **Consistency:** Strong. Notes/review/PN agree UFL1 is the UFM1 E3 (UREL: UFL1+DDRGK1+CDK5RAP3; scaffold-type E3 activating UFC1; principal substrate RPL26 → 60S recycling). Review ACCEPTs GO:0061666 (UFM1 ligase activity, IDA x16), GO:0071568, GO:0071569, ER membrane; downstream DNA-damage/immune/ERphagy roles KEEP_AS_NON_CORE. No contradictions.
- **PN story / NEW pressure:** All PN assertions captured. GO:0006515 (verified) projected new_to_goa via RQC group is broad; UFL1's RQC role = ufmylation-driven 60S recycling (GO:0071569 annotated; review core_function explicitly describes RPL26→recycling). Conclusion: **already captured**; GO:0006515 over-reaches as a direct UFL1 term. (Note: the more specific GO:0072344 rescue-of-stalled-ribosome appears 4x in UFL1 GOA, a better fit than GO:0006515 if any RQC process were to be added.)
- **Evidence alignment:** PN E3 row cites PMID:20018847 (shared — review uses it 7x, in GOA as IDA for GO:0061666), plus 25852645 and 20368332 (not in review; family/review citations). Good core-evidence overlap on the E3-ligase identification paper.
- **Verdict:** Consistent and complete; PN E3/UFMylation/ERphagy story fully captured by GO:0061666 + GO:0071569. GO:0006515 broader than UFL1's already-annotated GO:0072344/GO:0071569 — not warranted as a direct add.

## Full Consistency Review

- **UniProt:** O94874 · **batch:** proteostasis-batch-2026-06-07c · **review status:** complete (core MF GO:0061666; large annotation set triaged)
- **PN placement:** `Translation|Cytosolic translation|Ribosome-associated QC|UFMylation`; `ALP|...|ERphagy|UFMylation of ER proteins`; `UPS|E3 ubiquitin and UBL ligases|UBL modifiers|UFMylation` ; **PN-node mapping:** UFMylation type→GO:0071569; ERphagy→GO:0061709; E3 class→GO:0061630 (context only); E3 UBL-modifier type→no_mapping.
- **Consistency:** Strong. Notes/review/PN agree UFL1 is the UFM1 E3 (UREL: UFL1+DDRGK1+CDK5RAP3; scaffold-type E3 activating UFC1; principal substrate RPL26 → 60S recycling). Review ACCEPTs GO:0061666 (UFM1 ligase activity, IDA x16), GO:0071568, GO:0071569, ER membrane; downstream DNA-damage/immune/ERphagy roles KEEP_AS_NON_CORE. No contradictions.
- **PN story / NEW pressure:** All PN assertions captured. GO:0006515 (verified) projected new_to_goa via RQC group is broad; UFL1's RQC role = ufmylation-driven 60S recycling (GO:0071569 annotated; review core_function explicitly describes RPL26→recycling). Conclusion: **already captured**; GO:0006515 over-reaches as a direct UFL1 term. (Note: the more specific GO:0072344 rescue-of-stalled-ribosome appears 4x in UFL1 GOA, a better fit than GO:0006515 if any RQC process were to be added.)
- **Mapping strategy:** PN node correctly leaves the E3 UBL-modifier type at no_mapping and the E3 class at context-only GO:0061630 (ubiquitin protein ligase activity) — appropriately broad, not propagated. The gene-level specific MF is GO:0061666 (review). UFL1 does not change the node.
- **Evidence alignment:** PN E3 row cites PMID:20018847 (shared — review uses it 7x, in GOA as IDA for GO:0061666), plus 25852645 and 20368332 (not in review; family/review citations). Good core-evidence overlap on the E3-ligase identification paper.
- **Verdict:** Consistent and complete; PN E3/UFMylation/ERphagy story fully captured by GO:0061666 + GO:0071569. GO:0006515 broader than UFL1's already-annotated GO:0072344/GO:0071569 — not warranted as a direct add.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/UFL1/UFL1-ai-review.yaml
- PN workbook rows: 3

## PN row 1: Translation | Cytosolic translation | Ribosome-associated QC | UFMylation
- UniProt: O94874
- In branches: TR, ALP, UPS
- PN-node mapping records (path + ancestors):
    - [type] Translation|Cytosolic translation|Ribosome-associated QC|UFMylation
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0071569 protein ufmylation]
        rationale: This PN RQC type denotes UFM1 conjugation in ribosome quality control. Protein ufmylation is the shared process target.
    - [group] Translation|Cytosolic translation|Ribosome-associated QC
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0006515 protein quality control for misfolded or incompletely synthesized proteins]
        rationale: The PN ribosome-associated quality-control group covers surveillance and disposal of stalled or defective nascent-chain translation products. GO lacks a dedicated ribosome-associated QC term in the local cache, so the broader protein-quality-control process is the best supported target.
    - [class] Translation|Cytosolic translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0002181 cytoplasmic translation]
        rationale: The PN class Cytosolic translation is centered on the cytoplasmic translation apparatus and process, but it also houses supporting machinery such as ribosome biogenesis factors. The GO process term is a useful high-level label for the class, but propagating it to all members would over-annotate genes whose PN placement is through assembly or maturation context rather than core cytoplasmic translation.
    - [branch] Translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0006412 translation]
        rationale: The PN Translation branch is organized around the translation apparatus and immediately associated cotranslational quality-control systems. GO translation is the closest high-level process label, but the PN branch also contains adjacent machinery such as ribosome biogenesis and nascent-chain handling. Keeping this relationship is useful for interpretation, but it is too broad to project safely onto every member.

## PN row 2: Autophagy-Lysosome Pathway | Autophagy substrate selection | Marking substrates for selective autophagy | ERphagy | UFMylation of ER proteins
- UniProt: O94874
- In branches: TR, ALP, UPS
- Notes: E3-type protein that catalyzes UFMylation. Knockdown of UFL1 decreased DDRGK1 levels and inhibits ER-phagy.UFL1 UFMylates RPN1 and RPL26 to target ER sheets for degradation.
- PN references (titles):
    - A Genome-wide ER-phagy Screen Highlights Key Roles of Mitochondrial Metabolism and ER-Resident UFMylation - ScienceDirect
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy|ERphagy|UFMylation of ER proteins
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061709 reticulophagy]
        rationale: This PN subtype captures a specific ER-cargo marking mechanism used in ERphagy. Because GO uses reticulophagy for ER autophagy, this subtype can propagate to reticulophagy.
    - [type] Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy|ERphagy
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061709 reticulophagy]
        rationale: The PN ERphagy marking category captures factors that mark ER cargo for selective autophagic turnover. GO uses reticulophagy for this pathway, so propagation to reticulophagy is appropriate.
    - [group] Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagy substrate selection
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad substrate-selection container. GO has useful targets for specific receptor, cargo-adaptor, and selective-autophagy leaves, but this class mixes marking, recognition, receptor regulation, and unknown roles and should not propagate as one term.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 3: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | UBL modifiers | UFMylation
- UniProt: O94874
- In branches: TR, ALP, UPS
- Signature domains: IPR056579
- Auxiliary domains: (none)
- PN references (titles):
    - 25852645
    - 20018847
    - 20368332
- PN-node mapping records (path + ancestors):
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|UBL modifiers|UFMylation
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a UBL-modifier subtype or architecture bucket. The subtree mixes catalytic ligases with cofactors/idiosyncratic contexts, so no direct GO propagation is made from this node.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|UBL modifiers
        status=context_only scope=too_broad_to_propagate GO=[GO:0019787 ubiquitin-like protein transferase activity]
        rationale: This group records UBL-modifier ligase context, but descendants include cofactors and idiosyncratic SUMOylation/ATGylation entries that are not uniformly transferase activities. Keep as context only.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (4)
- GO:0006515 protein quality control for misfolded or incompletely synthesized proteins | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Ribosome-associated QC
- GO:0071569 protein ufmylation | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Translation|Cytosolic translation|Ribosome-associated QC|UFMylation
- GO:0061709 reticulophagy | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy|ERphagy
- GO:0061709 reticulophagy | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy|ERphagy|UFMylation of ER proteins

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
