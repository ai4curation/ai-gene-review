# GRIN1 (human, Q05586) review notes

## 2026-11-10: first review

### Deep research status

- `just deep-research-falcon human GRIN1 --fallback perplexity-lite` failed: neither the falcon nor the
  perplexity provider is configured in this environment ("Provider 'falcon' not available. Available:
  openscientist, claude_code").
- `just deep-research-openscientist human GRIN1` was run as a substitute and finished after the verdicts
  were drafted (`GRIN1-deep-research-openscientist.md`). It was read as a cross-check. It agrees with the
  review on every point compared and changed no verdict. It supplied one extra citation for the glutamate
  binding removal [PMID:12805203 "NMDA receptors require both glycine and glutamate for activation with NR1
  and NR2 forming glycine and glutamate sites, respectively"]. Its quote attributed to PMID:9089692 is not in
  that paper's abstract, so it was not used; its other citations were not checked.
- No provider deep-research file was written by hand.

### What the gene does

- Human NMDAR1 expressed in oocytes has the properties of the NMDA receptor [PMID:7679115 "Expression in
  Xenopus oocytes demonstrated that the single protein encoded by the cloned cDNA possesses the
  electrophysiological and pharmacological properties characteristic of the NMDA receptor, including Ca2+
  permeability, voltage-dependent Mg2+ block, and inhibition by selective antagonists such as Zn2+ and
  channel blockers"].
- Currents need glycine [PMID:7685113 "Oocytes injected with cRNA synthesized from the hNR1 cDNA express
  glutamate and NMDA-activated currents in the presence of glycine"].
- GluN1 carries the glycine site, GluN2 the glutamate site [UniProt Q05586 DOMAIN, "The ligand-binding
  domain (LBD) binds to glycine (GluN1 and GluN3 subunits) and glutamate (GluN2 subunits) and control
  opening of the channel gate"].
- Receptors are heterotetramers [PMID:36309015 "NMDARs are glycine- and glutamate-gated ion channels that
  exist as heterotetramers composed of obligatory GluN1 and GluN2(A-D) and/or GluN3(A-B)"].
- With GluN3, GluN1 forms glycine-gated channels [PMID:38598639 "Uniquely, NMDARs composed of GluN1 and
  GluN3 are activated exclusively by glycine"; PMID:11823786 "NR3A or NR3B co-assembles with NR1 to form
  excitatory glycine receptors that are unaffected by glutamate or NMDA"].
- GluN1 is needed for GluN2 ER exit and depends on GluN2 for synaptic accumulation [PMID:15317856
  "GluRepsilon/NR2 subunits strictly require the GluRzeta1/NR1 subunit to exit from endoplasmic reticulum
  (ER) to the cell surface in vitro and to the postsynapse in vivo"; "the GluRzeta1 subunit, by itself, is
  virtually unable to accumulate at postsynaptic sites, regardless of C-terminal forms"].
- CA1-specific deletion in mouse removes NMDA currents, LTP and spatial memory [PMID:8980238 "Adult mice
  lack NMDA receptor-mediated synaptic currents and long-term potentiation in the CA1 synapses and exhibit
  impaired spatial memory but unimpaired nonspatial learning"].

### Decisions worth a second look

1. **glutamate binding (GO:0016595, IDA, PMID:7685113): REMOVE.** The only cached text is the abstract,
   which reports currents, not binding. PMID:12805203, the UniProt DOMAIN comment (evidence ECO:0000269) and the structural
   literature place glutamate on GluN2 and glycine on GluN1. This is a removal of an experimental row on the
   ground that the function is contradicted, not on the ground that the abstract is about another gene. If
   the full text contains a binding assay on hNR1 alone, revisit.
2. **propylene metabolic process (GO:0018964, ISS from mouse P35438): REMOVE, with a source defect** for
   ARUK-UCL/BHF-UCL. The mouse IDA cites PMID:21795692 (Shank3 and mGluR5); the full text does not contain
   the word propylene.
3. **NOT cellular response to amyloid-beta (IGI, PMID:21883149): MARK_AS_OVER_ANNOTATED.** The negative
   result is real [PMID:21883149 "Also globulomer Aβ had no effect on glutamate-induced NMDA currents"] but
   comes from one oligomer preparation on recombinant receptors in oocytes.
4. **amyloid-beta binding (ISS from rat): MARK_AS_OVER_ANNOTATED** [PMID:17308309 "ADDLs bind to or in close
   proximity to NMDA-Rs, triggering neuronal damage through NMDA-R-dependent calcium flux"].
5. **calcium ion binding (ISS from mouse): UNDECIDED.** Donor PMID:15663482 is abstract-only and shows a
   Ca2+/calmodulin dependence, not Ca2+ binding by NR1.
6. **"regulation of" terms changed to the process itself** (GO:2000463 to GO:0060079, GO:1904062 to
   GO:0098655, GO:0010524 to GO:0097553): the channel carries the current or flux, it does not regulate it.
7. **General terms changed to specific descendants already on the gene** (relationships checked in
   QuickGO on 2026-11-10): ligand-gated/monoatomic ion channel activity, signaling receptor activity and
   transmitter-gated channel activity to NMDA glutamate receptor activity and/or glycine-gated cation
   channel activity; calcium channel activity to glutamate-gated calcium ion channel activity; membrane,
   synapse, synaptic membrane to plasma/postsynaptic membrane; neuron projection to dendrite and dendritic
   spine; chemical synaptic transmission to excitatory chemical synaptic transmission; ion and cation
   transport to monoatomic cation transmembrane transport.
8. **ER membrane (Reactome TAS x4): KEEP_AS_NON_CORE.** Kept because subunit assembly in the ER is a
   required step and GluN2 cannot leave the ER without GluN1; not core because the channel does not act
   there (projects/ORGANELLES.md rule 7).
9. **synaptic vesicle (ISS from mouse): MARK_AS_OVER_ANNOTATED.** Donor PMID:10846156 describes KIF17
   transport vesicles in dendrites.
10. **protein binding (4 IPI rows): REMOVE** under the protein-binding policy. Partners GRIN2B and GRIN3A
    are covered by the complex term; APP and FUS are yeast two-hybrid hits.

### Things not done

- No NEW annotations were proposed. Candidates considered and left out: D-serine binding (not checked
  against a cached primary paper), long-term synaptic potentiation (covered by the accepted plasticity
  terms).
- PAINT losses: `just paint-losses human GRIN1` reports no IRD or IKR on the lineage.
- GO-CAM models containing GRIN1 (gocams/index.tsv: 6690711d00000596, 66c7d41500000672,
  66c7d41500001120, 66c7d41500001953, 66c7d41500003371, 66c7d41500003458, 66e382fb00000049) use
  NMDA glutamate receptor activity or glycine-gated cation channel activity with cation transmembrane
  transport at the postsynaptic membrane, which matches the core functions here. They were not reviewed.
- Several early papers are cached as abstracts only (PMID:7679115, 7681588, 7685113, 9489750, 21376300),
  so their rows were accepted on the abstract plus the curator's reading.
