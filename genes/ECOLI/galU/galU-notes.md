# galU (P0AEP3, GALU_ECOLI) notes

## Deep research status

- 2026-10-23: `just deep-research ECOLI galE --provider perplexity` failed in this
  environment (`Provider 'perplexity' not available. Available: falcon, openscientist`),
  so it was not re-attempted for galU. No deep-research file was generated. This review
  is based on cached publications, additional PMIDs fetched with `just fetch-pmid`, and
  the UniProt record.

## Identity

- E. coli K-12 galU (b1236; also ychD), UTP--glucose-1-phosphate uridylyltransferase
  (UDP-glucose pyrophosphorylase, UGPase), EC 2.7.7.9; 302 aa, initiator Met removed.
- Prokaryotic UGPase family (UDPGP type 2), unrelated to the eukaryotic UGP1 family
  [PMID:17322528 "the prokaryotic and eukaryotic forms of the enzyme are unrelated in
  amino acid sequence and structure"]. InterPro IPR005771, NCBIfam TIGR01099 galU,
  Pfam PF00483 NTP_transferase, PANTHER PTHR43197:SF1.
- Gene lies immediately downstream of hns, transcribed in the opposite direction
  [PMID:8169209 "The galU gene is located immediately downstream of the hns gene"].

## Molecular function

- Catalyses UTP + alpha-D-glucose 1-phosphate = UDP-alpha-D-glucose + PPi; sequential
  mechanism, Mg2+-requiring, inhibited by free UTP and PPi [PMID:7961613 "The
  recombinant enzyme overproduced in E. coli cells and purified to homogeneity catalyzed
  the synthesis and pyrophosphorolysis of UDP-glucose by a sequential mechanism. The
  enzyme required Mg2+ for maximal activity and was inhibited by free UTP and
  pyrophosphate."].
- In vitro substrate promiscuity: accepts several sugar 1-phosphates and dTTP
  [PMID:17322528 "The E. coli UGPase used in this investigation was active against the
  following sugar 1–phosphates: glucose, galactose, xylose, mannose, glucosamine,
  N -acetylglucosamine, fucose, and galactosamine"].
- Structure 1.9 A: homotetramer (dimer of dimers), fold like RmlA
  glucose-1-phosphate thymidylyltransferase [PMID:17322528 "The protein is a tetramer
  with 222 point group symmetry."]. Modelled active-site residues Gln109, Asp137, Glu201,
  Lys202; Mg2+ ligands not established.
- Oligomeric state from purification: tetramer [PMID:8169209 "The functional enzyme
  appears to be a tetramer of the galU gene product."]; UniProt: homotetramer or
  homopentamer.
- GalF (paralog in the O-antigen/colanic acid region) is catalytically inactive but
  interacts with GalU and modulates it (E. coli O7:K1) [PMID:8971705 "We propose that
  GalF is a non-catalytic subunit of the UDP-glucose pyrophosphorylase modulating the
  enzyme activity to increase the formation of UDP-glucose"].

## Biological roles (all via UDP-glucose supply)

- Sole route to UDP-glucose; galU mutants lack it (PMID:13979281, title only;
  [PMID:330527 "Mutants unable to synthesize UDP-glucose do not contain significant
  amounts of the membrane-derived oligosaccharides."]).
- Galactose: galU mutants are Gal-negative because GalT needs UDP-glucose
  [PMID:7961613 "complemented the galU mutation, which renders the bacterium unable to
  ferment galactose"].
- Membrane-derived oligosaccharides / OPG [PMID:1320618 "Another set of mutations mapped
  near 27 min closely linked to osmZ; these appear to be in the galU gene."].
- LPS core: galU Tn10 mutants are deep rough [PMID:10398745 "These adhesion mutants were
  found to exhibit a deep-rough phenotype"]. UPEC delta-galU loses O-antigen
  [PMID:26481693 "We were able to show a loss of the O-polysaccharide side chain of the
  ΔgalU mutant LPS."].
- Trehalose: galU mutants do not make trehalose and are osmosensitive
  [PMID:3131312 "GalU mutants, defective in synthesis of UDP-glucose, did not accumulate
  trehalose."].
- sigma S regulation: galU mutants have higher sigma S levels; UDP-glucose has been
  proposed as a signal [PMID:7814331 "we propose that the cellular content of UDP-glucose
  serves as an internal signal that controls expression of osmY and other sigma
  S-dependent genes"]. This is the likely origin of UniProt's "May play a role in
  stationary phase survival".
- Colanic acid (glucose-containing exopolysaccharide): IMP row from PMID:1320618; kept as
  non-core precursor supply.

## Location

- Cytosol (proteomics PMID:18304323, PMID:15911532, PMID:16858726).

## Review decisions summary

- GO:0003983 core MF accepted (IBA, IDA x2, IEA).
- GO:0006011 UDP-glucose metabolic process (IEA, IMP x2) -> MODIFY to GO:0120530
  UDP-alpha-D-glucose biosynthetic process (descendant). Note: the module
  `udp_glucose_and_udp_galactose_biosynthesis` currently uses GO:0006011 for the GalU
  step; GO:0120530 is the more specific descendant.
- Downstream consumer processes (LPS core, colanic acid, OPG, Leloir pathway) kept as
  non-core: GalU only supplies the UDP-glucose donor.
- Mg2+ binding: non-core cofactor. identical protein binding / protein-containing
  complex: non-core (homotetramer; no more specific GO term for a homotetramer).
