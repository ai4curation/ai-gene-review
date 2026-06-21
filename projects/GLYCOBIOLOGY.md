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

### Reusing these resources for curation

How the resources feed GO curation (forward `cazy2go` propagation, GlycoCoO→GO
alignment, and confirmatory GlyGen cross-checks; GO-CAM/pathway deferred) is a
decision record in
[GLYCOBIOLOGY-resource-reuse.md](GLYCOBIOLOGY/GLYCOBIOLOGY-resource-reuse.md),
with a seeded [`cazy2go.sssom.yaml`](GLYCOBIOLOGY/cazy2go.sssom.yaml) (CAZy
family → GO molecular function, the glyco analogue of `interpro2go`) built from
the exemplar GT families.

## Exemplar reviews (calibration set)

Seven human genes were reviewed to calibrate the over-/under-annotation
hypotheses across the main functional axes of animal glycobiology. Phase 1
covered one **glycosyltransferase**, one **lectin**, and one **CDG** gene;
Phase 2 broadened the GT axis across four more transferase sub-types
(O-fucosyl-, GlcNAc-branching-, sialyl-, galactosyl-). Each Phase-2 gene was
reviewed with a **FutureHouse Falcon deep-research report integrated from the
start**, and the Phase-1 three were retro-fitted with their Falcon findings.

| Gene | UniProt | Axis (CAZy) | Why chosen |
|------|---------|-------------|------------|
| **B3GALNT2** | Q8NCR0 | β-1,3-GalNAc-T (GT31) | α-dystroglycan O-mannosyl (matriglycan) elongation; dystroglycanopathy (secondary CDG); [RHEA](RHEA.md)-flagged GO gap |
| **LGALS3** | P17931 | lectin (galectin) | chimera-type β-galactoside-binding galectin; large pleiotropic set — protein-binding + pleiotropy stress-test |
| **PMM2** | O15305 | CDG (precursor) | phosphomannomutase 2; PMM2-CDG is the commonest CDG; "guilt-by-association" on a precursor-supply enzyme |
| **POFUT1** | Q9H488 | O-fucosyl-T (GT65) | ER O-fucosyltransferase on EGF repeats; Notch O-fucosylation; ER (not Golgi) localization test |
| **MGAT1** | P26572 | GlcNAc-T I (GT13) | medial-Golgi gatekeeper committing N-glycans to hybrid/complex processing |
| **ST6GAL1** | P15907 | sialyl-T (GT29) | trans-Golgi α-2,6-sialyltransferase (CD22 ligand / CD75 epitope) |
| **B4GALT1** | P15291 | β-1,4-Gal-T (GT7) | LacNAc synthase; bifunctional lactose synthase with α-lactalbumin; CDG-IID |

All seven validate clean (`status: DRAFT`).

### Verdict distributions (authoritative, from the YAMLs)

| Gene | N | ACCEPT | NON_CORE | OVER | MODIFY | REMOVE | NEW |
|------|--:|-------:|---------:|-----:|-------:|-------:|----:|
| B3GALNT2 | 16 | 5 | 2 | 2 | 7 | 0 | 0 |
| LGALS3 | 106 | 21 | 64 | 20 | 0 | 0 | 1 |
| PMM2 | 23 | 16 | 2 | 1 | 1 | 3 | 0 |
| POFUT1 | 21 | 15 | 2 | 3 | 1 | 0 | 0 |
| MGAT1 | 26 | 11 | 6 | 5 | 4 | 0 | 0 |
| ST6GAL1 | 35 | 23 | 5 | 2 | 4 | 1 | 0 |
| B4GALT1 | 76 | 44 | 21 | 6 | 5 | 0 | 0 |
| **Total** | **303** | **135** | **102** | **39** | **22** | **4** | **1** |

Only **4/303 REMOVE** (all high-throughput-interactome `protein binding`), against
**102 NON_CORE + 39 OVER + 22 MODIFY** — i.e. ~54% of annotations are *demoted or
refined* but ~99% are *retained in some form*. The mis-annotation signal is
overwhelmingly **altitude/specificity and pleiotropy**, not wrong functions —
exactly the project's prediction.

### What the exemplars confirmed (audit hypotheses → evidence)

- **Generic-MF-term collapse to the specific activity is the dominant GT fix.**
  Every transferase carried over-general parent MF terms that were **MODIFY**'d to
  the specific child: B3GALNT2 (`UDP-glycosyltransferase`/`hexosyltransferase` →
  `GO:0008376`), MGAT1 (`acetylglucosaminyltransferase` → `GO:0003827` GlcNAc-TI),
  ST6GAL1 (`sialyltransferase` → `GO:0003835` α-2,6-sialyl-T), B4GALT1
  (`galactosyltransferase`/`UDP-galactosyltransferase` → `GO:0003831`).
- **Substrate "guilt-by-association" over-annotation is real and gene-class-dependent.**
  GTs and the precursor enzyme (PMM2) carry downstream whole-pathway terms beyond
  their molecular role. B3GALNT2's broad process terms were MODIFY'd to the precise
  `GO:0035269` (O-mannosyl). PMM2 — which only supplies GDP-mannose and is *not* a
  glycosyltransferase — had `protein N-linked glycosylation` kept **NON_CORE**.
  MGAT1's many complex-N-glycan-dependent physiologies are likewise NON_CORE.
- **Compartment errors.** POFUT1 is a soluble **ER-luminal** enzyme; its `membrane`
  calls (TM-prediction/proteomics) were over-annotated and ER localization affirmed
  — a reminder that GT localization annotations need the right organelle.
- **Lectin "protein binding" under-specificity is pervasive.** Galectin-3 carried
  **21** generic `protein binding` (GO:0005515) IPI annotations — *all* downgraded;
  many are glycan-mediated lectin contacts whose informative MF is `carbohydrate
  binding` (GO:0030246).
- **Pleiotropy ≠ core.** The dominant LGALS3 verdict was **NON_CORE (64/106)**; its
  immune/apoptosis/fibrosis/cancer biology is downstream of one core activity
  (β-galactoside CRD binding + N-terminal LLPS lattice). A new `GO:0062093 lysophagy`
  annotation was *added* (the damaged-endomembrane glycan-sensing role).
- **GO coverage gaps surfaced for curation — 7 `proposed_new_terms`** across the set:
  protein-O-mannose β-1,3-GalNAc-T activity (B3GALNT2, the [RHEA](RHEA.md)-flagged
  EC 2.4.1.313 gap); galectin-glycan-lattice-assembly + damaged-endomembrane-glycan-
  sensor (LGALS3); phosphomannomutase-in-GDP-mannose-biosynthesis (PMM2);
  O-fucosylation-coupled ER quality control (POFUT1); oligomannose→complex N-glycan
  conversion (MGAT1); protein-N-glycan α-2,6-sialyltransferase activity (ST6GAL1);
  and a **lactose synthase complex** CC term (B4GALT1).
- **Citation hygiene (verify, don't trust).** Reviews flagged real citation problems
  via `reference_review`: PMM2's FlyBase IMP **MISCITED** (PMID:9525984 is MPI/CDG-Ib,
  a different enzyme); POFUT1's MF TAS to a *Drosophila* survey marked MISCITED; and
  across all Falcon integrations, preprint-only / unresolvable-PMID claims and a
  stale EC number (ST6GAL1 "2.4.99.1" → current 2.4.3.1) were rejected and recorded
  in notes rather than cited.

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
  external resource landscape defined; **7 exemplar reviews complete** (B3GALNT2,
  LGALS3, PMM2, POFUT1, MGAT1, ST6GAL1, B4GALT1; 303 annotations; all validate
  clean), each backed by a **FutureHouse Falcon deep-research report** integrated
  into the YAML. They confirm the altitude/specificity + pleiotropy
  over-annotation hypotheses (135 ACCEPT / 102 NON_CORE / 39 OVER / 22 MODIFY /
  4 REMOVE / 1 NEW).
- **Next steps**: (1) run the GOA closure query for the anchor terms across the
  animal taxa to enumerate the glycogene set and its verdict baseline; (2) flesh
  out [GLYCOBIOLOGY-resources.md](GLYCOBIOLOGY/GLYCOBIOLOGY-resources.md) with
  access recipes; (3) promote the 7 exemplar `proposed_new_terms` as GO new-term
  requests; (4) extend the review/Falcon pass to the already-curated anchor genes
  (GPC6, Notch1, Uggt1) and a glycosidase/CDG type-II gene.
