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
- Regulation of cilium beat frequency IMPs kept as non-core (phenotype, not a
  regulatory activity).
- Sperm motility IMP (PMID:18492703) marked over-annotated.
- protein localization to motile cilium (CFAP45) kept as non-core.

## PANTHER / IBA check
Human DNAH11 (Q96DT5) and mouse Dnah11 (E9Q7N9) have identical IBA sets (7 terms);
no human-versus-mouse family split. UniProt PANTHER: PTHR45703:SF12.
