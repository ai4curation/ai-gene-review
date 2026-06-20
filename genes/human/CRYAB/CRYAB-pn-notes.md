# CRYAB PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: priority-only PN rereview against local AIGR review and available deep-research artifacts
- UniProt: P02511
- AIGR review status: COMPLETE
- Priority category: ontology_gap_bridge
- Local AIGR project status: local_review_complete_not_phase1
- Related project: UNFOLDED_PROTEIN_BINDING.md

## Source Files Checked

- AIGR review YAML: present - [genes/human/CRYAB/CRYAB-ai-review.yaml](CRYAB-ai-review.yaml)
- AIGR review HTML: present - [genes/human/CRYAB/CRYAB-ai-review.html](CRYAB-ai-review.html)
- Gene notes: present - [genes/human/CRYAB/CRYAB-notes.md](CRYAB-notes.md)
- GOA TSV: present - [genes/human/CRYAB/CRYAB-goa.tsv](CRYAB-goa.tsv)
- UniProt record: present - [genes/human/CRYAB/CRYAB-uniprot.txt](CRYAB-uniprot.txt)
- PROTEOSTASIS priority table: [projects/PROTEOSTASIS/priority_genes.tsv](../../../projects/PROTEOSTASIS/priority_genes.tsv)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)
- PN mapping file: [projects/PROTEOSTASIS/mappings/chaperone_systems.yaml](../../../projects/PROTEOSTASIS/mappings/chaperone_systems.yaml)
- PN mapping file: [projects/PROTEOSTASIS/mappings/mitochondrial_proteostasis.yaml](../../../projects/PROTEOSTASIS/mappings/mitochondrial_proteostasis.yaml)

### Deep Research Files

- [genes/human/CRYAB/CRYAB-deep-research-falcon.md](CRYAB-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: CRYAB (alpha-crystallin B chain, also known as HSPB5) is a small heat shock protein that functions as a molecular chaperone with holdase activity. It binds partially denatured or destabilized proteins in an ATP-independent manner to prevent their aggregation, but unlike HSP70-family foldase chaperones, it does NOT actively refold substrates. CRYAB forms large polydisperse oligomeric complexes, typically of 10-40 subunits, and can hetero-oligomerize with CRYAA (HSPB4). The canonical sHSP architecture comprises a central alpha-crystallin domain (ACD) flanked by a variable N-terminal domain (NTD) and a short C-terminal domain (CTD); chaperone activity is tightly coupled to oligomeric assembly and dynamic subunit exchange (DOI:10.1038/s41467-024-54647-7). A conserved N-terminal IXI-like motif (NT-IXI) engages the ACD hydrophobic groove, and perturbation of this motif transforms native assemblies into reversible elongated helical fibrils, as resolved by cryo-EM (DOI:10.1038/s41467-024-54647-7). Stress-activated phosphorylation at Ser19/Ser45/Ser59 by p38 MAPK modulates oligomeric state; the p38-CRYAB(pS59) cascade is a stress-response module that can shift CRYAB condensates toward less dynamic, aggregate-prone states under pathological conditions (DOI:10.1016/j.isci.2024.109510, DOI:10.1172/jci163730). In the eye lens, CRYAB serves dual roles as a structural protein contributing to transparency and refractive index, and as a chaperone preventing aggregation of damaged crystallins. Outside the lens, it is highly expressed in cardiac and skeletal muscle where it associates with cytoskeletal elements including desmin intermediate filaments and titin at Z-bands and intercalated disks. CRYAB also functions as a mitochondrial chaperone and anti-apoptotic protein, binding pro-apoptotic factors Bax, Bcl-X(S), cytochrome c, and VDAC; the E105K mutation causing hereditary optic atrophy reduces these interactions and impairs mitochondrial OXPHOS assembly (DOI:10.1172/jci.insight.182209). CRYAB is secreted via extracellular vesicles and exerts paracrine effects including promotion of angiogenesis in cardiac contexts (DOI:10.1186/s13287-023-03468-4, DOI:10.1038/s42003-022-04402-9). Mutations in CRYAB cause myofibrillar myopathy, cataracts, dilated cardiomyopathy, restrictive cardiomyopathy, and hereditary optic atrophy.
- Existing/core annotation action counts: ACCEPT: 49; KEEP_AS_NON_CORE: 19; MARK_AS_OVER_ANNOTATED: 24; MODIFY: 9

## PN Consistency Summary

- **Consistency:** Priority-only record; no phase-1 dossier section exists yet. Local review status is `local_review_complete_not_phase1`. PN placement: Cytonuclear proteostasis > small HSP; Mitochondrial proteostasis > small HSP; Extracellular proteostasis > chaperone. Main issue: Shows how PN adds multi-branch context around a reviewed holdase gene
- **PN story / NEW pressure:** Current projection rows: GO:0044183 protein folding chaperone (more_specific_than_existing_goa).
- **Mapping strategy:** Use as a bridge case for ontology design: the PN placement may expose missing or underspecified GO proteostasis terms rather than a simple gene-to-existing-term propagation.
- **Verdict:** Create bridge dossier for multi-branch proteostasis semantics and small-HSP ontology gaps

## Priority Review Context

- Category: ontology_gap_bridge
- PN annotations: Cytonuclear proteostasis > small HSP; Mitochondrial proteostasis > small HSP; Extracellular proteostasis > chaperone
- Why interesting: Shows how PN adds multi-branch context around a reviewed holdase gene
- Suggested next step: Create bridge dossier for multi-branch proteostasis semantics and small-HSP ontology gaps
- Related project: UNFOLDED_PROTEIN_BINDING.md

## PN Projection Rows

- GO:0044183 protein folding chaperone - more_specific_than_existing_goa; scope=ok_for_propagation_to_go; mapping=chaperone_systems.yaml;mitochondrial_proteostasis.yaml; PN=Cytonuclear proteostasis|Chaperone|small HSP system|small HSP;Mitochondrial proteostasis|Chaperone|small HSP

## PN Dossier Context

No phase-1 dossier exists for this priority-only gene. This note preserves the current PROTEOSTASIS boundary or exception decision and should be superseded by a dossier section if the gene is promoted into a full phase-1 batch.

## Note

This file is generated from the current PROTEOSTASIS priority table, PN projection outputs, and local gene-review artifacts. Edit those source records rather than this generated note when correcting the underlying curation.
