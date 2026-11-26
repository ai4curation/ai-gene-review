# erg13B review notes

Falcon deep research was unavailable because `agentapi` was unavailable. The
review therefore used the seeded GOA rows, UniProtKB Q4WXT8, the local
PTHR43323 family review, `PTHR43323-paint.tsv`, `PTHR43323-entries.csv`, and the
two publications already cached from the UniProt record.

## Evidence summary

- Q4WXT8 is the Aspergillus fumigatus Af293 erg13B protein and sits in
  `PANTHER:PTHR43323:SF2`, the fungal/ERG13 HMG-CoA synthase subfamily.
  The same Af293 genome also has erg13A/Q4WBQ3 in `PANTHER:PTHR43323:SF2`, so
  the A. fumigatus mevalonate-pathway HMG-CoA synthase step is duplicated.
- The PAINT node `PANTHER:PTN000222418` asserts the inherited
  `GO:0004421` HMG-CoA synthase activity and broader `GO:0006084` acetyl-CoA
  metabolic process. The local PTHR43323 family review judges both nodes sound.
- The PAINT node `PANTHER:PTN000933803` asserts `GO:0006696` ergosterol
  biosynthetic process at the fungal sterol node seeded by Saccharomyces ERG13,
  and the local PTHR43323 family review judges that node sound.
- UniProt records the Q4WXT8 reaction as acetoacetyl-CoA plus acetyl-CoA plus
  water producing HMG-CoA plus CoA and a proton, EC 2.3.3.10, by similarity to
  UniProtKB:P41338.
- Q4WXT8 is still `PE 3: Inferred from homology`. The UniProt record preserves
  the HMG-CoA synthase PROSITE and NCBIfam signatures, the expected predicted
  catalytic Glu/Cys/His residues, and HMG-CoA binding residues, but the cached
  literature does not distinguish erg13B activity or expression from erg13A.
- Ferreira et al. 2005 is abstract-only in the cache and supports only the
  high-level statement that A. fumigatus has a duplicated ergosterol pathway.
- Yasmin et al. 2012 does not directly assay erg13B, but it experimentally ties
  mevalonate supply to A. fumigatus ergosterol and siderophore metabolism and
  supports the broader isoprenoid/sterol process context.

## Annotation decisions

- Accepted all three `GO:0004421` rows. The IBA, combined IEA, and ISS rows all
  converge on the same HMG-CoA synthase activity, and Q4WXT8 retains the
  predicted active-site and ligand-binding residues expected for a working
  HMG-CoA synthase.
- Accepted the `GO:0006696` IBA. PTN000933803 is a fungal ergosterol PAINT node,
  and Q4WXT8 belongs to the retained fungal HMG-CoA synthase subfamily.
- Kept the two `GO:0006084` acetyl-CoA metabolic process rows as non-core. The
  claim is true because the reaction consumes acetyl-CoA, but it is less
  informative than the exact HMG-CoA synthase activity.
- Kept `GO:0008299` isoprenoid biosynthetic process as non-core. Mevalonate is a
  precursor for ergosterol, TAFC siderophore, and other isoprenoid products in
  A. fumigatus.
- Marked `GO:0016746` acyltransferase activity as `TOO_GENERAL` because
  `GO:0004421` is the exact retained acyltransferase activity.

## Remaining biology gap

- A. fumigatus has two same-subfamily HMG-CoA synthase paralogs, erg13A and
  erg13B, but the available cached evidence does not establish which paralog
  carries mevalonate flux in vivo, whether erg13B is redundant with erg13A, or
  whether erg13B contributes under iron starvation when mevalonate is split
  between sterol and TAFC siderophore production.
