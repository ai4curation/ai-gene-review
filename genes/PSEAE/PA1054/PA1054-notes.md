# PA1054 (Q9I4S0, ShaAB) notes

## 2026-10-28 review (PseudoCAP IBA-seed worklist, rank 68)

No deep-research provider was available; literature collected by PubMed search
and cached abstracts or full texts. The PseudoCAP-cited paper (PMID:16030218,
Kosono et al. 2005) is abstract-only here (PMC1196046 is a scanned PDF). Sister
reviews of the same cluster: PA1055 (ShaC) and PA1057 (ShaE), with PA1056,
PA1058 and PA1059 reviewed in the same session.

### Identity

- UniProt Q9I4S0 (unreviewed, PE 4), 933 aa, about 22 predicted TM helices.
  InterPro IPR050616 CPA3_Na-H_Antiporter_A, IPR001750 ND/Mrp_TM,
  IPR001516 Proton_antipo_N, IPR025383/IPR046806 MrpA_C, IPR007182 MnhB;
  Pfam PF00361, PF00662, PF13244 MbhD, PF20501 MbhE, PF04039 MnhB; PANTHER
  PTHR43373:SF1 [file:PSEAE/PA1054/PA1054-uniprot.txt]. The UniProt name
  "Probable NADH dehydrogenase" is the submitter's name, not a finding.
- First gene of the six-gene sha cluster PA1054-PA1059. The MnhB Pfam match
  in the C-terminal part matches the A-B fusion found in Gram-negative Mrp
  operons [PMID:29218041 "This group belongs to bacteria such as Pseudomonas
  aeruginosa and Vibrio cholerae, in which it appears that the mrpA gene is
  fused with the mrpB gene encoding a fusion protein"]. So PA1054 = ShaAB.
  Gene order and families give PA1055 = C, PA1056 = D, PA1057 = E,
  PA1058 = F, PA1059 = G.

### What PMID:16030218 shows for PA1054

- Cluster lacking PA1054 fails to complement E. coli TO114 [PMID:16030218
  "The gene cluster PA1054 to PA1059, but not the cluster with a deletion of
  PA1054, complemented a growth defect in the presence of 0.2 M NaCl and a
  defect in Na+/H+ antiport activity of the Escherichia coli TO114 mutant"].
- PA1054 disruption in P. aeruginosa [PMID:16030218 "Disruption of PA1054
  resulted in severe Na+ sensitivity during growth and decreased Na+ efflux
  activity."] and attenuated virulence [PMID:16030218 "In mice, the deletion
  mutant of PA1054 also exhibited an attenuated virulence in systemic,
  pulmonary, and urinary tract infections"].
- So, unlike PA1055-PA1059, PA1054 has a real mutant phenotype. IMP is the
  right code for both PseudoCAP rows on PA1054.

### Mrp family biology for MrpA

- No antiport with MrpA alone [PMID:29218041 "In previous studies, none of
  the Mrp antiporters exhibited antiport activity with MrpA or MrpD alone."];
  complex needed [PMID:20624916 "Antiport activity requires hetero-oligomeric
  complexes of all six or seven hydrophobic Mrp proteins (MrpA-MrpG)."].
- B. subtilis mrpA deletion is Na+-sensitive and complemented in trans
  [PMID:21236240 "Deletion of either mrpA or mrpD from the Bacillus subtilis
  chromosome resulted in a Na+ and pH sensitive growth phenotype."]; model
  [PMID:21236240 "Presumably, MrpA transports Na+ whereas MrpD transports H+
  in opposite directions, resulting in antiporter activity."]. The structure
  gives MrpA a proton path [PMID:36241630 "His248MrpA accepts the proton from
  Lys353MrpA and delivers it to the conserved Lys/Glu pair of the MrpA
  subunit"]. The MrpA C-terminal domain is needed at pH 8.4, where complex
  formation is needed [PMID:24021651 "at pH 8.4, where Mrp-complex formation
  is needed for function, the C-terminal domain of MrpA was absolutely
  required"].
- Archaeal MBH lacks MrpA [PMID:29754813 "MrpA is the only Mrp subunit that
  does not have a homolog in MBH"].

### PAINT node (PA1054-bioinformatics/RESULTS.md)

PTN000511949 = PTHR43373 root (LUCA), 16 leaves/15 taxa, 16 GO_Central IBAs
per term. GO:0015385 seeds: PA1054 and B. subtilis MrpA Q9K2S2 (IMP,
PMID:20509166). GO:0035725 seed: PA1054 only. No Thermococcus MBH leaf; one
hydrogenase-named leaf (Sulfolobus SSO1021 "HycC").

### Annotation decisions

- GO:0015385 (IBA, IMP): ACCEPT (core), qualifier should be contributes_to;
  PSEUDOCAP WRONG_QUALIFIER REPOINT and GO_CENTRAL WRONG_QUALIFIER CHECK.
  No evidence-code defect (PA1054 was mutated).
- GO:0035725 (IBA, IMP): ACCEPT.
- GO:0005886 plasma membrane: ACCEPT; GO:0016020 membrane: MODIFY to plasma
  membrane.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN000511949 | GO:0015385 sodium:proton antiporter activity | 2 | 16 | GO:0015385, IMP, PMID:16030218 | SOUND | PA1054 is the one sha gene the paper deleted: the cluster lacking PA1054 no longer restores antiport in E. coli TO114, and the P. aeruginosa disruptant loses Na+ tolerance and Na+ efflux. The node is the MrpA family root (no MBH members; one HycC-named Sulfolobus leaf). Caveat: activity is of the complex (no Mrp shows antiport with MrpA alone), so the qualifier should be `contributes_to`, for the seed and for the IBD. A second, independent seed (B. subtilis MrpA, IMP) supports the node. |
| PTN000511949 | GO:0035725 sodium ion transmembrane transport | 1 (sole) | 16 | GO:0035725, IMP, PMID:16030218 | SOUND | Direct mutant evidence: PA1054 disruption decreases Na+ efflux. MrpA carries putative ion translocation pathways, and the process fits all MrpA-family members. |
