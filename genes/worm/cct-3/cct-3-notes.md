# cct-3 notes

## Session 2026-10-08 (claude-code)

- Accession: UniProtKB:Q9N4J8 (F54A3.3), gamma subunit of CCT/TRiC; same accession as modules/c_elegans_cct_chaperonin_folding.yaml.
- Deep research: `just deep-research-falcon worm cct-3 --fallback perplexity-lite` failed (falcon exit 137; perplexity provider not configured). No deep-research file was created; review is based on cached publications plus PubMed searches.
- Conserved mechanism: CCT is an ATP-dependent folding machine for actin and tubulin [PMID:16762366 "The eukaryotic cytosolic chaperonin CCT is an essential ATP-dependent protein folding machine whose action is required for folding the cytoskeletal proteins actin and tubulin"]; eight distinct subunits per ring [PMID:15704212 "stoichiometric array of eight different subunits, which are denoted Cct1p-Cct8p"].
- Nucleotide hierarchy: cct-3 is a low-ATP-affinity subunit (CCT3/6/7/8) [PMID:23041314 "However, CCT3, CCT6, CCT7, and CCT8 have very low ATP occupancy even at high ATP concentrations, and thus are classified as low-affinity subunits"]; ATP binding/hydrolysis annotations therefore KEEP_AS_NON_CORE and core MF is only contributes_to GO:0140662.
- Worm CCT in vivo: depletion causes actin aggregation and tubulin loss [PMID:25143409 "CCT depletion causes a reduction in the tubulin levels and disorganization of the microtubule network"]; other subunits give similar phenotypes to cct-5 [PMID:25143409 "Because RNAi knockdown of other CCT subunits resulted in similar phenotypes in terms of abnormal mC-ACT-5 localization"].
- cct-3 RNAi phenocopies cct-4 axis-assembly defects in meiosis [PMID:41136395 "phenotypes that were also observed for cct-1(RNAi) and cct-3(RNAi)"].
- UniProt cites PMID:16054029 (Srayko 2005 embryonic MT-growth RNAi screen) for a role in microtubule polymerization; abstract-only, does not name cct-3. Interpreted as indirect via tubulin folding; not annotated.
- All eight cct genes are negative regulators of the heat shock response in muscle [PMID:23637632 "knockdown of subunits of the TRiC/CCT chaperonin induces HS reporter expression"].

- Consistency: reviews modelled on genes/worm/cct-1 and genes/worm/cct-8 (GO:0140662 accepted as best available MF; contributes_to in core_functions).
