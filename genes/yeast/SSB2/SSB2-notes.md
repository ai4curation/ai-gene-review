# SSB2 review notes

## 2026-08-12 re-review

- Identity verified as *Saccharomyces cerevisiae* SSB2/YNL209W, UniProt P40150,
  the canonical ribosome-associated Ssb-type Hsp70 paralog of SSB1/P11484.
- Ssb2 directly binds nascent chains at the cytosolic 60S tunnel exit. RAC's
  Zuo1 J-domain stimulates Ssb ATP hydrolysis, driving the NBD/SBD cycle used for
  ATP-dependent cotranslational folding. [PMID:9670014 "Ssb to function as a
  chaperone on the ribosome, preventing the misfolding of"]
- GO:0044183 is modified to the more specific GO:0140662, consistent with the
  existing unfolded-protein-binding annotations and SSB1 project decision.
- ATP binding and hydrolysis are genuine core biochemical activities. Broad
  nucleotide-binding and hydrolase parents are over-annotated, while protein
  refolding is retained only as a plausible non-core general Hsp70 capability.
  [PMID:9860955 "Here we report that the ATPase activities of these two classes
  of Hsp70s exhibit different kinetic properties."]
- Plasma-membrane localization is unsupported for this soluble cytosolic Hsp70;
  the IBA transfer is audited against its PANTHER family node. Cytoplasm is true
  but less specific than the core cytosolic ribosome localization.
- The consolidated core function combines GO:0140662 with de novo
  cotranslational folding and cytosolic localization. Translational fidelity,
  frameshifting, and glucose-starvation responses remain supported annotations
  but are not modeled as processes directly carried out by the chaperone MF;
  PMID:15456889 describes fidelity as extending beyond the nascent-chain
  chaperone role.
- Roughly half of cellular Ssb is ribosome-associated, but this is dynamic rather
  than stable complex membership, so the core function uses cytosol as location
  and describes the 60S tunnel-exit position in prose instead of `in_complex`.
