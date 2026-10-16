# DUG2 (YBR281C, UniProt P38149) notes

- Identified in a screen for defective utilization of glutathione; GSH and gamma-Glu-Cys degradation "required the participation of the DUG2 and DUG3 gene products as well" [PMID:17179087]. "The DUG2 gene encodes a protein with a peptidase domain and a large WD40 repeat region" [PMID:17179087].
- Cytoplasmic: "all three proteins were observed to have uniform GFP fluorescence throughout the cytoplasm" [PMID:17179087].
- Biochemistry: "Dug2p, which has an N-terminal WD40 and a C-terminal M20A peptidase domain, has no peptidase activity." [PMID:22277648]; "purified Dug2p showed negligible cleavage of Cys-Gly peptide (only 4%)" [PMID:22277648].
- "In vitro reconstitution assays revealed that Dug2p and Dug3p were required together for the cleavage of glutathione into glutamate and Cys-Gly." [PMID:22277648]; Dug2-Dug3 interaction via the Dug2 WD40 domain; Dug2 homodimerizes via its M20A domain; active complex (Dug2p-Dug3p)2, Km GSH 1.2 mM [PMID:22277648].
- Catalytic nucleophile is the N-terminal Cys of Dug3 (GATase II) [PMID:22277648]; Dug2 is the non-catalytic (scaffold) partner.
- DUG2 and DUG3 derepressed by sulfur limitation [PMID:22277648].

## Annotation issues
- Peptidase/hydrolase/proteolysis IBA and IEA rows assume an active M20 dipeptidase; contradicted by direct assay. M20A predicted Zn ligands are annotated by similarity in UniProt but metal binding is unverified.
- Module (glutathione_synthesis_gamma_glutamyl_cycle) correctly models Dug2 as a non-catalytic partner of Dug3 in cytosol.
- YeastCyc: no Dug2/Dug3 reaction (glutathione + H2O -> glutamate + Cys-Gly) in PWYQT-4432 / PWY3O-114; only mentioned in the comment. The DUG pathway step is missing from YeastCyc.
