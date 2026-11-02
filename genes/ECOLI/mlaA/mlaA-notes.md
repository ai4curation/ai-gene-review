# mlaA (P76506) curation notes

## Deep research
- `just deep-research ECOLI mlaA --provider perplexity` was attempted on 2026-10-23 and failed:
  "Provider 'perplexity' not available. Available: falcon, openscientist". No deep-research
  file was generated; the review is based on cached primary literature and the UniProt record.

## Literature summary
- Founding Mla paper: mla mutants accumulate PL in the OM outer leaflet [PMID:19383799 "We have identified an ABC transport system in Escherichia coli with predicted import function that serves to prevent PL accumulation in the outer leaflet of the OM."]
- MlaA is an OM lipoprotein that binds OmpC and OmpF; porin binding alone targets unlipidated MlaA to the OM [PMID:26314242 "We show that the OM lipoprotein MlaA interacts specifically with OmpC and OmpF." ; "This interaction is sufficient to localize MlaA lacking its lipid anchor to the OM."]
- Structure: monomeric alpha-helical doughnut in the inner leaflet with an amphipathic pore; selectively removes outer-leaflet PLs; porins not active in transport [PMID:29038444 "MlaA represents a lipid transport protein that selectively removes outer leaflet phospholipids to help maintain the essential barrier function of the bacterial OM."]
- OmpC-MlaA architecture: MlaA entirely within the bilayer, hydrophilic channel, gating hairpin loop [PMID:29848551 "In addition, MlaA forms a hydrophilic channel, likely enabling PL translocation across the OM."]
- MlaA-MlaC transient complex (cryo-EM 2.9 Å, PDB 8I8R/8I8X): MlaC docks at the MlaA periplasmic base, juxtaposing channel and MlaC cavity; apo-MlaC binding opens MlaA channel [PMID:38092770 "in the first step, the OmpC-MlaA complex transfers PLs to the periplasmic chaperone MlaC"].
- mlaA* gain-of-function allele: PL flow into outer leaflet, LPS increase, vesiculation, death [PMID:26929379].
- Ekiert 2017 model: "Binding of MlaC to the lipid-bound MlaA-OmpC/OmpF complex results in lipid transfer to the hydrophobic pocket of MlaC" [PMID:28388411].
- Reconstitution with MlaA donor proteoliposomes, MlaC and MlaFEDB acceptor proteoliposomes [PMID:39080293 "transport from donor MlaA containing proteoliposomes to acceptor MlaFEDB proteoliposomes by the MlaC chaperone"].
- Direction: ATP drives retrograde (OM to IM) transport [PMID:34873038]; anterograde proposals [PMID:31235958] are disputed.

## Decisions
- Protein binding (3 IPI rows, OmpC/OmpF): REMOVE per protein-binding policy; interactions are real.
- Cell outer membrane IEA + RCA: ACCEPT. Membrane IEA: MODIFY -> cell outer membrane.
- GO:0120010 IBA + IDA: ACCEPT.
- Core MF: contributes_to GO:0120014 phospholipid transfer activity. GO:0120014 is defined as removing
  a PL from a membrane, carrying it through the aqueous phase in a hydrophobic pocket and delivering it.
  MlaA does the removal/hand-off step but not aqueous carriage (that is MlaC), so `enables` would overstate;
  `contributes_to` records MlaA as the OM half of the MlaA-MlaC transfer step. GO:0005543 phospholipid
  binding was not asserted: there is no direct binding measurement for MlaA (lipid interaction comes from
  MD and channel structure). No GO term exists for OM phospholipid extraction by a channel; raised as a
  suggested question. No NEW annotation rows added.
