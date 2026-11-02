# NIP3-1 review notes

- 2026-10-28: Created review. fetch-gene resolved Q9ATN1 (reviewed Swiss-Prot,
  GeneID 541885); GOA has 18 rows, all IBA/IEA, no experimental rows for maize.
- Gene = tassel-less1 (tls1) [PMID:25035406; PMID:24685595]. Core function: boric acid
  (borate) channel at the plasma membrane mediating B uptake; also water-permeable in
  oocytes [PMID:25035406 "the TLS1 protein facilitates the movement of B and water into Xenopus laevis oocytes"].
- Ensembl Compara rows from AtNIP5;1 (AT4G10380) for histone H3T11 kinase activity,
  nucleus, response to glucose and (via inference) chromatin remodeling come from TAIR
  annotations to PMID:39367257, a paper about nuclear pyruvate kinases PK6/PK7/PK8.
  Removed and recorded as source defects (TAIR wrong gene product upstream).
- Arsenite rows: plausible from AtNIP5;1 As(III) permeability (PMID:19029297), untested
  for ZmNIP3;1 -> UNDECIDED.
- Lateral plasma membrane: from AtNIP5;1 polar localization (PMID:20194745); untested in
  maize -> UNDECIDED (the GO term definition is epithelial-flavoured too).
- No NEW process terms: inflorescence/meristem phenotypes are downstream of B supply.
- The task listed PMID:18430213 as a key paper; it is about maize tryptophan synthase
  alpha (ZmTSA) and is unrelated to NIP3-1. Not used.
