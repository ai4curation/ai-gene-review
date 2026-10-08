# cct-2 notes

## Session 2026-10-08 (claude-code)

- Accession: UniProtKB:P47207 (T21B10.7), beta subunit of CCT/TRiC; same accession as modules/c_elegans_cct_chaperonin_folding.yaml.
- Deep research: `just deep-research-falcon worm cct-2 --fallback perplexity-lite` failed (falcon exit 137; perplexity provider not configured). No deep-research file was created; review is based on cached publications plus PubMed searches.
- Conserved mechanism: CCT is an ATP-dependent folding machine for actin and tubulin [PMID:16762366 "The eukaryotic cytosolic chaperonin CCT is an essential ATP-dependent protein folding machine whose action is required for folding the cytoskeletal proteins actin and tubulin"]; eight distinct subunits per ring [PMID:15704212 "stoichiometric array of eight different subunits, which are denoted Cct1p-Cct8p"].
- Nucleotide hierarchy: cct-2 is one of the four high-ATP-affinity subunits (CCT1/2/4/5) [PMID:23041314 "Introducing the BND mutation into any of the high-affinity subunits identified by our biochemical analyses (i.e., CCT4, CCT5, CCT1 and CCT2) was lethal"].
- Worm CCT in vivo: depletion causes actin aggregation and tubulin loss [PMID:25143409 "CCT depletion causes a reduction in the tubulin levels and disorganization of the microtubule network"]; other subunits give similar phenotypes to cct-5 [PMID:25143409 "Because RNAi knockdown of other CCT subunits resulted in similar phenotypes in terms of abnormal mC-ACT-5 localization"].
- Somatic cct-2 overexpression extends lifespan and reduces polyQ toxicity, less than cct-8 [PMID:27892468 "our results indicate that both cct-8 and cct-2 extend longevity by sustaining the integrity of the proteome during adulthood"].
- cct-2 RNAi lowers endogenous CCT-6 levels and causes ectopic RNA-binding protein condensates in oocytes [PMID:39167497 "We created a FLAG-tagged allele of cct-6, and after RNAi of cct-2, our semiquantitative Western analysis revealed levels of CCT-6 reduced"].
- Ortholog of mouse Cctb [PMID:7576182 "The four genes, cct-2, cct-4, cct-5, and cct-6 are orthologs of the mouse chaperonin genes Cctb, Cctd, Ccte, and Cctz"].
- GO:0005515 protein binding (IPI, PMID:19123269) is a single HT-Y2H hit with Y39A1A.3 (G5EEN7, SSSCA1-like); REMOVE per protein-binding policy.

- Consistency: reviews modelled on genes/worm/cct-1 and genes/worm/cct-8 (GO:0140662 accepted as best available MF; contributes_to in core_functions).
