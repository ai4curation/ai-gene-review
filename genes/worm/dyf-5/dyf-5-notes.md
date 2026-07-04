# dyf-5 (C. elegans) research notes

UniProt: B3WFY8 (DYF5_CAEEL). WormBase: WBGene00001121 / M04C9.5. Gene name "dyf-5"
(dye filling defective-5). 489 aa. Protein kinase domain 11-291; ATP-binding Lys at
17-25/40; catalytic Asp/proton-acceptor at 132. Two isoforms (b = B3WFY8-1 displayed;
a = B3WFY8-2). Family: protein kinase superfamily, CMGC group, RCK subfamily
(MAK/ICK/CILK1-related); human relatives MAK, ICK/CILK1, MOK.

## Summary of what is KNOWN

DYF-5 is a ciliary serine/threonine protein kinase of the MAK/RCK (CMGC) family
that governs the length, morphology and intraflagellar-transport (IFT) dynamics of
*C. elegans* sensory-neuron cilia. It is expressed in ciliated head and tail sensory
neurons and enriched at the transition zone / distal ciliary segments; loss of
function gives long, misshapen, misaligned cilia with IFT-protein accumulation (the
"dye-filling defective" ciliary phenotype).

### 1. Molecular function — protein serine/threonine kinase (CORE)
- Two independent studies directly demonstrate DYF-5 kinase activity **in vitro** on
  purified/recombinant ciliary substrates (both underpin the WormBase IDA
  GO:0004674 annotations):
  - Phosphorylates the tubulin-binding N-terminal module of the IFT-B subunit
    **IFT-74** at 11 Ser/Thr sites [PMID:35969738 "identified 11 phosphorylation sites"],
    with a defined substrate motif [PMID:35969738 "the DYF-5/MAK kinase substrate motif, (R)PX[S/T]*"].
    This phosphorylation lowers IFT-74/81 tubulin affinity
    [PMID:35969738 "reducing the tubulin-binding affinity of IFT-74/81 approximately sixfold"].
  - Phosphorylates the **OSM-3** kinesin C-terminal fragment (444-699)
    [PMID:38806659 "Our in vitro protein kinase assays revealed that DYF-5 directly phosphorylates the C-terminal fragment of OSM-3 (444"].
- Human/mouse orthologue (RCK/MAK-ICK family) similarity underpins the ISS
  annotations; UniProt EC=2.7.11.1 (Ser/Thr kinase). ATP binding is a standard
  active-site feature (ATP-binding loop 17-25).
- NOTE on "MAP kinase": DYF-5 was historically named a "MAP kinase"
  [PMID:17420466 "we identify DYF-5, a conserved MAP kinase"] and is still described as
  MAPK-family [PMID:38806659 "DYF-5 belongs to a conserved family of mitogen-activated protein kinases (MAPKs) that localize at the distal region of the cilium to regulate ciliary elongation"].
  Molecularly it is a MAK/ICK/CILK1 (RCK) CMGC kinase with a TDY-like activation loop,
  NOT a canonical MAPK that is activated within a three-tier MAP3K→MAP2K→MAPK cascade.
  The specific term GO:0004674 (protein serine/threonine kinase activity, IDA) is the
  well-supported MF; GO:0004707 (MAP kinase activity, ISS) and GO:0000165 (MAPK cascade,
  IEA-from-EC/logical-inference) are legacy/name-driven over-annotations.

### 2. Regulation of anterograde IFT motor handover (CORE)
- Anterograde IFT in worm cilia uses two kinesin-2 motors: heterotrimeric kinesin-II
  (KLP-11/KLP-20/KAP-1) in the middle segment and homodimeric OSM-3 in the distal
  segment. DYF-5 coordinates the handover between them.
- In *dyf-5(lf)*: kinesin-II is not restricted to the middle segment
  [PMID:17420466 "dyf-5 is required "] and OSM-3 detaches from IFT particles and slows
  [PMID:17420466 "OSM-3 moves at a reduced speed and is not attached to IFT "].
- Model: DYF-5 promotes undocking of kinesin-II and docking of OSM-3
  [PMID:17420466 "in the docking of OSM-3 onto IFT particles"]. Consistent with a direct
  action, DYF-5 phosphorylates OSM-3 and regulates it cell-autonomously
  [PMID:38806659 "DYF-5 regulates OSM-3CA in a cell-autonomous manner"].

### 3. Cilium length / ciliogenesis control (CORE)
- *dyf-5* null cilia are elongated, misaligned and accumulate IFT proteins
  [PMID:17420466 "the cilia of dyf-5 loss-of-function (lf) animals are elongated and are not "],
  [PMID:17420466 "six IFT proteins accumulate in "] — DYF-5 normally restrains cilium
  elongation (negative regulator of length).
- Mechanistically, DYF-5→IFT-74 phosphorylation drives ciliary-tip tubulin unloading:
  blocking or mimicking IFT-74 phosphorylation elongates or shortens cilia respectively
  [PMID:35969738 "Ablation or constitutive activation of IFT-74 phosphorylation abnormally "],
  fitting the balance-point model of length control. DYF-5 protein is positioned at the
  middle-segment tip through the distal tip
  [PMID:35969738 "the endogenous DYF-5 protein distributes from the tip of the middle ciliary segment"].

### 4. Localization (well supported, non-core)
- Perikaryon, dendrite, axon and cilium (UniProt EXP/IDA, PMID:17420466); enriched at
  the transition zone / dendrite-cilium junction and distal cilium. Worm sensory cilia
  are non-motile (GO:0097730 non-motile cilium, IDA).

## What is NOT known (candidate knowledge gaps)
- **Full in-vivo substrate set.** Only two direct substrates (IFT-74, OSM-3) are
  biochemically established; the field explicitly states more remain
  [PMID:35969738 "understanding the undocking of kinesin-II and docking of OSM-3 onto IFT particles"].
  Which substrate(s) mediate the kinesin-II undocking step is unresolved.
- **Mechanism of the kinesin-II→OSM-3 handoff.** It is unknown whether DYF-5 triggers
  handover directly by phosphorylating a motor/adaptor or indirectly via IFT-train
  remodelling; the ~50 aa OSM-3 fragment phosphosites and their functional residues are
  not mapped in vivo.
- **Upstream activation.** How DYF-5 kinase activity and its ciliary-tip localization are
  themselves regulated (the RCK-family activator, e.g. CCRK/CDK-like input, and the
  activation-loop phospho-state in worm) is not established here.
- **Isoform specificity.** Whether the two splice isoforms (a/b, differing in the
  C-terminal tail that is required for ciliary targeting) have distinct roles is untested.

## Annotation-review reasoning (high level)
- ACCEPT the experimental MF (GO:0004674 IDA×2), the ciliary CC (non-motile cilium,
  cilium), and the IFT/cilium-length BPs (intraciliary [anterograde] transport, cilium
  assembly, non-motile cilium assembly and its regulation).
- MARK_AS_OVER_ANNOTATED / MODIFY the MAPK-legacy terms (MAP kinase activity → Ser/Thr
  kinase; MAPK cascade; intracellular signal transduction) and the phylogenetically
  over-propagated nucleus CC (no worm evidence; contradicts ciliary/cytoplasmic
  localization).
- KEEP_AS_NON_CORE the general/location terms (ATP binding, protein kinase activity,
  protein serine kinase activity, cytoplasm, axon, dendrite, perikaryon, neuronal cell
  body, intracellular protein localization).

## Provenance / methods note
- `just deep-research-falcon worm dyf-5 --fallback perplexity-lite` completed after ~21 min
  (falcon/Edison, 33 citations): `dyf-5-deep-research-falcon.md`. The perplexity-lite
  fallback 401'd on quota but was not needed. The falcon report is genuine model output and
  corroborates this review (conserved DYF-5/LF4/ICK-CILK1/MAK/LmxMPK9 module; upstream
  DYF-18/CCRK activation; ICK phosphorylation of kinesin-2 KIF3A Thr674). It reinforces the
  two knowledge gaps (substrate set; kinesin-II->OSM-3 handoff) and the upstream-activation
  suggested question. The review's graded conclusions remain grounded in the primary
  literature below plus UniProt (B3WFY8) and GOA; no deep-research file was fabricated.
- Reference-validation caveat: the repo reference validator only sees each paper's
  PubMed ABSTRACT (not the full text cached in `publications/`). All `supporting_text`
  quotes here were therefore drawn from abstract text (verbatim, whitespace/punctuation-
  normalized). Full-text-only facts (e.g. DYF-5 phosphorylates the OSM-3 C-terminus in
  vitro; endogenous DYF-5 distribution along the axoneme) are used in prose/reasoning and
  anchored via the curator IDA annotations, not quoted as supporting_text.

## References used
- PMID:17420466 Burghoorn et al. 2007 PNAS — primary genetic/imaging characterization
  (abstract-only in cache; experimental annotations by WormBase/UniProt curators from
  full text). HIGH.
- PMID:35969738 Jiang et al. 2022 PNAS — DYF-5 phosphorylates IFT-74, tubulin unloading,
  cilium-length control (full text). HIGH.
- PMID:38806659 Xie et al. 2024 EMBO J — DYF-5 phosphorylates OSM-3 C-terminus; dyf-5
  suppressors of hyperactive OSM-3 (full text). HIGH.
