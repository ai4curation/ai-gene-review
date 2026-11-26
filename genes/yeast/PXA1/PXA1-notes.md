# PXA1 notes

Module: `peroxisomal_beta_oxidation` (substrate entry, abcd_transport_activity). PXA1/PXA2 are missing from YeastCyc YEAST-FAO-PWY.

## Evidence journal
- Long-chain activated FA import via Pat1p/Pat2p (PXA2/PXA1) [PMID:8670886 "long-chain fatty acids are imported from the cytosolic pool of activated long-chain fatty acids via Pat1p and Pat2p"].
- Heterodimer, coIP; not required for peroxisome assembly; Pxa1p unstable without Pxa2p [PMID:8876235 "Finally, we find that Pxa1p and Pxa2p coimmuno-precipitate."; "is associated with peroxisomes but not required for their assembly."].
- C18:1-CoA (not C8:0-CoA) import via Pxa2p, ATP-dependent [PMID:9395310 "we show that C18:1-CoA, but not C8:0-CoA, enters the peroxisome via Pxa2p, in an ATP-dependent fashion."].
- Spectrum of acyl-CoAs; human ABCD1 complements [PMID:18757502 "we show that the Pxa1p/Pxa2p heterodimer is involved in the transport of a spectrum of acyl-CoA esters."]; ABCD2 also complements [PMID:21145416].
- Mechanism: acyl-CoA hydrolysed by the complex, FA moiety translocated, re-esterified by Faa2p/Fat1p [PMID:22493507 "very long chain acyl-CoA esters are hydrolyzed by the Pxa1p-Pxa2p complex prior to the actual transport of their fatty acid moiety into the peroxisomes"].
- Pxa2p C-terminus required for Pxa1p interaction and function [PMID:25118695].
- Also mediates unidirectional ATP uptake into peroxisomes [PMID:35127709 "the ABC transporter protein complex Pxa1p/Pxa2p, which mediates both uni-directional acyl-CoA and ATP uptake"].

## Curation decisions
- Core MF GO:0005324 long-chain fatty acid transmembrane transporter activity (fits the hydrolysis-then-FA-translocation mechanism; GOA IBA/IGI), BP GO:0015910, CC GO:0005778, complex GO:0043190.
- The module uses GO:0015607 ABC-type fatty-acyl-CoA transporter activity (acyl-CoA on both sides); this conflicts with PMID:22493507 and is not in GOA. Raised as a suggested question.
- IBA peroxisome organization: REMOVE (contradicted by PMID:8876235).
- MYTH protein-binding hits (PMID:23831759): REMOVE; Pxa1-Pxa2 coIP protein binding -> MODIFY to GO:0046982.
- ATP transport (IDA) and fatty-acyl-CoA transport (IGI): non-core.
