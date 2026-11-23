# MPST PTHR11364 review notes

## 2026-11-23 family review

Deep-research automation was not available in this checkout: `just deep-research-falcon human MPST --fallback perplexity-lite` failed because only the `claude_code` provider was configured. This manual note summarizes the local UniProt, GOA, PAINT, Reactome and cached-literature evidence used for the review.

Human MPST is the PTHR11364:SF25 member and keeps the eukaryotic PTN000146244 3-mercaptopyruvate sulfurtransferase and tRNA wobble uridine thiolation calls. Parsed cached PAINT tree `.cache/panther_trees/19.0/PTHR11364.json.gz`: the human MPST leaf P25325 is PTN002478498 and is not under PTN008517019, the TST-branch IRD node that blocks the ancestral MST and tRNA-thiolation calls.

Core molecular function: MPST is the human 3-mercaptopyruvate sulfurtransferase. UniProt records the RHEA:21740 / EC 2.8.1.2 reaction transferring sulfur from 3-mercaptopyruvate to thioredoxin to produce hydrogen sulfide and pyruvate by orthology to rat MPST; Reactome records human MPST reactions using 3-mercaptopyruvate to make thiosulfate, to persulfurate Cys248-MPST, and with TXN2 to release disulfanide/HSS-. Ogunkola et al. 2023 directly corroborate MPST/TUM1 contributions to sulfur transfer for cytosolic tRNA thiolation in human HEK293T knockout cells.

Locations: UniProt transfers cytoplasm and mitochondrion from rat MPST and synaptosome from mouse Mpst; Morgenstern et al. 2021 put MPST in MitoCoP, the high-confidence human mitochondrial proteome; Reactome places the curated human MPST sulfur-transfer reactions in the mitochondrial matrix. The synapse/neuron-projection calls are peripheral localizations. Urinary and prostatic exosome proteomics are peripheral high-throughput detections rather than MPST core locations.

Weak and misplaced rhodanese/cyanide calls: MPST has weak thiosulfate-cyanide sulfurtransferase activity and can support 3-mercaptopyruvate-dependent cyanide conversion in Reactome, but TST is the dedicated human thiosulfate-cyanide sulfurtransferase. PMID:9070219 cloned and expressed TST/rhodanese, not MPST; the three PINC annotations citing that paper on MPST are legacy misapplications.

Cyanate is not cyanide. The MPST GO:0009440 cyanate catabolic process rows cite either ARBA:ARBA00092626 or the TST cDNA paper PMID:9070219, and neither source establishes catabolism of OCN- cyanate by MPST.

No human MPST source in this review provides a direct kidney, liver, or spinal cord developmental role for MPST; those Ensembl rows are rat phenotype transfers and sit downstream of sulfur-transfer metabolism rather than naming the MPST molecular work.

The exact MPST/TST family did not match an existing production GO-CAM or an existing `modules/` review. The human members are a biochemical paralog pair rather than a stable multi-protein module: MPST participates with GOT2/TXN2, MOCS3/NFS1, and URM1/CTU1/CTU2 in broader sulfur-transfer contexts, while TST is the mitochondrial rhodanese that also moonlights with MRPL18 in 5S rRNA import.
