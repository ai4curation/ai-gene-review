# murB (P08373) – E. coli K-12 – curation notes

No deep-research file was generated for this gene; these notes come from the cached
publications, the UniProt record and a targeted full-text check of PMID:16436710.

## Identity

- murB (b3972) encodes UDP-N-acetylenolpyruvoylglucosamine reductase (UDP-N-acetylmuramate
  dehydrogenase, EC 1.3.1.98), 342 aa, monomeric flavoenzyme, MurB family (HAMAP MF_00037,
  TIGR00179, PANTHER PTHR21071:SF4), PCMH-type FAD-binding domain (residues 13-183).
- Cloned by complementation of the murB mutant ST5 [PMID:1311302 "The murB gene, which complemented the UDP-N-acetylenolpyruvoylglucosamine reductase (EC 1.1.1.158) mutation in Escherichia coli ST5, was cloned from an E. coli chromosomal library."].

## Reaction, cofactor and mechanism

- Purified enzyme is a monomer with stoichiometric bound FAD reduced in turnover; uses the
  4-pro-S hydride of NADPH to reduce UDP-GlcNAc-enolpyruvate to UDP-MurNAc
  [PMID:8448160 "It was found to be a monomer and to contain stoichiometric amounts of bound FAD which is reducible in catalytic turnover."; "The enzyme utilizes the 4-pro-S hydrogen of NADPH to reduce the enolpyruvyl group of UDP-N-acetylglucosamine enolpyruvate to the lactyl ether in UDP-N-acetylmuramic acid."].
- Ping-pong bi-bi kinetics; NADPH (not NADH) is the reductant; K+/NH4+ activation; NADPH and
  UNAGEP share a subsite [PMID:7727397 "Initial velocity measurements as a function of both substrates produced patterns consistent with a ping pong bi bi double competitive substrate inhibition mechanism."; "Alternate reduced nicotinamide dinucleotides, including NHXDPH, 3'-NADPH, and alpha-NADPH, were substrates, whereas NADH was not."; "The data suggest that NADPH and UNAGEP share a subsite that prevents both molecules from binding at once."].
- NMR confirms NADP+ and UNAGEP use the same pocket [PMID:9150408 "The NMR data indicate that NADP+ and UNAGEP utilize the same binding pocket"].
- Ser229 is the proton donor in the second half-reaction; S229A is ~10^7-fold defective
  [PMID:9020778 "The single point mutation of residue 229 from serine to alanine eliminated a hydroxyl group which has previously been proposed to play a critical role as a proton donor during the second half-reaction of MurB"].
- Substrate-induced closure of domain 3; Tyr190 contacts the alpha-phosphate
  [PMID:8805513 "Tyr190 swings over the channel opening and establishes a hydrogen bond with an oxygen of the alpha-phosphate of the sugar nucleotide substrate which is critical to substrate binding."].
- Second committed step; sequential with MurA [PMID:9020778 "MurB catalyzes the second committed step in the synthesis of peptidoglycan, a key component of the bacterial cell wall."]; [PMID:8805513 "sequential enol ether transfer and reduction steps catalyzed by MurA and MurB respectively"].

## PMID:16436710 (source of the IMP/IDA rows)

- Inhibitor paper: 3,5-dioxopyrazolidines inhibit E. coli MurB (IC50 4-7 uM), crystal
  structure of E. coli MurB with compound 4 bound to the FAD-containing active site
  [PMID:16436710 "The crystal structure indicated the binding of a compound at the active site of MurB and specific interactions with active-site residues and the bound flavin adenine dinucleotide cofactor."].
- Peptidoglycan synthesis inhibition was measured in Staphylococcus epidermidis, not E. coli
  [PMID:16436710 "Peptidoglycan biosynthesis studies using a strain of Staphylococcus epidermidis revealed reduced peptidoglycan biosynthesis upon incubation with 3,5-dioxopyrazolidines"].
- Full text (PMC1366903, read via web; not in cache) reportedly states the compounds had no
  activity against E. coli whole cells and reports no cell-shape or localization experiment.
  So the IMP rows (peptidoglycan biosynthesis, cell wall organization, regulation of cell shape)
  and the IDA cytoplasm row from this paper are weakly grounded for E. coli MurB. Under the
  repo rule (do not REMOVE experimental rows on incomplete cached evidence) the true terms are
  accepted/kept on independent evidence and the cell-shape row is marked over-annotated.

## Location

- Soluble cytosolic enzyme (no TM segments); cytosol proteomics [PMID:18304323].

## Annotation decisions (summary)

- GO:0008762 (all rows): ACCEPT – core MF.
- GO:0009252: ACCEPT (IEA, IMP).
- GO:0071949 FAD binding: KEEP_AS_NON_CORE (cofactor binding, ancillary to catalysis);
  GO:0050660 flavin adenine dinucleotide binding: MODIFY -> GO:0071949.
- GO:0005829 cytosol: ACCEPT; GO:0005737 cytoplasm: MODIFY -> cytosol.
- GO:0071555 cell wall organization: KEEP_AS_NON_CORE (downstream consequence; the direct
  process is GO:0009252). Consistent with PSEPK murB review.
- GO:0008360 regulation of cell shape: MARK_AS_OVER_ANNOTATED (MurB is not a regulator of
  shape; precursor enzymes affect shape only indirectly; consistent with PSEPK Mur reviews).
- UniProt keyword "Cell division" has no GOA row for murB; not proposed.
