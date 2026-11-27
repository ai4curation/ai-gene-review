# VAV3 notes

Deep research could not be generated in this environment: `just deep-research-falcon human VAV3 --fallback perplexity-lite` failed because the installed `deep-research-client` exposed only the `claude_code` provider, and this workstream is not using sub-workers.

VAV3 is a broadly expressed VAV-family Rho GTPase guanine nucleotide exchange factor in `PTHR45818:SF1`. Its original characterization showed exchange activity for RhoA and RhoG, and weaker activity toward Rac1, after activation by protein tyrosine kinases [PMID:10523675, "Vav-3 promotes the exchange of nucleotides on RhoA, on RhoG and, to a lesser extent, on Rac-1"].

The PINC `GO:0005096` GTPase activator activity row on PMID:10523675 has the reaction direction backwards. The paper describes nucleotide exchange and binding to nucleotide-free GTPases, which is GEF rather than GAP chemistry [PMID:10523675, "promote both the binding to GTP-hydrolases and their GDP-GTP nucleotide exchange"]. This should be reported as a wrong-term source defect and removed from the review.

PMID:15708849 directly supports VAV3 recruitment to the immunological synapse in T cells. The abstract reports that TCR-induced VAV3 association with SLP-76 is required for membrane/immunological-synapse localization and function [PMID:15708849, "TCR-induced association of Vav3 with SLP-76 is required for its membrane/IS localization and function"].

Four older UniProt IMP rows cite PMID:17875758 for DNA damage response, response to xenobiotic stimulus, B-cell proliferation and B-cell receptor signalling. The cache has only the abstract, which foregrounds CLL subgroup expression of ATM, CTLA4, MNDA and HEM1 and does not expose the evidence for VAV3. Those rows stay `UNDECIDED` rather than being removed from an incomplete paper view.

Reactome's GEF rows are largely consistent with the VAV3 abstract and the PAINT root GEF node, but the azathioprine `R-HSA-9751201` event is not strong enough to resolve the xenobiotic-response biological-process rows while the abstract-only PMID:17875758 UniProt row is also present: the Reactome event says the 6-thio-GTP exchange is only "presumably mediated by VAV proteins" [Reactome:R-HSA-9751201, "can block RAC1 activity by binding to it instead of GTP (presumably mediated by VAV proteins)"].
