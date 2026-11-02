# dug1 (SPBC1198.08, UniProt Q9P6I2) – notes

Cys-Gly metallodipeptidase, M20A family. Module: DUG1/CNDP2 step. S. cerevisiae ortholog DUG1 (review genes/yeast/DUG1).

## Evidence
- S. pombe genetic evidence: [PMID:19346245 "We also show that the Dug1p Schizosaccharomyces pombe orthologue functions as the exclusive Cys-Gly peptidase in this organism."] — not captured in GOA as experimental (only ISO from SGD); an IMP could be added.
- Biochemistry from S. cerevisiae Dug1: [PMID:19346245 "Dug1p is a homodimer that can also function in a Dug2-Dug3-independent manner as a dipeptidase with high specificity for Cys-Gly and no activity toward tri- or tetrapeptides in vitro."]; [PMID:19346245 "This activity requires zinc or manganese ions."]
- Cytoplasm (ORFeome) [PMID:16823372]; nucleus also seen.
- UniProt FUNCTION text says "Gly-Cys dipeptidase" (should be Cys-Gly) and describes Dug1 as "Catalytic component of the GSH degradosomal complex" — the degradosome model was later revised (Dug2-Dug3 GATase upstream, Dug1 independent; PMID:22277648).

## Decisions
- Proteolysis IBA marked over-annotated (dipeptide catabolism), same as yeast DUG1.
- Core MF GO:0070573, BP GO:0006751, cytosol — matches yeast DUG1 and GO-CAM.
