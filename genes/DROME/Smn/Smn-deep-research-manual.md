# Smn (Drosophila melanogaster, Q9VV74) - manual literature synthesis

No deep-research provider was available for this review. This file is a manual
literature synthesis compiled by the reviewer from the cached publications in
`publications/` (full text where available, otherwise abstract) and the curated
UniProt record `Smn-uniprot.txt`. Provenance is given inline.

## Identity and domain architecture

- Smn (CG16725, FBgn0036641, GeneID 39844) encodes the single Drosophila ortholog of
  human SMN1/SMN2, a 226-aa protein with an N-terminal Gemin2-binding region, a central
  Tudor domain (residues 69-128) and a C-terminal YG-box self-association region
  [UniProt Q9VV74 FT DOMAIN 69..128 "Tudor"; FT REGION 159..226 "Required for
  homodimerization" (PubMed:11113446)]. Pfam: SMN_G2-BD (PF20636), SMN_Tudor (PF06003),
  SMN_YG-box (PF20635).
- Homodimerization through the C-terminal region is abolished by the SMA-like allele
  Smn-B (S201F), which is lethal at late larval stages [UniProt FT MUTAGEN 201].

## Core molecular function: snRNP (Sm core) assembly as part of the SMN complex

- The fly SMN complex is unusually simple. Affinity purification of tagged dSMN from
  S2 cells yielded a complex "composed of SMN and Gemin2 only" that is assembly-active
  [PMID:18621711 "An affinity chromatography strategy has permitted us the purification
  of an assembly-active complex composed of SMN and Gemin2 only."].
- The SMN-Gemin2 complex carries the whole set of Sm proteins
  [PMID:18621711 "Strikingly, the entire set of Sm proteins, namely SmB, SmD1 (gene
  snRNP69D), SmD2 (CG1249), SmD3, SmE (CG18591), SmF (DebB), and SmG (CG9742), was
  prominently present in the elution."] and transfers them selectively to Sm-site
  RNAs [PMID:18621711 "In contrast, Sm proteins bound to the SMN complex were
  exclusively transferred onto the cognate snRNA"; "Importantly, Sm proteins bound to
  the SMN complex could not be transferred onto RNAs lacking a functional Sm site"].
- Later proteomics using flies expressing only Flag-SMN from its native promoter found
  Gemin2, Gemin3, Gemin5 (rig) and a Gemin4 ortholog (CG2941/Glos and two paralogs)
  co-purifying with SMN [PMID:30563832 "we previously found that Gemin2, Gemin3, Gemin5,
  and all nine classical Sm proteins, including Lsm10 and Lsm11, co-purify with SMN.
  Here, we show that CG2941 is also highly enriched in the pulldown."].
- Gemin3 binds Smn in vivo [PMID:19023405 "Moreover, co-immunoprecipitation experiments
  using Drosophila larval muscle extracts show that Gemin3 binds to SMN in vivo."];
  Gemin3 depletion co-depletes dSMN and inhibits Sm core assembly [PMID:18923150 abstract
  "RNA interference for dGem3 codepletes dSMN and inhibits efficient Sm core assembly
  in vitro."].
- Knockdown of Smn in S2 cells reduces assembly of new Sm cores [PMID:17353360 "As
  assayed by two independent methods, Smn dsRNA-treated S2 cells were deficient in
  assembly of new Sm cores"].
- Smn null larvae have reduced snRNA levels, most strongly for minor (U12-type)
  spliceosome snRNAs [PMID:22813737 abstract "Smn null mutants display larval lethality
  and show significant locomotion defects as well as reductions in minor-class
  spliceosomal snRNAs."; PMID:23063131 "the levels of all the snRNAs were decreased in
  smn73Ao mutants with differential effects of SMN deficiency on the accumulation of
  individual snRNAs ranging from a 70% reduction of U4atac to a 30% reduction of U1"].

## Downstream: pre-mRNA splicing (indirect)

- Lotti et al. found SMN-dependent retention of a subset of U12 introns in fly larvae
  [PMID:23063131 "Consistent with inefficient U12 splicing, we found increased U12
  intron retention for 6 of these genes in U6atacK01105 mutants and for 2 of these
  genes in smn73Ao mutants"], including stasimon (CG8408).
- Praveen et al. instead saw no appreciable minor-intron splicing defects despite
  snRNA reduction, and rescued viability/locomotion with low-level transgenic SMN that
  did not restore snRNAs [PMID:22813737 abstract "Despite these reductions, we found no
  appreciable defects in the splicing of mRNAs containing minor-class introns."].
  The relationship between the snRNP-assembly function and organismal phenotypes is
  therefore contested.

## Subcellular localization

- Predominantly cytoplasmic; enriched in cytoplasmic U bodies, which contain U snRNPs
  and assembly factors and abut P bodies [PMID:17595295 abstract "In addition to snRNPs,
  U bodies contain essential snRNP assembly factors, suggesting that U bodies are sites
  for assembly or storage of snRNPs before their import into the nucleus."].
- A minor nuclear pool in Cajal bodies and gems [PMID:16533947 "we find that SMN is
  colocalized with U2 snRNA and U85 scaRNA in CBs in the female germline and in follicle
  cell nuclei."; PMID:21627586 abstract "Drosophila gems contained endogenous SMN and at
  times overlapped with Cajal bodies."].
- In flight muscle, at the sarcomeric I band and Z line, co-precipitating with
  alpha-actinin [PMID:17353360 "Collectively, these studies show that dSMN forms a
  complex with α-actinin in vivo."].
- Concentrated postsynaptically at the larval NMJ [PMID:18791638 "However, at the
  Drosophila NMJ, SMN is concentrated at the post-synaptic regions in the muscle."].

## Organismal phenotypes (pleiotropic; necessity, not mechanism)

- Zygotic mutants: larval lethality, small larvae, reduced locomotion; NMJ bouton and
  glutamate receptor clustering defects [PMID:12783845 abstract "Clustering of a
  neurotransmitter receptor subunit in the muscle at the neuromuscular junction is
  severely reduced."]; [PMID:18791638 "we conclude that the NMJ morphology is dependent
  upon both pre- and post-synaptic SMN activity."].
- Motor circuit: SMN needed in cholinergic proprioceptive neurons/interneurons, not in
  motor neurons, for normal NMJ transmission [PMID:23063130 abstract "SMN must be
  expressed in proprioceptive neurons and interneurons in the motor circuit to
  nonautonomously correct defects in motor neurons and muscles."]. Evoked release is
  increased, not decreased, in smn mutants [PMID:23063131 "Evoked neurotransmitter
  release from motor neurons is increased in Drosophila smn mutants"].
- FGF signalling links: [PMID:21300852 abstract "Smn activity regulates the expression
  of FGF signaling components and thus FGF signaling."].
- Stem cells / neuroblasts: [PMID:21490958 "Clonal analysis indicates that SMN deficient
  stem cells have a reduced number of divisions and also generate cells with lower
  levels of U2 and U5 snRNPs."].
- Germline nuclear organization and U body-P body integrity [PMID:19464282 abstract
  "mutations in smn disrupt the function and organization of U bodies and P bodies."].
- Tracheal terminal cells: a single tracheal RNAi line abolishes gas-filled lumens
  [PMID:23029159 "When we did this, we found that terminal cells lack their gas-filled
  lumens, a phenotype very similar to Zpr1 loss of function (Fig. 4)."].

## Interpretation

Smn's directly demonstrated molecular activity is as the core scaffold of the SMN
complex that loads Sm proteins onto snRNAs (spliceosomal snRNP assembly), with
specificity for Sm-site RNAs. Nearly all developmental and neuromuscular annotations
derive from loss-of-function phenotypes of an essential housekeeping gene and are
best treated as non-core; several (cholinergic transmission regulation, AMPA receptor
clustering, basal protein localization) are mechanistically unsupported.
