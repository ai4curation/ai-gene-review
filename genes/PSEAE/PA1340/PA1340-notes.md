# PA1340 (Q9I404) notes

## Review session 2026-10-28 (PseudoCAP IBA-seed protocol)

Fetched with `just fetch-gene PSEAE PA1340` (no gene symbol; locus tag used as
folder name). Accession Q9I404 matches the worklist (rank 100). Unreviewed
TrEMBL entry (PE 3). No deep-research provider was used. Reviewed alongside
PA1341 (same operon).

### Identity

- HisMQ-subfamily ABC permease; PANTHER PTHR30614:SF1 "GLUTAMATE_ASPARTATE
  IMPORT PERMEASE PROTEIN GLTK"; four predicted TM helices; TCDB 3.A.1.3.22.
- Operon PA1342-PA1339, orthologous to P. putida AatJQMP (PP1071-PP1068) and
  E. coli GltIJKL. PA1340 is the GltK-type permease (AatM by operon order).

### Literature

- Johnson et al. 2008 (PMID:18833300; full text cached), Biolog/plate screen of
  transposon mutants (PAK background):
  - [PMID:18833300 "All three mutants were defective for utilization of
    L-glutamic acid as a carbon source, and expression of two of these genes was
    induced by L-glutamic acid"] (PA1340 induced 9.4-fold by L-Glu, Table 3).
  - [PMID:18833300 "Additionally, one of these mutants (PA1340) also showed
    significantly decreased utilization of the related compounds, L-glutamine,
    D-glutamic acid, and N-acetyl-L-glutamic acid."] Table 2: L-Glu C+/-, L-Gln
    C+/-, L-Glu N+/-, D-Glu N-, N-acetyl-L-Glu N+/-.
- Singh and Rohm 2008 (PMID:18310026; abstract only) is a P. putida KT2440
  study: [PMID:18310026 "The system (AatJMQP, for acidic amino acid transport)
  is encoded by an operon involving genes PP1071-PP1068."] Mutants were of
  the binding protein (aatJ) and ATPase (aatP): [PMID:18310026 "A deletion mutant
  with inactivated solute-binding protein (KTaatJ) failed to grow on Glu and Gln
  as sole sources of carbon and nitrogen"]. Binding: [PMID:18310026 "The purified
  solute-binding protein AatJ exhibited high affinity towards Glu and Asp
  (K(d)=0.4 and 1.3 muM, respectively), while Gln and Asn as well as
  dicarboxylates (succinate and fumarate) were bound with much lower affinity."]
  The abstract also names a periplasmic glutaminase/asparaginase AnsB in the
  same AauR regulon, so Gln growth phenotypes may partly reflect deamidation.
- He et al. 2014 (PMID:25082951; abstract only), PAO1 D-Glu catabolism:
  [PMID:25082951 "expression of the previously characterized AatJMQP
  transporter for acidic l-amino acid uptake was found inducible by D-Glu and
  essential for D-Glu utilization"]. Which aat gene was mutated is not stated in
  the abstract.

Key finding: the PseudoCAP IMP GO:0006868 L-glutamine transport to
PMID:18310026 attaches a P. putida mutant phenotype (of the binding protein,
not the permease) to P. aeruginosa PA1340. The abstract states the organism and
the genes explicitly, so this is a reference/evidence-code error. PA1340's own
glutamine evidence is the partial Biolog phenotype in PMID:18833300.

### Clade checks (cached PAINT IBD/leaf GAF; QuickGO 2026-10-28)

- PTN000764525 (GO:0006868 L-glutamine transport; sole seed PA1340): 6 leaves
  in 5 taxa: E. coli GltK (P0AER5), Salmonella GltK, Yersinia GltK,
  Bradyrhizobium bll7598, blr3098, PA1340. The only other experimental
  annotation is plasma membrane (IDA) for E. coli GltK. GltIJKL is the E. coli
  glutamate/aspartate importer; glutamine is carried by GlnHPQ. The sister GltJ
  node PTN004745596 carries L-glutamate import (sole seed PA1341). Glutamine
  is the wrong node term for this clade.
- PTN000770157 (GO:0006865 amino acid transport; 5 seeds): see PA1341 notes;
  appropriate general term.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN000770157 | GO:0006865 amino acid transport | 5 | 84 (28 taxa) | GO:0006868 IMP PMID:18310026; GO:0042940 IMP PMID:25082951; GO:0051938 IMP PMID:18833300; GO:1903803 IMP PMID:18833300 (PseudoCAP) | SOUND | General term for a HisMQ-subfamily permease clade; it is supported by the sound PA1340 L-Glu rows and by E. coli seeds, whatever the status of the glutamine row. |
| PTN000764525 | GO:0006868 L-glutamine transport | 1 (sole) | 6 (5 taxa) | GO:0006868, IMP, PMID:18310026 (PseudoCAP) | WRONG | The cited paper studies P. putida aatJ/aatP mutants, not PA1340 or any GltK-type permease, so the IMP does not apply. PA1340's own Gln phenotype (PMID:18833300) is partial, and Gln is at most a low-affinity secondary substrate. The node is a GltK clade of glutamate/aspartate importers; L-glutamate import (as on the sister GltJ node) would fit. |

Defects filed: PSEUDOCAP WRONG_EVIDENCE_CODE (CHECK) on the GO:0006868 IMP
row (P. putida paper); GO_CENTRAL WRONG_TERM (CHECK, suggested GO:0051938) for
the PTN000764525 IBD on the IBA row. On the PA1340 leaf itself, glutamine
import is kept as non-core.

## Decisions summary

- ACCEPT: plasma membrane (IBA, IEA).
- KEEP_AS_NON_CORE: D-amino acid transport (IMP), L-glutamine import across
  plasma membrane (IMP).
- MODIFY: L-glutamine transport (IBA, IMP) -> L-glutamine import across plasma
  membrane; L-glutamate import (IMP) and transmembrane transport (IEA) ->
  L-glutamate import across plasma membrane; amino acid transmembrane
  transporter activity (IBA) and transmembrane transporter activity (IEA) ->
  ATPase-coupled L-glutamate transmembrane transporter activity; membrane ->
  plasma membrane; ABC transporter complex -> substrate-binding
  subunit-containing ABC transporter complex.
