# Cacnb3 (mouse, P54285) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

This is a new review; no earlier mouse or rat Cacnb3 review existed. No ProtNLM2 files were opened or used.

### Process

- `just fetch-gene mouse Cacnb3` seeded 51 GOA rows. GOA lists 53; the two missing rows were collapsed by the stub seeder. No distinct GO term was lost.
- Deep research failed. Falcon gave `Exception: Failed to authenticate` from edison_client, and the perplexity-lite fallback returned HTTP 401 `insufficient_quota`. No deep-research file exists. The review is built from primary literature found with a PubMed search for beta3 knockout papers and cached with `just fetch-pmid`.
- I traced the ISO/ISS donor annotations for rat Cacnb3 (P54287) with QuickGO and cached their source papers, so that each transferred row could be judged on its source.

### Evolutionary grounding

From `Cacnb3-bioinformatics/RESULTS.md`, which uses the PANTHER 19.0 classification files and global alignment:

- Mouse P54285, human P54284 and rat P54287 are all in PTHR11824:SF8 (beta-3) and are 99.2% identical over 484 aa. Transfer from rat and human is therefore at subfamily level.
- The paralogs are in other subfamilies: beta1 SF17, beta2 SF9, beta4 SF7, each about 65-69% identical. Beta1b/beta2a-specific CaMKII binding [PMID:18205403 "activated/autophosphorylated CaMKII binds to beta1b and beta2a with a similar apparent affinity but does not bind to beta3 or beta4"] must not be transferred.
- PAINT: node PTN000930213 (family root) carries GO:0005891, GO:0006816 and GO:0008331, and mouse Cacnb3 descends from it. PAINT placed GO:0035249 (PTN000214435, seeded by another beta) and GO:0007268 (PTN002625095, seeded by another beta) on nodes that do not cover Cacnb3. I treat those omissions as deliberate and did not propose them.

### Experimentally established in mouse itself

- Regulation of HVA L- and N-type currents. [PMID:9751781 "in sympathetic beta3-/- neurons, the L- and N-type current was significantly reduced relative to wt"]; [PMID:12920136 "a 30% reduction in Ca2+ channel current density, a slower inactivation rate, and a decreased dihydropyridine-sensitive current in beta3-null mice"]; olfactory receptor neurons [PMID:17335778]; chromaffin cells [PMID:20144588]; outer hair cells [PMID:19755851]. The effect is subtle in ileum smooth muscle [PMID:17580090].
- Alpha1 surface expression and protein level. [PMID:12920136 "significant reduction in expression of the alpha1 subunit in the plasma membrane of beta3-null mice"]; [PMID:12161429 "low expression of N-type calcium channels (alpha1B)"].
- Complex membership. Co-IP with alpha1A/alpha1B in mouse brain [PMID:10328888].
- T-cell TCR calcium/NFAT response requires beta3 [PMID:17028169]. Annotated as acts_upstream_of_or_within; kept as non-core.
- Channel-independent phenotypes with no defined mechanism: enhanced IP3-mediated calcium release and insulin secretion in beta cells [PMID:15479643]; enhanced NMDAR currents and LTP with unchanged Ca2+ currents [PMID:18339621]. Not annotated, because these are necessity data and no step performed by beta3 has been shown. Raised as suggested questions and experiments.

### Inferred, not tested in mouse

- Cav1.2 surface targeting through the GK-AID interface [PMID:20478999] and the beta3 core/AID crystal structure [PMID:15170217], both done with rat beta3.
- Apical membrane in enterocytes (rat jejunum) [PMID:17272350].

### Key decisions

- Enables GO:0005245 and GO:0008331 → MODIFY to GO:0005246 calcium channel regulator activity, because beta is not the pore. The contributes_to GO:0005245 row is ACCEPTed. A validator warning about inconsistent actions on GO:0005245 remains; it reflects the qualifier difference and is intended.
- REMOVE GO:1902630 regulation of membrane hyperpolarization. The rat source reports a hyperpolarising shift of inactivation, which is not a change in membrane potential.
- REMOVE GO:0050966 and GO:1905788 (mechanical pain and touch detection). These are rat nerve-injury phenotypes; GO:1905788 also has the sign reversed. In mouse, acute mechanical nociception is largely unaffected in the knockout [PMID:12161429].
- MARK_AS_OVER_ANNOTATED: GO:0098903 (repolarisation), GO:1901386 (negative regulation; seen only with oocyte overexpression) and GO:2000463 (EPSP; a presynaptic effect in the rat source, with no basal transmission change in mouse hippocampus).
- UNDECIDED: GO:0019901 protein kinase binding. The abstract of the rat source argues against CaMKII binding to beta3, but the full text is not cached.
- Generic protein binding IPI rows → GO:0044325 transmembrane transporter binding.
