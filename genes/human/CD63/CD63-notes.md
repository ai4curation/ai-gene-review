# CD63 notes

Deep research providers were unavailable in this environment (`just deep-research-falcon human CD63
--fallback perplexity-lite` failed: no provider configured). Research done from the 29 cached
publications and the UniProt record (P08962).

## Topology and localization (key for surface-accessibility questions)
- Tetraspanin: four transmembrane helices, large glycosylated second extracellular loop, cytoplasmic
  N- and C-termini; C-terminal GYEVM lysosomal targeting motif. UniProt: "Multi-pass membrane protein".
- Steady state is mostly intracellular: lysosome membrane, late endosome membrane, MVB/intraluminal
  vesicles, melanosomes, platelet dense granules, azurophil granules, Weibel-Palade bodies.
  [PMID:10793155 "the tetraspanin CD63/lamp3 distributes predominantly to the internal membranes of
  multivesicular-multilamellar late endosomes"]
- A functional plasma-membrane/cell-surface pool exists and increases on degranulation (classic
  platelet/basophil activation marker) [PMID:1993697 "originally described as a blood platelet activation marker"];
  surface TIMP1 binding [PMID:16917503] and surface association with beta1 integrin and VEGFR2
  [PMID:23632027] confirm extracellular-loop exposure.
- Released on exosomes (canonical exosome marker; many IDA/HDA rows).

## Functions
- Cell-surface binding partner for TIMP1, promoting beta1 integrin activation, survival and migration
  [PMID:16917503, PMID:24635319].
- Bridges VEGFR2 and beta1 integrin, required for VEGFR2 activation and internalization
  [PMID:23632027 "CD63 was furthermore required for efficient internalization of VEGFR2 in response to VEGF"].
- ESCRT-independent sorting of the PMEL luminal domain into ILVs; melanosome maturation [PMID:21962903].
- Limits surface abundance of the colonic H+-K+-ATPase [PMID:15647390].

## Curation decisions
- Protein-binding rows: TIMP1 rows modified to signaling receptor activity (CD63 is the cell-surface
  receptor for TIMP1); EspZ, retroviral env FRET-PLA methods paper and HuRI TMEM80 rows removed as
  uninformative.
- Broad location terms (lysosome, late endosome, MVB, membrane, vesicle, extracellular region) modified
  to the specific compartments already carried experimentally.
