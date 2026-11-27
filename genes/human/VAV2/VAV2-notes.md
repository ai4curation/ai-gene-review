# VAV2 notes

Deep research could not be generated in this environment: `just deep-research-falcon human VAV2 --fallback perplexity-lite` failed because the installed `deep-research-client` exposed only the `claude_code` provider, and this workstream is not using sub-workers.

VAV2 is a broadly expressed VAV-family Rho GTPase guanine nucleotide exchange factor. The human protein belongs to PANTHER subfamily `PTHR45818:SF4`; PAINT places the shared VAV cytoplasmic GEF/small-GTPase signalling activity on PTN005252413, and Reactome separately curates VAV2 as a GEF for several Rho-family substrates, including RhoA, RhoB, RhoC, Rac1, Rac2, Rac3 and RhoG.

The original VAV2 cloning paper established VAV2 as a widely expressed VAV paralog rather than as the tuberous sclerosis gene TSC1 [PMID:7762982, "A novel widely expressed homologue of the VAV oncogene, VAV2"]. The experimentally curated GEF row cites the VAV1 Nature paper, but VAV2 has family-level, domain-level, UniProt and Reactome support for the same DH-domain exchange chemistry.

Two rows capture phosphotyrosine recognition by the VAV2 SH2 domain. Mehlitz et al. used a human SH2/PTB protein microarray and found phosphopeptide binding by VAV2 SH2 to the Chlamydia Tarp effector [PMID:20624904, "Numerous high affinity interactions occurred, most notably with the SH2 domains of ... VAV2"]. Spindler et al. solved the VAV2 SH2 complex with a phosphorylated PPxY motif from TXNIP and reported that the VAV2 and Src SH2 domains bind tyrosine-phosphorylated TXNIP peptides [PMID:26919541, "tyrosine-phosphorylated PPxY motifs also bind to SH2 domains of Vav2 and Src"].

The family-wide immune, Fc receptor, platelet and VEGF rows are kept as non-core contexts because VAV2 can be recruited into these signalling pathways as a Rho-family GEF, especially through Reactome's FCGR3A and VAV2/VAV3 SYK modules. The same azathioprine caveat as for VAV1 applies: `R-HSA-9751201` is evidence for the generic RAC1 exchange chemistry but only speculative support for a normal xenobiotic-response role.
