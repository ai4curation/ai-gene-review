# SDH2 (YLL041C, P21801) notes

Evidence journal for the review. No paid deep research was run; sources are the UniProt record and cached publications.

- Iron-sulfur (Ip) subunit of complex II; forms the catalytic dimer with Sdh1p [UniProt:P21801 "SDH1 and SDH2 form the catalytic dimer."].
- Electron relay: [PMID:24954416 "The two electrons that result from succinate oxidation are channeled through the three iron-sulfur clusters in Sdh2 to ubiquinone"]; [PMID:9822678 "The membrane extrinsic domain, consisting of Sdh1p and Sdh2p, contains a covalent FAD cofactor and three iron-sulfur clusters."]
- Architecture: [PMID:24954416 "The Sdh3/Sdh4 dimer binds the peripheral membrane protein Sdh2 (SDHB), which tethers the catalytic Sdh1 (SDHA) subunit to the complex."]
- Required for the holocomplex: [PMID:24954416 "We also observed that deletion of SDH2 or SDH4, which ablates the SDH holocomplex"].
- Genetics: [PMID:16232921 "the activity disappeared in double disruptants of the SDH1 and SDH2 or SDH1b (the SDH1 homologue) genes"].
- Membrane association depends on Sdh1p: [PMID:1939170 "Disruption of the flavoprotein subunit gene results in the simultaneous loss of both the iron-sulfur and the flavoprotein subunits from mitochondrial membranes."]
- Cofactors (UniProt, by similarity): one [2Fe-2S], one [3Fe-4S], one [4Fe-4S]. Only 2Fe-2S binding and generic Fe-S binding are in GOA; 3Fe-4S (GO:0051538) and 4Fe-4S (GO:0051539) binding are not annotated (possible addition).

Curation decisions
- The three IPI 'protein binding' rows (all with Sdh1p) were removed as uninformative; complex membership is captured by GO:0045273.
- Core MF: electron transfer activity (subunit-specific), contributes_to SQR activity GO:0008177. The existing 'enables' GO:0008177 rows (IDA 1957, IMP/IGI 2000) were accepted rather than second-guessed.
- Generic 'protein-containing complex' (RCA) and 'oxidoreductase activity' (IEA) were changed to the specific terms.
