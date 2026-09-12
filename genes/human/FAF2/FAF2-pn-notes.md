# FAF2 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q96CS3
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-11
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/FAF2/FAF2-ai-review.yaml](FAF2-ai-review.yaml)
- AIGR review HTML: missing - genes/human/FAF2/FAF2-ai-review.html
- Gene notes: present - [genes/human/FAF2/FAF2-notes.md](FAF2-notes.md)
- GOA TSV: present - [genes/human/FAF2/FAF2-goa.tsv](FAF2-goa.tsv)
- UniProt record: present - [genes/human/FAF2/FAF2-uniprot.txt](FAF2-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/FAF2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/FAF2.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FAF2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FAF2.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/FAF2/FAF2-deep-research-falcon.md](FAF2-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: FAF2 (also known as UBXD8, ETEA, UBXN3B) is a 445-residue, membrane-anchored cofactor of the AAA-ATPase p97/VCP. It contains an N-terminal UBA domain that binds ubiquitin conjugates, a central UAS (thioredoxin-like) domain implicated in unsaturated fatty-acid sensing, a coiled-coil region, and a C-terminal UBX domain that docks onto p97/VCP. By bridging ubiquitinated client proteins to the p97/VCP segregase, FAF2 functions as a substrate-recruiting adaptor at the endoplasmic reticulum membrane and on lipid droplets. At the ER it is a component of the SEL1L/HRD1-associated ER-associated degradation (ERAD) machinery, where it promotes the dislocation/retrotranslocation of misfolded ER proteins to the cytosol for proteasomal degradation. On lipid droplets, FAF2 recruits p97/VCP and binds directly to the lipase PNPLA2/ATGL, inhibiting it by displacing its coactivator ABHD5/CGI-58, thereby restraining triacylglycerol lipolysis and increasing lipid-droplet size; its partitioning between the ER and lipid droplets is controlled by the ER-resident rhomboid pseudoprotease UBAC2. FAF2 also links lipid metabolism through p97-dependent dislocation of Insig-1 (SREBP regulation) and, upon heat stress, binds ubiquitinated G3BP1 to recruit p97/VCP and drive stress-granule disassembly. FAF2 is broadly expressed.
- Existing/core annotation action counts: ACCEPT: 21; KEEP_AS_NON_CORE: 16; MARK_AS_OVER_ANNOTATED: 2

## PN Consistency Summary

- **Consistency:** Excellent. Deep research, review and PN concur on the core: membrane-tethered UBX p97/VCP substrate-recruiting cofactor (UBA binds ubiquitin, UBX docks p97) in SEL1L/HRD1 ERAD dislocation, plus lipid-droplet/ATGL inhibition, stress-granule disassembly, Insig-1/SREBP, and newer pexophagy (PMID:39472561) and ER-mitochondria contact-site (PMID:36746962) roles. The review correctly avoids `protein binding` as core, using GO:0030674 adaptor, GO:0043130 ubiquitin binding, GO:0034098 VCP-NPL4-UFD1 complex. No contradictions.
- **PN story / NEW pressure:** PN's only NEW projection is GO:0035694 mitochondrial protein catabolic process (verified real; NOT in GOA) from the mitoTAD-pathway row. FAF2/UBXD8 does participate in mitochondrial outer-membrane-associated degradation (mitoTAD) and p97-dependent extraction at mitochondria (PMID:41258083 "extract membrane proteins from the ER and mitochondria"), so this is a DEFENSIBLE (if non-core) ADD — but the review captures FAF2's degradation roles only as ERAD/retrotranslocation, not a mitochondrial-catabolism BP. Conclude: ERAD captured; GO:0035694 a defensible NEW (non-core), mildly broader than the review's ER-centric framing.
- **Evidence alignment:** Good. PN UBX rows cite "18438607 / rev" and "18775313" — PMID:18775313 IS in the review (UBX/p97 cofactor family, HIGH). PMID:18438607 is NOT in the review (likely a UBX-domain review). The review's ERAD/LD/SG evidence (PMID:18711132, 23297223, 25660456, 34739333, + Falcon-added 26389662/35920641/36746962/39472561/41258083) is far richer than the PN rows.
- **Verdict:** Fully consistent; ERAD already captured, GO:0035694 mitochondrial protein catabolic process a defensible (non-core) NEW from the mitoTAD role. PN correctly declines to over-propagate the VCP-adaptor architecture rows. No YAML change strictly required.

## Full Consistency Review

- **UniProt:** Q96CS3 (UBXD8/ETEA) · **batch:** proteostasis-batch-2026-06-11 · **review status:** COMPLETE (very thorough; UBA-UAS-UBX p97/VCP cofactor — ERAD + lipid-droplet/ATGL + stress-granule + pexophagy + ERMCS)
- **PN placement:** 5 rows — `ER proteostasis|...|ERAD|Retrotranslocation channel complex`; `Mitochondrial proteostasis|Organelle-specific protein degradation|mitoTAD pathway`; three UPS rows (`UBX domain|VCP adaptors`, `VCP and associated proteins|adaptors|UBX`, `Ubiquitin and UBL binding|VCP-associated adaptor`). **PN-node mapping:** ERAD group→GO:0036503 exact (in_goa); Mito-degradation class→GO:0035694 mitochondrial protein catabolic process (new_to_goa); the three UPS adaptor rows all no_mapping/context_only (GO:0019787, GO:0034098, GO:0043335, GO:0140036 as too_broad context only). Projected: GO:0036503 (in GOA), GO:0035694 (new).
- **Consistency:** Excellent. Deep research, review and PN concur on the core: membrane-tethered UBX p97/VCP substrate-recruiting cofactor (UBA binds ubiquitin, UBX docks p97) in SEL1L/HRD1 ERAD dislocation, plus lipid-droplet/ATGL inhibition, stress-granule disassembly, Insig-1/SREBP, and newer pexophagy (PMID:39472561) and ER-mitochondria contact-site (PMID:36746962) roles. The review correctly avoids `protein binding` as core, using GO:0030674 adaptor, GO:0043130 ubiquitin binding, GO:0034098 VCP-NPL4-UFD1 complex. No contradictions.
- **PN story / NEW pressure:** PN's only NEW projection is GO:0035694 mitochondrial protein catabolic process (verified real; NOT in GOA) from the mitoTAD-pathway row. FAF2/UBXD8 does participate in mitochondrial outer-membrane-associated degradation (mitoTAD) and p97-dependent extraction at mitochondria (PMID:41258083 "extract membrane proteins from the ER and mitochondria"), so this is a DEFENSIBLE (if non-core) ADD — but the review captures FAF2's degradation roles only as ERAD/retrotranslocation, not a mitochondrial-catabolism BP. Conclude: ERAD captured; GO:0035694 a defensible NEW (non-core), mildly broader than the review's ER-centric framing.
- **Mapping strategy:** Correct. All UBX/VCP-adaptor UPS rows are conservatively no_mapping/context_only (avoids the TOMM20/HSPA8-style over-broad propagation of GO:0043335 protein unfolding / GO:0034098 to a mere adaptor). ERAD group→GO:0036503 exact is right. Mito-class→GO:0035694 is the conservative shared target. No node-status change warranted.
- **Evidence alignment:** Good. PN UBX rows cite "18438607 / rev" and "18775313" — PMID:18775313 IS in the review (UBX/p97 cofactor family, HIGH). PMID:18438607 is NOT in the review (likely a UBX-domain review). The review's ERAD/LD/SG evidence (PMID:18711132, 23297223, 25660456, 34739333, + Falcon-added 26389662/35920641/36746962/39472561/41258083) is far richer than the PN rows.
- **Verdict:** Fully consistent; ERAD already captured, GO:0035694 mitochondrial protein catabolic process a defensible (non-core) NEW from the mitoTAD role. PN correctly declines to over-propagate the VCP-adaptor architecture rows. No YAML change strictly required.
- **Recommended edits:** [YAML] (optional) add GO:0035694 mitochondrial protein catabolic process (involved_in; mitoTAD/mito membrane-protein extraction, PMID:41258083) as a non-core BP to mirror the PN projection. [REF] PN-cited PMID:18438607 (UBX row) absent from review — verify whether gene-specific or a UBX-family review.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/FAF2/FAF2-ai-review.yaml
- PN workbook rows: 5

## PN row 1: ER proteostasis | Organelle-specific protein degradation | ER associated degradation | Retrotranslocation channel complex
- UniProt: Q96CS3
- In branches: ER, MI, UPS
- PN-node mapping records (path + ancestors):
    - [type] ER proteostasis|Organelle-specific protein degradation|ER associated degradation|Retrotranslocation channel complex
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower taxonomy bucket already covered by a curated parent mapping or by gene-level annotations. No additional direct GO mapping is appropriate from this node.
    - [group] ER proteostasis|Organelle-specific protein degradation|ER associated degradation
        status=mapped scope=exact GO=[GO:0036503 ERAD pathway]
        rationale: The PN group "ER associated degradation" is a direct lexical and biological match to the GO ERAD pathway term. The additional branch and class context disambiguates the source string from any broader degradation language.
    - [class] ER proteostasis|Organelle-specific protein degradation
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## PN row 2: Mitochondrial proteostasis | Organelle-specific protein degradation | mitoTAD pathway
- UniProt: Q96CS3
- In branches: ER, MI, UPS
- PN-node mapping records (path + ancestors):
    - [group] Mitochondrial proteostasis|Organelle-specific protein degradation|mitoTAD pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower taxonomy bucket that is already covered by a curated parent mapping or by gene-level annotations. No additional direct GO mapping is appropriate from this node.
    - [class] Mitochondrial proteostasis|Organelle-specific protein degradation
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0035694 mitochondrial protein catabolic process]
        rationale: This PN class groups mitochondrial protein-degradation pathways. GO mitochondrial protein catabolic process is the conservative shared target.
    - [branch] Mitochondrial proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## PN row 3: Ubiquitin Proteasome System | Ubiquitin and UBL proteins | UBX domain | VCP adaptors | thioredoxin-like, UBA
- UniProt: Q96CS3
- In branches: ER, MI, UPS
- Signature domains: IPR001012
- Auxiliary domains: IPR054109, IPR036249
- PN references (titles):
    - 18438607 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|Ubiquitin and UBL proteins|UBX domain|VCP adaptors|thioredoxin-like, UBA
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a UBX-domain/VCP-adaptor architecture subdivision. The domain label does not by itself establish a direct GO annotation beyond gene-level VCP-adaptor evidence.
    - [type] Ubiquitin Proteasome System|Ubiquitin and UBL proteins|UBX domain|VCP adaptors
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a UPS taxonomy container. Its descendants mix catalytic roles, complex membership, binding domains, regulators, adaptors, and substrate-context labels, so a single propagating GO assertion would overstate the shared biology.
    - [group] Ubiquitin Proteasome System|Ubiquitin and UBL proteins|UBX domain
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a UBX-domain protein bucket. UBX domain architecture is useful PN taxonomy but not itself a GO propagation target.
    - [class] Ubiquitin Proteasome System|Ubiquitin and UBL proteins
        status=context_only scope=too_broad_to_propagate GO=[GO:0019787 ubiquitin-like protein transferase activity]
        rationale: This class groups ubiquitin, UBL modifiers, UBX/UBL-domain proteins, and UBL-containing enzymes. The branch is UPS-relevant but too mixed to propagate as a single GO annotation.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## PN row 4: Ubiquitin Proteasome System | VCP and associated proteins | adaptors | UBX | thioredoxin-like, UBA
- UniProt: Q96CS3
- In branches: ER, MI, UPS
- Signature domains: IPR001012
- Auxiliary domains: IPR036249, IPR009060
- PN references (titles):
    - 18775313
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|VCP and associated proteins|adaptors|UBX|thioredoxin-like, UBA
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a VCP-adaptor motif or architecture subdivision. The label is useful taxonomy but too indirect for direct GO propagation without gene-level evidence.
    - [type] Ubiquitin Proteasome System|VCP and associated proteins|adaptors|UBX
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a VCP-adaptor motif or architecture subdivision. The label is useful taxonomy but too indirect for direct GO propagation without gene-level evidence.
    - [group] Ubiquitin Proteasome System|VCP and associated proteins|adaptors
        status=context_only scope=too_broad_to_propagate GO=[GO:0034098 VCP-NPL4-UFD1 AAA ATPase complex]
        rationale: This PN group records VCP adaptor context, but it mixes UBX, SHP, VIM, VBM, membrane, and other adaptor classes. Direct propagation should come only from narrower complex-specific nodes or gene-level review.
    - [class] Ubiquitin Proteasome System|VCP and associated proteins
        status=context_only scope=too_broad_to_propagate GO=[GO:0043335 protein unfolding]
        rationale: This class records the VCP segregase branch context, but descendants include VCP, substrate adaptors, DUBs, E3 ligases, channels, and unrelated associated enzymes. Direct propagation is restricted to narrower nodes.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## PN row 5: Ubiquitin Proteasome System | Ubiquitin and UBL binding | VCP-associated adaptor | with UBX & TRX-like | UBA-like
- UniProt: Q96CS3
- In branches: ER, MI, UPS
- Signature domains: IPR054109
- Auxiliary domains: IPR001012, IPR036249
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|Ubiquitin and UBL binding|VCP-associated adaptor|with UBX & TRX-like|UBA-like
        status=no_mapping scope= GO=[]
        rationale: Reviewed manually as a UPS source node. No single GO term is appropriate for direct propagation from this PN label without narrower context or gene-level evidence.
    - [type] Ubiquitin Proteasome System|Ubiquitin and UBL binding|VCP-associated adaptor|with UBX & TRX-like
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a UPS taxonomy container. Its descendants mix catalytic roles, complex membership, binding domains, regulators, adaptors, and substrate-context labels, so a single propagating GO assertion would overstate the shared biology.
    - [group] Ubiquitin Proteasome System|Ubiquitin and UBL binding|VCP-associated adaptor
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a UPS taxonomy container. Its descendants mix catalytic roles, complex membership, binding domains, regulators, adaptors, and substrate-context labels, so a single propagating GO assertion would overstate the shared biology.
    - [class] Ubiquitin Proteasome System|Ubiquitin and UBL binding
        status=context_only scope=too_broad_to_propagate GO=[GO:0140036 ubiquitin-modified protein reader activity]
        rationale: This class records ubiquitin/UBL-reader context, but the subtree mixes ubiquitin, SUMO, UBL-domain, domain-architecture, catalytic, signaling, trafficking, and nucleic-acid process buckets. It is useful context, not a safe direct propagation.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (2)
- GO:0036503 ERAD pathway | scope=exact | goa_status=already_in_goa_exact | from=ER proteostasis|Organelle-specific protein degradation|ER associated degradation
- GO:0035694 mitochondrial protein catabolic process | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Mitochondrial proteostasis|Organelle-specific protein degradation

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
