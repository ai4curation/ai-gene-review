# DDRGK1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q96HY6
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07c
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/DDRGK1/DDRGK1-ai-review.yaml](DDRGK1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/DDRGK1/DDRGK1-ai-review.html](DDRGK1-ai-review.html)
- Gene notes: present - [genes/human/DDRGK1/DDRGK1-notes.md](DDRGK1-notes.md)
- GOA TSV: present - [genes/human/DDRGK1/DDRGK1-goa.tsv](DDRGK1-goa.tsv)
- UniProt record: present - [genes/human/DDRGK1/DDRGK1-uniprot.txt](DDRGK1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/DDRGK1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/DDRGK1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DDRGK1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DDRGK1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: DDRGK1 (DDRGK domain-containing protein 1; also called UFBP1, Dashurin) is a single-pass endoplasmic-reticulum membrane protein that is an obligate component of the UFM1 ribosome E3 ligase (UREL) complex, together with the E3 ligase UFL1 and CDK5RAP3. DDRGK1 tethers the complex to the ER membrane through its N-terminal transmembrane helix, thereby restricting ufmylation activity to ER-docked ribosomes, and stabilizes UFL1. Following mono-ufmylation of the 60S ribosomal protein RPL26/uL24, DDRGK1 acts as a UFM1 reader, in that its UFM1-interacting motif (UFIM) binds ufmylated RPL26, producing stable association of the 60S subunit with the UREL complex and promoting release and recycling of the large subunit from SEC61 translocons. DDRGK1 is itself a substrate of ufmylation (at Lys-267). Through ER-resident ufmylation it participates in ribosome recycling, reticulophagy (ER-phagy), the response to ER stress and the unfolded protein response (regulating IRE1-alpha/ERN1 stability). Biallelic loss-of-function variants cause Shohat-type spondyloepimetaphyseal dysplasia, reflecting a role in cartilage development via SOX9 stabilization.
- Existing/core annotation action counts: ACCEPT: 27; KEEP_AS_NON_CORE: 55

## PN Consistency Summary

- **Consistency:** Strong agreement. Notes, review, dossier, and projections all converge on DDRGK1 as the obligate ER-membrane UFM1-ligase cofactor / UFM1 reader. Review captures every projected term as an existing annotation (GO:0071569 ufmylation ACCEPT; GO:0061709 reticulophagy KEEP_AS_NON_CORE; ribosome-recycling/RQC via GO:0072344, GO:0032790). No contradictions.
- **PN story / NEW pressure:** The RQC group projects GO:0006515 protein QC as `new_to_goa`. GOA already carries the *specific* RQC outputs GO:0072344 (rescue of stalled cytosolic ribosome) and GO:0032790 (ribosome disassembly), both reviewed. Adding the broad GO:0006515 umbrella would be a less-informative parent of terms already present — over-reaches; the RQC role is **already captured** at greater specificity. GO:0071569 and GO:0061709 are already_in_goa_exact. No defensible NEW term.
- **Evidence alignment:** Excellent overlap. Dossier ERphagy ref PMID:32160526 and UFMylation-cofactor refs PMID:36121123 / PMID:38383789 are all present, verified, and HIGH-relevance in the review.
- **Verdict:** Consistent and high quality; only the broad GO:0006515 RQC projection over-reaches relative to existing specific GOA terms. **Recommended edits:** [MAP] drop/downgrade GO:0006515 projection for DDRGK1 (specific RQC terms GO:0072344/GO:0032790 already in GOA and reviewed).

## Full Consistency Review

- **UniProt:** Q96HY6 · **batch:** proteostasis-batch-2026-06-07c · **review status:** COMPLETE (large, well-evidenced review; 60+ annotations)
- **PN placement:** 4 rows across TR/ALP/UPS — `Translation|Cytosolic translation|Ribosome-associated QC|UFMylation`; `ALP|...|ERphagy|UFMylation of ER proteins`; two UPS `...|UFMylation cofactor` rows ; **PN-node mapping:** types mapped to GO:0071569 protein ufmylation and GO:0061709 reticulophagy (ok_for_propagation); RQC group → GO:0006515 protein QC (ok); UPS nodes no_mapping/context_only.
- **Consistency:** Strong agreement. Notes, review, dossier, and projections all converge on DDRGK1 as the obligate ER-membrane UFM1-ligase cofactor / UFM1 reader. Review captures every projected term as an existing annotation (GO:0071569 ufmylation ACCEPT; GO:0061709 reticulophagy KEEP_AS_NON_CORE; ribosome-recycling/RQC via GO:0072344, GO:0032790). No contradictions.
- **PN story / NEW pressure:** The RQC group projects GO:0006515 protein QC as `new_to_goa`. GOA already carries the *specific* RQC outputs GO:0072344 (rescue of stalled cytosolic ribosome) and GO:0032790 (ribosome disassembly), both reviewed. Adding the broad GO:0006515 umbrella would be a less-informative parent of terms already present — over-reaches; the RQC role is **already captured** at greater specificity. GO:0071569 and GO:0061709 are already_in_goa_exact. No defensible NEW term.
- **Mapping strategy:** Mapped status/scope for ufmylation and reticulophagy is correct. The RQC-group → GO:0006515 projection is broader than this gene's reviewed annotations (cf. TOMM20/HSPA8/RAB7A broader-rejection precedent); recommend NOT projecting GO:0006515 onto DDRGK1.
- **Evidence alignment:** Excellent overlap. Dossier ERphagy ref PMID:32160526 and UFMylation-cofactor refs PMID:36121123 / PMID:38383789 are all present, verified, and HIGH-relevance in the review.
- **Verdict:** Consistent and high quality; only the broad GO:0006515 RQC projection over-reaches relative to existing specific GOA terms. **Recommended edits:** [MAP] drop/downgrade GO:0006515 projection for DDRGK1 (specific RQC terms GO:0072344/GO:0032790 already in GOA and reviewed).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/DDRGK1/DDRGK1-ai-review.yaml
- PN workbook rows: 4

## PN row 1: Translation | Cytosolic translation | Ribosome-associated QC | UFMylation
- UniProt: Q96HY6
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
- UniProt: Q96HY6
- In branches: TR, ALP, UPS
- Notes: Involved in reticulophagy, brings UFL1 ligase to ER surface to UFMylate RPN1 and RPL26
- PN references (titles):
    - A Genome-wide ER-phagy Screen Highlights Key Roles of Mitochondrial Metabolism and ER-Resident UFMylation - PubMed (nih.gov)
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

## PN row 3: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | UBL modifier cofactors | UFMylation cofactor | transmembrane
- UniProt: Q96HY6
- In branches: TR, ALP, UPS
- Signature domains: (none)
- Auxiliary domains: IPR019153
- PN references (titles):
    - 36121123
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|UBL modifier cofactors|UFMylation cofactor|transmembrane
        status=no_mapping scope= GO=[]
        rationale: Reviewed manually as a UPS source node. No single GO term is appropriate for direct propagation from this PN label without narrower context or gene-level evidence.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|UBL modifier cofactors|UFMylation cofactor
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a UPS taxonomy container. Its descendants mix catalytic roles, complex membership, binding domains, regulators, adaptors, and substrate-context labels, so a single propagating GO assertion would overstate the shared biology.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|UBL modifier cofactors
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a UPS taxonomy container. Its descendants mix catalytic roles, complex membership, binding domains, regulators, adaptors, and substrate-context labels, so a single propagating GO assertion would overstate the shared biology.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## PN row 4: Ubiquitin Proteasome System | Ubiquitin and UBL binding | E3 ligase / UBLM | UFMylation cofactor | UFM1 binding
- UniProt: Q96HY6
- In branches: TR, ALP, UPS
- Signature domains: PMID: 38383789
- Auxiliary domains: IPR019153
- PN references (titles):
    - 38383789
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|Ubiquitin and UBL binding|E3 ligase / UBLM|UFMylation cofactor|UFM1 binding
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a binding-branch UBL-modifier subtype. Because this context mixes catalytic ligases and cofactors, no direct GO propagation is made from this node.
    - [type] Ubiquitin Proteasome System|Ubiquitin and UBL binding|E3 ligase / UBLM|UFMylation cofactor
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a binding-branch UBL-modifier subtype. Because this context mixes catalytic ligases and cofactors, no direct GO propagation is made from this node.
    - [group] Ubiquitin Proteasome System|Ubiquitin and UBL binding|E3 ligase / UBLM
        status=context_only scope=too_broad_to_propagate GO=[GO:0019787 ubiquitin-like protein transferase activity]
        rationale: This binding-branch group records E3/UBL-modifier context, but it includes cofactors as well as catalytic ligases. Direct propagation should come from narrower enzyme-specific nodes.
    - [class] Ubiquitin Proteasome System|Ubiquitin and UBL binding
        status=context_only scope=too_broad_to_propagate GO=[GO:0140036 ubiquitin-modified protein reader activity]
        rationale: This class records ubiquitin/UBL-reader context, but the subtree mixes ubiquitin, SUMO, UBL-domain, domain-architecture, catalytic, signaling, trafficking, and nucleic-acid process buckets. It is useful context, not a safe direct propagation.
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
