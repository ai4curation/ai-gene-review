# cct-4 notes

## Session 2026-10-08 (claude-code)

- Accession: UniProtKB:P47208 (K01C8.10), delta subunit of CCT/TRiC; same accession as modules/cct_chaperonin_folding.yaml.
- Deep research: `just deep-research-falcon worm cct-4 --fallback perplexity-lite` failed (falcon exit 137; perplexity provider not configured). No deep-research file was created; review is based on cached publications plus PubMed searches.
- Conserved mechanism: CCT is an ATP-dependent folding machine for actin and tubulin [PMID:16762366 "The eukaryotic cytosolic chaperonin CCT is an essential ATP-dependent protein folding machine whose action is required for folding the cytoskeletal proteins actin and tubulin"]; eight distinct subunits per ring [PMID:15704212 "stoichiometric array of eight different subunits, which are denoted Cct1p-Cct8p"].
- Nucleotide hierarchy: cct-4 is one of the four high-ATP-affinity subunits (CCT1/2/4/5) [PMID:23041314 "Introducing the BND mutation into any of the high-affinity subunits identified by our biochemical analyses (i.e., CCT4, CCT5, CCT1 and CCT2) was lethal"].
- Worm CCT in vivo: depletion causes actin aggregation and tubulin loss [PMID:25143409 "CCT depletion causes a reduction in the tubulin levels and disorganization of the microtubule network"]; other subunits give similar phenotypes to cct-5 [PMID:25143409 "Because RNAi knockdown of other CCT subunits resulted in similar phenotypes in terms of abnormal mC-ACT-5 localization"].
- CCT-4 is nuclear in germline cells and binds meiotic HORMADs [PMID:41136395 "Consistent with its function as a subunit of TRiC, CCT-4-appeared as cytoplasmic foci in wild-type germlines, but also showed abundant nuclear localization in mitotic and meiotic cells."]. Proposed NEW: located_in nucleus (IDA). No new BP proposed: the folding of HORMADs is covered by protein folding.
- cct-4 and other subunits needed for intestinal endocytic trafficking [PMID:36607310 "In C. elegans, deficiency of cct-4 as well as other CCT subunits impairs the trafficking of endocytic markers in intestinal cells"] (abstract only; not annotated as BP since it is attributed to dynamin folding).
- GO:0040032 post-embryonic body morphogenesis (IMP, Kamath 2003 genome-wide RNAi) kept as non-core pleiotropic phenotype.
- Note: PMID:39167497 and PMID:41136395 both report a mislabelled cct-4 RNAi library clone (39167497: "We note the clone labeled cct-4 in the Source Bioscience RNAi library is misidentified"); older RNAi-based cct-4 data should be interpreted with care.

- Consistency: reviews modelled on genes/worm/cct-1 and genes/worm/cct-8 (GO:0140662 accepted as best available MF; contributes_to in core_functions).
