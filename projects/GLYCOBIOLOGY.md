---
title: "Glycobiology Project"
maturity: IN_PROGRESS
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [human, mouse, rat, worm]
---

# Glycobiology Project

## Overview

Glycobiology studies the structure, biosynthesis, degradation, and biological
roles of glycans (sugars) and glycoconjugates (glycoproteins, glycolipids,
proteoglycans, GPI-anchored proteins). Glycosylation is the most common and
structurally diverse co-/post-translational modification: glycans decorate the
majority of the cell-surface and secreted proteome, mediate cell–cell and
host–pathogen recognition, and tune protein folding, trafficking, stability, and
signalling. Genetic defects in the glycosylation machinery cause the
[congenital disorders of glycosylation (CDGs)](https://www.ncbi.nlm.nih.gov/books/NBK579928/) —
a heterogeneous family of >130 Mendelian diseases — and aberrant glycosylation is
a hallmark of cancer, inflammation, and autoimmune disease.

This project has **two complementary aims**:

1. **GO-usage audit (animals).** Survey how the glycobiology-related GO term
   landscape — glycosyltransferase/glycosidase activities, carbohydrate binding
   (lectins), and the N-/O-linked/GPI glycosylation biological processes — is
   actually used to annotate animal gene products (human, mouse, rat, worm), and
   identify systematic over-/under-/mis-annotation patterns the way the
   [SPKW](SPKW.md), [RHEA](RHEA.md), and [INTERPRO](INTERPRO.md) source-audit
   projects do for their pipelines.
2. **External-resource landscape.** Map the dedicated glycoscience databases,
   ontologies, and tools (the GlySpace Alliance — GlyGen, GlyCosmos,
   Glyco@Expasy/GlyConnect — plus GlyTouCan, UniCarbKB, CAZy, and the
   GlycoConjugate Ontology GlycoCoO) and assess how each could feed, cross-check,
   or extend GO-based curation of glycogenes. Reference dossier:
   [GLYCOBIOLOGY-resources.md](GLYCOBIOLOGY/GLYCOBIOLOGY-resources.md).

The two aims meet at one question: **where does GO under-represent glycan biology
that the specialist glyco resources capture well, and where does GO
over-annotate glycogenes** (e.g. propagating downstream "guilt-by-substrate"
metabolic processes onto an enzyme that only adds one sugar)?

## The glycobiology GO term landscape

Key entry points into the ontology (GO IDs/labels verified against QuickGO,
GO release current as of 2026-06). Closure (descendant) sets under these terms
define the working scope of the audit.

### Molecular function (the enzymes and binders)

| GO ID | Label | Notes |
|-------|-------|-------|
| GO:0016757 | glycosyltransferase activity | builds glycosidic bonds from activated sugar donors; ~the CAZy **GT** families |
| GO:0016798 | hydrolase activity, acting on glycosyl bonds | glycosidases; ~the CAZy **GH** families (parent of glycosidase children) |
| GO:0030246 | carbohydrate binding | parent of the **lectin** activities |
| GO:0120153 | calcium-dependent carbohydrate binding | C-type lectin domain signature |
| GO:0097367 | carbohydrate derivative binding | nucleotide-sugar / activated-donor binding |

### Biological process (where the sugars go)

| GO ID | Label | Notes |
|-------|-------|-------|
| GO:0070085 | glycosylation | broad parent process |
| GO:0006486 | protein glycosylation | protein-acceptor branch |
| GO:0006487 | protein N-linked glycosylation | Asn-linked; dolichol/OST pathway |
| GO:0006493 | protein O-linked glycosylation | Ser/Thr-linked |
| GO:0036066 | protein O-linked glycosylation via fucose | e.g. POFUT1/2 on EGF/TSR repeats (Notch) |
| GO:0180059 | protein O-linked glycosylation via glucose | e.g. POGLUT on EGF repeats |
| GO:0006505 | GPI anchor metabolic process | PIG-/PGAP- gene family |
| GO:0006506 | GPI anchor biosynthetic process | dolichol-phosphate / ER-luminal assembly |
| GO:0120574 | GPI anchor remodelling | post-attachment editing (PGAP genes) |

These anchor terms give a reproducible way to pull the animal glycogene set from
GOA for the usage audit (filter by aspect + closure under these IDs, restricted
to the animal taxa we curate).

## External glycoscience resources (landscape)

Full dossier with URLs, identifier schemes, licences, and programmatic-access
notes: **[GLYCOBIOLOGY-resources.md](GLYCOBIOLOGY/GLYCOBIOLOGY-resources.md)**.
Headline resources:

| Resource | Type | Role for GO curation |
|----------|------|----------------------|
| [GlyGen](https://www.glygen.org/) | Integrating portal (glycoprotein- + glycan-centric); REST API + SPARQL | one-stop cross-reference hub; harmonises GlyConnect, UniCarbKB, GlyTouCan, CAZy, UniProt |
| [GlyTouCan](https://glytoucan.org/) | International glycan-structure repository (accessions) | the canonical glycan-structure identifier space |
| [GlyCosmos](https://glycosmos.org/) | Web portal integrating glyco- with omics (JSCR) | gene/disease/pathway links; RDF |
| GlyConnect / [Glyco@Expasy](https://www.expasy.org/glycomics) | Glycan structures, sites, biosynthetic enzymes | enzyme↔glycan↔site evidence to cross-check MF annotations |
| [UniCarbKB](https://unicarbkb.org/) | Curated glycan structures + glycoprotein sites | site-level glycosylation evidence |
| [CAZy](http://www.cazy.org/) | Carbohydrate-active enzyme families (GT/GH/PL/CE/CBM) | sequence-family ↔ activity mapping; sanity-checks MF over-/under-annotation |
| [GlycoCoO](https://github.com/glycoinfo/GlycoCoO) | GlycoConjugate Ontology | semantic model for glycoconjugate annotation; alignment target for GO |

The GlySpace Alliance (GlyGen + Glyco@Expasy + GlyCosmos) is the coordinating
umbrella; GlyTouCan is the shared structure-ID backbone they all link to.

## Exemplar reviews (calibration set)

Three human genes were chosen to calibrate the over-/under-annotation hypotheses
across the main functional axes of animal glycobiology — one **glycosyltransferase**,
one **lectin**, and one **CDG** gene:

| Gene | UniProt | Axis | Why chosen | GOA annotations |
|------|---------|------|------------|----------------:|
| **B3GALNT2** | Q8NCR0 | Glycosyltransferase (CAZy GT31) | β-1,3-GalNAc-T in α-dystroglycan O-mannosyl glycan (matriglycan) elongation; dystroglycanopathy (secondary CDG); already flagged in [RHEA](RHEA.md) as lacking a specific acetylgalactosaminyltransferase GO term | 16 |
| **LGALS3** | P17931 | Lectin (galectin) | chimera-type β-galactoside-binding galectin; large, pleiotropic annotation set — ideal stress-test for the "generic protein binding → carbohydrate binding" and pleiotropy/non-core hypotheses | 105 |
| **PMM2** | O15305 | CDG (precursor supply) | phosphomannomutase 2; PMM2-CDG (CDG-Ia) is the most common CDG; tests "substrate guilt-by-association" on a metabolic enzyme that only supplies a GDP-mannose precursor | 23 |

Each gene was fetched (`fetch-gene`) and fully reviewed against the repo workflow
(literature research, per-annotation action, `core_functions`,
`proposed_new_terms`). All three validate clean (`status: DRAFT`).

### Verdict distributions

| Gene | N | ACCEPT | NON_CORE | OVER_ANNOTATED | MODIFY | REMOVE |
|------|--:|-------:|---------:|---------------:|-------:|-------:|
| B3GALNT2 (GT) | 16 | 5 | 2 | 3 | 6 | 0 |
| LGALS3 (lectin) | 105 | 21 | 64 | 20 | 0 | 0 |
| PMM2 (CDG) | 23 | 16 | 2 | 1 | 1 | 3 |

### What the exemplars confirmed (audit hypotheses → evidence)

- **Substrate "guilt-by-association" over-annotation is real and gene-class-dependent.**
  Both the GT (B3GALNT2) and the precursor enzyme (PMM2) carry downstream
  whole-pathway/process terms that exceed their molecular role. On B3GALNT2 the
  broad `glycoprotein biosynthetic process` / generic `protein O-linked
  glycosylation` were **MODIFY**'d down to the precise `GO:0035269` (O-mannosyl,
  the α-dystroglycan core-M3 pathway it actually elongates). On PMM2 — which only
  supplies the GDP-mannose precursor and is **not** a glycosyltransferase —
  `protein N-linked glycosylation` and `glycoprotein biosynthetic process` were
  kept **NON_CORE** (true at the disease/organism level, not the enzyme's MF).
- **Generic-MF-term collapse to the specific activity.** B3GALNT2's parent terms
  (`UDP-glycosyltransferase activity`, `hexosyltransferase activity`, IEA/IBA)
  were MODIFY'd to the IDA/TAS-supported specific `GO:0008376`.
- **Lectin "protein binding" under-specificity is pervasive.** Galectin-3 carried
  **21** generic `protein binding` (GO:0005515) IPI annotations — *all* downgraded
  as uninformative; many are in fact glycan-mediated lectin contacts whose
  informative MF is `carbohydrate binding` (GO:0030246) / galactoside binding.
- **Pleiotropy ≠ core.** The dominant LGALS3 verdict was **KEEP_AS_NON_CORE (64/105)**:
  its immune/apoptosis/fibrosis/cancer biology is downstream of one core
  activity — β-galactoside binding by the single CRD plus N-terminal-tail
  self-association/LLPS giving lattice multivalency.
- **GO coverage gaps surfaced for curation.** Reviews proposed **4 new terms**:
  a protein-O-mannose β-1,3-GalNAc-transferase activity (B3GALNT2, closing the
  [RHEA](RHEA.md)-flagged EC 2.4.1.313 gap); a phosphomannomutase-in-GDP-mannose-
  biosynthesis term (PMM2, to capture precursor supply at correct granularity);
  and galectin-glycan-lattice-assembly + damaged-endomembrane-glycan-sensor terms
  (LGALS3).
- **Citation hygiene.** The PMM2 review flagged FlyBase's `GDP-mannose
  biosynthetic process` IMP as **MISCITED** (PMID:9525984 is about MPI/CDG-Ib, a
  different enzyme) — kept the correct term but recorded the wrong reference via
  `reference_review` rather than overruling the experimental annotation.

Net: across 144 annotations the verdict skew (only 3 REMOVE, all
high-throughput-interactome `protein binding`; heavy NON_CORE + MODIFY) matches
the project's prediction — glycogene mis-annotation is dominated by **altitude /
specificity and pleiotropy**, not outright wrong functions.

## Candidate animal genes already in the repo

The corpus already contains glyco-relevant gene reviews that can seed the audit
without new fetches — useful for calibrating annotation patterns before scaling:

- **GPC6** (human glypican) — heparan-sulfate proteoglycan
- **Notch1 / NOTCH1** (mouse, human) — O-fucosylation substrate; entry point to POFUT/POGLUT biology
- **Uggt1** (rat) — UDP-glucose:glycoprotein glucosyltransferase (ER glycoprotein folding QC)
- **Aga** (rat) — aspartylglucosaminidase (N-glycan catabolism; aspartylglucosaminuria)
- **Ugt2a1 / Ugt85A2** (rat, plant) — UDP-glucuronosyl/glucosyltransferases (small-molecule GTs — note paralog/specificity pitfalls)
- **clec-60** (worm), **lys-7** (worm) — C-type lectin / carbohydrate-recognition domain proteins
- **ROT1, CNE1, CRH1, PDI1** (yeast) — ER glycoprotein folding/QC context (out-of-animal-scope but methodologically adjacent)

A reproducible GOA closure query (per the term table above) will produce the
fuller candidate list; these are the already-curated anchors.

## Curation considerations (hypotheses to test in the audit)

- **Substrate "guilt-by-association" over-annotation.** A glycosyltransferase
  that adds one sugar may be annotated to the whole downstream pathway/process of
  the mature glycan (cf. the RHEA/EC altitude problem). Expect `MARK_AS_OVER_ANNOTATED`
  / `MODIFY` candidates.
- **Paralog/specificity errors in large GT families.** UGT, GALNT, ST3GAL/ST6GAL,
  B3GALNT, fucosyltransferase families are big and sequence-similar; IEA/IBA
  propagation can land the wrong substrate specificity on the wrong paralog
  (cf. the de Crécy-Lagard PLI/`PARALOG_OVERANNOTATION` pattern).
- **Lectin "protein binding" under-specificity.** Carbohydrate-binding proteins
  are often annotated only with generic `protein binding`; the informative
  `carbohydrate binding` (GO:0030246) child is the better MF (per repo guidance
  to avoid `protein binding`).
- **GO vs specialist-resource coverage gaps.** Site-level and structure-level
  glycosylation evidence in GlyConnect/UniCarbKB may have no GO counterpart →
  `proposed_new_terms` / gap-filling candidates, mirroring the RHEA reverse-gap
  analysis.

## Open questions

- How large is the animal glycogene set under the anchor terms, and what is the
  ACCEPT/MODIFY/OVER/REMOVE verdict distribution relative to the corpus baseline?
- Can CAZy GT/GH family membership be used as an independent check on
  glycosyltransferase/glycosidase MF annotations (right family → right activity
  class)?
- Which GlyConnect/UniCarbKB enzyme→glycan→site facts have no GO representation,
  and are they new-term candidates?
- Is GlycoCoO alignable to GO well enough to import/cross-validate annotations?

## Status

- **Started**: 2026-06-21
- **Maturity**: IN_PROGRESS — scope, GO anchor-term set (QuickGO-verified), and
  external resource landscape defined; **3 exemplar reviews complete** (B3GALNT2,
  LGALS3, PMM2; 144 annotations; all validate clean) and they confirm the
  altitude/specificity + pleiotropy over-annotation hypotheses.
- **Next steps**: (1) run the GOA closure query for the anchor terms across the
  animal taxa to enumerate the glycogene set and its verdict baseline; (2) flesh
  out [GLYCOBIOLOGY-resources.md](GLYCOBIOLOGY/GLYCOBIOLOGY-resources.md) with
  access recipes; (3) promote the 4 exemplar `proposed_new_terms` as GO new-term
  requests; (4) extend the review pass to the already-curated anchor genes
  (GPC6, Notch1/POFUT axis, Uggt1).
