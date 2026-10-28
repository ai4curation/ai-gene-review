# PA1055 (Q9I4R9, ShaC) notes

## 2026-10-28 review (PseudoCAP IBA-seed worklist, rank 21)

No deep-research provider was available; literature collected by PubMed search
and cached abstracts or full texts. The PseudoCAP-cited paper (PMID:16030218,
Kosono et al. 2005) is abstract-only here: its PMC copy (PMC1196046) is a
scanned PDF with no text, and the PDF could not be retrieved.

### Identity

- UniProt Q9I4R9 (unreviewed), 112 aa, two predicted TM helices (Phobius
  32-57, 69-90). InterPro IPR050601 CPA3_antiporter_subunitC and IPR039428
  NUOK/Mnh_C1-like; Pfam PF00420 (Oxidored_q2, the NuoK/ND4L family);
  PANTHER PTHR34583:SF2 [file:PSEAE/PA1055/PA1055-uniprot.txt].
- Second gene of the six-gene sha cluster PA1054-PA1059. The authors name the
  cluster shaABCDEFG for six genes, as in other Gram-negative Mrp operons,
  where mrpA and mrpB are fused [PMID:29218041 "This group belongs to bacteria
  such as Pseudomonas aeruginosa and Vibrio cholerae, in which it appears that
  the mrpA gene is fused with the mrpB gene encoding a fusion protein"]. So
  PA1054 = ShaAB and, by gene order and family, PA1055 = ShaC (MrpC). The
  abstract names only PA1054 (shaA) explicitly; the PA1055 = ShaC mapping is
  an inference.

### What PMID:16030218 shows

- The whole cluster PA1054-PA1059, but not the cluster with PA1054 deleted,
  complemented Na+ sensitivity and the antiport defect of E. coli TO114
  [PMID:16030218 "The gene cluster PA1054 to PA1059, but not the cluster with
  a deletion of PA1054, complemented a growth defect in the presence of 0.2 M
  NaCl and a defect in Na+/H+ antiport activity of the Escherichia coli TO114
  mutant lacking the three major Na+/H+ antiporters"].
- Only PA1054 was disrupted in P. aeruginosa [PMID:16030218 "We disrupted
  PA1054 (a shaA homologue gene) and determined its effect on Na+ tolerance
  during growth, Na+ efflux, and pathogenicity in mice."].
- So the paper has no PA1055 mutant. The IMP rows on PA1055 rest on a PA1054
  mutant plus whole-cluster complementation. The cluster data do show that
  the six gene products together make a Na+/H+ antiporter that is largely
  responsible for Na+ extrusion.

### Mrp/Sha complex biology (family)

- Activity needs the hetero-oligomeric complex of all subunits
  [PMID:20624916 "Antiport activity requires hetero-oligomeric complexes of
  all six or seven hydrophobic Mrp proteins (MrpA-MrpG)."], [PMID:29218041
  "Generally, all Mrp subunits, mrpA-G, are required for enzymatic activity."].
- MrpC is the NuoK/ND4L homologue [PMID:29218041 "the small subunit MrpC has
  homology with NuoK"]. In the 2.2 A B. pseudofirmus structure, MrpC sits at a
  hydrated region proposed to carry Na+ [PMID:36241630 "the pronounced
  hydration in the vicinity of MrpC suggests a role in sodium transfer"]. The
  MrpC-Q70A mutant keeps antiport activity but loses the monomeric complex
  [PMID:20624916 "Two mutants, MrpB-P37G and MrpC-Q70A, showed a normal
  phenotype but lacked the MrpA-MrpG monomeric complex while retaining the
  dimeric hetero-oligomeric complex."].
- Archaeal membrane-bound hydrogenase (MBH) contains an Mrp-like
  Na+-translocating module [PMID:29754813 "The Na+-translocating unit, absent
  in complex I, resembles that found in the Mrp H+/Na+ antiporter"].

### Annotation decisions (summary)

- GO:0015385 sodium:proton antiporter activity (IBA, IMP): ACCEPT as the core
  activity, but as a subunit contribution: `contributes_to`, not `enables`.
  Defects filed for the qualifier (PSEUDOCAP, GO_CENTRAL) and the IMP code.
- GO:0035725 sodium ion transmembrane transport (IBA, IMP): ACCEPT; IMP code
  flagged.
- GO:0005886 plasma membrane (IEA): ACCEPT.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN002160376 | GO:0015385 sodium:proton antiporter activity | 1 (sole) | 24 | GO:0015385, IMP, PMID:16030218 | INDIRECT-PHENOTYPE | No PA1055 mutant was made. The row rests on a PA1054 (shaA) disruption and on complementation of E. coli TO114 by the whole PA1054-PA1059 cluster. That shows the Sha complex is a Na+/H+ antiporter, not that PA1055 enables antiport alone. Biologically right as `contributes_to` (a subunit of the antiporter complex), wrong as `enables` + IMP. The node is the LUCA root of the subunit-C family and includes MBH/MBX hydrogenase subunits (TK2086, TK1221), for which a stand-alone antiporter MF is doubtful. |
| PTN002160376 | GO:0035725 sodium ion transmembrane transport | 1 (sole) | 24 | GO:0035725, IMP, PMID:16030218 | SOUND | As a subunit of the complex responsible for Na+ extrusion, PA1055 takes part in Na+ transmembrane transport. Structural work places MrpC at the putative Na+ pathway. The process fits the whole clade, MBH Na+-translocating modules included. Caveat: the IMP code is not right for PA1055, since no PA1055 mutant exists; filed as a CHECK. |
