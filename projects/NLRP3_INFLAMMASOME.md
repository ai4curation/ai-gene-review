---
title: "NLRP3 Inflammasome Assembly Project"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN, FLAGSHIP]
species: [human]
manifest:
  slides:
    - href: NLRP3_INFLAMMASOME/slides/NLRP3_INFLAMMASOME-slides.html
      description: AI generated
  artifacts:
    - href: https://claude.ai/artifact/NjmYtfwPS1nDE8WcAWGBDN
      title: Project brief
---

# NLRP3 Inflammasome Assembly Project

**Bottom line:** the NLRP3 inflammasome is a danger-sensing complex in which
the sensor NLRP3 recruits the adaptor PYCARD (ASC) to activate caspase-1, which
matures IL-1β and IL-18 and cleaves gasdermin D to open pyroptotic pores.
Scoped, with the pathway now modelled: this page lists ten candidate human genes
and the pathway architecture, and the assembly chain has been built as
[canonical NLRP3 inflammasome](../modules/canonical_nlrp3_inflammasome.html),
a four-part module (licensed sensor → ASC filament → caspase-1 → GSDMD pore)
aligned with GO-CAM
[gomodel:635b1e3e00001811](https://bioregistry.io/go.model:635b1e3e00001811).
No gene-level review work has been done under this project. Three candidates
already have complete reviews from other work (NLRP3,
CASP4 and GSDMD, 364 annotations between them; most removals are generic
`protein binding` rows, 24 of 25 on NLRP3), and the NLRP3 review proposes a
new GO term, *inflammasome sensor activity*, because GO:0140299 molecular
sensor activity requires binding the sensed molecule. The adaptor PYCARD, the effector
CASP1, CASP5, IL1B, IL18, NEK7 and BRCC3 have no gene folder. The draft
[metazoan NLR signaling module](../modules/nlr_signaling.html) keeps NLRP3,
PYCARD and CASP1 as a compact pathway-level view alongside the NOD2–RIPK2
branch; the mechanistic detail now lives in the dedicated inflammasome module.

We scoped this because NLRP3 is a major therapeutic target and drives
autoinflammatory disease (CAPS) and inflammation in gout, atherosclerosis and
Alzheimer disease, and recent work on activation sites, post-translational
control and structure is likely to be under-represented in GO.

## Overview

The NLRP3 inflammasome is a multiprotein complex that activates inflammatory caspases in response to diverse danger signals, leading to IL-1β/IL-18 release and pyroptotic cell death. Recent discoveries have clarified activation mechanisms and identified new regulators.

## Model Species

**Primary: Homo sapiens (human)**
- Major therapeutic target
- Autoinflammatory disease relevance

## Core Pathway Architecture

### 1. Sensor
- **NLRP3** - NOD-like receptor, sensor component

### 2. Adaptor
- **PYCARD** (ASC) - Adaptor with PYD and CARD domains

### 3. Effector Caspases
- **CASP1** - Caspase-1, cleaves pro-IL-1β
- **CASP4/5** - Non-canonical inflammasome

### 4. Substrates/Outputs
- **IL1B** - Pro-inflammatory cytokine
- **IL18** - Pro-inflammatory cytokine
- **GSDMD** - Gasdermin D, pore-forming executioner

### 5. Critical Regulators
- **NEK7** - Essential NLRP3 activator (discovered 2016)
- **BRCC3** - Deubiquitinase
- **Various negative regulators**

### 6. Priming/Licensing
- **NFKB pathway** - Transcriptional priming

## Candidate Genes (~12-15)

| Gene | UniProt | Function |
|------|---------|----------|
| NLRP3 | Q96P20 | Sensor |
| PYCARD | Q9ULZ3 | ASC adaptor |
| CASP1 | P29466 | Effector caspase |
| CASP4 | P49662 | Non-canonical |
| CASP5 | P51878 | Non-canonical |
| GSDMD | P57764 | Pore formation |
| IL1B | P01584 | Cytokine |
| IL18 | Q14116 | Cytokine |
| NEK7 | Q8TDX7 | Essential activator |
| BRCC3 | P46736 | Deubiquitinase |

## Mechanism as currently modelled

Reconciled against [PMID:41062723](https://pubmed.ncbi.nlm.nih.gov/41062723/)
(Dubey et al., *Cell Mol Immunol* 2025, "Molecular mechanisms and regulation of
inflammasome activation and signaling") and the primary structural literature it
cites. Details and evidence quotes are in
[the module](../modules/canonical_nlrp3_inflammasome.html).

- **Priming vs activation.** Canonical activation is two-step. Priming is
  TLR/NF-κB transcriptional licensing of NLRP3 and pro-IL-1β plus poising
  modifications (PKD phosphorylation, ZDHHC5 palmitoylation, TRIM28 SUMOylation);
  activation is the second signal. The module covers activation onward and treats
  priming as upstream context, so priming belongs with the TLR modules.
- **Inactive cage → active disc.** Inactive NLRP3 is not a monomer: human NLRP3
  is an ADP-bound decamer ([PMID:35114687](https://pubmed.ncbi.nlm.nih.gov/35114687/))
  and endogenous mouse NLRP3 a membrane-bound 12–16-mer double-ring cage with the
  pyrin domains shielded inside
  ([PMID:34861190](https://pubmed.ncbi.nlm.nih.gov/34861190/)). The active form is
  a disc whose PYDs form a filament
  ([PMID:36442502](https://pubmed.ncbi.nlm.nih.gov/36442502/)).
- **NEK7's actual role.** NEK7 is kinase-independent here: it binds the NLRP3 LRR
  ([PMID:26642356](https://pubmed.ncbi.nlm.nih.gov/26642356/)), its catalytic
  activity is dispensable
  ([PMID:26814970](https://pubmed.ncbi.nlm.nih.gov/26814970/)), it bridges
  adjacent NLRP3 subunits
  ([PMID:31189953](https://pubmed.ncbi.nlm.nih.gov/31189953/)), and it is proposed
  to break the inactive cage. It is therefore modelled as a licensing annoton
  inside the sensor part, not as a step in the sequence.
- **TGN and MTOC.** NLRP3 binds PtdIns4P on the dispersed trans-Golgi network
  ([PMID:30487600](https://pubmed.ncbi.nlm.nih.gov/30487600/)); assembly and
  caspase activation occur at the microtubule organizing center, with HDAC6 as the
  dynein adapter ([PMID:32943500](https://pubmed.ncbi.nlm.nih.gov/32943500/)).
- **ASC speck.** One polymerization mechanism serves both families: the sensor
  nucleates ASC PYD filaments, clustered ASC CARDs nucleate caspase-1 CARD
  filaments, and the protease is activated by induced proximity
  ([PMID:24630722](https://pubmed.ncbi.nlm.nih.gov/24630722/)).
- **GSDMD pores.** Caspase-1 and caspase-4/5/11 cleave the interdomain linker
  ([PMID:26375003](https://pubmed.ncbi.nlm.nih.gov/26375003/)); GSDMD-NT binds
  inner-leaflet lipids and oligomerizes into pores
  ([PMID:27383986](https://pubmed.ncbi.nlm.nih.gov/27383986/)) whose negatively
  charged conduit electrostatically favours mature cytokines over their acidic
  precursors ([PMID:33883744](https://pubmed.ncbi.nlm.nih.gov/33883744/)).
  Terminal membrane rupture additionally requires NINJ1, which has its own review.
- **Non-canonical caspase-4/5/11.** These bind cytosolic LPS directly through
  their CARD and cleave GSDMD themselves; the resulting K⁺ efflux is what
  activates NLRP3. So the non-canonical route is a *separate sensing module* that
  joins this one at a single feedback edge, not an alternative sensor inside it.
  CASP4's review already models it with GO:0160074/GO:0160075.

## Other inflammasomes in the review (not modelled here)

PMID:41062723 also covers NLRP1, NLRP6, NLRP7, NLRP9, NLRP10, NLRP12,
NAIP–NLRC4, AIM2, Pyrin, IFI16, CARD8 and MxA. Two patterns matter for future
modelling:

- **Shared effector core.** Several differ from NLRP3 only in the sensor and reuse
  the ASC → caspase-1 → GSDMD chain verbatim. These are best added later as sensor
  variants over a shared effector core rather than as duplicate modules. AIM2 is
  the cleanest case (HIN200 binds dsDNA sequence-independently, PYD nucleates ASC;
  GO even has GO:0097169 for the complex).
- **Mechanisms that do not fit this module's shape.** NLRP1 and CARD8 are
  activated by *functional degradation* — FIIND autoproteolysis leaves two
  non-covalently associated fragments, and proteasomal destruction of the
  N-terminal fragment liberates a UPA–CARD that oligomerizes; DPP8/DPP9 restrain
  this and Val-boroPro releases it. NAIP–NLRC4 puts ligand recognition on NAIP
  (mouse NAIPs are specialised for flagellin vs T3SS needle/rod, humans have a
  single NAIP) while NLRC4 builds the platform and recruits caspase-1 with or
  without ASC. Both need their own module shapes.

## Disease Relevance

- CAPS (Cryopyrin-associated periodic syndromes)
- Gout, atherosclerosis
- Alzheimer's disease
- COVID-19 severity

## Modules

- [Canonical NLRP3 inflammasome](../modules/canonical_nlrp3_inflammasome.html) —
  the assembly chain, four parts, grounded on GO-CAM gomodel:635b1e3e00001811 and
  the NLRP3/GSDMD/CASP4 gene reviews.
- [Metazoan NLR signaling](../modules/nlr_signaling.html) — compact pathway-level
  view, NOD2–RIPK2 plus NLRP3–ASC–caspase-1.
- [Plant NLR resistosome signalling](../modules/plant_nlr_resistosome_signaling.html)
  — the plant counterpart, split out so the metazoan module's scope is unambiguous.
  Not part of this project, listed because the scope boundary was drawn here.

## Project Status

- [ ] Stub - needs gene folder setup
- [x] Canonical assembly chain modelled and reconciled with the 2025 CMI review
- [ ] Gene folders for PYCARD, CASP1, NEK7, IL1B, IL18 (PYCARD and NEK7 are the
      highest value: both are modelled above but neither has a review, and PYCARD
      currently has `GO:0070269 pyroptotic inflammatory response` by NAS only)
- [ ] Decide whether a shared ASC→caspase-1→GSDMD effector core module is worth
      factoring out before adding AIM2/NLRC4/NLRP1 sensor variants
- [ ] Ontology follow-up: the *inflammasome sensor activity* term proposed in the
      NLRP3 review is still the blocker for typing NLRP3's sensing function; the
      module works around it with `GO:0035591 signaling adaptor activity`
