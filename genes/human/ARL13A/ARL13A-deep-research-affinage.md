---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ARL13A
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q5H913
self_evaluation_pairwise: 
faith_pct: 100.0
n_discoveries: 14
citation_count: 14
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ARL13A (human)

## Current model (mechanistic narrative)

ARL13A is studied almost entirely through its ortholog/paralog ARL13B and conserved counterparts in invertebrate and protozoan models, where it functions as a ciliary small GTPase governing membrane protein trafficking within cilia [PMID:20231383, PMID:36943875]. It localizes to a defined proximal subciliary membrane compartment that excludes the transition zone, a placement that depends on a C-terminal RVVP motif, palmitoylation-based membrane anchoring, and active retention by IFT-A/B, BBS, and the MKS/NPHP transition-zone diffusion barrier and CEP-290 [PMID:20231383, PMID:24339792, PMID:26982032]. Mechanistically, ARL13 operates within a GTPase cascade: in its GTP-bound, membrane-anchored state it acts as a guanine-nucleotide exchange factor for ARL3, which in turn engages downstream effectors such as UNC119 to deliver lipidated cargo into the cilium [PMID:30097558, PMID:32587088]. Cycling between membrane-bound GTP and matrix GDP states allows ARL13-GTP to recruit the remodeled BBSome as an effector and, upon GTP hydrolysis, release cargo-laden BBSome onto retrograde IFT trains, thereby enabling BBSome-dependent export of membrane proteins such as phospholipase D [PMID:36040375, PMID:36943875]. ARL13 also coordinates IFT subcomplex A/B association together with ARL3 through an HDAC6-dependent route [PMID:20530210], is SUMOylated by UBC-9 to control ciliary targeting of sensory receptors and polycystin-2 [PMID:23128241], and functions upstream of Gli2 in Sonic hedgehog signaling during morphogenesis [PMID:32169553]. The zebrafish Arl13a paralog specifically localizes to microtubules in ciliated and dividing embryonic cells with a craniofacial-restricted expression pattern distinct from Arl13b, indicating divergent paralog roles [PMID:30009987]; beyond this, ARL13A itself has not been independently characterized in the available corpus.

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0003924 GTPase activity, GO:0098772 molecular function regulator activity
- **localization:** GO:0005929 cilium, GO:0005886 plasma membrane, GO:0005856 cytoskeleton
- **pathway (Reactome):** *(none)*
- **partners:** ARL3, BBS3, IFT46, IFT74, UBC-9, UNC119
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2010 | High | C. elegans ARL-13 (ARL13B ortholog) localizes to proximal ciliary membranes via palmitoylation modification motifs; loss-of-function causes defects in cilium morphology/ultrastructure, abnormal accumulation of ciliary transmembrane proteins, elevated PKD-2 ciliary abundance, and destabilized anterograde IFT. | PMID:20231383 | The Journal of cell biology |
| 2010 | High | C. elegans ARL-13 localizes exclusively to the doublet segment of the cilium; arl-13 mutants show shortened cilia with ultrastructural deformities and disrupted association between IFT subcomplexes A and B; depletion of ARL-3 partially suppresses arl-13 ciliogenesis defects by restoring IFT-A/B binding via an HDAC6-dependent pathway, indicating ARL-13 and ARL-3 coordinately regulate IFT. | PMID:20530210 | The Journal of cell biology |
| 2012 | High | UBC-9 (E2 SUMO-conjugating enzyme) physically interacts with and SUMOylates the C-terminus of C. elegans ARL-13; SUMOylation-abolishing mutations do not affect ciliogenesis but impair proper ciliary targeting of sensory receptors and corresponding sensory functions; constitutively SUMOylated ARL-13 fully rescues ciliary defects. In human ARL13B, SUMOylation is required for ciliary entry of polycystin-2. | PMID:23128241 | The Journal of cell biology |
| 2013 | High | ARL13B/ARL-13 localizes to an Inversin-like subciliary membrane compartment (excluding the transition zone) in C. elegans and mammalian cells; compartmentalization requires a C-terminal RVVP motif and membrane anchoring; IFT-A/B, IFT-dynein, and BBS genes prevent ARL-13 accumulation at periciliary membranes; MKS/NPHP modules additionally inhibit ARL-13 at TZ membranes and form a diffusion barrier; ARL-13 undergoes IFT-like motility; human ARL13B physically associates with IFT-B complexes via IFT46 and IFT74. | PMID:24339792 | PLoS genetics |
| 2014 | High | In C. elegans, arl-13 and nphp-2 (Inversin) define distinct but interacting genetic modules redundantly required for ciliogenesis; arl-13 module (with unc-119) and nphp-2 module (with klp-11) are both antagonized by hdac-6 deacetylase; these modules modulate InvC and doublet region sizes, ciliary microtubule ultrastructure, and protein localization, but ciliary targeting of ARL-13 does not require TZ, doublet region, or InvC-associated genes. | PMID:25501555 | PLoS genetics |
| 2016 | Medium | CEP-290 at the transition zone keeps ARL-13 (Arl13b) from leaking out of cilia via the TZ, functioning as a ciliary gate component that retains ARL-13 within the cilium. | PMID:26982032 | PLoS biology |
| 2018 | Medium | Trypanosoma brucei TbArl13 (Arl13b ortholog) acts as a guanine-nucleotide exchange factor (GEF) for two TbArl3 homologs (TbArl3A and TbArl3C); TbArl13 is distinctly associated with the axoneme through a dimerization/docking (D/D) domain rather than the ciliary membrane; flagellar enrichment is functionally required but the mechanism is flexible (D/D domain replaceable by a membrane-targeting sequence in RNAi rescue). | PMID:30097558 | Journal of cell science |
| 2018 | Medium | Zebrafish Arl13a (the paralog to Arl13b) localizes to microtubules in ciliated and dividing cells of early zebrafish embryo; expression is downregulated by 2 dpf and restricted to craniofacial structures, contrasting with Arl13b's sustained neural expression, indicating distinct functional roles. | PMID:30009987 | Gene expression patterns : GEP |
| 2020 | Medium | TbArl13 in Trypanosoma brucei catalyzes nucleotide exchange on TbArl3A (but not TbArl3C) which then interacts with TbUnc119 in a GTP-dependent manner, supporting a conserved lipidated protein intraflagellar transport (LIFT) pathway where Arl13b acts upstream of Arl3 to facilitate myristoylated cargo delivery to the flagellum. | PMID:32587088 | The Journal of biological chemistry |
| 2020 | Medium | Loss of Arl13b in mouse embryos causes inverted optic cup orientation due to misregulation of Sonic hedgehog (Shh) signaling; the Arl13b−/− eye phenotype is rescued by deletion of Gli2 (a downstream Shh effector), placing Arl13b upstream of Gli2 in the Shh pathway during optic morphogenesis. | PMID:32169553 | Developmental biology |
| 2022 | Medium | Loss of ARL13 in Chlamydomonas impedes BBSome-dependent protein export from cilia (not IFT or BBSome traffic per se): the membrane-associated phospholipase D (PLD), which normally moves via BBSome-dependent IFT, accumulates in arl13 mutant cilia; ARL13 itself only rarely and transiently travels by IFT, indicating it is not a co-migrating adapter but acts indirectly to enable BBSome-cargo coupling. | PMID:36040375 | The Journal of cell biology |
| 2023 | Medium | In Chlamydomonas, ARL13 in GTP-bound form (ARL13GTP) anchors to the ciliary membrane; upon ciliary entry, ARL13 undergoes GTPase cycling between membrane (GTP) and matrix (GDP) states; membrane-anchored BBS3GTP acts as a GEF for ARL13GDP to generate ARL13GTP; ARL13GTP recruits the post-remodeled BBSome to the ciliary membrane as an effector; ARL13GTP then hydrolyzes GTP to release the PLD-laden BBSome for loading onto retrograde IFT trains. | PMID:36943875 | Proceedings of the National Academy of Sciences of the United States of America |
| 2024 | Low | In Trypanosoma brucei, ARL13 and ARL3 both function in IFT-related cargo transport in motile cilia; ARL3 (not ARL13) directly binds ODA16 as a specific effector to dissociate it from the IFT complex for cargo unloading, while ARL13 acts upstream. Depletion of ARL3 stabilizes ODA16-IFT interaction causing accumulation and axonemal assembly defects. | PMID:39231220 | Science advances |
| 2025 | Medium | In C. elegans, ARL-13 (ARL13B) is essential for juxtaposed cilia-cilia elongation (JCE); ARL-13 modulates JCE independently of cilia length; loss of NPHP-2/inversin plus HDAC-6 enhances the cilia misdirection phenotype of arl-13 mutants; disruption of the BBSome complex (but not microtubule components) partially suppresses JCE defects in arl-13 mutants; arl-13 mutants show altered ciliary membrane phospholipid composition. | PMID:39925426 | iScience |

## Citations

- PMID:20231383
- PMID:20530210
- PMID:23128241
- PMID:24339792
- PMID:25501555
- PMID:26982032
- PMID:30009987
- PMID:30097558
- PMID:32169553
- PMID:32587088
- PMID:36040375
- PMID:36943875
- PMID:39231220
- PMID:39925426
