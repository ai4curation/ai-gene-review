# pvdE Notes

## Identity and basic architecture

- `pvdE` in *Pseudomonas putida* KT2440 corresponds to UniProt `Q88F82` / locus `PP_4216` and is annotated as a "Pyoverdine ABC export system, fused ATPase and permease components" [file:PSEPK/pvdE/pvdE-uniprot.txt, "SubName: Full=Pyoverdine ABC export system, fused ATPase and permease components"].
- PvdE is a 552 aa fused ABC exporter with an N-terminal multi-pass membrane domain and a C-terminal nucleotide-binding domain [file:PSEPK/pvdE/pvdE-uniprot.txt, "DOMAIN          12..299"] [file:PSEPK/pvdE/pvdE-uniprot.txt, "DOMAIN          336..552"].
- UniProt predicts cell membrane localization and multiple transmembrane helices, consistent with an inner membrane transporter [file:PSEPK/pvdE/pvdE-uniprot.txt, "SUBCELLULAR LOCATION: Cell membrane"] [file:PSEPK/pvdE/pvdE-uniprot.txt, "Multi-pass membrane protein"].

## Function inference

- *P. putida* KT2440 produces a characterized pyoverdine siderophore, so `pvdE` fits an intact pyoverdine biosynthetic/export module in this strain [PMID:19459056 Siderophore-mediated iron acquisition in the entomopathogenic bacterium Pseudomonas entomophila L48 and its close relative Pseudomonas putida KT2440, "Structural analysis of the pyoverdine produced by the closely related P. putida KT2440 showed that this strain produces an already characterised pyoverdine"].
- In experimentally dissected pyoverdine biosynthesis in *Pseudomonas aeruginosa*, PvdE transports the precursor PVDIq to the periplasm before downstream maturation steps [PMID:24816606 PvdP is a tyrosinase that drives maturation of the pyoverdine chromophore in Pseudomonas aeruginosa, "PvdE transports PVDIq to the periplasm"].
- The best-supported specific role is ATP-dependent export of the pyoverdine precursor PVDIq from the cytoplasmic side of the inner membrane to the periplasm [PMID:24816606 PvdP is a tyrosinase that drives maturation of the pyoverdine chromophore in Pseudomonas aeruginosa, "PvdE transports PVDIq to the periplasm"].
- The specific substrate assignment is based on experimental work in *Pseudomonas aeruginosa* and on strong orthology/domain conservation, not on a direct biochemical assay of the KT2440 protein.

## GO review implications

- `GO:0005886` plasma membrane is appropriate for this protein because the UniProt entry calls it a cell membrane multi-pass protein and the topology is transporter-like.
- `GO:0140359` ABC-type transporter activity is the most reliable current molecular function term for the KT2440 protein.
- `GO:1904680` peptide transmembrane transporter activity is plausible because the transported cargo is a peptidyl pyoverdine precursor, but the term is still imperfect because it does not convey siderophore-precursor specificity.
- `GO:0034040` ATPase-coupled lipid transmembrane transporter activity is not supported; the inferred cargo is a pyoverdine precursor rather than a lipid.
- `GO:0015891` siderophore transport is a better biological process term than generic `transmembrane transport` for this protein.
- `GO:0019290` siderophore biosynthetic process is justified because PvdE acts within the pyoverdine maturation pathway rather than in general peptide transport.

## Term gap

- Current GO molecular function terms do not capture ATP-driven export of a pyoverdine precursor from the cytoplasmic membrane to the periplasm.
- A useful new term would be "pyoverdine precursor transmembrane transporter activity".
