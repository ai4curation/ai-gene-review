# AVR-Pia (PYROR, UniProt B9WZW9) curation notes

## 2026-10-10 initial review

Sources: UniProt entry (TrEMBL, 85 aa, signal peptide 1-19, disulfide C25-C66,
PDB 2MYW/2N37/6Q76/9RSV), the Falcon deep-research report, and cached full text of
PMID:25024433, 28087830, 19454732, 27528510, 26506000, 42441725 (PMID:23548743 is
abstract only).

### Identity and structure
- Cloned as pex22 by association genetics; recognised inside Pia rice cells
  [PMID:19454732 "whose products are recognized inside rice cells possessing the cognate R genes"].
- Signal-peptide-less expression in Pia rice gives faster cell death
  [PMID:19454732 "supporting the idea that pex22 is recognized by Pia inside rice cells"].
- MAX effector fold, shared with AVR1-CO39, AvrPiz-t, ToxB
  [PMID:26506000 "Despite a lack of sequence similarity, both proteins have very similar 6 β-sandwich structures"].

### Expression and location
- Infection-specific; accumulates in BIC and enters host cytosol
  [PMID:27528510 "AVR-Pia accumulates in biotrophic interfacial complexes before being delivered to the plant cytosol"].

### Recognition by RGA4/RGA5
- Direct binding to RGA5-A; inactive allele does not bind
  [PMID:23548743 "Direct binding seems to be required for resistance as an inactive AVR-Pia allele did not bind RGA5-A."].
- AVR-Pia + RGA4 + RGA5 gives cell death in N. benthamiana and rice protoplasts; RGA4 is
  executor, RGA5 repressor/receptor
  [PMID:25024433 "Upon recognition of the pathogen effector AVR-Pia by direct binding to RGA5, repression is relieved and cell death occurs."].
- ITC Kd 7.8 uM to RGA5 RATX1; F24S abolishes binding and recognition; AVR-Pia also
  associates with RGA5 outside RATX1, but that is insufficient
  [PMID:28087830 "binding to the RATX1 domain is necessary for pathogen recognition but can be of moderate affinity"].

### Virulence targets
- Binds OsHPP09 (Kd 115 nM), OsHPP11, OsHIPP21, OsHPP10 HMA domains
  [PMID:42441725 "AVR-Pia bound to OsHPP09-HMA with an apparent KD of 115 nM"];
  outcome of binding unknown
  [PMID:42441725 "It is unknown whether the interactions of AVR-Pia, AVR-Pik, and Pwl2 with OsH(I)PPs lead to similar outcomes"].

### Curation decisions
- All three GO:0140404 rows (PHI-base, EXP/IDA) -> MODIFY to GO:0080185 effector-mediated
  activation of plant HR by symbiont (descendant of GO:0140404, verified on QuickGO). The
  only demonstrated immune effect of AVR-Pia is recognition-triggered HR/resistance; no
  immune suppression shown. Same treatment as FULFL/AVR9.
- NEW: GO:0030430 host cell cytoplasm (PMID:27528510). RGA5 binding and host
  HMA-protein binding are left without an MF term (only generic protein binding would
  apply).
- Signaling receptor binding (GO:0005102) for RGA5 binding was drafted and then dropped
  on the comparator check: no fungal or oomycete gene product carries it with
  experimental evidence in GOA (QuickGO, 2026-10-10), and its definition is written for
  hormone/neurotransmitter-type receptors. Raised as a suggested question instead.
- Project question 1: annotations are symbiont-side terms and backed by experiments on
  the effector, not IEA. Question 5: RGA5 carries the receptor activity; AVR-Pia carries
  the ligand-side binding and the symbiont-side HR term.
