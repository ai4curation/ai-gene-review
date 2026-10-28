# PA1056 (Q9I4R8, ShaD) notes

## 2026-10-28 review (PseudoCAP IBA-seed worklist, rank 69)

No deep-research provider was available; literature collected by PubMed search
and cached abstracts or full texts. PMID:16030218 (Kosono et al. 2005) is
abstract-only here (PMC1196046 is a scanned PDF). Verdicts kept consistent
with the completed PA1055 (ShaC) and PA1057 (ShaE) reviews.

### Identity

- UniProt Q9I4R8 (unreviewed, PE 3), 499 aa, 14 predicted TM helices.
  InterPro IPR050586 CPA3_Na-H_Antiporter_D, IPR003918 NADH_UbQ_OxRdtase,
  IPR001750 ND/Mrp_TM; Pfam PF00361; PANTHER PTHR42703:SF1
  [file:PSEAE/PA1056/PA1056-uniprot.txt]. "Probable NADH dehydrogenase" is
  the submitter's name.
- Third gene of the sha cluster PA1054-PA1059. With PA1054 = ShaAB (fused,
  PMID:29218041) and PA1055 = ShaC, gene order and family (CPA3 subunit D)
  make PA1056 = ShaD (MrpD).

### What PMID:16030218 shows

- Whole-cluster complementation of E. coli TO114, lost when PA1054 is
  deleted; only PA1054 disrupted in P. aeruginosa [PMID:16030218 "We
  disrupted PA1054 (a shaA homologue gene) and determined its effect on Na+
  tolerance during growth, Na+ efflux, and pathogenicity in mice."]. So
  there is no PA1056 mutant: IMP cannot apply to PA1056.

### MrpD biology (family)

- B. subtilis mrpD deletion is Na+ and pH sensitive [PMID:21236240
  "Deletion of either mrpA or mrpD from the Bacillus subtilis chromosome
  resulted in a Na+ and pH sensitive growth phenotype."]; proposed H+
  carrier [PMID:21236240 "Presumably, MrpA transports Na+ whereas MrpD
  transports H+ in opposite directions, resulting in antiporter activity."].
- MrpD needed for complex formation [PMID:29218041 "These results suggested
  that the MrpD subunit is important in the formation of the Bp–Mrp
  complex."]; no antiport with MrpD alone [PMID:29218041 "In previous
  studies, none of the Mrp antiporters exhibited antiport activity with MrpA
  or MrpD alone."].
- Structural model [PMID:36241630 "Binding of the first proton to the
  Lys/Glu pair of MrpD drives the transfer of sodium bound at SLS1"].
- MrpD is homologous to complex I NuoM/NuoN [PMID:29218041 "MrpD has the
  closest homology to complex I NuoM and NuoN subunits."], which explains the
  IPR003918 InterPro2GO rows (NADH dehydrogenase, respiratory electron
  transport). The sha cluster has no redox subunits, so those are wrong for
  PA1056.

### PAINT node (PA1056-bioinformatics/RESULTS.md)

PTN001865541 = Eubacteria node of PTHR42703 (root PTN000511965, LUCA, 28
leaves), 16 leaves/13 taxa, 16 GO_Central IBAs per term. GO:0015385 seeds:
B. subtilis MrpD O05229 (IMP, PMID:20509166) and PA1056. GO:0035725 seed:
PA1056 only. The archaeal MBH/MBX subunit-H proteins (TK2087, TK1220,
TK1219) are in the Archaea-Eukaryota branch, outside the node. Possible
non-antiporter leaves: Leptospira LA_4273 ("Formate hydrogenase subunit B"),
Thermotoga TM_1105/TM_1211, Rhodopirellula RB1430/RB1431.

### Annotation decisions

- GO:0015385 (IBA, IMP): ACCEPT (core) as contributes_to; defects: PSEUDOCAP
  WRONG_EVIDENCE_CODE CHECK and WRONG_QUALIFIER REPOINT; GO_CENTRAL
  WRONG_QUALIFIER CHECK.
- GO:0035725 (IBA, IMP): ACCEPT; IMP code flagged (CHECK).
- GO:0008137 NADH dehydrogenase (ubiquinone) and GO:0042773 ATP synthesis
  coupled electron transport (InterPro2GO IPR003918): REMOVE.
- GO:1902600 proton transmembrane transport (GO_REF:0000108 from GO:0008137):
  ACCEPT; true on its own grounds for an antiporter subunit.
- GO:0005886 plasma membrane: ACCEPT; GO:0016020 membrane: MODIFY.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN001865541 | GO:0015385 sodium:proton antiporter activity | 2 | 16 | GO:0015385, IMP, PMID:16030218 | INDIRECT-PHENOTYPE | No PA1056 mutant was made; the evidence is a PA1054 disruption plus whole-cluster complementation of E. coli TO114. Right only as `contributes_to` (subunit of the antiporter complex). The IBD itself survives: an independent B. subtilis MrpD IMP seed supports it, and the bacterial node excludes the archaeal MBH subunits. The IBD qualifier should still be `contributes_to`. |
| PTN001865541 | GO:0035725 sodium ion transmembrane transport | 1 (sole) | 16 | GO:0035725, IMP, PMID:16030218 | SOUND | As a subunit of the complex responsible for Na+ extrusion, PA1056 takes part in Na+ transmembrane transport; structural models couple MrpD protonation to Na+ transfer. The process fits the bacterial MrpD clade. Caveat: IMP is the wrong code for PA1056; filed as a CHECK. |
