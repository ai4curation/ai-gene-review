# VMA8 manual notes

## Evidence synthesis

Candida albicans Vma8 is UniProtKB:P87220, a reviewed V-type proton ATPase
subunit D in PANTHER family PTHR11671. UniProt links the C. albicans record to
PTHR11671 directly [file:genes/CANAL/VMA8/VMA8-uniprot.txt,
"DR   PANTHER; PTHR11671; V-TYPE ATP SYNTHASE SUBUNIT D; 1."] and curates the
protein as a V1-sector subunit by similarity to S. cerevisiae VMA8/P32610.

The primary experimental donor evidence is in S. cerevisiae. Graham et al.
identified VMA8 as the 32-kDa subunit D of the vacuolar V-ATPase and showed
that a vma8 deletion had no vacuolar V-ATPase activity and failed to recruit
V1 subunits to the vacuolar membrane [PMID:7797485, "Vacuolar membranes
isolated from vma8 delta yeast cells exhibited no V-ATPase activity."].
Xu and Forgac then mutagenized Vma8p and showed that subunit D affects coupling
between proton transport and ATP hydrolysis [PMID:10801866, "These results
suggest that subunit D plays an important role in coupling of proton transport
and ATP hydrolysis"].

The PTHR11671 PAINT slice should be read node-first:

- `PTN000912657` is a curated fungal node and asserts `GO:0000329`
  fungal-type vacuole membrane and `GO:0016471` vacuolar
  proton-transporting V-type ATPase complex. Its short extant donor list is
  not a weakness; the assertion is the curator's placement on the fungal
  branch.
- `PTN000186829` asserts `GO:0007035` vacuolar acidification on a broader
  eukaryotic branch.
- `PTN002268884` asserts `GO:0046961` proton-transporting ATPase activity,
  rotational mechanism for subunit D descendants. GOA correctly weakens this
  row with `contributes_to`, since Vma8 is a V-ATPase subunit rather than an
  independent proton pump.

## Curation decisions

I accepted the PAINT rows for fungal-type vacuole membrane, the vacuolar
V-ATPase complex, vacuolar acidification, and contribution to the rotary
proton-transporting ATPase activity. The UniProt and EnsemblFungi rows for
`GO:0005774` vacuolar membrane and `GO:0033176` proton-transporting V-type
ATPase complex are true parents of the accepted fungal/vacuolar terms, so they
are `TOO_GENERAL` rather than false.

The UniProt ISS row to `GO:0000221` V1 domain is true for C. albicans Vma8, but
the GOA `WITH/FROM` donor is UniProtKB:P16140, which is S. cerevisiae VMA2
subunit B rather than the VMA8 ortholog P32610. I kept the row because the
term is right and noted the source-side donor problem in the row review.

The EnsemblFungi `GO:0045121` membrane raft row was marked
`MARK_AS_OVER_ANNOTATED`. That location is absent from the PTHR11671 PAINT
family and from the curated subcellular-location comment in the P87220 UniProt
record, which states "Vacuole membrane" for the Candida protein
[file:genes/CANAL/VMA8/VMA8-uniprot.txt, "CC   -!- SUBCELLULAR LOCATION:
Vacuole membrane"].

The UniProt IEA row to `GO:0046961` uses `enables`, which overstates a
complex-level activity for this non-catalytic subunit. The accepted PAINT row
uses `contributes_to` and is the correct qualifier.

The 2026 H. pylori co-culture paper directly measures VMA8 expression after
co-culture, but not Vma8 activity, localization, or vacuolar acidification
[PMID:41957610, "The results demonstrated that the first passage CacoHp
exhibited higher expression levels of END3, SNQ2, ENO1, VMA8, and CTA1
compared with the SC5314 strain"]. I kept it only as a low-relevance stress
expression note.
