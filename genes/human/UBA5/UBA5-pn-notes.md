# UBA5 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9GZZ9
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07c
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/UBA5/UBA5-ai-review.yaml](UBA5-ai-review.yaml)
- AIGR review HTML: present - [genes/human/UBA5/UBA5-ai-review.html](UBA5-ai-review.html)
- Gene notes: present - [genes/human/UBA5/UBA5-notes.md](UBA5-notes.md)
- GOA TSV: present - [genes/human/UBA5/UBA5-goa.tsv](UBA5-goa.tsv)
- UniProt record: present - [genes/human/UBA5/UBA5-uniprot.txt](UBA5-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/UBA5.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/UBA5.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/UBA5.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/UBA5.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: UBA5 (ubiquitin-like modifier-activating enzyme 5) is the E1-activating enzyme of the ufmylation pathway, the first and rate-limiting step in conjugation of the ubiquitin-like modifier UFM1 to substrate proteins. UBA5 is a minimalistic, single-domain (ThiF/MoeB-type adenylation domain) E1 that functions as a homodimer. It activates mature UFM1 by adenylating UFM1's C-terminal glycine with ATP and then forming a high-energy thioester between that glycine and the catalytic cysteine (Cys250), releasing AMP. UFM1 is bound in trans across the two subunits of the UBA5 homodimer, and activated UFM1 is then transferred to the E2-conjugating enzyme UFC1 via UBA5's C-terminal UFC1-binding sequence. UBA5 binds zinc and uses a UFM1-interacting sequence (UIS) that also engages GABARAP/LC3 family proteins, which recruit UBA5 to the ER membrane. Acting at the cytosol and ER, UBA5-initiated ufmylation supports ribosome recycling, the response to ER stress, reticulophagy, the DNA-damage response, innate-immune (RIG-I/interferon) signaling, and erythroid/megakaryocyte differentiation. Biallelic UBA5 loss-of-function variants cause developmental and epileptic encephalopathy (DEE44) and autosomal-recessive spinocerebellar ataxia (SCAR24).
- Existing/core annotation action counts: ACCEPT: 33; KEEP_AS_NON_CORE: 33; MODIFY: 1

## PN Consistency Summary

- **Consistency:** Strong. Notes/review/PN agree UBA5 is the UFM1 E1 (adenylation + Cys250 thioester, homodimer). Review ACCEPTs GO:0071566 (UFM1 activating enzyme activity, IDA x5), GO:0071569, ER membrane and cytosol; MODIFY on GO:0008641→GO:0071566. Reticulophagy KEEP_AS_NON_CORE present in GOA. No contradictions.
- **PN story / NEW pressure:** Everything the PN asserts (UFM1 activation, ufmylation, ERphagy) is already in GOA/review. GO:0006515 (verified) projected new_to_goa for the RQC group is broad; UBA5's RQC contribution is via ufmylation (GO:0071569) which is annotated. Conclusion: **already captured**; GO:0006515 over-reaches as a direct UBA5 annotation.
- **Evidence alignment:** PN row 2 cites the ER-phagy screen (PMID:32160526, in GOA as IDA for reticulophagy); review uses UniProt + cascade PMIDs (15071506 etc.). Overlap on the ufmylation/ERphagy evidence; PN E1 row is domain-signature only (IPR000594).
- **Verdict:** Consistent and complete; PN UFMylation/E1/ERphagy story fully captured. Specific GO:0071566 should be preferred over the PN's broad GO:0008641 at gene level; GO:0006515 not warranted as a direct add.

## Full Consistency Review

- **UniProt:** Q9GZZ9 · **batch:** proteostasis-batch-2026-06-07c · **review status:** complete (E1 core function + homodimerization; many protein-binding rows triaged)
- **PN placement:** `Translation|Cytosolic translation|Ribosome-associated QC|UFMylation`; `ALP|...|ERphagy|UFMylation of ER proteins`; `UPS|E1 activating enzymes|activation of UFM1` ; **PN-node mapping:** UFMylation type→GO:0071569; ERphagy→GO:0061709; E1 group→GO:0008641 (broad UBL E1 activity); RQC group→GO:0006515.
- **Consistency:** Strong. Notes/review/PN agree UBA5 is the UFM1 E1 (adenylation + Cys250 thioester, homodimer). Review ACCEPTs GO:0071566 (UFM1 activating enzyme activity, IDA x5), GO:0071569, ER membrane and cytosol; MODIFY on GO:0008641→GO:0071566. Reticulophagy KEEP_AS_NON_CORE present in GOA. No contradictions.
- **PN story / NEW pressure:** Everything the PN asserts (UFM1 activation, ufmylation, ERphagy) is already in GOA/review. GO:0006515 (verified) projected new_to_goa for the RQC group is broad; UBA5's RQC contribution is via ufmylation (GO:0071569) which is annotated. Conclusion: **already captured**; GO:0006515 over-reaches as a direct UBA5 annotation.
- **Mapping strategy:** Distinguish specific from broad MF — PN E1-group projects the broad GO:0008641 (ubiquitin-like modifier activating enzyme activity); the review correctly prefers the specific GO:0071566 (UFM1 activating enzyme activity) and even MODIFIES the IEA GO:0008641 toward it. PN should keep GO:0008641 as the safe group-level term but acknowledge the gene-level specific term is GO:0071566 (precedent: broader parents not propagated over specific). UBA5 does not change the node.
- **Evidence alignment:** PN row 2 cites the ER-phagy screen (PMID:32160526, in GOA as IDA for reticulophagy); review uses UniProt + cascade PMIDs (15071506 etc.). Overlap on the ufmylation/ERphagy evidence; PN E1 row is domain-signature only (IPR000594).
- **Verdict:** Consistent and complete; PN UFMylation/E1/ERphagy story fully captured. Specific GO:0071566 should be preferred over the PN's broad GO:0008641 at gene level; GO:0006515 not warranted as a direct add.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/UBA5/UBA5-ai-review.yaml
- PN workbook rows: 3

## PN row 1: Translation | Cytosolic translation | Ribosome-associated QC | UFMylation
- UniProt: Q9GZZ9
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
- UniProt: Q9GZZ9
- In branches: TR, ALP, UPS
- Notes: E1-type protein that catalyzes UFMylation. Knockdown of UFL1 decreased DDRGK1 levels and inhibits ER-phagy.UFL1 UFMylates RPN1 and RPL26 to target ER sheets for degradation.
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

## PN row 3: Ubiquitin Proteasome System | E1 activating enzymes | activation of UFM1
- UniProt: Q9GZZ9
- In branches: TR, ALP, UPS
- Signature domains: IPR000594
- Auxiliary domains: (none)
- PN-node mapping records (path + ancestors):
    - [group] Ubiquitin Proteasome System|E1 activating enzymes|activation of UFM1
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0008641 ubiquitin-like modifier activating enzyme activity]
        rationale: This PN group represents E1 activation of the UFM1 modifier family. The generic GO activating enzyme activity term is the safest propagation target.
    - [class] Ubiquitin Proteasome System|E1 activating enzymes
        status=context_only scope=too_broad_to_propagate GO=[GO:0008641 ubiquitin-like modifier activating enzyme activity]
        rationale: This class is a real ubiquitin-like modifier E1 context, but it spans ubiquitin, SUMO, NEDD8, UFM1, URM1, ISG15, FAT10, and autophagy modifiers. Propagation is safer from the curated child groups.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (5)
- GO:0006515 protein quality control for misfolded or incompletely synthesized proteins | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Ribosome-associated QC
- GO:0071569 protein ufmylation | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Translation|Cytosolic translation|Ribosome-associated QC|UFMylation
- GO:0061709 reticulophagy | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy|ERphagy
- GO:0061709 reticulophagy | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy|ERphagy|UFMylation of ER proteins
- GO:0008641 ubiquitin-like modifier activating enzyme activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|E1 activating enzymes|activation of UFM1

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
