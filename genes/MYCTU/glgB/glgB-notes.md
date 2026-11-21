# glgB (Rv1326c, P9WN45) — curation notes

## Identity and reaction
GlgB is the 1,4-alpha-glucan branching enzyme of *Mycobacterium tuberculosis*
H37Rv, EC 2.4.1.18, GH13 family (GlgB subfamily), PANTHER PTHR43651:SF3
[file:MYCTU/glgB/glgB-uniprot.txt "Belongs to the glycosyl hydrolase 13 family. GlgB"].
It forms alpha-1,6 branch points by cleaving an alpha-1,4 linkage in a growing
alpha-1,4-glucan chain and transferring the excised oligosaccharide to a new
alpha-1,6 position [file:MYCTU/glgB/glgB-uniprot.txt "Essential enzyme that
catalyzes the formation of the"]. It is a monomer (PMID:17005418) with a
four-domain architecture solved by X-ray crystallography (PDB 3K1D;
PMID:20444687 "catalyzes the branching of a linear glucose chain during
glycogenesis by cleaving a 1-->4 bond and making a new 1-->6 bond").

## Pathway context and essentiality
GlgB is the fourth, branching step of the TreS-Pep2-GlgE-GlgB route, acting on
the linear alpha-1,4-glucan built by GlgE. It is required for biosynthesis of
both intracellular glycogen and the surface-exposed capsular alpha-glucan
[PMID:18808383 "the synthesis of glucan and glycogen involves the
alpha-1,4-glucosyltransferases Rv3032 and GlgA (Rv1212c), the ADP-glucose
pyrophosphorylase GlgC (Rv1213) and the branching enzyme GlgB (Rv1326c)."], and
is essential in vitro [PMID:18808383 "Unexpectedly, GlgB was found to be an
essential enzyme."].

## WhiB1 redox interaction
GlgB is a specific substrate of the thioredoxin-like redox regulator WhiB1,
which reduces a GlgB intramolecular disulfide [PMID:19121228 "branching enzyme
(GlgB) of M. tuberculosis as a interaction partner of WhiB1"]. The disulfide
state does not alter branching activity, but may couple GlgB to the redox state
of the cell. GOA annotates this only as bare protein binding (GO:0005515, IPI),
which is removed under the protein-binding policy; the interaction itself is
real and is recorded as a MEDIUM-relevance reference and a suggested question.

## Annotation decisions
- **GO:0003844** branching enzyme activity (IBA, 2× IDA, IEA) ACCEPT (core).
- **GO:0003824** catalytic activity (IEA) MODIFY → GO:0003844.
- **GO:0004553** hydrolase, hydrolyzing O-glycosyl (IEA, GH13 N-domain)
  MARK_AS_OVER_ANNOTATED: GlgB is a branching transglycosylase; the 1,4
  cleavage is the first half of an intramolecular transfer, not net hydrolysis.
- **GO:0043169** cation binding (IEA) MARK_AS_OVER_ANNOTATED: GlgB activity is
  *inhibited* by Zn2+/Cu2+ and unaffected by Mg2+/Mn2+/Ca2+; no functional
  cation site.
- **GO:0005515** protein binding (IPI WhiB1) REMOVE (protein-binding policy).
- **GO:0005737** cytoplasm (IBA) MODIFY → GO:0005829 cytosol (also carried by a
  separate IBA node); **GO:0005829** cytosol ACCEPT (core location).
- **GO:0005978** glycogen biosynthetic (IBA, IEA, IMP) ACCEPT (core).
- **GO:0009250** glucan biosynthetic (IMP) MODIFY → GO:0030979 alpha-glucan
  biosynthetic (the M.tb polymer is alpha-glucan).
- **GO:0005975** carbohydrate metabolic / **GO:0044042** glucan metabolic (IEA)
  MODIFY → GO:0030979 + GO:0005978 (supported descendants).
- **GO:0045227** capsule polysaccharide biosynthetic (IEA) KEEP_AS_NON_CORE: a
  genuine but specific downstream destination of the branched alpha-glucan.
