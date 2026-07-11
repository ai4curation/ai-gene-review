# hsp-110 (C. elegans) — research notes

Gene: **hsp-110** / ORF **C30C11.4** / WormBase **WBGene00016250**
UniProt: **Q05036** (HS110_CAEEL), 776 aa, chromosome III.
Product: Heat shock protein 110 (HSP110 / HSPH-family Hsp70 relative).

## Identity / family (KNOWN)

- UniProt: "Belongs to the heat shock protein 70 family" (SIMILARITY, ECO:0000305). Domain
  architecture is the canonical Hsp70 fold: N-terminal actin-like ATPase nucleotide-binding
  domain (NBD; CDD cd10228 `ASKHA_NBD_HSP70_HSPA4_like`, InterPro IPR043129) + Hsp70
  substrate/peptide-binding-like domain (IPR029047) + Hsp70 C-terminal subdomain (IPR029048)
  [file:worm/hsp-110/hsp-110-uniprot.txt].
- This is the **HSP110 / HSPA4 (HSPH) subfamily**, not a canonical Hsp70. FunFam/Gene3D and
  PANTHER (PTHR45639) place it with "Heat shock 70 kDa protein 4" (HSPA4); the ALS paper
  identifies C30C11.4 as "homolog to human apg-1 (a heat shock 110 kDa protein)"
  [PMID:19165329 "C30C11.4 ... homolog to human apg-1 (a heat shock 110 kDa protein)"].
  Human orthologs of the HSP110/HSPH class are HSPH1 (HSP105), HSPA4 (APG-2) and HSPA4L
  (APG-1/apg-1). The IBA reference set for the NEF activity includes yeast SSE1/SSE2
  (SGD:S000000373/S000006027) and human HSPH1 (UniProtKB:Q92598), confirming the orthology
  basis [file:worm/hsp-110/hsp-110-goa.tsv].

## Molecular function (KNOWN at family level; INFERRED for worm)

HSP110-family proteins are the principal **cytosolic nucleotide-exchange factors (NEFs) for
Hsp70**. Established biochemically/structurally in yeast (Sse1p) and conserved across
eukaryotes:

- Sse1p (yeast Hsp110) "acts as an efficient nucleotide exchange factor (NEF) for both yeast
  cytosolic Hsp70s, Ssa1p and Ssb1p. The mechanism involves formation of a stable
  nucleotide-sensitive complex, but does not require ATP hydrolysis by Sse1p" [PMID:16688211
  "acts as an efficient nucleotide exchange factor (NEF) for both yeast cytosolic Hsp70s, Ssa1p
  and Ssb1p. The mechanism involves formation of a stable nucleotide-sensitive complex, but does
  not require ATP hydrolysis by Sse1p"].
- Structurally, "the NBD of Sse1p is ATP bound, and together with the 3HBD it embraces the NBD
  of Hsp70, inducing opening and the release of bound ADP from Hsp70. Mutations that abolish NEF
  activity are lethal, thus defining nucleotide exchange on Hsp70 as an essential function of
  Sse1p" [PMID:18555782 "the NBD of Sse1p is ATP bound, and together with the 3HBD it embraces
  the NBD of Hsp70, inducing opening and the release of bound ADP from Hsp70. Mutations that
  abolish NEF activity are lethal, thus defining nucleotide exchange on Hsp70 as an essential
  function of Sse1p"].

Implications for the GO annotations:
- **ATP binding (GO:0005524)** is genuine and functionally required: Hsp110's own NBD must be
  ATP-loaded to embrace and open the Hsp70 NBD [PMID:18555782].
- **ATP hydrolysis (GO:0016887)**, in contrast, is **not required** for the defining NEF
  activity, and Hsp110 "does not employ the nucleotide-dependent allostery and peptide-binding
  mode of canonical Hsp70s" [PMID:18555782 "Sse1p does not employ the nucleotide-dependent
  allostery and peptide-binding mode of canonical Hsp70s, and that direct interactions of
  substrate with Sse1p may support Hsp70-assisted protein folding in a cooperative process"].
  So the IEA `ATP hydrolysis activity` (propagated from the generic Hsp70 fold) is an
  over-annotation relative to the characterized mechanism (weak/atypical ATPase; hydrolysis
  dispensable).
- Beyond NEF, Hsp110 also has intrinsic **holdase / substrate-binding** activity ("direct
  interactions of substrate with Sse1p may support Hsp70-assisted protein folding"
  [PMID:18555782]), and its NEF activity stimulates Hsp70-mediated **refolding** of denatured
  substrate ("The NEF activity of Sse1p stimulates in vitro Ssa1p-mediated refolding of
  thermally denatured luciferase" [PMID:16688211]).

## Worm-specific biological role (KNOWN — experimental)

1. **Prevents aggregation of a misfolding-prone protein in neurons in vivo (disaggregase/
   holdase partner of the Hsp70 machine).** In a pan-neuronal mutant human SOD1(G85R) ALS model,
   an RNAi screen for modifiers of aggregation found that knockdown of a set of chaperones —
   "including an Hsp110 (C30C11.4), a DnaJ (A2) (dnj-19), an Hsp70 (stc-1), and a neuron specific
   Hsp16 (F08H9.4)" — **strongly increased** SOD1 inclusion formation [PMID:19165329 "including
   an Hsp110 (C30C11.4), a DnaJ (A2) (dnj-19), an Hsp70 (stc-1), and a neuron specific Hsp16
   (F08H9.4)"]. The effect was confirmed with the loss-of-function allele **gk533** (Table 2:
   "C30C11.4 ... homolog to human apg-1 (a heat shock 110 kDa protein) 3 gk533 ++", strong
   increase of inclusions). This co-set (Hsp110 + Hsp40/DnaJ + Hsp70) is exactly the metazoan
   Hsp70–Hsp40–Hsp110 disaggregation machinery, giving in vivo support for
   GO:0035966 (response to topologically incorrect protein). UniProt records the disruption
   phenotype: "RNAi-mediated knockdown in a sod-1 mutant background results in increased
   aggregation of denatured proteins in neurons" [file:worm/hsp-110/hsp-110-uniprot.txt].

2. **Modifier of proteostasis / polyglutamine folding (protein folding, IMP).** In a genome-wide
   RNAi screen in body-wall muscle, C30C11.4 was one of six chaperone-class genes among the polyQ
   (Q35/Q37) aggregation modifiers ("Protein Folding and transport ... Chaperone (6) F08H9.3;
   cyn-11; cyn-12; C30C11.4; dnj-22; phb-2") whose knockdown suppressed polyQ aggregation
   [PMID:22242008 "F08H9.3; cyn-11; cyn-12; C30C11.4; dnj-22; phb-2"]. It was a Class A (strong,
   Q35+Q37) modifier. This is the basis of the WormBase IMP GO:0006457 (protein folding)
   annotation. (Note the direction: here *knockdown* suppresses aggregation, whereas in the
   neuronal SOD1 model knockdown *increases* aggregation — i.e. the readout is model-dependent,
   but both link hsp-110 to the folding/aggregation environment.)

3. **Contributes to longevity of insulin/IGF-1-signaling (ILS) mutants (determination of adult
   lifespan, IGI).** Morley & Morimoto showed that "Down-regulation of individual molecular
   chaperones, transcriptional targets of HSF-1, also decreased longevity of long-lived mutant
   but not wild-type animals" [PMID:14668486 "Down-regulation of individual molecular chaperones,
   transcriptional targets of HSF-1, also decreased longevity of long-lived mutant but not
   wild-type animals"]. The WormBase IGI annotation records a genetic interaction with
   WB:WBGene00000090 = **age-1** (PI3K, an ILS long-lived mutant background). This paper is
   abstract-only in our cache (full_text_available: false); the specific hsp-110 result is in the
   full text the curator read. Treated as a real experimental annotation (do not remove); it is a
   pleiotropic/downstream organismal role, not the core molecular function → KEEP_AS_NON_CORE.

## Localization (KNOWN at family level)

- HSP110 proteins are "exclusively found in the eukaryotic cytosol" [PMID:16688211 "The Hsp110
  proteins, exclusively found in the eukaryotic cytosol"] → cytosol (GO:0005829) is the core
  site. The IBA `nucleus` (GO:0005634) is a phylogenetic propagation (mammalian HSPH1 can also be
  nuclear); no direct worm evidence → KEEP_AS_NON_CORE.

## NOT known (candidate knowledge gaps)

- **Whether C. elegans HSP-110 is genetically required for Hsp70/Hsp40-dependent protein
  DISAGGREGATION in vivo, and the identity of its worm-specific Hsp70 (HSP-1 vs STC-1 vs HSP-70)
  and Hsp40/J-protein partners.** PMID:19165329 shows hsp-110/dnj-19/stc-1 co-suppress SOD1
  aggregation, but the biochemical disaggregase reconstitution and the definitive partner set for
  the worm are not established.
- **The endogenous worm client repertoire of HSP-110** (which native metastable proteins depend
  on HSP-110 NEF activity) is undefined; existing evidence is limited to heterologous
  aggregation-prone reporters (polyQ, mutant SOD1) and to family-level in vitro substrates.
- **Whether HSP-110's own weak/atypical ATPase activity has any in vivo role in the worm**, given
  that the defining NEF mechanism does not require ATP hydrolysis [PMID:16688211; PMID:18555782].
- **Whether HSP-110 has an Hsp70-independent holdase function in the worm** (direct substrate
  binding), as suggested at the family level [PMID:18555782].

## Deep research

- Falcon (Edison Scientific Literature) deep research completed after a ~29-min run
  (`hsp-110-deep-research-falcon.md`, 23 citations). It independently reaches the same
  conclusions used here: HSP-110 is the cytosolic HSP110-family **NEF for Hsp70** and a component
  of the **metazoan Hsp70–Hsp40–Hsp110 protein-disaggregation machine**. It surfaces two
  directly relevant papers for the knowledge gaps — Rampelt et al. 2012 EMBO J "Metazoan Hsp70
  machines use Hsp110 to power protein disaggregation" and, crucially for the worm, Kirstein et
  al. 2017 Aging Cell "In vivo properties of the disaggregase function of J-proteins and Hsc70 in
  Caenorhabditis elegans stress and aging" — that establish the C. elegans disaggregase context
  against which HSP-110's specific in-vivo requirement (knowledge gap #1) is defined.
- The falcon report uses DOI-keyed citations (no PMIDs); per repo experience the reference
  validator does not check `file:`/DOI quotes, so NONE of the falcon text is used verbatim in the
  review. All `supporting_text` in the review is PMID-anchored and verified against the cached
  publications (PMID:19165329, PMID:22242008, PMID:14668486, PMID:16688211, PMID:18555782).
