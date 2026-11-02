# sox9-a (Xenopus laevis, UniProt B7ZR65) - review notes

Project context: `projects/NEURAL_CREST_ORIGINS.md`, Tier 1 (neural crest specifiers).
Homeolog: sox9-b (Q6DFF5). Cross-check: `genes/human/SOX9/`.

## Identity and molecular activity

- SoxE-group HMG-box transcription factor, 477 aa; HMG box 105-173, dimerization
  domain 63-103, transactivation domains TAM (224-308) and TAC (361-477), all by
  similarity to human SOX9 [file:XENLA/sox9-a/sox9-a-uniprot.txt "DNA_BIND        105..173"].
- Activator in vivo in Xenopus: an HMG-box/engrailed-repressor fusion phenocopies
  the morpholino [PMID:15464575 "Expression of a construct in which Sox9 DNA-binding domain (HMG box) is fused to the repressor domain of Drosophila engrailed blocked neural crest formation"];
  [PMID:15464575 "we demonstrate that Sox9 functions as a transcriptional activator during neural crest formation"].
  This is the best evidence for GO:0001228 (DNA-binding transcription activator
  activity, RNA polymerase II-specific). No Xenopus evidence for a repressor role;
  GO:0000122 (IBA) comes from mammalian/other SoxE members and is kept as non-core.
- SUMOylation at K61 and K365 switches output between crest/melanocyte-promoting and
  otic-promoting activities [PMID:16256735 "the activities of individual SoxE factors are well conserved and are regulated by SUMOylation"];
  [file:XENLA/sox9-a/sox9-a-uniprot.txt "Lys-365 is the major site of sumoylation"].
  The IPI rows with Ube2i (P63282) and Sumo1-a (O57686) reflect Sox9 being a SUMOylation
  substrate, not a binding function of Sox9 itself.
- Nucleus (functional site). Cytoplasm transferred from X. tropicalis Sox9 (Q6F2E7),
  where it is cytoplasmic in previtellogenic oocytes - a storage/oocyte localisation
  [file:XENLA/sox9-a/sox9-a-uniprot.txt "localizes to the cytoplasm of previtellogenic oocytes in the ovary"].

## Expression (where/when)

- Maternal, then from mid-gastrula at the lateral edges of the neural plate; persists in
  migrating cranial crest into the pharyngeal arches [PMID:11807034 "It is expressed maternally and accumulates shortly after gastrulation at the lateral edges of the neural plate, in the neural crest-forming region"].
- Order of onset in Xenopus SoxE: Sox8 precedes Sox9, which precedes Sox10
  [PMID:16943273 "in contrast to its mouse and chick orthologs, Sox8 expression precedes that of Sox9 and Sox10 in neural crest progenitors"].
- Also otic placode from stage 13/14, eye, genital ridges, notochord, pancreas
  (UniProt tissue specificity).

## Loss / gain of function

- MO: loss of NC progenitors with expansion of neural plate; later loss of NC-derived
  cranial skeletal elements [PMID:11807034 "causes a dramatic loss of neural crest progenitors and an expansion of the neural plate"].
- Required for Wnt-mediated NC induction, and needed for specification but not for
  migration [PMID:15464575 "Wnt-mediated neural crest induction is inhibited in the context of Sox9-depleted embryos"];
  [PMID:15464575 "we show that Sox9 function is required for neural crest specification but not for its subsequent migration"].
- Sox9 rescues Sox10 MO; SoxE proteins are functionally interchangeable
  [PMID:16256735 "Sox9 and the closely related factor Sox10 are essential for the formation of neural crest precursor cells"].
- Otic placode: MO loses Pax8/Tbx2; inducible dominant-negative shows placode
  specification, not patterning, requires Sox9
  [PMID:15084460 "we demonstrate that Sox9 function is required for otic placode specification but not for its subsequent patterning"].
- Gain of function expands crest/otic markers (deep research summary of Taylor and
  LaBonne 2005; full text not cached here).

## Network layer

Sox9 is a **neural crest specifier**, not a neural plate border specifier and not a
competence/pluripotency factor:
- it acts downstream of Wnt-driven induction (required for it) and its expression follows
  Sox8 at the border;
- its loss converts crest to neural plate fate (a fate-specification phenotype);
- it is dispensable for migration once specified;
- it is later reused in the crest-derived chondrogenic lineage.
So the appropriate process term is `GO:0014036 neural crest cell fate specification`
(a part/descendant of `GO:0014029 neural crest formation`). The existing IMP rows use
the broader `GO:0014029`. I MODIFY the Spokony 2002 row (the phenotype it reports is a
specification phenotype) and keep the other two, which I cannot read beyond the abstract,
at the broader term. GO lacks a neural plate border term; not needed for this gene.

## Chondrogenesis (core, ancestral)

- Xenopus MO loses neural crest-derived skeletal elements [PMID:11807034 "morpholino-treated embryos have a specific loss or reduction of neural crest-derived skeletal elements"].
- Deep research (Schock & LaBonne 2020 review): loss of Meckel's cartilage in morphants.
- Conservation: lamprey Sox9 is co-expressed with Col2a1 in the developing skeleton
  [PMID:16492784 "the genetic pathway for chondrogenesis is conserved in lampreys and gnathostomes from earliest Sox9 expression through cartilage matrix gene activation"].
- Amphioxus SoxE is expressed in the gill bars (cellular cartilage-like skeleton) - PMID:18369444,
  not cached; mentioned only.

## Evolution (for project synthesis)

- Lamprey has three SoxE genes; SoxE1 and SoxE2 are needed for the chondrogenic crest
  [PMID:21889937 "Our results suggest that SoxE1 and SoxE2 are required for specification of the chondrogenic neural crest"].
  The SoxE duplications in agnathans and gnathostomes were independent
  [PMID:21889937 "our results also have implications for understanding the independent evolution of duplicated SoxE genes among agnathan and gnathostome vertebrates"],
  so one-to-one Sox9 orthology to lamprey SoxE genes should not be assumed.
- Recruitment of SoxE into the crest is at the cis-regulatory level: amphioxus soxE is
  not co-expressed with AP2 and lacks crest enhancers [PMID:22241841 "because AP2 and SoxE are not co-expressed in amphioxus, and because neural crest enhancers are not detected proximal to amphioxus soxE"].
- Interpretation: the SoxE protein activity (HMG-box activator, chondrogenic program)
  is ancestral; the deployment in the border/crest is a vertebrate novelty.

## Homeologs

All experimental (IMP/IDA/IPI) annotations are attached to sox9-a (B7ZR65). The
morpholinos and the mRNA constructs in these papers were described as "Sox9"; whether they
distinguish the L and S homeologs is not stated in the abstracts. Do not transfer by
assertion; note as question.

## Pleiotropy: core vs non-core

- Core: Pol II activator activity; NC cell fate specification; chondrocyte
  differentiation/cartilage development (cranial crest-derived).
- Non-core: otic placode formation (real, well-supported but a separate deployment);
  heart development, epithelial morphogenesis, oligodendrocyte differentiation (IBA,
  no Xenopus data); mouse-derived growth-plate, osteoblast, fatty-acid and Wnt terms.
- Sex determination: Xenopus laevis uses DM-W, not a Sox9-centred mechanism; expression in
  genital ridges only. No annotation exists or is proposed.
