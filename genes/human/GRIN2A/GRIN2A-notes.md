# GRIN2A (GluN2A / NR2A, Q12879) — review notes

## Provider / workflow situation
- Falcon and Perplexity deep-research providers are not configured in this environment. Deep research
  was generated with OpenScientist: `genes/human/GRIN2A/GRIN2A-deep-research-openscientist.md`
  (`just deep-research-openscientist human GRIN2A`). Treated as a lead; claims checked against the
  cached publications and UniProt before use.
- `just paint-losses human GRIN2A` reports no IRD/IKR loss on this gene's lineage.
- Reviewed as the GluN2A partner of the already-merged GRIN1 review (`genes/human/GRIN1/`); structure,
  tone and MODIFY patterns kept consistent with it.

## Core biology
- GluN2A is one of four GluN2 subunits of NMDA receptors. Receptors are heterotetramers of two GluN1 +
  two GluN2 (A–D) and/or GluN3. **GluN2 binds glutamate; GluN1 binds the co-agonist glycine/D-serine**
  [PMID:12805203 "NMDA receptors require both glycine and glutamate for activation with NR1 and NR2
  forming glycine and glutamate sites, respectively"]. Channel opening needs both ligands plus
  depolarisation to relieve Mg2+ block. The channel conducts Na+, K+ and Ca2+; Ca2+ entry drives
  plasticity.
- UniProt records experimental/structural L-glutamate binding residues on GluN2A (FT BINDING
  L-glutamate 511/513/518/689/690/731, ECO:0000269|PubMed:26875626 and PDB evidence), and a
  high-affinity N-terminal-domain Zn2+ site (44/128/266/282). Zinc is a GluN2A-selective allosteric
  inhibitor [PMID:27288002 "marked alterations in the sensitivity to zinc, a potent allosteric
  inhibitor of GluN1/GluN2A receptors"].
- Recombinant human GluN1/GluN2A channels have NMDA-receptor properties [PMID:8768735 cloning in
  oocytes]. Disease-variant studies establish the channel's gating/permeability: L812M gain-of-function
  [PMID:24504326 "the mutation enhances agonist potency, decreases sensitivity to negative modulators
  including magnesium, protons and zinc, prolongs the synaptic response time course and increases
  single-channel open probability"], M3/pre-M1 variants [PMID:36117210, PMID:38538865], trafficking and
  agonist potency [PMID:28242877], schizophrenia LoF vs epilepsy GoF [PMID:38307912].

## Key review decisions
- **Added NEW GO:0016595 glutamate binding (IDA)** — GRIN2A had no glutamate-binding annotation, yet it
  is the defining GluN2 molecular function. Supported by UniProt glutamate-binding residues and the
  FUNCTION statement.
- Channel MF cluster (GO:0004972 etc.): ACCEPT. Generic MF terms (ion channel, cation channel,
  ligand-gated channel, signaling receptor activity) MODIFY → GO:0004972; calcium channel activity
  MODIFY → GO:0022849 (verified descendant in QuickGO).
- GO:0005515 protein binding (IPI, many) → REMOVE per protein-binding policy; interactions (PSD-95/DLG
  PDZ scaffolds, nNOS, LRP1, etc.) are real but uninformative. Captured by the NMDA receptor complex term.
- ER (GO:0005783) and ER membrane (Reactome) rows → MARK_AS_OVER_ANNOTATED (assembly/transit, not
  residence; ER transit-not-residence rule).
- Amyloid-beta binding (GO:0001540, TAS PMID:26719327) → MARK_AS_OVER_ANNOTATED: the cited review states
  "no direct binding of AβO to NMDAR subunits has been reported." Negated cellular-response-to-Aβ
  (GO:1904646, IGI NOT PMID:21883149) → MARK_AS_OVER_ANNOTATED (narrow negative result), mirroring GRIN1.
- response to ethanol (GO:0045471, IDA PMID:18445116) → MARK_AS_OVER_ANNOTATED (drug effect on the
  channel, not participation in a response pathway).
- Zinc ion binding (GO:0008270, ISS) → KEEP_AS_NON_CORE (genuine but modulatory).
- Location refinements mirror GRIN1: synapse/synaptic membrane/postsynapse → postsynaptic membrane;
  neuron projection → dendrite + dendritic spine; membrane → plasma + postsynaptic membrane; synaptic
  vesicle → over-annotated; presynaptic membrane/cytoplasmic-vesicle membrane → non-core.

## Action totals
See the PR body. 146 annotation rows (145 GOA + 1 NEW glutamate binding).
