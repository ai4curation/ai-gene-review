# PAO1 PhaG evidence scope, 2026-11-07

The normal seed and raw files were retained. Actual Falcon attempt failed403; no provider report was fabricated. Cached PMID10713430 is abstract-only; publisher full-text attempts were inaccessible. Its abstract explicitly reports native P. aeruginosa phaG replacement and heterologous complementation of a P. putida phaG mutant. Native gluconate-supported PHA falls to approximately40% of wild type, whereas fatty-acid-supported accumulation remains at wild-type levels. This is conditional pathway contribution, not sole-route necessity or isolated protein kinetics.

Official AF209711/AAF61903.1 is 300/300 identical to Q51553 and records ATCC15692, a PAO1 strain alias. This identity proof is independently captured in ../literature-consultation/identity/results.json and AF209711.embl. P. putida complementation is a different host assay. The primary abstract says the data suggest transacylase activity; it does not claim a PAO1 purified forward-transfer assay. Curated UniProt FUNCTION plus P. putida reverse-transfer biochemistry support the acyltransferase inference, while 2022 heterologous E. coli controls favor transacylation over exclusively hydrolytic release.

Both original IBA rows descend from actual PTN002455972, seeded by BioH P13001, with PAO1 leaf PTN002251180 in SF5. The retrieved lineage has no recorded IRD/IKR, but that does not prove biochemical equivalence. The node includes PhaG and RhlA as well as BioH. No PAO1 pimelyl-ACP methyl-ester assay or biotin-specific physiological test was identified. Alternate PHA physiology alone cannot establish absence of secondary chemistry; retain UNDECIDED rather than claim a proven evolutionary loss.

The sole new assertion is inferred non-amino-acyl transfer, a molecular role not represented by either BioH seed row. It rests on target sequence-linked genetics, curated function and characterized PhaG biochemistry, not a need to satisfy module coverage. No new BP, location, DNA-regulatory or stress-response row is proposed. The PHA process is captured in core synthesis because PhaG supplies the hydroxyacyl reaction connecting monomer pools, not merely because its knockout changes output. RhlA and BioH share the broad fold but distinct reaction specificity, so no family-wide PhaG grant is implied.


## PR6194 follow-up — 2026-11-07

New normally fetched PMID36689471 directly establishes dedicated native PAO1 BioH/PA0502 and biotin rescue/complementation. GO0009102 is now MAOA because the ancestral pathway assignment exceeds PhaG evidence; GO0090499 remains UNDECIDED, as endogenous failure to compensate is not a purified PhaG-negative assay. Original authored NEW IC payload is unchanged. Frozen UniProt EC2.4.1.- versus hydroxyacyl-transfer chemistry is recorded as a source defect without rewriting the raw record.

Exact evidence, before/after payload audit and source hashes: analysis/module_audits/bacterial_mcl_pha_synthesis_and_mobilization/review-followup/implementation/.
