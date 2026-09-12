# HYPK PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9NX55
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07c
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/HYPK/HYPK-ai-review.yaml](HYPK-ai-review.yaml)
- AIGR review HTML: present - [genes/human/HYPK/HYPK-ai-review.html](HYPK-ai-review.html)
- Gene notes: present - [genes/human/HYPK/HYPK-notes.md](HYPK-notes.md)
- GOA TSV: present - [genes/human/HYPK/HYPK-goa.tsv](HYPK-goa.tsv)
- UniProt record: present - [genes/human/HYPK/HYPK-uniprot.txt](HYPK-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/HYPK.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/HYPK.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/HYPK.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/HYPK.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: HYPK (Huntingtin-interacting protein K) is a small, largely intrinsically disordered protein that functions as a ribosome-associated, NatA-associated chaperone. It is a stable component of the N-terminal acetyltransferase A (NatA)/HYPK complex (with the catalytic NAA10 and auxiliary NAA15 subunits), where it binds principally to NAA15 and acts as a negative regulator that reduces the N-terminal acetyltransferase activity of NatA and modulates its interaction with NAA50 (the NatE catalytic subunit). Independently of catalysis, HYPK has chaperone-like activity: it suppresses aggregation of aggregation-prone clients, notably preventing polyglutamine (polyQ) aggregation of an expanded N-terminal huntingtin (HTT) fragment in neuronal cells, an activity it exerts in association with the NatA complex. Through these chaperone and complex-modulating roles HYPK contributes to protein stabilization and is reported to negatively regulate apoptosis. HYPK is found in both the cytoplasm and the nucleus.
- Existing/core annotation action counts: ACCEPT: 5; KEEP_AS_NON_CORE: 19

## PN Consistency Summary

- **Consistency:** Mostly consistent, with one tension. Deep research and review agree HYPK is an intrinsically disordered NatA-associated chaperone that (a) suppresses polyQ-HTT aggregation (GO:0044183 protein folding chaperone, EXP/IDA) and (b) is a non-catalytic NatA subunit that INHIBITS NatA N-terminal acetyltransferase activity (core_function GO:0010699 acetyltransferase inhibitor activity). The PN row-1 projection of GO:0006474 (N-terminal acetylation, the catalytic process) sits awkwardly: HYPK does not itself acetylate and the review explicitly frames HYPK as a NatA inhibitor/modulator. So PN's "performs N-terminal acetylation" projection partially contradicts the review's "inhibits/modulates NatA" reading.
- **PN story / NEW pressure:** PN row 1 → GO:0006474 N-terminal protein amino acid acetylation (verified real). This is NOT in HYPK's GOA, but HYPK is a regulatory/modulator subunit, not a catalytic acetyltransferase — projecting the catalytic process term over-attributes activity. The review's own GO:0010699 acetyltransferase inhibitor activity (MF) and complex membership (GO:0031415 NatA complex) better capture the role. Row 2 (UPS / NACA-domain reader) is correctly no_mapping. Conclusion: **over-reaches** — GO:0006474 should not be propagated to HYPK as an enabling/involved_in catalytic term.
- **Evidence alignment:** PN row 1 lists no titles; row 2 lists signature domain IPR044034 (UBA/NAC domain), no PMIDs. Review anchors on PMID:17947297 (chaperone/anti-apoptosis), PMID:18076027 (intrinsically disordered chaperone), PMID:20154145 (HYPK-NatA complex, cotranslational NAT + anti-HTT-aggregation). No citation conflict.
- **Verdict:** Mostly consistent; PN's catalytic N-terminal-acetylation projection over-reaches for a NatA-modulator. **Recommended edits:** treat node GO:0006474 as context-only for HYPK (do not propagate the catalytic process term); keep the review's GO:0010699 inhibitor activity + GO:0031415 NatA complex as the accurate captures [MAP].

## Full Consistency Review

- **UniProt:** Q9NX55 · **batch:** proteostasis-batch-2026-06-07c · **review status:** COMPLETE
- **PN placement:** TWO rows. Row 1 (TR) `Translation|Cytosolic translation|Nascent peptide husbandry|N-terminal acetylation of nascent peptide|Modulator of NatA and NatE complexes` (type `N-terminal acetylation`=mapped→GO:0006474 N-terminal protein amino acid acetylation [new_to_goa]; subtype/group=no_mapping; class/branch=context_only). Row 2 (UPS) `Ubiquitin and UBL binding|other protein modifiers|N-terminal acetylation|UBA (NACA)` — all no_mapping; class=context_only→GO:0140036 ubiquitin-modified protein reader activity.
- **Consistency:** Mostly consistent, with one tension. Deep research and review agree HYPK is an intrinsically disordered NatA-associated chaperone that (a) suppresses polyQ-HTT aggregation (GO:0044183 protein folding chaperone, EXP/IDA) and (b) is a non-catalytic NatA subunit that INHIBITS NatA N-terminal acetyltransferase activity (core_function GO:0010699 acetyltransferase inhibitor activity). The PN row-1 projection of GO:0006474 (N-terminal acetylation, the catalytic process) sits awkwardly: HYPK does not itself acetylate and the review explicitly frames HYPK as a NatA inhibitor/modulator. So PN's "performs N-terminal acetylation" projection partially contradicts the review's "inhibits/modulates NatA" reading.
- **PN story / NEW pressure:** PN row 1 → GO:0006474 N-terminal protein amino acid acetylation (verified real). This is NOT in HYPK's GOA, but HYPK is a regulatory/modulator subunit, not a catalytic acetyltransferase — projecting the catalytic process term over-attributes activity. The review's own GO:0010699 acetyltransferase inhibitor activity (MF) and complex membership (GO:0031415 NatA complex) better capture the role. Row 2 (UPS / NACA-domain reader) is correctly no_mapping. Conclusion: **over-reaches** — GO:0006474 should not be propagated to HYPK as an enabling/involved_in catalytic term.
- **Mapping strategy:** Recommend the type-node GO:0006474 be treated as context_only for HYPK (it is a regulator, not a catalyst). The review correctly does not annotate HYPK with N-terminal acetyltransferase activity. UPS-branch no_mappings are appropriate (NatA/UBA-domain reader context, no single safe GO assertion).
- **Evidence alignment:** PN row 1 lists no titles; row 2 lists signature domain IPR044034 (UBA/NAC domain), no PMIDs. Review anchors on PMID:17947297 (chaperone/anti-apoptosis), PMID:18076027 (intrinsically disordered chaperone), PMID:20154145 (HYPK-NatA complex, cotranslational NAT + anti-HTT-aggregation). No citation conflict.
- **Verdict:** Mostly consistent; PN's catalytic N-terminal-acetylation projection over-reaches for a NatA-modulator. **Recommended edits:** treat node GO:0006474 as context-only for HYPK (do not propagate the catalytic process term); keep the review's GO:0010699 inhibitor activity + GO:0031415 NatA complex as the accurate captures [MAP].

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/HYPK/HYPK-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Translation | Cytosolic translation | Nascent peptide husbandry | N-terminal acetylation of nascent peptide | Modulator of NatA and NatE complexes
- UniProt: Q9NX55
- In branches: TR, UPS
- PN-node mapping records (path + ancestors):
    - [subtype] Translation|Cytosolic translation|Nascent peptide husbandry|N-terminal acetylation of nascent peptide|Modulator of NatA and NatE complexes
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower taxonomy bucket already covered by a curated parent mapping or by gene-level annotations. No additional direct GO mapping is appropriate from this node.
    - [type] Translation|Cytosolic translation|Nascent peptide husbandry|N-terminal acetylation of nascent peptide
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0006474 N-terminal protein amino acid acetylation]
        rationale: This PN type denotes N-terminal acetyltransferase machinery acting on nascent peptides. The GO N-terminal acetylation process is the direct target.
    - [group] Translation|Cytosolic translation|Nascent peptide husbandry
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [class] Translation|Cytosolic translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0002181 cytoplasmic translation]
        rationale: The PN class Cytosolic translation is centered on the cytoplasmic translation apparatus and process, but it also houses supporting machinery such as ribosome biogenesis factors. The GO process term is a useful high-level label for the class, but propagating it to all members would over-annotate genes whose PN placement is through assembly or maturation context rather than core cytoplasmic translation.
    - [branch] Translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0006412 translation]
        rationale: The PN Translation branch is organized around the translation apparatus and immediately associated cotranslational quality-control systems. GO translation is the closest high-level process label, but the PN branch also contains adjacent machinery such as ribosome biogenesis and nascent-chain handling. Keeping this relationship is useful for interpretation, but it is too broad to project safely onto every member.

## PN row 2: Ubiquitin Proteasome System | Ubiquitin and UBL binding | other protein modifiers | N-terminal acetylation | UBA (NACA)
- UniProt: Q9NX55
- In branches: TR, UPS
- Signature domains: IPR044034
- Auxiliary domains: (none)
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|Ubiquitin and UBL binding|other protein modifiers|N-terminal acetylation|UBA (NACA)
        status=no_mapping scope= GO=[]
        rationale: Reviewed manually as a UPS source node. No single GO term is appropriate for direct propagation from this PN label without narrower context or gene-level evidence.
    - [type] Ubiquitin Proteasome System|Ubiquitin and UBL binding|other protein modifiers|N-terminal acetylation
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a UPS taxonomy container. Its descendants mix catalytic roles, complex membership, binding domains, regulators, adaptors, and substrate-context labels, so a single propagating GO assertion would overstate the shared biology.
    - [group] Ubiquitin Proteasome System|Ubiquitin and UBL binding|other protein modifiers
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a UPS taxonomy container. Its descendants mix catalytic roles, complex membership, binding domains, regulators, adaptors, and substrate-context labels, so a single propagating GO assertion would overstate the shared biology.
    - [class] Ubiquitin Proteasome System|Ubiquitin and UBL binding
        status=context_only scope=too_broad_to_propagate GO=[GO:0140036 ubiquitin-modified protein reader activity]
        rationale: This class records ubiquitin/UBL-reader context, but the subtree mixes ubiquitin, SUMO, UBL-domain, domain-architecture, catalytic, signaling, trafficking, and nucleic-acid process buckets. It is useful context, not a safe direct propagation.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:0006474 N-terminal protein amino acid acetylation | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Nascent peptide husbandry|N-terminal acetylation of nascent peptide

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
