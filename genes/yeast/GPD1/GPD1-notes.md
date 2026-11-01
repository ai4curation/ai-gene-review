# GPD1 (YDL022W, UniProt Q00055) notes

## Activity / role
- NADH-dependent cytosolic GPDH, key enzyme of glycerol synthesis [PMID:8196651 "We have cloned a gene encoding the key enzyme of glycerol synthesis, the NADH-dependent cytosolic glycerol-3-phosphate dehydrogenase, and we named it GPD1."]
- Osmotic role [PMID:8196651 "gpd1 delta mutants produced very little glycerol, and they were sensitive to osmotic stress."]; HOG-regulated [PMID:8196651 "hog1 delta mutants lacking a protein kinase involved in osmostress-induced signal transduction (the high-osmolarity glycerol response [HOG] pathway) failed to increase glycerol-3-phosphate dehydrogenase activity and mRNA levels when osmotic stress was imposed."]
- GPDH (not Gpp) is rate-limiting for glycerol flux [PMID:11676566 "These results demonstrate that GPDH, but not the glycerol 3-phosphatase, is rate-limiting for glycerol production."]
- Reaction EC 1.1.1.8, RHEA:11092 [UniProt:Q00055]

## Localization
- Cytosol + peroxisome [PMID:15210723 "Gpd1p, the other Gpd isoform, is partly cytosolic and partly peroxisomal and becomes more strictly peroxisomal in respiratory-deficient mutants."]
- PTS2/Pex7 import [PMID:20026609 "Here, we show that Gpd1p is directed to peroxisomes by virtue of an N-terminal type 2 peroxisomal targeting signal (PTS2) in a Pex7p-dependent manner."]; nucleus under osmotic stress [PMID:20026609 "Exposure of cells to osmotic stress induces changes in the subcellular distribution of Gpd1p to the cytosol and nucleus."]
- Piggyback carrier for Pnc1p [PMID:26276932 "Pnc1p, a nicotinamidase without functional PTS2, is co-imported into peroxisomes by piggyback transport via Gpd1p."]
- Mitochondrion HDA (PMID:24769239) unsupported by targeted work -> marked over-annotated.

## Curation observations
- [NAD(P)+] GPDH rows (IBA/IMP/RCA) -> MODIFY to NAD+-specific GO:0141152.
- InterPro2GO 'glycerol-3-phosphate catabolic process' is direction-wrong for this enzyme in vivo -> MODIFY to G3P biosynthetic process.
- YeastPathways superpathway RCA 'phospholipid biosynthetic process' marked over-annotated; PA biosynthesis kept non-core.
