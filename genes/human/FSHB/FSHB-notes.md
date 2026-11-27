# FSHB notes

## GO-CAM 69b3372b00003343 review

FSHB is in GO-CAM `69b3372b00003343` as one part of the
`GO:0016914` follicle-stimulating hormone complex that enables
`GO:0016913` follicle-stimulating hormone activity. The model is correct to
use the complex rather than FSHB alone for the extracellular ligand step:
human FSH is a CGA:FSHB heterodimer, and cotransfecting `FSHB` with `CGA`
rescues rapid secretion of biologically active recombinant FSH
[PMID:2494176, "cotransfection of the FSH beta and alpha subunit genes
resulted in \"rescue\" of the beta subunit and rapid secretion of dimer"].

The same GO-CAM activity has the reference defect already called out in the
GO-CAM review and in the CGA review: the `occurs_in extracellular region` and
`has_input FSHR` evidence on activity
`gomodel:69b3372b00003343/69b3372b00003379` cite `PMID:27889227`, a GPCR
trafficking review that does not mention FSH or FSHR. The FSHB review records
that as a `GO_CAM` source defect on the matching extracellular-region TAS row.

The FSH hormone activity in the model is not explicitly placed in
`GO:0042699` follicle-stimulating hormone signaling pathway. That missing
pathway context should be included in the final GO-CAM consistency notes PR,
not in a per-gene PR.

## Evidence summary

Direct experimental evidence establishes all three pieces of the FSHB core
function:

- Heterodimer assembly and secretion: FSHB alone was secreted slowly in CHO
  cells, while FSHB+CGA coexpression produced rapidly secreted dimeric FSH
  [PMID:2494176].
- Hormone-receptor engagement: the FSH:FSHR hormone-binding-domain crystal
  structure showed partially deglycosylated human FSH bound to the FSHR
  ectodomain [PMID:15662415], and the full-ectodomain structure resolved the
  hinge sulfotyrosine interaction that links FSH binding to receptor activation
  [PMID:22802634].
- Full receptor activation: the FSH-bound FSHR-Gs cryo-EM structure placed the
  FSH alpha and beta subunits in the active full-length receptor complex
  [PMID:36720854].

The older human FSH crystal structure is useful for the CGA:FSHB heterodimer
itself [PMID:11222739]. Later mutagenesis against the FSH:FSHR trimer model
tested FSH glycosylation and exosite residues in FSHR beta-arrestin and
granulosa estradiol assays [PMID:24692546].

## Over-annotation checks

Several rows are true only as downstream effects of FSHR signaling. I treated
these as over-annotations where the FSHB product is the extracellular ligand
rather than a component of the intracellular or cellular process:

- MAPK cascade from the FSH/FSHR review [PMID:35002517].
- Notch1 expression, proliferation, migration and transcriptional activation in
  SK-OV-3 ovarian cancer cells after FSH treatment [PMID:20613903].
- Betaglycan/TGF-beta pathway and progesterone rows from granulosa-luteal cells
  treated with FSH or prostaglandin [PMID:14557487].
- Female pregnancy from the FSHB loss-of-function case; the case supports
  follicular maturation/ovulation upstream of pregnancy [PMID:8220432].

`GO:0005737` cytoplasm is left as non-core rather than removed. The cached
`PMID:14602737` record is abstract-only and does not show the FSHB assay, so
it is not enough to overrule the direct UniProt row. A broad cytoplasmic or
secretory-granule signal is plausible for pituitary gonadotroph FSH beta during
biosynthesis, but the mature hormone acts in the extracellular region.

## Deep research

Automated deep research was attempted with Falcon plus Perplexity fallback for
FSHB, but the provider stack was unavailable in this runtime. I manually
reviewed the cached GOA publications, the FSHB UniProt record, the Reactome
events pulled by `just fetch-gene`, and the overlapping completed CGA and FSHR
reviews instead.
