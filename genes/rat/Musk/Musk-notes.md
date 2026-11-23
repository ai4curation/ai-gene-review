# Musk (rat) review notes

## 2026-10-28 session

- Fetched with `just fetch-gene rat Musk`; UniProt Q62838 (MUSK_RAT, Swiss-Prot, RGD:3211, GeneID 81725). 58 GOA rows.
- No deep-research provider; manual synthesis in `Musk-deep-research-manual.md`.
- Key paper PMID:21419809 (Woller et al. 2011, Rinl) read in full: identifies Rinl as a MuSK
  kinase-domain binder by Y2H with the rat MuSK cytoplasmic domain (aa 517-868) [PMID:21419809 "The MuSK cytoplasmic domain (Rattus norvegicus, aa 517–868) was subcloned into the modified pBTM116 vector"];
  binding independent of MuSK phosphorylation; authors state they could not connect Rinl to MuSK function
  [PMID:21419809 "However so far, we have not been able to correlate Rinl action and MuSK function."].
  No GOA row derives from it; it adds no MF beyond protein binding, so no NEW row.
- Full text available: 14749715, 17011580, 20603078, 21419809, 22309736, 22253844. Abstract-only: 12220490,
  15604144, 16818610, 16870737, 16899069, 18420419, 7546737, 9698449, 18848351.

### Decisions
- Core MF = transmembrane receptor protein tyrosine kinase activity (GO:0004714); generic kinase /
  PTK rows MODIFY to it.
- Core BP: cell surface RTK signaling pathway, skeletal muscle AChR clustering, NMJ development,
  positive regulation of synaptic assembly at NMJ. Receptor clustering and regulation of synaptic
  assembly rows MODIFY to their specific children.
- CC: plasma membrane ACCEPT (also extrajunctional/aneural myotube surface); postsynaptic membrane and NMJ
  ACCEPT; membrane and synapse MODIFY.
- Expression-only rows (retina, cochlea development) MARK_AS_OVER_ANNOTATED; injury/activity
  response IEPs kept non-core. Brain (memory, LTP, cholinergic transmission) kept non-core.
- Neuron apoptosis ISO: muscle protein acting non-cell-autonomously via retrograde signalling;
  over-annotated.
- No NEW rows.
