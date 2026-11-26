# MVP1 (At1g54030; ERMO3/GOLD36/NUC/GLL25) - manual literature research

No deep-research API was available; this summary was compiled manually from
cached publications (publications/PMID_*.md) and a PubMed search
(`(MVP1 OR GOLD36 OR ERMO3 OR At1g54030) AND Arabidopsis`, 7 hits).

## Identity

- UniProt Q7XA74 (GDL21_ARATH), 417 aa, "Inactive GDSL esterase/lipase-like protein 25",
  TAIR AT1G54030, GeneID 841841. Predicted signal peptide 1-50, three N-glycosylation
  sites, no transmembrane segment (UniProt FT).
- GDSL lipase family (Pfam PF00657; PANTHER PTHR45966:SF36); belongs to the
  myrosinase-associated protein (MyAP)/GLL cluster that includes ESM1 and GLL23.
- The block-I catalytic motif is GDGL instead of GDSL [PMID:19880612 "its putative
  lipolytic sequence was divergent from the canonical GDSL motif, which in wild-type
  Col-0 plants is GDGL"].

## Four independent forward-genetic identifications

1. mvp1 (Agee et al. 2010, PMID:19880612, full text): GFP-deltaTIP screen; perinuclear
   aggregates of endomembrane markers; salt sensitivity, gravitropic and growth defects;
   GST pull-down shows interaction with myrosinase TGG2 but not TGG1; TGG2-GFP and
   TGG1-GFP trapped in aggregates; increased nitrile production on glucosinolate
   hydrolysis. Recombinant MVP1 had no esterase activity on p-nitrophenyl acetate and no
   lipase/esterase activity on tributyrin/Tween plates [PMID:19880612 "MVP1 does not act
   as a lipase or esterase"]. Transient MVP1-GFP labelled ER, ER bodies and (by
   transvacuolar strands) tonoplast.
2. gold36 (Marti et al. 2010, PMID:20626647, abstract only): ST-GFP Golgi marker screen;
   P80L mutation; ER bulges and skein-like structures; defective ER export of Golgi
   markers and of a secreted bulk-flow marker. GOLD36 is a vacuolar protein; mutant form
   retained in ER [PMID:20626647 "Subcellular localization analyses indicated that GOLD36
   is a vacuolar protein and that its mutated form is retained in the ER"].
3. ermo3 (Nakano et al. 2012, PMID:23155454, full text): SP-GFP-HDEL screen; ER aggregates
   only in ER-body-developing (NAI1-expressing) cells; loss of NAI1 suppresses
   aggregation; ERMO3-tagRFP in vacuolar lumen (and ER, cleared by cycloheximide, i.e.
   transit) [PMID:23155454 "ERMO3-tagRFP was translated in the ER and transported to the
   vacuolar lumen"]; ERMO3-Venus-HDEL (ER/Golgi cycling) complements; G59S variant
   (restored catalytic Ser) also complements, so enzymatic activity is not needed; Co-IP/MS
   finds PYK10 complex components (PYK10, PBP1, JALs, GLLs); ER-Golgi transport defect is
   interpreted as secondary to ER disorganization [PMID:23155454 "the defective protein
   transport observed in ermo3 cells was the secondary effect caused by abnormal
   organization of the ER"].
4. nuc (Jancowski et al. 2014, PMID:24330158, abstract only): GLL23 accumulates in
   perinuclear ER aggregates in nuc (G341R); NUC needed for GLL23 ER export; the p24
   protein CYB needed for GLL23 and NUC export [PMID:24330158 "Without NUC, GLL23
   accumulates in the ER this situation suggests that NUC is in fact active in the ER"].
5. alp4 (Underwood 2022, PMID:35147444, abstract only): a GOLD36 allele that mistargets
   PEN3 ABC transporter and reduces penetration resistance to powdery mildew.

## Proteomics

- Vacuole proteome of rosette-leaf vacuoles (PMID:15539469) found At1g54030 among
  myrosinase-associated proteins.
- Plasmodesmal proteome (PMID:21533090) gives the plasmodesma HDA row; At1g54030 is not
  named in the cached text (supplementary table).

## Synthesis

MVP1 is a catalytically inactive GDSL-lipase-like (pseudoenzyme) secretory protein that
transits the ER and ends in the vacuole lumen. Its job, defined genetically, is to keep the
ER (and the organelles enmeshed in it) from aggregating, specifically in cells that make ER
bodies and the PYK10 complex. It binds PYK10-complex components and TGG2 and is needed for
ER export of GLL23 and for correct targeting of TGG2 and PEN3. Its molecular activity is
unknown; a chaperone- or inhibitor-like action on the PYK10/myrosinase complexes is
proposed but untested.
