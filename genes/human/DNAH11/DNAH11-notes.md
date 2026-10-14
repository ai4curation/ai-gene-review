# DNAH11 curation notes

## Deep research
Falcon deep research failed twice ("Failed to authenticate"); no deep-research
file. Review based on cached publications, UniProt, and the Europe PMC full text
of PMID:33139725 (PMC7606486), which was read but is cached abstract-only.

## Biology summary (with provenance)
- Proximal ODA beta heavy chain [PMID:26909801 "IFM analysis demonstrated native
  DNAH11 localization in only the proximal region of wild-type human respiratory
  cilia"]; partial proximal ODA loss by tomography [PMID:26909801].
- Hyperkinetic stiff beat, normal ultrastructure [PMID:18022865, PMID:22184204].
- Mouse orthologue lrd: mutated in iv/lgl [PMID:9353118]; in motile node monocilia
  needed for nodal flow [PMID:12859898].
- Situs inversus totalis with DNAH11 nonsense mutation [PMID:12142464].
- Not in sperm axoneme [PMID:31178125]; biallelic nonsense compatible with male
  fertility [PMID:18022865].
- CFAP45 co-IPs DNAH11; CFAP45 mislocalized in DNAH11-mutant cilia (full text of
  PMID:33139725).

## Annotation decisions
- NEW: outer dynein arm (part_of), since DNAH11 has only the generic dynein
  complex; comparator check: DNAH5, DNAH9 and DNAH17 carry the term.
- Regulation of cilium beat frequency IMPs modified to epithelial cilium movement
  involved in extracellular fluid movement (GO:0003351): the hyperkinetic beat is a
  loss-of-function phenotype of the motor, not a regulatory activity, and DNAH11
  has no cilium movement row in GOA.
- Sperm motility IMP (PMID:18492703) marked over-annotated.
- protein localization to motile cilium (CFAP45, IMP) marked over-annotated: CFAP45
  depends on DNAH11 for its axonemal position [PMC7606486 full text "In contrast,
  CFAP45 ciliary localization was abnormal or undetectable in respiratory cilia from
  several genetically distinct DNAH11-mutant subtypes"], which does not make DNAH11
  a participant in protein localization. The cached record is abstract-only, so
  the full-text sentence is recorded as supporting_text_fulltext.
- Light intermediate chain binding (IEA/IBA) removed: the outer dynein arm has no
  light intermediate chain subunit, so the claim is unlikely to be correct.
- microtubule-based process and microtubule-based movement (IEA) set to
  TOO_GENERAL.

## PANTHER / IBA check
Human DNAH11 (Q96DT5) and mouse Dnah11 (E9Q7N9) have identical IBA sets (7 terms);
no human-versus-mouse family split. UniProt PANTHER: PTHR45703:SF12.
