# CD3E (human, P07766) review notes

Project: ADAPTIVE_IMMUNITY (T cell receptor trunk).

## Biology summary (with provenance)

- TCR-CD3 composition: "The T cell receptor complex (TCR-CD3) is composed of TCR alpha/beta ligand binding subunits bound to the CD3 subunits responsible for signal transduction" [PMID:12110186]. Cryo-EM: "The octameric TCR-CD3 complex is assembled with 1:1:1:1 stoichiometry of TCRαβ:CD3γε:CD3δε:CD3ζζ." [PMID:31461748]
- Assembly: "The TCR/CD3 complex is assembled after a series of pairwise interactions involving the formation of dimers of CD3 epsilon with either CD3 gamma or CD3 delta." [PMID:9485181]; "the CD3-epsilon chain is central to CD3 core assembly and full complex formation" [PMID:8490660]; "CD3 epsilon is critical for the assembly of pre-TCR" [PMID:9886373].
- gamma-delta TCR: "whereas αβTCRs contain both CD3δɛ and CD3γɛ dimers, most γδTCRs were found to contain only CD3γɛ dimers" [PMID:16418397].
- ITAM/kinases: SPR, "The association rate and equilibrium binding constants for the ZAP-70 and syk SH2 domains were determined for the CD3 epsilon ITAM." [PMID:7761456]; N-terminal ITAM Tyr needed for ZAP-70 association [PMID:11855827].
- Proline-rich sequence/NCK: "ligand engagement of TCR-CD3 induces a conformational change that exposes a proline-rich sequence in CD3 epsilon and results in recruitment of the adaptor protein Nck" [PMID:12110186]; PxxDY motif shares Y166 with the ITAM, and its phosphorylation switches off SH3 binding [PMID:17617578]; structures with EPS8L1 SH3 [PMID:18644376] and NCK1 SH3.1 [PMID:18955169].
- Endocytosis: "Here we report that CD3 epsilon displays endocytosis determinants." [PMID:10384095]
- Newer regulators: ITPRIPL1 is "an inhibitory ligand of CD3ε" [PMID:38614099]; LAG-3 condensates with CD3E disrupt CD3E-Lck association [PMID:40592325].
- Disease: IMD18 (T-B+NK+ SCID) from CD3E mutations [PMID:8490660; UniProt].

## Curation decisions (106 GOA rows)

- 17 `protein binding` IPI rows: MODIFY to SH3 domain binding (NCK1/NCK2/EPS8L1 rows from PMID:17617578, 18644376, 18955169), protein tyrosine kinase binding (ZAP70/SYK from PMID:7761456, 11855827, 9698567), protein heterodimerization activity (CD3D/CD3G from PMID:9485181); REMOVE HuRI Y2H hits (PMID:32296183) and CEACAM1 (PMID:18424730).
- REMOVE: GPCR signaling pathway and RTK signaling pathway (TAS, PMID:8530500) - TCR-CD3 is neither.
- Over-annotated: integrin adhesion regulation (SKAP-55 paper, downstream of TCR), mouse neuronal development terms (dendrite/cerebellum development, phenotype-based), ARBA regulation terms, apoptosis (CD8-CD3E chimera crosslinking), T cell receptor binding (intra-complex contact; NAS from CD3G letter).
- UNDECIDED: positive/negative regulation of gene expression IMP (PMID:23817958, galectin-9 in MSCs; abstract does not mention CD3E, full text unavailable). Leaves one consistency warning vs the ARBA IEA row (MARK_AS_OVER_ANNOTATED) - intentional.
- Non-core: MHC class II receptor activity (contributes_to), positive thymic T cell selection (IBA), positive regulation of T cell proliferation, identical protein binding (in vitro oligomerization of disordered tails), neuronal locations, cell-cell junction.
- Necessity vs participation: process terms kept as core only where CD3E does part of the work (TCR signaling, TCR complex assembly). Proliferation/selection kept as non-core outcomes.

## Core functions

1. GO:0004888 transmembrane signaling receptor activity, in GO:0042105, directly in GO:0050852.
2. GO:1990782 protein tyrosine kinase binding (phospho-ITAM docking of ZAP70/SYK).
3. GO:0017124 SH3 domain binding (NCK recruitment via PRS).
4. GO:0030159 signaling receptor complex adaptor activity, in GO:0065003 protein-containing complex assembly, complex GO:0042101.

## Deep research

`just deep-research-falcon human CD3E --fallback perplexity-lite` launched in background at start of review; see status below.
