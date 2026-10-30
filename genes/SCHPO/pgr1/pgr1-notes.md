# pgr1 (SPBC17A3.07, UniProt P78965) – notes

Glutathione reductase of S. pombe; module roles: GSR step in `glutathione_synthesis_gamma_glutamyl_cycle` and `glutathione_thioredoxin_redox_systems`. S. cerevisiae ortholog GLR1 (review: genes/yeast/GLR1).

## Evidence
- Activity/gene: [PMID:9287302 "The level of transcript as well as the GR enzyme activity increased more than 11-fold when the cloned pgr1(+) gene was expressed on a multicopy plasmid."]
- Essential, unlike budding yeast: [PMID:9287302 "When the pgr1(+) gene was disrupted, the haploid spores were not viable."]
- Overexpression protects against menadione but not H2O2 (basis of the NOT GO:0070301): [PMID:9287302 "This overexpression conferred on S. pombe cells more resistance against menadione, a redox cycling agent, but not against H2O2."]
- Pap1-dependent stress induction: [PMID:9287302 "The level of pgr1(+) transcripts increased by treatment with oxidants such as menadione, cumene hydroperoxide, and diamide."]
- Localisation: single start codon (no GLR1-like alternative initiation) yet dual location [PMID:16950927 "Therefore, unlike Saccharomyces cerevisiae , S. pombe uses only one start codon for GR."]; [PMID:16950927 "We found that GR resides in both cytosolic and organellar fractions of the cell."]. Organellar fraction was crude; "most likely in mitochondria". ORFeome HDA also says mitochondrion [PMID:16823372].
- Essential role = Fe-S enzyme maintenance; suppressed by mitochondrial Trx2: [PMID:16950927 "These results indicate that the essentiality of GR in the aerobic growth of S. pombe is derived from its role in maintaining oxidation-labile Fe-S enzymes and iron homeostasis."]
- FAD cofactor/homodimer by similarity to GLR1 [UniProt:P78965].

## Comparison
- Core function matches yeast GLR1 review (GO:0004362; BP cell redox homeostasis + glutathione metabolic process; cytosol + mitochondrion). S. pombe-specific differences: essential gene; single translation product (no alternative start).
- PomBase GO-CAM 68b0f0d000008341 places pgr1 only in mitochondrion (IDA PMID:16950927) and part_of GO:0006749; the module annoton puts it in cytosol. Both compartments are supported.
