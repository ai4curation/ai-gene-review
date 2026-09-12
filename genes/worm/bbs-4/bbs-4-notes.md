# bbs-4 (C. elegans) research notes

UniProt: Q5CZ52 (BBS4_CAEEL). WormBase: WBGene00043992 / F58A4.14. 462 aa.
Gene: bbs-4 (Bardet-Biedl syndrome 4 protein homolog / "BBSome complex member bbs-4").

## Summary of gene identity

BBS-4 is a **core structural subunit of the BBSome**, the octameric complex (bbs-1, bbs-2,
bbs-4, bbs-5, osm-12/bbs-7, bbs-8/ttc-8, bbs-9) that couples intraflagellar transport (IFT)
to ciliary membrane-cargo trafficking. BBS-4 is a tetratricopeptide-repeat (TPR) protein
(UniProt annotates 7 TPR repeats spanning ~89–402, with a disordered N-terminal region
1–46). The BBSome shares structural features with the COPI/COPII/clathrin vesicle coats and
is thought to act as a membrane coat/cargo adaptor at cilia.

## KNOWN (with provenance)

### BBSome membership and architecture
- BBS-4 is part of the BBSome: [UniProt SUBUNIT "Part of BBSome complex, that contains at
  least bbs-1, bbs-2, bbs-4, bbs-5, osm-12, bbs-8/ttc-8 and bbs-9 (By similarity)"].
- Assembly order places BBS4 peripherally, added last: [PMID:26150102 "during the assembly
  of the BBSome, BBS2, 7, and 9 form the core, then BBS1, 5, 8, and finally BBS4 are added
  in a stepwise manner"].
- BBS-4 is a TPR protein; BBS5 is a PH-domain protein — the two share no domains yet are
  functionally redundant: [PMID:26150102 "BBS4 is a multiple tetratricopeptide repeats (TPR)
  containing protein, whereas BBS5 is a pleckstrin homology (PH) domain-containing protein
  ... two BBSome components that share no similar protein domains ... can function redundantly
  in the context of cilia"].

### BBSome function in IFT assembly / turnaround (the core ciliary role)
- The BBSome assembles IFT particles at the ciliary base and rides the anterograde IFT
  particle to the tip to regulate turnaround/recycling: [PMID:22922713 "the BBSome ...
  assembles IFT complexes at the ciliary base, then binds to the anterograde IFT particle in
  a DYF-2- ... and BBS-1-dependent manner, and lastly reaches the ciliary tip to regulate
  proper IFT recycling"], [PMID:22922713 "the in vivo function for the BBSome is to regulate
  the assembly of the IFT particles at the ciliary base"].
- The BBSome binds IFT like a cargo, not as an integral structural part of the IFT particle:
  [PMID:22922713 "After IFT particles are assembled at the ciliary base, the BBSome binds to
  the IFT particle like a cargo but not a structural component"].
- BBSome shares coat features and can recognize IFT cargo: [PMID:22922713 "The BBSome also
  shares the common structural features with COPI, COPII, and clathrin coats, and can directly
  recognize IFT cargos"].

### BBS-4 ciliary localization (experimental, worm)
- BBS-4 localizes to cilia / ciliary basal body (GOA IDA GO:0036064, MGI, PMID:22922713).
- In dyf-2 or bbs-1 mutants that uncouple the BBSome from moving IFT, BBS-4 completely loses
  ciliary localization and accumulates at the ciliary base: [PMID:22922713 "Some of them
  (BBS-1, BBS-4) totally lost the ciliary localization; the others (BBS-2, -5, -7, -8, -9)
  only showed very dim ciliary staining"].

### BBS-4–BBS-5 direct interaction and redundancy (PMID:26150102)
- BBS-4 directly interacts with BBS-5, via its C-terminus: [PMID:26150102 "We further mapped
  down the binding region in BBS-4 to the C-terminal 193 amino acids (a.a. 270–462)"] and
  in vivo [PMID:26150102 "strong fluorescence complementation between BBS-4 and BBS-5 was
  observed ... indicative of in vivo BBS-4-BBS-5 association"].
- Single mutants have no ciliogenesis defect; double bbs-4; bbs-5 mutants do:
  [PMID:26150102 "bbs-4 or bbs-5 single mutants are completely normal in dye-filling assay,
  indicating that BBS-4 or BBS-5 alone is dispensable for ciliogenesis"], [PMID:26150102
  "bbs-4; bbs-5 double mutants show typical cilia defect as observed in other bbs mutants"].
- Double mutants disrupt IFT integrity (IFT-A/IFT-B uncoupling, CHE-11 absent distally,
  OSM-6 accumulates): [PMID:26150102 "bbs-4; bbs-5 and bbs-7 share similar mutant phenotypes
  in that CHE-11 is absent, but OSM-6 abnormally accumulates, in the distal segments"].

### BBS-4/BBS-5 role in ciliary sensory-receptor removal / degradative sorting
- Redundantly required for **removal** (not entry) of ciliary sensory receptors PKD-2,
  OSM-9, ODR-10 — receptors abnormally accumulate in double mutants: [PMID:26150102 "both
  OSM-9 and ODR-10 show strong accumulations, with ~6-fold increasing of protein levels in
  their native expressing cilia in bbs-4; bbs-5 mutants"], and the defect is degradative:
  [PMID:26150102 "BBS-4 and BBS-5 play redundant role in the BBSome to ubiquitously regulate
  the lysosome-targeted degradation of ciliary sensory receptors"].
- The BBSome acts upstream of the early endosome, at the ciliary base, not by retrograde IFT
  for these non-IFT cargoes: [PMID:26150102 "the BBSome acts upstream of the early endosome,
  probably in endocytic stage at cilia base, to regulate the lysosomal sorting of ciliary
  receptors"].
- Polycystin signaling (mating behavior) is defective in double but not single mutants:
  [PMID:26150102 "bbs-4; bbs-5 double mutants, but not bbs-4 or bbs-5 single mutants, exhibit
  defective polycystin signaling similar to that observed in bbs-7 mutants"].

### Disease-relevant mutagenesis (worm mimics of human BBS4 alleles)
- A388E (mimics human pathogenic BBS4 A364E): abolishes BBS-4–BBS-5 interaction and ciliary
  targeting: [UniProt MUTAGEN 388 "A->E: Abolishes interaction with bbs-5. Unable to target
  to cilia."], [PMID:26150102 "BBS-4A388E, but not BBS-4E107Q, lost ciliary targeting"].
- E107Q (mimics weak human BBS4 E85Q, LCA-like): no obvious phenotype; still rescues:
  [UniProt MUTAGEN 107 "E->Q: No obvious phenotype."], [PMID:26150102 "BBS-4E107Q, but not
  BBS-4A388E, can rescue the ciliogenesis defect in bbs-4; bbs-5 mutants"].
- Conservation to mammals: human BBS4 and BBS5 also interact directly and redundantly
  downregulate ciliary polycystin-2 [PMID:26150102 "human BBS4 and BBS5 interact directly and
  function redundantly in downregulating ciliary polycystin-2"].

## NOT known / knowledge gaps

- **No experimentally demonstrated biochemical/molecular activity for BBS-4 itself.** The only
  MF annotation (GO:0030674 protein-macromolecule adaptor activity) is an ISS transfer from
  human BBS4 (UniProtKB:Q96RK4). What cargo(s) BBS-4's TPR array directly recognizes within
  the BBSome coat is undefined.
- **Ontology gap:** there is no GO molecular-function term expressing "membrane-coat / cargo-
  adaptor subunit of the BBSome" analogous to a COPI/COPII/clathrin coat subunit. The BBSome
  is explicitly described as coat-like [PMID:22922713 "shares the common structural features
  with COPI, COPII, and clathrin coats"], but a subunit of it is annotatable only with the
  generic adaptor term or `protein binding`. This is the same structural-subunit pattern
  flagged as an ontology gap in projects/FUNCTION_KNOWLEDGE_GAPS.md.
- **Centrosome / pericentriolar-material role is mammalian-derived, not shown in worm.** The
  ISS annotations GO:0000242 (pericentriolar material) and GO:0007098 (centrosome cycle), and
  the SubCell-mapped GO:0005813 centrosome / GO:0005856 cytoskeleton, all trace to the
  mammalian BBS4 pericentriolar/dynein role (By similarity, UniProtKB:Q96RK4). C. elegans
  BBS-4 has been characterized only in the ciliary/BBSome context; no worm experiment supports
  a pericentriolar-satellite function (and nematodes largely lack the mammalian centriolar-
  satellite system). Treated here as over-annotation for this organism.
- Structural position/stoichiometry of BBS-4 in the worm BBSome, and whether its redundancy
  with BBS-5 reflects a shared coat-surface, are not resolved.

## Annotation-review plan (13 GOA rows)

- GO:0034464 BBSome (NAS, part_of) — ACCEPT (core; complex membership).
- GO:0030674 protein-macromolecule adaptor activity (ISS, enables) — ACCEPT as the best
  available (subunit-adaptor) MF; flag the ontology gap.
- GO:0060271 cilium assembly (IBA + NAS) — ACCEPT (core; redundant with bbs-5 experimentally).
- GO:0061512 protein localization to cilium (IBA) — ACCEPT (core; BBSome traffics membrane
  cargo to/from cilium).
- GO:0036064 ciliary basal body (IBA is_active_in + IDA located_in) — ACCEPT (IDA experimental).
- GO:0005929 cilium (NAS) — ACCEPT (general but correct).
- GO:0060170 ciliary membrane (IEA SubCell) — ACCEPT.
- GO:0005813 centrosome (IEA SubCell) — KEEP_AS_NON_CORE (basal body is centriole-derived;
  general).
- GO:0005856 cytoskeleton (IEA SubCell) — KEEP_AS_NON_CORE (general parent).
- GO:0000242 pericentriolar material (ISS) — MARK_AS_OVER_ANNOTATED (mammalian-derived, no
  worm support).
- GO:0007098 centrosome cycle (ISS) — MARK_AS_OVER_ANNOTATED (mammalian-derived, no worm
  support).

## References used
- PMID:22922713 Wei et al. 2012 Nat Cell Biol — BBSome controls IFT assembly & turnaround (full text cached).
- PMID:26150102 Xu et al. 2015 Sci Rep — BBS4/BBS5 redundancy, direct interaction, receptor removal (full text cached).
- UniProt Q5CZ52 (BBS4_CAEEL).
</content>
</invoke>

## Deep research (falcon / Edison Scientific Literature)

`bbs-4-deep-research-falcon.md` was generated by the falcon provider (Edison Scientific
Literature; 36 citations, ~29 min run; the just-recipe wrapper reported a 600s subprocess
timeout but the client completed and wrote real output). It corroborates every point above
and adds cross-species structural/assembly context (not in the two worm papers, cited by DOI
in that report, so used here only as background, not as annotation provenance):

- BBS-4 is a **non-enzymatic TPR α-solenoid structural adaptor**; cryo-EM places it in the
  BBSome "body" with BBS5/BBS8/BBS18, with BBS18 acting as a stabilizing "U-bolt" through the
  BBS4/BBS8 TPRs and BBS1's β-propeller binding the BBS4 TPR N-terminus (Klink 2020 eLife
  10.7554/elife.53910; Singh 2020 eLife 10.7554/elife.53322; Tian 2023 eLife 10.7554/elife.87623).
- BBS-4 is the **last subunit added** to the BBSome and its incorporation requires BBS1
  (Zhang 2012 JBC 10.1074/jbc.m112.341487) — consistent with PMID:26150102's stepwise-assembly
  statement used in the review.
- The BBSome recognizes cargo via a central negatively-charged cleft and specific GPCR motifs
  ([W/F/Y][K/R] in helix 8, VxP C-terminal) (Yang 2020 eLife 10.7554/elife.55954) — background
  for the ontology-gap framing (no GO MF term for a coat cargo-adaptor subunit).
- The centriolar-satellite / PCM1 / actin-cytoskeleton roles are reported for **mammalian**
  BBS4 (Novas 2015 FEBS Lett 10.1016/j.febslet.2015.07.031; Tian 2023) — supporting the
  MARK_AS_OVER_ANNOTATED calls on the worm pericentriolar-material and centrosome-cycle ISS rows.

These DOI-only sources are recorded here as background; the review's annotation provenance
uses only the two cached full-text worm papers (PMID:22922713, PMID:26150102) plus the falcon
file reference.
