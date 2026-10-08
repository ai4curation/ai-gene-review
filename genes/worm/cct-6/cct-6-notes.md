# cct-6 notes

## Session 2026-10-08 (claude-code)

- Accession: UniProtKB:P46550 (F01F1.8), zeta subunit of CCT/TRiC; same accession as modules/c_elegans_cct_chaperonin_folding.yaml.
- Deep research: `just deep-research-falcon worm cct-6 --fallback perplexity-lite` failed (falcon exit 137; perplexity provider not configured). No deep-research file was created; review is based on cached publications plus PubMed searches.
- Conserved mechanism: CCT is an ATP-dependent folding machine for actin and tubulin [PMID:16762366 "The eukaryotic cytosolic chaperonin CCT is an essential ATP-dependent protein folding machine whose action is required for folding the cytoskeletal proteins actin and tubulin"]; eight distinct subunits per ring [PMID:15704212 "stoichiometric array of eight different subunits, which are denoted Cct1p-Cct8p"].
- Nucleotide hierarchy: cct-6 is a low-ATP-affinity subunit (CCT3/6/7/8) [PMID:23041314 "However, CCT3, CCT6, CCT7, and CCT8 have very low ATP occupancy even at high ATP concentrations, and thus are classified as low-affinity subunits"]; ATP binding/hydrolysis annotations therefore KEEP_AS_NON_CORE and core MF is only contributes_to GO:0140662.
- Worm CCT in vivo: depletion causes actin aggregation and tubulin loss [PMID:25143409 "CCT depletion causes a reduction in the tubulin levels and disorganization of the microtubule network"]; other subunits give similar phenotypes to cct-5 [PMID:25143409 "Because RNAi knockdown of other CCT subunits resulted in similar phenotypes in terms of abnormal mC-ACT-5 localization"].
- Endogenous CCT-6::3xFLAG abundant in germline and oocytes [PMID:39167497 "We detected high levels of CCT-6 in oocytes and throughout the germline"]; N-terminal GFP tag was larval lethal in that study.
- cct-6 knockdown partially suppresses lifespan extension by cct-8(OE) and cct-2(OE) [PMID:27892468 "knockdown of cct-6 partially reduces the longevity phenotype of both cct-8(OE) and cct-2(OE) worms"].
- Ortholog of mouse Cctz [PMID:7576182]. Human has two paralogs (CCT6A, CCT6B); the worm has one.

- Consistency: reviews modelled on genes/worm/cct-1 and genes/worm/cct-8 (GO:0140662 accepted as best available MF; contributes_to in core_functions).
