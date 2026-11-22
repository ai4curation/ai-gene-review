# trpl (Drosophila melanogaster, UniProt P48994) - manual literature synthesis

No deep-research API was available; this synthesis was assembled manually from the cached
publications in `publications/` and the UniProt record. Full text was read for
PMID:22952921, PMID:23687378, PMID:24013593, PMID:15695363 and PMID:10908615; the other
papers are abstract-only in the cache.

## Identity and domain architecture
- 1124 aa TRPC-family (STrpC subfamily) channel subunit: N-terminal ankyrin repeats, six
  transmembrane helices (341-666), TRP domain, two C-terminal calmodulin-binding sites
  (UniProt P48994).
- Cloned as a calmodulin-binding protein homologous to trp [PMID:1314616 "We propose the name transient receptor potential-like (trpl) to describe this newly isolated gene."].

## Channel activity
- TRPL alone is a constitutively active cation channel; TRPL-TRPgamma heteromers are
  PLC-regulated [PMID:10896160 "While TRPL and TRPgamma homomultimers are constitutively active, we demonstrate that TRPL-TRPgamma heteromultimers form a regulated phospholipase C- (PLC-) stimulated channel."].
- Ca2+-permeable [PMID:11514552 "Transient receptor potential and transient receptor potential-like (TRPL) are Ca(2+)-permeable cation channels found in Drosophila photoreceptor cells"]; PCa:PNa about 4:1 versus about 100:1 for TRP (cited in PMID:22952921).
- TRP-TRPL co-expression gives a store-operated current in vitro [PMID:9215637 "coexpression of TRP and TRPL leads to a store-operated, outwardly rectifying current distinct from that owing to either TRP or TRPL alone"], but in vivo TRP and TRPL are separate homomultimers [PMID:23687378 "We found that TRP and TRPL assemble exclusively as homomultimeric channels in their native environment."].

## Phototransduction
- The light-activated conductance is TRP plus TRPL [PMID:8646774 "We demonstrate that the light-activated conductance is composed of TRP and TRPL ion channels and that each can be activated on its own."].
- Located in rhabdomere microvillar membranes [PMID:8646774 "We now show that TRP and TRPL localize to the membrane of the transducing organelle, together with rhodopsin and PLC"].
- Light-regulated translocation to the cell body tunes sensitivity [PMID:11931743 "TRPL, is translocated back and forth between the signaling membrane and an intracellular compartment by a light-regulated mechanism"].
- Metabolic stress (anoxia, uncouplers, ATP depletion) opens TRP/TRPL [PMID:10908615 "Genetic elimination of both TRP and TRPL channels prevented the effects of anoxia, mitochondrial uncouplers, and depletion of ATP"].

## Regulation
- Calmodulin binding sites CBS-1/CBS-2 [PMID:8670063 "we now show that two calmodulin-binding sites are present in the C-terminal domain of the Trpl protein, CBS-1 and CBS-2"; PMID:10371201].
- FKBP59 binds the 701-LPPPFNVLP-709 motif and inhibits TRPL [PMID:11514552 "Expression of dFKBP59 produced an inhibition of Ca(2+) influx via TRPL in fura-2 assays."].
- In oocytes, TRPL is modulated by CaM, PKC, InsP3 and G proteins [PMID:9494079].

## Roles outside phototransduction
- Taste: camphor-activated channel in bitter GRN dendrites; downregulated by Ube3a after chronic camphor feeding [PMID:24013593 "The transient receptor potential-like (TRPL) cation channel was a direct target for camphor in gustatory receptor neurons"].
- Malpighian tubule: required for CAP2b-stimulated Ca2+ signalling and fluid secretion [PMID:15695363 "Thus, in an epithelial context, TRPL is sufficient for wild-type responses."].
- Photoreceptor axons: TRPL present in lamina/medulla terminals; trpl;trp double mutants lose depletion-induced Ca2+ entry and exocytosis, while single mutants are normal [PMID:22952921 "In TRP (trp) and TRPL (trpl) single mutants the level of exocytosis induced by depolarization was comparable to wt flies"].
- Hearing: reported in a Johnston's organ screen [PMID:22939627], abstract only.
