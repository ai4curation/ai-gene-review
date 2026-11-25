# PHS1 (YJL097W; UniProt P40857) notes

Evidence journal (no paid deep research run; built from UniProt and cached publications).

## Function
- Very-long-chain (3R)-3-hydroxyacyl-CoA dehydratase (HACD family), EC 4.2.1.134, essential [UniProt:P40857].
- [PMID:18272525 "Yeast Phs1 is the 3-hydroxyacyl-CoA dehydratase that catalyzes the third reaction of the four-step cycle in the elongation of very long-chain fatty acids (VLCFAs)"].
- Topology: [PMID:18272525 "Phs1 is a membrane-spanning protein that traverses the membrane six times and has an N terminus and C terminus facing the cytosol"]; essential residues Tyr-149, Glu-156.
- [PMID:23416297 "The enzyme kinetics study implicated the direct involvement of the Arg83 and Gly152 residues in the catalytic process."].
- Sphingolipid consequence: [PMID:18272525 "reduced Phs1 levels result in significant impairment of the conversion of ceramide to inositol phosphorylceramide"].

## Location
- ER membrane (topology, HTP ER calls). Huh/Hazbun/Matsumoto HTP vacuole/vacuolar membrane calls kept as non-core.

## YeastPathways issues
- PWY-5177 (glutaryl-CoA degradation) RCA rows: carboxylic acid catabolic process and cytosol removed; Phs1 is an ER anabolic (3R) enzyme. MF row kept.
- PWY-5080-1 uses EC 4.2.1.17 (enoyl-CoA hydratase, 3S beta-oxidation) for the dehydration step; correct EC is 4.2.1.134 -> GO:0102158.
- Vacuolar transport (IMP, Yu et al. 2006 screen) marked over-annotated [PMID:16943325 "we identified four new genes involved in protein trafficking (NUS1, PHS1, PGA2, PGA3)"].

## Genome-scale metabolic models (2026-11-21)
- PHS1 is absent from iMM904 GPRs. In yeast-GEM 9.1.1 its seven reactions are all ER-membrane dehydrations (EC 4.2.1.134), none on (R) metabolites: three (S) (r_2168, r_2169, r_2174) and four unspecified [file:gocams/YeastPathways_PWY-5177/YeastPathways_PWY-5177-bioinformatics/gem_gene_audit.md]. EC 4.2.1.134 is (3R)-specific, so the (S) labels are a candidate yeast-GEM defect; no change to this review.

## Source defects filed (2026-11-23)
- Filed `SGD` `DELETE_ROW` defects (PROBABLE) on three YeastPathways RCA rows that this review REMOVEs: cytosol from PWY-5080-1, cytosol from PWY-5177, and carboxylic acid catabolic process from PWY-5177 (cause `SCOPE_OVER_REACH`). Phs1 is a six-pass integral ER membrane protein acting in VLCFA elongation. The matching GO-CAM activity defects are on gomodel:YeastPathways_PWY-5177/RXN-11667.
- No defect is filed on the GO:0004300 rows (MODIFY to GO:0102158): the term is general, not wrong.
- The yeast-GEM 9.1.1 (S)-labelling of PHS1 reactions is summarised in projects/YEAST_METABOLIC_ENGINEERING/RESULTS.md (FOX2 PR, #6784); GEM errors have no source-defect home.
- (PR #6796 review) The cytosol defects now say why they ask for DELETE_ROW where the GO-CAM activity asks for a repoint: PHS1 already has is_active_in ER membrane from the PAINT IBA, so a repoint would duplicate that row. The topology quote no longer includes the cytosol-facing-termini clause.
