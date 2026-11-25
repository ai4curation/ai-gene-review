# exg1 notes

## 2026-10-11

`just fetch-gene SCHPO exg1` seeded 19 GOA annotations for Q9URU6/SPBC1105.05
and cached the GOA literature. `just deep-research-falcon SCHPO exg1
--fallback perplexity-lite` could not run because no deep-research provider
credentials are configured, so this review was done manually from GOA, UniProt,
the PTHR31297 PAINT rows, cached full-text papers, and a web search for newer
`SPBC1105.05` / `exg1` / *Schizosaccharomyces pombe* literature.

The search found no newer exg1-specific functional paper beyond the 2025
phosphate-starvation secretome study already present in GOA as PMID:39660919.

### Core activity and localization

PMID:20852022 is the key direct biochemical and localization paper. The authors
identified fission-yeast `exg1+`, `exg2+`, and `exg3+` as GH5 proteins and
showed that Exg1 is secreted/extracellular, localizes to the division septum
during cytokinesis, and hydrolyzes beta-1,6-glucan endolytically rather than
exo-hydrolyzing beta-1,3-glucan:

- "Exg1 is secreted to the periplasmic space, Exg2 is a membrane protein, and
  Exg3 is a cytoplasmic protein."
- "The Exg1 protein localizes to the septum region in a pattern that was
  different from that of the endo-beta(1,3)-glucanase Eng1."
- "activity was detected only when pustulan was used as a substrate, indicating
  that Exg1 was a glucanase specific for beta(1,6) linkages"
- "The production of small amounts of glucose and large amounts of
  oligosaccharides of different sizes proved that Exg1 degraded linear
  beta(1,6)-glucan substrates with an endolytic mode of action."

The same paper argues Exg1 contributes to cell-wall beta-glucan metabolism but
does not show a strong cell-separation phenotype: `exg1Delta` and the triple
`exg1Delta exg2Delta exg3Delta` mutant had no obvious growth/cell-wall-agent
phenotype, and `exg1Delta eng1Delta` was essentially indistinguishable from
`eng1Delta`.

### Mating fusion

PMID:25825517 directly localizes GFP-tagged Exg1, Exg2, and Exg3 to the
Myo52-marked actin fusion focus during mating and shows that glucanase delivery
is part of focal cell-wall dissolution:

- "We used GFP tagged alleles of seven distinct glucanases--the
  endo-alpha(1,3)-glucanases Agn1 and Agn2 ..., the endo-beta(1,3)-glucanases
  Eng1 and Eng2 ..., and the beta(1,6)-glucanases Exg1, Exg2, and Exg3 ..."
- "Remarkably, all seven colocalized with Myo52-tdTomato at the fusion focus"
- "Further combinatorial double and triple deletion of agn2, eng2, and exg3 led
  to progressive decrease in fusion efficiency, indicating that each glucanase
  additively contributes to fusion."
- "glucanases are cargoes for myosin V Myo52, which concentrates them at the
  fusion focus for cell wall digestion during cell fusion."

### Phosphate-starvation secretome

PMID:39660919 used medium proteomics after 12 h in phosphate-free ePMGT medium
and detected Exg1 among the abundant secreted proteins. This corroborates the
extracellular-region annotation but should not be read as a phosphate-specific
core function for Exg1; the main biology of that paper is Efn1/Efn2
extracellular 5'-nucleotidase activity. The Exg1-relevant result is that the 13
most abundant phosphate-starved secretome proteins included "enzymes involved in
cell wall metabolism" and that previous RNA-seq found "exg1 (up eightfold)".

### PAINT / PTHR31297

PTHR31297 is the broad GH5 family containing fission-yeast Exg1, Exg2, and Exg3;
Saccharomycetales Exg1/Exg2/Spr1/Xog1 exo-1,3-beta-glucosidases; and
filamentous ascomycete exgB/exgD proteins.

Current PAINT rows:

- `PTN001262628` places `GO:0009251 glucan catabolic process` broadly in the
  family from *Aspergillus nidulans* exgD/exgB roots. This is broad but
  biologically consistent with Exg1 beta-glucan hydrolysis.
- `PTN001262686` places extracellular-region and fungal-type cell wall
  beta-glucan metabolic process on a fungal secreted/cell-wall glucanase node
  seeded by *Candida albicans* XOG1, fission-yeast exg1, and budding-yeast
  EXG1/EXG2/SPR1. This is sound for `exg1`; the direct PomBase annotation is an
  expected self-source, not circular support.
- `PTN001262687` places `GO:0004338 glucan exo-1,3-beta-glucosidase activity` on
  the Saccharomycetales XOG1/EXG1/SPR1 branch and should not hit
  fission-yeast `exg1`.
- `PTN008631699` places fission-yeast-specific `GO:0000935 division septum` and
  `GO:0046557 glucan endo-1,6-beta-glucosidase activity` from the PomBase
  `SPBC1105.05` experimental annotations; this exactly captures the lineage
  split from the Saccharomycetales exo-1,3-beta-glucosidases.
