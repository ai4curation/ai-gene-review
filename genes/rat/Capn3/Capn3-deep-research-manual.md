# Capn3 (rat, P16259) - manual literature synthesis

No deep-research API was available for this session. This file was written by hand from the
cached publications in `publications/`, the UniProt record (`Capn3-uniprot.txt`) and PubMed
searches. Each assertion carries its source.

## Identity

- Rat Capn3 (calpain-3, p94; RGD:2269; GeneID 29155), UniProt P16259, 821 aa. The rat cDNA was
  cloned with the human one in the original description of p94 [PMID:2555341 "a cDNA clone encoding a
  novel member of the CANP large subunit family was obtained"; "the mRNA for p94 exists only in skeletal
  muscle with none detected in other tissues including heart muscle and smooth muscles"].
- Domain organisation: calpain catalytic domain (74-417) with active-site residues C129, H334, N358,
  domain III (418-586), linker, and a penta-EF-hand domain IV (650-820) with Ca2+-binding residues
  (UniProt FT records, PROSITE-ProRule). Unique insertions NS, IS1 and IS2 [PMID:2555341 "p94 contains
  two unique sequences of 62 and 77 residues in domains II and III, respectively"].
- Family: peptidase C2 family (calpain), MEROPS C02.004, PANTHER PTHR10183:SF329 (CALPAIN-3).

## Catalytic activity and autolysis

- Calcium-activated cysteine endopeptidase. Rat recombinant Lp82, a lens splice variant of Capn3,
  autolyzes with calcium and has caseinolytic activity [PMID:11904300 "After incubation with calcium,
  rLp82 autolyzed into two major fragments at approximately 60 and 22 kDa"; "Lp82 also hydrolyzed
  calpastatin"].
- Disease mutants lose substrate proteolysis [PMID:9642272 "All mutants completely or almost completely
  lose the proteolytic activity against a potential substrate, fodrin"].
- Autolysis of the protease core is intramolecular and Ca2+-dependent [PMID:12482600 "Ca2+-dependent
  autolysis must be an intramolecular event"].
- Endogenous rat calpain-3 in skinned single fibres is tightly bound and autolyzes only when resting
  [Ca2+] is raised slightly [PMID:19144634 "Calpain-3 autolyzes (becoming proteolytically active) in a
  tightly calcium-dependent manner"; "Virtually all calpain-3 present in mature muscle fibers is tightly
  bound in the vicinity of the titin N2A line and triad junctions"].
- Substrates shown in vitro or in cells: filamin C C-terminus [PMID:14506720 "C3 cleaves the C-terminal
  portion of FLNC"], titin and MARP2/Ankrd2 [PMID:18310072 "MARP2/Ankrd2 competed with p94 for binding to
  connectin and was also proteolyzed by p94"], aldolase A on co-expression though not in vivo
  [PMID:18676612 "In co-expression studies CAPN3 degraded AldoA"], MyoD [PMID:20139084].

## Sodium dependence (disputed)

- Ono et al. 2010 report Na+-dependent autolysis in the absence of Ca2+, using partially purified rat
  wild-type p94 among other preparations [PMID:20460380 "underwent Na(+)-dependent, but not
  Cs(+)-dependent, autolysis in the absence of Ca(2+)"; "a conserved Ca(2+)-binding sequence in the
  protease acted as a Na(+) sensor"; "the [Na+] required for half-maximal autolytic activity was 15 mm at
  [Ca2+] = 100 nm"].
- Wette et al. 2023 used rat and human muscle and confirm Na+-induced autolysis only if K+ is absent
  [PMID:37298357 "this only occurred if all K+ normally present in a muscle cell was absent, and it did not
  occur even in 36 mM Na+"]. Physiological Na+ activation is therefore disputed; the in vitro phenomenon
  is reproducible.

## Titin binding and localization

- p94 binds connectin/titin at the N2A, PEVK and M-line regions; N2A binding suppresses autolysis
  [PMID:18310072 "p94 binds to connectin at multiple sites"; "p94-N2A interactions suppress p94
  autolysis"].
- In rat fibres calpain-3 is bound within the contractile filament lattice and is not washed out with
  membranes [PMID:19144634 "Most calpain-3 is evidently bound within the contractile filament lattice"].
  After complete autolysis it becomes diffusible into the cytoplasm [PMID:37298357 "After it was
  autolysed, CAPN3 unbound from its tight binding on titin and became diffusible"].
- Rat brain astrocytes express calpain-3 protein [PMID:12663060 "Calpain 3 was almost exclusively found
  in cells displaying astrocyte morphology"].

## Non-proteolytic role at the triad/SR (mouse)

- CAPN3 is needed to recruit aldolase A to triads; calcium release is reduced in null fibres
  [PMID:18676612 "we found CAPN3 to be necessary for recruitment of AldoA to one specific location, namely
  the triads"].
- In C129S knock-in mice the inactive protein supports SR Ca2+ efflux [PMID:21295580 "calpain-3 functions
  as a nonenzymatic element for the Ca(2+) efflux machinery in the SR, rather than as a protease"].

## Myogenic cell state (mouse)

- CAPN3 promotes the reserve-cell (quiescent) pool by lowering MyoD activity [PMID:20139084 "calpain 3
  participates in the establishment of the pool of reserve cells by decreasing the transcriptional
  activity of the key myogenic regulator MyoD via proteolysis"].
- Null mice show disorganized sarcomeres [PMID:15138196 "Myogenic cells fused normally in vitro, but
  lacked well-organized sarcomeres"].

## Expression responses (rat)

- Capn3 mRNA changes during soleus regeneration after cryolesion and is blocked by cyclosporin A
  [PMID:15726428 "CsA treatment blocked calpain-3 gene expression rise induced by 10 days of
  cryolesion"]. This is an expression response, not evidence of a function.
