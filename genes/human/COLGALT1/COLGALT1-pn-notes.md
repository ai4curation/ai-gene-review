# COLGALT1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q8NBJ5
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/COLGALT1/COLGALT1-ai-review.yaml](COLGALT1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/COLGALT1/COLGALT1-ai-review.html](COLGALT1-ai-review.html)
- Gene notes: present - [genes/human/COLGALT1/COLGALT1-notes.md](COLGALT1-notes.md)
- GOA TSV: present - [genes/human/COLGALT1/COLGALT1-goa.tsv](COLGALT1-goa.tsv)
- UniProt record: present - [genes/human/COLGALT1/COLGALT1-uniprot.txt](COLGALT1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/COLGALT1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/COLGALT1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/COLGALT1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/COLGALT1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: COLGALT1 (collagen beta(1-O)galactosyltransferase 1; also known as GLT25D1) is a soluble enzyme of the endoplasmic reticulum lumen that catalyzes the first committed step of collagen O-linked glycosylation. It transfers galactose from UDP-alpha-D-galactose onto (5R)-5-hydroxy-L-lysine (hydroxylysine) residues of collagen, forming the beta(1-O)-linked Gal-O-hydroxylysine (EC 2.4.1.50). This galactose is then the acceptor for subsequent alpha1,2-glucosylation, generating the Glc(alpha1-2)Gal disaccharide that is strongly conserved across animal collagens. The enzyme belongs to glycosyltransferase family 25 (GT25), adopts a GT-A-like fold with metal-dependent (Mn2+) catalysis, and uses essential aspartate residues (D166/D168, D461/D463) for activity. COLGALT1 acts on multiple collagen types (including types I and IV) as well as the collagenous domain of mannose-binding lectin, and co-localizes in the early secretory pathway with the upstream lysyl hydroxylase PLOD3/LH3. As the predominant of two paralogous collagen galactosyltransferases (the other being COLGALT2/GLT25D2), it is broadly expressed and its loss reduces collagen glycosylation, causing intracellular collagen accumulation. Biallelic loss-of-function variants in COLGALT1 cause an autosomal recessive cerebral small vessel disease (brain small vessel disease 3).
- Existing/core annotation action counts: ACCEPT: 10; KEEP_AS_NON_CORE: 1; MARK_AS_OVER_ANNOTATED: 2; NEW: 1

## PN Consistency Summary

- **Consistency:** Consistent. Review, notes-equivalent (rich references), PN annotation, and PN-node mapping all describe COLGALT1/GLT25D1 as a soluble ER-lumen collagen beta(1-O)galactosyltransferase (EC 2.4.1.50) performing the first committed step of collagen O-glycosylation. The collagen-biosynthesis framing is concordant across sources.
- **PN story / NEW pressure:** PN projects collagen biosynthetic process (GO:0032964, verified real OLS). COLGALT1's curated core function is the more specific GO:0050211 procollagen galactosyltransferase activity (MF) plus GO:0180062 protein O-linked glycosylation via galactose (BP), and it already carries GO:0030199 collagen fibril organization. GO:0032964 is a broader pathway-context process consistent with these but more general. Conclusion: PN context is **already captured** at a finer grain in the review; no additional NEW-term pressure from the PN node. (Review's own NEW is GO:0030145 Mn ion binding — orthogonal to PN.)
- **Evidence alignment:** PN row carries no reference titles; review evidence (PMID:19075007, PMID:20470363, PMID:22216269, PMID:27402836, PMID:30412317, Reactome collagen-galactosylation reactions) fully supports the collagen-biosynthesis mapping. No divergence.
- **Verdict:** Consistent; PN collagen-biosynthesis role already captured (more specifically) in review. No edits required.

## Full Consistency Review

- **UniProt:** Q8NBJ5 · **batch:** proteostasis-batch-2026-06-07 · **review status:** COMPLETE
- **PN placement:** `ER proteostasis | Maturation and folding of specific substrates | ER collagen processing and folding` ; **PN-node mapping:** group=mapped, scope=ok_for_propagation_to_go, GO:0032964 collagen biosynthetic process (class/branch = no_mapping)
- **Consistency:** Consistent. Review, notes-equivalent (rich references), PN annotation, and PN-node mapping all describe COLGALT1/GLT25D1 as a soluble ER-lumen collagen beta(1-O)galactosyltransferase (EC 2.4.1.50) performing the first committed step of collagen O-glycosylation. The collagen-biosynthesis framing is concordant across sources.
- **PN story / NEW pressure:** PN projects collagen biosynthetic process (GO:0032964, verified real OLS). COLGALT1's curated core function is the more specific GO:0050211 procollagen galactosyltransferase activity (MF) plus GO:0180062 protein O-linked glycosylation via galactose (BP), and it already carries GO:0030199 collagen fibril organization. GO:0032964 is a broader pathway-context process consistent with these but more general. Conclusion: PN context is **already captured** at a finer grain in the review; no additional NEW-term pressure from the PN node. (Review's own NEW is GO:0030145 Mn ion binding — orthogonal to PN.)
- **Mapping strategy:** No change. Mapping the group node to GO:0032964 is appropriate as a shared substrate-specific pathway context for the collagen-processing group; it is broader than COLGALT1's specific MF/BP but is a process-level umbrella, not an over-reach (unlike a CC/complex claim). Ancestors correctly no_mapping.
- **Evidence alignment:** PN row carries no reference titles; review evidence (PMID:19075007, PMID:20470363, PMID:22216269, PMID:27402836, PMID:30412317, Reactome collagen-galactosylation reactions) fully supports the collagen-biosynthesis mapping. No divergence.
- **Verdict:** Consistent; PN collagen-biosynthesis role already captured (more specifically) in review. No edits required.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07
- review_yaml: genes/human/COLGALT1/COLGALT1-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Maturation and folding of specific substrates | ER collagen processing and folding
- UniProt: Q8NBJ5
- In branches: ER
- PN-node mapping records (path + ancestors):
    - [group] ER proteostasis|Maturation and folding of specific substrates|ER collagen processing and folding
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0032964 collagen biosynthetic process]
        rationale: This PN group contains ER factors dedicated to collagen maturation, processing, and folding. Collagen biosynthetic process captures the shared substrate-specific pathway context.
    - [class] ER proteostasis|Maturation and folding of specific substrates
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (1)
- GO:0032964 collagen biosynthetic process | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=ER proteostasis|Maturation and folding of specific substrates|ER collagen processing and folding

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
