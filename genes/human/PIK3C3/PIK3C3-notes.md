# PIK3C3 notes

- PIK3C3 encodes VPS34, the catalytic lipid kinase of the human class III PI3K system, and the core molecular-function claim should stay at specific phosphatidylinositol 3-kinase activity rather than generic kinase terms [PMID:7628435 A human phosphatidylinositol 3-kinase complex related to the yeast Vps34p-Vps15p protein sorting system., "PtdIns 3-kinase does not associate with p85 and phosphorylates PtdIns, but not PtdIns4P or PtdIns(4,5)P2."].
- The strongest PN-supported core case is macroautophagy initiation through PI3KC3-C1/type I, which contains VPS34 with VPS15, BECN1, and ATG14 and acts at the earliest autophagy stages [PMID:40442316 Structure and activation of the human autophagy-initiating ULK1C:PI3KC3-C1 supercomplex., "All forms of canonical autophagy, bulk and selective, are initiated upon the recruitment and activation of the FIP200 protein4 and the class III phosphatidylinositol 3-OH kinase complex I (PI3KC3-C1)5–7."] [PMID:40442316 Structure and activation of the human autophagy-initiating ULK1C:PI3KC3-C1 supercomplex., "PI3KC3-C1 contains one copy each of the lipid kinase VPS34, the pseudokinase VPS15 and the regulatory subunits BECN1 and ATG14."].
- PI3P production is the key process-level output shared across VPS34 deployments and directly underpins autophagosome formation and maturation, which makes `GO:0036092` a better process term than broad phosphatidylinositol-phosphate biosynthesis [PMID:33637724 VPS34 K29/K48 branched ubiquitination governed by UBE3C and TRABID regulates autophagy, proteostasis and liver metabolism., "This complex catalyzes the production of PI3P and is required for both bulk and selective types of autophagy by controlling both autophagosome formation and maturation."].
- Human data also support a UVRAG-containing PI3KC3-C2/type II complex linked to endosomal sorting and later autophagy-associated trafficking, but this should be kept contextual rather than core in the PN framing [PMID:40442316 Structure and activation of the human autophagy-initiating ULK1C:PI3KC3-C1 supercomplex., "The former three subunits are also present in PI3KC3-C2 involved in endosomal sorting and late steps in autophagy, while ATG14 is uniquely involved in autophagy initiation."].
- Endosomal trafficking and cytokinesis are supported human roles for VPS34 complexes, but they should remain non-core relative to the autophagy-initiation case [PMID:14617358 Human VPS34 and p150 are Rab7 interacting partners., "The hVPS34/p150 complex colocalized with rab7 on late endosomes and hVPS34 activity was dependent on nucleotide cycling of rab7."] [PMID:20208530 PtdIns(3)P controls cytokinesis through KIF13A-mediated recruitment of FYVE-CENT to the midbody., "Depletion of the VPS34 or Beclin 1 subunits of PI(3)K-III causes cytokinesis arrest and an increased number of binucleate and multinucleate cells, in a similar manner to the depletion of FYVE-CENT, KIF13A or TTC19."] [PMID:20643123 A phosphatidylinositol 3-kinase class III sub-complex containing VPS15, VPS34, Beclin 1, UVRAG and BIF-1 regulates cytokinesis and degradative endocytic traffic., "High-content microscopy-based assays combined with siRNA-mediated depletion of individual subunits indicated that a specific sub-complex containing VPS15, VPS34, Beclin 1, UVRAG and BIF-1 regulates both receptor degradation and cytokinesis, whereas ATG14L, a PI3K-III subunit involved in autophagy, is not required."].
- Broad membrane proteomics is too weak to retain as a meaningful PIK3C3 localization assertion in the review [PMID:19946888 Defining the membrane proteome of NK cells., "The remaining species were largely involved in cellular processes and molecular functions that could be predicted to be transiently associated with membranes."].

## Description cleanup note

The YAML `description` field was revised to keep it as a standalone biological summary. Project-specific curation framing moved here instead.

- Moved out of the YAML description: the Proteostasis Network context emphasized the autophagy-initiation complex and macroautophagy as central core claims, with endosomal trafficking and cytokinesis as supported contextual extensions.


## 2026-09-20 IBA re-review

Restored membrane and endosomal/type-II-complex annotations as core; added endosomal lipid-kinase core synthesis. Separated pexophagy from peroxisomal localization for adjudication; withdrew unsupported abstract-only and untraced context exclusions. Corrected generic protein-binding action semantics.

Evidence inspected: [PMID:14617358](https://pubmed.ncbi.nlm.nih.gov/14617358/), [PMID:20643123](https://pubmed.ncbi.nlm.nih.gov/20643123/), [PMID:40442316](https://pubmed.ncbi.nlm.nih.gov/40442316/), [PMID:17307798](https://pubmed.ncbi.nlm.nih.gov/17307798/), [PMID:25327288](https://pubmed.ncbi.nlm.nih.gov/25327288/).

Remaining questions:

- Pexophagy participation and peroxisome residence assessed separately (OpenScientist running).
- Second opinion on GO:0006897 uptake-step participation versus the directly established post-uptake trafficking role.
- Recover specific neuronal/nutrient ortholog evidence and full text for PMID:17307798 and PMID:25327288 localization claims.

The project audit records all changed row indices and decisions in `projects/IBA_REVIEW/rereview-2026-09-20/localization.yaml`.


## 2026-09-20 recovered pexophagy report and primary check

Recovered and assessed the exact OpenScientist final report from a cancelled job via its artifact bundle (see hypothesis recovery-provenance.json). Pexophagy is retained as a conserved conditional process. Catalytic PI3P production is execution work. Full Grunau PMID:21121900 confirms peroxisome association under biogenesis conditions, disproving the report’s proposed cargo-confusion explanation; other locations do not exclude it. Human peroxisome localization remains UNDECIDED, with no further provider job pending. See the primary-check note for methods and limits.


## Recovery review consistency follow-up (2026-09-22)

Restored readable identifiers in manual prose. Where applicable, reconciled AP3M2 reference notes with the retained contextual claim, removed unrelated PIK3C3 support from unresolved projections, separated PIK3C3 aspect-specific reasons, and documented the surviving/renamed ATG14 membrane term. Source assertion fields and verbatim quotations are unchanged.
