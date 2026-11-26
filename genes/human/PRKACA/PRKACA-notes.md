# PRKACA notes for GO-CAM 69b3372b00003343

## Scope

GO-CAM 69b3372b00003343 uses UniProtKB:P17612 for the PRKACA catalytic alpha
subunit in the nuclear PKA step of the human granulosa-cell FSH model. The
activity is typed as cAMP-dependent protein kinase activity and is connected
directly to CREB1.

## Core biology

PRKACA is the alpha catalytic subunit of PKA. The catalytic subunit binds PKA
regulatory subunits in inactive tetrameric holoenzymes; cAMP binding to the
regulatory dimer releases active catalytic subunits. PMID:21812984 states that
"PKA is a heterotetrameric holoenzyme consisting of a regulatory (R) subunit
dimer and two catalytic (C) subunits" and that C-alpha-2 is sperm restricted,
while the UniProt record describes isoform 1 as ubiquitous and isoform 2 as
sperm-specific.

The granulosa-cell paper used in the GO-CAM, PMID:29397057, reports that
knockdown of AKAP8 or inhibition of AKAP95 in KGN and primary cultured human
luteinised granulosa cells "reduced the amount of PKA anchored in the nucleus
and attenuated the phosphorylation of CREB" after FSH or cAMP/PKA stimulation.
The same abstract reports reduced FSH-induced CYP19A1 expression and estrogen
synthesis. This supports the GO-CAM pathway context, but it does not distinguish
which PKA catalytic isoform phosphorylates CREB in granulosa cells strongly
enough to add a PRKACA-specific ovarian follicle development row.

## GO-CAM consistency notes

- The PRKACA activity's molecular function, `GO:0004691` cAMP-dependent protein
  kinase activity, agrees with this review.
- The nucleus location agrees with this review. PRKACA has cytosolic and nuclear
  roles, and the FSH granulosa-cell evidence specifically uses nuclear PKA.
- The GO-CAM edge from PRKACA to CREB1 is biologically right: PKA phosphorylates
  CREB at Ser-133 and thereby promotes CREB transcriptional activity. The
  attached `PMID:11029056`, however, is the MAP2c phosphorylation paper and does
  not support a CREB1 edge; the model review correctly points to `PMID:2573431`
  or the granulosa-cell `PMID:29397057` instead.
- The GO-CAM process evidence for PRKACA uses malformed `GO_REF:000024` with no
  with/from. The final GO-CAM consistency PR should either point this context to
  granulosa-cell evidence such as `PMID:29397057` or keep the follicle
  development term at the model level rather than as a direct PRKACA gene
  annotation.
- The incoming GNAS-to-PRKACA edge intentionally compresses adenylyl cyclase,
  cAMP production and release of PRKACA from the PKA regulatory subunit dimer.
  That compression should be noted in the final GO-CAM consistency PR, but it is
  not a conflict with the gene review.

## Annotation-review notes

PAINT loss check: `just paint-losses human PRKACA` on 2026-11-25 reported no IRD
or IKR loss on the PRKACA P17612 lineage.

The many `GO:0005515` rows were handled under the generic protein-binding
policy. Rows whose partner is a PKA regulatory subunit were modified to
`GO:0034237` protein kinase A regulatory subunit binding; rows whose partner is
GSK3 or LRRK2 were modified to `GO:0019901` protein kinase binding; low-throughput
substrate papers that support catalysis were modified to `GO:0004691`; and
high-throughput interaction-only rows were removed as uninformative.

The RyR2/cardiac review rows, GLP-1 potassium-channel rows, GPR146 cholesterol
row, HSF1 heat-shock row, Raptor/mTORC1 row, GLI/OFD1 ciliary rows, and
SLC6A6 plasma-membrane localization row all describe real peripheral PKA
branches. They were kept as non-core unless the row was a broad tissue phenotype
that did not show PRKACA itself executing a step in that process.

The remaining over-annotation calls are broad inferences or detections that stop
short of interpretable PRKACA biology. The EnsemblCompara domain-specific-binding
row lacks a named binding domain or a named partner. The same electronic source
for neuromuscular junction does not show stable PRKACA localization at the
junction. The prostate extracellular-vesicle HDA row is a weak possible cargo
detection beside stronger cytosolic and nuclear PKA locations.
