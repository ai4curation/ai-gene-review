# Tcs5 (Q9VRJ6) review notes

## Identity
- Bud32/TP53RK (PRPK) ortholog, RIO-type atypical kinase; KEOPS subunit (PANTHER PTHR12209:SF0).

## Literature
- [PMID:25629598 "Archaea and Eukarya use the KEOPS complex composed of Tcs3 (Kae1), Tcs5 (Bud32), Tcs6 (Pcc1) and Tcs7 (Cgi121) proteins"]
- [PMID:25629598 "Thus, Kae1 apparently modifies the phosphotransferase activity of Bud32 and switches it from a kinase to an ATPase."]
- [PMID:34614169 "the auxiliary subunits Cgi121, the kinase/ATPase Bud32, Pcc1 and Gon7 play a supporting role"]
- Fly bud32 complements yeast [PMID:26516084 "the two KEOPS components Drosophila kae1 and bud32 both conferred substantial rescue"]
- Growth/TOR: [PMID:23444356 "Prpk operates as a transducer of the PI3K/TOR pathway, being essential for TOR kinase activation"]
- Link via t6A-tRNAi: [PMID:26063805 "We report that the t(6)A-modified form of tRNAi (Met) is the actual limiting factor."]

## Decisions
- Core: contributes_to GO:0061711 (complex activity), in KEOPS, cytoplasm (same pattern as other non-catalytic subunits, e.g. CG3434).
- PR #4482 review: UniProt lists obsolete GO:0070525 IBA (replaced_by GO:0002949), absent from GOA. Yeast BUD32 carries GO:0002949; human TP53RK does not. Added NEW GO:0002949 (ISS) and put it in core_functions.
- Ser/Thr kinase rows non-core; general kinase/transferase/catalytic MODIFY to GO:0004674; tyrosine kinase and chromosome over-annotated.

## Deep research (falcon) additions
- [file:DROME/Tcs5/Tcs5-deep-research-falcon.md "Crucially, the threonylcarbamoyl group is transferred to tRNA by the **Kae1/Tcs3 subunit**, *not* by Tcs5."]
- Supports treating Tcs5 as a non-catalytic (contributes_to) KEOPS subunit; no fly Tcs5 protein-phosphorylation substrate established. No change to decisions.
