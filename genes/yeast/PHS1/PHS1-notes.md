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
