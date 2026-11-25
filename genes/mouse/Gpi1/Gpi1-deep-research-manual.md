# Gpi1 manual deep research

Automated Falcon deep research with `--fallback perplexity-lite` failed in this
workspace because neither provider was available, so this file records the manual
research pass from UniProt, the mouse GPI primary literature already cached for
GOA, the human GPI review, the Schizosaccharomyces pombe pgi1 review, the
PANTHER:PTHR11469 family review, and the 61e0/62d0 GO-CAM context.

## Accession

`just fetch-gene mouse Gpi1` initially resolved exact UniProt gene name `Gpi1` to
the 191 aa TrEMBL fragment `A0A0U1RQ18`. The GO-CAM enabled_by is
`MGI:MGI:95797`, and UniProt reviewed full-length mouse GPI is `P06745`
(`G6PI_MOUSE`), a 558 aa entry cross-referenced to the same MGI gene. The review
was therefore re-fetched as `P06745 --alias Gpi1` and all decisions below apply
to the full-length protein.

## Core enzyme

Mouse Gpi1 encodes the canonical soluble GPI enzyme: "The mouse Gpi1 gene
encodes the glycolytic enzyme glucose phosphate isomerase" and GPI "catalyses
the conversion of glucose-6-phosphate to fructose-6-phosphate at the second step
in glycolysis and the reverse reaction during gluconeogenesis" [PMID:27103217].
Mouse ENU alleles directly reduce GPI activity in blood and tissues [PMID:2344351,
"Two glucose-6-phosphate isomerase (GPI) mutants with approximately 60%
residual activity in blood compared to wild type"]. A null allele eliminates
enzyme activity and homozygotes die early after implantation [PMID:1582174,
"Homozygous mutants died at an early post-implantation stage of embryogenesis"].

The PANTHER PTHR11469 review places `GO:0004347 glucose-6-phosphate isomerase
activity`, `GO:0006094 gluconeogenesis`, `GO:0051156 glucose 6-phosphate
metabolic process`, and `GO:0048029 monosaccharide binding` at PAINT node
`PTN000157839` for the family. `just paint-losses mouse Gpi1` found no IRD or
IKR on the `P06745` lineage, so the PAINT assertions are current for mouse.

## Secondary and peripheral roles

Secreted GPI moonlights as neuroleukin/autocrine motility factor. The
neuroleukin literature supports immunoglobulin secretion [PMID:3020690,
"Neuroleukin is a lymphokine product of lectin-stimulated T cells that induces
immunoglobulin secretion by cultured human peripheral blood mononuclear cells"],
and AMF stimulates endothelial and tumor-cell motility [PMID:11437381, "AMF
stimulated in vitro motility of human umbilical vein endothelial cells";
PMID:1649192, "Purified AMF stimulated HT-1080 cell migration in a
dose-dependent fashion"]. These are genuine moonlighting functions but are
peripheral to the cytosolic G6P/F6P isomerase function.

UniProt curates the G6P anomerase and mannose-6-phosphate C2-epimerase
activities by similarity to yeast or mammalian proteins rather than from mouse
assays. `GO:0047938 glucose-6-phosphate 1-epimerase activity` is therefore kept
as non-core, while the broader carbohydrate racemase/epimerase parent is
redundant.

## GO-CAM context

Gluconeogenesis 1 (`61e0e55600001225`) and Gluconeogenesis 3
(`62d0afa500000298`) use `MGI:MGI:95797` to enable `GO:0004347` in
`GO:0005829` and `GO:0006094`. That matches the reviewed full-length mouse GPI
core function: Fbp1 produces fructose 6-phosphate, Gpi1 converts it to glucose
6-phosphate in the cytosol, and Slc37a4 then moves glucose 6-phosphate into the
ER for dephosphorylation.
