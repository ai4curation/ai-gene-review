# cct-5 notes

## Session 2026-10-08 (claude-code)

- Accession: UniProtKB:P47209 (C07G2.3), epsilon subunit of CCT/TRiC; same accession as modules/c_elegans_cct_chaperonin_folding.yaml.
- Deep research: `just deep-research-falcon worm cct-5 --fallback perplexity-lite` failed (falcon exit 137; perplexity provider not configured). No deep-research file was created; review is based on cached publications plus PubMed searches.
- Conserved mechanism: CCT is an ATP-dependent folding machine for actin and tubulin [PMID:16762366 "The eukaryotic cytosolic chaperonin CCT is an essential ATP-dependent protein folding machine whose action is required for folding the cytoskeletal proteins actin and tubulin"]; eight distinct subunits per ring [PMID:15704212 "stoichiometric array of eight different subunits, which are denoted Cct1p-Cct8p"].
- Nucleotide hierarchy: cct-5 is one of the four high-ATP-affinity subunits (CCT1/2/4/5) [PMID:23041314 "Introducing the BND mutation into any of the high-affinity subunits identified by our biochemical analyses (i.e., CCT4, CCT5, CCT1 and CCT2) was lethal"].
- Worm CCT in vivo: depletion causes actin aggregation and tubulin loss [PMID:25143409 "CCT depletion causes a reduction in the tubulin levels and disorganization of the microtubule network"]; other subunits give similar phenotypes to cct-5 [PMID:25143409 "Because RNAi knockdown of other CCT subunits resulted in similar phenotypes in terms of abnormal mC-ACT-5 localization"].
- Biochemically identified in purified worm CCT with anti-CCT-5 antibody [PMID:9434769 "SDS-gel electrophoresis and Western blot analyses with antibodies against C. elegans CCT-1 and CCT-5"].
- Cytoplasmic in intestinal cells; RNAi causes actin aggregation, tubulin loss and microvillus defects [PMID:25143409 "CCT existed diffusely in the cytoplasm but less in the nucleus"; "is essential for proper formation of microvilli in intestinal cells"].
- Co-IPs with CCT-4 and HIM-3 in germline [PMID:41136395 "Furthermore, CCT-5 was detected in immunoprecipitated CCT-4-containing complexes"].

- Consistency: reviews modelled on genes/worm/cct-1 and genes/worm/cct-8 (GO:0140662 accepted as best available MF; contributes_to in core_functions).
