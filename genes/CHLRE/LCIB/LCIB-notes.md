# LCIB (Chlamydomonas reinhardtii, UniProt Q75NZ2) - curation notes

## Provenance of this review

- 2026-10-03: GOA file for Q75NZ2 is empty (header only). There are no existing
  GO annotations to review; all entries in `existing_annotations` are `NEW`.
- Deep research was not run. The falcon provider currently returns HTTP 402
  and perplexity is unavailable, so no `-deep-research-*.md` file exists. The
  literature below was found by PubMed esearch ("LCIB AND Chlamydomonas",
  "pmp1 AND Chlamydomonas", "ad1 AND air-dier") and cached with
  `ai-gene-review fetch-pmid`.
- Jin et al. 2016 (PMID:27911826) is abstract-only in the cache. I read the full
  text at PMC5187666 to check which LCIB homologs had CA activity (see below).
  Those full-text statements cannot be quoted as `supporting_text` because the
  cached file has only the abstract; they are described in review text instead.

## Identity

- UniProt Q75NZ2 (TrEMBL, 448 aa, gene name LciB), Pfam PF18599 LCIB_C_CA,
  InterPro IPR040703 (LCIB/C_CA), PANTHER PTHR38016:SF1.
- LCIB is the gene mutated in the classical air-dier mutants pmp1 and ad1
  [PMID:16777959 "Molecular analyses revealed that the Ad1/Pmp1 protein is encoded by LciB, a gene previously identified as a CO(2)-responsive gene."]
- Air-dier phenotype: dies at air CO2 but grows at high and very low CO2
  [PMID:16777959 "we identified and characterized a pmp1 allelic mutant, air dier 1 (ad1) that, like pmp1, cannot grow in low CO(2) (350 ppm) but can grow either in high CO(2) (5% CO(2)) or in very low CO(2) (<200 ppm)."]
- Small family of four related soluble plastid proteins (LCIB, LCIC, LCID, LCIE)
  [PMID:16777959 "LciB and three related genes in C. reinhardtii compose a unique gene family that encode four closely related, apparently soluble plastid proteins with no clearly identifiable conserved motifs."]
- Strongly induced at low CO2 under CCM1 control (PMID:15235119, the paper that
  deposited the AB168093 cDNA).

## Complex with LCIC

- [PMID:20660228 "we provide evidence to demonstrate that LCIB interacts with the LCIB homologous protein LCIC in yeast and in vivo."]
- [PMID:20660228 "We also show that LCIB and LCIC are co-localized in the vicinity of the pyrenoid under LC conditions in the light, forming a hexamer complex of approximately 350 kDa, as estimated by gel filtration chromatography."]
- Loss of LCIB destabilises LCIC: [PMID:34791500 "In B3 cells, LCIC (49 kDa), the interacting protein of LCIB (48 kDa), was also hardly detected as with the previously reported LCIB RNAi strains"]
- Jin et al. (full text, PMC5187666) found that co-expressed recombinant LCIB and
  LCIC form a ~440 kDa complex at 1:1 stoichiometry, whereas mixing separately
  purified proteins did not reconstitute it; LCIB alone forms a ~390 kDa
  homo-oligomer and LCIC alone a dimer.
- LCIB, LCIC and EPYC1 co-occur in the Mackinder spatial interactome
  [PMID:28938113 "EPYC1, LCIB and LCIC (Figure 5F)."]

## Localization

- Chloroplast stroma, soluble; under very low CO2 it relocates to a ring around
  the pyrenoid, outside the starch sheath.
  [PMID:34791500 "LC-inducible protein B (LCIB), structurally characterized as carbonic anhydrase, localizes in the chloroplast stroma under CO2-supplied and LC conditions."]
  [PMID:34791500 "In VLC conditions, it migrates to aggregate around the pyrenoid, where the CO2-fixing enzyme ribulose 1,5-bisphosphate carboxylase/oxygenase is enriched."]
- Relocation requires LCIC and is switched at ~7 uM CO2
  [PMID:34791500 "These results suggest that the localization changes of LCIB require LCIC and are controlled by CO2 concentration with ∼7 µM as the boundary."]
- Light and low-CO2 dependent; diffuses away in the dark or at high CO2
  [PMID:20660228 "In contrast, in the dark or under high-CO2 conditions when the CCM was inactive, LCIB immediately diffused away from the pyrenoid."]
  Note that Yamano et al. 2022 later found that relocation at very low CO2 can
  happen in the dark (PMID:34791500 abstract), so the light requirement depends
  on CO2 level.
- Starch sheath is required for peripheral localization
  [PMID:32041908 "These results suggest that the starch sheath around the pyrenoid is required for the correct localization of LCIB and for the operation of CCM."]
  and LCIB itself has no starch-binding domain
  [PMID:32041908 "Because LCIB and LCIC do not have a starch-binding domain and exist as soluble proteins in the chloroplast stroma"]
- Mislocalisation mutants (abl) have CCM defects
  [PMID:24384670 "abl-1 and abl-3 with dispersed and speckled localization of LCIB in the chloroplast showed significant decreases in Ci affinity, Ci accumulation, and CO2 fixation."]
- Decision: location = GO:0009570 chloroplast stroma. I do NOT use GO:1990732
  pyrenoid: LCIB sits outside the starch sheath around the matrix, not in the
  Rubisco matrix.

## Molecular function: carbonic anhydrase (beta-CA fold) - with caveats

- Structure: Jin et al. 2016 solved CrLCIB and CrLCIC structures with
  beta-CA-like zinc sites
  [PMID:27911826 "We determined the crystal structures of LCIB and limiting CO2-inducible C protein (LCIC) from C. reinhardtii and a CA-functional homolog from Phaeodactylum tricornutum, all of which harbor motifs bearing close resemblance to the active site of canonical β-CAs."]
  [PMID:27911826 "Three of the six homologs are functional carbonic anhydrases (CAs)."]
- **Careful: the three CA-active homologs were NOT the Chlamydomonas proteins.**
  Full text (PMC5187666): "PtLCIB3, PtLCIB4, and FjLCIB exhibited diverse levels
  of CA activity ... whereas CsLCIB, CrLCIB, CrLCIC, recombinant CrLCIB-LCIC
  complex, and native CrLCIB-LCIC complex were inactive under all conditions
  tested". The zinc site (Cys120, His180, Cys204 in CrLCIB) is present, but the
  loop carrying the catalytic His162/Arg194 equivalents is disordered, and an
  Arg at the position of PtLCIB4 Ser47 (Arg121) restricts dimer gap closure;
  back-mutation R121S did not restore activity. The authors proposed a tightly
  regulated CA in Chlamydomonas.
- Heterologous complementation (Kasili et al. 2023):
  [PMID:36856938 "Although both LCIB and LCIC are structurally similar to βCAs, their CA activity has not been demonstrated to date."]
  [PMID:36856938 "We provide evidence that LCIB is an active CA using a Saccharomyces cerevisiae CA knockout mutant (∆NCE103) and an Arabidopsis thaliana βCA5 knockout mutant (βca5)."]
  [PMID:36856938 "We show that different truncated versions of the LCIB protein complement ∆NCE103, while the full length LCIB protein complements βca5 plants, so that both the yeast and plant mutants can grow in low CO2 conditions."]
  Abstract-only in cache. This is a genetic (complementation) argument, IGI.
- Tobacco stromal expression raises total leaf CA activity (Barsoum et al. 2026)
  [PMID:42328090 "LCIB was exclusively localized in the stroma and remained biologically active, leading to a ~3-fold increase in total carbonic anhydrase activity and a lower apparent CO2 compensation point (-10%)."]
  [PMID:42328090 "Leaf extracts from LB-3 and LB-6 lines showed significantly higher total carbonic anhydrase activity than wild-type and vector controls."]
  Caveat: a crude-extract measurement; could include indirect effects on
  endogenous CAs, but consistent with intrinsic activity.
- Wang & Spalding review (2014) predates the structure and calls LCIB motif-less
  [PMID:24307449 "LCIB, which has been demonstrated as a key player in the eukaryotic algal CO2-concentrating mechanism (CCM), is a novel protein in Chlamydomonas lacking any recognizable domain or motif, and its exact function in the CCM has not been clearly defined."]
- Decision: GO:0004089 carbonate dehydratase activity is supported for LCIB by
  two independent heterologous gain-of-function assays (yeast, Arabidopsis)
  plus increased CA activity in tobacco, and by a beta-CA zinc site in the
  crystal structure. Direct in-vitro CA activity of purified CrLCIB or of the
  native LCIB-LCIC complex has NOT been shown (Jin 2016 negative). I assert it
  as `molecular_function` (LCIB alone complements, so it is not only a
  contributes_to relationship) but flag the in vitro discrepancy in the review
  and in suggested experiments.

## Physiological role: CO2 recapture / CO2 uptake into stromal Ci pool

- Genetic placement downstream of CAH3
  [PMID:19074623 "We conclude that LCIB functions downstream of CAH3 in the CO2-concentrating mechanism and probably plays a role in trapping CO2 released by CAH3 dehydration of accumulated Ci."]
- Suppressor screen
  [PMID:21409559 "is proposed to play a role in trapping CO(2) released by CAH3 (thylakoid lumen carbonic anhydrase) catalyzed dehydration of accumulated Ci, especially in low CO(2) (L-CO(2); ~0.04% CO(2)) conditions."]
- Distinct from LCIA bicarbonate uptake
  [PMID:25336519 "Although both LCIA and LCIB are essential for very low CO2 acclimation, LCIB appears to function in a CO2 uptake system, whereas LCIA appears to be associated with a HCO3(-) transport system."]
- HLA3 knockdown in lcib background
  [PMID:19321421 "Collectively, the data presented here provide compelling evidence that HLA3 is directly or indirectly involved in HCO 3 − transport, along with additional evidence supporting a role for LCIA in chloroplast envelope HCO 3 − transport and a role for LCIB in chloroplast Ci accumulation."]
- Modelling (Fei et al. 2022) treats LCIB/LCIC as the stromal CA that converts
  CO2 to bicarbonate, and its pyrenoid-peripheral relocation as reducing leakage
  [PMID:35596080 "Consequently, LCIB relocalized near the starch sheath increases energy efficiency by recapturing CO2 molecules that diffuse out of the matrix and trapping them as HCO3− in the chloroplast (Fig."]

## GO biological process

- GO has no "CO2-concentrating mechanism" process term (searched "carbon
  concentrat", "carbon dioxide"; only transport/response/detection terms).
  I do not propose a NEW BP. "response to carbon dioxide" would describe the
  induction of LCIB expression rather than LCIB's work. Raised as a question.

## Complex

- No GO cellular component term for the LCIB-LCIC complex. Proposed as a new
  term; `in_complex` left unset because the field requires a GO complex id.

## Module assertion check (modules/pyrenoid_ccm.yaml, annoton lcib_lcic_ca)

- carbonate dehydratase activity GO:0004089: supported (complementation,
  structure), with the caveat that purified Chlamydomonas protein/complex was
  inactive in vitro (Jin 2016). The module text "CA activity of the
  Chlamydomonas complex itself has not been robustly measured in vitro" is
  accurate. The evidence statement for PMID:27911826 ("several LCIB-family
  homologs are functional CAs") is also accurate, but readers should know that
  the CA-active homologs were diatom/bacterial, not CrLCIB/CrLCIC.
- chloroplast stroma GO:0009570: supported.
