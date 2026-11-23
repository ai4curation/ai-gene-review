# AP3B1 notes

## 2026-11-13 ORGANELLES Golgi batch 1 (Golgi apparatus rows)

Rows: GO:0005794 IEA (GO_REF:0000044) and TAS (PMID:9151686), both `located_in`; both ACCEPT -> KEEP_AS_NON_CORE. UniProt line: [file:human/AP3B1/AP3B1-uniprot.txt "Golgi apparatus {ECO:0000305|PubMed:9151686}"] (curator inference from a paper we have in full). Golgi removed from core_functions[0].locations (early endosome kept), because the activity is shown at endosomes. Added PMID:8666661 (fetched, abstract only).

Shared AP-3 evidence (same claim for AP3B1, AP3B2, AP3S1, AP3S2; siblings AP3D1, AP3M1, AP3M2 already KEEP_AS_NON_CORE):
- [PMID:9151686 "Immunofluorescence using anti-delta antibodies reveals that the AP-3 complex is associated with the Golgi region of the cell as well as with more peripheral structures."] Full text: endogenous AP-3 is BFA-sensitive [PMID:9151686 "We have shown that the complex is brefeldin A–sensitive in vivo as well as in vitro"], but double labelling with the TGN markers p200 and gamma-adaptin gives distinct patterns in the same perinuclear region.
- [PMID:8666661 "Endogenous complex in primary cultures of neuronal cells is also localized to the TGN"] (abstract only; immuno-EM of the neuronal p47/beta-NAP complex).
- [PMID:9118953 "Immunofluorescence microscopy analyses show that the sigma3-containing complex is present both in the area of the TGN and in peripheral structures, some of which contain the transferrin receptor."]
- [PMID:15051738 "No significant AP-3 labeling was found in these TGN profiles"] and [PMID:15051738 "Our results provide evidence for the function of the AP-3 complex in the trafficking of lysosomal membrane proteins from endosomes, whereas no support for a role at the TGN was found."] (quantitative immuno-EM, HepG2).
- AP-3 is a cytosolic coat recruited by ARF1: complex membership supports the root at most, never a sub-compartment; the tethering route does not apply (cycling coat).
- Outcome: Golgi rows KEEP_AS_NON_CORE (recruited pool reported, activity shown at endosomes, not Golgi). MARK_AS_OVER_ANNOTATED is the close alternative if the HepG2 EM is taken as decisive for nonneuronal AP-3. No TGN (GO:0005802) row: the sub-compartment lines disagree. No is_active_in rows.
