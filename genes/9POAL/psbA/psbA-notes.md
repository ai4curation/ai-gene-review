# psbA (Photosystem II protein D1) - Zea mays - Review Notes

## Gene Overview

psbA encodes the D1 protein, one of the two core reaction center subunits of Photosystem II (PSII). It is chloroplast-encoded and one of the most highly conserved genes across all oxygenic photosynthetic organisms. The UniProt representative entry used for this review is P48183 (Zea mays, maize).

## Key Functional Features

### Water:plastoquinone oxidoreductase (EC 1.10.3.9)
- D1/D2 heterodimer catalyzes: 2 plastoquinone + 4 hν + 2 H₂O = 2 plastoquinol + O₂
- D1 provides the QB plastoquinone binding site (His-215, Ser-264, Phe-265)

### Oxygen-Evolving Complex (OEC)
- D1 provides 5 of 7 protein ligands to the Mn₄-Ca-O₅ cluster: Asp-170, His-189, Glu-332, His-333, Ala-342, Ala-344
- Tyr-161 (TyrZ) is the redox-active radical intermediate that extracts electrons from water

### Cofactor binding
- Chlorophyll a: ChlzD1 (His-118), PD1 (His-198, part of P680 reaction center)
- Pheophytin a: PheoD1 (Glu-126)
- Non-heme Fe: His-215, His-272 (shared with D2)
- Plastoquinone QB: His-215, Ser-264, Phe-265

### Herbicide target
- QB binding pocket is the target of triazine (atrazine), urea (diuron), and nitrile (ioxynil) herbicides
- Herbicide resistance mutations in psbA are well-characterized (e.g., Ser-264 → Gly confers atrazine resistance)

### Photoinhibition and turnover
- D1 is the primary target of light-induced damage in PSII
- Rapid turnover: damaged D1 is degraded by FtsH and Deg1 proteases and replaced by de novo synthesis
- In maize: D1 degradation is faster in bundle sheath cells [PMID:22833285]

### Post-translational modifications
- C-terminal processing by CTPA protease (essential for OEC assembly)
- N-terminal acetylation at Thr-2 [PMID:22833285]
- Phosphorylation at Thr-2, light-dependent [PMID:22833285]

## Review Decisions

### Accepted as core
- GO:0009523 (photosystem II) - IBA, defining CC annotation
- GO:0010242 (oxygen evolving activity) - IEA, core MF
- GO:0016168 (chlorophyll binding) - IEA, core MF
- GO:0016682 (oxidoreductase activity, diphenols as donors, O₂ as acceptor) - IEA, core MF (EC 1.10.3.9)
- GO:0009055 (electron transfer activity) - IEA, core MF
- GO:0009535 (chloroplast thylakoid membrane) - IEA, confirmed by PMID:22833285
- GO:0009772 (photosynthetic electron transport in PSII) - IEA, most specific BP

### Kept as non-core
- GO:0005506 (iron ion binding) - real but subsidiary to Mn₄-Ca-O₅ cluster binding
- GO:0015979 (photosynthesis) - too broad, redundant with GO:0009772
- GO:0009536 (plastid) - too broad, redundant with GO:0009535
- GO:0019684 (photosynthesis, light reaction) - intermediate specificity, redundant

### Proposed new annotations
- GO:0030145 (manganese ion binding) - D1 provides most OEC cluster ligands
- GO:0048038 (quinone binding) - QB plastoquinone binding site, herbicide target

## Organism Context

9POAL (Poales) is a taxonomic grouping. The representative entry P48183 is from Zea mays (maize, NCBITaxon:4577). psbA is essentially identical across Poales grasses given its extreme conservation.

## References

- PMID:22833285 - Fristedt et al. 2012, thylakoid protein phosphorylation in maize M/BS cells
- PMID:7666415 - Maier et al. 1995, complete maize chloroplast genome sequence
- HAMAP-Rule:MF_01379 - comprehensive annotation rule for PSII D1
