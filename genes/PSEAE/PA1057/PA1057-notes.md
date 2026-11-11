# PA1057 (Q9I4R7, ShaE) notes

## 2026-10-28 review (PseudoCAP IBA-seed worklist, rank 26)

No deep-research provider was available; literature collected by PubMed search
and cached abstracts or full texts. The PseudoCAP-cited paper (PMID:16030218,
Kosono et al. 2005) is abstract-only here: its PMC copy (PMC1196046) is a
scanned PDF with no text. The same paper also seeds the subunit C IBD
(see `genes/PSEAE/PA1055/PA1055-notes.md`).

### Identity

- UniProt Q9I4R7 (unreviewed), 174 aa, three predicted TM helices (Phobius
  12-30, 36-57, 69-88). InterPro IPR002758 Cation_antiport_E; Pfam PF01899
  (MNHE); PANTHER PTHR34584:SF1 [file:PSEAE/PA1057/PA1057-uniprot.txt].
- Fourth gene of the six-gene sha cluster PA1054-PA1059 (shaABCDEFG with
  shaA and shaB fused in Gram-negative Mrp operons [PMID:29218041 "in which
  it appears that the mrpA gene is fused with the mrpB gene encoding a fusion
  protein"]). By gene order and family, PA1057 = ShaE (MrpE); the abstract
  names only PA1054 explicitly, so the mapping is an inference.

### What PMID:16030218 shows

- Whole-cluster complementation of E. coli TO114, lost when PA1054 is deleted
  [PMID:16030218 "The gene cluster PA1054 to PA1059, but not the cluster with
  a deletion of PA1054, complemented a growth defect in the presence of 0.2 M
  NaCl and a defect in Na+/H+ antiport activity of the Escherichia coli TO114
  mutant lacking the three major Na+/H+ antiporters"].
- The abstract reports disruption of PA1054 only [PMID:16030218 "We disrupted PA1054 (a shaA
  homologue gene) and determined its effect on Na+ tolerance during growth,
  Na+ efflux, and pathogenicity in mice."]. The abstract describes no PA1057 mutant (full text not read).

### MrpE in the family

- Needed for normal membrane levels of other subunits and for complex
  formation in B. pseudofirmus [PMID:20624916 "The results extended
  indications that MrpE is required for normal membrane levels of other Mrp
  proteins and for complex formation."]. MrpE-T113Y abolishes antiport and
  complex [PMID:29218041 "In category 1, MrpD-D75A, MrpD-R258A, MrpE-T113Y,
  and MrpF-D32A were studied, and their Na+/H+ antiport activity was found to
  be completely lost, with no Mrp complex detected."].
- But in B. subtilis MrpE was reported dispensable for ion transport
  [PMID:29218041 "However, in B. subtilis, it was reported that MrpE is
  dispensable for ion transport activity"].
- Structure: two short TMHs plus a cytoplasmic domain; one model has Na+
  entering via MrpE [PMID:36241630 "Steiner and Sazanov propose that
  trans-membrane proton transfer is carried out by the MrpA and MrpD subunits
  while sodium is taken up from the cytoplasm by MrpE and released to the
  periplasm at the interface of MrpA, MrpC, and MrpD"].

### Annotation decisions (summary)

- GO:0015385 sodium:proton antiporter activity (IBA, IMP): ACCEPT as the core
  activity, but `contributes_to`; defects for qualifier and IMP code.
- GO:0035725 sodium ion transmembrane transport (IBA, IMP): ACCEPT; IMP code
  flagged.
- GO:0008324 (IEA): MODIFY to GO:0015385; GO:0006812 (IEA): MODIFY to
  GO:0035725; GO:0016020 (IEA): MODIFY to GO:0005886; GO:0005886: ACCEPT.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN002160407 | GO:0015385 sodium:proton antiporter activity | 1 (sole) | 20 | GO:0015385, IMP, PMID:16030218 | INDIRECT-PHENOTYPE | The abstract describes no PA1057 mutant. The evidence is a PA1054 disruption plus whole-cluster complementation of E. coli TO114, which shows the Sha complex is an antiporter. MrpE is an accessory subunit needed for complex assembly in B. pseudofirmus but reported dispensable for transport in B. subtilis. Right as `contributes_to`, not as `enables` + IMP. The LUCA-root node also covers MBH/MBX hydrogenase subunit A proteins (TK2080, TK1226). |
| PTN002160407 | GO:0035725 sodium ion transmembrane transport | 1 (sole) | 20 | GO:0035725, IMP, PMID:16030218 | SOUND | As a subunit of the Na+-extruding complex, PA1057 takes part in Na+ transmembrane transport, and MrpE is proposed as the Na+ entry route. The process fits the clade, MBH Na+ modules included. Caveat: IMP looks like the wrong code for PA1057 (no mutant in the abstract); filed as a CHECK. |

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
