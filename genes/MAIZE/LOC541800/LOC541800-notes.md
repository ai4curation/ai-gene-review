# LOC541800 (ZmYS1) review notes

## 2026-10-28 session

- `just fetch-gene MAIZE LOC541800` resolved A0A1D6HET4 (GeneID 541800, Zm00001eb249020), 6 GOA rows
  (3 IBA from PTN001270331, 3 IEA). Accession confirmed as requested; no switch.
- Identity: NCBI Gene 541800 = "yellow stripe 1" (ys1, zmYS1, GRMZM2G156599). The Swiss-Prot entry
  YS1_MAIZE Q9AY27 is the same gene (4 residue differences, 682 aa both). The Ueno 2009 antibody
  peptide DEMAALDDLQRDEI (377-390) matches A0A1D6HET4 exactly
  [PMID:19549626 "Antibody against ZmYS1 was prepared by immunizing rabbits with a synthetic peptide C-DEMAALDDLQRDEI (positions 377–390 of ZmYS1)"].
- Full text read: PMID:19549626 (Ueno 2009), PMID:23667491, PMID:21831857, PMID:16815956.
  Abstract only: PMID:11201743 (Curie 2001), PMID:14699112 (Schaaf 2004), PMID:15107503 (Roberts 2004),
  PMID:17707820, PMID:15255869.
- Core activity: proton-coupled uptake of Fe(III)-phytosiderophore
  [PMID:14699112 "ZmYS1 encodes a proton-coupled broad-range metal-phytosiderophore transporter that additionally transports Fe- and Ni-nicotianamine"].
  Chosen terms: GO:0015343 siderophore-iron transmembrane transporter activity (definition is
  siderophore-iron + H+ symport) and GO:0051980 iron-nicotianamine transmembrane transporter activity.
  Caveat: ChEBI classes phytosiderophore (CHEBI:38155) as iron chelator / iron ionophore, not under
  the "siderophore role" grouping class that GO:0015343 references; raised as a suggested question.
- BP: GO:0033214 siderophore-iron import into cell (Fe-PS uptake into root epidermal cells).
- InterPro2GO oligopeptide transporter MF (and the inferred oligopeptide transport BP) are the
  wrong substrate class for the YSL clade; MODIFY + source_defects.
- IBA "response to iron ion": PAINT seeds are Arabidopsis IEP rows (expression); ZmYS1 expression is
  Fe-regulated but the protein is not a participant in sensing/responding -> MARK_AS_OVER_ANNOTATED.
- IBA "seed development": seeded by AtYSL1 IGI/AtYSL3 (Waters 2006 / Chu 2010); no maize data ->
  MARK_AS_OVER_ANNOTATED.
- Plasma membrane IBA accepted (immunostaining in planta, PMID:19549626).
- No NEW rows: the core MF/BP terms are reached through MODIFY of the IEA rows.
