# spz (Spätzle, P48607) — review notes

## Status of inputs
- UniProt, GOA (91 rows, 89 seeded annotations after de-duplication) and all 35 GOA PMIDs are cached.
- The review was drafted from UniProt, GOA and the cached primary literature; Falcon deep research
  (spz-deep-research-falcon.md) completed afterwards and was checked for consistency.

## Identity and structure
- Secreted cystine-knot protein, synthesised as a disulfide-linked dimeric pro-protein; many
  maternal splice isoforms share the C-terminal cystine-knot domain (C-106) and differ in the
  pro-domain [UniProt P48607; PMID:18790733 "Through alternative splicing, the Spätzle gene encodes
  for several isoforms that (with one exception, the "propeptide isoform") share C106 but differ in
  the prosequence."].
- Easter cleaves pro-Spz after Arg220 to release C-106, a disulfide-linked NGF-like dimer
  [PMID:9533958 "An active form of Easter protease cleaves the Spätzle protein, generating a
  carboxyterminal polypeptide fragment which, when microinjected into the perivitelline space of a
  spätzle deficient embryo, directs production of ventrolateral pattern elements."].
- During immunity the cleaving enzyme is SPE [PMID:16399077 "Here, we report a protease, called
  Spätzle-processing enzyme (SPE), required for Toll-dependent antimicrobial response."]; an
  SPE-independent protease can also process Spz [PMID:26843333 "Our data suggest that an
  unidentified protease besides SPE processes Spätzle under conditions of microbial challenge."].
- The pro-domain is needed for folding/secretion and masks the Toll-binding determinants
  [PMID:17324925 "Here we show that before processing the pro-domain of Spätzle is required for
  correct biosynthesis and secretion."].

## Molecular function: Toll ligand (cytokine)
- Direct high-affinity binding of mature Spz to the Toll ectodomain; pro-Spz inactive
  [PMID:12872120 "in vitro experiments showed that the mature form of Spätzle bound to the Toll
  ectodomain with high affinity and with a stoichiometry of one Spätzle dimer to two receptors"].
- Crystal structures: Spz C-106 dimer binds the concave face of the membrane-distal LRR domain of
  Toll, asymmetric, neurotrophin-like [PMID:24733933 "Spätzle binds to the concave surface of the
  membrane-distal LRR domain"; PMID:24282309 "Spz C106 interacts via its cystine-knot structure in
  an asymmetric binding mode that is reminiscent of the neurotrophin NGF bound to the receptor p75
  NTR"].
- Spz-1 also binds Toll-7 in co-IP and activates the drosomycin promoter through Toll-1 and Toll-7
  in S2 cells [PMID:31088910 "Thus, three Spz family members (Spz-1, -2, and -5) exhibit features
  consistent with functioning as cytokines that bind to Toll-1 and Toll-7, which activates downstream
  Toll signaling and the drosomycin promoter."].
- Toll is not a PRR: Spz is an endogenous ligand [PMID:12872120 "These results show that, in
  contrast to the human Toll-like receptors, Drosophila Toll requires only an endogenous protein
  ligand for activation and signaling."; PMID:31088910 "However, vertebrate TLRs do not bind
  cytokines like Spz-1 but instead function as pattern recognition receptors (PRRs)"].

## Processes
- Embryonic dorsal-ventral patterning: ventrally processed Spz defines where Toll is active
  [PMID:8124709; PMID:8026333].
- Immunity: Spz/Toll/Cactus control drosomycin and antifungal defence [PMID:8808632]; required for
  resistance to Gram-positive bacteria [PMID:11823479]; for defence against fungi and Gram-positive
  bacteria but not Gram-negative bacteria in the DIAP2 study [PMID:16894030 "a mutation in the
  spatzle gene ( spatzle rm7 ), which blocks Toll activation, sensitized animals only to infection by
  gram-positive bacteria and fungi"].
- Haemocyte-derived Spz drives Toll-dependent drosomycin in larval fat body [PMID:19934223].
- Neurotrophic roles (with DNT1/DNT2): CNS neuron survival, SNa motor axon targeting
  [PMID:19018662 "Apoptosis increases in the CNS of spz2 and Tollr3/Df(3R)ro80b mutant embryos,
  indicating that both Spz and Toll are required for neuronal survival"].
- Other contexts, all via Toll signalling: epidermal requirement for muscle patterning
  [PMID:9676200], cell competition [PMID:30146479], tumour response in fat body [PMID:24582964],
  wound-induced epidermal gene expression downstream of H2O2 [PMID:28289197].

## Substrate / participation analysis (proteolysis terms)
- GO:0160032 "Toll receptor ligand protein activation cascade" (part_of GO:0140448 signaling
  receptor ligand precursor processing) describes the protease cascade that cleaves pro-Spz.
- Comparator check (QuickGO, D. melanogaster, 2026-09-30): the term is carried by the proteases
  and recognition factors (SPE, ea, snk, gd, psh, modSP, grass, Hayan, MP1, ndl, pip, GNBP1/3,
  PGRP-SA ...) and **not** by spz. GO:0140448 likewise sits on the processing enzymes
  (BACE1, ADAM10, ADAM17, MEP1A, CASP1) and not on their substrates.
- Spz supplies no catalytic, scaffold or cofactor work to its own cleavage: it is the substrate
  and product. No NEW annotation to GO:0160032 / GO:0140448 / proteolysis is proposed. The
  enzyme–substrate relationship belongs on SPE/Easter as `has input`.
- In contrast, the Toll signalling pathway starts with ligand binding to Toll (GO:0008063
  definition), so Spz as the ligand does participate and those rows are accepted.
- No GO-CAM in gocams/index.tsv contains spz.

## Questionable rows
- GO:0007310 oocyte dorsal/ventral axis specification (IEP, PMID:8124709): oocyte axis polarity is
  set in the follicle/oocyte upstream (gurken, pipe); spz acts post-fertilisation in the
  perivitelline space. The general GO:0009950 is already present with IDA/IGI support.
- GO:0050829 defense response to Gram-negative bacterium (IMP, PMID:26843333): abstract-only; the
  abstract mentions only M. luteus and B. subtilis (Gram-positive) challenge; conflicting with
  PMID:16894030. Left UNDECIDED.
- GO:0045087 innate immune response (IDA, PMID:17018283): abstract is about human RalB/TBK1; full
  text not cached. Function is clearly correct for spz, so accepted in deference to the curator.
- GO:0010628 positive regulation of gene expression (IMP, PMID:34432851): too general; the paper is
  about the Toll-regulated antifungal Baramicin; proposed MODIFY to GO:0002804.

## Deep research status
- spz-deep-research-falcon.md (completed 2026-09-30) agrees with the review: Spz is a secreted,
  non-enzymatic cystine-knot cytokine, activated by Easter (embryo) or SPE/MP1 and other proteases
  (immunity, damage), acting in the perivitelline space and haemolymph; Toll-1 is the established
  receptor and Toll-7 binding is less firmly established. Its statement that Gram-negative bacteria
  can activate the pathway draws largely on other insects (e.g. Tenebrio), so it does not resolve
  the GO:0050829 row, which stays UNDECIDED. No annotation changes resulted.
