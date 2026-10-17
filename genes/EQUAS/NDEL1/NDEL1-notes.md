# NDEL1 (donkey, A0A9L0IJ72) notes

DONKEY40 cohort review. Evidence: donkey UniProt TrEMBL record (PE 3), donkey GOA (28 IEA rows: TreeGrafter,
Ensembl orthology projection GO_REF:0000107, combined GO_REF:0000120, SubCell GO_REF:0000044), the human
Swiss-Prot record and existing review in `genes/human/NDEL1/`, the PTHR10921 family review
(`interpro/panther/PTHR10921/PTHR10921-review.yaml`), and a donkey-human comparison
(`NDEL1-bioinformatics/RESULTS.md`, run against `genes/human/NDEL1/NDEL1-uniprot.txt`). No deep-research
provider call was made.

## Sequence

- Donkey 481 aa vs human 345 aa: 97.1% identity over all 345 human residues
  [file:EQUAS/NDEL1/NDEL1-bioinformatics/RESULTS.md "with 97.1% identity across 345 paired residues"].
- Donkey residues 339-474 have no human counterpart [RESULTS.md "donkey residues 339-474."]; human
  canonical sequence runs to ...SSAP(338) then GMLPLSV, and none of the three human isoforms has the donkey
  extension (human VAR_SEQ at 316..345 gives isoforms 2 and 3 with different C-termini). Whether this is a
  real exon or a gene-model artefact is unknown. All characterized human regions (LIS1-binding coiled coil,
  dynein IC / CENP-F binding C-terminal region, CDK5 sites) lie within 1-338 and are conserved.

## Function (human/rodent, transferred)

- Dynein regulator via LIS1 [file:human/NDEL1/NDEL1-uniprot.txt "Also positively regulates the activity of
  the minus-end directed microtubule motor protein dynein."].
- Centrosome microtubule anchoring [human UniProt "Required for organization of the cellular microtubule
  array and microtubule anchoring at the centrosome."].
- Neuronal migration [human UniProt "Also required during brain development for the migration of newly
  formed neurons from the ventricular/subventricular zone toward the cortical plate."].
- Kinetochore via CENP-F [human UniProt "Localizes to the kinetochore in a CENPF-dependent manner."].
- Family review: cytoskeletal motor regulator activity is family-wide; kinesin complex not applicable
  [file:interpro/panther/PTHR10921/PTHR10921-review.yaml "No member is a kinesin subunit."].

## Decisions

Mirrors the human NDEL1 review: ACCEPT location/core rows (centrosome, kinetochore, spindle, MTOC, axon,
microtubule associated complex, microtubule binding, cortical radial migration, cell migration, vesicle
transport along microtubule, centrosome localization); KEEP_AS_NON_CORE mitotic/secondary rows; REMOVE kinesin
complex (TreeGrafter; family review NOT_APPLICABLE); MARK_AS_OVER_ANNOTATED synaptic vesicle and insulin
receptor signalling; MODIFY identical protein binding -> protein homodimerization activity; NEW cytoskeletal
motor regulator activity (GO:0140659).

## ProtNLM2 GO predictions

- GO:0005815 microtubule organizing center: CNN (exact term in donkey GOA).
- GO:0005737 cytoplasm: LSP (donkey GOA has centrosome, spindle, axon etc.).
- GO:0030154 cell differentiation: UNC (generic; NDEL1 acts in neuronal migration and neurite outgrowth).
