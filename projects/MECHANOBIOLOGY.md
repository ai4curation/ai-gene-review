# Mechanobiology Gene Review Project

## Scope

This project reviews genes whose core function is to sense mechanical cues, transmit force-dependent signals, or reshape the mechanical microenvironment in ways that drive reproducible biological outcomes.

This scaffold was informed by [cmungall/stuff#671](https://github.com/cmungall/stuff/issues/671), but the project stays deliberately narrower and more practical than the grant-style framing in that issue:
- focus on reviewable genes, evidence-backed mechanisms, and curation outputs
- use disease relevance to prioritize batches, not to over-claim translational impact
- treat ontology or knowledge-graph follow-up as optional downstream outputs, not the primary deliverable

Operationally, each reviewed gene should be placed in a concrete chain:

`mechanical stimulus -> sensor/transducer -> downstream axis -> phenotype/context`

## Practical inclusion criteria

Include genes when there is evidence for one or more of the following:
- direct sensing of membrane tension, stretch, shear, compression, or osmotic/mechano-osmotic change
- force transmission through adhesions, cortex, cytoskeleton, primary cilium, or nucleus
- robust mechanosensitive downstream signaling repeatedly tied to defined mechanical contexts
- active remodeling of ECM stiffness/compliance or tissue mechanics that is central to the gene's biological role

Deprioritize genes when they are only:
- generic proliferation, migration, or stress-response genes without a defined mechanical trigger
- broad ECM structural components with no mechanotransduction-specific evidence
- one-off assay hits from poorly defined stretching/stiffness systems

## Mechanical stimulus space to capture explicitly

- **Matrix stiffness / compliance**: soft vs stiff substrate responses, durotaxis, fibrotic stiffening
- **Fluid shear stress**: endothelial flow sensing, tubular flow, ciliary flow detection
- **Tensile stretch / cyclic stretch**: muscle, lung, vessel wall, epithelium
- **Compression / confinement**: cartilage, tumor growth, nuclear squeezing during migration
- **Membrane tension**: channel gating, blebbing, osmotic swelling, cell shape change
- **Cell crowding / packing forces**: contact-dependent YAP/TAZ control, epithelial jamming
- **Topography / curvature**: force-sensitive adhesion and cytoskeletal organization

## Candidate mechanosensor and transduction modules

### 1. Direct or near-direct mechanical sensors

- **PIEZO1, PIEZO2**: canonical mechanically activated ion channels
- **TRPV4**: osmotic and mechanical channel with recurring roles in cartilage, vasculature, and fibrosis-related signaling
- **PKD1, PKD2**: flow/ciliary mechanosensation candidates with strong kidney/cilia relevance

### 2. Adhesion and focal-adhesion force coupling

- **ITGB1, ITGA5**: integrin-mediated ECM force coupling
- **TLN1, VCL, PXN, ILK, PTK2/FAK1**: adhesion proteins that convert load-bearing contacts into signaling outputs

### 3. Cytoskeletal force transmission

- **RHOA, ROCK1, ROCK2**: contractility and cortical tension axis
- **ACTN1, ACTN4, FLNA, MYH9, MYH10**: actomyosin-linked mechanical response machinery

### 4. Nuclear mechanotransmission

- **LMNA**: nuclear lamina stiffness and force buffering
- **SYNE1, SYNE2, SUN1, SUN2, EMD**: LINC/nuclear-envelope components transmitting cytoskeletal force to the nucleus

### 5. Downstream mechanosensitive effectors

- **YAP1, WWTR1 (TAZ), LATS1, LATS2**: Hippo-linked mechanical state readout
- **MAPK1, MAPK3, MTOR, MRTFA, SRF**: common downstream axes that often need careful specificity in curation
- **SMAD2, SMAD3, TGFB1, CTGF/CCN2**: stiffness/fibrosis-linked outputs that should usually be treated as downstream context, not primary sensors

### 6. Mechanical microenvironment modifiers

- **FN1, LOX, COL1A1, SPARC, DCN**: ECM regulators that can change tissue stiffness and feed back onto mechanosensing
- These belong in scope only when the mechanical consequence is central, not merely because they are ECM genes

## Suggested first review batches

### Batch A: canonical direct mechanosensors

- PIEZO1
- PIEZO2
- TRPV4
- PKD1
- PKD2

### Batch B: integrin-adhesome force transduction

- ITGB1
- ITGA5
- TLN1
- VCL
- PTK2
- PXN

### Batch C: nucleus-cytoskeleton coupling

- LMNA
- SYNE1
- SYNE2
- SUN1
- SUN2
- EMD

### Batch D: downstream mechanical state effectors

- YAP1
- WWTR1
- LATS1
- LATS2
- RHOA
- ROCK1
- ROCK2

### Batch E: matrix stiffening and fibrosis anchor genes

- FN1
- LOX
- SPARC
- DCN
- TGFB1
- CTGF

## Downstream axes to record in reviews

When a gene is in scope, reviewers should try to capture which of these axes is actually supported:
- **Ca2+ influx and ion-channel signaling**
- **RhoA/ROCK-actomyosin contractility**
- **Hippo/YAP/TAZ nuclear localization or transcriptional output**
- **FAK/Src/MAPK signaling**
- **mTOR / growth-state coupling**
- **TGF-beta / SMAD fibrotic remodeling**
- **Endothelial flow programs** such as KLF2/KLF4/NOS3
- **Migration / invasion / EMT-like programs** when clearly tied to force context

## Disease and tissue anchors for prioritization

These are useful anchors for choosing batches, but should not become hype-driven claims:
- **Fibrosis**: lung, liver, heart, kidney; matrix stiffening and feed-forward myofibroblast activation
- **Cancer invasion and metastasis**: confinement, adhesion turnover, ECM remodeling, YAP/TAZ programs
- **Cardiovascular and endothelial biology**: shear stress, stretch, cardiac remodeling
- **Kidney and cilia-linked mechanosensation**: flow detection and tubular phenotypes
- **Cartilage, bone, tendon, and muscle**: load-bearing mechanobiology

## Expected outputs

- a reviewed starter set of high-confidence mechanobiology genes in `genes/<organism>/<gene>/`
- a project-level summary table linking stimulus, sensor/transducer class, downstream axis, and phenotype
- a shortlist of over-annotation patterns or recurrent GO term pain points in mechanobiology curation
- possible pathway-style summary pages once the first review batches stabilize
- optional bioinformatics sidecars only where they answer a concrete curation question

## Questions to keep asking during curation

- Is this gene a **direct mechanosensor**, a **force-transducing component**, a **downstream effector**, or a **mechanical-context modifier**?
- What is the actual stimulus: stiffness, shear, stretch, compression, membrane tension, osmotic change, or something more indirect?
- Is the evidence from a defined mechanical perturbation, or just from a generic migration/adhesion assay?
- Is the reported function likely cell-type or tissue specific?
- Are existing annotations too broad, especially around `cell adhesion`, `ECM organization`, `actin binding`, `response to mechanical stimulus`, or generic signaling terms?
- Does the paper support a core function, a conditional context-specific role, or only a disease-associated correlation?

## Guardrails

- Do not treat every ECM or cytoskeletal gene as mechanobiology by default.
- Do not elevate downstream fibrosis or cancer markers into "mechanosensors" unless the upstream mechanical link is demonstrated.
- Prefer a smaller, well-argued starter set over a sprawling catch-all list.
- Only propose ontology or schema extensions after repeated curation pain points appear across reviewed genes.

## How issue #671 influenced this framing

The issue materially improved the scaffold in four ways:

1. It expanded the project from a narrow ECM/stiffness idea into a fuller mechanical landscape including shear, tension, compression, membrane tension, and osmotic pressure.
2. It surfaced a practical shortlist of mechanobiology anchor classes: Piezo channels, integrin/adhesion machinery, nuclear lamins, and YAP/TAZ-linked signaling.
3. It pushed the framing toward explicit `stimulus -> sensor -> downstream phenotype` chains rather than a flat list of "mechanics-related genes."
4. It suggested useful disease anchors and outputs, especially fibrosis, cancer invasion, and cardiovascular remodeling.

What was intentionally **not** adopted from the issue as a primary goal:
- a new mechanobiology ontology
- a large AI extraction platform
- broad therapeutic-discovery claims

Those may become relevant later, but the present project is first a grounded curation and synthesis effort for `ai-gene-review`.

## Source input

- Key ideation source: [cmungall/stuff issue #671](https://github.com/cmungall/stuff/issues/671), fetched 2026-04-11
