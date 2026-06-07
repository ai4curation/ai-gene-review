# Contractile Vacuole Tethering — Obsoletion & Replacement (GO:0140025)

## Overview

A GO obsoletion proposal retires **GO:0140025 contractile vacuole tethering
involved in discharge** (a BP term). The rationale mirrors the parallel
membrane-tether obsoletions in this batch (ER–PM, mito–ER,
peroxisome–chloroplast): the activity is more appropriately captured at the
molecular function level. The new MF term
**GO:7770067 contractile vacuole-plasma membrane tether activity** has been
added upstream as the replacement, with parent
**GO:0140177 membrane-membrane adaptor activity**.

This project tracks the impact on AI Gene Review and queues the two affected
*Dictyostelium discoideum* genes (rab8A and p2xA) for review.

## Upstream tickets

- Annotation tracker: [geneontology/go-annotation#6387](https://github.com/geneontology/go-annotation/issues/6387)
- Ontology ticket: [geneontology/go-ontology#31870](https://github.com/geneontology/go-ontology/issues/31870)
- New term PR: [geneontology/go-ontology#31942](https://github.com/geneontology/go-ontology/pull/31942) (adds GO:7770067)
- Obsoletion PR: [geneontology/go-ontology#31950](https://github.com/geneontology/go-ontology/pull/31950) (obsoletes GO:0140025)

## Obsoletion plan (per upstream)

| Obsoleted term | ID | Replacement |
|---|---|---|
| contractile vacuole tethering involved in discharge | GO:0140025 | MF: GO:7770067 contractile vacuole-plasma membrane tether activity |

The new MF term definition (per upstream PR #31942):

> The binding activity of a molecule that brings together the contractile
> vacuolar membrane and the plasma membrane, either via membrane lipid binding
> or by interacting with a membrane protein, to establish or maintain the
> localization of the contractile vacuole at a specific plasma membrane
> discharge site. [PMID:22323285]

Synonyms: "contractile vacuole-plasma membrane tethering activity" (EXACT),
"plasma membrane-contractile vacuole tether activity" (EXACT).

### Affected upstream groups (from issue body)

| Group | Annotations | Status |
|---|---:|---|
| dictyBase | 2 | pending — "May be automatically transferred" per upstream |

The two annotations are:

| Gene | Locus | UniProt | Reference | Evidence |
|---|---|---|---|---|
| rab8A | DDB_G0280043 | P20790 | PMID:22323285 | IMP |
| p2xA  | DDB_G0272004 | Q86JM7 | PMID:24335649 | IMP |

### Mappings to be reviewed

None. The issue body explicitly lists no InterPro2GO, UniProt-Keywords, or
UniRule mappings for GO:0140025.

## Impact on this repo

Neither rab8A nor p2xA is currently reviewed in this repository
(`genes/DICDI/` contains tlcd4b, mlcD, and nip7 — none of the contractile
vacuole tether annotations). This means **no existing reviews need refresh**
for the obsoletion itself, but the two affected genes represent a coherent
small candidate set for proactive review now that the replacement MF term
is in place.

## Scope

- **Organisms**: *Dictyostelium discoideum* only. The contractile vacuole is
  a Protozoan/protist organelle, and these are the only two direct annotations
  to GO:0140025 in the GO annotation database.
- **GO branches**: BP (the obsoleted term itself) and the new MF
  GO:7770067. Both sit in the membrane contact site / membrane-adaptor branch
  under GO:0140177.
- **Type of fix**: terminological in GO; the underlying biology
  (Essid et al. 2012 on Rab8a-mediated kiss-and-run discharge; Sivaramakrishnan
  & Fountain 2013 on the P2X receptor) is well established. Reviews should
  evaluate whether the MF replacement is the better core-function term and
  add it where the underlying IMP evidence supports it.

## Candidate genes for initial review

Verify each with `just fetch-gene DICDI <gene>` before starting; confirm the
UniProt accession from the UniProt API.

1. **rab8A** (*D. discoideum*, UniProt P20790, locus DDB_G0280043) — Rab8a
   small GTPase. PMID:22323285 (Essid et al. 2012, *Mol Biol Cell*) is the
   anchor publication for the new MF term itself: "Rab8a regulates the
   exocyst-mediated kiss-and-run discharge of the *Dictyostelium*
   contractile vacuole". This is the cleanest review target — the underlying
   experiment characterised the molecular tethering activity of Rab8a at the
   contractile vacuole / plasma membrane discharge site.

2. **p2xA** (*D. discoideum*, UniProt Q86JM7, locus DDB_G0272004) — P2X
   receptor A (DdP2X). PMID:24335649. The IMP annotation should be evaluated
   carefully: P2X receptors are normally Ca²⁺/cation channels, so the
   tether-activity assignment should be verified against the paper's actual
   loss-of-function phenotype before accepting GO:7770067 as a core function.
   This is the more interpretation-sensitive review.

## Proposed approach and priority

1. **Wait for the dictyBase migration.** The issue body notes that the two
   annotations "may be automatically transferred". If dictyBase has not yet
   migrated them at the time of review, the new rows should appear under
   GO:7770067; the review can then ACCEPT (rab8A) or assess (p2xA) the
   migrated MF annotations directly.

2. **Anchor on rab8A.** rab8A is the direct PMID:22323285 case that motivated
   the new MF term, so it is the natural anchor review. ACCEPT GO:7770067
   as a core function, capture the exocyst interaction
   (rab8A → Sec3/Sec5 etc.) as a related binding activity, and propose
   contractile vacuole discharge (GO:0070177) as the process context.

3. **Review p2xA second.** Use the rab8A review template, but verify that
   the PMID:24335649 evidence really supports a tether activity rather than a
   channel-mediated regulatory role. If the evidence is weak,
   MARK_AS_OVER_ANNOTATED rather than mechanically ACCEPTing the migrated
   row.

4. **Use the pair as a coherent batch** — these are the only two annotations
   to the obsoleted term, so completing both closes the loop for the entire
   GO:0140025 → GO:7770067 migration as far as the literature is concerned.

## Priority

**Low–medium.** Only 2 affected annotations, both in a non-priority organism
for this repository (*D. discoideum* has only 3 existing reviews — tlcd4b,
mlcD, nip7), and the upstream migration is likely to be handled directly by
dictyBase. The review value is mainly in (a) anchoring the new GO:7770067
term with a high-quality core_function entry for rab8A, and (b) sanity-checking
the p2xA tether call before it propagates further.

## Status

- 2026-05-31 — Project file created. Tracking upstream issue #6387 (last
  updated 2026-04-22). GO:7770067 has been added (PR #31942) and GO:0140025
  has been obsoleted (PR #31950) per upstream comments by raymond91125;
  dictyBase migration of the two IMP annotations is the remaining upstream
  step. No gene reviews started in this repo yet.
