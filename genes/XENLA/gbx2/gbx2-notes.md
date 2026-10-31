# gbx2 (Xenopus laevis, Q91907) review notes

Project: NEURAL_CREST_ORIGINS, Tier 2 (neural plate border specifiers).
Reviewed 2026-10-05 by claude-code.

## Identity and paralog/homeolog situation

- Q91907 (GBX2_XENLA, 340 aa) is the von Bubnoff 1996 Xgbx-2 cDNA; UniProt
  cross-references it to Xenbase `gbx2.2.L` (XB-GENE-866652). It is the only
  reviewed X. laevis Gbx entry.
- X. laevis carries four gbx2 copies (two paralogous genes, gbx2.1 and gbx2.2,
  each with L/S homeologs) plus gbx1.S. Pairwise global alignment against Q91907
  (BLOSUM62, run 2026-10-05 in scratch, sequences from UniProt REST):
  A0ACK5WZN6 gbx2.2.L 339/340 identical; A6H8J9 / A0AA58EVU7 gbx2.1.L 333/340;
  Q90YY2 ("Gbx2b", gbx2.S/gbx2.1.S) and A0A8J0PTF7 324 identical (336 aa);
  A0A1L8EPH5 gbx2.2.S 316/340.
- Tour et al. 2001 found two X. laevis Gbx2 genes [PMID:11684099 "Two Gbx2 genes
  were identified in Xenopus laevis, differing in 13 amino acids, including a
  change in the homeodomain."] and [PMID:11684099 "Both genes encode functionally
  homologous proteins, which differ primarily in their temporal and spatial
  expression patterns."]. Q90YY2 is the "Gbx2b" entry and differs from Q91907 at
  about this many positions, so Tour's Xgbx2a is most likely the Q91907 lineage.
  This is an inference from sequence, not a stated mapping.
- The Wnt-target paper (Li 2009) names "Gbx2" without a paralog. Yokota 2017
  refers to it as gbx2.2 [PMID:28695961 "However, unlike another Wnt/Ctnnb1
  target, gbx2.2, apoc1 is not required for patterning of the neural border."],
  which matches Q91907's Xenbase gene.
- **No X. laevis or X. tropicalis Gbx entry carries any experimental GO
  annotation.** All 13 Q91907 rows are IBA/IEA/TAS. The Xenopus Gbx2 literature
  (Li 2009, Steventon 2012, Tour 2002) is uncurated in GO.

## Expression

- [PMID:8652408 "Expression of Xgbx-2 is first detectable by in situ
  hybridization at the midgastrula stage when it is predominantly expressed in
  the dorsolateral ectoderm, with a gap in expression at the dorsal midline."]
- [PMID:8652408 "The anteriormost expression in the neural ectoderm persists
  throughout the early stages of development, and was mapped to the region of
  rhombomere 1, with an anterior expression border in the region of the
  midbrain-hindbrain boundary."]
- Early gbx2 sits between Otx2 and Xcad2 domains [PMID:11850185 "Early
  transcription of the Xenopus Gbx2 homologue, Xgbx2a, is spatially restricted
  between Otx2 and Xcad2."]
- BMP timing: [PMID:37489332 "Expression of gbx2 and hoxd1 was significantly
  reduced and only detectable from stage 11."] (after BMP inhibition), so gbx2 is
  in a BMP-sensitive, temporally ordered head-patterning sequence.
- In the pre-placodal region (PPR) gbx2 and otx2 form an abutting boundary:
  [PMID:22564795 "Thus, like in the neural plate, Gbx2 and Otx2 form a gene
  expression boundary within the PPR in Xenopus and chick."]

## Upstream: a direct Wnt target

- [PMID:19736322 "We show here that the homeobox gene Gbx2 is essential in this
  process and is directly activated by Wnt/beta-catenin signalling."]
- [PMID:19736322 "By ChIP and transgenesis analysis we show that the Gbx2
  regulatory elements that drive expression in the NC respond directly to
  Wnt/beta-catenin signalling."]
- Reactome R-XLA-9835542 models exactly this step (tcf7l1:ctnnb1 binding the gbx2
  promoter). Note: this is regulation *of* gbx2, not an activity *of* Gbx2.
- Conserved in zebrafish via the paralog gbx1 [PMID:19341460 "we propose that
  gbx1 acts at the transcriptional level to mediate Wnt8 posteriorizing effects
  on hindbrain patterning."]

## Molecular activity

- Homeodomain (residues 239-298, PROSITE PS50071); InterPro GBX-1/2 family
  IPR042982; PANTHER PTHR24334:SF3.
- Repressor in early ectoderm, frog data: [PMID:11850185 "Using obligatory
  activator and repressor versions of Xgbx2a, we demonstrate that, during early
  embryogenesis, Xgbx2a acts as a transcriptional repressor."]
- Repressor in the PPR, frog/chick: [PMID:22564795 "Together, these results
  demonstrate that in the PPR Otx2 and Gbx2 act as transcriptional repressors and
  mutually repress each other suggesting that this interaction generates the
  Gbx2/Otx2 expression boundary."]
- But an activator for otic genes: [PMID:22564795 "Gbx2 is required for the
  onset of otic-specific genes, where it appears to act as transcriptional
  activator: the constitutive repressor Gbx2-EnR mimics MO-mediated
  knock-down."] and [PMID:22564795 "This is in contrast to its earlier role as
  repressor during boundary formation (see above) suggesting that the
  availability of cofactors determines the final outcome as observed for other
  homeobox factors"]. So GO:0000981 (generic RNAPII TF) remains the right core
  MF, and GO:0001227 is added as NEW for the well-evidenced repressor mode.
  Mouse Gbx2 carries GO:0001228 activator by IDA (PMID:23144817); I did not add
  GO:0001228 for frog, since the frog activator evidence is indirect (EnR
  phenocopy only).
- Repression mechanism (cell culture plus medaka, not frog): eh1-like motif binds
  Groucho/TLE [PMID:17060451 "we show that engrailed homology region 1
  (eh1)-like motifs of both transcription factors physically interact with the
  WD40 domain of Groucho/Tle corepressor proteins."] and [PMID:17060451
  "Groucho is required for the repression of Otx2 by Gbx2"]. Not used for a frog
  NEW GO:0001222, because the protein tested was not Xenopus Gbx2 and the cached
  text is abstract-only. Raised as a question.

## Network position: neural plate border specifier

- Li 2009 (abstract only in cache, PMC2808295; Europe PMC full-text fetch failed
  with HTTP 500 on 2026-10-05; the falcon deep research quotes the full text):
  - [PMID:19736322 "Loss-of-function experiments using antisense morpholinos
    against Gbx2 inhibit NC and expand the preplacodal domain, whereas Gbx2
    overexpression leads to transformation of the preplacodal domain into NC
    cells."]
  - [PMID:19736322 "We show that the NC specifier activity of Gbx2 is dependent
    on the interaction with Zic1 and the inhibition of preplacodal genes such as
    Six1."]
  - [PMID:19736322 "In addition, we demonstrate that Gbx2 is upstream of the
    neural fold specifiers Pax3 and Msx1."]
  - [PMID:19736322 "Our results place Gbx2 as the earliest factor in the NC
    genetic cascade being directly regulated by the inductive molecules, and
    support the notion that posteriorization of the neural folds is an essential
    step in NC specification."]
  - Deep research (full text): two MOs inhibit snail2, rescued by MO-resistant
    Gbx2; Pax3 or Msx1 RNA rescues Gbx2 MO but Gbx2 does not rescue Pax3/Msx1
    loss; at the doses used regional neural plate markers (otx2, en2) were
    largely unchanged. That last point means the NC effect is a neural-fold
    (border) patterning role, separable from neural plate AP patterning.
- Field consensus that Gbx2 is a border specifier, not a crest specifier:
  [PMID:24360906 "These neural border specifiers include the transcription
  factors Pax3, Pax7, Gbx2, Msx1, Zic1, AP2, and Hairy2, which are essential for
  further neural crest development but not always maintained in the neural crest
  progenitors themselves"] and [PMID:23509273 "In addition, Pax3/Pax7, Gbx2, and
  Zic1 are also essential for neural border specification"].
- Gbx2 also turns up among Pax3+Zic1-induced genes in animal caps
  [PMID:24360908 "This group included 10 well-characterized NC-specific genes:
  ednra, foxd3, gbx2, olig4, snail2, sox8, sox9, tcf7, twist and zic5 (Table
  2)."], so there is feedback within the border module, but Li 2009 places Gbx2
  upstream of Pax3.

**Layer placement:** border specifier. It is a direct Wnt target, acts upstream
of pax3/msx1 and in parallel with Zic1, and works by giving the neural fold a
*posterior* identity, which separates crest (posterior border) from anterior
placodal (six1) fate. It is not a crest specifier: it does not activate the crest
programme alone, and it needs Zic1.

## NC-branch term decision: GO:0014029 (not GO:0014036)

- GO:0014029 neural crest formation (QuickGO definition): "The formation of the
  specialized region of ectoderm between the neural ectoderm (neural plate) and
  non-neural ectoderm."; GO:0014036 is part_of GO:0014034, which is part_of
  GO:0014029.
- Gbx2 acts on the border region as a whole: it positions the crest/placode
  split along the AP axis and acts upstream of the other border genes. By the
  pending project convention (specifiers narrowed to GO:0014036; non-specifiers
  and border genes keep GO:0014029), GO:0014029 is the right level. GO:0014036
  would claim Gbx2 makes cells autonomously crest, which Li 2009 contradicts:
  Gbx2 activity "is dependent on the interaction with Zic1".
- Added as NEW (IMP, PMID:19736322) because Q91907 has no NC term at all.

### Comparator checks (QuickGO, 2026-10-05)

1. All Gbx accessions in human, mouse, rat, chick, zebrafish, X. laevis and
   X. tropicalis (30 accessions from UniProt REST query
   `(gene:gbx2 OR gene:gbx1 OR gene:gbx2.1 OR gene:gbx2.2 OR ...) AND
   (organism_id:8355 OR 8364 OR 9606 OR 10090 OR 10116 OR 7955 OR 9031)`), then:
   `https://www.ebi.ac.uk/QuickGO/services/annotation/downloadSearch?geneProductId=<30 ids>&goId=GO:0014029&goUsage=descendants&goUsageRelationships=is_a,part_of,occurs_in`
   gives **0 rows**. With goId=GO:0014032 / GO:0014033 / GO:0001755 descendants:
   mouse Gbx2 P48031 carries GO:0001755 neural crest cell migration by IMP
   (PMID:15996652, PMID:19700621, PMID:23144817), and rat G3V8J6 by ISO.
   So the Gbx family is **not** systematically excluded from the NC branch. The
   frog gap reflects uncurated literature (Q91907 has no experimental rows), not
   a convention.
2. Same-layer peers, exact GO:0014029 query on Q645N4 (pax3-a), O73689 (zic1),
   Q90Z12 (hes4-a): hes4-a 4x IMP; pax3-a IMP + IGI; zic1 4x IMP + 1 IEA.
   pax3-a and zic1 additionally carry GO:0014034 (IMP/IGI). **None** carries
   GO:0014036. GO:0014029 for gbx2 matches its border-specifier peers.
3. Neural plate pattern terms: GO:0060897 neural plate regionalization has a
   single non-electronic annotation in all of GO (zebrafish bmp7b), and no Gbx
   carries GO:0060896/GO:0060897. Not used.
4. GO:0030917 midbrain-hindbrain boundary development (exact): mouse Gbx2 IMP
   (PMID:16651541); X. laevis irx1-a IMP (PMID:11923198), also a frog MHB
   homeobox gene; plus zebrafish fgf8a, her5 and others. Mouse Gbx2 and zebrafish
   gbx1 also carry GO:0021555 MHB morphogenesis (IMP). Supports a NEW
   GO:0030917 for frog gbx2.
5. GO:0043049 otic placode formation (exact): used for zebrafish otic TFs (foxi1,
   dlx3b/4b, msx1a/b) and X. laevis lsm14a-a; mouse Gbx2 carries GO:0042472
   inner ear morphogenesis (IMP). Supports a NEW GO:0043049 for frog gbx2.

## Midbrain-hindbrain boundary / posterior neural plate

- [PMID:11850185 "Xgbx2a is a negative regulator of Otx2 and a weak positive
  regulator of Xcad2."]
- [PMID:11850185 "we show that the ability of Xgbx2a to induce head
  malformations is restricted to gastrula stages and correlates with its ability
  to repress Otx2 during the same developmental stages."]
- [PMID:11744364 "In contrast, Gbx2 is a negative regulator of Otx2 and the MHB
  genes."]
- [PMID:9707329 "misexpression of Xgbx-2 prevents N-cadherin expression during
  early neurulation"]. This is gain of function only; the adhesion link is
  indirect.
- Frog evidence here is mostly gain of function plus an inducible antimorph. The
  necessity evidence comes from mouse Gbx2 (human GBX2 review, PMID:10490024,
  PMID:21266408). Synthesized: MHB development is a conserved core role.

## Placodes

- Otic: [PMID:22564795 "Gbx2 knock-down by splice- and translation-blocking
  morpholinos prevents the expression of the otic markers Pax8 and Pax2"];
  [PMID:22564795 "Thus, Gbx2 is required for otic, but not for PPR
  specification."]; [PMID:22564795 "Thus, while Gbx2 is not sufficient to impart
  otic identity to non-otic cells, it plays a dual role during otic
  specification: it restricts Otx2 (which otherwise inhibits posterior fate; see
  below) and provides a positive input for otic specifiers."]
- Later cell behaviour: [PMID:27659690 "Automatic cell tracking reveals that
  when Gbx2 targets are repressed, the persistence of movement is decreased"].
  This is an engineered EnR fusion; no GO term is proposed for it.

## Evolution / outgroups

- Amphioxus has a single Gbx with a posterior domain abutting Otx [PMID:16687133
  "Amphioxus Gbx is expressed in all germ layers in the posterior 75% of the
  embryo, and in the CNS, the Gbx and Otx domains abut at the boundary between
  the cerebral vesicle (forebrain/midbrain) and the hindbrain."] and
  [PMID:16687133 "Thus, the genetic machinery to position the MHB was present in
  the protochordate ancestors of the vertebrates, but is insufficient for
  induction of organizer genes."]. The Otx/Gbx AP-positioning function is
  ancestral to chordates; organizer properties are vertebrate.
- [PMID:18836256 "However, migratory neural crest is lacking in amphioxus, and
  although it has homologs of the genes that specify neural crest, they are not
  expressed at the edges of the amphioxus neural plate."]. Gbx is a positional
  (AP) gene in amphioxus; I found no report of amphioxus Gbx being specifically
  border-restricted.
- *Ciona* has lost Gbx [PMID:12736825 "loss of genes had occurred independently
  in the Ciona lineage and was noticed in Gbx of the EHGbox subclass"]. The
  tunicate border/"rudimentary NC" (a9.49) therefore works without Gbx, which
  argues that Gbx2's NC role is not a requirement of the ancestral border
  programme. Caveat: Ciona has lost many genes.
- Lamprey: gbx2 shows NPB dynamics like Xenopus [PMID:39060477 "In both lamprey
  and Xenopus, clusters with this signature included canonical neural plate
  border factors such as prdm1, gbx2 and wnt8 (Fig."]. In the same analysis myc,
  pax3, msx1 and zic1 had these dynamics in Xenopus but not lamprey. Gbx2 at the
  border is therefore at least as old as crown vertebrates. PubMed eutils for
  `Gbx[tiab] AND lamprey[tiab]` returned 0 hits, so no lamprey functional data.
- Interpretation: Gbx protein activity (posterior homeodomain repressor, Otx
  antagonist) is chordate-ancestral. Its use to split the border into posterior
  crest versus anterior placode looks like a vertebrate deployment of an
  ancestral AP-patterning gene. This is an "ancestral activity, new context"
  case, like Id/SoxE in Tier 1, except that the gene was already in the
  ectoderm.

## Decisions summary

- All MF IBA/IEA rows ACCEPT except GO:0003677 (MODIFY to GO:0000977, as in
  human GBX2).
- GO:0006355 MODIFY to GO:0006357 (as in human).
- GO:0051960 IBA/IEA: KEEP_AS_NON_CORE (as in human; true but broad; the
  specific processes are added as NEW).
- Location rows ACCEPT.
- NEW: GO:0014029 (IMP PMID:19736322), GO:0001227 (IMP PMID:11850185 plus
  PMID:22564795), GO:0030917 (IMP PMID:11850185), GO:0043049 (IMP
  PMID:22564795).
- Not added: GO:0001228 (frog activator evidence indirect), GO:0001222
  (TLE binding shown with non-frog protein), GO:0060897 (essentially unused
  term), GO:0014036 (wrong layer), cell adhesion or migration terms (indirect).

## Homeolog caveat

All NEW rows sit on Q91907 (gbx2.2.L). The morpholinos (Li 2009) and Tour's
Xgbx2a constructs cannot be mapped to a single copy from the abstracts, and the
four X. laevis gbx2 copies are 93-99.7% identical. The same evidence plausibly
covers gbx2.2.S and the gbx2.1 pair. Not fixed by assertion.
