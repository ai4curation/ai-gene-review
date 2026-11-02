# YNK1 (YKL067W, UniProt P36010) notes

## Function
- Sole NDP kinase (EC 2.7.4.6) of yeast, NM23/NME homologue: "which contains a single NM23 homolog, YNK1" [PMID:18983998].
- Broad specificity: acceptor order "dTDP greater than CDP greater than UDP ..."; "The broad substrate specificity and kinetic data suggest that the enzyme is involved in both DNA and RNA metabolism" [PMID:1659321].
- Mostly cytosolic, small IMS fraction: "a small fraction of total NDPK activity encoded by YNK1 is present in the intermembrane space (IMS) of mitochondria" [PMID:12472466]; IMS proteome confirms Ynk1 [PMID:22984289].
- ynk1 deletion: "delayed repair of UV- and etoposide-induced nuclear DNA damage by 3-6h" [PMID:18983998] (mechanism unknown).

## YeastCyc / GO-CAM
- YeastCyc UDPKIN-RXN has no gene, yet GOA RCA and GO-CAM PWY-7176 attach YNK1 to the UDP->UTP step (module notes this).
- RCA process mappings inherited from purine pathways are partly wrong for an NDPK: 'de novo GMP biosynthetic process' (PWY-6125, PWY-7221, PWY-7222-1), 'adenosine metabolic/biosynthetic process' (PWY-7220-1, PWY-6126-1), 'de novo pyrimidine nucleobase biosynthetic process' (PWY-7176, PYRIMID-RNTSYN-PWY, YEAST-DE-NOVO-PYRMID-DNT). MODIFIED to (d)GTP / dATP / UTP / dNTP biosynthesis.

## Review decisions
- Accept all NDPK MF rows (incl. 15 RCA), NTP biosynthesis, GTP/UTP/CTP biosynthesis, cytosol/cytoplasm, mitochondrion/IMS.
- Non-core: DNA damage response (IMP), pyrimidine ribonucleotide salvage, purine-containing compound salvage.
