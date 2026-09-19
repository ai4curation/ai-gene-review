---
title: "Pancrustacea Metamorphosis Gene Families"
maturity: IN_PROGRESS
tags: [BIOLOGY_DOMAIN]
species: [DROME]
genes: [kni, hairy, klg, trn, caps, kek1, krz, insc]
---

# Pancrustacea Metamorphosis Gene Families

**Four independent origins of metamorphic development across the arthropod
clade Pancrustacea repeatedly recruited *different* gene families that
nonetheless converge on the *same* developmental functions. This project
tracks the specific gene families that a recent phylogenomic study implicates
in that convergence, as candidates for GO-annotation review.**

## Source

Campli G, Chipman AD, Robinson-Rechavi M, Waterhouse RM.
*Convergent gene family evolution underpins repeated transitions to
metamorphic development across Pancrustacea.*
bioRxiv (2026), posted July 26, 2026.
doi: [10.64898/2026.05.06.723392](https://doi.org/10.64898/2026.05.06.723392)
(preprint, not peer reviewed; CC-BY 4.0).

This page is a reviewer's digest of that preprint plus a curation to-do list.
It is not a reproduction of the paper.

## What the paper does

The study asks whether the repeated evolution of **metamorphosis** —
a post-embryonic, moult-mediated life-stage progression to adulthood marked by
major morphological and ecological change — leaves a shared genomic signature.
It assembles a phylogenomic dataset of **54 species across 26 pancrustacean
orders** (median Arthropoda BUSCO completeness 95.8%) and time-calibrates a
species tree spanning ~500 My. Four clades are treated as **independent
evolutionary replicates** of a transition to metamorphic development
("Metamorphosis LCAs"):

| Metamorphic clade | Example taxa | Non-metamorphic sister ("Sister LCA") |
|---|---|---|
| **Insecta** | mayflies → flies | non-insect Hexapoda (springtails) |
| **Eucarida** | Decapoda (crabs, shrimp, lobster) + Euphausiacea (krill) | Peracarida (isopods, amphipods) |
| **Copepoda** | Calanoida, Harpacticoida | Branchiopoda (fairy shrimp, water fleas) |
| **Thecostraca** | barnacles (Balanomorpha, Pollicipedomorpha) | Podocopida (ostracods) |

Orthologous groups (OGs) were delineated at the Pancrustacea LCA with
OrthoLoger/OrthoDB (42,841 OGs, 782,987 genes, 73% of input), phyletic ages
assigned, and gene gains/losses reconstructed with CAFE v5 on ancient,
widespread OGs (≥85% species). GO enrichment (GenBank/RefSeq/FlyBase/InterPro
annotations) was contrasted between Metamorphosis LCAs, Sister LCAs, and deeper
ancestral nodes, and OU/BM evolutionary models tested for lineage-specific
adaptive expansions.

## Key findings a curator should carry

1. **More births, more expansions at metamorphic origins.** Metamorphosis LCAs
   show elevated gene-family births (8.7%, 3,722 OGs vs 2.6%, 1,112 at Sister
   LCAs) and expansions (2,078 OGs vs 843 at Sisters / 442 at Deep nodes).
   Emergent and expanding families are *more sequence-constrained* (lower
   divergence) than at Sister LCAs.
2. **Convergent functions, divergent genes.** Of 100 GO terms enriched among
   families expanding at any Metamorphosis LCA, **60 are shared by all four**
   (28 semantic clusters) — yet the expansions mostly involve **distinct
   genes**, not parallel expansion of the *same* family. Functional convergence
   is achieved through different genetic trajectories.
3. **The convergent functions** cluster on: central/peripheral nervous-system
   development and neurogenesis; epithelial and cuticle morphogenesis
   ("chitin-based cuticle development"); developmental maturation; neuropeptide
   signalling and regulation of autophagy; compound-eye/photoreceptor
   development; segmentation; and immune activation. These are all plausibly
   tied to the morphological reorganisation and adaptive-landscape shift of
   metamorphosis.
4. **A small adaptive core.** Of 528 shared-enrichment expanding families, only
   **15 (3%)** show OU two-optima signatures of lineage-specific adaptive
   expansion (largest optimum in the metamorphic lineages), annotated to
   nervous-system development, chitin-based cuticle development, dorsal closure,
   head involution, imaginal-disc-derived wing-vein/chaeta/salivary-gland
   morphogenesis, and MAPK-signalling regulation.
5. **Reframing moulting.** The authors argue the ancestral moulting programme is
   an *evolutionarily flexible developmental substrate* whose repeated
   modification enabled complex multi-phasic life histories — echoing (but
   distinct from) toolkit overlap seen in arthropod terrestrialisation studies.

**Curation caveat (stated by the authors, important here):** nearly all
functional knowledge for the named families comes from **model insects
(chiefly *Drosophila*)**. Copy number is dynamic across lineages, and
pleiotropy, post-duplication regulatory rewiring, and co-option/exaptation mean
insect-derived functions should *not* be assumed to transfer to crustacean
orthologues. Any review should keep organism-of-evidence explicit and resist
propagating *Drosophila* function onto uncharacterised paralogues.

## Candidate gene families for review

The paper singles out these families as showing adaptive, lineage-specific
expansion at metamorphic origins. Named genes below are the *Drosophila*
reference members — the natural entry points for a GO-annotation review, none
of which is yet reviewed in this corpus. "Family N" is the paper's numbering.

| Drosophila gene | Family | Protein type | Implicated roles (per paper) | Review |
|---|---|---|---|---|
| **knirps** (*kni*) | 11 | orphan nuclear receptor (NR0A1), C4 zinc-finger short-range repressor (gap gene) | segmentation (pair-rule control), tracheal branch morphogenesis, gut endoreduplication; regulates ecdysteroid-biosynthesis enzymes in prothoracic gland | ✅ [reviewed](../genes/DROME/kni/kni-ai-review.yaml) |
| **hairy** (*h*) | 5 | bHLH-Orange (HES-family) Groucho-recruiting repressor (pair-rule) | segmentation cascade (conserved across arthropods), sensory-bristle patterning via *achaete-scute* repression | ✅ [reviewed](../genes/DROME/hairy/hairy-ai-review.yaml) |
| **klingon** (*klg*) | 1 | GPI-anchored Ig-superfamily cell-adhesion glycoprotein | homophilic adhesion, R7 photoreceptor fate/differentiation, axon guidance, long-term memory | ✅ [reviewed](../genes/DROME/klg/klg-ai-review.yaml) |
| **Kurtz** (*krz*) | 12 | non-visual (β-)arrestin | GPCR binding/internalization adaptor; pleiotropic MAPK/Toll/Hedgehog/Notch attenuation | ✅ [reviewed](../genes/DROME/krz/krz-ai-review.yaml) |
| **inscuteable** (*insc*) | 7 | cytoskeletal spindle-orientation adaptor | apical-basal spindle orientation in asymmetric neuroblast/SOP division | ✅ [reviewed](../genes/DROME/insc/insc-ai-review.yaml) |
| **tartan** (*trn*) | 3 | LRR transmembrane adhesion molecule | motor-axon guidance, affinity boundaries, tracheal/salivary morphogenesis | ✅ [reviewed](../genes/DROME/trn/trn-ai-review.yaml) |
| **capricious** (*caps*) | 3 | LRR transmembrane adhesion molecule (trn paralog) | axon target recognition, homophilic adhesion, tracheal branch fusion | ✅ [reviewed](../genes/DROME/caps/caps-ai-review.yaml) |
| **kekkon-1** (*kek1*) | 9 | LRR + Ig transmembrane receptor-inhibitor | negative-feedback inhibition of EGFR signalling (binds DER directly) | ✅ [reviewed](../genes/DROME/kek1/kek1-ai-review.yaml) |

*deadpan (dpn)* is also mentioned alongside *knirps*/*hairy* in insect neural
development but was not called out as an adaptively expanding family.

**Suggested review order:** the two transcription factors *knirps* and *hairy*
are the best-characterised and most cross-lineage-informative starting points;
the adhesion/receptor families (*klingon*, *tartan*/*capricious*, *kekkon*) form
a coherent "neuronal wiring & disc morphogenesis" second batch; *Kurtz* and
*inscuteable* round out the signalling/asymmetric-division angle.

To start a review for any of these:

```bash
just fetch-gene DROME kni      # then deep research + notes, then the ai-review.yaml
```

## Open questions this paper raises for curation

- Do the *Drosophila* GO annotations for these families over-attribute
  insect-specific developmental roles (e.g. imaginal-disc terms) that cannot
  hold in crustacean orthologues? This is a candidate over-annotation pattern.
- For pleiotropic pair-rule/gap TFs (*hairy*, *knirps*), are segmentation,
  neurogenesis, and ecdysteroid-regulation roles all separately supported, or is
  one propagated from another by IEA/IBA?
- Which of the convergent GO clusters ("chitin-based cuticle development",
  "neuropeptide signalling pathway", "regulation of autophagy") are backed by
  experimental evidence in *Drosophila* vs inferred electronically?

## Status

**IN_PROGRESS.** All eight *Drosophila* reference genes named in the paper have
now been reviewed. The two transcription factors:

- **knirps (*kni*, P10734)** — 29 annotations adjudicated (17 ACCEPT, 8 MODIFY,
  3 KEEP_AS_NON_CORE, 1 REMOVE). Notable: removed an
  over-propagated `intracellular receptor signaling pathway` term (knirps is a
  ligand-independent orphan NR that lost its ligand-binding domain) and
  redirected the IBA `nuclear receptor activity` / `estrogen response element
  binding` terms and the bare `protein binding` IPIs to informative repressor /
  corepressor-binding terms.
- **hairy (*h*, P14003)** — 45 annotations adjudicated (28 ACCEPT, 9 MODIFY, 6
  KEEP_AS_NON_CORE, 1 UNDECIDED, 1 MARK_AS_OVER_ANNOTATED). Notable:
  resolved every `protein binding` IPI to its curated `WITH/FROM` partner — STUbL
  (Topors/Degringolade) ligase binding, Groucho/CtBP corepressor binding, and
  DNA-binding transcription factor binding for the Ultrabithorax interaction — and
  flagged a distal `membrane organization` term as over-annotation of a nuclear
  repressor.

The adhesion/receptor and signalling/asymmetric-division candidates are now also
reviewed:

- **klingon (*klg*, Q9VCT4)** — 19 annotations. GPI-anchored IgSF adhesion
  molecule; core homophilic-adhesion and R7 photoreceptor roles accepted, distal
  ethanol/long-term-memory behaviours kept non-core, bare `protein binding`
  redirected to `cell adhesion molecule binding` (WITH/FROM partner cDIP), and the
  IBA `axon guidance receptor activity` corrected to `cell-cell adhesion mediator
  activity` (as in *trn*), since a GPI-anchored protein cannot itself transduce a
  guidance signal.
- **tartan (*trn*, M9PFH7)** — 6 annotations. LRR adhesion molecule; IBA
  `signaling receptor activity` corrected to `cell-cell adhesion mediator
  activity` (propagated from a TLR-containing family).
- **capricious (*caps*, A0A0S0WP14)** — 11 annotations. LRR adhesion molecule
  (trn paralog); core homophilic-adhesion / axon-target-recognition accepted,
  tissue-specific contexts (some the cited papers found caps dispensable for)
  kept non-core.
- **kekkon-1 (*kek1*, Q9VK54)** — 22 annotations. Dedicated negative-feedback
  inhibitor of EGFR signalling; the EGF-receptor-binding / receptor-inhibitor /
  neg-reg-EGFR core is strongly experimentally supported and accepted.
- **Kurtz (*krz*, Q9V393)** — 21 annotations. Non-visual β-arrestin; core
  GPCR-binding/internalization adaptor accepted, the many pleiotropic
  signalling-attenuation roles (MAPK/Toll/Hedgehog/Notch) kept non-core.
- **inscuteable (*insc*, Q9W2R4)** — 30 annotations. Cytoskeletal
  spindle-orientation adaptor; `establishment of mitotic spindle localization`
  corrected to `…orientation`; two mis-cited/unverifiable references flagged in
  `reference_review`.

All eight reviews validate clean, with every `supporting_text` quote
independently confirmed verbatim against the cached literature. Each bare
`protein binding` IPI was resolved through the GOA `WITH/FROM` partner to a
specific binding term. The full candidate set named in the paper is now reviewed;
next steps are the GO-CAM/module angle (e.g. an ecdysteroid-biosynthesis-
regulation module) and, optionally, the secondary mentions (*deadpan*).

**Data-provenance note.** For *klingon* and *inscuteable*, `fetch-gene` first
resolved sparse TrEMBL accessions (3 and 1 annotations); the reviews use the
annotation-rich accessions **Q9VCT4** and **Q9W2R4** instead.
