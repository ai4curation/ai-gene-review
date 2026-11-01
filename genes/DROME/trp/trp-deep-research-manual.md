# trp (Drosophila melanogaster, UniProt P19334) - manual literature synthesis

No deep-research API was available for this review; this synthesis was compiled
by hand from the cached publications in `publications/` and PubMed metadata.

## Identity

- `trp` (transient receptor potential; FlyBase FBgn0003861; GeneID 43542) encodes a
  1275-aa multipass membrane protein, the founding member of the TRP channel
  superfamily (TRPC subfamily). UniProt: "Belongs to the transient receptor (TC
  1.A.4) family. STrpC subfamily."
- Domain architecture: N-terminal ankyrin repeats, six transmembrane helices with a
  pore loop (Ion_trans, PF00520), the TRP domain (PF08344) and a long, largely
  disordered cytoplasmic C-terminus ending in the INAD-binding PDZ ligand.

## Channel activity

- trp mutants lose the Ca2+-permeable, La3+-sensitive component of the light-induced
  current [PMID:1314617 "We conclude that the recently sequenced trp protein
  represents a class of light-sensitive channel required for inositide-mediated Ca2+
  entry"].
- The light-activated conductance is formed by TRP plus TRPL [PMID:8646774 "We
  demonstrate that the light-activated conductance is composed of TRP and TRPL ion
  channels and that each can be activated on its own."].
- Pore-forming subunit, Asp621 selectivity filter [PMID:17234592 "provide the first
  rigorous demonstration that a TRP protein is a pore-forming subunit in any native
  system"].
- Gating: PLC-dependent; PUFAs activate native TRP/TRPL [PMID:9930700]; metabolic
  stress/anoxia opens TRP and TRPL [PMID:10908615 "Genetic elimination of both TRP and
  TRPL channels prevented the effects of anoxia, mitochondrial uncouplers, and
  depletion of ATP"]. Store-operated behaviour was seen in heterologous expression
  [PMID:9215637 "In vitro studies indicate that TRP is a SOC"], but in the rhabdomere
  gating is "independent of internal membrane systems, which are absent in the
  microvilli" [PMID:22952921]. In photoreceptor axon terminals TRP/TRPL appear to
  provide store-operated Ca2+ entry that supports exocytosis [PMID:22952921].

## Assembly

- TRP-TRPL interact directly in vitro [PMID:9215637], but in vivo "TRP and TRPL
  assemble exclusively as homomultimeric channels in their native environment"
  [PMID:23687378].
- Auxiliary single-TM subunits INAF-B (and INAF-C in R7) are reciprocally required
  for TRP stability [PMID:17968007; PMID:32434796].

## Signalplex anchoring

- The TRP C-terminus binds INAD PDZ3 [PMID:8630257; PMID:26853938 "The C-terminal 15
  residues of TRP are required for the specific interaction with INAD PDZ3."].
- TRP and INAD form the core unit that retains the signalplex (NORPA, INAC/eye-PKC) in
  the rhabdomere [PMID:10995445; PMID:9010208]. Channel and anchoring functions are
  separable [PMID:16301334 "Drosophila transient receptor potential (TRP) serves dual
  roles as a cation channel and as a molecular anchor for the PDZ protein, INAD"].

## Location

- Rhabdomere membranes [PMID:2516726], base of microvilli [PMID:7751943], rhabdomere
  microvillus membrane [PMID:8646774]; also photoreceptor axons/terminals in the
  lamina [PMID:22952921 "Immunohistochemical images revealed considerable expression in
  photoreceptors axons at the lamina."].

## Regulation

- Eye-PKC phosphorylates TRP Ser982 for fast deactivation [PMID:16914683]; light-dependent
  dephosphorylation at S936 tunes frequency response [PMID:28314815].

## Phenotypes (indirect)

- Loss of channel function causes light-dependent retinal degeneration [PMID:16301334];
  constitutively active TrpP365 causes Ca2+-overload degeneration with mitochondrial
  damage [PMID:10632594; PMID:27054334].
- trp mutants defective in olfactory adaptation [PMID:10366618]; hearing screen
  implicated phototransducer components [PMID:22939627, abstract only].
