# che-11 (C. elegans) — research notes

Gene: **che-11** / ORF **C27A7.4** / WormBase **WBGene00000490** / UniProt **P90757** (1437 aa).
Ortholog: **IFT140** (human IFT140; UniProt Q96RY7). PANTHER PTHR15722:SF7 "INTRAFLAGELLAR
TRANSPORT PROTEIN 140 HOMOLOG". Domain architecture (UniProt P90757): two N-terminal
WD40 β-propellers ("IFT140 first/second beta-propeller", Pfam PF23383/PF23385) followed by a
long TPR/α-solenoid ("IF140/IFT172/WDR19 TPR", PF24762; "IF140 C-terminal TPR", PF24760).
No catalytic domain. ComplexPortal CPX-1289 = Intraflagellar transport complex A. Reactome
R-CEL-5620924 (Intraflagellar transport), R-CEL-5610787 (Hedgehog 'off' state).

Note on nomenclature: che-11 = **IFT140** (retrograde IFT-A core subunit). This is distinct
from the paralogous IFT-A subunit **dyf-2 = WDR19/IFT144** (already reviewed in this repo).
Both are IFT-A core subunits; do not conflate them.

## KNOWN (well supported)

### 1. CHE-11 is a core subunit of the IFT-A ("Complex A") particle
- [PMID:11301258 "DAF-10 and CHE-11 (two Complex A polypeptides)"] — Qin, Rosenbaum & Barr
  (2001) directly identified CHE-11 as one of the two Complex A (IFT-A) polypeptides assayed
  (with DAF-10), alongside OSM-5 (Complex B) and CHE-2.
- ComplexPortal CPX-1289 (IFT complex A) records CHE-11 as a subunit (NAS, GOA reference
  PMID:28479320).
- [PMID:27930654 "disrupted CHE-11 (IFT140), which is a component of IFT-A essential for IFT"]
  — Jensen et al. (2016) describe CHE-11 as the IFT140 component of IFT-A that is essential
  for IFT.

### 2. CHE-11 undergoes/drives intraflagellar transport in sensory cilia
- [PMID:11301258 "move at the same rate"] — OSM-5, DAF-10, CHE-11 and CHE-2 all move at the
  same rate along C. elegans sensory cilia (i.e. as part of the moving IFT machinery).
- The IFT-A complex is the retrograde (tip-to-base) module of IFT (driven by cytoplasmic
  dynein-2); the anterograde module is IFT-B + kinesin-2. As an IFT-A subunit CHE-11 is
  required for retrograde transport and, because retrograde return of IFT components is needed
  to sustain the whole cycle, for IFT/cilium assembly overall.

### 3. CHE-11 is required for ciliary IFT and cilium assembly (loss-of-function phenotype)
- [PMID:27930654 "Although GFP::RAB-28 is observed within the truncated cilia of che-11
  mutants, we could not detect processive movement of the GFP signals"] — che-11(e1810)
  mutants have **truncated cilia** and abolished processive ciliary transport of the IFT cargo
  RAB-28; this establishes CHE-11 as required for (a positive regulator of) IFT of ciliary
  cargo and for building a normal-length cilium.
- Localizes to the (non-motile) sensory cilium: CHE-11 moves within cilia (PMID:11301258) and
  CHE-11::GFP is imaged in cilia in IFT studies. GOA carries IDA "non-motile cilium"
  (PMID:11301258, PMID:17420466).

### 4. che-11 mutants are Dyf (dye-filling defective) with structurally defective chemosensory cilia
- [PMID:1732156 "Dauer-defective mutations in nine genes cause structurally defective
  chemosensory cilia, thereby blocking chemosensation"] — Vowels & Thomas (1992): che-11 is
  one of the cilium-structure genes whose mutations block chemosensation and perturb
  chemosensory (dauer) decision-making.
- [PMID:14982934 "mev-4 had a nonsense mutation on the che-11 gene"] — the paraquat-resistance
  mutant mev-4 is a che-11 nonsense allele with a **Dyf phenotype** (dye-filling defective).

### 5. Downstream / pleiotropic sensory consequences of losing ciliary function
These are phenotypes of the *cilium-defective animal*, not molecular activities of CHE-11.
- Extended adult lifespan: [PMID:14982934 "One mutant named mev-4 was long-lived and showed
  cross-resistance to heat and Dyf phenotype"]. (Also GOA IMP determination of adult lifespan
  from PMID:19208769.)
- Resistance to oxidative stress (paraquat): [PMID:14982934 "We isolated mutants resistant to
  paraquat from nematode Caenorhabditis elegans"]; paraquat is an oxidative-stress generator.
- Cross-resistance to heat (response to heat): PMID:14982934 (same quote as lifespan).
- Hyperosmotic response: GOA IMP (PMID:14982934) — WB curator annotation; not stated in the
  abstract but consistent with Dyf/osmotic-avoidance phenotypes of ciliary mutants.
- Dauer entry: GOA IGI (PMID:1732156) — genetic interactions with daf genes; cilium-structure
  gene acting in chemosensory control of the dauer decision.
These are best captured as KEEP_AS_NON_CORE (pleiotropic, downstream of the ciliary sensory
defect) rather than core molecular/cellular functions.

### 6. Conserved disease relevance
Human IFT140 mutations cause skeletal ciliopathies and retinal dystrophy (short-rib thoracic
dysplasia / Mainzer–Saldino syndrome / non-syndromic retinitis pigmentosa). Not separately
cached here; used only as conserved-function context, not for any worm annotation.

## NOT known / gaps
- **No molecular_function annotation and no adequate MF term.** CHE-11 is a structural IFT-A
  scaffold with no catalytic activity; GO has no "structural constituent of intraflagellar
  transport particle" term, so its MF is effectively dark (same ontology gap as its paralog
  dyf-2). The worm GOA record for che-11 carries only CC and BP terms.
- **Subunit-resolved IFT-A architecture in the worm is not solved.** The precise CHE-11
  contacts within IFT-A (with DAF-10/IFT122, DYF-2/WDR19, IFT-139, IFT-43, IFTA-1) and how
  IFT-A engages dynein-2 for retrograde turnaround are inferred from orthology/proteomics, not
  from a worm structure.
- **Anterograde vs retrograde requirement.** GOA carries both "positive regulation of
  intraciliary anterograde transport" and "...retrograde transport" (IMP, PMID:27930654) for
  che-11; mechanistically CHE-11/IFT-A is primarily the retrograde module, and the anterograde
  effect is largely an indirect consequence of failed IFT-component recycling. The direct vs
  indirect boundary for anterograde regulation is not resolved.

## Annotation review plan (summary)
- IFT-A membership (GO:0030991), retrograde IFT (GO:0035721), IFT (GO:0042073), cilium
  assembly (GO:0060271), ciliary localization (non-motile cilium GO:0097730, cilium
  GO:0005929, axoneme GO:0005930, ciliary basal body GO:0036064): ACCEPT (core / core CC).
- positive regulation of intraciliary retrograde/anterograde transport (PMID:27930654): KEEP —
  retrograde is on-target (near-core); anterograde is an indirect requirement, non-core.
- Stress/lifespan/dauer/hyperosmotic (PMID:14982934, PMID:1732156, PMID:19208769):
  KEEP_AS_NON_CORE — pleiotropic downstream sensory phenotypes.
- Core function: structural constituent of IFT-A (MF: structural molecule activity), in_complex
  IFT particle A, driving intraciliary retrograde transport and cilium assembly.

## Update after falcon deep research (Edison Scientific, 2026-07-04)

Genuine falcon report landed at 17:16 after the wrapper's 600s timeout (kept and
committed as che-11-deep-research-falcon.md; 30 citations to real papers). It
corroborates the PMID-grounded review above and adds context (citations here are to
the falcon report's sources, not cached in publications/, so used as context only):

- **IFT-A architecture is cryo-EM-solved (general/cross-species).** CHE-11/IFT140 sits in
  the IFT-A core (A1) with DYF-2/IFT144 and DAF-10/IFT122; IFT140 and IFT144 form an
  antiparallel TPR–TPR heterodimer (V-shaped, β-propellers splayed ~50 Å), IFT122 bridges
  A1 to the peripheral A2 module (IFT139/IFT121/IFT43) [Meleppattu et al. 2022 Cell,
  10.1016/j.cell.2022.11.033]. This is why the review's gap #2 boundary now notes the
  general architecture is solved while the worm-specific/dynein-2 turnaround remains open.
- **Domain division of labour:** N-terminal WD40 β-propellers → retrograde velocity +
  import of membrane-associated cargo (GPCRs, lipid-anchored signaling proteins); C-terminal
  TPR → IFT-A assembly [Picariello et al. 2019 J Cell Sci, 10.1242/jcs.220749].
- **CHE-11 is required to recruit other IFT-A subunits:** in che-11 mutants IFTA-1 fails to
  localize to cilia [Blacque et al. 2006 Mol Biol Cell, 10.1091/mbc.e06-06-0571].
- **Transition-zone gating (worm-specific):** IFT-140 controls ciliary entry/accumulation of
  MKS-module proteins and targets IFT-121/IFT-139 to trains [Scheidel & Blacque 2018 Curr
  Biol, 10.1016/j.cub.2018.08.017] — a worm IFT-140 function not captured in current GOA.
- **Transcriptional regulation:** che-11 is a DAF-19/RFX X-box target, co-regulated by FKH-8
  [Brocal-Ruiz et al. 2023 eLife, 10.7554/eLife.89702]. Consistent with expression in ~30+
  ciliated sensory neurons.
- **Nomenclature confirmed:** CHE-11 = IFT140 (distinct from DYF-2 = WDR19/IFT144). No
  contradiction with any ACCEPT/KEEP decision in the review.
