# TULP3 (O75386) curation notes

## Deep research status
`just deep-research-falcon human TULP3` first failed (falcon timed out at 600 s; perplexity-lite fallback unavailable in this environment). Re-run with `--timeout 2400` succeeded: see TULP3-deep-research-falcon.md.

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

## Additional points from deep research (falcon)
- TULP3 is an associated IFT-A adaptor, not an obligate IFT-A subunit [deep research: "depleting TULP3 did not itself dismantle IFT-A or IFT-B localization, supporting its classification as an associated adaptor rather than an obligate structural IFT-A subunit."]; IFT-A interface residues ~23-68 (K41, K42, R43, F47, V49) from human TULP3-IFT-A cryo-EM (PDB 8FH3).
- TULP3 also delivers lipidated ARL13B (tubby domain recognizes the ARL13B amphipathic helix; Palicharla et al. 2023, not cached), placing TULP3 upstream of ARL13B -> ARL3 -> UNC119B/PDE6D cargo release (NPHP3, CYS1, INPP5E). This links TULP3 to the other stage-5 members of the module.
- A 2025 study implicates a tubby-domain beta-barrel surface distinct from the PIP2 site in cargo recognition; patient variants R382W/R408H impair cargo trafficking.
- Human disease: biallelic TULP3 variants cause progressive liver, kidney and heart fibrosis (Devane et al. 2022, PMID:35397207, cached).
