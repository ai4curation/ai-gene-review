# myc-a (Xenopus laevis, P06171) review notes

## Identity

- UniProt P06171, "Transcriptional regulator Myc-A" (AltName c-Myc I); Xenbase myc.S
  (XB-GENE-6053022). Homeolog myc-b is P15171. Both entries carry an identical set of 11
  electronic/phylogenetic GO annotations (QuickGO, checked 2026-10-01), with no
  experimental annotation on either.
- bHLH-LZ protein of the Myc family (IPR002418, IPR003327, IPR011598). UniProt FUNCTION is
  by similarity to human MYC P01106: binds 5'-CAC[GA]TG-3' E-boxes as a heterodimer with MAX.
- Two Xenopus c-myc genes differ mainly in UTRs; c-myc I is the major maternal mRNA and is
  re-expressed zygotically after gastrulation, while c-myc II is maternal only
  [PMID:2686981 "It is the major mRNA species expressed during oogenesis and is expressed again from the zygotic genome in post-gastrula embryos"].
- NOTE: the UniProt DEVELOPMENTAL STAGE line says the opposite ("C-MYC I is active in
  oocytes, while C-MYC II is active in both oocytes and post-gastrula embryos"). The
  c-myc I/II naming may differ between Vriz et al. 1989 and Principaud & Spohr 1991
  (PMID:2057364). Which homeolog (L or S) carries the zygotic expression is therefore not
  settled from the cached sources. Raised as a suggested question.

## Molecular activity

- Canonical vertebrate Myc-Max E-box transcription factor; the activity is inferred from
  domain structure and the PANTHER node (IBA), consistent with human MYC
  (genes/human/MYC core function: GO:0000981, Myc-Max complex, GO:0046983).
- The xc-myc1 gene transforms primary mammalian cells, so the frog protein is functionally
  equivalent to mammalian c-Myc in that assay
  [PMID:8455622 "this homology was consistent with the ability of the xc-myc1 and xN-myc1 genes to function as oncogenes in primary mammalian cells"].
- Stage-specific exception: in the transcriptionally silent cleavage embryo, nuclear c-Myc
  does not bind DNA with Max, and embryonic nuclei dissociate Myc/Max complexes
  [PMID:7651422 "During early development, when the entire embryonic genome is transcriptionally inactive, c-Myc does not exhibit a DNA binding activity with Max"].
  The protein is stored in oocyte cytoplasm and enters nuclei after fertilization
  [PMID:7651422 "Fertilization triggers the selective and total entry of only p64 c-Myc into the nucleus"].
  These protein studies do not resolve the two c-myc genes.

## Neural crest: network layer

- Expression: c-myc is at the neural plate border before slug
  [PMID:12791268 "c-myc is localized at the neural plate border prior to the expression of early neural crest markers, such as slug"].
  Earlier, Myc is expressed in pluripotent blastula cells and declines as explants lose
  potential [PMID:25931449 "Oct60, Sox3, FoxD3, and Myc expression was high in blastula-stage explants but reduced by late gastrula stages, correlating with loss of potential"].
  It is classed with the NC "potency factors" first expressed in naive blastula cells
  [PMID:30144418 "Many neural crest potency factors are first expressed in naïve blastula cells, including Snail1, Myc, Foxd3, Ets1, Ap2, and Vent2"].
- Loss of function: morpholino knockdown removes NC precursors and derivatives, without a
  change in proliferation or death
  [PMID:12791268 "A morpholino-mediated \"knockdown\" of c-Myc protein results in the absence of neural crest precursor cells and a resultant loss of neural crest derivatives"];
  [PMID:12791268 "These effects are not dependent upon changes in cell proliferation or cell death"].
  The morpholino targets a region shared by the c-myc variants and rescue used a c-Myc
  II-like cDNA (deep research summary of the full text), so the result applies to Xenopus
  c-Myc collectively, not to myc-a alone (homeolog issue).
- Downstream target: Id3 is a Myc target required for NC progenitor formation; Myc is
  proposed to prevent premature fate decisions in NC-forming ectoderm
  [PMID:15772131 "recent work has suggested that Myc functions to prevent premature cell fate decisions in neural crest forming regions of the early ectoderm"];
  [PMID:15772131 "Id3 is a Myc target that plays an essential role in the formation and maintenance of neural crest stem cells"].
- Chick: cMyc is expressed later, in the dorsal neural tube, and maintains the size of the
  premigratory NC stem cell pool by self-renewal through a non-canonical Myc/Miz1 complex
  [PMID:27926868 "rather than via E-Box binding, cMyc acts in the dorsal neural tube by interacting with another transcription factor, Miz1, to promote self-renewal"].
  The paper notes the frog/chick switch in c-Myc vs N-Myc expression
  [PMID:27926868 "In the frog, the expression of these paralogs is switched such that cMyc is expressed early in the neural plate border"].

### Layer placement

Myc is neither a classical border specifier (Pax3/Zic1/Msx1) nor a crest specifier
(Sox10/FoxD3/Snai2). It is a blastula-inherited competence / potency factor that is retained
at the neural plate border and is required, upstream of slug and Id3, for NC precursors to
form. The best-supported GO process is therefore GO:0014029 neural crest formation (the
broader term), not GO:0014036 neural crest cell fate specification. Comparator check:
X. laevis id3-a (Q91399, Myc's target, same layer) carries GO:0014029 by IMP (5 papers) and
zic1 carries GO:0014029 IMP. Human P01106, mouse P01108 and X. laevis P06171/P15171 c-Myc
carry no NC term, but the Myc family is not systematically absent: zebrafish mych carries
GO:0014032 neural crest cell development by IMP [PMID:18446220, "The mych gene is required
for neural crest survival during zebrafish development"; QuickGO check 2026-10-02]. So the
c-Myc gap reflects the Bellmeyer paper never having been curated, not a convention.
Stem cell population maintenance (GO:0019827) for the NC pool is supported in chick only;
left as a suggested question.

## Pleiotropic / non-core roles

- Positive regulation of cell proliferation (IBA): conserved family role, but the frog NC
  requirement is explicitly independent of proliferation, so non-core here.
- Maternal stockpile in oocytes; possible role linked to early replication cycles (Lemaitre
  1995; speculative). Thyroid hormone-driven c-Myc/PRMT1 role in intestinal stem cells at
  metamorphosis (review, paralog unresolved; deep research only).

## Evolutionary points

- Myc is part of the shared blastula/NC regulatory programme (PMID:25931449); the
  amphioxus single Myc and lamprey Myc border expression were not reviewed here (no cached
  source). The frog (c-Myc at border) vs chick (c-Myc late, N-Myc at border) switch
  suggests the NC requirement is for "Myc activity" rather than a specific paralog.
