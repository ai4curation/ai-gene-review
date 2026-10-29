# PA1058 (Q9I4R6, ShaF) notes

## 2026-10-28 review (PseudoCAP IBA-seed worklist, rank 63)

No deep-research provider was available; literature collected by PubMed search
and cached abstracts or full texts. PMID:16030218 (Kosono et al. 2005) is
abstract-only here (PMC1196046 is a scanned PDF). Verdicts kept consistent
with the completed PA1055 (ShaC) and PA1057 (ShaE) reviews.

### Identity

- UniProt Q9I4R6 (unreviewed, PE 3), 89 aa, two predicted TM helices (34-53,
  60-83). InterPro IPR007208 MrpF/PhaF-like; Pfam PF04066; NCBIfam
  NF004812; PANTHER PTHR34702:SF1 [file:PSEAE/PA1058/PA1058-uniprot.txt].
  The UniProt name "K+/H+ antiporter subunit F" is a ProtNLM prediction, not
  evidence of K+ specificity.
- Fifth gene of the sha cluster PA1054-PA1059; by gene order and family,
  PA1058 = ShaF (MrpF).

### What PMID:16030218 shows

- Whole-cluster complementation of E. coli TO114, lost when PA1054 is
  deleted; the abstract reports disruption of PA1054 only [PMID:16030218 "We disrupted PA1054 (a shaA
  homologue gene) and determined its effect on Na+ tolerance during growth,
  Na+ efflux, and pathogenicity in mice."]. The abstract describes no PA1058 mutant, so IMP looks wrong for PA1058 (full text not read).

### MrpF biology (family)

- MrpF-D32A loses antiport and complex [PMID:29218041 "In category 1,
  MrpD-D75A, MrpD-R258A, MrpE-T113Y, and MrpF-D32A were studied, and their
  Na+/H+ antiport activity was found to be completely lost, with no Mrp
  complex detected."].
- MrpF = MBH subunit B [PMID:29754813 "Mutations D32A and R33A in MrpF,
  equivalent to D29 and R30 of MBH subunit B, either abolished (D32A) or
  reduced (R33A) the H+/Na+ antiporter activity"].
- B. subtilis MrpF has a possible stand-alone role [PMID:11004162
  "Expression of mrpF in the mrp null (VKN1) strain also restored cholate
  transport and increased Na+ efflux, indicating that MrpF does not require
  even low levels of other mrp gene expression for its own function."].
  This does not change the GO:0015385 assessment (Na+/H+ antiport of the
  Sha complex), but is a question for ShaF.
- Complex needed for antiport [PMID:20624916 "Antiport activity requires
  hetero-oligomeric complexes of all six or seven hydrophobic Mrp proteins
  (MrpA-MrpG)."].

### PAINT node (PA1058-bioinformatics/RESULTS.md)

PTN002162906 = PTHR34702 root (LUCA), 19 leaves/16 taxa. GOA: 19 GO_Central
GO:0015385 IBAs plus 272 TreeGrafter rows with the same with/from (live
QuickGO). Sole seed PA1058. B. subtilis MrpF (O05228) has no experimental
GO:0015385 row. No GO:0035725 IBA from this node. Includes Thermococcus MBH
subunit B proteins TK2081 (MbhB) and TK1225 (MbxB).

### Annotation decisions

- GO:0015385 (IBA, IMP): ACCEPT (core) as contributes_to; PSEUDOCAP
  WRONG_EVIDENCE_CODE CHECK and WRONG_QUALIFIER REPOINT; GO_CENTRAL
  WRONG_QUALIFIER CHECK (plus MBH reach).
- GO:0035725 (IMP): ACCEPT; IMP code flagged. Seeds no IBD.
- GO:0015075, GO:0015297: MODIFY to GO:0015385. GO:0034220: MODIFY to
  GO:0035725. GO:0016020: MODIFY to GO:0005886. GO:0005886: ACCEPT.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN002162906 | GO:0015385 sodium:proton antiporter activity | 1 (sole) | 19 (GO_Central; plus 272 TreeGrafter) | GO:0015385, IMP, PMID:16030218 | INDIRECT-PHENOTYPE | The abstract describes no PA1058 mutant. The evidence is a PA1054 disruption plus whole-cluster complementation of E. coli TO114, which shows the Sha complex is an antiporter. Right as `contributes_to` (MrpF Asp32 is needed for antiport and assembly), not as `enables` + IMP. The LUCA-root node also covers MBH/MBX hydrogenase subunit B proteins (TK2081, TK1225), for which a stand-alone antiporter MF is doubtful. |

## Audit 2026-10-29: confidence matched to what was read

PMID:16030218 is still abstract-only here: the PubMed MCP returns no body
text (the PMC copy, PMC1196046, is a scanned PDF the publisher does not
release as XML), and the PMC, Europe PMC and ASM pages were not retrievable.
The WRONG_EVIDENCE_CODE (IMP) defects on this gene rest on the abstract not
describing a mutant of this gene, so they are lowered from PROBABLE to
SUSPECTED. The WRONG_QUALIFIER defects (enables vs contributes_to) rest on
positive statements in other Mrp papers and stay PROBABLE. The reference
correctness for PMID:16030218 is changed from MISCITED to UNVERIFIED.
Annotation actions are unchanged.
