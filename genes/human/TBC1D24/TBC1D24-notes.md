# TBC1D24 notes

## Domain architecture and the GAP question

- TBC domain (47-262) plus TLDc domain (343-554). The TBC domain is atypical: TBC1D24 "is an
  unconventional TBC/RABGAP because it lacks the "arginine finger" in the TBC domain"
  [PMID:32004315 "TBC1D24 is an unconventional TBC/RABGAP because it lacks the "arginine finger" in the TBC domain"].
- GOA carries no GTPase activator activity row, so the GAP question only affects core
  functions. Rab35 GAP activity was inferred genetically for the fly ortholog Skywalker
  [PMID:21458671 "chiefly by controlling Rab35 GTPase activity"]; no purified-protein GAP
  assay exists for the human protein. I did not assert any GAP activity.
- The best-supported molecular activity of the TBC domain is phosphoinositide binding through
  a conserved cationic pocket [PMID:27669036 "this pocket binds phosphoinositides phosphorylated at the 4 and 5 positions"],
  added as NEW `GO:0005546` (ISS, fly structural data).

## ARF6

- Coimmunoprecipitation with ARF6 [PMID:20727515 "By coimmunoprecipitation assay we found that TBC1D24 binds ARF6"].
  The protein binding IPI row was modified to small GTPase binding (`GO:0031267`).
- Postsynaptic spine maintenance by ARF6 inhibition
  [PMID:32004315 "TBC1D24 is present at the postsynaptic sites of excitatory synapses, where it is required for the maintenance of dendritic spines through inhibition of the small GTPase ARF6"].
- The reduced mEPSC frequency after knockdown is attributed to fewer synapses, so the IEA
  "positive regulation of excitatory postsynaptic potential" was marked over-annotated
  [PMID:32004315 "the reduced mEPSC frequency of the GFP-positive postsynaptic neuron was likely resulted from cell-autonomous decrease in synapse number on the postsynaptic neuron"].

## Presynaptic trafficking

- Mouse: [PMID:30335140 "genetic disruption of Tbc1d24 expression in the mouse leads to an impairment of endocytosis and an enlarged endosomal compartment in neurons"].
  Together with the fly data this supports a NEW ISS row for regulation of synaptic vesicle
  recycling (`GO:1903421`).

## TLDc, oxidative stress and V-ATPase

- Null N2a cells are arsenite-sensitive [PMID:30335140 "these cells were not only viable, but they also demonstrated reduced survival under oxidative stress"];
  kept as non-core.
- V-ATPase direction conflicts: in vitro inhibition by disassembly [PMID:38593795 "TLDC2, TBC1D24, and the TLDc domains of OXR1 and NCOA7 inhibit V-ATPase by inducing enzyme disassembly"]
  versus positive regulation in knockout neurons [PMID:39758816 "we demonstrate that TBC1D24 is a positive regulator of v-ATPase activity in neurons"].
  No GOA row covers it; left as a suggested question.

## Other calls

- NOT regulation of cilium assembly (Yoshimura screen) accepted
  [PMID:17646400 "However, other human Rabs and GAPs are not."].
- Neuromuscular junction ISS (from fly NMJ) marked over-annotated: the fly NMJ was the model
  synapse; no vertebrate NMJ evidence.
