---
title: "G protein-coupled receptors (GPCRs): families, modules and functions"
maturity: SCOPING
last_reviewed: 2026-10-15
tags: [BIOLOGY_DOMAIN, FLAGSHIP]
species: [human]
genes: [ADRB2, ADGRV1, FZD7, GPR101, GPR161, CASR, GNAS, OPRM1]
---

# G protein-coupled receptors (GPCRs): families, modules and functions

**Bottom line:** GPCRs are the largest receptor superfamily in the human genome
and the targets of a large share of approved drugs, yet only a handful have a
review here (human ADRB2, ADGRV1, FZD7, GPR101, GPR161, CASR and OPRM1, plus the transducer GNAS). This
project curates the superfamily on three levels: **families** (whether
PANTHER/PAINT and InterPro propagation of GPCR terms is safe), **modules**
(the transducer pathways downstream of the receptors), and **gene functions**
(per-gene reviews, starting with receptors that are drug targets). It is
paired with the dismech project
[GPCR drug mechanisms and disease modules](https://github.com/monarch-initiative/dismech/blob/main/projects/GPCR.md),
which uses the same receptors as the molecular anchors for drug-mechanism and
disease modules.

## Why GPCRs

- **Annotation volume, uneven depth.** `GO:0004930` G protein-coupled receptor
  activity and `GO:0007186` G protein-coupled receptor signaling pathway are
  among the most propagated terms in the corpus, mostly via IBA and
  InterPro2GO. The ligand-specific MF terms (e.g. `GO:0004941`
  beta2-adrenergic receptor activity) are much thinner, and the coupling
  terms (`GO:0007189` adenylate cyclase-activating, `GO:0007193`
  adenylate cyclase-inhibiting, `GO:0007200` phospholipase C-activating) are
  inconsistently applied.
- **Families are large and functionally heterogeneous.** Class A alone spans
  aminergic, peptide, lipid, nucleotide, olfactory and orphan receptors; a
  family-wide term is only safe at the right node.
- **Direct bridge to disease and pharmacology.** The receptors carrying the
  best experimental evidence are also the drug targets dismech needs as
  anchors (beta-blockers, opioids, GLP-1 agonists, calcimimetics,
  antipsychotics, triptans, antihistamines).

## Workstream 1 — Families

Review PANTHER families for the coherence of GPCR terms, following the
[Protein Families](FAMILIES.md) and [IBA review](IBA_REVIEW.md) conventions.
Candidate families (ids and names read from `interpro/panther/panther.obo`;
membership still to be checked against the PANTHER member index before any
module uses them):

| PANTHER id | PANTHER name | Question |
|---|---|---|
| PTHR24248 | ADRENERGIC RECEPTOR-RELATED G-PROTEIN COUPLED RECEPTOR | Which aminergic subfamilies does it contain, and at what node does Gs vs Gi/o vs Gq coupling diverge? |
| PTHR24247 | 5-HYDROXYTRYPTAMINE RECEPTOR | Same coupling question across 5-HT1/2/4/6/7. |
| PTHR24249 | HISTAMINE RECEPTOR-RELATED G-PROTEIN COUPLED RECEPTOR | H1 (Gq) vs H2 (Gs) vs H3/H4 (Gi/o). |
| PTHR24246 | OLFACTORY RECEPTOR AND ADENOSINE RECEPTOR | A mixed family name; check what the adenosine receptors share with ORs. |
| PTHR26452, PTHR26453, PTHR26454 | OLFACTORY RECEPTOR | Deferred (see Decisions). |
| PTHR11394 | TASTE RECEPTOR TYPE 2 | Bitter-taste receptors; extra-oral roles. |
| PTHR24060 | METABOTROPIC GLUTAMATE RECEPTOR | Class C; glutamate vs GABA-B vs CaSR divergence. |
| PTHR24061 | CALCIUM-SENSING RECEPTOR-RELATED | CASR, GPRC6A, taste type 1. |
| PTHR12011 | ADHESION G-PROTEIN COUPLED RECEPTOR | Many members have no demonstrated G protein coupling; tethered-agonist mechanism. |
| PTHR11309 | FRIZZLED | Wnt receptors: is `GO:0004930` justified, or should coupling be left to SMO-like evidence? |
| PTHR11334 | MAS-RELATED G-PROTEIN COUPLED RECEPTOR | Primate-expanded MRGPRs; itch/mast-cell ligands. |
| PTHR11792 | ARRESTIN | Visual vs beta-arrestins; scaffolding functions. |
| PTHR24355 | G PROTEIN-COUPLED RECEPTOR KINASE/RIBOSOMAL PROTEIN S6 KINASE | A family that mixes GRKs with S6 kinases; kinase substrate terms must not cross the split. |

Several PANTHER families are named only "G-PROTEIN COUPLED RECEPTOR"
(e.g. PTHR22750, PTHR24230, PTHR24232); their contents are to be identified
from the member index, not guessed from the name.

Deliverable per family: a family review (coherence call, term-scope calls for
`GO:0004930`, the coupling BP terms, and the ligand-specific MF terms), and
IBA findings feeding [IBA_REVIEW](IBA_REVIEW.md).

## Workstream 2 — Modules

Two GPCR modules exist as drafts: `gpcr_camp_pka_signaling` (Gs) and
`gpcr_plc_calcium_pkc_signaling` (Gq). Related existing modules:
`chemokine_signaling`, `wnt_signaling`, `hedgehog_signaling`.

Planned work, using the module-curation skill:

1. **Promote the two drafts**: ground GNAS, ADCY5, PRKACA, CREB1 and the Gq
   parts in PAINT nodes where the evidence is clear; otherwise leave PTN
   claims out.
2. **Gi/o inhibitory module**: Gi/o alpha inhibition of adenylyl cyclase plus
   G beta-gamma activation of GIRK channels and inhibition of voltage-gated
   calcium channels (the opioid, D2, alpha2, M2 and GABA-B arm).
3. **G12/13-RhoA module**: Galpha12/13, RhoGEFs (ARHGEF1/11/12), RhoA-ROCK.
4. **Receptor desensitization and arrestin module**: GRK phosphorylation,
   arrestin recruitment, clathrin-dependent internalization, recycling vs
   degradation. This is where `GO:1904022` positive regulation of G
   protein-coupled receptor internalization and the arrestin-scaffold terms
   belong.
5. **RGS GAP module**: RGS-accelerated GTP hydrolysis terminating signaling
   (RGS4 and the R7/R4 subfamilies).
6. **Rod phototransduction** as a well-characterized exemplar (rhodopsin,
   transducin, PDE6, GRK1, visual arrestin), if no existing module already
   covers it.

Each module should list the receptor gene reviews it depends on; a module
part with no reviewed gene is a curation gap recorded in the module `notes`.

## Workstream 3 — Gene functions

Per-gene reviews with the `review` skill. Order by how much each review
unblocks: a receptor that anchors a dismech drug-mechanism module, a module
part, or a family review comes first.

**Tranche 1 — drug-target receptors** (each anchors a dismech module):
ADRB1, ADRB2 (refresh), ADRA1A, ADRA2A, DRD2, HTR2A, HTR1B, HTR1D, OPRM1,
HRH1, HRH2, AGTR1, GLP1R, GIPR, CASR (refresh), CHRM3, S1PR1, P2RY12, CNR1, MC4R,
CALCRL, TSHR.

**Tranche 2 — transducers and regulators** (module parts): GNAS (refresh), GNAI1,
GNAI2, GNAO1, GNAQ, GNA11, GNA12, GNA13, GNB1, GNG2, ARRB1, ARRB2, GRK2,
GRK3, GRK5, GRK6, RGS2, RGS4, ADCY5, PLCB1.

**Tranche 3 — disease-gene receptors without a drug** (feed dismech disease
modules): RHO, OPN1LW, MC2R, PTH1R, AVPR2, GNRHR, KISS1R, LHCGR, FSHR,
GPR143, ADGRG1, ADGRV1 (refresh), FZD4.

Recurring function questions to resolve while reviewing:

- `GO:0004930` alone is uninformative when a ligand-specific child is
  supported; use `MODIFY` toward the specific term (e.g. `GO:0004941`).
- Coupling BP terms: annotate the Galpha class with direct evidence, not the
  one inferred from family membership.
- Orphan receptors: keep `GO:0004930` only with evidence of G protein
  coupling; constitutive-activity evidence (GPR101, GPR161) counts.
- Arrestin-biased and G protein-independent signaling: decide when an
  arrestin-dependent BP is warranted (cf. `GO:0160213`
  beta-arrestin-dependent dopamine receptor signaling pathway).
- Frizzled and adhesion GPCRs: whether the GPCR MF terms reflect the
  receptor's actual mechanism.

## First pairing: mu-opioid receptor

Chosen as the first receptor (2026-10-15) because dismech already has many
opioid-treated entries waiting for a shared mechanism module. Gene side:

- OPRM1 gene review (then OPRD1, OPRK1, OPRL1, so one family call covers
  the classical opioid receptors; their PANTHER family is to be identified
  from the member index, since no PANTHER family name mentions them)
- Gi/o module: adenylyl cyclase inhibition, G beta-gamma activation of GIRK
  channels and inhibition of voltage-gated calcium channels
- Desensitization/arrestin module: GRK phosphorylation, beta-arrestin
  recruitment, internalization (the tolerance-relevant arm)

The dismech side builds the mu-opioid agonism and antagonism modules on top.

## Plan

- [x] OPRM1 gene review

- [ ] Pull GOA term counts for all human GPCRs to size the over-annotation problem
- [ ] Family reviews for PTHR24248, PTHR24247, PTHR24249 (aminergic)
- [ ] Family reviews for PTHR12011 (adhesion) and PTHR11309 (Frizzled)
- [ ] Taste receptor family call (PTHR11394)
- [ ] Promote `gpcr_camp_pka_signaling` and `gpcr_plc_calcium_pkc_signaling`
- [ ] New modules: Gi/o, G12/13-RhoA, desensitization/arrestin, RGS
- [ ] Tranche 1 gene reviews (agree the list with the dismech side)
- [ ] Tranche 2 gene reviews
- [ ] Tranche 3 gene reviews
- [ ] Cross-link each reviewed receptor to the dismech module that uses it

## Decisions

- **Olfactory receptors are deferred** (decided 2026-10-15): no family or
  per-gene review of the ~400 human ORs for now.

## Open questions

- Should a GPCR family index page (like the CASPL one) be generated, or do
  family reviews live only under `interpro/panther/`?
- Do we use GPCRdb / IUPHAR-Guide to Pharmacology classifications as a
  reference alongside PANTHER, and if so how are they cited?
