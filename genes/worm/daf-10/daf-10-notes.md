# daf-10 (C. elegans) research notes

UniProt: G5EFW7 (IF122_CAEEL). WormBase: WBGene00000906 / F23B2.4. Chromosome IV.
Human ortholog: IFT122 (Q9HBG6). 1192 aa; WD40 β-propeller + TPR solenoid + C-terminal
Zn-ribbon. No catalytic domain.

## Summary of identity and role (KNOWN)

daf-10 encodes the *C. elegans* ortholog of **IFT122** (Chlamydomonas IFT122), a core
subunit of the **intraflagellar transport complex A (IFT-A)**. IFT-A is the retrograde
(ciliary tip -> base) IFT subcomplex, moved by cytoplasmic dynein-2. daf-10 is required
for building/maintaining the non-motile sensory cilia of the worm's ciliated sensory
neurons, and — as a downstream sensory consequence — for chemosensation, dauer larva
formation, and modulation of insulin/IGF and TGF-β signaling.

The gene was named for its mutant phenotype: **abnormal DAuer Formation** (daf). daf-10
mutants are *dauer-defective* (Daf-d): they fail to form dauers because their chemosensory
cilia are structurally defective and cannot detect the dauer pheromone / environmental cues.

### IFT-A membership (KNOWN)
- UniProt SUBUNIT: "Component of the IFT complex A (IFT-A) composed of at least che-11,
  daf-10, dyf-2, ift-139, ift-43 and ifta-1" [ECO:0000269|PubMed:28479320]. The worm IFT-A
  composition was defined by affinity purification / mass spectrometry
  [PMID:28479320 "our affinity purification and genetic analyses show that IFT-A" ...
  "IFT-139 and IFT-43 function redundantly to promote dynein-2 motility"].
- ComplexPortal CPX-1289 = Intraflagellar transport complex A (worm).
- Founding molecular-identity paper: daf-10 and osm-1 gene products contain WD and WAA
  repeats, and daf-10 (with che-11) encodes an **IFT complex A** component
  [PMID:16648645 "The daf-10 and osm-1 gene products resemble each other and contain WD and WAA repeats"]
  [PMID:16648645 "mutation in daf-10 or che-11 , which encode complex A components"].
  Loss of daf-10/che-11 (complex A) gives *thicker-than-wild-type* patches of OSM-6::GFP in
  the dendritic endings (IFT-B accumulation), the classic IFT-A retrograde-defect signature,
  distinct from the *foreshortened/reduced* OSM-6::GFP of IFT-B (osm-1/osm-5/che-2/che-13)
  mutants.

### Subcellular localization (KNOWN)
- Cell projection, cilium [ECO:0000305|PubMed:11301258]. DAF-10 shuttles along the amphid
  and phasmid sensory cilia at the same rate as IFT-B proteins (osm-1, osm-5, osm-6)
  (Qin, Rosenbaum & Barr 2001, PubMed:11301258 — the paper that first showed a worm IFT-A/PKD
  homolog undergoing IFT).
- Ciliary basal body: GO:0036064 IDA from PMID:27623382 (Girdin/basal-body-positioning study;
  consistent with IFT proteins concentrating at the ciliary base/transition-fibre region
  before axonemal entry). Abstract-only cache; daf-10 not named in the abstract.

### Cilium assembly / IFT function (KNOWN)
- daf-10 is one of the classic dauer-defective genes whose mutations cause *structurally
  defective chemosensory cilia* [PMID:1732156 "structurally defective chemosensory cilia"].
- daf-10/IFT122 mutations disrupt ciliogenesis [PMID:21124868 "daf-10/IFT122 mutations (which disrupt ciliogenesis)"].
- IFT-A/retrograde IFT is required for cilium assembly & maintenance and for ciliary import
  of membrane cargo, including GPCRs (UniProt FUNCTION: "entry into cilia of G protein-coupled
  receptors (GPCRs)"). GPCR ciliary-localization requirement scored by IMP in PMID:24646679
  (abstract-only; daf-10 not named in abstract, but IFT-A is a known requirement for ciliary
  GPCR import).

### Dauer / sensory / signaling roles (KNOWN but non-core / downstream)
- Positive regulation of dauer larval development (daf-10 loss -> dauer-defective) — IMP,
  PMID:6583682 (Golden & Riddle 1984 pheromone switch; "Dauer-defective mutants fail to
  respond to added pheromone").
- Regulation of dauer larval development via genetic interaction with daf-25/Ankmy2
  (daf-25 dauer-constitutive phenotype is suppressed by daf-10 ciliogenesis loss) — IGI,
  PMID:21124868.
- Regulation of insulin receptor signaling pathway — IGI, PMID:11381260 (Lin et al. 2001).
  Sensory-neuron cilia modulate DAF-16/insulin nuclear localization systemically
  ("sensory neurons and germline activity regulate DAF-16 accumulation in nuclei"). This is
  an indirect, whole-organism, sensory-input effect, not a molecular function of an IFT-A
  structural subunit.
- Chemotaxis / chemosensation defects (UniProt KW Chemotaxis; disruption phenotype: defective
  chemotaxis, 86% reduced tracking to NH4Cl; sterile) — downstream of the ciliary defect.

## What is NOT known / gaps
- **No molecular-function annotation.** GOA carries only CC and BP terms; daf-10 reads as
  MF-dark. There is no GO MF term for "structural constituent of the IFT particle" (cf.
  structural constituent of ribosome). Its role is a WD40/TPR/Zn-ribbon scaffold within IFT-A.
- **Subunit-resolved architecture of the worm IFT-A** and daf-10's direct neighbor contacts
  are not solved structurally (composition known from mass-spec; no cryo-EM of the worm complex).
- **Which cilium-assembly / cargo-import functions are daf-10-specific vs generic IFT-A** is
  not separately dissected in the worm (most readouts are complex-level).

## Deep research status
Falcon deep research (`just deep-research-falcon worm daf-10 --fallback perplexity-lite`)
was run twice in the foreground; both the falcon primary attempt and the perplexity-lite
fallback timed out at the 600s wrapper limit on each run (~40 min total), producing no
deep-research file. No `-deep-research-*.md` file was fabricated. This review is grounded
directly in UniProt (G5EFW7), the QuickGO GOA record, and the cached primary literature
(PMIDs below), with every supporting_text a verified verbatim substring of the cited
PubMed abstract.

## Provenance / cache status
- Full text available: PMID:16648645 (founding daf-10 IFT paper), PMID:21124868 (DAF-25).
- Abstract-only cache: PMID:28479320, 27623382, 24646679, 1732156, 6583682, 11381260.
  For experimental annotations from abstract-only papers I defer to the WormBase/UniProt
  curator (full text read by them) per repo guidance; I do not REMOVE on absence-from-abstract
  grounds.

## Annotation review plan (see -ai-review.yaml)
Core: IFT-A membership (GO:0030991), retrograde IFT (GO:0035721) / intraciliary transport,
non-motile cilium localization (GO:0097730 / GO:0005929), cilium assembly (GO:0060271 /
GO:1905515), protein localization to cilium (GO:0061512).
Non-core downstream: dauer regulation (GO:0061065/0061066), receptor localization to cilium
(GO:0097500), regulation of insulin receptor signaling (GO:0046626), basal body (GO:0036064
kept as location).
