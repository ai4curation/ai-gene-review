# NPLOC4 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q8TAT6
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07c
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/NPLOC4/NPLOC4-ai-review.yaml](NPLOC4-ai-review.yaml)
- AIGR review HTML: present - [genes/human/NPLOC4/NPLOC4-ai-review.html](NPLOC4-ai-review.html)
- Gene notes: present - [genes/human/NPLOC4/NPLOC4-notes.md](NPLOC4-notes.md)
- GOA TSV: present - [genes/human/NPLOC4/NPLOC4-goa.tsv](NPLOC4-goa.tsv)
- UniProt record: present - [genes/human/NPLOC4/NPLOC4-uniprot.txt](NPLOC4-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/NPLOC4.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/NPLOC4.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/NPLOC4.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/NPLOC4.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: NPLOC4 (Nuclear protein localization protein 4 homolog, NPL4) is an essential ubiquitin-binding cofactor of the AAA+ ATPase VCP/p97. With UFD1 it forms the obligate UFD1-NPL4 heterodimer, the principal substrate-recruiting adaptor of p97, generating the VCP-NPL4-UFD1 segregase complex. NPL4 binds polyubiquitin chains through its C-terminal RanBP2-type zinc finger and, together with UFD1, engages and unfolds the initiating ubiquitin to thread substrates into the p97 central pore. The complex extracts ubiquitinated proteins from membranes, chromatin, and macromolecular assemblies and delivers them for proteasomal degradation. It is central to endoplasmic-reticulum-associated degradation (ERAD), where it drives retrotranslocation of misfolded proteins from the ER to the cytosol, and it participates in many other p97-dependent processes including ribosome-associated quality control, spindle disassembly and nuclear-envelope reformation at the end of mitosis, and Golgi membrane reassembly. NPL4 also contributes to a non-canonical role of the p97 complex in innate immunity, acting as a negative regulator of type I interferon production by helping bind RIG-I (RIGI/DDX58) and recruit RNF125 for its ubiquitination and degradation. NPL4 contains an MPN(-like) domain, a ubiquitin-like region, and the RanBP2-type zinc finger, and localizes to the cytosol, the ER membrane and the nucleus.
- Existing/core annotation action counts: ACCEPT: 31; KEEP_AS_NON_CORE: 33

## PN Consistency Summary

- **Consistency:** Strong on the core, with one correctly-handled caveat. Review/notes and PN agree NPLOC4=NPL4, the ubiquitin-binding cofactor that with UFD1 forms the UFD1-NPL4 heterodimer / VCP-NPL4-UFD1 segregase, central to ERAD retrotranslocation and many p97 processes. The UPS DUB/MPN rows reflect NPLOC4's **non-catalytic MPN-like (pseudo-DUB)** domain; the PN correctly did NOT propagate DUB activity (GO:0101005) from these — consistent with the review, which asserts ubiquitin binding (GO:0043130) and ATPase binding (GO:0051117), NOT deubiquitinase activity. No contradiction.
- **PN story / NEW pressure:** Two relevant projections. (1) GO:0034098 and GO:0036503 are confirmed **already in GOA** (grep) and accepted in the review — already captured, no NEW pressure. (2) GO:0006515 (RQC group) is verified real, absent from NPLOC4 GOA, and NOT an ancestor of the review's existing RQC terms (GO:1990116/GO:0072344, NAS, kept non-core). So GO:0006515 would be an ADD; however the review treats p97-RQC as **one of many** p97 processes (non-core), so adding it as non-core is defensible but low priority. Conclusion: core p97/ERAD story fully captured; GO:0006515 a permissible non-core ADD, not over-reach.
- **Evidence alignment:** Concordant. PN rows 4-5 cite PMID:12370088 and PMID:28451587; review anchors complex/ERAD/RIG-I to PMID:11574150, PMID:25660456, PMID:26471729, PMID:28819009, RQC to PMID:35452614. Review independently caught PMID:39329031 as WRONG_IDENTIFIER (Morocco ID clinical study mis-attached by ComplexPortal) — a real citation defect the PN does not surface.
- **Verdict:** Consistent, high-quality; core captured, DUB correctly suppressed, one ComplexPortal mis-citation already flagged. **Recommended edits:** Optionally add GO:0006515 (involved_in, non-core) to mirror the RQC-group projection [YAML]; PMID:39329031 already flagged WRONG_IDENTIFIER on GO:0034098/GO:0043161/GO:1904949 — replace with a correct p97 complex reference [REF].

## Full Consistency Review

- **UniProt:** Q8TAT6 · **batch:** proteostasis-batch-2026-06-07c · **review status:** COMPLETE
- **PN placement:** 6 rows across ER, TR, UPS branches — ERAD (`ER proteostasis|...|ER associated degradation|VCP system for retrotranslocation in ERAD|VCP accessories`), RQC (`Translation|...|Ribosome-associated QC|Ubiquitin recognition`), and four UPS DUB/MPN-domain rows. **PN-node mapping:** ERAD group→GO:0036503 ERAD pathway (exact, already_in_goa); RQC group→GO:0006515 (ok_for_propagation, new_to_goa); VCP-associated subtype→GO:0034098 VCP-NPL4-UFD1 AAA ATPase complex (ok_for_propagation, already_in_goa); all DUB/MPN nodes→context_only/no_mapping (correctly suppressed).
- **Consistency:** Strong on the core, with one correctly-handled caveat. Review/notes and PN agree NPLOC4=NPL4, the ubiquitin-binding cofactor that with UFD1 forms the UFD1-NPL4 heterodimer / VCP-NPL4-UFD1 segregase, central to ERAD retrotranslocation and many p97 processes. The UPS DUB/MPN rows reflect NPLOC4's **non-catalytic MPN-like (pseudo-DUB)** domain; the PN correctly did NOT propagate DUB activity (GO:0101005) from these — consistent with the review, which asserts ubiquitin binding (GO:0043130) and ATPase binding (GO:0051117), NOT deubiquitinase activity. No contradiction.
- **PN story / NEW pressure:** Two relevant projections. (1) GO:0034098 and GO:0036503 are confirmed **already in GOA** (grep) and accepted in the review — already captured, no NEW pressure. (2) GO:0006515 (RQC group) is verified real, absent from NPLOC4 GOA, and NOT an ancestor of the review's existing RQC terms (GO:1990116/GO:0072344, NAS, kept non-core). So GO:0006515 would be an ADD; however the review treats p97-RQC as **one of many** p97 processes (non-core), so adding it as non-core is defensible but low priority. Conclusion: core p97/ERAD story fully captured; GO:0006515 a permissible non-core ADD, not over-reach.
- **Mapping strategy:** Well-judged across all 6 rows. Suppressing DUB propagation from the MPN/UBXL nodes (NPLOC4 is a pseudo-DUB) avoids a false catalytic claim; VCP-NPL4-UFD1 complex and ERAD are the safe targets. No node-mapping change warranted.
- **Evidence alignment:** Concordant. PN rows 4-5 cite PMID:12370088 and PMID:28451587; review anchors complex/ERAD/RIG-I to PMID:11574150, PMID:25660456, PMID:26471729, PMID:28819009, RQC to PMID:35452614. Review independently caught PMID:39329031 as WRONG_IDENTIFIER (Morocco ID clinical study mis-attached by ComplexPortal) — a real citation defect the PN does not surface.
- **Verdict:** Consistent, high-quality; core captured, DUB correctly suppressed, one ComplexPortal mis-citation already flagged. **Recommended edits:** Optionally add GO:0006515 (involved_in, non-core) to mirror the RQC-group projection [YAML]; PMID:39329031 already flagged WRONG_IDENTIFIER on GO:0034098/GO:0043161/GO:1904949 — replace with a correct p97 complex reference [REF].

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/NPLOC4/NPLOC4-ai-review.yaml
- PN workbook rows: 6

## PN row 1: ER proteostasis | Organelle-specific protein degradation | ER associated degradation | VCP system for retrotranslocation in ERAD | VCP accessories
- UniProt: Q8TAT6
- In branches: ER, TR, UPS
- PN-node mapping records (path + ancestors):
    - [subtype] ER proteostasis|Organelle-specific protein degradation|ER associated degradation|VCP system for retrotranslocation in ERAD|VCP accessories
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [type] ER proteostasis|Organelle-specific protein degradation|ER associated degradation|VCP system for retrotranslocation in ERAD
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0036503 ERAD pathway]
        rationale: This PN type captures the VCP/p97-dependent retrotranslocation machinery used in ERAD. It is not a separate process from ERAD, but a core mechanistic subsystem within it.
    - [group] ER proteostasis|Organelle-specific protein degradation|ER associated degradation
        status=mapped scope=exact GO=[GO:0036503 ERAD pathway]
        rationale: The PN group "ER associated degradation" is a direct lexical and biological match to the GO ERAD pathway term. The additional branch and class context disambiguates the source string from any broader degradation language.
    - [class] ER proteostasis|Organelle-specific protein degradation
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## PN row 2: Translation | Cytosolic translation | Ribosome-associated QC | Ubiquitin recognition
- UniProt: Q8TAT6
- In branches: ER, TR, UPS
- PN-node mapping records (path + ancestors):
    - [type] Translation|Cytosolic translation|Ribosome-associated QC|Ubiquitin recognition
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [group] Translation|Cytosolic translation|Ribosome-associated QC
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0006515 protein quality control for misfolded or incompletely synthesized proteins]
        rationale: The PN ribosome-associated quality-control group covers surveillance and disposal of stalled or defective nascent-chain translation products. GO lacks a dedicated ribosome-associated QC term in the local cache, so the broader protein-quality-control process is the best supported target.
    - [class] Translation|Cytosolic translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0002181 cytoplasmic translation]
        rationale: The PN class Cytosolic translation is centered on the cytoplasmic translation apparatus and process, but it also houses supporting machinery such as ribosome biogenesis factors. The GO process term is a useful high-level label for the class, but propagating it to all members would over-annotate genes whose PN placement is through assembly or maturation context rather than core cytoplasmic translation.
    - [branch] Translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0006412 translation]
        rationale: The PN Translation branch is organized around the translation apparatus and immediately associated cotranslational quality-control systems. GO translation is the closest high-level process label, but the PN branch also contains adjacent machinery such as ribosome biogenesis and nascent-chain handling. Keeping this relationship is useful for interpretation, but it is too broad to project safely onto every member.

## PN row 3: Ubiquitin Proteasome System | Ubiquitin and UBL proteins | UBL domain | DUB | MPN
- UniProt: Q8TAT6
- In branches: ER, TR, UPS
- Signature domains: IPR024682
- Auxiliary domains: IPR037518
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|Ubiquitin and UBL proteins|UBL domain|DUB|MPN
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower UBL-domain DUB subdivision. The domain architecture is not sufficient for propagation because the subtree includes noncatalytic MPN/UBL-domain cases; active DUB mappings are handled elsewhere.
    - [type] Ubiquitin Proteasome System|Ubiquitin and UBL proteins|UBL domain|DUB
        status=context_only scope=too_broad_to_propagate GO=[GO:0101005 deubiquitinase activity]
        rationale: This UBL-domain type is DUB-related context, but the subtree includes noncatalytic MPN/UBL-domain cases. Active DUB propagation is handled from the DUB-family branch.
    - [group] Ubiquitin Proteasome System|Ubiquitin and UBL proteins|UBL domain
        status=context_only scope=too_broad_to_propagate GO=[GO:0043130 ubiquitin binding]
        rationale: This group records UBL-domain protein context, but descendants include enzymes, adaptors, chaperone-related proteins, non-enzymatic proteins, and nucleic-acid factors. Propagation is restricted to narrower nodes.
    - [class] Ubiquitin Proteasome System|Ubiquitin and UBL proteins
        status=context_only scope=too_broad_to_propagate GO=[GO:0019787 ubiquitin-like protein transferase activity]
        rationale: This class groups ubiquitin, UBL modifiers, UBX/UBL-domain proteins, and UBL-containing enzymes. The branch is UPS-relevant but too mixed to propagate as a single GO annotation.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## PN row 4: Ubiquitin Proteasome System | DUBs and UBL demodifiers | JAMM / MPN | VCP-associated
- UniProt: Q8TAT6
- In branches: ER, TR, UPS
- Signature domains: IPR037518
- Auxiliary domains: IPR001876
- PN references (titles):
    - 12370088 / rev
- PN-node mapping records (path + ancestors):
    - [type] Ubiquitin Proteasome System|DUBs and UBL demodifiers|JAMM / MPN|VCP-associated
        status=no_mapping scope= GO=[]
        rationale: Reviewed manually as a UPS source node. No single GO term is appropriate for direct propagation from this PN label without narrower context or gene-level evidence.
    - [group] Ubiquitin Proteasome System|DUBs and UBL demodifiers|JAMM / MPN
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a UPS taxonomy container. Its descendants mix catalytic roles, complex membership, binding domains, regulators, adaptors, and substrate-context labels, so a single propagating GO assertion would overstate the shared biology.
    - [class] Ubiquitin Proteasome System|DUBs and UBL demodifiers
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a UPS taxonomy container. Its descendants mix catalytic roles, complex membership, binding domains, regulators, adaptors, and substrate-context labels, so a single propagating GO assertion would overstate the shared biology.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## PN row 5: Ubiquitin Proteasome System | VCP and associated proteins | associated DUBs | MPN | UBXL
- UniProt: Q8TAT6
- In branches: ER, TR, UPS
- Signature domains: PMID: 28451587 (UBXL)
- Auxiliary domains: IPR037518
- PN references (titles):
    - 28451587
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|VCP and associated proteins|associated DUBs|MPN|UBXL
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0034098 VCP-NPL4-UFD1 AAA ATPase complex]
        rationale: This PN subtype identifies NPLOC4 in the VCP-NPL4-UFD1 complex context. The safe GO target is VCP-NPL4-UFD1 AAA ATPase complex, not DUB activity.
    - [type] Ubiquitin Proteasome System|VCP and associated proteins|associated DUBs|MPN
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower VCP-associated DUB/adaptor subdivision. The VCP context includes both catalytic DUBs and noncatalytic complex members, so no additional direct DUB propagation is made from this node.
    - [group] Ubiquitin Proteasome System|VCP and associated proteins|associated DUBs
        status=context_only scope=too_broad_to_propagate GO=[GO:0101005 deubiquitinase activity]
        rationale: This VCP-associated group is DUB-related context, but it includes NPLOC4 complex membership as well as catalytic DUBs. Direct DUB propagation comes from the DUB-family branch or narrower reviewed nodes.
    - [class] Ubiquitin Proteasome System|VCP and associated proteins
        status=context_only scope=too_broad_to_propagate GO=[GO:0043335 protein unfolding]
        rationale: This class records the VCP segregase branch context, but descendants include VCP, substrate adaptors, DUBs, E3 ligases, channels, and unrelated associated enzymes. Direct propagation is restricted to narrower nodes.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## PN row 6: Ubiquitin Proteasome System | Ubiquitin and UBL binding | DUB | MPN & UBXL | RanBP2-type ZnF
- UniProt: Q8TAT6
- In branches: ER, TR, UPS
- Signature domains: IPR001876
- Auxiliary domains: IPR037518
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|Ubiquitin and UBL binding|DUB|MPN & UBXL|RanBP2-type ZnF
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower UBL-binding DUB-domain subdivision. Because this subtree includes noncatalytic or pseudo-DUB cases, active DUB propagation is handled by the DUB-family branch rather than this binding-domain node.
    - [type] Ubiquitin Proteasome System|Ubiquitin and UBL binding|DUB|MPN & UBXL
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower UBL-binding DUB-domain subdivision. Because this subtree includes noncatalytic or pseudo-DUB cases, active DUB propagation is handled by the DUB-family branch rather than this binding-domain node.
    - [group] Ubiquitin Proteasome System|Ubiquitin and UBL binding|DUB
        status=context_only scope=too_broad_to_propagate GO=[GO:0101005 deubiquitinase activity]
        rationale: This UBL-binding group is DUB-related context, but it includes noncatalytic or pseudo-DUB domain cases such as NPLOC4/USP39-like entries. Active DUB propagation is handled from the DUB-family branch.
    - [class] Ubiquitin Proteasome System|Ubiquitin and UBL binding
        status=context_only scope=too_broad_to_propagate GO=[GO:0140036 ubiquitin-modified protein reader activity]
        rationale: This class records ubiquitin/UBL-reader context, but the subtree mixes ubiquitin, SUMO, UBL-domain, domain-architecture, catalytic, signaling, trafficking, and nucleic-acid process buckets. It is useful context, not a safe direct propagation.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (4)
- GO:0036503 ERAD pathway | scope=exact | goa_status=already_in_goa_exact | from=ER proteostasis|Organelle-specific protein degradation|ER associated degradation
- GO:0036503 ERAD pathway | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=ER proteostasis|Organelle-specific protein degradation|ER associated degradation|VCP system for retrotranslocation in ERAD
- GO:0006515 protein quality control for misfolded or incompletely synthesized proteins | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Ribosome-associated QC
- GO:0034098 VCP-NPL4-UFD1 AAA ATPase complex | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|VCP and associated proteins|associated DUBs|MPN|UBXL

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
