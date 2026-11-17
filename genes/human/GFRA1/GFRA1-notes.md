# GFRA1 notes

## Deep research
- `just deep-research-falcon human GFRA1 --fallback perplexity-lite` failed (providers unavailable,
  2026-10-21). Notes from cached publications and UniProt P56159.

## Function
- GPI-anchored GDNF co-receptor. GDNFR-alpha is "a novel glycosylphosphatidylinositol-linked cell surface
  receptor for glial cell line-derived neurotrophic factor (GDNF)" that "binds GDNF specifically and mediates
  activation of the Ret protein-tyrosine kinase (PTK)" [PMID:8674117].
- Soluble GDNFR-alpha can activate RET in trans in cells lacking it [PMID:8674117].
- High-affinity GDNF binding requires cRET co-expression; suggests GFRA1-RET pre-association [PMID:10829012].
- Cryo-EM: GDNF/GFRα1/RET 2:2:2 complex; ligand/co-receptor pairs induce RET dimerization for
  trans-autophosphorylation [PMID:31535977].
- SORL1 binding drives GFRA1 internalization to TGN, endosomes, MVBs (UniProt, by similarity to rat).
- Disease: biallelic variants cause renal hypodysplasia/aplasia 4 (bilateral renal agenesis) [UniProt].
- Not a major HSCR gene [PMID:9545641].

## Localization
- Signal peptide 1-24; GPI-anchor at Ser429; C-terminal propeptide removed. Outer leaflet / external side of
  plasma membrane, cell surface; also soluble released form; SORL1-dependent endosomal pool.
- Conclusion: PM outer leaflet (GPI-anchored, entirely extracellular), with endosomal/TGN pools.

## 2026-11-15 ORGANELLES Golgi batch 2 (Golgi apparatus rows)

- One Golgi row: IEA GO_REF:0000044. The human UniProt item "Golgi apparatus, trans-Golgi
  network" is ECO:0000250 from rat Q62997 (taxon 10116), where the same item is ECO:0000269
  from PMID:23333276 (Glerup et al. 2013, Cell Rep; checked in the live rat UniProt entry).
- PMID:23333276 is abstract-only in the cache, has no PMCID, and the publisher site
  (cell.com / sciencedirect, PII S221112471200455X) returned 403, so the TGN marker, cell type
  and whether SORL1/GFRA1 were overexpressed could not be checked.
- Verdict: KEEP_AS_NON_CORE -> UNDECIDED under the unreadable-donor rule (CD247); readings set
  out in the reason (SORL1-dependent recycling stop vs co-transfection perturbation pool). No
  trans-Golgi network row. The description sentence about SORL1 diverting GFRA1 to the TGN was
  left unchanged (outside the Golgi rows); it rests on the same unverified source.
