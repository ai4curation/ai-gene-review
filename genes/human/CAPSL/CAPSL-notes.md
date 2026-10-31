# CAPSL evidence notes

Human UniProt Q8WWF8 provides four EF-hand domains and PROSITE-ProRule calcium-binding positions; this is sequence inference, not a direct binding assay. Horse A0A3Q2I3U9 has VGNC:16048 CAPSL identity, corresponding EF-hand domains and 202/208 identical aligned human residues (97.1%; see the horse alignment report). The 17-residue horse N-terminal extension does not erase the aligned EF-hand core.

[PMID:39264149](https://pubmed.ncbi.nlm.nih.gov/39264149/), DOI [10.7554/eLife.96907](https://doi.org/10.7554/eLife.96907), full text cached: “CAPSL is localized in both the cytoplasm and the nucleus of cells”. Human HREC depletion directly impairs endothelial phenotypes; endothelial-specific mouse knockout supplies in vivo retinal angiogenesis evidence. The paper does not establish a direct CAPSL–MYC physical interaction or enzymatic activity.

[PMID:31186450](https://pubmed.ncbi.nlm.nih.gov/31186450/), full text cached, examines human adipose-derived cells and mouse 3T3-L1 cells. “CapslKO cells showed enhanced propensity for differentiation, while CapslOE cells showed no proper lipid accumulation”. These results suggest regulation of adipogenesis and autophagic flux but do not establish an intrinsic enzyme function or a horse tissue-specific phenotype.

Horse record is unreviewed and has genome-sequencing identification rather than horse-specific functional experiments. A dedicated horse Edison report is not warranted by these sources. A completed human Falcon report has been inspected; primary sources above are independently inspected and cached.

## Human deep-research integration

The Falcon report retrieved a June 2026 mechanistic preprint, Cai et al., [DOI:10.64898/2026.06.11.731632](https://doi.org/10.64898/2026.06.11.731632), independently verified through Europe PMC PPR1251699 (raw source cached in the human directory). Its abstract states: “We identify the calcium-binding protein CAPSL as a lumenal MIP that forms a pseudo-helical spiral and stabilizes microtubules  in vitro .” The native structure is bovine tracheal cilia, a legitimate mammalian comparison; the report describes recombinant human CAPSL experiments, but those assay details have not yet been independently inspected because full-text retrieval was unavailable. This is a substantial structural lead, not proof supplied by an AI conclusion. It supports a provisional ciliary structural role and makes the nuclear/cytoplasmic observations compatible with multiple cellular pools.

The Falcon synthesis missed the independently inspected peer-reviewed FEVR and adipogenesis studies above. Retain their evidence rather than adopting its claim that no human phenotype study exists. The calcium-binding assignment remains an EF-hand inference; direct calcium occupancy/affinity measurements were not established.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Scope: full re-review of benchmark accession Q8WWF8 (cohorts HORSE40 + HORSE40_HUMAN_PAIR). ProtNLM2 output was not consulted.

Identity: Q8WWF8 is the reviewed Swiss-Prot canonical human CAPSL entry (208 aa, sequence version 4). It is not a fragment, isoform or alternative gene model. All four EF-hand domains are present (39-74, 75-110, 111-146, 154-191). PROSITE-ProRule assigns calcium-coordinating positions only in EF-hands 1 and 2 (52, 54, 56, 58, 63; 88, 90, 92, 94, 99), with two PS00018 hits.

Evolutionary grounding: UniProt places human (Q8WWF8), mouse (Q6P8Y1) and bovine (A6H790) CAPSL in PANTHER PTHR34524:SF5 (calcyphosin-like protein). All three are 208 aa. Ungapped positional identity to human is 96.2% for bovine and 94.7% for mouse (simple same-length comparison of UniProt FASTA sequences, run in the session scratchpad, not a published analysis). Calcyphosin CAPS (Q13938) sits in SF2 and CFAP68 in SF1, so subfamily-specific functions of those paralogs are not transferred. The CAPS crystal structure (PMID:18775726) is used only for the shared EF-hand calcium-binding architecture. The PANTHER family review interpro/panther/PTHR34524/PTHR34524-review.yaml also places CAPSL in SF5, so the placement agrees. Its calcium-binding scope is UNRESOLVED, and its summary does not yet mention the ciliary MIP evidence.

Corrections made:
- The cytoplasm/nucleus sentence in PMID:39264149 cites the Human Protein Atlas ("(https://www.proteinatlas.org/)"). It is not an experiment of that paper. The previous review treated it as a direct observation. Cytoplasm was changed from ACCEPT to KEEP_AS_NON_CORE.
- The organelle row (ARBA) was changed from KEEP_AS_NON_CORE to MODIFY, with replacement GO:0035869 ciliary transition zone (is_a descendant via cilium, checked with OLS hierarchicalAncestors). The basis is the Cai et al. 2026 transition-zone cryo-ET preprint (DOI:10.64898/2026.06.11.731632). Its native structure is from the bovine SF5 ortholog. Only the abstract could be cached (landing_page_only).
- NEW GO:0008017 microtubule binding: CAPSL is a lumenal microtubule inner protein that "stabilizes microtubules in vitro" (abstract). This is the protein's own physical activity. It is provisional until the paper is peer reviewed. I did not choose the axonemal inner-sheath terms (GO:0160110-2), because the preprint describes the transition-zone doublet as a structurally independent segment from the axonemal doublet.
- Calcium ion binding was kept as ACCEPT and remains a core property. The structural model places the EF-hands away from tubulin, and calcium regulation is untested.
- The description was rewritten to lead with the ciliary MIP role and to describe the FEVR/adipogenesis data as genetic phenotypes without a known mechanism.

Not added (deliberately): MGI annotates mouse Capsl with IMP terms from PMID:39264149 (angiogenesis, vasculogenesis, endothelial cell migration and proliferation, retina development, gene expression). Human GOA has no counterpart. These are loss-of-function phenotypes with an unknown mechanism (MYC protein is lowered, but MYC mRNA is not), so they are not added as human process participation. The question is raised in suggested_questions instead.

Relative for next review: mouse Capsl (Q6P8Y1), an ortholog in the same SF5 subfamily with MGI IMP annotations. The repo has no review for it (no genes/mouse/Capsl).

Modules: no module in modules/ references CAPSL or Q8WWF8, and there is no gocams/index.tsv entry.
