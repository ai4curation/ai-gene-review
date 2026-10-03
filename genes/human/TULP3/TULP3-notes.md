# TULP3 (O75386) curation notes

## Deep research status
DR_STATUS_PLACEHOLDER

## Summary of function
- TULP3 binds IFT-A, which directs TULP3 into cilia [PMID:20889716 "We find that specific Tubby family proteins, notably Tubby-like protein 3 (TULP3), bind to the IFT-A complex."; "the IFT-A complex has a second role directing ciliary entry of TULP3"]; both IFT-A binding and phosphoinositide binding are needed for ciliary GPCR localization [PMID:20889716 "Both IFT-A and membrane phosphoinositide-binding properties of TULP3 are required for ciliary GPCR localization."].
- General adaptor for integral membrane cargo [PMID:28154160 "the tubby family protein TULP3 functions as a general adapter for ciliary trafficking of structurally diverse integral membrane cargo"], three-step model: PI(4,5)P2-dependent capture, IFT-A delivery, release into PI(4,5)P2-deficient ciliary membrane.
- Structure: TULP3 N-terminus binds IFT-A [PMID:36775821 "TULP3, the cargo adapter, interacts with IFT-A through its N-terminal region, and interface mutations disrupt cargo transport."].
- Negative regulator of Hh in neural tube [PMID:20889716 "TULP3 and IFT-A proteins both negatively regulate Hedgehog signaling in the mouse embryo"].
- Tubby domain binds PI(4,5)P2; Gq/PLC releases tubby/TULP3 to nucleus [PMID:11375483 "The localization of tubby-like protein 3 (TULP3) is similarly regulated."].
- Reads ciliary phosphoinositides set by INPP5E [PMID:26305592 "Tulp3 reads out ciliary phosphoinositides to control ciliary protein localization, enabling Hh signaling."].
- Other reported roles (mouse, UniProt by similarity): lithocholic acid binding, SIRT1 activation, AMPK/TORC1 regulation; human TULP3-SIRT1 co-IP (PMID:35397207). Treated as non-core.

## Key decisions
- 24 protein binding rows (interactome screens, SIRT1) REMOVE.
- Core MF: protein-macromolecule adaptor activity (GO:0030674), PI(4,5)P2 binding (GO:0005546), IFT-A binding (GO:0120160).
- protein-containing complex binding MODIFY -> GO:0120160.
- intraciliary anterograde transport: KEEP_AS_NON_CORE (cargo adaptor riding IFT, not IFT machinery).
- Transcription regulation and GPCR signalling pathway NAS: MARK_AS_OVER_ANNOTATED.

## HPA cilium atlas vs module role
- Module (stage 5): "IFT-A membrane cargo adaptor", process protein localization to cilium (GO:0061512).
- HPA v25: Primary cilium (Supported), Primary cilium transition zone (Supported), Basal body (Uncertain); main locations Nucleoplasm; Primary cilium. GOA HPA rows: cilium, ciliary transition zone, plasma membrane, nucleoplasm, nucleolus.
- Interpretation: strong agreement. The cilium and transition-zone calls match entry of TULP3 with IFT-A through the ciliary base; the plasma membrane call matches the PI(4,5)P2-dependent cargo-capture step; the nucleoplasm call matches PLC-induced nuclear translocation. core_functions agree with the module role (adaptor activity; protein localization to non-motile cilium, a child of GO:0061512).
