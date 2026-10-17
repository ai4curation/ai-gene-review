# sox2 (Sox2, XSox2; O42569) — Xenopus laevis — review notes

Project: NEURAL_CREST_ORIGINS (Tier 3, blastula programme retained in the crest; SoxB1 to SoxE
transition). Reviewed 2026-10-07. Read alongside `genes/XENLA/sox3-a/` (SoxB1 paralog, reviewed in
parallel by another agent) and `genes/human/SOX2/`.

## Identity

- O42569, 311 aa SoxB1 HMG-box transcription factor; HMG box 37-105, C-terminal 9aaTAD
  transactivation motif (by similarity to human SOX2) [file:XENLA/sox2/sox2-uniprot.txt].
- UniProt function: "Functions as a switch in neuronal development, participating in the
  differentiation of embryonic neuroectodermal cells into neural tissues by making the ectodermal
  cells responsive to FGF-neuralizing signals." [file:XENLA/sox2/sox2-uniprot.txt]
- Xenbase sox2.L (XB-GENE-865099). A UniProt search for sox2 in taxon 8355 (2026-10-07) returns
  only O42569 (no sox2.S entry), so homeolog splitting does not arise here.
- Paralogs: Sox1, Sox3 (SoxB1 group). Most frog loss-of-function reagents are dominant-negative
  Sox2 constructs (which can interfere with any SoxB1 protein) or combined Sox2+Sox3 morpholinos, so
  attribution to Sox2 alone is often uncertain [file:XENLA/sox2/sox2-deep-research-falcon.md "Most frog
  studies identify *sox2* or Sox2 without establishing that an assay discriminates every closely
  related SoxB1 protein or *X. laevis* homeolog."].

## Expression

- Blastula animal pole (pluripotent cells), with Sox3 [PMID:30144418 "The SoxB1 factors Sox2 and
  Sox3 are robustly expressed in the animal pole region of blastula embryos, where pluripotent cells
  reside (Figure 1A)."]; also co-expressed with crest/pluripotency factors in animal caps
  [PMID:39060477 "Indeed, in Xenopus neural crest regulatory genes such as snai1, zic1, id3, tfap2a,
  and foxd3 are co-expressed with the core pluripotency genes sox2, pou5, myc, and ventx/nanog8,9 in
  blastula (“animal pole”) stem cells, and are required for maintenance of pluripotency1."].
- Prospective neuroectoderm from the onset of gastrulation, induced by Chordin and suppressed by
  BMP4 [PMID:9435279 "Expression of the two genes is first detected widely in the prospective
  neuroectoderm at the beginning of gastrulation"].
- Restricted to the neural plate by late gastrula; overlaps SoxE at the border only transiently
  [PMID:30144418 "By late gastrula/early neurula stages, expression of Sox2 and Sox3 has been
  restricted to the prospective neural plate, marking the transition from their role in pluripotency
  to their subsequent roles in maintaining neuronal progenitor cells."]; [PMID:30144418 "The expression
  of SoxB1 and SoxE factors overlap at late gastrula stages, when both are expressed in neural crest
  regions of the neural plate border; however, by early neurula stages their expression is
  distinct."]; [PMID:30144418 "By early neurula stages the expression domains of SoxB1 factors and
  SoxE factors have become mutually excusive."].
- Note: Buitrago-Delgado 2015 [PMID:25931449] lists Sox3, not Sox2, among the genes with *enhanced*
  border expression at late gastrula ("several genes, including Oct60, Sox3, Vent2, Ets1, Zic1, Pax3,
  and Snail1, showing enhanced expression at the neural plate border by late gastrula stages"). Sox2
  is mentioned there only as a blastula-expressed pluripotency factor.
- Later: CNS, eye (retina and lens), retinal ciliary marginal zone, spinal-cord ventricular zone
  [file:XENLA/sox2/sox2-uniprot.txt]; [PMID:25797152 "We found that cells expressing Sox2 and/or Sox3
  are present in the ventricular zone of regenerative animals and decrease in non-regenerative
  froglets."].

## Molecular function

- HMG-box DNA-binding transcriptional activator (family-level; frog-specific evidence is indirect).
  Direct frog target: Rax (Rx1) CNS1 enhancer, bound by endogenous Sox2 together with Otx2, with
  synergistic activation and physical Otx2–Sox2 interaction [PMID:18385377 "We revealed that endogenous
  Otx2 and Sox2 proteins bound to the conserved noncoding sequence (CNS1) located approximately 2 kb
  upstream of the Rax promoter."]; [PMID:18385377 "Reporter assays showed that Otx2 and Sox2
  synergistically activated transcription via CNS1."]; [PMID:18385377 "Furthermore, the Otx2 and Sox2
  proteins physically interacted with each other"].
  -> The IPI `protein binding` (with Q91813 otx2-a) is MODIFIED to GO:0140297 DNA-binding transcription
  factor binding (Otx2 is a homeodomain DNA-binding TF; mouse Sox2 P48432 carries GO:0140297 by IPI,
  QuickGO 2026-10-07).
- Repression: SoxB1 gain of function at the border lowers foxd3/snail2 (see below), but no direct
  repressed target is mapped in frog; the IBA repression term is kept as non-core.

## Biological roles

1. **Neural induction / neuroectoderm competence (core).** Sox2 alone does not neuralise but makes
   ectoderm responsive to FGF [PMID:9435279 "Sox-2 alone is not sufficient to cause neural
   differentiation, but can work synergistically with FGF signaling to initiate neural induction."];
   [PMID:9435279 "Sox-2 makes the ectoderm responsive to extracellular signals"]. Dominant-negative Sox2
   blocks neural differentiation in caps and embryos [PMID:10648237 "Microinjection of dominant-negative
   forms of Sox2 (dnSox2) mRNA inhibits neural differentiation of animal caps caused by attenuation of
   BMP signals."]; [PMID:10648237 "These data suggest that Sox2-class genes are essential for early
   neuroectoderm cells to consolidate their neural identity during secondary steps of neural
   differentiation."]. Combined Sox2/Sox3 MOs block Chordin-induced neural induction, rescued by Sox2
   or Sox3 but not SoxE [PMID:30144418 "We first showed that morpholino-mediated depletion of Sox2 and
   Sox3 prevented chordin-mediated neural induction (Figure 6A–B)."].
   Caveat: dnSox2 is "Sox2-class"; the authors themselves generalise to SoxB1.
2. **Retinal progenitor competence and timing of differentiation (core, neural progenitor role).**
   Frizzled-5/Wnt maintains Sox2 in the optic vesicle; blocking Sox2 mimics loss of Xfz5 (less
   proliferation, no proneural onset, non-neural bias) [PMID:15820691 "Blocking Sox2 function mimics
   these effects."]. Later Sox2 suppresses neuronal differentiation via Notch and favours Müller glia;
   Sox2 must be switched off for neurons to form [PMID:19736324 "We now report that Wnt and Sox2 inhibit
   neural differentiation through Notch activation."]; [PMID:19736324 "For neuronal differentiation to
   proceed, Sox2 must also be switched off to relieve the inhibition of proneural activity."].
   -> NEW GO:0045665 negative regulation of neuron differentiation (IMP, PMID:19736324) and NEW
   GO:0060041 retina development in camera-type eye (IMP, PMID:15820691). Comparator: human SOX2 carries
   GO:0045665 (ISS) and mouse Sox2 carries GO:0045665 (IDA, PMID:16631155) (QuickGO 2026-10-07).
3. **Spinal-cord regeneration (non-core, not annotated).** Sox2 knockdown / dnSox2 disrupt recovery
   [PMID:25797152 "Sox2 knockdown and overexpression of a dominant negative form of Sox2 disrupts
   locomotor and anatomical-histological recovery."]. Left as narrative; no NEW term.
4. **Blastula pluripotency (competence; not annotated).** Combined Sox2+Sox3 MOs abolish animal-cap
   competence to form mesoderm/endoderm in response to activin, rescued by Sox2, Sox3, Sox9 or Sox10
   [PMID:30144418 "Cells depleted of SoxB1 factors are no longer competent to form mesoderm or endoderm
   in response to activin treatment, as assayed by expression of Brachyury and Endodermin (Figure
   5A–C), confirming that SoxB1 function is essential for pluripotency in blastula stem cells."]. The
   evidence is for SoxB1 jointly (double knockdown), and the project convention (lin28a, id3-a, myc-a,
   snai1) raises stem cell population maintenance as a question rather than annotating it. Raised as a
   suggested question.

## Does Sox2 belong in the neural crest network?

- **SoxB1 must be switched OFF for crest.** Activating SoxB1 (Sox2-GR or Sox3-GR, dex at stage 10) at
  the border lowers foxd3 and snail2, whereas SoxE raises them [PMID:30144418 "Interestingly, we found
  that inducing SoxB1 activity at the neural plate border at these stages led to down-regulation of
  neural crest factors Foxd3 and Snail2 (Figure 3B, S1C)."]. SoxB1 cannot substitute for SoxE in
  crest induction [PMID:30144418 "By contrast Sox2 or Sox3 showed little or no ability to rescue Foxd3
  expression."]. SoxE can substitute for SoxB1 in blastula pluripotency (overexpression), not in
  neural induction.
- **Who switches whom off?** Buitrago-Delgado attribute the SoxB1/SoxE exclusion "at least in part, to
  the repressive activity of Snail2 on Sox2 expression (Acloque et al., 2011)". The cited paper
  [PMID:21920318] is about chick/mouse **Sox3** and Snail2 at gastrulation ("this decision to
  internalize is mediated by reciprocal transcriptional repression of Snail2 and Sox3 factors"), not
  Sox2 and not the crest. So the crest-side repressor of Sox2 in frog is not directly shown; relevant to
  the sox3-a review too.
- **Participation test (CLAUDE.md).** Sox2's contribution to crest is (a) upstream, as part of the
  SoxB1 blastula competence that crest-precursor cells inherit, and (b) its *removal*. A factor that
  must be switched off does not do any of the work of crest formation; the work (fate specification)
  is done by SoxE, Snail, FoxD3 etc. Sox2 provides no scaffold, cofactor or catalytic contribution to
  the crest process. Only gain-of-function evidence links Sox2 to the crest (ectopic SoxB1 represses
  crest markers); no Sox2-specific loss of function expands crest. So: **no `GO:0014029`, no
  `GO:0014036`, and no `GO:0090301`/`GO:1905296` negative-regulation term.**
- **Comparator check (QuickGO, 2026-10-07, descendants of GO:0014029, GO:0014033, GO:0090299,
  GO:1905292).** Zero annotations on human SOX2 (P48431), mouse Sox2 (P48432), zebrafish sox2
  (Q6P0E1), X. laevis sox3-a (P55863) and X. laevis sox2 (O42569). SoxB1 proteins carry no crest
  process term (positive or negative) in any species; this is consistent with the reading above, not
  a gap. By contrast mammalian SOX2 carries stem-cell maintenance terms: human GO:0035019 (IDA/IMP),
  GO:0097150 (ISS); mouse GO:0019827 (IMP x3), GO:0097150 (IGI). Zebrafish sox2 and frog sox2/sox3
  carry none.
- **Network placement.** Sox2 is a neural plate / neural progenitor gene and a blastula pluripotency
  factor, *not* a member of the module's `progenitor_competence_maintenance` part (which holds
  Myc, Id3, Hairy2: factors that stay on in border/crest progenitors and whose loss causes progenitor
  arrest). If the module represents SoxB1 at all, it should be as an upstream blastula competence state
  (Sox2/Sox3 as a set) whose hand-off to SoxE precedes crest specification, or as a knowledge-gap note
  on the SoxB1 to SoxE transition — not as an annoton with a crest process term.

## Evolution

- The SoxB1 to SoxE switch is conserved in lamprey: soxB1 orthologs are expressed in blastula, gastrula
  ectoderm and border, then downregulated in premigratory crest as soxE comes on [PMID:39060477
  "Orthologs of soxB1 were also expressed in the blastula, gastrula ectoderm and neural plate border,
  but then downregulated in premigratory neural crest (Fig. 2a; Extended Data Fig. 2), concomitant
  with a switch to soxE factor expression, a feature conserved with Xenopus14."]. So the hand-off dates
  to the vertebrate ancestor.
- SoxB1 neural roles are pan-bilaterian (the IBA neuron differentiation node includes Drosophila
  SoxNeuro/Dichaete and C. elegans sox-2 donors). The vertebrate novelty is not a new SoxB1 activity
  but the recruitment of SoxE into blastula-like potency; SoxB1 is the ancestral state being handed
  off [PMID:30144418 "In contrast to most neural crest potency factors (including Snail1, Myc, Foxd3,
  Ets1, Ap2, and Vent2), Sox9 and Sox10 are not first expressed in pluripotent naïve blastula cells."].

## Decisions summary

- 25 GOA rows: MF activator/DNA binding/nucleus accepted; IPI protein binding -> GO:0140297; IMP
  nervous system development accepted (core, neural induction); IBA neuron differentiation accepted;
  brain development, repression, cytoplasm, cell differentiation and ARBA anatomical term non-core.
- NEW: GO:0045665 (IMP PMID:19736324), GO:0060041 (IMP PMID:15820691).
- No crest term. Questions: SoxB1 blastula pluripotency term; Snail2 -> Sox2 repression evidence in
  frog; paralog attribution of dnSox2 and combined-MO results.
