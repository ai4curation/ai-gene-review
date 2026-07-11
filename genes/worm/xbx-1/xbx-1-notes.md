# xbx-1 (Caenorhabditis elegans) — research notes

Gene: **xbx-1** (X-Box promoter gene 1) / WormBase F02D8.3 / WBGene00006960
UniProt: **Q19119** (Cytoplasmic dynein 2 light intermediate chain 1)
Human ortholog: **DYNC2LI1 / D2LIC** (UniProt Q8TCX1); PANTHER family **PTHR13236** (subfamily SF0
"CYTOPLASMIC DYNEIN 2 LIGHT INTERMEDIATE CHAIN 1"), Pfam **PF05783 (DLIC)**.

## Identity / bioinformatic context

- UniProt RecName: "Cytoplasmic dynein 2 light intermediate chain 1"; SIMILARITY: "Belongs to the
  dynein light intermediate chain family." Sequence 370 aa; contains a P-loop (Walker A) motif
  `AGNRKSGKSS` near residue ~55 (Gene3D P-loop NTPase / SSF52540), characteristic of the DLIC family,
  although DLICs are catalytically inert G-domain-like folds (no established GTPase/ATPase activity of
  the LIC itself).
- Name origin: "xbx" = **X-box**; the gene was found as an X-box (RFX/DAF-19) promoter-motif gene,
  i.e. a member of the DAF-19-regulated ciliary gene battery.

## KNOWN (well supported)

**Molecular role — a light intermediate chain of the cytoplasmic dynein-2 (retrograde IFT) motor.**
- xbx-1 "shares homology with a mammalian dynein light intermediate chain (D2LIC)"
  [PMID:12802075 "a novel \nCaenorhabditis elegans gene, xbx-1, that is required for retrograde IFT and \nshares homology with a mammalian dynein light intermediate chain (D2LIC)"].
- XBX-1 functions together with the CHE-3 dynein heavy chain in retrograde IFT:
  [PMID:12802075 "the DLIC protein XBX-1 functions together with the CHE-3 dynein in retrograde IFT, \ndownstream of the complex A proteins"].
  CHE-3 is the C. elegans cytoplasmic dynein-2 heavy chain (DYNC2H1 ortholog); XBX-1 is its LIC
  partner. This is the basis of the ISS "dynein heavy chain binding" (GO:0045504) annotation
  (with/from UniProtKB:Q6AY43 = rat D2LIC).
- In the BBSome paper XBX-1 is referred to as "the retrograde IFT motor dynein light chain XBX-1
  (the ortholog of human D2LIC)" [PMID:22922713 "the retrograde IFT motor dynein light chain XBX-1 (the ortholog of human D2LIC)"].

**Biological process — retrograde intraflagellar transport (IFT) required for cilium assembly.**
- xbx-1 is "required for retrograde IFT and shares homology with a mammalian dynein light intermediate
  chain" [PMID:12802075].
- Loss of xbx-1 gives short, malformed cilia with a distal bulb where IFT proteins pile up (the
  classic retrograde-IFT/dynein-mutant phenotype): [PMID:12802075 "Analysis of cilia in xbx-1 mutants
  reveals that they are shortened and have a bulb like \nstructure in which IFT proteins accumulate"].
  This underlies the IMP annotations to intraciliary retrograde transport (GO:0035721) and non-motile
  cilium assembly (GO:1905515).
- Placement in the pathway: XBX-1/CHE-3 dynein acts downstream of the IFT-A (complex A) proteins;
  notably "retrograde XBX-1 movement was detected in complex A mutants" [PMID:12802075 "retrograde \nXBX-1 movement was detected in complex A mutants"], distinguishing dynein-2 motor behaviour from
  IFT-A cargo.

**Localization — ciliary base/basal body and the axoneme, moving bidirectionally.**
- "XBX-1 localizes to the base of the cilia and undergoes anterograde and \nretrograde movement along
  the axoneme" [PMID:12802075]. (Note: the anterograde run reflects the motor being carried as
  inactive cargo by kinesin-2 to the ciliary tip, then powering the retrograde run.)
- Restated in later work: "The dynein light intermediate chain protein XBX-1 localizes to the basal
  body and undergoes bidirectional movement along the ciliary axoneme (Schafer et al., 2003)"
  [PMID:33460640].
- Used as a canonical IFT/ciliary marker: "tdTomato-tagged XBX-1 (IFT protein that localises to the
  ciliary base and axoneme)" [PMID:27930654].
- Curated experimental (IDA) localizations across papers cover: ciliary base (GO:0097546), ciliary
  basal body (GO:0036064), axoneme (GO:0005930), ciliary transition zone (GO:0035869), cilium
  (GO:0005929), and non-motile cilium (GO:0097730). Several of these come from studies that used
  XBX-1::GFP/tdTomato as the reference IFT/ciliary marker while assaying other proteins
  (PMID:27930654 RAB-28; PMID:25335890 AFD bipartite compartment; PMID:17420466 DYF-5;
  PMID:27623382 GRDN-1/Girdin; PMID:33460640 GRDN-1; PMID:22922713 BBSome). The curators annotating
  these IDA calls read the full text.

**Transcriptional regulation.**
- xbx-1 is part of the DAF-19 (RFX) ciliary gene battery: "xbx-1 \nexpression in ciliated sensory
  neurons is regulated by the transcription factor \nDAF-19" [PMID:12802075]. (This is regulation OF
  xbx-1, not a molecular function of the protein — informative for the gene's identity as an X-box
  ciliary gene, but not a GO MF/BP annotation for the protein.)

## NOT known / uncertain (candidate knowledge gaps)

- The **specific role of the LIC subunit within dynein-2** is not resolved in C. elegans. In
  mammals/Chlamydomonas the DLIC (D2LIC/DYNC2LI1) is required for dynein-2 complex stability and for
  loading/coupling the motor for IFT, but the precise molecular contribution of XBX-1 — motor complex
  assembly/stability vs. cargo adaptor/IFT-train coupling vs. regulation of motor
  activation/autoinhibition at the tip — has not been dissected in the worm. The LIC itself has no
  demonstrated enzymatic activity; the ATP-dependent minus-end-directed motor activity is a property
  of the dynein-2 heavy chain (CHE-3)/complex.
- Whether XBX-1 has any **dynein-2-independent function** (e.g. at the basal body/centriole outside
  the assembled motor) is untested.
- The **G-domain/P-loop of the DLIC fold**: whether the residual nucleotide-binding fold in XBX-1
  binds a nucleotide or is a purely structural relic in vivo is unknown.
- **Ontology gap:** GO has no specific "cytoplasmic dynein 2 complex" cellular-component term; the
  closest available term is GO:0005868 "cytoplasmic dynein complex" (which conflates dynein-1 and
  dynein-2). OLS search for "cytoplasmic dynein 2 complex" returns only HGNC gene-group, not a GO
  class (checked 2026-07-04).

## Annotation review plan (summary of decisions)

Core (keep, represent the evolved function):
- GO:0045504 dynein heavy chain binding (MF) — its own molecular function (binds CHE-3 HC). ACCEPT.
- GO:0005868 cytoplasmic dynein complex (CC, part_of) — dynein-2 motor membership. ACCEPT (best
  available term; a dynein-2-specific term would be preferable — ontology gap).
- GO:0035721 intraciliary retrograde transport (BP) — ACCEPT (core; IMP + IBA).
- GO:0035735 intraciliary transport involved in cilium assembly (BP) — ACCEPT (core; broader IFT/
  assembly framing).
- GO:1905515 non-motile cilium assembly (BP, IMP) — ACCEPT (core; C. elegans sensory cilia are
  non-motile).
Locations (accept as experimentally supported; non-core CC context):
- GO:0097546 ciliary base, GO:0036064 ciliary basal body, GO:0005930 axoneme, GO:0035869 ciliary
  transition zone, GO:0005929 cilium, GO:0097730 non-motile cilium — ACCEPT (IDA/IBA).
IEA/electronic:
- GO:0005813 centrosome (IEA, SubCell) — KEEP_AS_NON_CORE / cautious: centrosome is the SubCell
  mapping of the basal body/MTOC; in C. elegans sensory neurons the relevant structure is the ciliary
  basal body, and there is no direct evidence for a canonical mitotic centrosome role. Mark non-core.
- Duplicate IEA (InterPro/SubCell) mirrors of IDA/IBA terms (dynein complex, axoneme, retrograde
  transport, IFT-in-assembly) — ACCEPT as consistent electronic support (redundant with experimental
  calls).

## Falcon deep-research summary (xbx-1-deep-research-falcon.md, 2026-07-04)

The falcon report (provider Edison Scientific Literature; 34 citations) is consistent with the
primary-literature review above and adds complex-composition/structural detail (citation keys are
falcon-internal, NOT PMIDs; not imported into the review YAML to avoid unverifiable citations):
- C. elegans IFT-dynein (dynein-2) composition: heavy chain CHE-3 (DYNC2H1), light intermediate chain
  XBX-1 (DYNC2LI1), plus Tctex-type light chains DYLT-1/DYLT-2 and a Roadblock-type light chain
  DYRB-1 (falcon: "hao2011theretrogradeift"). This supports XBX-1's assignment as the LIC of the
  retrograde IFT motor.
- Mammalian dynein-2 cryo-EM: DYNC2LI1 binds directly to the N-terminal non-motor tail of DYNC2H1;
  the holocomplex is 11 subunits in three subcomplexes with ~2:2:1:1 DYNC2H1:DYNC2LI1:WDR60:WDR34
  stoichiometry (falcon: "qiu2022combinationsofdeletion", "hiyamizu2023multipleinteractionsof",
  "tsurumi2019interactionsofthe"). This frames XBX-1 as a structural bridge between the heavy-chain
  motor and the intermediate/light-chain tail module — consistent with, but not fully resolving, the
  C. elegans-specific mechanistic knowledge gap (assembly/stability vs. IFT-train coupling vs. motor
  regulation).
- Reaffirms XBX-1 is non-enzymatic (structural/regulatory), that loss gives short cilia with IFT
  accumulation, and that xbx-1 is DAF-19/X-box regulated.
These points reinforce the review; none contradict it, and none required changing an action.

## References consulted
- PMID:12802075 Schafer et al. 2003 MBoC — primary XBX-1 characterization (abstract-only in cache;
  rich abstract). HIGH relevance.
- PMID:22922713 Wei et al. 2012 (BBSome controls IFT assembly/turnaround) — XBX-1 as dynein-2 marker.
- PMID:27930654 Jensen et al. 2016 (RAB-28) — XBX-1::tdTomato as base/axoneme IFT marker.
- PMID:25335890 Nguyen et al. 2014 (AFD bipartite compartment) — XBX-1 as ciliary/axoneme marker.
- PMID:17420466 Burghoorn et al. 2007 (DYF-5) — XBX-1 as non-motile cilium marker (abstract has no
  xbx-1 mention; IDA from full text).
- PMID:27623382 Nechipurenko et al. 2016 (Girdin/GRDN-1 BB positioning) — cilium marker (abstract has
  no xbx-1 mention; IDA from full text).
- PMID:33460640 Nechipurenko et al. 2021 (GRDN-1 dendrite/cilium position) — restates XBX-1 basal
  body + axoneme localization.
