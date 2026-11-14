# AP3B2 Notes

## 2026-10-05: OpenScientist clathrin/Arf1 follow-up

- Re-read the AP3B2 OpenScientist report in `AP3B2-hypotheses/kgap-ap3b2-clathrin-vs-arf1-neuronal-ap3/openscientist.md`.
- The stale review was overpromoting PMID:9545220 into a proposed `GO:0035615 clathrin-cargo adaptor activity` core molecular function. The 1998 Dell'Angelica paper supports beta3/clathrin binding, but not that AP3B2-containing AP-3 primarily loads cargo into clathrin-coated vesicles.
- Added the final PNAS version of the Begley, Aragon, and Baker AP-3 structure paper, PMID:39705307. It supersedes the preprint PMID:38895279 cited by the OpenScientist report and supports a cargo- and Arf1-coupled AP-3 coat-initiation model.
- Added Kaufman et al. 2026, PMID:42139345, to match the sibling AP-3 subunit reviews' decisive clathrin-independence evidence: reconstituted AP3:ARF1 carriers assemble without a clathrin lattice.
- Added Peden et al. 2002, PMID:11807095, because it is the key functional counterweight to a clathrin-centric AP-3 model. The clathrin-box point mutant was beta3A/AP3B1, not beta3B/AP3B2, so it weakens an obligate AP-3 clathrin model but does not by itself settle the neuronal beta3B clathrin-box question.
- Removed the proposed `GO:0035615` row, changed the AP3B2 core molecular function to `GO:0140312 cargo adaptor activity`, modified `GO:0035654` to the clathrin-neutral parent `GO:0035459 vesicle cargo loading`, and kept the clathrin-coated vesicle membrane row as an over-annotation rather than deleting curator-imported assertions wholesale.

## 2026-11-13 ORGANELLES Golgi batch 1 (Golgi apparatus rows)

Row: GO:0005794 IEA (GO_REF:0000044), `located_in`; ACCEPT -> KEEP_AS_NON_CORE. UniProt line: [file:human/AP3B2/AP3B2-uniprot.txt "Golgi apparatus {ECO:0000250}"] (by similarity). The strongest beta3B-specific line is the 1996 immuno-EM of the endogenous neuronal complex at the TGN [PMID:8666661], which supports the root; it is contradicted for the TGN by the 1997 marker double-labelling and the HepG2 EM, so no TGN row. The old support quote from PMID:7671305 (soluble and membrane-bound pools) said nothing about the Golgi and was replaced. Core functions had no Golgi location; unchanged.

Shared AP-3 evidence (same claim for AP3B1, AP3B2, AP3S1, AP3S2; siblings AP3D1, AP3M1, AP3M2 already KEEP_AS_NON_CORE):
- [PMID:9151686 "Immunofluorescence using anti-delta antibodies reveals that the AP-3 complex is associated with the Golgi region of the cell as well as with more peripheral structures."] Full text: endogenous AP-3 is BFA-sensitive [PMID:9151686 "We have shown that the complex is brefeldin A–sensitive in vivo as well as in vitro"], but double labelling with the TGN markers p200 and gamma-adaptin gives distinct patterns in the same perinuclear region.
- [PMID:8666661 "Endogenous complex in primary cultures of neuronal cells is also localized to the TGN"] (abstract only; immuno-EM of the neuronal p47/beta-NAP complex).
- [PMID:9118953 "Immunofluorescence microscopy analyses show that the sigma3-containing complex is present both in the area of the TGN and in peripheral structures, some of which contain the transferrin receptor."]
- [PMID:15051738 "No significant AP-3 labeling was found in these TGN profiles"] and [PMID:15051738 "Our results provide evidence for the function of the AP-3 complex in the trafficking of lysosomal membrane proteins from endosomes, whereas no support for a role at the TGN was found."] (quantitative immuno-EM, HepG2).
- AP-3 is a cytosolic coat recruited by ARF1: complex membership supports the root at most, never a sub-compartment; the tethering route does not apply (cycling coat).
- Outcome: Golgi rows KEEP_AS_NON_CORE (recruited pool reported, activity shown at endosomes, not Golgi). MARK_AS_OVER_ANNOTATED is the close alternative if the HepG2 EM is taken as decisive for nonneuronal AP-3. No TGN (GO:0005802) row: the sub-compartment lines disagree. No is_active_in rows.
