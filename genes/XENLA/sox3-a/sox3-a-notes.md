# sox3-a (Sox3, xSox3, xSox-B1; P55863) — Xenopus laevis — review notes

Project: NEURAL_CREST_ORIGINS (Tier 3, blastula programme retained in the crest; SoxB1 to SoxE
transition). Reviewed 2026-10-07. Read alongside `genes/XENLA/sox2/` (SoxB1 paralog, reviewed in
parallel by another agent; not edited here).

## Identity and homeologs

- P55863, 309 aa SoxB1 HMG-box transcription factor; single-exon gene; 9aaTAD by similarity
  [file:XENLA/sox3-a/sox3-a-uniprot.txt].
- UniProt P55863 "sox3-a" maps to **Xenbase sox3.S** (XB-GENE-484819), RefSeq NM_001090679.1. The
  homeolog Q5FWM3 "sox3-b" (307 aa; RefSeq NM_001173404.1) must therefore be sox3.L. Note that UniProt
  lists "sox11" as a synonym of sox3-b (Q5FWM3) — this looks like a legacy clone-name artefact and should
  be checked; it is not a SoxC protein.
- All experimental GO rows sit on sox3-a only. QuickGO (2026-10-07): Q5FWM3 sox3-b and X. tropicalis
  sox3 (Q68FA4) carry ISS copies from P55863 (GO:0000122, GO:0001704, GO:0008013, GO:0043565,
  GO:0045892, nucleus, cytoplasm), but NOT the Wnt (GO:0090090) or BMP (GO:0030514) rows.
- The Phelps 2023 CUT&RUN construct was sox3.S = NM_001090679.1 = P55863 itself
  [PMID:37787392 "we performed CUT&RUN on stage 8 embryos injected with mRNA encoding V5 epitope-tagged
  pou5f3.3.L and sox3.S."]. So the chromatin-binding evidence is genuinely P55863-specific; the
  morpholinos (Zhang 2003 MO) probably hit both homeologs. Phelps also report maternal sox3 RNA from both
  subgenomes (falcon deep research).

## Expression

- Maternal: most abundant in stage I oocytes, protein in stage I/II oocytes [PMID:9099866 "the XSox3
  protein was detected in stage I and II oocytes"]; RNA in eggs and late blastula [PMID:9328277 "The
  message of the xSox-B1 gene was also detected in unfertilized eggs and the late blastula embryos of X.
  laevis."]. Animal hemisphere of egg and cleavage embryos [file:XENLA/sox3-a/sox3-a-uniprot.txt].
- Protein primarily cytoplasmic early, nuclear later [file:XENLA/sox3-a/sox3-a-uniprot.txt "Primarily
  cytoplasmic in early embryos"].
- Blastula animal pole (pluripotent cells), with Sox2 [PMID:30144418 "The SoxB1 factors Sox2 and Sox3 are
  robustly expressed in the animal pole region of blastula embryos, where pluripotent cells reside (Figure
  1A)."].
- Only SoxB1 throughout ectoderm before neural induction [PMID:18992330 "sox3 is uniquely expressed
  throughout the ectoderm prior to neural induction suggesting a role in neural competence"]; induced by
  BMP inhibition alone, not FGF [PMID:22172147 "other early genes, sox3, geminin and zicr1 are induced by
  BMP inhibition alone."].
- Border at late gastrula, then excluded from crest: [PMID:25931449 "several genes, including Oct60,
  Sox3, Vent2, Ets1, Zic1, Pax3, and Snail1, showing enhanced expression at the neural plate border by
  late gastrula stages"]; [PMID:30144418 "By late gastrula/early neurula stages, expression of Sox2 and
  Sox3 has been restricted to the prospective neural plate, marking the transition from their role in
  pluripotency to their subsequent roles in maintaining neuronal progenitor cells."]; [PMID:30144418 "By
  early neurula stages the expression domains of SoxB1 factors and SoxE factors have become mutually
  excusive."]; [PMID:39060477 "Arrowheads denote expression of sox3 largely excluded from the neural crest
  at late neurula stages."].
- Animal-cap potency correlation [PMID:25931449 "Oct60, Sox3, FoxD3, and Myc expression was high in
  blastula-stage explants but reduced by late gastrula stages, correlating with loss of potential"].
- Later CNS, otic vesicle, branchial arches, lens; adult mainly ovary [file:XENLA/sox3-a/sox3-a-uniprot.txt].

## Molecular function

- Sequence-specific DNA binding (AACAAT / AACAAAG) with recombinant protein [PMID:9099866
  "Recombinant XSox3 protein produced in Escherichia coli bound specifically to sequences containing the
  binding motif for the HMG box of SRY or SOX proteins, AACAAT or AACAAAG, demonstrating its
  sequence-specific DNA binding property."]; [PMID:9328277 "Recombinant polypeptide of the xSox-B1 HMG
  domain preferentially binds to the AACAAT sequence."].
- In vivo chromatin occupancy at stage 8; SOX3 motif top de novo hit; Oct-Sox heterodimer motifs
  [PMID:37787392 "Homer de novo motif analysis recovered the OCT4 and SOX3 binding sequences as top
  hits"]; [PMID:37787392 "suggesting Pou5f3 and Sox3 may form a complex in the blastula, similar to
  mammalian OCT4 and SOX2"].
- **Context-dependent activator and repressor.**
  - Repressor (maternal): Xnr5 promoter [PMID:14522872 "XSOX3 acts as a transcriptional repressor of
    Xnr5 in both the intact embryo and animal caps injected with VegT RNA."]; Sox3-VP16 or MO raise Xnr5
    [PMID:14522872 "Expression of a chimeric polypeptide composed of XSOX3 and a VP16 transcriptional
    activation domain or morpholino-induced decrease in endogenous XSOX3 polypeptide levels lead to an
    increase in Xnr5 expression"]. Mechanism is DNA binding, not beta-catenin binding [PMID:14522872 "this
    effect is due not to the binding of XSOX3 to beta-catenin nor to its competition with
    beta-catenin-regulated TCF-type transcription factors for specific DNA binding sites"].
  - Activator (ZGA and neural): [PMID:37787392 "Together, our findings establish the pluripotency factors
    Pou5f3.3 and Sox3 as maternal activators of embryonic genome activation, which are differentially
    recruited to the two homeologous subgenomes of X."]; [PMID:18992330 "Sox3 functions as an activator to
    induce expression of the early neural genes, sox2 and geminin in the absence of protein synthesis and
    to indirectly inhibit the Bmp target Xvent2."].
  - So GO:0001228 (activator) is the best-supported MF, and repression of xnr5 is captured at process
    level (GO:0000122). No NEW GO:0001227: the Xnr5 repression is DNA-binding-dependent, but Sox3 is
    "commonly thought" to be an activator and the repression may be partner-dependent; leave as question.
- beta-catenin binding [PMID:10549281 "Two additional Sox proteins, XSox17 alpha and XSox3, likewise bind
  to beta-catenin and inhibit its TCF-mediated signaling activity."] — real interaction but Zhang 2003
  shows it is not how Sox3 blocks axis formation in vivo -> non-core.

## Biological roles (synthesis)

1. **Maternal germ-layer patterning (core).** Animal Sox3 restricts nodal-related genes vegetally:
   [PMID:15302595 "In Xenopus, SOX3 acts as a negative regulator of Xnr5, which encodes a nodal-related
   TGFbeta-family protein."]; [PMID:15302595 "maternal B1-type SOX functions together with the
   VegT/beta-catenin system to regulate nodal expression and to establish the normal pattern of germ
   layer formation in Xenopus."]; [PMID:17608734 "Animally localized Sox3 acts to inhibit Nodal (Xnr5 and
   Xnr6) expression, and induces the expression of genes (Ectodermin, Xema, and Coco) whose products repress
   Nodal signaling."]. (Candidate: GO:1900108 negative regulation of nodal signaling pathway — no SoxB1
   carries it in QuickGO; left as question.)
2. **Zygotic genome activation (core; NEW GO:0141064).** Sox3.S occupies enhancers at stage 8; Sox3 MO
   (with Pou5f3 MOs) misregulates genome activation; bound elements lie near genes that fail to activate
   [PMID:37787392 "Down-regulated genes are highly significantly nearer to predicted regulatory elements
   with enriched Pou5f3 and Sox3 binding"]. Comparator (QuickGO 2026-10-07): GO:0141064 is carried by
   zebrafish sox19b (Q9DDD7, a SoxB1, IMP PMID:35145080) and zebrafish pou5f3 (IMP, same paper) — same
   role (maternal SoxB1 / Pou5 pioneer activators of ZGA). No mammalian/frog SoxB1 carries it yet; the
   term is new (2023). Participation test: Sox3 is a sequence-specific transcription activator bound at the
   regulatory elements of the activated genes — it performs a step of the process. Passes.
   Caveat: Sox3 single MO had modest effects; strongest phenotypes are in combination with pou5f3 MOs.
3. **Blastula pluripotency / ectodermal competence (shared with Sox2; question only).** [PMID:30144418
   "Cells depleted of SoxB1 factors are no longer competent to form mesoderm or endoderm in response to
   activin treatment, as assayed by expression of Brachyury and Endodermin (Figure 5A–C), confirming that
   SoxB1 function is essential for pluripotency in blastula stem cells."] — double Sox2/Sox3 MO, rescued
   by either. As for sox2, lin28a, id3-a, myc-a, snai1, a stem cell population maintenance term is raised
   as a question, not annotated.
4. **Neural induction / neural plate formation (core; NEW GO:0021990).** Sox3 is the only SoxB1 in naive
   ectoderm before induction; MO blocks Noggin-mediated neural induction, rescued by MO-resistant RNA
   [PMID:18992330 "With morpholino-mediated knockdown of Sox3, we demonstrate that it is required for
   induction of neural tissue by BMP inhibition."]; [PMID:18992330 "We were able to rescue this phenotype
   by injecting sox3 mRNA in which the Sox3MO annealing sequence was mutated"]; it directly
   (CHX-resistant) activates sox2 and geminin. Double Sox2/Sox3 MO blocks chordin neural induction,
   rescued by Sox3 [PMID:30144418]. Oct91 required for Sox3-driven neural induction [PMID:21147085
   "knockdown of Oct91 inhibits neural induction driven by either Sox2 or Sox3."].
   Term choice: GO:0021990 neural plate formation ("The formation of the flat, thickened layer of
   ectodermal cells known as the neural plate. The underlying dorsal mesoderm signals the ectodermal cells
   above it..." — i.e. neural induction). GO has no "neural induction" term (OLS search 2026-10-07).
   Comparator: no SoxB1 in QuickGO carries GO:0001840 or descendants; frog sox2 carries the broader
   GO:0007399 by IMP for the equivalent neural-induction experiments (PMID:9435279, PMID:10648237), and
   zebrafish/mouse SoxB1 carry nervous-system descendants. So the absence of a neural-plate term is
   granularity, not a convention against SoxB1 in neural induction. Participation: Sox3 is the TF that
   directly activates early neural plate genes (sox2, geminin) in the responding ectoderm; passes.
5. **Neural progenitor maintenance / delay of neurogenesis (non-core).** Gain of function only
   [PMID:18992330 "Sox3 increases cell proliferation, delays neurogenesis and inhibits epidermal and neural
   crest formation to expand the neural plate."]; constitutive Sox3 increases apoptosis [PMID:21147085].
   No NEW GO:0045665 (unlike frog sox2, which has retina-specific evidence); question only.
6. **BMP and Wnt antagonism (non-core).** BMP: Sox3 indirectly represses Xvent2/bmp4 [PMID:18992330].
   The GOA IMP row cites the XOct-25 paper PMID:17950579 (abstract-only, no Sox3 in abstract) — cannot
   verify, but the function is independently supported, so kept non-core. Wnt: TCF reporter inhibition
   [PMID:10549281]; the GOA IDA row cites PMID:17875931 (Sox17/Sox4 in colon cancer cells; abstract-only,
   full text not retrievable from PMC via the MCP) — kept non-core, deferring to curator.

## Does Sox3 belong in the neural crest network?

- **SoxB1 must be switched OFF for crest.** [PMID:30144418 "Interestingly, we found that inducing SoxB1
  activity at the neural plate border at these stages led to down-regulation of neural crest factors Foxd3
  and Snail2 (Figure 3B, S1C)."]; [PMID:30144418 "By contrast Sox2 or Sox3 showed little or no ability to
  rescue Foxd3 expression."]; [PMID:30144418 "Consistent with important sub-functionalization, we find
  that SoxE factors promote the neural crest cell state whereas SoxB1 factors inhibit the formation of
  neural crest cells (Figure 3B, 7D)."]. Rogers 2009: Sox3 overexpression delays then abnormally expands
  crest specifiers, ending in loss of crest cartilage [PMID:18992330 "Therefore, Sox3-overexpression causes
  a delay and then abnormal expansion of neural crest specifier genes."].
- SoxE substitutes for SoxB1 in blastula pluripotency only when overexpressed [PMID:30144418 "Thus,
  although they are not normally expressed in pluripotent cells of the blastula, Sox9 and Sox10 do have the
  ability to maintain pluripotency, although they may do so less robustly than SoxB1 factors do."].
- **Participation test.** Sox3's link to crest is (a) upstream — it is part of the maternal/blastula
  SoxB1 state that crest precursors pass through, and it is required for ectoderm to become neural; and
  (b) its *removal* from the border. A factor that must be switched off does no work of crest formation;
  specification is done by SoxE, Snail, FoxD3. All crest evidence is gain-of-function; no Sox3 loss of
  function expands the crest. Sox3's border expression at late gastrula [PMID:25931449] is transient and
  is lost from the crest by neurula. **No GO:0014029 / GO:0014036, and no GO:0090301.**
- **Comparator check (QuickGO 2026-10-07; descendants via is_a/part_of/regulates of GO:0014029,
  GO:0090299, GO:0014033, GO:0014032):** zero annotations for human SOX3 (P41225), mouse Sox3 (P53784),
  zebrafish sox3 (Q6EJB7), X. tropicalis sox3 (Q68FA4), X. laevis sox3-a (P55863), sox3-b (Q5FWM3), human
  SOX2 (P48431), mouse Sox2 (P48432), zebrafish sox2 (Q6P0E1), X. laevis sox2 (O42569). No SoxB1 protein
  carries any crest process term (positive or negative) in any species. Consistent with the reading above
  and with the sox2 review.
- Stem-cell maintenance comparator (GO:0019827 descendants): only mammalian SOX2 carries them (human
  GO:0035019 IDA/IMP, GO:0097150 ISS; mouse GO:0019827 IMP x3, GO:0097150 IGI); no SOX3 in any species.
- **Network layer.** Sox3 is a maternal/blastula transcription factor (germ-layer patterning, ZGA,
  pluripotency) and then a neuroectoderm competence / neural plate gene. It is NOT a member of the module's
  `progenitor_competence_maintenance` part (Myc, Id3, Hairy2, Oct25: factors that stay on in border/crest
  progenitors and whose loss causes crest progenitor loss). If represented at all, SoxB1 (Sox2/Sox3 as a
  set) belongs as the upstream blastula competence state that is handed off to SoxE before crest
  specification — a knowledge-gap / boundary note, not an annoton with a crest term.
- **OCT4–SOX2–TFAP2A gap.** In the frog blastula the Oct/Sox pair is Pou5f3–Sox3 at ZGA enhancers
  [PMID:37787392]. Sox3 is excluded from crest by neurula, so any redeployment of an Oct–SoxB1 complex to
  TFAP2A-bound crest enhancers (described for mammalian OCT4–SOX2 in the module deep research) is unlikely
  to involve frog Sox3 in definitive crest; Oct25 (pou5f3.2) stays at the border while SoxB1 leaves —
  if Oct25 has a crest partner it is more plausibly SoxE. Raised as a question.

## Evolution

- SoxB1 blastula + neural roles are ancestral: [PMID:39060477 "invertebrate chordates do express homologs
  of the neural stem cell factors soxB1 and myc in the blastula"]. IBA neuron-differentiation node
  includes Drosophila SoxNeuro/Dichaete and C. elegans donors.
- The SoxB1 → SoxE hand-off at the border is conserved in lamprey [PMID:39060477 "Orthologs of soxB1 were
  also expressed in the blastula, gastrula ectoderm and neural plate border, but then downregulated in
  premigratory neural crest"], dating it to the vertebrate ancestor. The novelty is SoxE recruitment into a
  blastula-like potency programme, not a change in SoxB1.
- Pou5 factors (vertebrate-specific) expand sox3 in the neural plate [PMID:39060477 "Strikingly, we found
  that all pou5 orthologs also expanded sox3 expression in the neural plate"].
- Maternal SoxB1 nodal repression is conserved with zebrafish (anti-SOX3c antibody cross-reacts and
  raises cyclops) [PMID:15302595].
- X. laevis allotetraploidy: Pou5f3/Sox3 binding differs between L and S subgenomes [PMID:37787392].

## Action summary (29 GOA rows + 2 NEW)

See review YAML. ACCEPT: transcription MF/BP, DNA binding, nucleus, repression of xnr5, germ layer
formation. Non-core: cytoplasm, brain development, neuron differentiation, cell differentiation, beta-catenin
binding, BMP and Wnt antagonism. NEW: GO:0141064 zygotic genome activation (IMP+IDA PMID:37787392);
GO:0021990 neural plate formation (IMP PMID:18992330).
