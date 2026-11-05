# BACSU gatB: biochemical and native-context review

GatB is the synthetase subunit of the GatCAB tRNA-dependent amidotransferase in Bacillus subtilis; it activates and amidates the tRNA-bound amino-acid side chain using ATP. Both glutamyl-tRNA(Gln) and aspartyl-tRNA(Asn) can feed the indirect pathways in this organism, which also retains a direct AsnS route.

The subunit contributes to the assembled catalytic complex. Ordinary relationship strings did not determine the action; the weaker contributes_to flag was respected where present.

PMID:9342321 directly localizes glutamine hydrolysis to GatA coexpressed with GatC, shows the assembled heterotrimer is most active, and finds GatC supports GatA expression/stability. The recombinant proteins were expressed in E. coli; operon disruption tested native Bacillus. PMID:9789001 tests Bacillus transamidation on Deinococcus tRNA and has an outdated discussion assumption that Bacillus lacks ND-AspRS; PMID:26804570 subsequently demonstrates the contrary.

GO:0070681 is currently obsolete; its explicit ontology comment warns against automatic reassignment to initial tRNA charging. GatCAB modifies an already esterified amino acid, so GO:0019988 is used for direct participation. GO:0006450 is not restricted to ribosomal factors: PMID:34225495 provides independent mechanistic evidence connecting GatCAB stability to fidelity in mycobacteria. Target-species extrapolation is qualified, not labeled as a native assay.

All original payloads and flags are preserved; no NEW annotations added. Actual Falcon/fallback and FEBA attempts failed; no source report or negative fitness phenotype fabricated. Normal publication caching succeeded.
