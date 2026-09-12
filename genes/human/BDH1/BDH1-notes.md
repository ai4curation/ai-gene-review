# BDH1 (Q02338) review notes

## Gene identity
- D-beta-hydroxybutyrate dehydrogenase, mitochondrial (BDH; SDR9C1). HGNC:1027, EC 1.1.1.30.
- Member of the short-chain dehydrogenase/reductase (SDR) family; NAD(P)-binding Rossmann fold
  [file:human/BDH1/BDH1-uniprot.txt "Belongs to the short-chain dehydrogenases/reductases (SDR) family"].
- 343 aa precursor; N-terminal mitochondrial transit peptide 1..46; mature chain 47..343
  [file:human/BDH1/BDH1-uniprot.txt TRANSIT 1..46; CHAIN 47..343].

## Verified core biology
- NAD+-dependent D-beta-hydroxybutyrate dehydrogenase catalysing the reversible interconversion
  of the two ketone bodies: (R)-3-hydroxybutanoate + NAD+ ⇌ acetoacetate + NADH + H+
  [file:human/BDH1/BDH1-uniprot.txt "Reaction=(R)-3-hydroxybutanoate + NAD(+) = acetoacetate + NADH + H(+)"; EC=1.1.1.30].
- Terminal step of ketogenesis (making beta-hydroxybutyrate, the main circulating ketone) and the
  first step of ketolysis (regenerating acetoacetate in peripheral tissues). Reactome represents
  both directions: R-HSA-73912 (acetoacetate + NADH -> BHB, synthesis direction) and
  R-HSA-73920 (BHB + NAD+ -> acetoacetate, utilization direction). UniProt DR: Reactome
  R-HSA-77108 Utilization of Ketone Bodies; R-HSA-77111 Synthesis of Ketone Bodies.
- Lipid-dependent enzyme: requires phosphatidylcholine as an allosteric activator
  [file:human/BDH1/BDH1-uniprot.txt "Requires phosphatidylcholine as an allosteric"]
  [PMID:8679568 "enzyme with a specific requirement of phosphatidylcholine (PC) for function"].
- Homotetramer [file:human/BDH1/BDH1-uniprot.txt "Homotetramer"].
- Localization: mitochondrion inner membrane / matrix side; also detected in matrix
  [file:human/BDH1/BDH1-uniprot.txt "Mitochondrion inner membrane"].

## Experimental evidence
- PMID:8679568 (Green et al. 1996, Biochemistry): expressed mature human heart BDH in Sf9 insect
  cells; catalytically active, Km for NAD+ and (R)-3-hydroxybutyrate similar to native enzyme;
  PC requirement confirmed; C-terminal region required for catalysis/lipid binding. Supports the
  IDA for GO:0003858 3-hydroxybutyrate dehydrogenase activity (abstract-only cache; full text read
  by curator).
- PMID:34800366 (MitoCoP, Cell Metab 2021): high-confidence human mitochondrial proteome (1,134
  genes); supports HTP mitochondrion localization.

## Annotation-decision summary
- Core MF: GO:0003858 3-hydroxybutyrate dehydrogenase activity (IBA + IEA-RHEA/EC + IDA) -> ACCEPT.
- GO:0016616 (oxidoreductase acting on CH-OH, NAD/NADP acceptor) is a direct parent of GO:0003858;
  ARBA IEA is not wrong but is redundant/less informative -> MARK_AS_OVER_ANNOTATED.
- Ketone-body processes: the Ensembl IEA terms GO:0042181 "ketone biosynthetic process" and
  GO:0042182 "ketone catabolic process" are more general than the ketone-BODY-specific terms.
  BDH1 acts specifically on the ketone body beta-hydroxybutyrate/acetoacetate, so MODIFY to
  GO:0046951 ketone body biosynthetic process and GO:0046952 ketone body catabolic process.
  (Note GO:1902224 "ketone body metabolic process" is OBSOLETE, verified via QuickGO 2026-07.)
- Locations: mitochondrial inner membrane (IBA/IEA/ISS), matrix side of inner membrane (ISS,
  most precise), matrix (IEA/ISS/TAS), mitochondrion (HTP) -> all ACCEPT (inner-membrane-anchored,
  matrix-facing active site).
- Reactome CLPXP TAS rows (R-HSA-9838035 binds, R-HSA-9838289 degrades): these place BDH1 in the
  matrix as a generic CLPXP protease substrate, not a BDH1-specific function. The matrix
  localization is fine; keep as non-core.

## Term-label verification (QuickGO, 2026-07)
- GO:0003858 3-hydroxybutyrate dehydrogenase activity (MF, current)
- GO:0005743 mitochondrial inner membrane (CC, current)
- GO:0005759 mitochondrial matrix (CC, current)
- GO:0016616 oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor (MF)
- GO:0046951 ketone body biosynthetic process (BP, current)
- GO:0046952 ketone body catabolic process (BP, current)
- GO:0099617 matrix side of mitochondrial inner membrane (CC, current)
- GO:0005739 mitochondrion (CC, current)
- GO:0051287 NAD binding (MF, current)
