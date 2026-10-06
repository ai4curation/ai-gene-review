# PSD2 (YGR170W, P53037) notes

## Identity
- Non-mitochondrial phosphatidylserine decarboxylase proenzyme 2, EC 4.1.1.65; type II PSD with two C2 domains; peripheral membrane protein [UniProt:P53037].

## Evidence
- PSD2 activity = 4-12% of total; psd1 psd2 -> ethanolamine auxotrophy [PMID:7890739 "Recessive mutations resulting in loss of this enzyme activity (denoted psd2) in cells containing the psd1-delta 1::TRP1 null allele also result in ethanolamine auxotrophy."]
- Golgi/vacuole-like fraction [PMID:7890739 "the PSD2 enzyme activity does not localize to the mitochondria, but to a low density subcellular compartment with fractionation properties similar to both vacuoles and Golgi"]; endosomes [PMID:20016005 "Fluorescence microscopy and biochemical fractionation experiments demonstrate that Psd2 is localized to the endosomal system"].
- PS transport to Psd2 requires PstB2/Pdr17 and Psd2 C2 domain [PMID:14660568 "the transfer of PtdSer from liposomes to Psd2p fails to occur in acceptor membranes from strains lacking PstB2p or the C2 domain of Psd2p"]; Psd2-PstB2-Pbi1 complex [PMID:24366873 "our model predicts that this process involves an acceptor membrane complex containing the C2 domains of Psd2p, PstB2p, and Pbi1p"].

## Curation decisions
- Core: GO:0004609 + PE biosynthesis on endosome membrane. Golgi membrane kept non-core.
- Golgi stack IEA removed (budding yeast Golgi not stacked; Psd2 endosomal). Cytosol RCA removed. protein binding (Pdr17) removed per policy.
- GO:0120010 NAS kept non-core (C2 domains structurally required for PS transfer).
- GO:0006656 IDA from PMID:6427211 (1984, pre-cloning) raised as a question.
