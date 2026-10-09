# mre11 (Drosophila MRE11) review notes

## Literature journal
- Telomere fusions in mre11 nulls: [PMID:15296751 "In mutant mitotic cells, an average of 30% of the chromosome ends engaged in telomere fusions."]; telomerase-independent [PMID:15296751 "Since Drosophila telomeres are not added by a telomerase, our findings support an additional role for both ATM and Mre11 in telomere maintenance that is independent of telomerase regulation."]
- Capping protein recruitment: [PMID:15296753 "This suggests that the MRN complex protects Drosophila telomeres by facilitating recruitment of HOAP and HP1 at chromosome ends."]
- Complex integrity and chromatin loading: [PMID:19520832 "Because of Nbs depletion, Mre11 and Rad50 (MR) are excluded from chromatin."]; [PMID:33556205 "Here, we show that Nbs interacts with Mre11 and transports the Mre11-Rad50 complex from the cytoplasm to the nucleus."]
- G2/M checkpoint: [PMID:16020777 "Our data indicate that both ATM and its regulator Mre11 are important for the checkpoint and that their roles become essential when animals are challenged with a low dose of X rays"]

## Curation decisions
- Core: ssDNA endonuclease (and 3'-5' exonuclease) of the MRN complex in DSB processing/HR; telomere capping with MRN.
- Protein binding (IPI, incl. DPIM2 AP-MS) removed as uninformative; covered by Mre11 complex.
- IBA meiotic DSB formation and mitochondrial DSB repair marked over-annotated (yeast-seeded, lineage-restricted).
- NHEJ and intra-S checkpoint (IBA) kept as non-core.
- Deep research (falcon) failed (rate limit / timeout); retried in background.
