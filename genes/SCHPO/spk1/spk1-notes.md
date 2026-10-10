# spk1 (P27638, SPAC31G5.09c) review notes

## Core identity

Spk1 is the fission-yeast Fus3/Kss1-like MAP kinase that acts at the bottom of
the Byr2 MAP3K -> Byr1 MAPKK -> Spk1 MAPK pheromone response cascade.

- Toda et al. first described `spk1+` as a protein kinase closely related to
  mammalian ERK1/MAP2 and budding-yeast KSS1/FUS3; spk1 was nonessential for
  vegetative growth but required for conjugation, and the 45 kD product was
  enriched in the nucleus. [PMID:1899230]
- Gotoh et al. showed that Spk1 undergoes mating-signal-dependent tyrosine
  phosphorylation, that phosphorylation is diminished in a `byr1` disruptant,
  and Xenopus MAPK can partially complement `spk1-` sporulation defects.
  [PMID:8413241]
- Neiman et al. established functional homology of the fission-yeast
  Byr2/Byr1/Spk1 module with the budding-yeast STE11/STE7/FUS3 pheromone module.
  [PMID:8443406]

## MAPK activity and pheromone-response cascade

The direct catalytic assay cached for this review is the Ste11 paper: a
constitutively active Byr2 allele activates the pheromone-responsive pathway,
Spk1 physically interacts with Ste11, and Spk1 phosphorylates Ste11 in vitro.
[PMID:15713656]

The `GO:0071507 pheromone response MAPK cascade` rows are well grounded:
Gotoh and Neiman establish the Byr2/Byr1/Spk1 cascade, Kjaerulff 1994 places
M-factor transcription under the pheromone-response machinery, and Kjaerulff
2005 connects Spk1 to Ste11-dependent downstream transcription and meiotic
output. [PMID:8413241; PMID:8443406; PMID:8196631; PMID:15713656]

## IBA / PAINT

The broad `PTN000622075` PANTHER node is the root MAPK family node. Its
Ser/Thr kinase, nucleus, and cytoplasm assertions are broad, but they are not
wrong-paralog propagations for Spk1: Spk1 retains the conserved MAPK catalytic
machinery and has target-specific evidence for MAPK activity and nuclear
localization.

The `PTN001172087` node is more specific: it is the fungal Spk1/Fus3
pheromone-MAPK node seeded by PomBase `SPAC31G5.09c` and SGD `S000000112`.
The target appearing in its own `WITH/FROM` reflects the Spk1 experimental
evidence used by PAINT to place the function at this node, not circular
propagation.

The PAINT file also has `PTN000622075` -> `GO:0035556 intracellular signal
transduction`, but that term would be a generic ancestor-like process beside
the direct pheromone response MAPK cascade rows, so it was not proposed as new.

## Interaction rows

The three `GO:0005515 protein binding` IPI rows are functionally interpretable
from their `WITH/FROM` partners:

- `P10506` is Byr1, the upstream MAPKK, so the useful replacement is
  `GO:0031434 mitogen-activated protein kinase kinase binding`.
- `SPBC32C12.02` is Ste11, a DNA-binding transcription factor substrate, so
  the useful replacement is `GO:0140297 DNA-binding transcription factor
  binding`.

## Newer literature

A 2026 Nature Communications paper identified Sms1 as a hemi-arrestin scaffold
that recruits and organizes the fission-yeast pheromone MAPK cascade at the
plasma membrane and showed that MAPK-dependent negative feedback opposes Sms1
membrane accumulation. This adds mechanistic detail to the pathway but does not
require a new Spk1 GO term beyond MAP kinase activity and the pheromone
response MAPK cascade. [PMID:41844616]

A 2026 PLOS Biology paper used phospho-Spk1 as a readout of pheromone MAPK
activation while studying Cdc42 thresholds for fission-yeast mating and cell
fusion; it did not change the Spk1 annotation decisions.
