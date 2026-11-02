# ARL3 (P36405) research notes

ADP-ribosylation factor-like protein 3, human. Small Arf-family GTPase; cargo-release factor for lipidated ciliary proteins.

## Deep research status
The first falcon run timed out at the 600 s default (the perplexity-lite fallback is unavailable). The rerun with --timeout 2400 was reported as timed out, but the falcon job eventually completed and wrote `ARL3-deep-research-falcon.md` at 22:29, after the initial review. I then read it and checked it against the review. It changes no actions:
- It supports the switch/release-factor framing (G protein activity rather than GTPase activity as the core MF): ["The best-supported functional annotation remains: **a GTP-dependent, spatially regulated allosteric release factor** ... with ARL13B/BART-dependent activation and RP2-dependent termination"] and ["ARL3-GTP binds these carriers allosterically and promotes cargo release at the cilium; it is neither the lipid-modifying enzyme nor the cargo’s membrane transporter."]
- It supports removing the NOT cilium row: ["ARL3 is a soluble, cilia-associated protein that can occur in the cell body as well as the ciliary compartment."]
- It supports marking small GTPase-mediated signal transduction as over-annotated: ["Ciliary signaling is chiefly a consequence of cargo composition, not a demonstrated direct receptor pathway for ARL3."]
- Correction: early retina-wide Arl3 deletion in mouse prevents connecting cilium and outer segment formation (Hanke-Gogokhia 2016, via the deep research). The cilium assembly reasons were reworded, since cilia are not universally independent of ARL3; both rows stay KEEP_AS_NON_CORE.
- New items not annotated: BART/ARL2BP acts as a co-GEF with ARL13B (ElMaghloob 2021). ARL3-GTP displaces DNAAF9/Shulin from outer dynein arms (2024 preprint, 2025 NSMB). Neither is cached here, so no new annotations were made.

## Summary of function
- Nucleotide binding with unusual biochemistry. [PMID:8034651 "Purified recombinant human Arl3 was shown to bind guanine nucleotides but lacks ARF activity and intrinsic or ARF GTPase-activating protein-stimulated GTPase activity."]
- GAP is RP2. [PMID:18588884 "Recently, we could identify RP2, responsible for a variant of X-linked retinitis pigmentosa, as the Arl3-specific GAP."; PMID:11847227 "Finally, we find that RP2 interacts with GTP-bound ADP ribosylation factor-like 3 protein"]
- GEF is ARL13B; Joubert variants at Arg149. [PMID:30269812 "Both missense variants replace the highly conserved Arg149 residue, which we show to be necessary for the interaction with its guanine nucleotide exchange factor ARL13B, such that the mutant protein is associated with reduced INPP5E and NPHP3 localization in cilia."]
- Cargo release: [PMID:22085962 "Furthermore, we found that binding of ARL3-GTP serves to release myristoylated cargo from UNC119."; "Our results uncover a selective, membrane targeting GTPase cycle that delivers myristoylated proteins to the ciliary membrane"]; [PMID:26455799 "The ciliary protein Arl3 has been shown to act as a specific release factor for myristoylated and farnesylated ciliary cargo molecules by binding to the effectors Unc119 and PDE6δ."]; [PMID:22002721 "We demonstrate that the G proteins Arl2 and Arl3 act in a GTP-dependent manner as allosteric release factors for farnesylated cargo."]
- Other locations and roles: centrosomes, spindles, midbodies, cilia, Golgi, nucleoplasm. Knockdown causes cytokinesis failure. [PMID:16525022 "Knockdown of Arl3 by siRNA resulted in changes in cell morphology, increased acetylation of α-tubulin, failure of cytokinesis, and increased number of binucleated cells."] Photoreceptor connecting cilium [PMID:12417528 "In contrast, cofactor C and Arl3 localized predominantly to the photoreceptor connecting cilium in rod and cone photoreceptors."]

## Key curation decisions
- Core MF: G protein activity (GO:0003925), which covers small GTPase switches. GTPase activity (IEA) is accepted but is RP2-dependent. GTP-dependent protein binding (GO:0030742; verified in OLS) is used as the replacement for effector protein-binding rows (PDE6D, UNC119, ARL2BP). GTPase activating protein binding (GO:0032794) replaces the RP2 row. TBL1X and Q5TEA3 rows REMOVE.
- NOT cilium (IDA, PMID:17646400) REMOVE. It is contradicted by endogenous (PMID:16525022, PMID:12417528), HPA and functional (PMID:30269812) evidence, and the cached text mentions Arl3 only by analogy.
- Small GTPase-mediated signal transduction (IDA, PMID:22085962): MARK_AS_OVER_ANNOTATED. The paper describes a protein-targeting GTPase cycle, not signal transduction.
- Cilium assembly (IBA, IMP zebrafish): KEEP_AS_NON_CORE. Patient fibroblasts form normal cilia, but early Arl3 deletion blocks photoreceptor ciliogenesis in mouse (per the deep research); the core defect is in membrane composition.
- Cytokinesis, midbody, spindle, Golgi, nucleus and microtubule binding: KEEP_AS_NON_CORE.

## HPA cilium atlas vs module role
- Module stage 5 (ciliary_membrane_composition): "ARL3-GTP displaces lipidated cargo from PDE6D and UNC119B inside the cilium". Module MF GO:0003924 GTPase activity; process protein localization to cilium.
- HPA v25: Primary cilium (Supported), Basal body (Approved), Centrosome (Supported); main locations Basal body, Centrosome and Nucleoplasm. GOA HPA rows: cilium (ACCEPT), centrosome and nucleoplasm (non-core).
- Assessment: HPA supports the module's ciliary placement. One difference in MF choice: I use G protein activity (GO:0003925) rather than the module's GTPase activity (GO:0003924) as the core MF. ARL3's intrinsic GTP hydrolysis is negligible and GAP (RP2)-driven, and its function is the GTP-dependent effector binding that releases cargo, which is the switch function GO:0003925 describes. Hydrolysis by RP2 is the off-step (inactivation), not the cargo-release step. The process (protein localization to cilium / ciliary membrane) agrees with the module.
