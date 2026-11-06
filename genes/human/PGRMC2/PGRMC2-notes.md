# PGRMC2 notes

## 2026-11-05 ORGANELLES ER batch 3 (endoplasmic reticulum rows)

Rows: GO:0005783 IBA (is_active_in in GOA), IEA (GO_REF:0000044, SL-0095), IDA (PMID:27754849). All ACCEPT (core); kept.

Checks:
- PAINT PTHR10281 node PTN000031653 IBD seeds: O15173 (PGRMC2 itself), Q9UMX5 (human NENF), RGD:1303289 (rat Nenf), MGI:1913458, AT5G52240, Q4WXS1 (Aspergillus). Seed identities for Q9UMX5, RGD:1303289 and Q4WXS1 checked against UniProt REST on 2026-11-05.
- Human UniProt: "Endoplasmic reticulum {ECO:0000269|PubMed:27754849}"; "Membrane {ECO:0000305|PubMed:23793472}; Single-pass membrane protein"; FT TRANSMEM 42..66 (ECO:0000255); no signal peptide.
- PMID:27754849 (full text): endogenous PGRMC2 (HPA041172) stains "the central ER" and the nuclear envelope/perinuclear ER in adrenocortical cells, HeLa and fibroblasts; no named ER marker (ER assigned from pattern; NPC mAb414 co-stain at the envelope).
- PMID:31748741 (fetched for this check, full text from PMC): "PGRMC2 is a single-pass transmembrane protein localized in the endoplasmic reticulum (ER) and the nuclear envelope" (background statement); depletion lowers labile heme in mitochondria, nuclei and, to a lesser extent, ER; PGRMC1 interaction maps to the heme-binding domain.

Outcome: root rows kept ACCEPT with dated reasons; IBA is_active_in judged defensible but no heme transfer is assayed at the ER itself. NEW GO:0005789 ER membrane (IC): predicted single TM without signal peptide + endogenous ER/nuclear-envelope staining + a cytosol-facing heme-chaperone function. Judgement call: no ER marker or membrane-extraction assay; core_functions unchanged.
