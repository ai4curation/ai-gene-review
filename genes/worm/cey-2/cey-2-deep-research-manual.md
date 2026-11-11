# cey-2 (C. elegans, F46F11.2, UniProt P91306): manual literature review

No deep-research API was available in this environment. This file records a manual
literature survey done with PubMed searches and the cached publications in
`publications/`. Every assertion carries its source.

## Search performed

PubMed query `(cey-2 OR CEY-2 OR "Y-box") AND elegans` (10 hits, 2026-10-28). The
relevant primary papers are PMID:16247027, PMID:16221731, PMID:25378320 and
PMID:39423228. The others concern mammalian YB-1/SOX proteins or are reviews.

## Identity and domain architecture

- CEY-2 is a 267-aa protein with a single cold shock domain (CSD, residues 65-135,
  PROSITE PS51857) followed by a long disordered, basic and low-complexity C-terminal
  region (MobiDB-lite) [file:worm/cey-2/cey-2-uniprot.txt].
- It is one of four C. elegans Y-box-binding proteins (CEY-1 to CEY-4). "CEY-2 and
  CEY-3 are around 270 amino acids in length and are 70% identical. As their
  expression patterns also overlap (see below), CEY-2 and CEY-3 very likely have
  redundant functions." [PMID:25378320]
- Unlike CEY-1 and CEY-4, CEY-2 lacks RG/RGG repeats: "Besides the CSD, CEY-1 and
  CEY-4 contain RG/RGG repeats, which are absent in CEY-2 and CEY-3." [PMID:25378320]
- Hayden et al. 2024 conclude that CEY-1, not CEY-2, is the closest ortholog of
  mammalian YBX1/YBX3 [PMID:39423228, "we determined that cey-1 is the closest
  ortholog to the mammalian Y-Box (YBX) RBPs"].

## Complex membership (CAR-1 / CGH-1 mRNP)

- Tandem affinity purification of GFP-LAP:CAR-1 from embryos/worms recovered CAR-1,
  CGH-1 and CEY-2 by mass spectrometry: "we obtained significant sequence coverage
  for CAR-1 and two additional proteins, the RNA helicase, CGH-1, and the Y-box
  domain–containing protein, CEY-2, which also is predicted to bind RNA"
  [PMID:16247027].
- The CAR-1/CGH-1 association is RNase-sensitive: "We conclude that CAR-1 is a
  component of an RNase-sensitive, multiprotein complex of conserved RNA-binding
  proteins." [PMID:16247027]
- The cey-2(ok902) deletion alone had no phenotype: "a strain harboring a cey-2
  deletion allele (ok902) did not exhibit any phenotype" [PMID:16247027].
- Depleting CEY-2 did not alter CAR-1 or CGH-1 localization: "depletion of CEY-2 or
  PGL-1 did not affect the targeting of CAR-1 or CGH-1" [PMID:16247027].
- Boag et al. 2005 independently describe CAR-1 associating "with CGH-1 and Y-box
  proteins within a conserved germline RNA-protein (RNP) complex" [PMID:16221731,
  abstract only; the abstract does not name CEY-2 specifically].
- Arnold et al. 2014 confirm by co-IP that FLAG-CEY-2 associates with CGH-1 and
  GLD-1 in an RNA-dependent way: "These data were confirmed by co-IPs performed
  again with or without RNAse treatment on FLAG-CEY-2 (chosen instead of FLAG-CEY-1
  to include a germline-specific CEY protein)" [PMID:25378320].

## Expression and subcellular localization

- Germline-specific: "cey-1 and cey-4 were present in both the soma and the
  germline, whereas cey-2 and cey-3 were only expressed in the germline"
  [PMID:25378320]. Upregulated on meiotic entry and lost during the
  oocyte-to-embryo transition [PMID:25378320, "we observed the disappearance of
  GFP-tagged versions of CEY-2 and CEY-3 during the oocyte-to-embryo transition"].
- Cytoplasmic, not nuclear: "immunostaining and GFP localization experiments showed
  that CEY proteins were only present in the cytoplasm in both soma and germline"
  and "Knockdown of xpo-1 ... did not cause an accumulation of CEY-1 or CEY-2 in the
  nucleus" [PMID:25378320].
- Single-cell RNA-seq detects cey-2 in only eight L4 neurons [PMID:39423228].

## RNA association

- RIP (FLAG-CEY-2 IP, RNA-seq) showed no specific mRNA enrichment: "We thus conclude
  that CEYs do not have a clear preference for binding specific subsets of mRNAs, a
  result expected for proteins that either do not bind mRNA or interact with
  messages in an unspecific fashion." [PMID:25378320]. Direct RNA binding by CEY-2
  has therefore not been demonstrated biochemically; it is inferred from the CSD
  and the RNA-dependent associations.

## Phenotypes (necessity evidence, not mechanism)

- cey-2,-3 RNAi: fewer proliferating germ cells, more germ-cell apoptosis and
  premature oocyte maturation markers [PMID:25378320, "Thus, CEY-2 and -3 are
  required for normal levels of germ cell proliferation and survival."].
- cey-2,-3 double mutants produce about half the wild-type progeny, and maternal
  mRNAs (e.g. rme-2) are reduced: "abundance of tested maternal mRNAs was more
  strongly affected in cey-2,-3 mutant animals, compared to cey-1,-4 double mutants,
  supporting a predominant role for CEY-2 and -3 during oogenesis" [PMID:25378320].
- In the cey-1,-2,-3,-4 quadruple mutant, CAR-1, CGH-1 and GLD-1 collect in aberrant
  RNP granules: "Thus, CEYs are important for normal RNP appearance in the C. elegans
  germline" [PMID:25378320].
- Polysome profiles of cey-2,-3 mutants were normal; the polysome role belongs to
  CEY-1/CEY-4 [PMID:25378320, "Polysome profiles from wild-type and cey-2,-3 mutants
  were indistinguishable."].
- Adult-only neuronal RNAi screen: "cey-2 knockdown causes ITM deficits"
  (intermediate-term memory) [PMID:39423228]. A single RNAi phenotype in a
  neuronally sensitized strain, for a gene detected in very few neurons.

## Synthesis

CEY-2 is a germline-specific, cytoplasmic Y-box (cold shock domain) protein that is a
component of the CAR-1/CGH-1 maternal mRNP and is, redundantly with its paralog
CEY-3, needed for normal oogenesis and maternal mRNA abundance. Its molecular
activity is most plausibly non-sequence-specific mRNA binding/packaging, as for
Xenopus FRGY2 and mouse MSY2, but this has not been shown directly for CEY-2.
