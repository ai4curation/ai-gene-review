# fruA curation notes

## Boundary and evidence

FruA (Q88PQ3; PP_0795) is the membrane-bound EIIB-EIIC component of the
fructose-specific PTS. Its exact UniProt reaction is RHEA:49252 (EC 2.7.1.202):
external fructose is transported and phosphorylated to intracellular fructose
1-phosphate. KT2440 literature independently identifies FruA as the
membrane-bound EIIBC polyprotein and shows that FruB is required for FruA-
dependent fructose transport [PMID:27933319 "EIIBC (membrane bound, encoded by
fruA)"; PMID:18296519 "FruB mutants cannot transport fructose through the
two-domain (EIIB Fru and EIIC Fru ) FruA permease"].

The InterPro-derived carbohydrate:proton symporter annotation and its inferred
proton-transmembrane-transport process were removed. They conflict with the
protein-phosphorelay mechanism and exact Rhea reaction. Generic membrane and
sugar-transporter terms were marked over-annotated because the review retains
specific plasma-membrane and fructose-PTS terms.


## 2026-11-06 comparative fructose-PTS review

Reviewed all original annotation rows and complete biological scope. Payloads, row order and source bytes are preserved. Broad true terms were refined rather than called over-annotated. No new GO annotation is proposed solely to fill a pathway diagram. Current GO definitions were checked against QuickGO; net phosphohistidine-donor transport and the immediate phosphocysteine step are compatible descriptions of one group-translocation mechanism.

A genuine default Falcon attempt failed with HTTP403; no provider report was fabricated. The review is based on cached primary literature, curated source statements and sequence/domain evidence.

Q88PQ3 has two EIIB-like domains, but cysteine-bearing motifs do not prove that both accept phosphate. The B-prime facilitation result is direct for E. coli (PMID8626640), not a demonstrated KT2440 mechanism. ARBA-only catalytic/localization prose and DE EC-number quotes were replaced by target family evidence plus the native FruA/FruB literature (PMID18296519, PMID27933319).
