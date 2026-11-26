# Fbp1 notes

## Deep research

`just deep-research mouse Fbp1 --provider perplexity` could not run in this
environment because the Perplexity provider was unavailable. I therefore used a
manual synthesis from the cached mouse UniProt record, the GOA-seeded
publications PMID:30150719 and PMID:16497803, the existing human and yeast FBP1
reviews, the PANTHER PTHR11556 family review, and the mouse Fbp1 GO-CAM
activities indexed in `gocams/index.tsv`.

## Core activity

Fbp1/Q9QXD6 is mouse fructose-1,6-bisphosphatase 1, a class I FBPase and EC
3.1.3.11 hydrolase that converts fructose 1,6-bisphosphate, plus water, to
fructose 6-phosphate and phosphate. The mouse UniProt catalytic-activity line
records RHEA:11064 for the reaction [file:mouse/Fbp1/Fbp1-uniprot.txt,
"Reaction=beta-D-fructose 1,6-bisphosphate + H2O = beta-D-fructose
6-phosphate + phosphate"], and the mouse metformin paper states that FBP1
catalyzes the irreversible F-1,6-P2 to F6P hydrolysis and is a key
rate-controlling enzyme of gluconeogenesis [PMID:30150719, "FBP1 catalyzes the
irreversible hydrolysis of fructose-1,6-bisphosphate (F-1,6-P2) to
fructose-6-phosphate (F6P) and inorganic phosphate"].

The GO-CAM activity for Fbp1 in both `61e0e55600001225` and
`62d0afa500000298` uses `GO:0042132` as part of `GO:0006094` in the cytosol,
which matches the core molecular function and the existing IBA/IEA/IMP/ISO/ISS
rows. The same PANTHER node, `PANTHER:PTN000168022`, is already reviewed as a
sound family-wide assertion of both `GO:0042132` and `GO:0006094` in
`interpro/panther/PTHR11556/PTHR11556-review.yaml`.

The GO-CAM index lists four mouse Fbp1 activities. The two siblings in scope
for this campaign, `61e0e55600001225` and `62d0afa500000298`, plus
`62d0afa500000132`, type Fbp1 as `GO:0042132` involved in `GO:0006094` in the
cytosol; `636d9ce800002041`, although titled "Positive regulation of
gluconeogenesis 1 (Mouse)", still types Fbp1 as the same enzyme step in
`GO:0006094`, matching the review's decision that Fbp1 is pathway machinery
rather than a distinct upstream regulator of gluconeogenesis.

PMID:16497803 showed that liver-directed human FBPase expression in transgenic
mice increased hepatic FBPase protein and enzyme activity and increased
glycerol conversion to glucose, supporting UniProt's statement that hepatic
FBPase abundance can modulate glycerol gluconeogenesis in mice.

## Non-core and propagated contexts

AMP binding, Mg2+ binding, substrate sugar-phosphate binding, and homotetrameric
self-association are true mechanistic properties of the enzyme rather than
separate core activities. The mouse UniProt record traces AMP, Mg2+, substrate,
and homotetramer statements by similarity to crystallographic bacterial or
human/rat FBPases.

Several GOA rows for Fbp1 are orthology transfers from human FBP1/P09467. The
human FBP1 review keeps the nuclear HIF-binding rows as non-core for human
clear-cell renal carcinoma cells. The same human evidence is enough to keep the
mouse ortholog transfers as plausible non-core HIF moonlighting rows, with the
open conservation question recorded below. The human gastric-cancer
cell-growth and Ras-context rows from PMID:19881551 are still cancer-cell
phenotypes rather than mouse Fbp1 physiology; the negative glycolysis term is
kept as non-core because FBP1 directly opposes the phosphofructokinase step.

The rat-derived Ensembl rows for responses to nutrient levels, insulin, cAMP,
osmotic stress, raffinose, phorbol ester, and extracellular localization are
not part of the conserved FBPase catalytic role, but the RGD source
publications were not inspected. Those rows are therefore left `UNDECIDED`
rather than given a definite over-propagation verdict.
