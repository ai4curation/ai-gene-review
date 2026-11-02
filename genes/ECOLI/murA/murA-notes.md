# murA (P0A749) – E. coli K-12 – curation notes

No deep-research file was generated for this gene; these notes are from the cached
publications (`publications/PMID_*.md`), the UniProt record and targeted web lookups.

## Identity and nomenclature

- murA (b3189; formerly murZ) encodes UDP-N-acetylglucosamine 1-carboxyvinyltransferase
  (UDP-GlcNAc enolpyruvyl transferase, EC 2.5.1.7), 419 aa, EPSP synthase family, MurA
  subfamily (HAMAP MF_00111; TIGR01072; PANTHER PTHR43783:SF1).
- Cloned by screening for clones conferring fosfomycin resistance; purified protein has
  the expected activity [PMID:1512209 "Identified by screening an E. coli genomic library for clones that conferred phosphomycin resistance"; "MurZ protein was purified to near homogeneity and found to have the expected UDP-N-acetylglucosamine enolpyruvyl transferase activity"].
- Essential, and the sole UDP-GlcNAc enolpyruvyl transferase of E. coli (unlike
  Gram-positives with MurAA/MurAB) [PMID:7608103 "We conclude that murZ is an essential gene and encodes the sole UDP-N-acetylglucosamine enolpyruvyl transferase of E. coli."].
- Historical note: the 1972 fosfomycin-resistant, temperature-sensitive "murA" mutant of
  Venkateswaran & Wu [PMID:4555418] mapped at 90 min, not at the 69.3 min murZ locus; Brown et
  al. 1995 explicitly flag this map discrepancy [PMID:7608103 "The map position of murZ (69.3 min) differed from that determined for murA (90 min), a gene which had been previously proposed to encode the same activity"]. The 1972 biochemistry (lower enzyme affinity for fosfomycin, reduced DAP incorporation) is consistent with an enolpyruvyl-transferase lesion, but the genetic identity of that allele is uncertain. Relevant to the IMP row from PMID:4555418.

## Reaction and mechanism

- PEP + UDP-GlcNAc -> UDP-GlcNAc-enolpyruvate + Pi; first committed step of
  peptidoglycan synthesis [PMID:8075064 "The MurZ enzyme catalyzes enolpyruvoyl transfer from phosphoenolpyruvate to the 3-OH of UDP-N-acetylglucosamine (UDP-GlcNAc) in Escherichia coli peptidoglycan biosynthesis."].
- Addition–elimination through a tetrahedral ketal intermediate; stereochemistry solved
  with C115A mutant [PMID:9485407 "catalyzes the enolpyruvyl transfer from phosphoenolpyruvate (PEP) to the 3'-OH of UDP-GlcNAc by an addition-elimination mechanism that proceeds through a tetrahedral ketal intermediate"].
- Covalent phospholactoyl (PEP–Cys115) adduct is kinetically competent
  [PMID:8075064 "the covalent enzyme-phospholactoyl adduct appeared and decayed on a time scale consistent with catalysis"].
- In Enterobacter cloacae MurA, PEP-Cys115 adduct plus bound UDP-MurNAc (MurB product)
  forms a "dormant" complex proposed to mediate feedback regulation [PMID:22378791 "tightening the complex with UNAM for the efficient feedback regulation of murein biosynthesis"]. E. cloacae, not E. coli; treated as family-level inference.

## Fosfomycin / Cys115 / UNAG

- Crystal structure of E. coli MurA with UNAG and fosfomycin: fosfomycin covalently on
  Cys115; UNAG bound between the two domains [PMID:8994972 "The fosfomycin molecule is covalently bound to the cysteine residue Cys115, whereas UDP-GlcNAc makes several hydrogen-bonding interactions with residues from both domains."].
- Terreic acid also alkylates Cys115; inactivation (like fosfomycin) requires UNAG; E. coli
  K-12 MurA was assayed [PMID:20392080 "terreic acid is a covalent inhibitor of the bacterial cell wall biosynthetic enzyme MurA from Enterobacter cloacae and Escherichia coli in vitro"; "Kinetic characterization established that the inactivation requires the presence of substrate UNAG"].
- UNAG-3-phosphate made by the PezT toxin competitively inhibits E. coli MurA
  (Ki 7 uM per UniProt) [PMID:21445328 "we were able to show that the phosphorylated product inhibits MurA, the enzyme responsible for the first step of peptidoglycan synthesis in bacteria"].

## Location

- Soluble cytosolic enzyme; detected in cytosolic fractions by proteomics
  [PMID:15911532 fractionation to "cytosol, periplasm, inner membrane, and outer membrane"]; [PMID:18304323 cytosol profiling].
  UniProt: "SUBCELLULAR LOCATION: Cytoplasm".

## Interactions (not modelled as GO terms)

- MurA binds LapB and the LPS/PL enzymes LpxA, LpxC, LpxD and FabZ (B2H + pull-downs);
  murA is a multicopy suppressor of lapB mutants; MurA is not a LapB/FtsH substrate
  [PMID:42604454 "MurA interacts not only with LapB but also with the LPS biosynthesis enzymes LpxA, LpxC, and LpxD as well as with the PL biosynthesis enzyme FabZ"]. Physical association only; no GO MF term is warranted (bare protein binding policy). Kept as a suggested question.

## Annotation decisions (summary)

- GO:0008760 (all rows): ACCEPT – core MF.
- GO:0009252: ACCEPT (IBA, IEA, IMP) – core BP.
- GO:0005829 cytosol: ACCEPT; GO:0005737 cytoplasm: MODIFY -> cytosol.
- GO:0003824, GO:0016765: TOO_GENERAL (entailed by GO:0008760).
- GO:0019277 UDP-GalNAc biosynthesis: REMOVE – InterPro2GO mis-mapping; MurA consumes UDP-GlcNAc and makes no UDP-GalNAc.
- UniProt keywords "Cell division", "Cell shape" have not been propagated to GOA rows for murA; no NEW rows proposed for them (over-annotation for a precursor enzyme).
