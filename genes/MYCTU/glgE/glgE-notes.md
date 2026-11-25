# glgE (Rv1327c, P9WQ17) — curation notes

## Identity and reaction
GlgE is the alpha-1,4-glucan:maltose-1-phosphate maltosyltransferase of
*Mycobacterium tuberculosis* H37Rv, EC 2.4.99.16, GH13 family (GlgE subfamily),
PANTHER PTHR47786 [file:MYCTU/glgE/glgE-uniprot.txt "Belongs to the glycosyl
hydrolase 13 family. GlgE"]. It uses alpha-maltose 1-phosphate (M1P) as the
activated donor to elongate alpha-1,4-glucan chains by maltosyl (two-glucose)
units, releasing phosphate (RHEA:42692) [file:MYCTU/glgE/glgE-uniprot.txt
"Essential maltosyltransferase that uses maltose 1-phosphate"]. The enzyme is an
alpha-retaining homodimer (PMID:21914799) that prefers acceptors of DP ≥ 4
(DP5 optimal); it can also run the reaction in reverse (phosphorolysis) and
disproportionate maltooligosaccharides in vitro.

## Pathway context
Fourth-named but third-acting enzyme of the TreS-Pep2(Mak)-GlgE-GlgB route from
trehalose to branched alpha-glucan [PMID:20305657 "We describe a new pathway
from trehalose to alpha-glucan in Mycobacterium tuberculosis comprising four
enzymatic steps mediated by TreS, Pep2, GlgE (which has been identified as a
maltosyltransferase that uses maltose 1-phosphate) and GlgB."]. GlgE consumes
the M1P made by Mak and hands its linear alpha-1,4-glucan to GlgB for branching.
Under laboratory growth the TreS-Pep2 branch supplies most of the M1P for this
pathway [PMID:27513637 "the TreS-Pep2 branch provides most of the M1P for the
GlgE pathway in M. tuberculosis"].

## Essentiality / drug target
GlgE is essential: its inactivation causes rapid death through self-poisoning
accumulation of M1P [PMID:20305657 "GlgE inactivation causes rapid death of M.
tuberculosis in vitro and in mice through a self-poisoning accumulation of
maltose 1-phosphate."], a synthetic-lethal validated drug target.

## Annotation decisions
- **MF**: GO:0016758 hexosyltransferase activity is the best existing GO term
  for the maltosyltransferase activity and is kept core (IDA/IBA/IEA all
  ACCEPT). GO lacks a substrate-specific maltosyltransferase term, so one is
  proposed under GO:0016757 glycosyltransferase activity (maltosyl = a
  disaccharidyl, not a single hexosyl, so the proposed parent is GO:0016757, not
  GO:0016758). This mirrors the mak review, which keeps GO:0019200 and proposes
  a maltokinase term. The module's GlgE leaf uses GO:0016758 and records the
  same ontology gap.
- **GO:0016757** (glycosyltransferase, IEA) MODIFY → GO:0016758, the more
  specific transferase term the gene already carries by IDA.
- **GO:0004553** hydrolase activity, hydrolyzing O-glycosyl compounds (IEA from
  the GH13 N/S signature) MARK_AS_OVER_ANNOTATED: GlgE is a transferase, and its
  reverse reaction is phosphorolytic, not hydrolytic.
- **GO:0005993** trehalose catabolic process (IMP) MODIFY → GO:0030979
  alpha-glucan biosynthetic process: the phenotype is real but GlgE acts on M1P,
  not trehalose; TreS performs the trehalose-cleaving step. The reframe assigns
  GlgE the process it actually catalyses.
- **GO:0005975** carbohydrate metabolic (IEA) MODIFY → GO:0030979 +
  GO:0005978 (supported descendants).
- **GO:0005978 / GO:0030979** biosynthetic process rows ACCEPT (core).
- **GO:0005886** plasma membrane (HDA membrane-fraction proteome,
  abstract-only) KEEP_AS_NON_CORE: soluble homodimer, no TM; peripheral/carryover.
