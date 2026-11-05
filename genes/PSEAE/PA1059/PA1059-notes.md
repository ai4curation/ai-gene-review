# PA1059 (Q9I4R5, ShaG) notes

## 2026-10-28 review (PseudoCAP IBA-seed worklist, rank 62)

No deep-research provider was available; literature collected by PubMed search
and cached abstracts or full texts. PMID:16030218 (Kosono et al. 2005) is
abstract-only here (PMC1196046 is a scanned PDF). Verdicts kept consistent
with the completed PA1055 (ShaC) and PA1057 (ShaE) reviews.

### Identity

- UniProt Q9I4R5 (unreviewed, PE 4), 115 aa, three predicted TM helices
  (12-33, 45-64, 76-99). InterPro IPR005133 PhaG_MnhG_YufB; Pfam PF03334;
  NCBIfam TIGR01300 CPA3_mnhG_phaG; PANTHER PTHR34703:SF1
  [file:PSEAE/PA1059/PA1059-uniprot.txt]. The name "Na+/H+ antiporter
  subunit G" is a ProtNLM prediction; the family matches are the evidence.
- Sixth (last) gene of the sha cluster PA1054-PA1059; by gene order and
  family, PA1059 = ShaG (MrpG).

### What PMID:16030218 shows

- Whole-cluster complementation of E. coli TO114, lost when PA1054 is
  deleted; the abstract reports disruption of PA1054 only [PMID:16030218 "We disrupted PA1054 (a shaA
  homologue gene) and determined its effect on Na+ tolerance during growth,
  Na+ efflux, and pathogenicity in mice."]. The abstract describes no PA1059 mutant, so IMP looks wrong for PA1059 (full text not read).

### MrpG biology (family)

- MrpG-P81A [PMID:29218041 "MrpG-P81A in category 7 did not retain Na+/H+
  antiport activity, but it was able to complement the sodium sensitivity of
  the E. coli KNabc."].
- MrpG = MBH subunit C [PMID:29754813 "Indeed, MBH subunit C P88 is
  equivalent to P81 in MrpG and in a previous study it was demonstrated that
  the H+/Na+ antiporter activity of Mrp was abolished when P81 is substituted
  by an alanine or a glycine"].
- Three-TMH subunit [PMID:36241630 "Each of the small subunits MrpC, MrpF,
  and MrpG consists of a linear arrangement of three TMH each."].

### PAINT node (PA1059-bioinformatics/RESULTS.md)

PTN002162936 = PTHR34703 root (LUCA), 19 leaves/16 taxa. GOA: 19 GO_Central
GO:0015385 IBAs plus 263 TreeGrafter rows (live QuickGO). Sole seed PA1059.
B. subtilis MrpG (O05227) has no experimental GO:0015385 row. No GO:0035725
IBA from this node. Includes Thermococcus MBH subunit C proteins TK2082
(MbhC) and TK1224 (MbxC).

### Annotation decisions

- GO:0015385 (IBA, IMP): ACCEPT (core) as contributes_to; PSEUDOCAP
  WRONG_EVIDENCE_CODE CHECK and WRONG_QUALIFIER REPOINT; GO_CENTRAL
  WRONG_QUALIFIER CHECK (plus MBH reach).
- GO:0035725 (IMP): ACCEPT; IMP code flagged. Seeds no IBD.
- GO:0015297 antiporter activity: MODIFY to GO:0015385. GO:0055085
  transmembrane transport: MODIFY to GO:0035725.
- NEW GO:0005886 plasma membrane (IC): the gene has no CC row; TM helices and
  complex membership agree.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN002162936 | GO:0015385 sodium:proton antiporter activity | 1 (sole) | 19 (GO_Central; plus 263 TreeGrafter) | GO:0015385, IMP, PMID:16030218 | INDIRECT-PHENOTYPE | The abstract describes no PA1059 mutant. The evidence is a PA1054 disruption plus whole-cluster complementation of E. coli TO114. Right as `contributes_to` (MrpG Pro81 is needed for Mrp antiport), not as `enables` + IMP. The LUCA-root node also covers MBH/MBX hydrogenase subunit C proteins (TK2082, TK1224), for which a stand-alone antiporter MF is doubtful. |

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
