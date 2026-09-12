---
title: "FAO module vs Reactome mitochondrial β-oxidation"
---

# Cross-check: our FAO module vs the Reactome mitochondrial β-oxidation pathway

[← back to the Fatty Acid β-Oxidation project](../FATTY_ACID_BETA_OXIDATION.md)

Our human gene reviews already **ingest and adjudicate** Reactome at the
annotation level — every human FAO review carries `original_reference_id:
Reactome:R-HSA-…` TAS annotations for the individual chain-length-specific
reactions, each reviewed (ACCEPT / KEEP_AS_NON_CORE). This page is the
**pathway-level** cross-check that was missing: does our cross-species module
([`MODULE:fatty_acid_beta_oxidation`](../../modules/fatty_acid_beta_oxidation.html))
agree with how Reactome models the mitochondrial FAO spiral?

Source: the cached Reactome reaction entries under `reactome/R-HSA-77*.md`
(the `Homo sapiens` mitochondrial β-oxidation reaction set; catalysts read from
each reaction's "mediated by the '…' of '…'" statement).

## Reactome's reaction inventory, by step and chain length

Reactome models the spiral one chain length at a time, with each turn's four
reactions catalysed as follows:

| Chain (acyl-CoA in) | ① dehydrogenase | ② hydratase | ③ 3-OH-acyl-CoA DH | ④ thiolase |
|---------------------|-----------------|-------------|--------------------|------------|
| C16 palmitoyl | **VLCAD** (77299) | MTP (77301) | MTP (77303) | MTP (77304) |
| C14 myristoyl | — | MTP (77277) | MTP (77283) | MTP (77271) |
| C12 lauroyl | — | **ECHS1** (77256) | **HADH** (77254) | MTP (77309) |
| C10 decanoyl | **ACADM** (77345) | **ECHS1** (77344) | **HADH** (77342) | MTP (77340) |
| C8 octanoyl | **ACADM** (77338) | **ECHS1** (77333) | **HADH** (77331) | MTP (77329) |
| C6 hexanoyl | (77327) | **ECHS1** (77325) | **HADH** (77323) | MTP (77321) |
| C4 butanoyl | **ACADS** (77319) | **ECHS1** (77314) | **HADH** (77312) | — |

("MTP" = Reactome's "Trifunctional Protein" complex.)

## Agreements — our module and Reactome match on steps ①–③

- **① Chain-length-specific dehydrogenases.** VLCAD for long (C16), ACADM/MCAD
  for medium (C8/C10), ACADS/SCAD for short (C4) — exactly our module's
  `vlcad`/`mcad`/`scad` variant sets.
- **② + ③ split at the same S/MC ↔ LC boundary.** Reactome routes the hydratase
  and 3-hydroxyacyl-CoA dehydrogenase steps through **ECHS1** and **HADH** for
  C4–C12, and through **MTP** for C14–C16 — the same short/medium-vs-long split
  our module encodes (ECHS1/HADH as the S/MC enzymes; HADHA/MTP as the LC
  enzymes). The boundary (C12 handled by ECHS1/HADH, C14 by MTP) is consistent.
- **The RHEA-chaining gap is a mapping artefact, independently confirmed.** Our
  module flags step ①→② as a break because the enoyl-CoA hydratase MF term
  `GO:0004300` maps only to RHEA:20724 (the (3E) variant), not the canonical
  (2E) crotonase RHEA:16105. Reactome models the same reaction with the correct
  (2E) substrate — e.g. R-HSA-77314 *"Crotonoyl-CoA + H2O ⇒ (S)-3-Hydroxybutanoyl-CoA"* —
  confirming the chemistry is (2E)-enoyl-CoA hydration and the gap lies purely
  in the `GO:0004300 → RHEA` mapping, not the biology.

## Divergence — the thiolase step ④

Reactome attributes the **thiolase step across the entire modelled spiral
(C6→C16) to the "Trifunctional Protein" complex**, and **neither ACAA2 nor
ACAT1 appears in any cited reaction**. Our reviews resolve step ④ more finely:

- **ACAA2** (3-ketoacyl-CoA thiolase, `GO:0003988`) — the medium/long-chain
  straight-chain thiolase of the matrix.
- **ACAT1** (acetoacetyl-CoA thiolase / T2) — the short-chain / ketone-body
  thiolase (the C4 acetoacetyl-CoA step).
- **HADHB / MTP** — the membrane-bound **long-chain** thiolase only.

So Reactome models steps ②–③ with the chain-length-appropriate soluble S/MC
enzymes (ECHS1/HADH) but keeps step ④ on MTP even at C6–C10, over-attributing
the medium/short-chain thiolysis to the trifunctional complex and omitting the
dedicated soluble thiolases. This is a **granularity difference, not an obvious
error** — MTP does carry a thiolase (HADHB) activity — but our per-gene reviews
capture the ACAA2 (M/LC) and ACAT1 (SC/ketone) contributions that this Reactome
pathway does not separate out. Flagged here for curators comparing the two
models.

## Scope note

The cached Reactome set begins at **C16 palmitoyl-CoA** (VLCAD) and does not
model the **very-long-chain** (C17–C22) entry that VLCAD/ACADVL and ACAD9 cover;
our module and the ACAD9/ACADVL reviews (and the ACAD9 `GO:0017099`→`GO:0004466`
chain-length MODIFY) address that end of the range separately.

## Bottom line

The module and Reactome agree on the pathway skeleton and on steps ①–③
(including the same S/MC-vs-LC enzyme split and the honestly-documented RHEA
mapping gap). The one substantive difference is step ④: our reviews resolve the
mitochondrial thiolase into ACAA2 (M/LC) and ACAT1 (SC/ketone), whereas the
Reactome pathway routes the whole thiolase step through the MTP complex.
