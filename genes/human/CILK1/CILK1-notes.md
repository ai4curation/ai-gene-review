# CILK1 / ICK (Q9UPZ9) curation notes

## Deep research status
DR_STATUS_PLACEHOLDER

## Summary of function
- Serine/threonine kinase with MAPK-like TDY motif [PMID:10699974 "harbors a dual phosphorylation site found in mitogen-activating protein (MAP) kinases that is important for kinase activity"]; activation by dual TDY phosphorylation [PMID:15988018 "Our studies establish ICK as the prototype for a new group of MAPK-like kinases requiring dual phosphorylation at TDY motifs."].
- ECO syndrome R272Q: loss of nuclear localization and reduced kinase activity [PMID:19185282 "We also demonstrate that the R272Q mutant fails to localize at the nucleus and has diminished kinase activity."].
- Ciliary tip kinase regulating IFT turnaround; phosphorylates KIF3A [PMID:24797473 "Here, we identified ICK localization at the tip of cilia as a regulator of ciliary transport."; "Loss of ICK caused the accumulation of IFT-A, IFT-B, and BBSome components at the ciliary tips."; "ICK directly phosphorylated Kif3a"].
- Negative regulator of cilium length [PMID:24853502 "down-regulation of Ick or overexpression of kinase-dead or ECO syndrome mutant ICK resulted in an elongation of primary cilia and abnormal Sonic hedgehog (Shh) signaling"; PMID:25243405 "localize to cilia of mouse renal epithelial (IMCD-3) cells and negatively regulate cilium length"]; ICK moves with IFT trains and alters IFT velocities [PMID:25243405].
- Cell-type dependence: some ICK-deficient cells show impaired ciliogenesis rather than elongation [PMID:24797473 "essential for proper ciliogenesis in development"].

## Key decisions
- Kinase activity rows ACCEPT; protein binding (HSP90AB1, FKBP5, SMYD2) REMOVE; nucleus KEEP_AS_NON_CORE.
- Signal transduction TAS MARK_AS_OVER_ANNOTATED; intracellular signal transduction KEEP_AS_NON_CORE.
- NEW negative regulation of non-motile cilium assembly (GO:1902856), ISS PMID:24853502. GO has no cilium-length term (checked QuickGO); comparator: mouse Mak carries GO:1902856 (IMP/IDA/IGI, PMID:21148103).

## HPA cilium atlas vs module role
- Module (stage 6 length control): RCK kinase, protein serine/threonine kinase activity, regulation of cilium assembly (GO:1902017), ciliary tip.
- HPA v25: Primary cilium (Supported) and Primary cilium tip (Supported); main locations Golgi apparatus; Vesicles. GOA HPA rows: cilium, ciliary tip.
- Interpretation: strong agreement; the HPA ciliary-tip call independently corroborates the tip localization central to the IFT-turnaround model. core_functions agree with the module and use the more specific descendant GO:1902856 (negative regulation of non-motile cilium assembly) rather than GO:1902017; the Golgi/vesicle calls are not explained by current literature.
