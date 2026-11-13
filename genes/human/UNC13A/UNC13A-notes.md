# UNC13A (Munc13-1, Q9UPW8) review notes

## Conclusions

- Core activity: the MUN domain binds syntaxin-1 and catalyses its transition from the
  closed Munc18-1 complex into the SNARE complex [PMID:21499244 "the Munc13-1 MUN domain,
  which plays a central role in vesicle priming, markedly accelerates the transition from
  the syntaxin-1-Munc18-1 complex to the SNARE complex"]. This is synaptic vesicle priming
  [PMID:10440375 "glutamatergic hippocampal neurons from mice lacking Munc13-1 form
  ultrastructurally normal synapses whose synaptic-vesicle cycle is arrested at the
  maturation step"]. Added a NEW ISS row for GO:0035543 positive regulation of SNARE
  complex assembly, since Munc13-1 performs the step itself.
- Second core function: C1-domain DAG/phorbol ester receptor [PMID:9697857 "Munc13-1 is a
  presynaptic high-affinity phorbol ester and diacylglycerol receptor"]; Munc13s, not PKC,
  are the main presynaptic DAG receptors [PMID:11792326 "We show that Munc13s are the main
  presynaptic DAG/beta phorbol ester receptors in hippocampal neurons."].
- Ca2+, calmodulin and C2B phospholipid binding are regulatory inputs; kept non-core. The
  phospholipid binding IEA was refined to calcium-dependent phospholipid binding on the
  C2B evidence [PMID:20154707 "unique Ca(2+)-dependent phospholipid-binding properties that
  favor phosphatidylinositolphosphates"]. That paper carries a 2025 expression of concern,
  so it is used only for non-core rows. The UniProt DOMAIN note denying Ca2+-dependent
  phospholipid binding by the C2 domains is outdated for C2B.
- Locations: presynaptic active zone and presynaptic membrane accepted; plasma membrane
  accepted as well because Munc13-1 also acts at the beta-cell plasma membrane
  [PMID:12871971 "Here, we demonstrate the presence of Munc13-1 in human, rat, and mouse
  pancreatic islet beta cells."]. Synaptic vesicle membrane (IBA) marked over-annotated:
  Munc13-1 is an active-zone plasma-membrane protein whose C2C only contacts vesicles
  transiently.
- Chemical synaptic transmission and neurotransmitter secretion refined to synaptic vesicle
  priming (a part_of descendant of both); neuron projection refined to terminal bouton.
- Positive regulation of dendrite extension (IDA, PMID:23999003) marked over-annotated:
  melanocyte dendrites are outside GO dendrite (a neuron projection), and the finding comes
  from a C2-domain overexpression screen [PMID:23999003 "Sixteen sets of C2
  domain-containing proteins were identified whose over-expression resulted in dendrite
  lengthening."]. Full text not available; the result itself is not disputed.

## Open points

- Calmodulin-binding primary paper (Junge et al. 2004) not cached; rows rest on PAINT and
  UniProt by-similarity.
- PAINT seeds for the synaptic vesicle membrane node were not inspected.
