# AMBRA1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9C0C7
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-03 (PR 1363)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/AMBRA1/AMBRA1-ai-review.yaml](AMBRA1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/AMBRA1/AMBRA1-ai-review.html](AMBRA1-ai-review.html)
- Gene notes: present - [genes/human/AMBRA1/AMBRA1-notes.md](AMBRA1-notes.md)
- GOA TSV: present - [genes/human/AMBRA1/AMBRA1-goa.tsv](AMBRA1-goa.tsv)
- UniProt record: present - [genes/human/AMBRA1/AMBRA1-uniprot.txt](AMBRA1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/AMBRA1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/AMBRA1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/AMBRA1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/AMBRA1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/AMBRA1/AMBRA1-deep-research-falcon.md](AMBRA1-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: AMBRA1 encodes a WD40-repeat scaffold and substrate-recognition component of CRL4/DDB1-CUL4 E3 ubiquitin ligase complexes. It regulates macroautophagy by linking ULK1 signaling to BECN1-PIK3C3 autophagosome nucleation, contributes to mitophagy through PRKN-, LC3/GABARAP-, and HUWE1-associated mechanisms, and acts as a CRL4 adaptor that promotes ubiquitin-dependent degradation of substrates such as D-type cyclins and ELOC. AMBRA1 also has context-specific roles in PP2A-dependent MYC and FOXO3 regulation, nuclear transcriptional scaffolding, immune-cell differentiation, and neural development.
- Existing/core annotation action counts: ACCEPT: 48; KEEP_AS_NON_CORE: 20; MARK_AS_OVER_ANNOTATED: 15; MODIFY: 2

## PN Consistency Summary

- **Consistency:** Largely consistent on the UPS/autophagy axes; one divergence on CMA. CRL4 adaptor (GO:1990756) and autophagy/mitophagy roles match across deep research, review, PN, and mapping. The **CMA-enhancer projection (GO:1904716) is NOT adopted** by the review: it has no proposed_new_terms, and explicitly asks (suggested_question/experiment) whether AMBRA1 should be excluded from GO:1904716 until direct LAMP2A/HSPA8 substrate-uptake evidence exists. Review notes correctly state the AMBRA1 CMA-enhancer **leaf (subtype) is no_mapping**, but the dossier shows the parent *type* is mapped and projects GO:1904716 — so the projection still fires.
- **PN story / NEW pressure:** Two PN MFs. GO:1990756 — already in GOA, abundant direct IDA support (PMID:23524951, 33854232/35/39, 30166453) → already captured (ACCEPT). GO:1904716 (verified real) — asserted via the CMA-enhancer bucket but supported only by the "CMA prevents neuronal proteome collapse" background paper, not AMBRA1-specific CMA substrate-uptake data. Verdict: GO:1990756 already captured; GO:1904716 over-reaches as a propagated annotation (candidate pending direct evidence).
- **Evidence alignment:** UPS row PN ref PMID:33854239 = review IDA reference PMID:33854239 (CRL4 cyclin-D) — strong overlap. CMA/autophagy PN titles (AMBRA1 network review; mTOR-ULK1-AMBRA1-TRAF6; CMA proteome-collapse) are background; review's autophagy/mitophagy calls rest on dedicated PMIDs (20921139, 21358617, 23524951, 25215947, 30217973).
- **Verdict:** GO:1990756 consistent/already captured; GO:1904716 CMA-enhancer projection over-reaches (review withholds pending direct CMA evidence).

## Full Consistency Review

- **UniProt:** Q9C0C7 · **batch:** proteostasis-batch-2026-06-03 · **review status:** COMPLETE
- **PN placement:** three rows (branches ALP+UPS) — Class-3 PI3K complex-1 / BECN1-localization modulator; `Chaperone-mediated autophagy|...|CMA enhancer|Enhancer of substrate uptake`; and `UPS|E3 ubiquitin and UBL ligases|Cul4A/Cul4B substrate receptor|WD40|other` ; **PN-node mapping:** PI3K subtree context_only (too_broad, GO:0035032 / GO:0016236, no CC/process projection); CMA-enhancer *type* mapped→GO:1904716 (positive regulation of CMA); CRL4-receptor *group* mapped→GO:1990756 (UBL ligase-substrate adaptor). Projections: **GO:1904716 more_specific_than_existing_goa**, **GO:1990756 already_in_goa_exact**.
- **Consistency:** Largely consistent on the UPS/autophagy axes; one divergence on CMA. CRL4 adaptor (GO:1990756) and autophagy/mitophagy roles match across deep research, review, PN, and mapping. The **CMA-enhancer projection (GO:1904716) is NOT adopted** by the review: it has no proposed_new_terms, and explicitly asks (suggested_question/experiment) whether AMBRA1 should be excluded from GO:1904716 until direct LAMP2A/HSPA8 substrate-uptake evidence exists. Review notes correctly state the AMBRA1 CMA-enhancer **leaf (subtype) is no_mapping**, but the dossier shows the parent *type* is mapped and projects GO:1904716 — so the projection still fires.
- **PN story / NEW pressure:** Two PN MFs. GO:1990756 — already in GOA, abundant direct IDA support (PMID:23524951, 33854232/35/39, 30166453) → already captured (ACCEPT). GO:1904716 (verified real) — asserted via the CMA-enhancer bucket but supported only by the "CMA prevents neuronal proteome collapse" background paper, not AMBRA1-specific CMA substrate-uptake data. Verdict: GO:1990756 already captured; GO:1904716 over-reaches as a propagated annotation (candidate pending direct evidence).
- **Mapping strategy:** PI3K subtree context_only is correctly conservative (no spurious GO:0035032 complex membership — avoids the TOMM20/RAB7A broader-than-review failure mode). The CMA-enhancer *type*→GO:1904716 mapping is the weak point: it propagates a positive-CMA process to AMBRA1 on thin evidence; review withholds it. CRL4 group→GO:1990756 is appropriately specific.
- **Evidence alignment:** UPS row PN ref PMID:33854239 = review IDA reference PMID:33854239 (CRL4 cyclin-D) — strong overlap. CMA/autophagy PN titles (AMBRA1 network review; mTOR-ULK1-AMBRA1-TRAF6; CMA proteome-collapse) are background; review's autophagy/mitophagy calls rest on dedicated PMIDs (20921139, 21358617, 23524951, 25215947, 30217973).
- **Verdict:** GO:1990756 consistent/already captured; GO:1904716 CMA-enhancer projection over-reaches (review withholds pending direct CMA evidence).
- **Recommended edits:** [MAP] Downgrade the CMA-enhancer *type*→GO:1904716 to context_only (or mark AMBRA1 a gene-level exclusion) so positive-CMA is not auto-projected without LAMP2A/HSPA8 substrate-uptake evidence, consistent with the review's withholding.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/AMBRA1/AMBRA1-ai-review.yaml
- PN workbook rows: 3

## PN row 1: Autophagy-Lysosome Pathway | Autophagophore initiation and elongation | Class 3 PI3K complex 1, direct | Modulator of class 3 PI3K complex 1 activity | Modulator of BECN1 localization
- UniProt: Q9C0C7
- In branches: ALP, UPS
- Notes: Interacts with BECN1 to tether the PI3K complex to the dynein motor complex. CUL4A/B-DDB1-AMBRA1 complex mediates K63 ubiquitination of BECN1, increasing activity of VPS34. Phosphorylation of AMBRA1 by ULK1 releases the PI3K complex to allow autophagy induction. Also an enahncer of chaperone-mediated autophagy by promoting substrate uptake.
- PN references (titles):
    - Full article: Connecting autophagy: AMBRA1 and its network of regulation (tandfonline.com)
    - mTOR inhibits autophagy by controlling ULK1 ubiquitylation, self-association and function through AMBRA1 and TRAF6 | Nature Cell Biology
    - Chaperone-mediated autophagy prevents collapse of the neuronal metastable proteome - ScienceDirect
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Class 3 PI3K complex 1, direct|Modulator of class 3 PI3K complex 1 activity|Modulator of BECN1 localization
        status=context_only scope=too_broad_to_propagate GO=[GO:0035032 phosphatidylinositol 3-kinase complex, class III]
        rationale: Reviewed as a class-III PI3K complex context or regulator bucket. This node is useful for curator interpretation, but it should not project cellular-component membership; only explicit complex-component leaves propagate to GO complex terms.
    - [type] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Class 3 PI3K complex 1, direct|Modulator of class 3 PI3K complex 1 activity
        status=context_only scope=too_broad_to_propagate GO=[GO:0035032 phosphatidylinositol 3-kinase complex, class III]
        rationale: Reviewed as a class-III PI3K complex context or regulator bucket. This node is useful for curator interpretation, but it should not project cellular-component membership; only explicit complex-component leaves propagate to GO complex terms.
    - [group] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Class 3 PI3K complex 1, direct
        status=context_only scope=too_broad_to_propagate GO=[GO:0035032 phosphatidylinositol 3-kinase complex, class III]
        rationale: Reviewed as a class-III PI3K complex context or regulator bucket. This node is useful for curator interpretation, but it should not project cellular-component membership; only explicit complex-component leaves propagate to GO complex terms.
    - [class] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation
        status=context_only scope=too_broad_to_propagate GO=[GO:0016236 macroautophagy]
        rationale: This class is a real macroautophagy context, but its descendants include core factors, component buckets, upstream modulators, localization roles, and residual categories. Projecting generic macroautophagy from this ancestor creates TRAPP-like overpropagation, so candidate GO annotations must come from narrower curated nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 2: Autophagy-Lysosome Pathway | Chaperone-mediated autophagy | Lysosomal modulator of chaperone-mediated autophagy | Chaperone-mediated autophagy enhancer | Enhancer of substrate uptake
- UniProt: Q9C0C7
- In branches: ALP, UPS
- Notes: Interacts with BECN1 to tether the PI3K complex to the dynein motor complex. CUL4A/B-DDB1-AMBRA1 complex mediates K63 ubiquitination of BECN1, increasing activity of VPS34. Phosphorylation of AMBRA1 by ULK1 releases the PI3K complex to allow autophagy induction. Also an enahncer of chaperone-mediated autophagy by promoting substrate uptake.
- PN references (titles):
    - Full article: Connecting autophagy: AMBRA1 and its network of regulation (tandfonline.com)
    - mTOR inhibits autophagy by controlling ULK1 ubiquitylation, self-association and function through AMBRA1 and TRAF6 | Nature Cell Biology
    - Chaperone-mediated autophagy prevents collapse of the neuronal metastable proteome - ScienceDirect
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Chaperone-mediated autophagy|Lysosomal modulator of chaperone-mediated autophagy|Chaperone-mediated autophagy enhancer|Enhancer of substrate uptake
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a contextual PN role. The label is useful for curator triage, but by itself does not support a universal GO assertion for all member genes beyond curated ancestor or child mappings.
    - [type] Autophagy-Lysosome Pathway|Chaperone-mediated autophagy|Lysosomal modulator of chaperone-mediated autophagy|Chaperone-mediated autophagy enhancer
        status=mapped scope=ok_for_propagation_to_go GO=[GO:1904716 positive regulation of chaperone-mediated autophagy]
        rationale: This PN type explicitly records enhancer roles for CMA. The directional GO regulation term is more accurate than projecting direct participation in CMA from the class ancestor.
    - [group] Autophagy-Lysosome Pathway|Chaperone-mediated autophagy|Lysosomal modulator of chaperone-mediated autophagy
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Chaperone-mediated autophagy
        status=context_only scope=too_broad_to_propagate GO=[GO:0061684 chaperone-mediated autophagy]
        rationale: The class label matches the GO CMA process, but the subtree includes both effectors and positive or negative modulators. The relation is retained as context so modulators are not projected as direct CMA participants unless a narrower node supports it.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 3: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul4A/Cul4B substrate receptor | WD40 | other
- UniProt: Q9C0C7
- In branches: ALP, UPS
- Signature domains: (none)
- Auxiliary domains: IPR001680
- PN references (titles):
    - 33854239
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul4A/Cul4B substrate receptor|WD40|other
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower substrate-receptor, adaptor, domain, or family subdivision already covered by the curated parent adaptor/receptor mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul4A/Cul4B substrate receptor|WD40
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower substrate-receptor, adaptor, domain, or family subdivision already covered by the curated parent adaptor/receptor mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul4A/Cul4B substrate receptor
        status=mapped scope=ok_for_propagation_to_go GO=[GO:1990756 ubiquitin-like ligase-substrate adaptor activity]
        rationale: This PN group captures substrate receptors/adaptors for cullin/UBL ligase systems. The shared GO molecular-function target is ubiquitin-like ligase-substrate adaptor activity.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (2)
- GO:1904716 positive regulation of chaperone-mediated autophagy | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Autophagy-Lysosome Pathway|Chaperone-mediated autophagy|Lysosomal modulator of chaperone-mediated autophagy|Chaperone-mediated autophagy enhancer
- GO:1990756 ubiquitin-like ligase-substrate adaptor activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul4A/Cul4B substrate receptor

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
