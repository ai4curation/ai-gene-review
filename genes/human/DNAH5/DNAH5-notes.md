# DNAH5 curation notes

## Deep research
Falcon deep research (`just deep-research-falcon human DNAH5`) failed twice with
"Failed to authenticate" from the provider API, so no deep-research file exists.
The review is based on the cached publications and UniProt record.

## Biology summary (with provenance)
- Gamma heavy chain of the outer dynein arm (ODA); orthologue of Chlamydomonas
  gamma-dynein [PMID:11788826 "which encodes a protein highly similar to the
  Chlamydomonas gamma-dynein heavy chain"].
- Present along the whole respiratory axoneme in two ODA types [PMID:18950741
  "Respiratory cilia contain at least two distinct ODA types: type 1, DNAH9
  negative and DNAH5 positive (proximal ciliary axoneme); and type 2, DNAH9 and
  DNAH5 positive (distal ciliary axoneme)."].
- Required for ODA assembly [PMID:18950741 "DNAH5 is also essential for the
  axonemal assembly of the ODA protein DNAI2 within ODA types 1 and 2."].
- Loss causes immotile cilia [PMID:15750039 "Cilia with complete axonemal DNAH5
  deficiency were immotile"].
- Not in human sperm axoneme [PMID:31178125 "DNAH17 and DNAH8, but not DNAH5,
  DNAH9, or DNAH11, colocalize with α-tubulin along the sperm axoneme"]; a DNAH5
  patient had normal sperm ODA heavy chains [PMID:15750039].
- Cytoplasmic preassembly with ZMYND10/FKBP8 chaperone relay [PMID:29916806].
- Mouse Dnah5 mutant: PCD, situs inversus, hydrocephalus [PMID:11912187];
  ependymal flow [PMID:15269178].

## Annotation decisions
- Sperm motility IMPs (PMID:15750039, PMID:18492703) marked over-annotated: the
  first abstract contradicts a sperm role, the second rests on heterozygous
  variants.
- Cilium assembly IMP (PMID:16492982) modified to outer dynein arm assembly.
- Light intermediate chain binding (IEA/IBA) removed: the outer dynein arm has no
  light intermediate chain subunit (UniProt SUBUNIT: heavy, light and intermediate
  chains), and LIC binding is grounded only in cytoplasmic dynein 1 heavy chains
  (PTN000743491 donors DYNC1H1/Dync1h1). The claim is unlikely to be correct, not
  just under-supported, so REMOVE rather than MARK_AS_OVER_ANNOTATED.
- microtubule motor activity (IEA), axonemal dynein complex (IEA) and
  microtubule-based movement (IEA) set to TOO_GENERAL: each is entailed by a more
  specific term the review keeps (minus-end-directed microtubule motor activity,
  outer dynein arm, cilium movement).
- cilium movement involved in cell motility (IBA) modified to epithelial cilium
  movement involved in extracellular fluid movement.

## PANTHER / IBA check
QuickGO IBA sets are identical for human DNAH5 (Q8TE73) and mouse Dnah5 (Q8VHE6):
7 IBA terms each, including outer dynein arm and outer dynein arm assembly from
node PTN002472868. No family-split gap of the DNAH12 kind. Note that the UniProt
PANTHER cross-reference puts DNAH5 in PTHR46532:SF13, a subfamily named after
cytoplasmic dynein 1 heavy chain 1.
