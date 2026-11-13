# CPLX1 (complexin-1, O14810) review notes

## Conclusions

- Core activity is binding to the assembled neuronal SNARE complex. Human complexin-1 was
  crystallised on a prefusion SNARE mimetic: "In the structure, hCPX binds one
  partially-zippered SNARE complex via its central helix (CPXcen, residues 48–75)"
  [PMID:21785412]. Complexins bind the core complex selectively: "Complexins bind weakly to
  syntaxin alone and not at all to synaptobrevin and SNAP-25, but strongly to the SNAP
  receptor-core complex composed of these three molecules" [PMID:7553862].
- Core process is regulation of synaptic vesicle fusion to the presynaptic active-zone
  membrane (GO:0031630). I kept the unsigned term because complexin both facilitates and
  clamps, and the balance depends on the preparation. Clamp: "Complexin prevents SNAREs from
  releasing neurotransmitters until an action potential arrives at the synapse"
  [PMID:21785414]. Facilitation (mouse double knockout, from the deep-research report):
  "a dramatically reduced transmitter release efficiency due to decreased Ca2+ sensitivity
  of the synaptic secretion process".
- Complex: GO:0070032 (syntaxin-1a/complexin I complex) accepted. The generic SNARE complex
  and protein-containing complex rows were changed to it with MODIFY (it is an is_a
  descendant of both, checked in QuickGO).
- The two IPI protein-binding rows (PMID:21785412, PMID:21785414) are changed to SNARE
  binding with MODIFY. The partners are the SNARE proteins.
- General terms were changed to specific ones the gene already carries: exocytosis,
  chemical synaptic transmission and neurotransmitter transport to GO:0016079 (it is a
  descendant of all three); regulation of exocytosis and modulation of chemical synaptic
  transmission to GO:0031630; synapse to presynapse.
- The postsynaptic rows (dendrite, postsynapse, regulation of exocytic insertion of
  neurotransmitter receptor) and the specific synapse-type rows (calyx of Held, Schaffer
  collateral-CA1, glutamatergic) are kept as non-core. They all come from rodent data.
  Insulin secretion and soma/perikaryon are also kept as non-core.
- GO:0070554 (syntaxin-3 complex) is UNDECIDED. Its sources are an ARBA row and a TAS citing
  the Sudhof review, whose cached abstract does not mention complexin, and the main neuronal
  partner is syntaxin-1.

## Open questions

- Whether complexin-1 is a true clamp at mammalian synapses is still contested.
- It is unexplained why loss of CPLX1 causes epilepsy (DEE63) in humans but ataxia in mice.
