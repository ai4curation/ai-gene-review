# KNG1 review notes

Automated deep research was attempted with Falcon and the `perplexity-lite` fallback, but neither
provider was available in this runtime, so this review used the seeded GOA rows, cached PubMed and
Reactome records, the kallikrein-kinin module, and the local ACE and BDKRB1 reviews.

## Core biology

- KNG1 produces secreted high- and low-molecular-weight kininogens. The shared N-terminal
  cystatin-like region accounts for cysteine proteinase inhibitor activity; low-molecular-weight
  kininogen was isolated among the human urinary cysteine proteinase inhibitors and was tested
  against papain and human cathepsin B [PMID:3488317].
- Bradykinin, released from high-molecular-weight kininogen by plasma kallikrein, is the kinin
  modeled in GO-CAM `6246724f00000632`. The peptide is an agonist for human BDKRB2 in cloned
  receptor assays [PMID:1314587; PMID:1329734].
- High-molecular-weight kininogen has a scaffold role in contact activation: it binds
  prekallikrein and surfaces or endothelial receptor complexes so that factor XII,
  prolylcarboxypeptidase and plasma kallikrein can generate bradykinin. A comparator check
  against `F8` nonenzymatic intrinsic-tenase cofactor annotations and `F12` contact-protease
  annotations supports a conservative new `GO:0007597` intrinsic coagulation assertion for this
  scaffold role, while keeping it distinct from any claim that KNG1 itself is the plasma or
  tissue kallikrein-kinin protease.
- Cleaved two-chain high-molecular-weight kininogen and domain 5 block vitronectin-dependent
  adhesion and platelet aggregation [PMID:11970955]. This is a real post-cleavage effect but a
  separate non-core branch from the kinin hormone precursor function.

## GO-CAM notes

- The GO-CAM's KNG1 annoton uses `GO:0005179` hormone activity in `GO:0042311` vasodilation, which
  matches the accepted KNG1 review after interpreting the active hormone as the released
  bradykinin peptide.
- Final GO-CAM consistency PR: change the KNG1 activity consistency from no gene review to
  consistent after this review merges.
