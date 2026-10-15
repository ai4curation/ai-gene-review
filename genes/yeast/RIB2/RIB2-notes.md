# RIB2 (YOL066C, PUS8) notes

UniProt Q12362; bifunctional: N-terminal RluA-family tRNA Psi32 synthase (EC 5.4.99.28) + C-terminal CMP/dCMP-deaminase-family riboflavin deaminase [UniProt:Q12362].

## Evidence journal
- [PMID:15466869 "two enzymes, Rib2/Pus8p and Pus9p, are required for Psi32 formation in cytoplasmic and mitochondrial tRNAs, respectively"]; [PMID:15466869 "Rib2/Pus8p is strictly cytoplasmic"].
- Domain assignment [PMID:15466869 "its C-terminal domain has a DRAP-deaminase activity required for riboflavin biogenesis in the cytoplasm, whereas its N-terminal domain carries the tRNA:Psi32-synthase activity"].
- Pathway order: reduction (Rib7) precedes deamination (Rib2) in yeast [PMID:4555411 "rib(7)-rib(2) strains show the phenotypic properties of rib(7) strains."]; Rib7 UniProt reaction uses ribosyl->ribityl substrate [UniProt:P33312].
- GO:0008835 (EC 3.5.4.26) is defined on the ribosyl substrate (bacterial RibD order). The ribityl-substrate term GO:0043723 (MetaCyc synonym YOL066C-MONOMER) is obsolete. UniProt Q12362 also lists the ribosyl reaction, inconsistent with RIB7 entry.

## Decisions
- IBA rRNA pseudouridine synthesis MARK_AS_OVER_ANNOTATED (tRNA-specific). Generic EC 3.5.4 / deaminase rows MODIFY -> GO:0008835. Two core functions.
