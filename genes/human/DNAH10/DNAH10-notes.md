# DNAH10 curation notes

Deep research: falcon failed (Edison API "Failed to authenticate"; retried once); no
deep-research file.

## Identity
- Q8IVF4, 4471 aa; stem 1-1793, AAA1-AAA6 motor and stalk (UniProt). I1-alpha-type heavy chain of
  the two-headed I1/f inner arm with DNAH2 [PMID:30060180; PMID:40898283]; it localizes
  independently of DNALI1 [PMID:36792588 "Being a component of subspecies I1α, DNAH10 was not
  affected by the loss of DNALI1"].

## Phenotypes
- MMAF / SPGF56 [PMID:34237282 "Morphological and ultrastructural analyses of the spermatozoa
  obtained from men harboring bi-allelic DNAH10 variants revealed striking flagellar defects with
  the absence of inner dynein arms (IDAs)."; PMID:34657236; PMID:39996363; PMID:40592014].
- PCD [PMID:37314648 "Immunostaining analysis showed the absence of DNAH10 and DNALI1 in the
  respiratory cilia"; PMID:40898283 "In summary, disruption of DNAH10 would render the IDAf complex
  instability, altering the beating frequency and direction of motile cilia."].
- Zebrafish ependymal monocilia and body axis [PMID:34915022].
- Less established: manchette/UCHL3-PACRG [PMID:41058558]; primary cilia and skeletal development
  [PMID:42086325]. Not annotated.

## Curation decisions
- Only electronic and IBA annotations plus one HPA IDA existed. Added NEW part_of inner dynein arm
  (IDA, PMID:40898283) and involved_in flagellated sperm motility (IMP, PMID:34237282). Comparator
  check: paralogs DNAH1 and DNAH2 carry both terms; DNAH10 is a structural/motor heavy chain of the
  arm, not a substrate.
- Light intermediate chain binding (IBA/IEA) marked over-annotated, as for DNAH2.

## PANTHER / IBA check
- Human DNAH10 and mouse Dnah10 (F7ABZ6, unreviewed) carry the same six IBA terms in QuickGO; no
  family split.
- PANTHER geneinfo places the protein in family PTHR10676 (the source of the IBAs), whereas the
  UniProt/InterPro cross-reference places it in PTHR22878 (each in a subfamily correctly named
  for this gene). This is the same two-route disagreement noted for DNAH12, but here it does not
  cost the gene any IBAs.
