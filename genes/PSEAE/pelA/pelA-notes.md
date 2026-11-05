# pelA (PA3064, Q9HZE4) notes

## Identity

- PelA, 948 aa, multidomain periplasmic Pel-modification enzyme: N-terminal
  GH166 (GH114-like TIM-barrel, Pfam PF03537, residues 68-296) glycoside
  hydrolase domain and a C-terminal CE21 carbohydrate esterase (deacetylase)
  domain (residues 520-804). Unreviewed TrEMBL entry with no curated comments.
  PANTHER PTHR35882 "PELA". First gene of the pelA-pelG operon.
- No deep-research provider was available; notes are from cached publications
  and PubMed searches.

## Literature

- PseudoCAP seed paper (Colvin et al. 2013, full text): purified PelA hydrolyses
  the pseudosubstrate p-nitrophenyl acetate; active-site point mutants lose
  activity and Pel-dependent biofilm/wrinkly colonies
  [PMID:23504011 "We first established that purified recombinant PelA hydrolyzed the pseudosubstrate p -nitrophenyl acetate in vitro , and site-specific mutations of predicted deacetylase active-site residues reduced activity greater than 10-fold."];
  [PMID:23504011 "PA14Δ pelA formed significantly reduced biofilms compared to the parental strain and, likewise, each point mutant was comparably impaired ( Fig."];
  fractionation places PelA in periplasmic and membrane fractions
  [PMID:23504011 "We found that PelA localized to both the periplasmic and membrane fractions but not to the cytoplasm."].
- PelA-PelB complex: the PelB TPR domain binds PelA directly in the periplasm,
  raising deacetylase and lowering hydrolase activity
  [PMID:28972168 "Copurification experiments indicated that the interaction between PelA and PelB is direct and that the deacetylase activity of PelA increases and its hydrolase activity decreases when these proteins interact."].
- Structure (2025): Pel is a partially deacetylated alpha-1,4 GalNAc polymer;
  PelA deacetylates and hydrolyses it before export; the deacetylase domain
  founds carbohydrate esterase family CE21; the hydrolase domain is an
  endo-alpha-1,4-N-acetylgalactosaminidase
  [PMID:40120681 "After synthesis and transport of the GalNAc polysaccharide across the inner membrane, PelA partially deacetylates and hydrolyzes Pel before its export out of the cell via PelB."];
  [PMID:40120681 "Characterization of the deacetylase domain revealed that PelA is the founding member of a new carbohydrate esterase family, CE21."];
  [PMID:40120681 "The deacetylase domain of PaPelA (residues 520–804) has previously been predicted to have structural similarity to CE4 enzymes (18, 33)."].

## Interpretation

The specific MF is GO:0047375 N-acetylgalactosaminoglycan deacetylase activity
(is_a deacetylase activity): PelA removes acetyl groups from GalNAc in the Pel
polymer and from alpha-1,4-GalNAc oligosaccharides. The hydrolase activity on
alpha-1,4-GalNAc has no exact GO term (GO:0033931 endogalactosaminidase is for
deacetylated poly-GalN), so it is raised as a question rather than annotated.
Biofilm formation is a downstream outcome of Pel production.

## Node leaf check (PTN002441861)

UniProt records of the other two leaves (retrieved 2026-10-28 via UniProt REST):

| leaf | organism | length | domains |
|---|---|---|---|
| Q9HZE4 PelA | P. aeruginosa PAO1 | 948 aa | GH114 TIM barrel (68-296) + CE21 deacetylase (520-804) |
| B8DZ50 Dtur_0372 | Dictyoglomus turgidum | 518 aa | GH114 TIM barrel (51-259) + CARDB (432-514) |
| Q9RWG2 DR_0706 | Deinococcus radiodurans | 252 aa | TIM barrel only |

Neither non-Pseudomonas leaf is long enough to contain the 520-804 deacetylase
domain, so the deacetylase IBD at this node is attached to a family defined by
the hydrolase domain. Domain mapping was from UniProt/InterPro features only, not
an alignment.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN002441861 | GO:0019213 deacetylase activity | 1 (sole seed) | 3 (3 taxa) | GO:0019213 deacetylase activity, IDA, PMID:23504011 (PseudoCAP) | SOUND | Direct assay of purified PelA (pNP-acetate esterase activity lost in active-site mutants), later confirmed on GalNAc oligosaccharides (PMID:40120681). The seed is sound for PelA. The node term does not suit the clade: the two other leaves (Dictyoglomus B8DZ50, 518 aa; Deinococcus Q9RWG2, 252 aa) contain only the GH114-like hydrolase domain and lack the CE21 deacetylase domain (PelA residues 520-804), so they cannot inherit the activity. A GO_CENTRAL defect asks for the IBD to be restricted to deacetylase-domain-containing PelA orthologs. |

## Decisions summary

- MODIFY: deacetylase activity (IBA, IDA) -> N-acetylgalactosaminoglycan
  deacetylase activity (GO:0047375); carbohydrate metabolic process (IEA) ->
  polysaccharide biosynthetic process.
- ACCEPT: polysaccharide biosynthetic process (TAS).
- KEEP_AS_NON_CORE: single-species biofilm formation (IMP).
- NEW: periplasmic space (IDA, PMID:23504011).
- GO_CENTRAL defect (PROBABLE): deacetylase IBD on leaves lacking the domain.
- No PSEUDOCAP defect.
