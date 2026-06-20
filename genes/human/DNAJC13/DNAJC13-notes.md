# DNAJC13 (RME-8) research notes

## Identity
- UniProt O75165, HGNC:30343, 2243 aa. Large multidomain DnaJ/HSP40 subfamily C protein.
- AltName "Required for receptor-mediated endocytosis 8" (RME-8). Synonyms KIAA0678, RME8.
- Domain architecture: N-terminal membrane-association region (1-453), multiple ARM/HEAT-like
  repeats (Gene3D 1.25.10.10 x2; SUPFAM ARM repeat x3), GYF-like domain, and a single J domain
  near the C-terminus (residues 1301-1366). [file:human/DNAJC13/DNAJC13-uniprot.txt]
- Note: J domain is internal/C-terminal, NOT N-terminal as in canonical type-I/II HSP40s.

## Core function: endosomal HSC70 co-chaperone / clathrin dynamics
- Co-chaperone of HSC70 (HSPA8). The J domain stimulates HSC70 ATPase to drive clathrin uncoating
  on endosomes, regulating retrieval/recycling sorting. (Established in C. elegans and conserved.)
- UniProt FUNCTION: "Involved in membrane trafficking through early endosomes, such as the early
  endosome to recycling endosome transport implicated in the recycling of transferrin and the early
  endosome to late endosome transport implicated in degradation of EGF and EGFR ... Involved in the
  regulation of endosomal membrane tubulation and regulates the dynamics of SNX1 on the endosomal
  membrane; via association with WASHC2 may link the WASH complex to the retromer SNX-BAR subcomplex"
  [file:human/DNAJC13/DNAJC13-uniprot.txt]

## Key experimental papers
- PMID:18256511 (Fujibayashi 2008): hRME-8 is a peripheral membrane protein tightly associated via
  N-terminal region, colocalizes with early (not late) endosomal markers, confined to Rab5aQ79L
  vacuoles. C-terminal truncations compromise transferrin recycling and EGF/EGFR degradation.
  "hRME is primarily involved in membrane trafficking through early endosomes, but not through
  degradative organelles". [PMID:18256511]
- PMID:18307993 (Girard & McPherson 2008): RME-8 depletion decreases EGFR via increased degradation;
  "implicate RME-8 in sorting decisions influencing EGFR at the level of endosomes". [PMID:18307993]
- PMID:24643499 (Freeman 2014): FAM21 (WASHC2) binds SNX1-interacting DNAJ protein RME-8. "Loss of
  RME-8 causes altered kinetics of SNX1 membrane association and a pronounced increase in highly
  branched endosomal tubules." Coordinates WASH complex with retromer SNX dimer membrane tubulation.
  [PMID:24643499]

## Disease
- DNAJC13 variants implicated in autosomal-dominant Parkinson disease (PARK21); p.Asn855Ser
  characterized as affecting endosomal membrane trafficking (transferrin accumulation in endosomal
  compartments). [PMID:24218364; PMID:25393719] (UniProt DISEASE/VARIANT). Pathogenicity later
  questioned (same family carried TMEM230 variants, PMID:27270108).

## Localization
- Early endosome / early endosome membrane / endosome membrane; peripheral membrane protein.
  IDA/EXP supported (PMID:18256511, PMID:24643499). [file:human/DNAJC13/DNAJC13-uniprot.txt]
- IEA SubCell terms (GO:0005769, GO:0010008, GO:0031901) redundant with experimental.
- HDA proteomics: membrane, extracellular exosome, lysosomal membrane — bulk MS, non-core.
- Reactome TAS: plasma membrane, secretory/azurophil granule membrane (neutrophil degranulation
  pathway R-HSA-6798739/6798743) — bulk granule proteome, peripheral to core endosomal function.

## GOA interaction partners (IPI GO:0005515)
- PMID:28514442, PMID:33961781 WITH O15126 = SCAMP1 (also in UniProt INTERACTION block).
- PMID:24643499 WITH A8K0Z3 (WASHC2C/FAM21), Q12768 (WASHC5/strumpellin/KIAA0196), Q9Y4E1 (WASHC2A/FAM21A).
  These are WASH complex subunits — informative; reflects WASH-complex binding.

## Curation decisions
- Core MF: not captured well by GOA (only bare protein binding). True MF = Hsp70/HSC70 co-chaperone
  (ATPase activator / Hsp70 binding via J domain) acting in endosomal clathrin dynamics. GOA lacks
  the J-domain MF terms; propose core functions for ATPase activator activity + Hsp70 binding, plus
  the well-supported BP of endosome organization / regulation of endosomal transport.
- receptor-mediated endocytosis (IBA): historical name; RME-8 acts on endosomes downstream of
  internalization rather than at the RME step per se. Keep as non-core (broadly correct process).
