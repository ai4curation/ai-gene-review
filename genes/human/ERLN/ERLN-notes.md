# ERLN (endoregulin, SMIM6; UniProt P0DI80) - review notes

## 2026-09-30 - initial review (claude-code)

### Identity
- Human ERLN, 62 aa, single predicted TM helix (UniProt TRANSMEM 25..45), cytosolic
  N-terminus, short luminal C-terminal tail. Former symbols C17orf110, SMIM6. Mouse
  ortholog Q3U0I6 (Elnl / 1110017F19Rik), 56 aa.
- GOA (human): only two rows, both GO:0005789 ER membrane (IEA from UniProt SubCell;
  ISS from mouse Q3U0I6). PAN-GO: no IBA. No human MF or BP annotation at all.
- Mouse Q3U0I6 GOA: IDA ER membrane, IPI protein binding (SERCA2b), IDA
  acts_upstream_of_or_within GO:1901895 negative regulation of ATPase-coupled calcium
  transmembrane transporter activity - all from PMID:27923914.

### Discovery - mouse (PMID:27923914, Anderson et al. 2016 Sci Signal; PubMed-verified)
- Found by screening the mouse genome for the SERCA-binding motif
  [PMID:27923914 "we used a bioinformatics approach to screen the mouse genome for potential open reading frames containing the SERCA binding motif of MLN, PLN, and SLN"].
- ER colocalisation with SERCA2b in COS-7 cells
  [PMID:27923914 "Similar to MLN, PLN, and SLN, ALN and ELN perfectly colocalized with mCherry-SERCA2b in a pattern consistent with the reticulated membranes of the ER"].
- Co-IP with SERCA2b, competed by PLN (same binding groove)
  [PMID:27923914 "All of the micropeptides formed a stable complex with Myc-SERCA2b, but not with the Myc-tag alone"].
- Ca uptake: lowers apparent Ca affinity (KCa) of SERCA3a, no Vmax change
  [PMID:27923914 "coexpression of ALN or ELN caused a significant reduction in the apparent affinity for Ca2+ of SERCA2b and SERCA3a, respectively"].
- Expression: non-muscle epithelia, overlapping SERCA3
  [PMID:27923914 "ELN expression showed a large degree of overlap with that of SERCA3 in the epithelial cells of the trachea and bronchus, lung, intestine, pancreas, and liver"].
- All constructs in this paper are mouse (mouse genome screen, 56-aa ELN).

### Human-sequence experimental evidence
- PMID:34445594 (Rathod et al. 2021 IJMS, Young lab): recombinant HUMAN ELN
  [PMID:34445594 "With the exception of MLN, recombinant human peptides were expressed as a maltose-binding protein (MBP) fusion"]
  co-reconstituted with purified rabbit SERCA1a
  [PMID:34445594 "SERCA1a was purified from rabbit skeletal muscle SR and this isoform was used for all functional measurements."]
  lowers Vmax, not KCa
  [PMID:34445594 "whereas ELN selectively alters the turnover rate (Vmax) of SERCA (Figure 7C)"].
  This is a purified two-component system: direct evidence that the human peptide itself
  inhibits the pump. Note the mechanistic discrepancy with the mouse data (KCa effect on
  SERCA3a in cell homogenates vs Vmax effect on SERCA1a in proteoliposomes); both are
  inhibitory. The authors themselves note the isoform caveat
  [PMID:34445594 "It should be noted that our reconstitution system used SERCA1a, while the primary targets of ALN and ELN are SERCA2b and SERCA3a, respectively."].
- PMID:36523160 (Phillips et al. 2023 Biophys J, Robia lab): human sequences
  [PMID:36523160 "human sequences of all micropeptides (PLB, SLN, DWORF, ALN, and ELN) were labeled using either mCerulean or YFP"];
  ELN homo- and hetero-oligomerises with PLN, SLN, ALN, DWORF (FRET in cells). This is
  the source of UniProt's SUBUNIT annotation (ECO:0000269).
- PMID:31449798 (Singh et al. 2019 JMB, Robia lab): micropeptides incl. ELN oligomerise
  but bind SERCA as monomers
  [PMID:31449798 "Micropeptides formed avid homo-oligomers with high-order stoichiometry (n > 2 protomers per homo-oligomer), but it was the monomeric form of all micropeptides that interacted with SERCA."].
  Species of the ELN construct is not stated in the cached text; the 2023 paper later
  comments that mouse sequences are satisfactory models, implying earlier work used mouse.
- PMID:39921961 (Cunningham et al. 2025 Cell Calcium; abstract only): ELN lowers ER Ca2+
  content in live cells
  [PMID:39921961 "Sarcolipin (SLN), endoregulin (ELN), and another-regulin (ALN) also decreased ER Ca2+ content, though less potently than PLB."].
  Species of construct not stated in abstract.

### Physiology
- No loss-of-function or disease data
  [PMID:34445594 "There are no current physiological or disease-associated roles for ELN or ALN"].

### Comparators (QuickGO, 2026-09-30)
- PLN (P26678): GO:0042030 ATPase inhibitor activity IDA/IBA/ISS/IEA; GO:0004857 ISS;
  GO:0051117 ATPase binding ISS; GO:1901894 etc.
- SLN (O00631): GO:0004857 enzyme inhibitor activity ISS; GO:1901895 IDA; GO:1901894 IDA.
- So the SERCA-inhibitory regulins carry an inhibitor MF and a negative regulation of
  ATPase-coupled calcium transporter activity BP. ERLN is in the same role (the peptide
  itself binds and inhibits the pump) - participation test is satisfied: ELN is the
  regulator performing the regulatory step, not a substrate.

### Decisions
- Both ER membrane rows: ACCEPT (mouse IDA + human localisation consistent).
- NEW MF GO:0042030 ATPase inhibitor activity (IDA, PMID:34445594 human peptide,
  purified system; mouse data corroborate). Considered GO:0141110 transporter inhibitor
  activity, but PLN precedent and the assay (ATPase turnover) favour GO:0042030.
- NEW BP GO:1901895 negative regulation of ATPase-coupled calcium transmembrane
  transporter activity (mirrors mouse IDA and SLN IDA).
- Not proposed: identical protein binding (homo-oligomerisation) - binding-only term,
  functional significance unclear; ER calcium ion homeostasis - only abstract-level
  live-cell data; tissue-level processes - none established.
