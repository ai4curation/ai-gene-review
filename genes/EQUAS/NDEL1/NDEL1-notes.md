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

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

No ProtNLM2 file or prediction-evidence folder was opened for this pass.

Deep research: `just deep-research-falcon EQUAS NDEL1 --fallback perplexity-lite` failed at Edison login
(`HTTPStatusError: Client error '403 Forbidden' for url 'https://api.platform.edisonscientific.com/auth/login'`);
no deep-research file was written. Literature used instead: cached primary papers cited by the human NDEL1
review (PMID:16291865, 15473966, 20007476, 20403325, 14970193, 17600710, 37086789, 37730751, 38194050, 21283621,
19492042, 22114287, 17035248, 11163259, 17997972) and the human Swiss-Prot record.

### Identity: the benchmark is an alternative gene model

- UniProt holds ten unreviewed donkey NDEL1 entries from one Ensembl gene; none is reviewed, so no
  reviewed donkey canonical exists. They share the N-terminus and differ at the C-terminus
  [file:EQUAS/NDEL1/NDEL1-bioinformatics/RESULTS-rereview.md "All share the same N-terminal
  sequence and differ at the C-terminus, as alternative last exons would."].
- A0A9L0IJ72 (481 aa) is the only donkey model with the human isoform-1 last exon. It is collinear with human
  Q9GZM8 isoform 1 (345 aa) through residue 338, then replaces human GMLPLSV (339-345) with a 143-residue tail
  (donkey 339-481) found in no human isoform. The earlier note "donkey residues 339-474" came from end
  placement in the pairwise alignment; 339-481 is the correct span.
- All mapped functional sites are retained (LIS1-binding 114-133, CDK/MAPK phosphosites S198/T219/S231/S242/T245,
  DISC1 L266/E267, palmitoyl C273, centrosome-targeting 256-291). Only S344 has no counterpart.
- Family: PANTHER PTHR10921:SF0 (NDEL1 subfamily), the same subfamily as human/mouse/rat NDEL1. This agrees with
  the PTHR10921 family review's subfamily structure; no placement disagreement.

### Changes vs the previous review

- GO:0005815 MTOC: ACCEPT -> MODIFY to centrosome (the reason already argued it was less specific).
- GO:0005875 microtubule associated complex: ACCEPT -> KEEP_AS_NON_CORE (transient association, not a subunit).
- GO:0033157: replaced support that quoted the human record's own DR GO line with PMID:21283621.
- NEW GO:0030473 nuclear migration along microtubule, GO:0034454 microtubule anchoring at centrosome and
  GO:0060090 molecular adaptor activity (ISS from human/rodent, matching the human review's core functions;
  participation via LIS1-dynein regulation and dynein/dynactin tethering at the mother centriole
  [PMID:16291865 "Moreover, Nudel seems to tether dynactin and dynein to the mother centriole for MT anchoring."]).
- Primary-paper quotes added to the rows that had only UniProt support. The description was rewritten to state
  the correct tail span.
- Unchanged: REMOVE kinesin complex (kinesin-1 cargo, not a subunit; family review NOT_APPLICABLE);
  MARK_AS_OVER_ANNOTATED synaptic vesicle and insulin receptor signalling; non-core mitotic rows (vertebrate
  NDE1/NDEL1 clade per the family review).

### Relative

Human NDEL1 (Q9GZM8), same PANTHER subfamily SF0; complete review at `genes/human/NDEL1/NDEL1-ai-review.yaml`.
Module: `modules/nucleokinesis.yaml`.
