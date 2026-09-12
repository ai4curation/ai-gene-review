# GCN1 (Stalled ribosome sensor GCN1 / GCN1L1) research notes

## Identity
- UniProt Q92616; very large (~2671 aa) HEAT-repeat / alpha-solenoid ribosome-binding protein. GCN1 family. Has an RWD-binding domain (RWDBD).

## Core function — two intertwined ribosome-surveillance roles
1. **Ribosome collision/stall sensor that activates the eIF2alpha kinase GCN2 (EIF2AK4) -> integrated stress response (ISR).**
   - [GCN1-uniprot.txt "Ribosome collision sensor that plays a key role in the RNF14-RNF25 translation quality control pathway"]
   - [GCN1-uniprot.txt "acts as a sentinel for colliding ribosomes"]
   - [GCN1-uniprot.txt "positive activator of the integrated stress response (ISR) by mediating activation of EIF2AK4/GCN2 in response to amino acid starvation"]
   - [GCN1-uniprot.txt "Interaction with EIF2AK4/GCN2 on translating ribosomes stimulates EIF2AK4/GCN2 kinase activity, leading to phosphorylation of eukaryotic translation initiation factor 2"]
   - Conserved from yeast: GCN1/GCN20 stimulate GCN2 on translating ribosomes. [PMID:9234705 title "Evidence that GCN1 and GCN20, translational regulators of GCN4, function on elongating ribosomes in activation of eIF2alpha kinase GCN2"]
   - GCN1 binds the RWD domain of GCN2; IMPACT competes. [PMID:36638793 "GCN1 is a conserved ribosome-associated scaffolding protein that binds the RWD domain of the integrated stress response kinase, GCN2"]
2. **Ribosome collision sensor in the RNF14/RNF25 elongation-factor quality-control pathway (RQC).**
   - [PMID:36638793 title "An E3 ligase network engages GCN1 to promote the degradation of translation factors on stalled ribosomes"]
   - [PMID:36638793 "interacts with RNF14 and is also essential for eEF1A degradation"]
   - GCN1 required for resolution of mRNA-RNA-protein crosslink (RPC) stalls (RNF14/RNF25). [PMID:37951216 "RNF14 and RNF25 were recently shown to promote the degradation of translation factors that persistently block the ribosomal A site, which also requires the ribosome collision sensor GCN1"]
   - [PMID:37651229 "activating a branch of the ribosome-associated quality control network, which involves the translational stress sensor GCN1 and the catalytic activity of the E3 ubiquitin ligases RNF14 and RNF25"]

## Localization
- Cytoplasm; associates with ribosomes / cytosolic ribosome (polysomes, 80S). [GCN1-uniprot.txt "Associates with ribosomes"; PMID:9234705]
- Membrane (HDA PMID:19946888) and cadherin binding (HDA PMID:25468996) and RNA binding (HDA PMID:22681889) are high-throughput proteomic/mRNA-interactome screens -> non-specific / over-annotation.

## Annotation notes
- GO:0170011 stalled ribosome sensor activity (IDA, multiple papers) = CORE MF.
- GO:0043539 protein serine/threonine kinase activator activity (ISS/IEA) + GO:0019887 protein kinase regulator activity (IBA) = CORE MF (activates GCN2). Prefer the more specific kinase-activator term.
- GO:0060090 molecular adaptor activity (IDA PMID:36638793) — GCN1 scaffolds GCN2/RNF14/IMPACT via RWDBD; reasonable, keep (adaptor/scaffold). 
- GO:0072344 rescue of stalled cytosolic ribosome (IDA x4) = CORE BP (RQC role).
- GO:0140469 GCN2-mediated signaling (IEA/ISS) + GO:0034198 cellular response to amino acid starvation (IBA/IEA) = CORE/near-core BP (ISR activation).
- GO:0006417 regulation of translation (IBA) — broad; keep non-core (the specific roles are GCN2 activation + RQC).
- GO:0160127 protein-RNA covalent cross-linking repair (IDA PMID:37951215) — GCN1's role in resolving formaldehyde RPC stalls; keep (RQC-adjacent), non-core relative to the sensor MF.
- protein binding IPI (PMID:17314511, 20936779, 38884001) all WITH MYC (P01106) — c-MYC interactome / adipocyte HaloMS screens; GCN1 is large & abundant; isolated HT, not core -> MARK_AS_OVER_ANNOTATED.
- GO:0045296 cadherin binding (HDA) — proximity/affinity proteomics artifact -> MARK_AS_OVER_ANNOTATED.
- GO:0016020 membrane (HDA) — over-annotation; GCN1 is cytosolic/ribosomal -> MARK_AS_OVER_ANNOTATED.
- GO:0003723 RNA binding (HDA mRNA-interactome) — GCN1 binds ribosomes/rRNA contextually; bare RNA binding from HT capture, keep non-core.
- GO:0008135 translation factor activity, RNA binding (NAS, 1997) — outdated framing; GCN1 is a sensor/scaffold, not a canonical translation factor -> MARK_AS_OVER_ANNOTATED.
- GO:0005840 ribosome / GO:0022626 cytosolic ribosome (NAS/IDA) — correct CC (ribosome-associated). Accept.
