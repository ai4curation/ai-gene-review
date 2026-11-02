# MYH8 (human, P13535) curation notes

## Gene identity

MYH8 encodes myosin-8, the perinatal (neonatal) skeletal muscle myosin heavy chain
(MyHC-perinatal, MyHC-neo), a 1937-residue class II sarcomeric myosin. UniProt domain layout:
SH3-like N-terminal domain (35-84), motor domain (88-781) with the ATP-binding P-loop (181-188)
and actin-binding regions (658-680, 760-774), an IQ region (781-813), and a coiled-coil rod
(842-1937) with 28-residue repeats [file:human/MYH8/MYH8-uniprot.txt "The rodlike tail sequence
is highly repetitive, showing cycles of a 28-residue repeat pattern composed of 4 heptapeptides,
characteristic for alpha-helical coiled coils."].

- Complex: hexamer of 2 heavy chains, 2 essential and 2 regulatory light chains (UniProt SUBUNIT).
- Location: [file:human/MYH8/MYH8-uniprot.txt "Cytoplasm, myofibril. Note=Thick filaments of the
  myofibrils."]; sarcomeric MyHCs are defined by a rod that allows thick filament formation
  [PMID:26970499 "a family can be identified as sarcomeric based on their molecular structure which
  allows thick filament formation"].

## Expression

- Cloned as a developmentally regulated sarcomeric MHC; high in 21-week fetal skeletal muscle,
  absent from fetal heart, persists at lower levels in adult skeletal muscle [PMID:2715179 "the mRNA
  encoding this isoform is expressed at high levels in 21-wk fetal skeletal tissue and not in fetal
  cardiac muscle"]. Head (S1) cDNA and full-length construct [PMID:2373371].
- Review of developmental myosins [PMID:26180627 "Developing skeletal muscles express unique myosin
  isoforms, including embryonic and neonatal myosin heavy chains, coded by the myosin heavy chain 3
  (MYH3) and MYH8 genes, respectively"; "developmental myosins persist throughout adult stages in
  specialized muscles, such as the extraocular and jaw-closing muscles, and in the intrafusal fibers
  of the muscle spindles"]. Neonatal myosin predominates at birth and is replaced by adult fast
  isoforms; re-expressed in regenerating fibres.
- All 10 sarcomeric isoforms, including NEO, detected in human extraocular muscle [PMID:26970499].
- Used as a myotube differentiation marker in cultured human satellite cells [PMID:21370490].

## Motor function (recombinant protein)

- First recombinant analysis of all human skeletal isoforms [PMID:20080549 "the developmental
  MyHC-Perinatal, with a similar V max as MyHC-IIa, has a very similar maximal motility velocity";
  "MyHC-Perinatal displays a slightly higher ATPase profile than MyHC-Embryonic"].
- Transient kinetics [PMID:31387944 "The perinatal is distinct from the embryonic isoform, appearing to
  have features in common with the adult fast-muscle isoforms, including weak affinity of ADP for
  actin·myosin and fast ADP release."].
- Single molecule [PMID:38377203 "WT perinatal and embryonic myosins had the highest powers due to a
  combination of large step sizes and fast kinetics."].
- Fibre-level: neonatal-rich fibres are slow-like [PMID:26180627 "Fibers expressing predominantly
  neonatal myosin show values of shortening velocity and ATPase activity comparable to slow fibers and
  much lower than fast 2X and 2B fibers"]. So no fibre-type-specific contraction term is warranted;
  `skeletal muscle contraction` is the right level.

## Disease (context, not GO annotation)

- Recurrent dominant R674Q causes trismus-pseudocamptodactyly syndrome (TPS, Dutch-Kentucky, DA7)
  [PMID:17041932 "All four TPS families shared the p.R674Q substitution."]; originally found with a
  Carney complex variant [PMID:15282353 "Arg674 is highly conserved evolutionarily, localizes to the
  actin-binding domain of the perinatal myosin head, and is close to the ATP-binding site."]. Toydemir
  et al. found no Carney features in their TPS families and no R674Q in 49 Carney complex cases.
- R674Q impairs the motor [PMID:38377203 "The mutations in the developmental myosins dramatically
  decreased the step size and load-sensitive actin-detachment rate of single molecules measured by
  optical tweezers, in addition to decreasing overall enzymatic (ATPase) cycle rate."].
- Heterozygous LoF variants do not cause TPS [PMID:28377322 "loss-of-function variants in the MYH8
  gene do not cause autosomal dominant trismus-pseudocamptodactyly syndrome"], consistent with an
  altered-function/dominant-negative mechanism.
- Mouse knockdown reports altered differentiation/metabolism/regeneration [PMID:38358038]; treated as
  indirect effects, not used for GO process terms (consistent with MYH7, where disease/phenotype data
  were not turned into developmental process terms).

## Annotation decisions (consistent with MYH7)

- Locations (cytoplasm, cytosol x4, myofibril, contractile muscle fiber, sarcomere, myosin filament)
  -> MODIFY to GO:0005863 striated muscle myosin thick filament.
- myosin complex / myosin II complex -> MODIFY to GO:0005859 muscle myosin complex; GO:0005859 NAS
  ACCEPT.
- cytoskeletal motor activity -> MODIFY to GO:0000146; GO:0000146 IBA/IMP ACCEPT.
- muscle contraction (IBA, NAS) and system process (ARBA) -> MODIFY to GO:0003009 skeletal muscle
  contraction; GO:0003009 IMP ACCEPT.
- ATP binding (IEA, IMP), ATP hydrolysis activity (IMP; GO term note asks for an accompanying
  ATP-dependent activity child, which is present), actin filament binding x3, muscle filament sliding
  x2, structural constituent of muscle -> ACCEPT.
- myosin light chain binding -> KEEP_AS_NON_CORE.
- ATP metabolic process (IMP) -> MARK_AS_OVER_ANNOTATED (as MYH7).
- myosin phosphatase activity (Reactome TAS, attached to "ATP hydrolysis by myosin") -> REMOVE:
  GO:0017018 is phosphomyosin dephosphorylation, which the heavy chain does not catalyse.

## Deep research

- openscientist run completed 2026-10-16 (`MYH8-deep-research-openscientist.md`, 14 citations);
  falcon was not used because its Edison authentication was failing that day.
- The report's identity checks and overall picture (perinatal skeletal MyHC; actin-activated ATPase
  motor; thick filament; developmental, regeneration and masseter expression; R674Q in TPS) agree
  with the review.
- Two of its stated limitations are out of date and were not adopted: it says no isoform-specific
  kinetics exist for human perinatal myosin and that the R674Q biophysical defect is unresolved. Both
  are addressed by recombinant studies cited here (PMID:20080549, PMID:31387944, PMID:38377203).
- Its mechanistic citations for the motor and filament assembly are generic myosin II papers
  (Dictyostelium, truncated head assays, cardiac MHC acetylation); MYH8-specific evidence above was
  preferred.
- Its "regulatory role in differentiation and oxidative phenotype" (PMID:38358038) was not turned
  into GO process terms: those knockdown effects are plausibly indirect consequences of disturbing
  the contractile apparatus, the same reasoning used for MYH7 disease phenotypes.
