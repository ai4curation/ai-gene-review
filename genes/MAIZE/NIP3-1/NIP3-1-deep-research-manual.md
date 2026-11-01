# NIP3-1 (ZmNIP3;1, TASSEL-LESS1) — manual literature research

Deep-research API providers were not available in this environment; this file was
compiled manually from PubMed searches and cached publications.

## Identity

- UniProt Q9ATN1 (NIP31_MAIZE), Aquaporin NIP3-1 / ZmNIP3;1, 302 aa, GeneID 541885,
  MaizeGDB 403452, Zm00001eb043650, chromosome 1. Named in the maize aquaporin survey
  [PMID:11244102 "Aquaporins constitute a large and highly divergent protein family in maize"].
- The classical inflorescence mutant locus *tassel-less1* (*tls1*) encodes ZmNIP3;1
  [PMID:24685595 "ZmNIP3;1 (a NOD26-like intrinsic protein) was identified as the candidate gene for tls1"];
  [PMID:25035406 "the six EMS -induced tls1 alleles were found to have nonsynonymous mutations in the coding region of a gene encoding the major intrinsic protein NIP3;1"].
- NIP subgroup II (NIP5;1/NIP6;1/OsNIP3;1 clade); grass tls1 clade with rice NIP3;1a
  [PMID:25035406 "tls1 falls in a well-supported (>0.95 posterior probability) monocot-specific clade along with rice NIP3;1a"].
  Shares NPS/NPV NPA variants and AIGR ar/R filter with AtNIP5;1 and OsNIP3;1
  [PMID:25035406 "TLS1, At-NIP5;1 and Os-NIP3;1a are conserved at the dual NPA and ar/R motifs"].

## Molecular function (experimental, Xenopus oocytes)

- Water: [PMID:25035406 "it was concluded from these results that the TLS1 protein can facilitate the transport of water"].
- Boric acid: iso-osmotic swelling in 200 mM boric acid and 4-fold B accumulation by ICP-MS
  [PMID:25035406 "These results indicate that TLS1 is able to transport boric acid under these conditions."];
  [PMID:25035406 "The TLS1-expressing oocytes contained 4 times as much B as the mock-injected oocytes"].
- No arsenite, glycerol or urea transport data for ZmNIP3;1 were found. Arabidopsis
  NIP5;1 (the ortholog) is permeable to As(III) [PMID:19029297 "NIP1;2 and NIP5;1, closely related homologs of NIP1;1, were also permeable to As(III)"].

## In planta role

- tls1 mutants have reduced B in roots (~42%) and shoots (~24%), reduced borate-crosslinked
  RG-II dimer in immature inflorescences, and phenotypes rescued by B application
  [PMID:25035406 "B content is reduced in tls1 mutants, and application of B rescues the mutant phenotype"].
- Genetic interaction with *rotten ear* (BOR1-type efflux transporter) in inflorescence
  development under B limitation [PMID:25035406].
- Leonard et al.: deletion, Mu insertion and RNAi alleles; foliar B rescues tassel and ear
  development [PMID:24685595 "Foliar application of boron could rescue the tls1 phenotypes"].
  These are necessity/phenotype data: inflorescence development is a downstream
  consequence of B supply, not a process the channel performs.

## Subcellular location

- No direct localization of ZmNIP3;1 found. AtNIP5;1 is at the plasma membrane
  [PMID:16679457 "green fluorescent protein-tagged NIP5;1 proteins localized to the plasma membrane"]
  and polarly in the outer (distal) PM domain of root cells [PMID:20194745].
  The oocyte assay shows functional PM expression in a heterologous cell.

## Ortholog annotation artifacts

- AtNIP5;1 (AT4G10380) carries TAIR IDA/IEP annotations from PMID:39367257
  (histone H3T11 kinase activity, nucleus, response to glucose). That paper is about
  nuclear PYRUVATE KINASE 6/7/8, not NIP5;1 [PMID:39367257 "PYRUVATE KINASE 6 (PK6), PK7 and PK8 enter the nucleus"].
  These annotations appear to be on the wrong Arabidopsis locus and were projected to
  ZmNIP3-1 by Ensembl Compara.

## Note on PMID:18430213

PMID:18430213 (Kriechbaumer et al. 2008, maize tryptophan synthase alpha subunit) was
named as a key paper for this gene by the task; it does not mention NIP3-1, aquaporins
or boron, and is not relevant to this gene.
